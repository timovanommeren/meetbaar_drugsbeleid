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
_coc_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, 12+"),("h01b_lastyear_use_18plus_ndm_pct","NDM, 18+")],"% of population"),
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
_coc_use_corr=[("h01_lastyear_use_pct","Last-year use 12+ (CBS)"),("h01b_lastyear_use_18plus_ndm_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
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
("Cannabis supply-chain sites",[("c20_cannabis_cutting_drying_sites","cutting/drying sites"),("c21_growshops_closed","growshops closed")],"sites"),
("OM investigations, large-scale cultivation",[("c10_investigations_cannabis_cultivation",None)],"investigations"),
("Cannabis seized by Douane (kg)",[("c01_seized_douane_weed_kg","marijuana"),("c01_seized_douane_hash_kg","hashish")],"kg"),
("Cannabis seizures by Douane (number)",[("c01_seizures_douane_weed_n","marijuana"),("c01_seizures_douane_hash_n","hashish")],"seizures"),
("Coffeeshops",[("c21_coffeeshops_n",None)],"coffeeshops"),
("Coffeeshop price, weed",[("c18_price_nederwiet_eur_g","nederwiet"),("c18_price_imported_weed_eur_g","imported")],"€ per gram"),
("Coffeeshop price, hashish",[("c18_price_nederhasj_eur_g","nederhasj"),("c18_price_imported_hash_eur_g","imported")],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents")]
_can_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, 12+"),("h01_lastyear_use_18plus_pct","NDM, 18+")],"% of population"),
("Last-month use",[("h01_lastmonth_use_pct","CBS, 12+"),("h01_lastmonth_use_18plus_pct","NDM, 18+")],"% of population"),
("(Almost) daily use, adults",[("h01_daily_use_18plus_pct",None)],"% 18+"),
("Lifetime use",[("h01_lifetime_use_pct","CBS, 12+"),("h01_lifetime_use_18plus_pct","NDM, 18+")],"% of population"),
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
_can_use_corr=[("h01_lastyear_use_pct","Last-year use 12+ (CBS)"),("h01_lastyear_use_18plus_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_daily_use_18plus_pct","Daily use 18+"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h03_lastyear_use_pupils_pct","Pupils, last year"),("h03_lastmonth_use_espad16_pct","ESPAD 15–16, last month"),("h04_lastmonth_use_mbo_pct","mbo students, last month"),("h02_cast_risk_users_pct","CAST risk among users"),
("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),("h05_treatment_secondary_all","Treatment secondary, all"),("h05_treatment_secondary_constant","Treatment secondary, constant"),
("h09_hospital_main_dx","Hospital, main dx"),("h09_hospital_secondary_dx","Hospital, secondary dx"),
("h06_mdi_share_mdi_hospitals_pct","Incident share, MDI hospitals"),("h06_mdi_share_lis_hospitals_pct","Incident share, LIS hospitals"),("h06_mdi_share_ambulance_pct","Incident share, ambulance"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),
("h12_thc_nederwiet_pct","THC, nederwiet"),("h12_thc_imported_weed_pct","THC, imported weed"),("h12_thc_nederhasj_pct","THC, nederhasj"),("h12_thc_imported_hash_pct","THC, imported hash")]

# ---- MDMA (ecstasy) ----------------------------------------------------------
_mdma_crime=[("Synthetic-drug production sites dismantled",[("c20_synthetic_production_sites","production"),("c20_synthetic_storage_sites","storage")],"sites"),
("MDMA labs dismantled",[("c20_mdma_labs_dismantled",None)],"labs"),
("Dumpings of drug waste",[("c22_drug_waste_dumpings",None)],"dumpings"),
("OM investigations, synthetic drugs",[("c10_investigations_synthetic_drugs",None)],"investigations"),
("Pre-precursors seized",[("c23_precursors_all_kg","all synthetic drugs"),("c23_precursors_pmk_kg","PMK-type (MDMA)")],"kg"),
("Ecstasy seized by Douane (kg)",[("c01_seized_douane_ecstasy_kg",None)],"kg"),
("Ecstasy seizures by Douane (number)",[("c01_seizures_douane_ecstasy_n",None)],"seizures"),
("Hard-drug offences registered (all list I)",[("c09_harddrug_offences_registered",None)],"offences"),
("Price per ecstasy pill",[("c18_price_pill_eur",None)],"€ per pill"),
("Price of MDMA powder",[("c18_price_powder_eur_g",None)],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents")]
_mdma_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, 12+"),("h01_lastyear_use_18plus_pct","NDM, 18+")],"% of population"),
("Last-month use",[("h01_lastmonth_use_pct","CBS, 12+"),("h01_lastmonth_use_18plus_pct","NDM, 18+")],"% of population"),
("Lifetime use",[("h01_lifetime_use_pct","CBS, 12+"),("h01_lifetime_use_18plus_pct","NDM, 18+")],"% of population"),
("Use among pupils 12–16 and mbo students",[("h03_lifetime_use_pupils_pct","pupils, lifetime"),("h04_lifetime_use_mbo_pct","mbo, lifetime"),("h04_lastmonth_use_mbo_pct","mbo, last month")],"% of pupils/students"),
("Treatment, ecstasy primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, ecstasy secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Drug incidents involving ecstasy (MDI)",[("h06_mdi_incidents_share_pct",None)],"% of drug incidents"),
("Deaths from psychostimulants",[("h08_deaths_psychostimulants",None)],"deaths (incl. amphetamine)"),
("MDMA in wastewater",[("h11_wastewater_amsterdam","Amsterdam"),("h11_wastewater_eindhoven","Eindhoven"),("h11_wastewater_utrecht","Utrecht")],"mg/1,000 inh./day"),
("MDMA per ecstasy pill",[("h12_mdma_per_pill_mg",None)],"mg (mean, DIMS)"),
("High-dose pills",[("h12_pills_over_140mg_pct",">140 mg"),("h12_pills_over_210mg_pct",">210 mg")],"% of pills tested"),
("MDMA powder purity",[("h12_mdma_powder_purity_pct",None)],"% MDMA")]
_mdma_crime_corr=[("c20_synthetic_production_sites","Production sites"),("c20_synthetic_storage_sites","Storage sites"),("c22_drug_waste_dumpings","Drug waste dumpings"),
("c10_investigations_synthetic_drugs","OM investigations, synthetic"),("c23_precursors_all_kg","Pre-precursors, all kg"),("c23_precursors_pmk_kg","Pre-precursors, PMK kg"),
("c01_seized_douane_ecstasy_kg","Seized, ecstasy kg"),("c01_seizures_douane_ecstasy_n","Seizures, ecstasy n"),("c09_harddrug_offences_registered","Hard-drug offences"),
("c18_price_pill_eur","Price per pill"),("c18_price_powder_eur_g","Price, MDMA powder")]
_mdma_use_corr=[("h01_lastyear_use_pct","Last-year use 12+ (CBS)"),("h01_lastyear_use_18plus_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h04_lastmonth_use_mbo_pct","mbo students, last month"),("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),
("h05_treatment_secondary_all","Treatment secondary, all"),("h05_treatment_secondary_constant","Treatment secondary, constant"),("h08_deaths_psychostimulants","Deaths, psychostimulants"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),
("h12_mdma_per_pill_mg","MDMA per pill"),("h12_pills_over_140mg_pct","Pills >140 mg"),("h12_pills_over_210mg_pct","Pills >210 mg")]

_amph_crime=[("Synthetic-drug production sites dismantled",[("c20_synthetic_production_sites","production"),("c20_synthetic_storage_sites","storage")],"sites"),
("Labs dismantled, by drug",[("c20_amphetamine_labs_dismantled","amphetamine"),("c20_meth_labs_dismantled","methamphetamine")],"labs"),
("Dumpings of drug waste",[("c22_drug_waste_dumpings",None)],"dumpings"),
("OM investigations, synthetic drugs",[("c10_investigations_synthetic_drugs",None)],"investigations"),
("Pre-precursors seized",[("c23_precursors_all_kg","all synthetic drugs"),("c23_precursors_bmk_kg","BMK-type (amphetamine)")],"kg"),
("Amphetamine seized by Douane (kg)",[("c01_seized_douane_amphetamine_kg",None)],"kg"),
("Amphetamine seizures by Douane (number)",[("c01_seizures_douane_amphetamine_n",None)],"seizures"),
("Hard-drug offences registered (all list I)",[("c09_harddrug_offences_registered",None)],"offences"),
("Price of amphetamine (speed)",[("c18_price_eur_g",None)],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents")]
_amph_use=[("Last-year use",[("h01_lastyear_use_pct","CBS, 12+"),("h01_lastyear_use_18plus_pct","NDM, 18+")],"% of population"),
("Last-month use",[("h01_lastmonth_use_pct","CBS, 12+"),("h01_lastmonth_use_18plus_pct","NDM, 18+")],"% of population"),
("Lifetime use",[("h01_lifetime_use_pct","CBS, 12+"),("h01_lifetime_use_18plus_pct","NDM, 18+")],"% of population"),
("Lifetime use, pupils 12–16 and mbo students",[("h03_lifetime_use_pupils_pct","pupils"),("h04_lifetime_use_mbo_pct","mbo students")],"% of pupils/students"),
("Treatment, amphetamine primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, amphetamine secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Hospital admissions with amphetamine diagnosis",[("h07_hospital_main_diagnosis","main diagnosis"),("h07_hospital_secondary_diagnosis","secondary diagnosis")],"admissions"),
("Drug incidents involving amphetamine (MDI)",[("h06_share_ambulance_pct","ambulance"),("h06_share_mdi_hospitals_pct","MDI hospitals"),("h06_share_lis_hospitals_pct","LIS hospitals")],"% of drug incidents"),
("Deaths from psychostimulants",[("h08_deaths_psychostimulants",None)],"deaths (incl. MDMA)"),
("Amphetamine in wastewater",[("h11_wastewater_amsterdam","Amsterdam"),("h11_wastewater_eindhoven","Eindhoven"),("h11_wastewater_utrecht","Utrecht")],"mg/1,000 inh./day"),
("Amphetamine content of speed",[("h12_amphetamine_purity_pct",None)],"% amphetamine (mean, DIMS)")]
_amph_crime_corr=[("c20_synthetic_production_sites","Production sites"),("c20_amphetamine_labs_dismantled","Amphetamine labs"),("c20_synthetic_storage_sites","Storage sites"),("c20_meth_labs_dismantled","Meth labs"),("c22_drug_waste_dumpings","Drug waste dumpings"),
("c10_investigations_synthetic_drugs","OM investigations, synthetic"),("c23_precursors_all_kg","Pre-precursors, all kg"),("c23_precursors_bmk_kg","Pre-precursors, BMK kg"),
("c01_seized_douane_amphetamine_kg","Seized, amphetamine kg"),("c01_seizures_douane_amphetamine_n","Seizures, amphetamine n"),("c09_harddrug_offences_registered","Hard-drug offences"),("c18_price_eur_g","Price per gram")]
_amph_use_corr=[("h01_lastyear_use_pct","Last-year use 12+ (CBS)"),("h01_lastyear_use_18plus_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h04_lifetime_use_mbo_pct","mbo students, lifetime"),("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),
("h05_treatment_secondary_all","Treatment secondary, all"),("h07_hospital_main_diagnosis","Hospital, main diagnosis"),("h07_hospital_secondary_diagnosis","Hospital, secondary diagnosis"),
("h06_share_ambulance_pct","MDI share, ambulance"),("h06_share_lis_hospitals_pct","MDI share, LIS hospitals"),("h08_deaths_psychostimulants","Deaths, psychostimulants"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),("h12_amphetamine_purity_pct","Amphetamine content")]

_her_crime=[("Heroin processing locations dismantled",[("c20_heroin_processing_sites",None)],"locations"),
("Heroin seized by Douane (kg)",[("c01_seized_douane_heroin_kg",None)],"kg"),
("Heroin seizures by Douane (number)",[("c01_seizures_douane_heroin_n",None)],"seizures"),
("OM investigations, cocaine and heroin",[("c10_investigations_cocaine_heroin",None)],"investigations"),
("Hard-drug offences registered (all list I)",[("c09_harddrug_offences_registered",None)],"offences"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents")]
_her_use=[("Heroin use, adults 18+",[("h01_lifetime_use_18plus_pct","lifetime"),("h01_lastyear_use_18plus_pct","last year")],"% of population"),
("Opioid painkillers without prescription",[("h01_painkiller_nonprescribed_lastyear_pct",None)],"% of adults, last year"),
("High-risk opioid users (estimate)",[("h02_high_risk_opioid_users",None)],"people"),
("Treatment, opioids primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, opioids secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Hospital admissions, opioid main diagnosis",[("h07_hospital_main_diagnosis","excl. synthetic"),("h07_hospital_main_diagnosis_incl_synthetic","incl. synthetic")],"admissions"),
("Hospital admissions, opioid secondary diagnosis",[("h07_hospital_secondary_diagnosis","excl. synthetic"),("h07_hospital_secondary_diagnosis_incl_synthetic","incl. synthetic")],"admissions"),
("Drug deaths involving opioids",[("h08_deaths_opioids","opioids (EUDA def.)"),("h08_deaths_f11_underlying","F11 underlying cause")],"deaths"),
("People dispensed oxycodone (context)",[("h13_oxycodone_users",None)],"people"),
("People dispensed methadone (context)",[("h13_methadone_users",None)],"people"),
("Heroin content of samples",[("h12_heroin_purity_pct",None)],"% heroin (mean, DIMS)")]
_her_crime_corr=[("c01_seized_douane_heroin_kg","Seized, heroin kg"),("c01_seizures_douane_heroin_n","Seizures, heroin n"),("c10_investigations_cocaine_heroin","OM investigations, coc./her."),
("c09_harddrug_offences_registered","Hard-drug offences")]
_her_use_corr=[("h01_lifetime_use_18plus_pct","Lifetime use 18+ (NDM)"),("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),
("h05_treatment_secondary_all","Treatment secondary, all"),("h07_hospital_main_diagnosis","Hospital, main diagnosis"),("h07_hospital_secondary_diagnosis","Hospital, secondary diagnosis"),
("h07_hospital_main_diagnosis_incl_synthetic","Hospital main, incl. synth."),("h08_deaths_opioids","Deaths, opioids (EUDA)"),("h08_deaths_f11_underlying","Deaths, F11 underlying"),("h13_oxycodone_users","Oxycodone users")]

PANELS={"cocaine":{"crime":_coc_crime,"use":_coc_use},"cannabis":{"crime":_can_crime,"use":_can_use},"mdma":{"crime":_mdma_crime,"use":_mdma_use},"amphetamine":{"crime":_amph_crime,"use":_amph_use},"heroin":{"crime":_her_crime,"use":_her_use}}
CORR={"cocaine":{"crime":_coc_crime_corr,"use":_coc_use_corr},"cannabis":{"crime":_can_crime_corr,"use":_can_use_corr},"mdma":{"crime":_mdma_crime_corr,"use":_mdma_use_corr},"amphetamine":{"crime":_amph_crime_corr,"use":_amph_use_corr},"heroin":{"crime":_her_crime_corr,"use":_her_use_corr}}
TEXT={
 "cocaine":{"crime_sub":"Enforcement, violence, recruitment, trade and market indicators, 2003–2025",
            "use_sub":"Prevalence, treatment, acute harm, mortality, consumption and product risk, 2003–2025",
            "sources":"CBS, Nationale Drug Monitor, Politie, OM, GI-TOC","first":2003,
            "note":", or (treatment 2006, 2015) an older report with a different institution base"},
 "cannabis":{"crime_sub":"Enforcement, cultivation, trade, coffeeshop market and nuisance indicators, 1999–2025",
             "use_sub":"Prevalence, problematic use, treatment, acute harm, consumption and product potency, 1999–2025",
             "sources":"CBS, Nationale Drug Monitor (Trimbos, LADIS, Politie, Douane, OM)","first":1999,"note":""},
 "mdma":{"crime_sub":"Synthetic-drug production, environmental crime, trade, enforcement and market indicators, 2003–2025",
         "use_sub":"Prevalence, treatment, acute harm, mortality, consumption and product risk, 2003–2025",
         "sources":"CBS, Nationale Drug Monitor (Trimbos DIMS, LADIS, Politie, Douane, OM), Monitor Drugsincidenten","first":2003,"note":""},
 "amphetamine":{"crime_sub":"Synthetic-drug production, environmental crime, trade, enforcement and market indicators, 2003–2025",
         "use_sub":"Prevalence, treatment, hospital and acute harm, mortality, consumption and product purity, 2003–2025",
         "sources":"CBS, Nationale Drug Monitor (Trimbos DIMS, LADIS, LBZ, Politie, Douane, OM), Monitor Drugsincidenten","first":2003,"note":""},
 "heroin":{"crime_sub":"Trade, enforcement and nuisance indicators, 2003–2025",
         "use_sub":"Prevalence, high-risk use, treatment, hospital harm, mortality and supply context (heroin and other opioids), 2003–2025",
         "sources":"CBS, Nationale Drug Monitor (Trimbos, LADIS, LBZ, GIP, Douane, OM), Politie","first":2003,"note":""}}

# Indicator IDs shared by the plots and the correlation matrices: C = crime, U = use/dependency,
# then the panel number and, for panels with several series, a letter per series (e.g. C1a, U4).
def ids(drug, dim):
    out = {}
    for i, (_, ser, _) in enumerate(PANELS[drug][dim], 1):
        for k, (col, _) in enumerate(ser):
            out[col] = f"{dim[0].upper()}{i}" + ("abc"[k] if len(ser) > 1 else "")
    return out
