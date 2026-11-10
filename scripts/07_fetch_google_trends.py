"""Google Trends search interest in the Netherlands for five drug topics, monthly 2004-2025.

Usage: python scripts/07_fetch_google_trends.py   (needs: pip install pytrends)
All five topics are requested in one query, so values share one 0-100 scale
(100 = the month with the highest interest in any of the five topics).
Writes data/raw/trends/google_trends_nl.csv (month, topic, value).
"""
import csv
from pytrends.request import TrendReq
from _paths import RAW

TOPICS = {"cocaine": "/m/0256b", "cannabis": "/m/054yc0", "mdma": "/m/02qpq", "amphetamine": "/m/0_0j", "heroin": "/m/03n5b"}
p = TrendReq(hl="en-US", tz=-60, timeout=(10, 30))
p.build_payload(list(TOPICS.values()), timeframe="2004-01-01 2025-12-31", geo="NL")
df = p.interest_over_time()
(RAW / "trends").mkdir(parents=True, exist_ok=True)
with open(RAW / "trends" / "google_trends_nl.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["month", "topic", "value"])
    for t, row in df.iterrows():
        for drug, mid in TOPICS.items(): w.writerow([t.strftime("%Y-%m"), drug, int(row[mid])])
print("saved", len(df), "months")
