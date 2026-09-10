#!/usr/bin/env python3
"""Validate a research CSV before an agent reports done.

usage: validate_csv.py FILE --fields N [--targets targets.csv]
exit 0 = clean, 1 = problems (printed)
"""
import argparse, csv, sys

TIERS = {"primary", "secondary", "unverified", "high", "medium", "low"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--fields", type=int, required=True)
    ap.add_argument("--targets", help="targets CSV with an eia_id column; every id must appear exactly once")
    a = ap.parse_args()

    with open(a.file, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        print("EMPTY FILE"); sys.exit(1)
    hdr, body = rows[0], [r for r in rows[1:] if any(c.strip() for c in r)]
    probs = []

    if len(hdr) != a.fields:
        probs.append(f"header has {len(hdr)} fields, expected {a.fields}")
    for i, r in enumerate(body, 2):
        if len(r) != a.fields:
            probs.append(f"line {i}: {len(r)} fields (expected {a.fields}) — unquoted comma?")

    idx = {h: i for i, h in enumerate(hdr)}
    for i, r in enumerate(body, 2):
        if len(r) != a.fields:
            continue
        # source links
        if "source_url" in idx and not r[idx["source_url"]].strip().startswith("http"):
            probs.append(f"line {i}: source_url missing or not a URL")
        for col in hdr:
            if col.endswith("_src"):
                cell = col[:-4]
                if cell in idx and r[idx[cell]].strip() == "Yes" and not r[idx[col]].strip().startswith("http"):
                    probs.append(f"line {i}: {cell}=Yes but {col} is not a URL")
        # tier vocabulary
        if "confidence" in idx and r[idx["confidence"]].strip().lower() not in TIERS:
            probs.append(f"line {i}: confidence={r[idx['confidence']]!r} not in Primary/Secondary/Unverified")
        if "rto" in idx and not r[idx["rto"]].strip():
            probs.append(f"line {i}: rto blank")

    if a.targets:
        with open(a.targets, newline="", encoding="utf-8") as fh:
            want = [t["eia_id"].strip() for t in csv.DictReader(fh)]
        got = [r[idx["eia_id"]].strip() for r in body if len(r) == a.fields and "eia_id" in idx]
        for t in want:
            n = got.count(t)
            if n != 1:
                probs.append(f"target eia_id {t} appears {n} times (expected 1)")
        extra = set(got) - set(want)
        if extra:
            probs.append(f"{len(extra)} eia_ids not in targets: {sorted(extra)[:5]}…")

    if probs:
        print(f"{len(probs)} problem(s) in {a.file}:")
        for p in probs[:60]:
            print("  -", p)
        if len(probs) > 60:
            print(f"  … {len(probs)-60} more")
        sys.exit(1)
    print(f"OK: {a.file} — {len(body)} rows × {a.fields} fields")

if __name__ == "__main__":
    main()
