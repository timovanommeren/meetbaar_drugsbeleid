"""(Cocaine only.) Derive cocaine incidents per medical service from the Monitor Drugsincidenten 2024 report.

Figure 3.2 (page 43) is a stacked bar chart of cocaine incidents by service, 2020-2024.
Bar segments are read from the PDF's vector drawing commands and multiplied by the
yearly totals printed above the bars. Writes data/raw/cocaine/mdi/mdi_services.json:
{year: {service: [share_pct, count], 'total': n}}.
"""
import json, urllib.request
import pymupdf
from _paths import RAW

URL = "https://www.trimbos.nl/wp-content/uploads/2026/05/TRI-41-031_Monitor-Drugsincidenten-Jaarrapportage-2024.pdf"
pdf = RAW / "cocaine" / "mdi" / "MDI-jaarrapportage-2024.pdf"
pdf.parent.mkdir(parents=True, exist_ok=True)
if not pdf.exists():
    pdf.write_bytes(urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read())

COLOURS = {(0.973, 0.463, 0.427): "ambulance", (0.639, 0.647, 0.0): "ehbo", (0.0, 0.749, 0.49): "forensic",
           (0.0, 0.69, 0.965): "mdi_hospital", (0.906, 0.42, 0.953): "lis_hospital"}
BAR_X = [94.5, 119.4, 144.2, 169.1, 194.0]          # panel A: all cocaine incidents
TOTALS = {2020: 696, 2021: 708, 2022: 996, 2023: 1119, 2024: 916}

page = pymupdf.open(pdf)[42]
segs = [(round(d["rect"].x0, 1), d["rect"].height, tuple(round(c, 3) for c in d["fill"]))
        for d in page.get_drawings() if d.get("fill") and 20 < d["rect"].width < 30]
out = {}
for x, (year, total) in zip(BAR_X, TOTALS.items()):
    h = {COLOURS[c]: ht for x0, ht, c in segs if abs(x0 - x) < 0.5 and c in COLOURS}
    H = sum(h.values())
    out[year] = {k: (round(v / H * 100, 1), round(v / H * total)) for k, v in h.items()}
    out[year]["total"] = total
json.dump(out, open(RAW / "cocaine" / "mdi" / "mdi_services.json", "w"))
for y, v in out.items(): print(y, v)
