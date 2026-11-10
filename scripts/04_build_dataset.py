"""Combine all sources for one drug into one dataset.

Usage: python scripts/04_build_dataset.py cocaine|cannabis|mdma|amphetamine|heroin

Inputs
  data/raw/<drug>/manual_values.csv  values copied from reports, press releases and NDM chart data
                                      (one row per value, with flag and source URL)
  data/raw/cbs/cbs_series.json       series from the CBS open data API (01_fetch_cbs.py)
  data/raw/cocaine/mdi/mdi_services.json  cocaine incidents per medical service (03_extract_mdi_services.py)
Outputs
  data/processed/<drug>_harm_long.csv  one row per indicator-year, with unit, flag and source URL
  data/processed/<drug>_harm_wide.csv  the data frame: years as rows, indicators as columns
"""
import csv, json, sys
from _paths import RAW, PROCESSED

DRUG = sys.argv[1] if len(sys.argv) > 1 else "cocaine"
API = "https://opendata.cbs.nl/ODataApi/odata/"
FIRST_YEAR = {"cocaine": 2003, "cannabis": 1999, "mdma": 2003, "amphetamine": 2003, "heroin": 2003}[DRUG]
rows = list(csv.DictReader(open(RAW / DRUG / "manual_values.csv", encoding="utf-8")))

# --- CBS open data -----------------------------------------------------------
# (indicator, dimension, column, unit, series key in cbs_series.json, table, first year, last year, flag)
LSM = "% population 12+ (CBS Leefstijlmonitor)"
VM = "% residents (often in neighbourhood)"
CBS = {
    "cocaine": [
        ("H01", "use", "h01_lastyear_use_pct", LSM, "lsm_AfgelopenJaar_45", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lastmonth_use_pct", LSM, "lsm_AfgelopenMaand_44", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lifetime_use_pct", LSM, "lsm_Ooit_46", "85457NED", 0, 9999, "exact"),
        ("H08", "use", "h08_deaths_f14_underlying", "deaths (ICD-10 F14 as underlying cause only)", "death_f14", "7233", 2005, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences", "reg_harddrug", "83648NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences", "reg_harddrug_old", "83363NED", 0, 2009, "exact (older table 83363NED)"),
        ("C09", "crime", "c09_harddrug_suspect_registrations", "registrations", "reg_harddrug_suspects", "83648NED", 0, 9999, "exact"),
        ("C07", "crime", "c07_murder_victims_total", "victims", "murder_total", "84726NED", 2005, 9999, "exact"),
        ("C07", "crime", "c07_murder_victims_firearm", "victims", "murder_firearm", "84726NED", 2005, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED", 0, 9999, "exact"),
    ],
    "cannabis": [
        ("H01", "use", "h01_lastyear_use_pct", LSM, "lsm_AfgelopenJaar_30", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lastmonth_use_pct", LSM, "lsm_AfgelopenMaand_29", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lifetime_use_pct", LSM, "lsm_Ooit_31", "85457NED", 0, 9999, "exact"),
        ("H08", "use", "h08_deaths_f12_underlying", "deaths (ICD-10 F12 as underlying cause)", "death_f12", "7233", 2005, 9999, "exact"),
        ("C09", "crime", "c09_softdrug_offences_registered", "offences", "reg_softdrug", "83648NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_softdrug_offences_registered", "offences", "reg_softdrug_old", "83363NED", 0, 2009, "exact (older table 83363NED)"),
        ("C09", "crime", "c09_softdrug_suspect_registrations", "registrations", "reg_softdrug_suspects", "83648NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED", 0, 9999, "exact"),
    ],
    "mdma": [
        ("H01", "use", "h01_lastyear_use_pct", LSM, "lsm_AfgelopenJaar_42", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lastmonth_use_pct", LSM, "lsm_AfgelopenMaand_41", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lifetime_use_pct", LSM, "lsm_Ooit_43", "85457NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not MDMA-specific)", "reg_harddrug", "83648NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not MDMA-specific)", "reg_harddrug_old", "83363NED", 0, 2009, "exact (older table 83363NED)"),
        ("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED", 0, 9999, "exact"),
    ],
    "amphetamine": [
        ("H01", "use", "h01_lastyear_use_pct", LSM, "lsm_AfgelopenJaar_39", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lastmonth_use_pct", LSM, "lsm_AfgelopenMaand_38", "85457NED", 0, 9999, "exact"),
        ("H01", "use", "h01_lifetime_use_pct", LSM, "lsm_Ooit_40", "85457NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not amphetamine-specific)", "reg_harddrug", "83648NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not amphetamine-specific)", "reg_harddrug_old", "83363NED", 0, 2009, "exact (older table 83363NED)"),
        ("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED", 0, 9999, "exact"),
    ],
    "heroin": [
        ("H08", "use", "h08_deaths_f11_underlying", "deaths (ICD-10 F11 as underlying cause)", "death_f11", "7233", 2005, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not heroin-specific)", "reg_harddrug", "83648NED", 0, 9999, "exact"),
        ("C09", "crime", "c09_harddrug_offences_registered", "offences (all list I drugs, not heroin-specific)", "reg_harddrug_old", "83363NED", 0, 2009, "exact (older table 83363NED)"),
        ("C16", "crime", "c16_nuisance_drug_use_pct", VM, "vm_druguse_nuis", "85146NED", 0, 9999, "exact"),
        ("C16", "crime", "c16_nuisance_drug_dealing_pct", VM, "vm_drugdeal_nuis", "85146NED", 0, 9999, "exact"),
    ],
}
cbs = json.load(open(RAW / "cbs" / "cbs_series.json"))
for ind, dim, col, unit, key, table, lo, hi, flag in CBS[DRUG]:
    for y, v in sorted(cbs[key].items()):
        if v is not None and lo <= int(y) <= hi:
            rows.append(dict(indicator_id=ind, dimension=dim, column=col, unit=unit, year=y, value=v, flag=flag, source_url=API + table))

# --- Cocaine only: Monitor Drugsincidenten, cocaine incidents per service --------
if DRUG == "cocaine":
    mdi = json.load(open(RAW / "cocaine" / "mdi" / "mdi_services.json"))
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
fields = ["indicator_id", "dimension", "column", "unit", "year", "value", "flag", "source_url"]
rows.sort(key=lambda r: (r["column"], int(r["year"])))
PROCESSED.mkdir(parents=True, exist_ok=True)
with open(PROCESSED / f"{DRUG}_harm_long.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)
cols = sorted({r["column"] for r in rows})
grid = {(r["column"], int(r["year"])): r["value"] for r in rows}
with open(PROCESSED / f"{DRUG}_harm_wide.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["year"] + cols)
    for y in range(FIRST_YEAR, 2026): w.writerow([y] + [grid.get((c, y), "") for c in cols])
print(f"{DRUG}: {len(rows)} values, {len(cols)} indicator columns")
