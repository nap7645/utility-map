#!/usr/bin/env python3
"""Merge one region's (or one batch's) raw research files into the processed datasets.

Replaces the one-off merge code written per region. Idempotent: re-running with the same files
adds nothing. Dry run by default; pass --apply to write.

    python3 scripts/merge_region.py --tag CA --denominator data/raw/hifld_over10k_caiso.csv
    python3 scripts/merge_region.py --tag CA --denominator data/raw/hifld_over10k_caiso.csv --apply

What it picks up for --tag X (file naming the research prompts already use):
    data/raw/program_chunks/chunk_X.csv, chunk_X_<anything>.csv      -> programs.csv
    data/raw/presence_scan/scan_X.csv, scan_X<digits>.csv            -> presence_scan.csv
    data/raw/interconnection/ic_X_state.csv                          -> interconnection_state.csv
    data/raw/interconnection/ic_X_utility.csv                        -> interconnection_utility.csv
    --denominator file (eia_id,hifld_name,hifld_state,customers)     -> data/raw/hifld_over10k.csv

Steps: validate every input (field counts, URLs on Yes cells, tier vocabulary) -> stop on any
problem; de-duplicate against what is already merged; report utility names that will not join a
map boundary (with the closest boundary names in the same state, for aliases.csv); then, with
--apply, write and rebuild docs/data/programs.json + presence.json.
"""
import argparse, csv, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_map_payload import norm, infer_scope

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
GENERIC = {"POWER","ELECTRIC","ENERGY","COOPERATIVE","UTILITIES","COMPANY","AND","OF","THE",
           "RURAL","MEMBERSHIP","ASSOCIATION","SERVICE","LIGHT","MUNICIPAL","DISTRICT","PUBLIC","CITY"}
TIERS = {"primary", "secondary", "unverified", "high", "medium", "low"}

# dataset: (processed file, fields, raw dir, filename regex template, de-dup key columns)
SETS = {
    "programs":  ("data/processed/programs.csv", 22, "data/raw/program_chunks",
                  r"^chunk_{t}(_[A-Za-z0-9_]+)?\.csv$", ["utility_name", "program_name", "program_category"]),
    "presence":  ("data/processed/presence_scan.csv", 17, "data/raw/presence_scan",
                  r"^scan_{t}\d*\.csv$", ["eia_id"]),
    "ic_state":  ("data/processed/interconnection_state.csv", 31, "data/raw/interconnection",
                  r"^ic_{t}_state\.csv$", ["state", "applies_to"]),
    "ic_util":   ("data/processed/interconnection_utility.csv", 21, "data/raw/interconnection",
                  r"^ic_{t}_utility\.csv$", ["utility_name", "state"]),
}

def read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        rr = list(csv.reader(fh))
    return (rr[0], [r for r in rr[1:] if any(c.strip() for c in r)]) if rr else ([], [])

def validate(path, nf):
    hdr, body = read(path)
    probs = []
    if len(hdr) != nf: probs.append(f"header has {len(hdr)} fields, expected {nf}")
    ix = {h: i for i, h in enumerate(hdr)}
    for n, r in enumerate(body, 2):
        if len(r) != nf:
            probs.append(f"line {n}: {len(r)} fields"); continue
        if "source_url" in ix and not r[ix["source_url"]].startswith("http"):
            probs.append(f"line {n}: source_url missing")
        for c in hdr:
            if c.endswith("_src") and c[:-4] in ix and r[ix[c[:-4]]] == "Yes" and not r[ix[c]].startswith("http"):
                probs.append(f"line {n}: {c[:-4]}=Yes without URL")
        if "confidence" in ix and r[ix["confidence"]].strip().lower() not in TIERS:
            probs.append(f"line {n}: confidence {r[ix['confidence']]!r}")
    return hdr, body, probs

