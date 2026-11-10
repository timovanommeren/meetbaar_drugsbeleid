# Drugsbeleid meetbaar maken: drug harm indicators for the Netherlands

This repository collects and combines yearly indicators of the two main harm dimensions of drug policy, as set out in the opinion piece *Drugsbeleid meetbaar maken*:

- **Crime harm**: harm from the illegal market (violence, recruitment of young people, corruption, cultivation), plus trade, enforcement and market indicators.
- **Use/dependency harm**: prevalence, problematic use, treatment, acute incidents, hospital care, mortality, consumption and product risk.

The goal is to place the Netherlands, year by year and per drug, in the two-dimensional space of figure 3 of the piece (crime harm × use harm).

**Status (10 Nov 2026):** steps 1–4 of the plan (identify measures, record biases, collect data, build one data frame) are done for:

| Drug | Indicator columns | Values | Years |
| --- | --- | --- | --- |
| Cocaine | 59 | 504 | 2003–2025 |
| Cannabis | 55 | 533 | 1999–2025 |
| MDMA (ecstasy) | 39 | 373 | 2003–2025 |
| Amphetamine (speed) | 39 | 346 | 2003–2025 |
| Heroin (and other opioids) | 28 | 240 | 2003–2025 |

Steps 5 (combining indicators per dimension) and 6 (plotting the two dimensions) are open. Alcohol and tobacco may follow.

## Repository structure

```
├── data/
│   ├── raw/
│   │   ├── cbs/cbs_series.json        series from the CBS open data API (all drugs)
│   │   ├── cocaine/
│   │   │   ├── manual_values.csv      values copied from reports, press releases and NDM chart data (flag + source URL)
│   │   │   ├── ndm_charts.json        chart tables behind the Nationale Drug Monitor cocaine pages
│   │   │   ├── mdi/mdi_services.json  cocaine incidents per medical service (Monitor Drugsincidenten)
│   │   │   └── ladis/                 LADIS Kerncijfers 2016–2025 (PDF) and the cocaine series from it
│   │   ├── cannabis/
│   │   │   ├── manual_values.csv      values taken from NDM chart data and page text (chart ID in the flag)
│   │   │   └── ndm_charts.json        chart tables behind the NDM cannabis pages
│   │   ├── mdma/                      same layout; NDM chapter 'ecstasy', plus MDI report figures
│   │   ├── amphetamine/               same layout; NDM chapter 'amfetamine'
│   │   └── heroin/                    same layout; NDM chapter 'opiaten' (Opioïden)
│   ├── sources/
│   │   └── <drug>_harm_sources.csv    one row per candidate measure: source, years, access, bias, status, dataset columns
│   └── processed/
│       ├── <drug>_harm_long.csv       one row per indicator-year: unit, value, flag, source URL
│       └── <drug>_harm_wide.csv       THE data frame: years × indicator columns
├── scripts/                           run in numeric order (see below); _config.py holds per-drug plot settings
├── output/
│   ├── figures/                       <drug>_{crime,use}_{indicators,correlations}.png
│   └── tables/                        correlation tables (r and n per pair)
└── docs/                              methods report and an HTML view of the cocaine sources table
```

## Data frames

`data/processed/<drug>_harm_wide.csv` has one row per year and one column per indicator; empty cells are missing years. Column names start with the indicator ID from that drug's sources table: `c..` = crime dimension, `h..` = use/dependency dimension (e.g. `c20_cannabis_farms_dismantled`, `h08_deaths_cocaine`). Plots and correlation matrices label indicators with shared panel IDs (C = crime, U = use, panel number, letter per series: C1a, U4), so a matrix cell can be traced to its plot panel. The same ID means the same kind of measure across drugs (e.g. `h05` = treatment, `c09` = registered offences). Units, quality flags and the source of every single value are in the matching long file.

In R:

```r
cocaine  <- read.csv("data/processed/cocaine_harm_wide.csv")
cannabis <- read.csv("data/processed/cannabis_harm_wide.csv")
long     <- read.csv("data/processed/cannabis_harm_long.csv")
```

Value flags in the long files:

| Flag | Meaning |
| --- | --- |
| `exact` | as published by the source |
| `exact (NDM chart data...)` | taken from the data table behind a Nationale Drug Monitor chart |
| `derived (...)` | calculated from published figures (method in the flag text) |
| `approximate (...)` | rounded in the source ("ruim 40.000") or read from a garbled table |
| `partial year (...)` | incomplete year |

## Reproducing

Requires Python 3.10+ (`pip install -r requirements.txt`) and internet access to opendata.cbs.nl, www.nationaledrugmonitor.nl, app.everviz.com and www.trimbos.nl. Scripts that work per drug take the drug as argument (`cocaine`, `cannabis`, `mdma`, `amphetamine` or `heroin`).

