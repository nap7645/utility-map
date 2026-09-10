---
name: utility-program-research
description: Web-research electric utility programs (demand response, TOU/RTP rates, storage incentives, VPPs, interconnection and net-metering rules) into schema-conformant CSVs for the utility-map repo. Use when asked to scan, research, or build CSV rows for utilities, states, or RTOs — presence scans, full program rows, interconnection rules, or wholesale market products. Encodes the hard-won rules from MISO/PJM so every agent writes the same way.
---

# Utility program research → CSV

You are producing rows for a dataset that backs a behind-the-meter PV+storage economics tool.
Every row must be traceable to a link. A wrong row is worse than a blank one.

## 1. Pick the job type and read its schema

| Job | Schema (read it FIRST, in full) | Fields | Prompt template |
|---|---|---|---|
| Presence scan (has/doesn't-have, 4 cells) | `data/raw/presence_scan/SCAN_SCHEMA.md` | 17 | `plans/prompts/presence_scan.md` |
| Full program rows | `data/processed/programs_SCHEMA.md` | 22 | `plans/prompts/programs.md` |
| Interconnection (state + utility deltas) | `data/processed/interconnection_SCHEMA.md` | 31 / 21 | `plans/prompts/interconnection.md` |
| Wholesale market products | `data/processed/programs_SCHEMA.md` (rto=`X-market`) | 22 | `plans/prompts/wholesale.md` |

If a region file exists at `plans/rto_<x>.md` or `plans/region_<x>.md`, read it — its cluster
notes (G&T memberships, TVA-style shortcuts, which co-ops are in a different RTO) cut the work
in half.

## 2. Set up the file before researching anything

```python
import csv, os
OUT = "<path from the prompt>"
HEADER = [...]            # copy exactly from the schema
if not os.path.exists(OUT):
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(HEADER)
def append(rows):
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
```

Append every ~8 rows. Never hold results in memory until the end — agents get killed by session
and spend limits mid-run, and unwritten work is gone. Never write CSV by hand or with bash
heredocs; unquoted commas inside values have cost repair passes before.

## 3. Research loop, per utility

1. Find the utility's own site (search `"<utility name>" rates` or `demand response`). Prefer its
   rates/tariff page and program pages over anything else.
2. If it's a co-op, check whether its G&T runs the program (Great River, Dairyland, Hoosier,
   Wolverine, Buckeye, Basin, Tri-State, Oglethorpe, Allegheny, ODEC…). If so, cite the G&T and
   mark the member — that's accurate. If it's a TVA distributor, cite TVA once.
3. Tag `rto` on every row. Utilities in the same state are routinely in different markets.
4. For each program: the exact published name, the category from the schema vocabulary, the
   dollar figure with units and date if published (blank if not), and a **deep link**.
5. Write `confidence` as a **source tier**, not a feeling:
   - `Primary` — the link *is* the source (utility tariff/program page, regulator order, RTO
     manual, statute).
   - `Secondary` — the link *reports on* it (news, DSIRE, trade press, a G&T page about a member).
   - `Unverified` — no usable link or the link doesn't show the claim.

## 4. Things that are not optional

- **Never invent** a row, a value, or a URL. Blank beats a guess.
- **`No` only if you looked** at the utility's own site/tariff and found nothing. Unreachable or
  JS-only site → `Unknown`.
- **One row per operating company.** AEP, FirstEnergy, Exelon, Duke, Southern, Xcel, PacifiCorp
  have different tariffs per state jurisdiction.
- **Carry state + EIA ID.** Carroll Electric exists in AR and OH. Southwestern Electric exists
  in IL, NM, and as SWEPCO. Name-only lookups cross-attribute.
- **Search budget ≈ 200 calls.** If you're running low, finish remaining targets as `Unknown`
  with `notes=search budget exhausted`. Don't guess to fill rows.
- `last_verified` = today's date, ISO format.

## 5. Validate before you report

Run the validator (it lives next to this file):

```
python3 .claude/skills/utility-program-research/validate_csv.py <file.csv> --fields <N> [--targets targets.csv]
```

It asserts: every row has exactly N fields; a `source_url` (or `*_src` for every `Yes`) starts
with `http`; `confidence` is one of the three tiers (or legacy H/M/L); and, if a targets file is
given, every target `eia_id` appears exactly once. Fix failures, then re-run until clean.

## 6. Report back

Row count; per-cell or per-category tallies; the RTO breakdown; and a short, honest list of what
you could not verify and why. Do not paste the CSV. If you wrote a `_gaps.md`, say so — it's as
valuable as the data.