def keyof(hdr, row, cols):
    ix = {h: i for i, h in enumerate(hdr)}
    return tuple(row[ix[c]].strip().lower() for c in cols)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True, help="file tag, e.g. CA, NY, SE1")
    ap.add_argument("--denominator", help="region denominator CSV (eia_id,hifld_name,hifld_state,customers)")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    a = ap.parse_args()
    t = re.escape(a.tag)

    plan, bad = {}, False
    for name, (dest, nf, rawdir, pat, key) in SETS.items():
        rx = re.compile(pat.format(t=t))
        files = sorted(f for f in os.listdir(P(rawdir)) if rx.match(f)) if os.path.isdir(P(rawdir)) else []
        dh, db = read(P(dest))
        seen = {keyof(dh, r, key) for r in db}
        pos = {keyof(dh, r, key): i for i, r in enumerate(db)}
        add, dup, upd = [], 0, 0
        for f in files:
            h, body, probs = validate(P(rawdir, f), nf)
            if probs:
                bad = True
                print(f"  !! {rawdir}/{f}: {len(probs)} problem(s): " + "; ".join(probs[:4]))
                continue
            if h != dh:
                bad = True; print(f"  !! {f}: header differs from {dest}"); continue
            for r in body:
                k = keyof(h, r, key)
                if k in seen:
                    # presence raw files are authoritative: a re-scan or fill pass replaces the merged row
                    if name == "presence" and k in pos and db[pos[k]] != r:
                        db[pos[k]] = r; upd += 1
                    else:
                        dup += 1
                    continue
                seen.add(k); add.append(r)
        plan[name] = (dest, dh, db, add, upd)
        print(f"{name:9s} files={files or '-'}  +{len(add)} new, {upd} updated, {dup} already merged")

    # denominator
    den_add = []
    dh, dbody = read(P("data/raw/hifld_over10k.csv"))
    if a.denominator:
        have = {r[0] for r in dbody}
        _, rows = read(P(a.denominator)) if not os.path.isabs(a.denominator) else read(a.denominator)
        den_add = [r for r in rows if r[0] not in have]
        print(f"{'denom':9s} +{len(den_add)} territories")

    # join check against the full denominator (existing + new)
    aliases = {r["utility_name"].strip(): r["hifld_name"].strip()
               for r in csv.DictReader(open(P("data/crosswalk/aliases.csv"), encoding="utf-8"))}
    den = dbody + den_add
    keys = {norm(r[1]): r for r in den}
    names = {}
    for nm in ("programs", "ic_util"):
        dest, h, _, add, _u = plan[nm]
        ix = {c: i for i, c in enumerate(h)}
        for r in add:
            names.setdefault(r[ix["utility_name"]], (r[ix["state"]], r[ix["rto"]] if "rto" in ix else ""))
    miss = []
    for n, (st, rto) in sorted(names.items()):
        if infer_scope(n, rto or "") != "utility": continue
        if norm(aliases.get(n, n)) not in keys: miss.append((n, st))
    if miss:
        print(f"\n{len(miss)} utility name(s) will not join a map boundary — add to data/crosswalk/aliases.csv:")
        for n, st in miss:
            words = set(norm(n).split()) - GENERIC
            cands = sorted(((len(words & (set(norm(r[1]).split()) - GENERIC)), r[1]) for r in den if r[2] == st), reverse=True)[:3]
            print(f"   {n!r} ({st})  closest: {[c for s, c in cands if s]}")
    else:
        print("\nall new utility names join a boundary")

    if bad:
        print("\nSTOPPED: fix the flagged files, then re-run."); return 1
    if not a.apply:
        print("\ndry run — nothing written. Re-run with --apply."); return 0

    for nm, (dest, h, db, add, upd) in plan.items():
        if not add and not upd: continue
        with open(P(dest), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(h); w.writerows(db + add)
    if den_add:
        with open(P("data/raw/hifld_over10k.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(dh); w.writerows(dbody + den_add)
    print("\nwritten. rebuilding map data…")
    for s in ("build_map_payload.py", "build_presence.py"):
        subprocess.run([sys.executable, P("scripts", s)], check=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
