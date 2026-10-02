# Independent verification: scripts/audit.py + audit/RUBRIC.md (2026-10-02)

Verifier did not author either file. All mutations ran on a scratch copy; nothing under the repo was modified except this report.
Harness: copy of the repo, one fault per run, restore from a pristine copy between runs, parse the result table.

Baseline on real data: A1 FAIL (6), A2-A5 PASS, A6 NOT RUN, A7 PASS (0/993 OTHER), A8 PASS (49/49 states, 983/983 targets). Exit 1.

## 1. Spec conformance (SPEC 6.2 automated checks)

| SPEC check | ID | Verdict | Notes |
|---|---|---|---|
| Every row passes validation | A1 | Partial | Row field count (short/long rows), confidence tier on all 4 CSVs, presence Yes/No/Unknown, rto, ownership, last_verified date, programs customer_segment, denominator customers. **Missing: header column count** (`nf` is passed at l.66-67 but never used; merge_region.validate does check it). Adding a 23rd column to programs.csv passes A1; renaming a column crashes the script with KeyError instead of FAILing. No enum checks on programs status/category or ic_state focus cells (the project's own validator doesn't check those either, so this is acceptable). |
| Every target territory has a presence row | A2 | Faithful | Checks docs/data/presence.json (what the map reads) against the denominator; duplicates checked in presence_scan.csv. Doesn't check that presence_scan.csv itself covers the targets, so a stale presence.json can hide a CSV gap (101 presence.json rows are derived from programs by design). |
| Every program/IC utility name joins a boundary | A3 | Partial | Joins by norm(name) only. It ignores JOIN_EXCLUDE and the `(XX)` suffix rejection that progsFor() applies, so a name whose only matching polygon is rejected by the map still passes. Demonstrated below (M-x2). |
| No cross-state name joins | A4 | Partial | FAILs only when one payload entry attaches to more than one polygon in different states. A **single** wrong-state join (one polygon, other state, no suffix) is only info/WARN, so it passes. Demonstrated below (M-x1). It also uses `alt_states` in the suffix test, but JS progsFor() (index.html:230) uses `u.state` only. No live divergence today; this is latent. |
| Every Yes has a URL | A5 | Faithful | presence_scan Yes cells, plus every programs/ic_state/ic_util row. presence.json-derived Yes cells aren't checked; independently verified: 0 Yes without URL there. |
| Link check >=95% non-4xx | A6 | Faithful, stricter than spec | It counts 5xx and network errors as failures. SPEC literally says "non-4xx", so 5xx and ERR would count as passing. 403/429 are reported separately. Code issues are listed in section 3. |
| Every territory has a governing body | A7 | Partial | Gates on **target** territories only. 10 non-target polygons resolve to OTHER and are reported but don't fail. The rtoOf() mirror diverges in two ways: (1) STATE_FIX isn't applied (index.html:693-694 rewrites STATE before rtoOf). Polygon 219 ALASKA POWER AND TELEPHONE gives OTHER in the audit but AK-islanded in the UI (non-target, so no effect on the result). (2) PRES comes from presence_scan.csv, but the UI uses presence.json. No output difference today; this is latent. |
| Polygon layer covers 100% of lower 48 | A8 | Partial (documented proxy) | It checks that every state has a polygon and every target has a polygon. There is no geometric coverage or gap test (needs a land mask), and the script says so. |

### RUBRIC.md vs SPEC 6.2

| Item | SPEC | RUBRIC | Match |
|---|---|---|---|
| Presence cells sample | ~5%, min 20 | ~5%, min 20 | Yes |
| Program rows sample | ~10%, min 15 | ~10%, min 15 | Yes |
| State interconnection | every row's 2 focus cells | every state, 2 focus cells | Yes. RUBRIC adds a "100%" bar that SPEC doesn't state. |
| Top-10 by customers | 100% | 100% of their rows and cells | Yes |
| Yes bar | >=95% | >=95% | Yes |
| No bar | >=90% | >=90% | Yes |
| $ among top-10 | 0 wrong | 0 wrong | Yes |
| Program-row field bar | not in SPEC | "<=1 in 10 other rows with any wrong field" | Added bar (not in SPEC) |
| Stratified sampling | "Stratified random samples" | "random sample (seeded)" | **Missing stratification** (state × ownership, say) |
| Errors | "every error logged and fixed" (in addition to bars) | Sec. 4: "passes only when every bar is met **or** every miss is fixed" | **Weaker than SPEC.** It should be "every bar met **and** every logged error fixed". |

## 2. Mutation tests

