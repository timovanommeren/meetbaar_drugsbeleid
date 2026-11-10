"""Shared paths. All scripts run from any working directory."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
SOURCES = ROOT / "data" / "sources"
FIGURES = ROOT / "output" / "figures"
TABLES = ROOT / "output" / "tables"
