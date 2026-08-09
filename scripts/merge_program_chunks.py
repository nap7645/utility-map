#!/usr/bin/env python3
"""Repair, merge, validate the MISO/PJM program chunks into one master CSV."""
import csv, glob, itertools, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
HDR = "rto,state,utility_name,ownership_type,program_name,program_category,customer_segment,eligible_assets,enrollment_basis,incentive_structure,incentive_value_usd,event_limits,tariff_schedule,on_peak_window,peak_offpeak_rates,export_compensation,storage_eligible,stackable_with,program_status,source_url,last_verified,confidence".split(",")
N = len(HDR)

RTO = {"MISO", "PJM", "MISO/PJM", "PJM-market", "MISO-market", "Non-RTO", "SPP", "SERC"}
OWN = {"IOU", "Municipal", "Cooperative", "Federal/State", "RTO", "Third-party CSP"}
CAT = {"DR-DLC", "DR-Curtailment", "DR-BYOT", "DR-BYOD", "VPP", "TOU-Rate", "RTP-Rate",
       "CPP-PTR", "Demand-Charge", "EV-Rate", "Storage-Incentive", "Export-Comp",
       "Wholesale-Market", "Interconnection"}
ENR = {"Opt-in", "Opt-out", "Default", "Closed to new", "Pilot", "Waitlist",
       "Proposed/pending", "Closed to new enrollment", "Mandatory", "N/A", ""}
STOR = {"Yes", "No", "Yes-restricted", "Unclear", ""}
STAT = {"Active", "Closed to new enrollment", "Pilot", "Proposed/pending", "Terminated"}
CONF = {"High", "Medium", "Low"}

def anchors_ok(f):
    """Validate the 10 enum-constrained positions. Returns match score."""
    if len(f) != N:
        return -1
    s = 0
    checks = [
        (0, lambda v: v in RTO), (1, lambda v: len(v) == 2 or v == "multi"),
        (3, lambda v: v in OWN), (5, lambda v: v in CAT),
        (8, lambda v: v in ENR), (16, lambda v: v in STOR),
        (18, lambda v: v in STAT), (19, lambda v: v.startswith("http") or v == ""),
        (20, lambda v: bool(re.match(r"\d{4}-\d{2}-\d{2}$", v))),
        (21, lambda v: v in CONF),
    ]
    for i, fn in checks:
        if fn(f[i].strip()):
            s += 1
        else:
            return -1
    return s

def repair(f):
    """Row has >N fields from unquoted commas. Brute-force which boundaries to re-join."""
    extra = len(f) - N
    best = None
    for combo in itertools.combinations(range(1, len(f)), extra):
        out, cur = [], f[0]
        for i in range(1, len(f)):
            if i in combo:
                cur = cur + "," + f[i]
            else:
                out.append(cur); cur = f[i]
        out.append(cur)
        if anchors_ok(out) < 0:
            continue
        # prefer joins where the continuation began with a space (i.e. original was ", ")
        pref = sum(1 for i in combo if f[i][:1] == " ")
        if best is None or pref > best[0]:
            best = (pref, out)
    return best[1] if best else None

rows, failed, per_chunk = [], [], {}
for path in sorted(glob.glob(os.path.join(D, "chunk_*.csv"))):
    name = os.path.basename(path)
    good = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for i, f in enumerate(csv.reader(fh)):
            if not any(x.strip() for x in f):
                continue
            if i == 0 and f[0].strip().lower() == "rto":
                continue
            if len(f) < N:
                f = f + [""] * (N - len(f))
            if len(f) > N:
                r = repair(f)
                if r is None:
                    failed.append((name, i + 1, f)); continue
                f = r
            f = [x.strip() for x in f]
            f[20] = "2026-08-08"
            rows.append(f); good += 1
    per_chunk[name] = good

# dedupe on (utility, program, category, tariff)
seen, dedup, dups = set(), [], 0
for r in rows:
    k = (r[2].lower(), r[4].lower(), r[5], r[12].lower())
    if k in seen:
        dups += 1; continue
    seen.add(k); dedup.append(r)

rto_ord = {"MISO": 0, "MISO/PJM": 1, "PJM": 2, "Non-RTO": 3, "MISO-market": 4, "PJM-market": 5}
dedup.sort(key=lambda r: (rto_ord.get(r[0], 9), r[1], r[2], r[5], r[4]))

out = os.path.join(D, "miso_pjm_dr_tou_bess_programs.csv")
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
    w.writerow(HDR); w.writerows(dedup)

print("per-chunk parsed:")
for k, v in per_chunk.items():
    print(f"  {k}: {v}")
print(f"\ntotal {len(rows)} | dupes dropped {dups} | final {len(dedup)}")
print(f"unrepairable {len(failed)}")
for n, ln, f in failed:
    print(f"  !! {n} line {ln} ({len(f)} fields)")

print(f"\nutilities: {len({r[2] for r in dedup})}")
print(f"states: {len({r[1] for r in dedup})}")
print("\nby rto:")
for k in sorted({r[0] for r in dedup}):
    print(f"  {k}: {sum(1 for r in dedup if r[0]==k)}")
print("\nby category:")
for k, c in sorted(((k, sum(1 for r in dedup if r[5] == k)) for k in {r[5] for r in dedup}), key=lambda x: -x[1]):
    print(f"  {k}: {c}")
print("\nby ownership:")
for k in sorted({r[3] for r in dedup}):
    print(f"  {k}: {sum(1 for r in dedup if r[3]==k)}")
print("\nby confidence:")
for k in sorted({r[21] for r in dedup}):
    print(f"  {k}: {sum(1 for r in dedup if r[21]==k)}")
print(f"\nrows missing source_url: {sum(1 for r in dedup if not r[19].startswith('http'))}")
print(f"storage_eligible Yes/Yes-restricted: {sum(1 for r in dedup if r[16] in ('Yes','Yes-restricted'))}")
