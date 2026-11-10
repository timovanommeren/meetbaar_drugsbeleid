"""Download cocaine, cannabis, ecstasy and drug-crime series from the CBS open data API (StatLine).

Writes data/raw/cbs/cbs_series.json: {series_name: {year: value}}.
Tables: 85457NED (Leefstijlmonitor), 7233 (deaths by cause), 83648NED/83363NED
(registered crime), 84726NED (murder victims), 85146NED (Veiligheidsmonitor).
"""
import json, urllib.parse, urllib.request
from _paths import RAW

API = "https://opendata.cbs.nl/ODataApi/odata/"

def get(table, flt=None, sel=None):
    q = {"$format": "json"}
    if flt: q["$filter"] = flt
    if sel: q["$select"] = sel
    with urllib.request.urlopen(API + table + "?" + urllib.parse.urlencode(q), timeout=120) as r:
        return json.load(r)["value"]

by_year = lambda rows, key: {r["Perioden"][:4]: r[key] for r in rows}
out = {}

# Leefstijlmonitor: cocaine, cannabis, ecstasy and amphetamine use (total population, point estimate)
dp = get("85457NED/DataProperties")
rows = get("85457NED/TypedDataSet", "Persoonskenmerken eq 'T009002' and Marges eq 'MW00000'")
for title in ("Cocaïnegebruik", "Cannabisgebruik", "Ecstasygebruik", "Amfetaminegebruik"):
    group = next(x["ID"] for x in dp if x.get("Title") == title)
    for x in dp:
        if x.get("ParentID") == group:
            out["lsm_" + x["Key"]] = by_year(rows, x["Key"])

# Deaths by underlying cause (ICD-10 F14 = mental/behavioural disorders due to cocaine)
# (F12 = cannabinoids, F11 = opioids)
for code, name in (("A011101", "death_f14"), ("A011099", "death_f12"), ("A011098", "death_f11")):
    rows = get("7233/TypedDataSet", f"DoodsoorzakenUitgebreideLijst eq '{code}' and Geslacht eq 'T001038' and Leeftijd eq '10000'")
    val = [k for k in rows[0] if k not in ("ID", "Geslacht", "Leeftijd", "DoodsoorzakenUitgebreideLijst", "Perioden")][0]
    out[name] = by_year(rows, val)

# Registered hard-drug (Opiumwet list I) and soft-drug (list II) offences and suspect registrations
for kind, new, old in (("harddrug", "CRI6100", "6010000"), ("softdrug", "CRI6200", "6020000")):
    rows = get("83648NED/TypedDataSet", f"SoortMisdrijf eq '{new}' and RegioS eq 'NL01  '")
    out[f"reg_{kind}"] = by_year(rows, "TotaalGeregistreerdeMisdrijven_1")
    out[f"reg_{kind}_suspects"] = by_year(rows, "RegistratiesVanVerdachten_6")
    rows = get("83363NED/TypedDataSet", f"SoortMisdrijf eq '{old}' and RegioS eq 'NL01  '")
    val = [k for k in rows[0] if k.startswith(("TotaalGeregistreerde", "GeregistreerdeMisdrijven"))][0]
    out[f"reg_{kind}_old"] = by_year(rows, val)

# Murder victims: total and by firearm
rows = get("84726NED/TypedDataSet", "Geslacht eq 'T001038'")
val = [k for k in rows[0] if k not in ("ID", "Geslacht", "Kenmerken", "Perioden")][0]
out["murder_total"] = by_year([r for r in rows if r["Kenmerken"].strip() == "10000"], val)
out["murder_firearm"] = by_year([r for r in rows if r["Kenmerken"].strip() == "A048759"], val)

# Veiligheidsmonitor: drug use / drug dealing seen often in own neighbourhood
rows = get("85146NED/TypedDataSet", "RegioS eq 'NL01   '", "Marges,Perioden,Drugsgebruik_29,Drugshandel_30")
rows = [r for r in rows if r["Marges"].strip() == "MW00000"]
out["vm_druguse_nuis"] = by_year(rows, "Drugsgebruik_29")
out["vm_drugdeal_nuis"] = by_year(rows, "Drugshandel_30")

(RAW / "cbs").mkdir(parents=True, exist_ok=True)
json.dump(out, open(RAW / "cbs" / "cbs_series.json", "w"), indent=1)
print("saved", len(out), "CBS series")
