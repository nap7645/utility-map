#!/usr/bin/env python3
"""Draw the audit samples (plans/SPEC.md 6.2, RUBRIC section 1). Seeded and reproducible.

    python3 scripts/audit_sample.py [--seed 20261002] [--top 5]

Writes audit/samples/<REGION>.json (items for one auditor agent) and audit/samples/INDEX.md.
Per region: 100% of the top-N territories by customers (their program rows + Yes/No presence cells), plus a stratified
random sample (ownership x customer tercile; Yes and No both represented) of ~5% of the remaining Yes/No presence cells
(min 20) and ~10% of the remaining program rows (min 15). State interconnection rows: the 2 focus cells per state.
"""
import argparse, csv, json, math, os, random, re, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from build_map_payload import norm, infer_scope
ROOT = os.path.dirname(HERE); P = lambda *a: os.path.join(ROOT, *a)
CELLS = ["res_habit", "res_dispatch", "ci_habit", "ci_dispatch"]
GROUP = {"MISO": "MISO", "MISO/PJM": "MISO", "PJM": "PJM", "SPP": "SPP", "AECI": "SPP", "ERCOT": "ERCOT", "ISO-NE": "ISO-NE",
         "Other-nonRTO": "ISO-NE", "NYISO": "NYISO", "CAISO": "CAISO", "TVA": "SE", "SERC-nonRTO": "SE", "FRCC-nonRTO": "SE",
         "Non-RTO": "SE", "WECC-nonRTO": "West", "AK-islanded": "AKHI", "HI-islanded": "AKHI"}
FORCE_TOP = {"ERCOT": ["44372", "8901", "3278"]}   # Oncor, CenterPoint, AEP Texas Central: customers blank in denominator

def rd(p):
    with open(p, newline="", encoding="utf-8") as fh: return list(csv.DictReader(fh))

