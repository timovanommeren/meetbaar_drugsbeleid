"""Combine all sources into one dataset.

Inputs
  data/raw/manual_values.csv   values copied from reports, press releases and NDM chart data (one row per value, with flag and URL)
  data/raw/cbs/cbs_series.json series from the CBS open data API (01_fetch_cbs.py)
  data/raw/mdi/mdi_services.json cocaine incidents per medical service (03_extract_mdi_services.py)
Outputs
  data/processed/cocaine_harm_long.csv  one row per indicator-year, with unit, flag and source URL
  data/processed/cocaine_harm_wide.csv  the single data frame: years 2003-2025 as rows, indicators as columns
"""
import csv, json
from _paths import RAW, PROCESSED

API = "https://opendata.cbs.nl/ODataApi/odata/"
rows = [r for r in csv.DictReader(open(RAW / "manual_values.csv", encoding="utf-8"))]

# --- CBS open data -----------------------------------------------------------
cbs = json.load(open(RAW / "cbs" / "cbs_series.json"))
def cbs_rows(ind, dim, col, unit, key, table, lo=0, hi=9999, flag="exact"):
    for y, v in sorted(cbs[key].items()):
        if v is not None and lo <= int(y) <= hi:
            rows.append(dict(indicator_id=ind, dimension=dim, column=col, unit=unit, year=y, value=v, flag=flag, source_url=API + table))
LSM = "% population (CBS Leefstijlmonitor)"
cbs_rows("H01", "use", "h01_lastyear_use_pct", LSM, "lsm_AfgelopenJaar_45", "85457NED")
cbs_rows("H01", "use", "h01_lastmonth_use_pct", LSM, "lsm_AfgelopenMaand_44", "85457NED")
cbs_rows("H01", "use", "h01_lifetime_use_pct", LSM, "lsm_Ooit_46", "85457NED")
cbs_rows("H08", "use", "h08_deaths_f14_underlying", "deaths (ICD-10 F14 as underlying cause only)", "death_f14", "7233", lo=2005)
cbs_rows("C09", "crime", "c09_harddrug_offences_registered", "offences", "reg_harddrug", "83648NED")
cbs_rows("C09", "crime", "c09_harddrug_offences_registered", "offences", "reg_harddrug_old", "83363NED", hi=2009, flag="exact (older table 83363NED)")
cbs_rows("C09", "crime", "c09_harddrug_suspect_registrations", "registrations", "reg_harddrug_suspects", "83648NED")
cbs_rows("C07", "crime", "c07_murder_victims_total", "victims", "murder_total", "84726NED", lo=2005)
cbs_rows("C07", "crime", "c07_murder_victims_firearm", "victims", "murder_firearm", "84726NED", lo=2005)
VM = "% residents (often in neighbourhood)"
cbs_rows("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED")
cbs_rows("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED")

# --- Monitor Drugsincidenten: cocaine incidents per service --------------------
mdi = json.load(open(RAW / "mdi" / "mdi_services.json"))
M24 = "https://www.trimbos.nl/wp-content/uploads/2026/05/TRI-41-031_Monitor-Drugsincidenten-Jaarrapportage-2024.pdf"
M23 = "https://www.trimbos.nl/wp-content/uploads/2025/04/MDI-jaarrapportage-2023.pdf"
F24 = "derived (MDI 2024 report fig. 3.2: share by service x total, read from vector chart)"
F19 = "derived (2019: cocaine share per service, rounded %, x service total N from MDI 2023 report)"
# 2019: cocaine share per service (NDM chart) x total drug incidents per service (MDI 2023 report, fig. 3.2)
d19 = {"ambulance": round(1591 * .15), "ehbo": round(2067 * .10), "forensic": round(523 * .22),
       "mdi_hospital": round(1477 * .22), "lis_hospital": round(1052 * .19)}
services = {"mdi_hospital": "h06_incidents_mdi_hospitals_n", "lis_hospital": "h06_incidents_lis_hospitals_n",
            "ambulance": "h06_incidents_ambulance_n", "ehbo": "h06_incidents_first_aid_events_n",
            "forensic": "h06_incidents_forensic_doctors_n"}
def add(col, unit, y, v, flag, url):
    rows.append(dict(indicator_id="H06", dimension="use", column=col, unit=unit, year=y, value=v, flag=flag, source_url=url))
for k, col in services.items():
    add(col, "cocaine incidents", 2019, d19[k], F19, M23)
    for y, v in sorted(mdi.items()): add(col, "cocaine incidents", int(y), v[k][1], F24, M24)
ED = "cocaine incidents (MDI + LIS hospital EDs)"
add("h06_incidents_hospital_ed_n", ED, 2019, d19["mdi_hospital"] + d19["lis_hospital"], F19, M23)
for y, v in sorted(mdi.items()): add("h06_incidents_hospital_ed_n", ED, int(y), v["mdi_hospital"][1] + v["lis_hospital"][1], F24, M24)

# --- write -------------------------------------------------------------------
num = lambda v: float(v)
fields = ["indicator_id", "dimension", "column", "unit", "year", "value", "flag", "source_url"]
rows.sort(key=lambda r: (r["column"], int(r["year"])))
PROCESSED.mkdir(parents=True, exist_ok=True)
with open(PROCESSED / "cocaine_harm_long.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)
cols = sorted({r["column"] for r in rows})
grid = {(r["column"], int(r["year"])): r["value"] for r in rows}
with open(PROCESSED / "cocaine_harm_wide.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["year"] + cols)
    for y in range(2003, 2026): w.writerow([y] + [grid.get((c, y), "") for c in cols])
print(f"{len(rows)} values, {len(cols)} indicator columns")