| Script | What it does |
| --- | --- |
| `01_fetch_cbs.py` | downloads CBS StatLine series (cocaine, cannabis, ecstasy and amphetamine use, F11/F12/F14 deaths, hard- and soft-drug offences and suspects, murder victims, Veiligheidsmonitor) |
| `02_fetch_ndm_charts.py <drug>` | downloads the chart tables behind the NDM pages of that drug (for checking the NDM values in `manual_values.csv`) |
| `03_extract_mdi_services.py` | cocaine only: downloads the MDI 2024 report and reads cocaine incidents per service from its vector chart |
| `04_build_dataset.py <drug>` | combines manual values, CBS series (and for cocaine the MDI counts) into the long and wide files |
| `05_plot_indicators.py <drug>` | small-multiple time-series plots per dimension |
| `06_plot_correlations.py <drug>` | correlation matrices per dimension (Pearson r, ≥5 shared years) |

To add or correct a value, edit `data/raw/<drug>/manual_values.csv` (one row per value, with its source URL) and rerun scripts 04–06 for that drug.

## Main caveats

- Many indicators partly measure institutional activity (enforcement, care supply, registration coverage) rather than harm. Seizures, dismantled cannabis farms and registered offences follow police and customs effort; treatment counts follow access to care.
- On the crime side, enforcement and harm indicators often move in opposite directions: for cocaine, seizures rose while liquidations fell; for cannabis, dismantled farms fell by 87% (2014–2025) while Douane seizures rose sharply.
- For MDMA, the most direct crime harm is environmental: dumpings of synthetic-drug waste (160–292 a year, 2015–2024). Production indicators cover all synthetic drugs, not MDMA alone, and deaths are only published for psychostimulants as a group.
- For amphetamine, use is flat (last year 1.0–1.6%) while treatment and hospital admissions (secondary diagnosis) move on their own. Production, dumping, OM and death series are shared with MDMA; BMK-type precursors are the amphetamine-specific production signal, and wastewater in Eindhoven may partly reflect dumped production waste.
- For heroin, population surveys miss the users (last-year use 0–0.1%); the relevant group is about 13,300 high-risk opioid users (2023). Most health series cover all opioids, and most opioid deaths now involve painkillers rather than heroin. Acquisitive crime and nuisance by dependent users, the classic crime harm, has no heroin-specific series.
- For cannabis, crime harm is hard to measure at all: violence in the criminal milieu cannot be attributed to cannabis, and coffeeshop supply ('back door') is unmeasured.
- Several sources measure the same thing differently (e.g. cocaine deaths: 61 in 2024 by the NDM definition vs 4 with F14 as underlying cause). Choosing one series per concept is an open step-5 decision.
- Series are short (often 5–10 years), so correlations are fragile and partly reflect shared time trends.

The procedure, cross-cutting limitations, discussion points and future directions are in the generic methods report (live: https://claude.ai/artifact/1c8ySyUMnzK6qrMtHMdzRG). Data, biases and discussion points per drug are in the drug reports: [cocaine](https://claude.ai/artifact/4xetkrZmXWykZsMcbr7HUR), [cannabis](https://claude.ai/artifact/7rEWZNSFcrYqbcvy9j7z7s), [MDMA](https://claude.ai/artifact/PuuUfdrtt2ZJVZDmhHMPEQ), [amphetamine](https://claude.ai/artifact/AQiDiSyayraJVQ6xsWwRMK), [heroin](https://claude.ai/artifact/8MFpiVJde3SBdZWtJz7unU). Per-indicator biases are in `data/sources/<drug>_harm_sources.csv` (cocaine 37, cannabis 33, MDMA 30, amphetamine 31, heroin 31 candidate measures). `docs/` holds an earlier Word export of the cocaine report.

## Main sources

CBS StatLine (open data API); Nationale Drug Monitor (Trimbos/WODC/Regioplan) and its chart data; LADIS Kerncijfers Verslavingszorg (Stichting IVZ); Monitor Drugsincidenten, DIMS and the THC monitor (Trimbos); Politie (*Fenomeenbeeld Geweld* 2024; dismantled cannabis farms); Openbaar Ministerie and Douane (seizures, HARC team); Nationaal Overzicht Drugslocaties 2023–2025 editions (labs by drug type, dumpings, cannabis farms, heroin processing sites); Trimbos *Harm reduction in Nederland* 2026; WODC/Intraval (*Coffeeshops in Nederland*); GI-TOC Global Organized Crime Index; NFI; EUDA/SCORE wastewater data (via NDM).

## Author

Timo van Ommeren (University of Amsterdam)