def group_of(rto):
    r = (rto or "").replace("-market", "")
    return GROUP.get(r) or GROUP.get(rto) or ("West" if r.startswith("WECC") else None)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--seed", type=int, default=20261002); ap.add_argument("--top", type=int, default=5)
    a = ap.parse_args(); rng = random.Random(a.seed)
    denom = rd(P("data/raw/hifld_over10k.csv")); pres = rd(P("data/processed/presence_scan.csv")); progs = rd(P("data/processed/programs.csv"))
    pj = json.load(open(P("docs/data/presence.json"), encoding="utf-8")); geo = json.load(open(P("docs/data/territories.geojson"), encoding="utf-8"))
    ic = rd(P("data/processed/interconnection_state.csv"))
    aliases = {r["utility_name"].strip(): r["hifld_name"].strip() for r in rd(P("data/crosswalk/aliases.csv"))}
    scope_ovr = {r["utility_name"].strip(): r["scope"].strip() for r in rd(P("data/crosswalk/scope_overrides.csv"))}
    html = open(P("docs/index.html"), encoding="utf-8").read()
    excl = set(re.findall(r"'(\d+)'", (re.search(r"JOIN_EXCLUDE = new Set\(\[(.*?)\]\)", html) or [None, ""])[1]))
    st_of = {r["eia_id"]: r["hifld_state"] for r in denom}
    cust = {r["eia_id"]: int(r["customers"] or 0) for r in denom}
    for p in geo["features"]:
        i = str(p["properties"]["ID"]);
        if i in cust and cust[i] == 0 and p["properties"]["CUSTOMERS"] > 0: cust[i] = p["properties"]["CUSTOMERS"]
    pr_by = {r["eia_id"]: r for r in pres}
    # territories by region
    reg_of, ids_by = {}, defaultdict(list)
    for r in denom:
        i = r["eia_id"]; e = pj.get(i, {}); g = group_of(e.get("rto")) or "West"
        reg_of[i] = g; ids_by[g].append(i)
    # polygon names by norm key -> eia ids (target territories only)
    key_ids = defaultdict(list)
    for r in denom: key_ids[norm(r["hifld_name"])].append(r["eia_id"])
    # program rows -> territory (or market bucket)
    prow_reg, prow_terr = {}, {}
    for n, r in enumerate(progs):
        name = r["utility_name"]; sc = scope_ovr.get(name) or infer_scope(name, r["rto"])
        ids = [i for i in key_ids.get(norm(aliases.get(name, name)), []) if i not in excl]
        st = r["state"]
        if sc == "utility" and ids:
            prow_terr[n] = ids[0]; prow_reg[n] = reg_of[ids[0]]
        else:
            prow_reg[n] = group_of(r["rto"]) or {"MN": "MISO"}.get(st, "West")
    os.makedirs(P("audit", "samples"), exist_ok=True)
    idx = ["# Audit sample index", f"seed {a.seed}, top-{a.top} per region", "", "| region | territories | top-N | top-N program rows | top-N presence cells | sampled cells (Y/N) | sampled program rows | total items |", "|---|---|---|---|---|---|---|---|"]
    tot = 0
    for g, ids in sorted(ids_by.items()):
        top = FORCE_TOP.get(g, [])[:a.top]
        for i in sorted(ids, key=lambda i: -cust[i]):
            if len(top) >= a.top: break
            if i not in top: top.append(i)
        items = []
        SHORT = {"res_habit": "rh", "res_dispatch": "rd", "ci_habit": "ch", "ci_dispatch": "cd"}
        def cell_item(i, c, bucket):
            e = pj.get(i)
            if not e or e[SHORT[c]] not in ("Yes", "No"): return None
            return {"type": "presence", "bucket": bucket, "eia_id": i, "utility_name": e["u"], "state": st_of[i], "ownership": e.get("ow", ""),
                    "customers": cust.get(i), "cell": c, "claimed": e[SHORT[c]], "source_url": e[SHORT[c][0:1] + SHORT[c][1:2] + "s"] if False else e[{"rh": "rhs", "rd": "rds", "ch": "chs", "cd": "cds"}[SHORT[c]]]}
        top_cells = [x for i in top for c in CELLS if (x := cell_item(i, c, "top"))]
        top_rows = [n for n, i in prow_terr.items() if i in top]
        # sample pools
        pool_cells = [x for i in ids if i not in top for c in CELLS if (x := cell_item(i, c, "sample"))]
        want = max(20, math.ceil(0.05 * (len(pool_cells) + len(top_cells))))
        terc = {}
        srt = sorted(ids, key=lambda i: cust[i]);
        for k, i in enumerate(srt): terc[i] = min(2, 3 * k // max(1, len(srt)))
        def strat(x): return (x["claimed"], x["ownership"], terc[x["eia_id"]])
        buckets = defaultdict(list)
        for x in pool_cells: buckets[strat(x)].append(x)
        for b in buckets.values(): rng.shuffle(b)
        chosen, k = [], 0
        keys = sorted(buckets, key=str)
        # guarantee both Yes and No are represented: round-robin over strata, Yes first until quotas
        quota = {"Yes": max(8, round(want * 0.4)), "No": max(8, round(want * 0.6))}
        taken = {"Yes": 0, "No": 0}
        while len(chosen) < min(want, len(pool_cells)) and any(buckets[kk] for kk in keys):
            for kk in keys:
                if buckets[kk] and taken[kk[0]] < quota[kk[0]] and len(chosen) < want:
                    chosen.append(buckets[kk].pop()); taken[kk[0]] += 1
            if all(not buckets[kk] or taken[kk[0]] >= quota[kk[0]] for kk in keys): break
        pool_rows = [n for n in prow_reg if prow_reg[n] == g and n not in top_rows]
        wantr = max(15, math.ceil(0.10 * len(pool_rows))); samp_rows = rng.sample(pool_rows, min(wantr, len(pool_rows)))
        def prog_item(n, bucket):
            r = progs[n]; return {"type": "program", "bucket": bucket, "row": n + 2, **{k: r[k] for k in r}}
        items = top_cells + chosen + [prog_item(n, "top") for n in top_rows] + [prog_item(n, "sample") for n in samp_rows]
        json.dump({"region": g, "seed": a.seed, "top_territories": [{"eia_id": i, "name": pj.get(i, {}).get("u", ""), "customers": cust[i]} for i in top], "items": items},
                  open(P("audit", "samples", g + ".json"), "w", encoding="utf-8"), indent=1)
        idx.append(f"| {g} | {len(ids)} | {len(top)} | {len(top_rows)} | {len(top_cells)} | {len(chosen)} (Y {taken['Yes']}/N {taken['No']}) | {len(samp_rows)} | {len(items)} |"); tot += len(items)
    # interconnection focus cells
    items = []
    for r in ic:
        for c in ("export_credit_basis", "grid_charging_allowed"):
            items.append({"type": "ic_state", "state": r["state"], "applies_to": r["applies_to"], "jurisdiction_body": r["jurisdiction_body"], "cell": c, "claimed": r[c], "source_url": r["source_url"]})
    json.dump({"region": "IC", "seed": a.seed, "items": items}, open(P("audit", "samples", "IC.json"), "w", encoding="utf-8"), indent=1)
    idx.append(f"| IC (state rules) | {len(ic)} | - | - | - | - | - | {len(items)} |"); tot += len(items)
    idx.append(f"\nTotal items: {tot}")
    open(P("audit", "samples", "INDEX.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n"); print("\n".join(idx))

if __name__ == "__main__":
    main()