| # | Fault injected | Expected | Result |
|---|---|---|---|
| a | presence_scan eia 20996 res_dispatch=Maybe | A1 | **Caught but masked**: A1 was already FAIL, and its count went from 6 to 7 problems. With the 6 blank denominator customers patched on the copy, A1 went from PASS to FAIL (1 problem). |
| b | delete presence.json key 13519 | A2 | Caught (A2 FAIL, 1 missing) |
| c | programs "Conway Corp" renamed to nonexistent | A3 | Caught (A3 FAIL, 1 unjoined) |
| d | duplicate ALLETE, INC. polygon with STATE=NV, no suffix | A4 | Caught (A4 FAIL, 1 ambiguous join) |
| e | presence eia 10697 ci_habit=Yes, src blank | A5 | Caught (A5 FAIL) |
| f | KENTUCKY UTILITIES CO (10171; resolved via CNTRL_AREA=LGEE, no presence-scan rto) CNTRL/PLAN set to NOT AVAILABLE | A7 | Caught (A7 FAIL, 1 OTHER) |
| g | remove all 17 VT polygons | A8 | Caught (A8 FAIL, 48/49 states, 4 targets without polygon). A3 also failed (3 VT names unjoined), which is expected. |
| h | programs line 4 confidence=Maybe | A1 | **Caught but masked**, same as (a): count went from 6 to 7. With the denominator patched, A1 went from PASS to FAIL. |
| x1 | ALLETE, INC. polygon STATE MN->NV (single join, no duplicate) | A4 | **MISSED**: A4 PASS. The join only shows up as a 17->18 info line. |
| x2 | programs row renamed to "City of Newark" / NJ (the only polygon is "CITY OF NEWARK - (DE)", which progsFor rejects) | A3 | **MISSED**: A3 PASS. On the map this row joins nothing. |
| x3 | programs.csv gets a 23rd column (header + rows) | A1 | **MISSED**: A1 count unchanged (6) |
| x4 | rename programs.csv header customer_segment | A1 | **Crash** (KeyError traceback) instead of a FAIL line |

`python3 scripts/audit.py --links --limit 20` on the copy ran without crashing and wrote audit/linkcheck.csv (20 rows). Result: 6 x 403 (http:// URLs, likely the sandbox proxy) and 14 x ERR URLError, because the sandbox has no egress to arbitrary hosts. That gives A6 FAIL at 0%, which is expected here and says nothing about the URLs.

### A1 baseline FAIL is a true finding, not a script bug
data/raw/hifld_over10k.csv has blank `customers` for 15270 POTOMAC ELECTRIC POWER CO (DC), 44372 ONCOR, 8901 CENTERPOINT, 40051 TEXAS-NEW MEXICO POWER, 3278 AEP TEXAS CENTRAL and 20404 AEP TEXAS NORTH.
- The 5 TX utilities carry the HIFLD -999999 sentinel in the geojson, so the source data really is missing.
- Pepco is a **denominator build defect**: the geojson has CUSTOMERS=927660 but the CSV is blank.
- Consequence beyond A1: the RUBRIC's "top-10 by customers" draw for PJM/ERCOT will silently drop Pepco, Oncor and CenterPoint if it's taken from this CSV. A8's "% of target customers" also counts them as 0.
- Fix: backfill Pepco from the geojson, and the 5 TX TDUs from EIA-861 (sales_ult_cust).

## 3. Bugs / fixes (scripts/audit.py)

1. **l.66-71 `nf` unused.** Header column count isn't validated (x3 missed), and a renamed column crashes (x4). Fix: read with csv.reader, then `if len(hdr)!=nf: probs.append(...)` and skip that file's per-row checks; access fields with `.get()`.
2. **l.167 A4 single-polygon cross-state joins pass (x1).** Fix: FAIL when an unsuffixed hit's STATE_FIX'd state isn't in `{u.state}`. Allowlist the 17 reviewed HQ-state cases in a crosswalk file (or extend STATE_FIX) so they don't fail.
3. **l.157-164 A4 uses alt_states; JS progsFor uses u.state only.** Make the two identical: drop alt_states here, or add alt_states to progsFor.
4. **l.126-134 A3 ignores progsFor rejection (x2).** Fix: only count a hit if the polygon ID isn't in JOIN_EXCLUDE and its `(XX)` suffix is absent or matches the row's state.
5. **l.199-209 rto_of mirror.** Apply `STATE_FIX` to p["STATE"] before the AK/HI tests, and build `pres_by_id` from docs/data/presence.json (the UI's PRES) instead of presence_scan.csv.
6. **l.264-280 check()** has several problems:
   - (a) `time.sleep(0.05)` (l.279) and `return url,"ERR"` (l.280) are unreachable, because every path returns inside the loop. As a result there is no per-host delay at all, only a concurrency cap of 2.
   - (b) `defaultdict(lambda: Semaphore(2))` is accessed from 24 threads, and `__missing__` isn't atomic, so two threads can get different semaphores for the same host. Fix: pre-create the semaphores for `{urlparse(u).netloc for u in items}` before starting the pool, or guard creation with a Lock.
   - (c) A HEAD returning 5xx (500/502/503 are common for HEAD-hostile servers) or 401 isn't retried as GET. Retry GET on any HEAD HTTPError.
   - (d) Add a real throttle: sleep about 0.5 s while still holding the host semaphore, after each request.
7. **l.284 `--limit` takes the alphabetical first N.** That biases the smoke sample (the http:// and 3cenergy URLs first). Use `random.Random(seed).sample`.
8. **l.291-296 A6 counts 5xx/ERR as failures.** This is stricter than SPEC's "non-4xx". Either keep it and state the stricter rule in RUBRIC sec. 0, or report both rates and gate on the SPEC definition.
9. **l.4 docstring says it writes `audit/AUTOMATED_<date>.md`, but l.319 writes AUTOMATED_latest.md** (overwritten on every run, no history). Fix the docstring, or write both files.
10. **RUBRIC.md** has three issues:
    - Sec. 1 should say "stratified (state × ownership)".
    - Sec. 4 should read "and every logged error fixed".
    - The program-row "<=1 in 10" bar and the interconnection "100%" bar should be marked as additions to SPEC or removed.
