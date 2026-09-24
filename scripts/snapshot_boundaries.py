#!/usr/bin/env python3
"""Snapshot HIFLD utility service-territory boundaries into docs/data/territories.geojson.

Why: the map used to query the HIFLD ArcGIS service on every page load. That is slow (10-20 s
for 22 states) and will not scale to the whole country. Run this once, commit the file, and the
map loads boundaries from GitHub Pages instead. Re-run when HIFLD updates (roughly yearly) or
when a region is added.

Usage (needs internet; run on your own machine, not the sandbox):
    python3 scripts/snapshot_boundaries.py            # states currently listed in docs/index.html
    python3 scripts/snapshot_boundaries.py --all      # all 50 states + DC (for nationwide work)

The state list and EXTRA_IDS are read from docs/index.html so there is one source of truth.
Standard library only.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVC = ("https://services3.arcgis.com/OYP7N6mAJJCyH6hd/arcgis/rest/services/"
       "Electric_Retail_Service_Territories_HIFLD/FeatureServer/0/query")
FIELDS = "ID,NAME,TYPE,STATE,CUSTOMERS,CNTRL_AREA,PLAN_AREA"
PAGE = 1000
ALL = ("AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV "
       "NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY").split()

def from_index():
    html = open(os.path.join(ROOT, "docs", "index.html"), encoding="utf-8").read()
    st = re.search(r"const STATES\s*=\s*\[(.*?)\]", html, re.S).group(1)
    ex = re.search(r"const EXTRA_IDS\s*=\s*\[(.*?)\]", html, re.S).group(1)
    q = lambda s: re.findall(r"'([^']+)'", re.sub(r"//[^\n]*", "", s))
    return q(st), q(ex)

def query(where):
    feats, offset = [], 0
    while True:
        params = urllib.parse.urlencode({
            "where": where, "outFields": FIELDS, "returnGeometry": "true", "outSR": "4326",
            "maxAllowableOffset": "0.005", "geometryPrecision": "4",
            "resultOffset": offset, "resultRecordCount": PAGE, "f": "geojson"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(f"{SVC}?{params}", timeout=120) as r:
                    gj = json.load(r)
                break
            except Exception as e:
                if attempt == 3: raise
                time.sleep(2 ** attempt)
        if "error" in gj: raise RuntimeError(gj["error"])
        batch = gj.get("features", [])
        feats += batch
        if not gj.get("exceededTransferLimit") or len(batch) < PAGE:
            return feats
        offset += len(batch)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="all 50 states + DC")
    a = ap.parse_args()
    states, extra = from_index()
    if a.all: states = ALL
    out, seen = [], set()
    for s in states:
        fs = query(f"STATE='{s}' AND COUNTRY='USA'")
        new = [f for f in fs if f["properties"]["ID"] not in seen]
        seen.update(f["properties"]["ID"] for f in new); out += new
        print(f"  {s}: {len(fs):4d} features  (total {len(out)})", flush=True)
    if extra:
        ids = ",".join(f"'{i}'" for i in extra if i not in seen)
        if ids:
            fs = query(f"ID IN ({ids})"); out += fs
            print(f"  EXTRA_IDS: {len(fs)} features  (total {len(out)})")
    path = os.path.join(ROOT, "docs", "data", "territories.geojson")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"type": "FeatureCollection",
                   "metadata": {"source": "HIFLD Electric Retail Service Territories", "snapshot": str(date.today()),
                                "states": states, "extra_ids": extra, "simplify_deg": 0.005},
                   "features": out}, fh, separators=(",", ":"))
    print(f"\nwrote {path}: {len(out)} features, {os.path.getsize(path)/1e6:.1f} MB")
    print("next: git add docs/data/territories.geojson && git commit -m 'snapshot boundaries' && git push")

if __name__ == "__main__":
    sys.exit(main())
