"""Per-drug plot configuration: which indicators appear in which panel (05) and matrix (06).

PANELS[drug][dimension] = [(panel title, [(column, series label or None), ...], y-axis unit), ...]
CORR[drug][dimension]   = [(column, matrix label), ...]
TEXT[drug]              = figure subtitles and footnote source line
"""
# ---- cocaine -----------------------------------------------------------------
_coc_crime=[("Hard-drug offences registered",[("c09_harddrug_offences_registered",None)],"offences"),
("Hard-drug suspect registrations",[("c09_harddrug_suspect_registrations",None)],"registrations"),
("Murder victims",[("c07_murder_victims_total","total"),("c07_murder_victims_firearm","by firearm")],"victims"),
("Criminal-milieu murders and liquidations",[("c05_murders_criminal_milieu","criminal milieu"),("c06_liquidations","liquidations")],"cases"),
("Attacks with explosives",[("c08_explosive_attacks",None)],"attacks"),
("Uithalers apprehended",[("c03_uithalers_apprehended",None)],"persons"),
("Cocaine seized",[("c01_seized_douane_total_kg","Douane total"),("c01_seized_douane_maritime_kg","Douane maritime"),("c01_seized_harc_rotterdam_kg","HARC Rotterdam")],"kg"),
("Douane seizures, number (all)",[("c01_seizures_douane_total_n",None)],"seizures"),
("Douane seizures, number (maritime)",[("c01_seizures_douane_maritime_n",None)],"seizures"),
("OM investigations, organised drug crime",[("c10_investigations_org_drug_crime","all drugs"),("c10_investigations_cocaine_heroin","cocaine & heroin")],"investigations"),
("Retail price",[("c18_retail_price_eur_g",None)],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents"),
("Cocaine seized at Schiphol",[("c01_seized_schiphol_kg",None)],"kg"),
("Cocaine labs dismantled",[("c20_cocaine_labs_dismantled",None)],"sites"),
("Payment-code fraud at terminals",[("c19_paymentcode_fraud",None)],"cases"),
("Organized Crime Index, cocaine trade",[("c14_ocindex_cocaine_trade",None)],"score (1–10)")]
_coc_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, all ages"),("h01b_lastyear_use_18plus_ndm_pct","NDM, 18+")],"% of population"),
("Last-month use (CBS)",[("h01_lastmonth_use_pct",None)],"% of population"),
("Lifetime use (CBS)",[("h01_lifetime_use_pct",None)],"% of population"),
("Lifetime use, pupils 12–16",[("h03_lifetime_use_pupils_pct",None)],"% of pupils"),
("Treatment, cocaine primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, cocaine secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Deaths involving cocaine",[("h08_deaths_cocaine","NDM definition"),("h08_deaths_f14_underlying","F14 underlying cause")],"deaths"),
("Hospital admissions, cocaine main diagnosis",[("h09_hospital_main_dx",None)],"admissions"),
("Hospital admissions, cocaine secondary diagnosis",[("h09_hospital_secondary_dx",None)],"admissions"),
("Cocaine share of drug incidents",[("h06_mdi_share_mdi_hospitals_pct","MDI hospitals"),("h06_mdi_incidents_share_pct","all services"),("h06_mdi_share_ambulance_pct","ambulance")],"% of incidents"),
("Cocaine in wastewater",[("h11_wastewater_amsterdam","Amsterdam"),("h11_wastewater_eindhoven","Eindhoven"),("h11_wastewater_utrecht","Utrecht")],"mg/1,000 inh./day"),
("Purity",[("h12_purity_dims_pct","DIMS samples"),("h17_purity_nfi_pct","NFI police seizures")],"% cocaine"),
("Adulterated samples (DIMS)",[("h12_adulterated_share_pct","any cutting agent"),("h12_levamisole_share_pct","levamisole")],"% of samples"),
("Last-year use, nightlife-goers",[("h04_lastyear_use_nightlife_pct",None)],"% of nightlife-goers"),
("Treatment per 100,000 inhabitants",[("h05_treatment_per100k_constant",None)],"clients (constant inst.)")]
_coc_crime_corr=[("c09_harddrug_offences_registered","Hard-drug offences"),("c09_harddrug_suspect_registrations","Hard-drug suspects"),
("c07_murder_victims_total","Murder victims, total"),("c07_murder_victims_firearm","Murder victims, firearm"),
("c05_murders_criminal_milieu","Criminal-milieu murders"),("c06_liquidations","Liquidations"),("c08_explosive_attacks","Explosive attacks"),
("c03_uithalers_apprehended","Uithalers"),("c01_seized_douane_total_kg","Seized, Douane total kg"),("c01_seized_douane_maritime_kg","Seized, Douane maritime kg"),
("c01_seized_harc_rotterdam_kg","Seized, HARC Rotterdam kg"),("c01_seizures_douane_total_n","Seizures, Douane total n"),("c01_seizures_douane_maritime_n","Seizures, Douane maritime n"),
("c10_investigations_org_drug_crime","OM investigations, all drugs"),("c10_investigations_cocaine_heroin","OM investigations, coc./her."),("c18_retail_price_eur_g","Retail price")]
_coc_use_corr=[("h01_lastyear_use_pct","Last-year use (CBS)"),("h01b_lastyear_use_18plus_ndm_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),("h05_treatment_secondary_all","Treatment secondary, all"),("h05_treatment_secondary_constant","Treatment secondary, constant"),
("h08_deaths_cocaine","Deaths (NDM)"),("h08_deaths_f14_underlying","Deaths (F14 underlying)"),("h09_hospital_main_dx","Hospital, main dx"),("h09_hospital_secondary_dx","Hospital, secondary dx"),
("h06_mdi_incidents_share_pct","Incident share, all services"),("h06_mdi_share_mdi_hospitals_pct","Incident share, MDI hospitals"),("h06_mdi_share_ambulance_pct","Incident share, ambulance"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),
("h12_purity_dims_pct","Purity (DIMS)"),("h12_adulterated_share_pct","Adulterated share"),("h12_levamisole_share_pct","Levamisole share")]

# ---- cannabis ----------------------------------------------------------------
_can_crime=[("Soft-drug offences registered",[("c09_softdrug_offences_registered",None)],"offences"),
("Soft-drug suspect registrations",[("c09_softdrug_suspect_registrations",None)],"registrations"),
("Soft-drug incidents (police, NDM)",[("c09b_softdrug_incidents_police",None)],"incidents"),
("Cannabis farms dismantled",[("c20_cannabis_farms_dismantled",None)],"farms"),
("OM investigations, large-scale cultivation",[("c10_investigations_cannabis_cultivation",None)],"investigations"),
("Cannabis seized by Douane (kg)",[("c01_seized_douane_weed_kg","marijuana"),("c01_seized_douane_hash_kg","hashish")],"kg"),
("Cannabis seizures by Douane (number)",[("c01_seizures_douane_weed_n","marijuana"),("c01_seizures_douane_hash_n","hashish")],"seizures"),
("Coffeeshops",[("c21_coffeeshops_n",None)],"coffeeshops"),
("Coffeeshop price, weed",[("c18_price_nederwiet_eur_g","nederwiet"),("c18_price_imported_weed_eur_g","imported")],"€ per gram"),
("Coffeeshop price, hashish",[("c18_price_nederhasj_eur_g","nederhasj"),("c18_price_imported_hash_eur_g","imported")],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents")]
_can_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, all ages"),("h01_lastyear_use_18plus_pct","NDM, 18+")],"% of population"),
("Last-month use",[("h01_lastmonth_use_pct","CBS, all ages"),("h01_lastmonth_use_18plus_pct","NDM, 18+")],"% of population"),
("(Almost) daily use, adults",[("h01_daily_use_18plus_pct",None)],"% 18+"),
("Lifetime use",[("h01_lifetime_use_pct","CBS, all ages"),("h01_lifetime_use_18plus_pct","NDM, 18+")],"% of population"),
("Use among pupils 12–16",[("h03_lifetime_use_pupils_pct","lifetime"),("h03_lastyear_use_pupils_pct","last year"),("h03_lastmonth_use_pupils_pct","last month")],"% of pupils"),
("Use among 15–16-year-olds (ESPAD)",[("h03_lifetime_use_espad16_pct","lifetime"),("h03_lastmonth_use_espad16_pct","last month")],"% of pupils"),
("Use among mbo students",[("h04_lifetime_use_mbo_pct","lifetime"),("h04_lastmonth_use_mbo_pct","last month")],"% of students"),
("Elevated risk of cannabis use disorder (CAST)",[("h02_cast_risk_users_pct",None)],"% of last-year users"),
("Treatment, cannabis primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, cannabis secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Hospital admissions, main diagnosis",[("h09_hospital_main_dx",None)],"admissions"),
("Hospital admissions, secondary diagnosis",[("h09_hospital_secondary_dx",None)],"admissions"),
("Cannabis share of drug incidents",[("h06_mdi_share_mdi_hospitals_pct","MDI hospitals"),("h06_mdi_share_lis_hospitals_pct","LIS hospitals"),("h06_mdi_share_ambulance_pct","ambulance")],"% of incidents"),
("Cannabis in wastewater",[("h11_wastewater_amsterdam","Amsterdam"),("h11_wastewater_eindhoven","Eindhoven"),("h11_wastewater_utrecht","Utrecht")],"mg THC-COOH/1,000 inh./day"),
("THC content, weed",[("h12_thc_nederwiet_pct","nederwiet"),("h12_thc_imported_weed_pct","imported")],"% THC"),
("THC content, hashish",[("h12_thc_nederhasj_pct","nederhasj"),("h12_thc_imported_hash_pct","imported")],"% THC")]
_can_crime_corr=[("c09_softdrug_offences_registered","Soft-drug offences"),("c09_softdrug_suspect_registrations","Soft-drug suspects"),("c09b_softdrug_incidents_police","Soft-drug incidents (police)"),
("c20_cannabis_farms_dismantled","Cannabis farms dismantled"),("c10_investigations_cannabis_cultivation","OM investigations, cultivation"),
("c01_seized_douane_weed_kg","Seized, marijuana kg"),("c01_seized_douane_hash_kg","Seized, hashish kg"),("c01_seizures_douane_weed_n","Seizures, marijuana n"),("c01_seizures_douane_hash_n","Seizures, hashish n"),
("c21_coffeeshops_n","Coffeeshops"),("c18_price_nederwiet_eur_g","Price, nederwiet"),("c18_price_imported_weed_eur_g","Price, imported weed"),("c18_price_nederhasj_eur_g","Price, nederhasj"),("c18_price_imported_hash_eur_g","Price, imported hash")]
_can_use_corr=[("h01_lastyear_use_pct","Last-year use (CBS)"),("h01_lastyear_use_18plus_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_daily_use_18plus_pct","Daily use 18+"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h03_lastyear_use_pupils_pct","Pupils, last year"),("h03_lastmonth_use_espad16_pct","ESPAD 15–16, last month"),("h04_lastmonth_use_mbo_pct","mbo students, last month"),("h02_cast_risk_users_pct","CAST risk among users"),
("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),("h05_treatment_secondary_all","Treatment secondary, all"),("h05_treatment_secondary_constant","Treatment secondary, constant"),
("h09_hospital_main_dx","Hospital, main dx"),("h09_hospital_secondary_dx","Hospital, secondary dx"),
("h06_mdi_share_mdi_hospitals_pct","Incident share, MDI hospitals"),("h06_mdi_share_lis_hospitals_pct","Incident share, LIS hospitals"),("h06_mdi_share_ambulance_pct","Incident share, ambulance"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),
("h12_thc_nederwiet_pct","THC, nederwiet"),("h12_thc_imported_weed_pct","THC, imported weed"),("h12_thc_nederhasj_pct","THC, nederhasj"),("h12_thc_imported_hash_pct","THC, imported hash")]

PANELS={"cocaine":{"crime":_coc_crime,"use":_coc_use},"cannabis":{"crime":_can_crime,"use":_can_use}}
CORR={"cocaine":{"crime":_coc_crime_corr,"use":_coc_use_corr},"cannabis":{"crime":_can_crime_corr,"use":_can_use_corr}}
TEXT={
 "cocaine":{"crime_sub":"Enforcement, violence, recruitment, trade and market indicators, 2003–2025",
            "use_sub":"Prevalence, treatment, acute harm, mortality, consumption and product risk, 2003–2025",
            "sources":"CBS, Nationale Drug Monitor, Politie, OM, GI-TOC","first":2003,
            "note":", or (treatment 2006, 2015) an older report with a different institution base"},
 "cannabis":{"crime_sub":"Enforcement, cultivation, trade, coffeeshop market and nuisance indicators, 1999–2025",
             "use_sub":"Prevalence, problematic use, treatment, acute harm, consumption and product potency, 1999–2025",
             "sources":"CBS, Nationale Drug Monitor (Trimbos, LADIS, Politie, Douane, OM)","first":1999,"note":""}}
