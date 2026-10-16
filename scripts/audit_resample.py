#!/usr/bin/env python3
"""Round-2 presence re-audit sample (fresh seed): per region, N Yes + M No cells not audited before.
    python3 scripts/audit_resample.py [--seed 20261015] [--yes 8] [--no 12] REGION...
Writes audit/samples_r2/<REGION>.json in the same item format as audit_sample.py."""
import argparse, csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from audit_sample import group_of, rd, P
SH = {"res_habit": "rh", "res_dispatch": "rd", "ci_habit": "ch", "ci_dispatch": "cd"}
ap = argparse.ArgumentParser(); ap.add_argument("regions", nargs="+"); ap.add_argument("--seed", type=int, default=20261015)
ap.add_argument("--yes", type=int, default=8); ap.add_argument("--no", type=int, default=12); ap.add_argument("--round", type=int, default=2); a = ap.parse_args()
pj = json.load(open(P("docs/data/presence.json"))); den = {r["eia_id"]: r for r in rd(P("data/raw/hifld_over10k.csv"))}
done = set()
for f in os.listdir(P("audit/results")):
    for x in json.load(open(P("audit/results", f))):
        if x.get("type") == "presence":
            s = json.load(open(P("audit/samples", f)))["items"][x["idx"]]; done.add((s["eia_id"], s["cell"]))
for rd_ in sorted(d for d in os.listdir(P("audit")) if d.startswith("results_r")):
    for f in os.listdir(P("audit", rd_)):
        for x in json.load(open(P("audit", rd_, f))): done.add((x["eia_id"], x["cell"]))
ap_out = "audit/samples_r%d" % a.round
os.makedirs(P(ap_out), exist_ok=True)
for g in a.regions:
    rng = random.Random(f"{a.seed}-{g}"); pool = {"Yes": [], "No": []}
    for i, e in pj.items():
        if i not in den or (group_of(e.get("rto")) or "West") != g: continue
        for c, k in SH.items():
            v = e[k]
            if v in pool and (i, c) not in done:
                pool[v].append({"type": "presence", "bucket": "r%d" % a.round, "eia_id": i, "utility_name": e["u"], "state": den[i]["hifld_state"],
                                "ownership": e.get("ow", ""), "customers": den[i]["customers"], "cell": c, "claimed": v, "source_url": e[k + "s"]})
    items = rng.sample(pool["Yes"], min(a.yes, len(pool["Yes"]))) + rng.sample(pool["No"], min(a.no, len(pool["No"])))
    json.dump({"region": g, "seed": a.seed, "items": items}, open(P(ap_out, g + ".json"), "w"), indent=1)
    print(g, "pool Y/N", len(pool["Yes"]), len(pool["No"]), "-> items", len(items))
