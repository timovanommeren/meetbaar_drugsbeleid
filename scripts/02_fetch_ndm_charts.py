"""Download the chart data behind the Nationale Drug Monitor's cocaine pages.

The NDM website draws its charts with everviz; each chart's data table is fetched
from app.everviz.com. Writes data/raw/ndm_charts/ndm_cocaine_charts.json:
{chart_id: {page, title, caption, table}}. Values in data/raw/manual_values.csv
flagged 'NDM chart data' were taken from these tables.
"""
import html, json, re, urllib.request
from _paths import RAW

NDM = "https://www.nationaledrugmonitor.nl/"
PAGES = [f"cocaine-{p}" for p in ["aanbod-en-markt", "algemene-ziekenhuizen", "gebruik-algemene-bevolking",
         "hulpvraag-en-incidenten", "incidenten", "prijzen", "problematisch-gebruik", "sterfte",
         "ziekte-en-sterfte", "gebruik-jongeren-en-jongvolwassenen", "uitgaande-jongeren-en-jongvolwassenen",
         "scholieren-veranderingen-gebruik", "gebruik-internationale-vergelijking", "laatste-feiten-en-trends"]]
PAGES += [f"illegale-handel-bezit-en-productie-{p}" for p in ["liquidaties", "georganiseerde-misdaad-en-drugshandel",
          "inbeslagnames-van-drugs-en-ontmantelingen-van-productielocaties"]]
UA = {"User-Agent": "Mozilla/5.0"}
fetch = lambda url: urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read().decode("utf-8")
clean = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).strip() if isinstance(s, str) else s

charts = {}
for page in PAGES:
    try: src = fetch(NDM + page + "/")
    except Exception as e: print("skip", page, e); continue
    for cid in re.findall(r"app\.everviz\.com/inject/([A-Za-z0-9_-]+)", src):
        charts.setdefault(cid, page)

out = {}
for cid, page in charts.items():
    js = fetch(f"https://app.everviz.com/inject/{cid}/")
    m = re.search(r"var options = (\{.*?\});\s*\n", js, re.S)
    if not m: continue
    try: o = json.loads(m.group(1))
    except json.JSONDecodeError: continue
    data, opt = o.get("data") or {}, o.get("options") or {}
    if not isinstance(data, dict): data = {"value": data}
    if not isinstance(opt, dict): opt = {}
    title = clean(((opt.get("title") or {}).get("text")) or "")
    caption = clean(((opt.get("caption") or {}).get("text")) or "")
    table = data.get("value") or [r.split(";") for r in (data.get("csv") or "").split("\n")]
    out[cid] = {"page": NDM + page + "/", "title": title, "caption": caption,
                "table": [[clean(c) for c in row] if isinstance(row, list) else row for row in table]}

(RAW / "ndm_charts").mkdir(parents=True, exist_ok=True)
json.dump(out, open(RAW / "ndm_charts" / "ndm_cocaine_charts.json", "w"), ensure_ascii=False, indent=0)
print("saved", len(out), "charts")
