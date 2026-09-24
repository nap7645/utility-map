#!/usr/bin/env python3
"""Build the has/doesn't-have presence table.

Two buckets x two segments:
  habit    = price-signal programs the customer responds to (TOU, RTP, CPP/PTR, demand charge, EV rate)
  dispatch = programs where the utility/aggregator controls the asset (DLC, BYOT, BYOD, VPP, curtailment)
  segments = residential, C&I

Three states per cell: Yes | No | Unknown.  A fourth, ViaAggregator, is reserved for the
dispatch cells once the aggregator layer (Phase 4) exists.

Inputs : data/raw/hifld_over10k.csv        (denominator: every territory >10k customers)
         data/processed/programs.csv        (derives Yes)
         data/processed/presence_scan.csv   (optional: agent-researched Yes/No for the rest)
         data/crosswalk/aliases.csv
Output : data/processed/presence.csv
         docs/data/presence.json
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_map_payload import norm, P
from source_tier import source_tier

HABIT = {"TOU-Rate", "RTP-Rate", "CPP-PTR", "Demand-Charge", "EV-Rate"}
DISPATCH = {"DR-DLC", "DR-BYOT", "DR-BYOD", "VPP", "DR-Curtailment"}
CELLS = ["res_habit", "res_dispatch", "ci_habit", "ci_dispatch"]
RESEARCHED_MIN = 3   # program rows needed before absence in a family counts as "No"

def segs(s):
    s = s or ""
    res = "Residential" in s or s.strip() == "All"
    ci = any(k in s for k in ("SmallC&I", "LargeC&I", "C&I")) or s.strip() == "All"
    return res, ci

def load_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def main():
    aliases = {r["utility_name"].strip(): r["hifld_name"].strip()
               for r in load_csv(P("data", "crosswalk", "aliases.csv"))}
    # reverse: normalized HIFLD key -> our utility_name (for entities in programs.csv)
    progs = load_csv(P("data", "processed", "programs.csv"))
    by_key = {}
    for r in progs:
        key = norm(aliases.get(r["utility_name"], r["utility_name"]))
        by_key.setdefault(key, {"name": r["utility_name"], "rto": r["rto"], "own": r["ownership_type"],
                                "rows": []})["rows"].append(r)

    # derive Yes from programs.csv
    def derive(rows):
        out = {c: "Unknown" for c in CELLS}
        src = {c: "" for c in CELLS}
        for r in rows:
            cat = r["program_category"]
            if r["program_status"] in ("Terminated",):
                continue
            res, ci = segs(r["customer_segment"])
            b = "habit" if cat in HABIT else "dispatch" if cat in DISPATCH else None
            if not b:
                continue
            for seg_ok, seg in ((res, "res"), (ci, "ci")):
                if seg_ok:
                    c = f"{seg}_{b}"
                    out[c] = "Yes"
                    if not src[c]:
                        src[c] = r["source_url"]
        # A utility that got full program research (>= RESEARCHED_MIN rows) and has nothing in a
        # cell's family is a checked "No", not "Unknown". 1-2 stray rows (e.g. one net-metering
        # entry) are not enough evidence of absence, so those stay Unknown.
        inferred = set()
        active = [r for r in rows if r["program_status"] != "Terminated"]
        if len(active) >= RESEARCHED_MIN:
            for c in CELLS:
                if out[c] == "Unknown":
                    out[c] = "No"; inferred.add(c)
        return out, src, inferred

    # agent scan results override Unknown (never override a derived Yes)
    scan = {r["eia_id"].strip(): r for r in load_csv(P("data", "processed", "presence_scan.csv"))}

    hifld = load_csv(P("data", "raw", "hifld_over10k.csv"))
    rows_out, stats = [], {c: {"Yes": 0, "No": 0, "Unknown": 0, "ViaAggregator": 0} for c in CELLS}
    matched = 0
    for h in hifld:
        key = norm(h["hifld_name"])
        m = by_key.get(key)
        rec = {
            "eia_id": h["eia_id"], "hifld_name": h["hifld_name"], "hifld_state": h["hifld_state"],
            "customers": h["customers"], "utility_name": m["name"] if m else "",
            "rto": m["rto"] if m else "", "ownership_type": m["own"] if m else "",
        }
        if m:
            matched += 1
            cells, src, inferred = derive(m["rows"])
        else:
            cells = {c: "Unknown" for c in CELLS}
            src = {c: "" for c in CELLS}
            inferred = set()
        s = scan.get(h["eia_id"])
        if s:
            for c in CELLS:
                # scans fill Unknown, and may overturn an inferred "No" (never a derived Yes)
                if (cells[c] == "Unknown" or (c in inferred and s.get(c, "").strip() == "Yes")) and s.get(c, "").strip():
                    cells[c] = s[c].strip()
                    src[c] = s.get(c + "_src", "").strip()
            for k in ("rto", "ownership_type", "utility_name"):
                if not rec[k] and s.get(k, "").strip():
                    rec[k] = s[k].strip()
        for c in CELLS:
            rec[c] = cells[c]
            rec[c + "_src"] = src[c]
            stats[c][cells[c] if cells[c] in stats[c] else "Unknown"] += 1
        rec["scan_notes"] = s.get("notes", "") if s else ""
        rec["last_verified"] = (s.get("last_verified") if s else "") or ("2026-08-08" if m else "")
        rows_out.append(rec)

    hdr = ["eia_id", "hifld_name", "hifld_state", "customers", "utility_name", "rto", "ownership_type"] + \
          [x for c in CELLS for x in (c, c + "_src")] + ["scan_notes", "last_verified"]
    out = P("data", "processed", "presence.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr)
        w.writeheader(); w.writerows(rows_out)

    # compact JSON keyed by eia_id for the map
    def tier_for(r, c):
        if r[c] != "Yes":
            return ""
        s = scan.get(r["eia_id"], {})
        conf = s.get("confidence", "") if s else "High"   # derived-from-programs.csv rows were read directly
        return source_tier(r[c + "_src"], conf)
    js = {r["eia_id"]: {"rh": r["res_habit"], "rd": r["res_dispatch"], "ch": r["ci_habit"], "cd": r["ci_dispatch"],
                        "rht": tier_for(r, "res_habit"), "rdt": tier_for(r, "res_dispatch"),
                        "cht": tier_for(r, "ci_habit"), "cdt": tier_for(r, "ci_dispatch"),
                        "u": r["utility_name"], "rto": r["rto"], "n": r["customers"]} for r in rows_out}
    os.makedirs(P("docs", "data"), exist_ok=True)
    with open(P("docs", "data", "presence.json"), "w", encoding="utf-8") as fh:
        json.dump(js, fh, separators=(",", ":"))

    print(f"presence.csv: {len(rows_out)} territories >10k; {matched} matched to programs.csv; "
          f"{len(scan)} scan rows applied")
    print(f"{'cell':14s} {'Yes':>5s} {'No':>5s} {'Unk':>5s} {'ViaAgg':>7s}")
    for c in CELLS:
        s = stats[c]
        print(f"{c:14s} {s['Yes']:5d} {s['No']:5d} {s['Unknown']:5d} {s['ViaAggregator']:7d}")
    unk = [r for r in rows_out if all(r[c] == "Unknown" for c in CELLS)]
    print(f"\nfully Unknown (scan targets): {len(unk)}")
    print(f"customers in scan targets: {sum(int(float(r['customers'] or 0)) for r in unk):,} "
          f"of {sum(int(float(r['customers'] or 0)) for r in rows_out):,}")

if __name__ == "__main__":
    main()
