# Drugsbeleid meetbaar maken: cocaine harm indicators for the Netherlands

This repository collects and combines yearly indicators of the two main harm dimensions of drug policy, as set out in the opinion piece *Drugsbeleid meetbaar maken*:

- **Crime harm**: harm from the illegal market (violence, recruitment of young people, corruption), plus trade, enforcement and market indicators.
- **Use/dependency harm**: prevalence, treatment, acute incidents, hospital care, mortality, consumption and product risk.

Cocaine is the first drug, as a proof of principle. The goal is to place the Netherlands, year by year, in the two-dimensional space of figure 3 of the piece (crime harm × use harm). Alcohol, tobacco, cannabis and MDMA follow later.

**Status (10 Nov 2026):** steps 1–4 of the plan are done for cocaine: candidate measures identified, biases recorded, data collected and combined into one data frame. Steps 5 (combining indicators per dimension) and 6 (plotting the two dimensions) are open.

## Repository structure

```
├── data/
│   ├── raw/
│   │   ├── manual_values.csv        values copied from reports, press releases and NDM chart data (with flag + source URL)
│   │   ├── cbs/cbs_series.json      series from the CBS open data API
│   │   ├── ndm_charts/              chart tables behind the Nationale Drug Monitor cocaine pages
│   │   ├── mdi/mdi_services.json    cocaine incidents per medical service (Monitor Drugsincidenten)
│   │   └── ladis/                   LADIS Kerncijfers 2016–2025 (PDF) and the cocaine series from it
│   ├── sources/
│   │   └── cocaine_harm_sources.csv one row per candidate measure: source, years, access, bias, status, dataset columns
│   └── processed/
│       ├── cocaine_harm_long.csv    one row per indicator-year: unit, value, flag, source URL
│       └── cocaine_harm_wide.csv    THE data frame: years 2003–2025 × 59 indicator columns
├── scripts/                         run in numeric order (see below)
├── output/
│   ├── figures/                     indicator plots and correlation matrices per dimension
│   └── tables/                      correlation tables (r and n per pair)
└── docs/                            methods report and an HTML view of the sources table
```

## Data frame

`data/processed/cocaine_harm_wide.csv` has one row per year (2003–2025) and one column per indicator; empty cells are missing years. Column names start with the indicator ID from the sources table: `c..` = crime dimension, `h..` = use/dependency dimension (e.g. `c06_liquidations`, `h08_deaths_cocaine`). Units, quality flags and the source of every single value are in `cocaine_harm_long.csv`.

In R:

```r
df   <- read.csv("data/processed/cocaine_harm_wide.csv")
long <- read.csv("data/processed/cocaine_harm_long.csv")
```

Value flags in the long file:

| Flag | Meaning |
| --- | --- |
| `exact` | as published by the source |
| `exact (NDM chart data)` | taken from the data table behind a Nationale Drug Monitor chart |
| `derived (...)` | calculated from published figures (method in the flag text) |
| `approximate (...)` | rounded in the source ("ruim 40.000") or read from a garbled table |
| `partial year (...)` | incomplete year |

## Reproducing

Requires Python 3.10+ (`pip install -r requirements.txt`) and internet access to opendata.cbs.nl, www.nationaledrugmonitor.nl, app.everviz.com and www.trimbos.nl.

| Script | What it does |
| --- | --- |
| `01_fetch_cbs.py` | downloads CBS StatLine series (cocaine use, F14 deaths, hard-drug offences and suspects, murder victims, Veiligheidsmonitor) |
| `02_fetch_ndm_charts.py` | downloads the chart tables behind the NDM cocaine pages (for checking the NDM values in `manual_values.csv`) |
| `03_extract_mdi_services.py` | downloads the MDI 2024 report and reads cocaine incidents per service from its vector chart |
| `04_build_dataset.py` | combines manual values, CBS series and MDI counts into the long and wide files |
| `05_plot_indicators.py` | small-multiple time-series plots per dimension |
| `06_plot_correlations.py` | correlation matrices per dimension (Pearson r, ≥5 shared years) |

To add or correct a value, edit `data/raw/manual_values.csv` (one row per value, with its source URL) and rerun scripts 04–06.

## Main caveats

- Many indicators partly measure institutional activity (enforcement, care supply, registration coverage) rather than harm. Seizures and registered offences follow police and customs effort; treatment counts follow access to care.
- On the crime side, enforcement indicators and violence indicators move in opposite directions (seizures up, liquidations down), so they should not be summed naively.
- Several sources measure the same thing differently (e.g. cocaine deaths: 61 in 2024 by the NDM definition vs 4 with F14 as underlying cause). Choosing one series per concept is an open step-5 decision.
- Series are short (often 5–10 years), so correlations are fragile and partly reflect shared time trends.

The full discussion, the per-step procedure and the list of open choices are in the methods report (`docs/`, live version: https://claude.ai/artifact/1c8ySyUMnzK6qrMtHMdzRG). Per-indicator biases are in `data/sources/cocaine_harm_sources.csv`.

## Main sources

CBS StatLine (open data API); Nationale Drug Monitor (Trimbos/WODC/Regioplan); LADIS Kerncijfers Verslavingszorg (Stichting IVZ); Monitor Drugsincidenten and DIMS (Trimbos); Politie, *Fenomeenbeeld Geweld* (2024); Openbaar Ministerie and Douane (seizures, HARC team); GI-TOC Global Organized Crime Index; NFI; EUDA/SCORE wastewater data (via NDM).

## Author

Timo van Ommeren (University of Amsterdam)
