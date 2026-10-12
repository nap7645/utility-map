# Verify: rule-change (2026-10-12)

Independent verifier. Scope: (A) `scripts/build_presence.py` diff, (B) `scan_AUDIT.csv` refill per `audit/fill_rulechange_2026-10-12.md`, (C) `programs.csv` line 689, plus offline `scripts/audit.py`. No data edited.

## A. build_presence.py

| Item | Result | Evidence |
|---|---|---|
| Derived Yes skips Terminated, `Proposed/pending`, `Closed to new*` | PASS | `if status in ("Terminated","Proposed/pending") or status.startswith("Closed to new"): continue`. Status vocabulary in programs.csv: Active 1180, Closed to new enrollment 67, Pilot 43, Proposed/pending 26, Terminated 11, Closed to new 3; all non-open values are covered. Pilot still counts. |
| Demand-Charge no longer sets ci_habit | PASS | `if cat == "Demand-Charge": ci = False`. Residential demand charge still sets res_habit. This matches RUBRIC "What counts" (a plain C&I demand charge does not count; a residential demand charge counts). |
| Cells backed only by such rows are never inferred No | PASS | A `weak` set collects every non-Terminated HABIT/DISPATCH row's cells, using raw segments before the Demand-Charge override. The inference step requires `c not in weak`. Terminated-only cells can still be inferred No, which is correct. |
| No side effect on dispatch cells beyond the status filter | PASS | The DISPATCH path changes only through the status skip and the weak guard. Comparing HEAD code with the new code on current data, the only dispatch changes are Yes to Unknown/No on Delmarva DE ci, ComEd res, NHEC res and Grant PUD res+ci. Each one is a closed or proposed row, and every resulting No comes from a scan row, not from inference. Across all cells: 17 Yes-to-X changes, 0 No-to-X changes. |
| Undocumented extra change | NOTE | The diff also adds `"ow": ownership_type` to presence.json. It is consumed by `docs/index.html:281` and is harmless, but it was not in the change description. |
| Rebuild matches the state on disk | PASS | The sha256 of `docs/data/presence.json` (db264f23…) and `data/processed/presence.csv` (5c4043de…) is identical before and after `python3 scripts/build_presence.py`. Both files are still uncommitted relative to HEAD, so "committed state" means the working tree here. |

## B. scan_AUDIT refill (cells listed in fill_rulechange report)

Counts: the report states no totals, so there was nothing to reconcile. The table has 18 cells: 9 Yes, 2 No, 7 Unknown. All 18 match `scan_AUDIT.csv`.

| eia / cell | Claim | Result | Evidence (page fetched 2026-10-12) |
|---|---|---|---|
| 5027 res_habit | Yes | PASS | The DE tariff PDF, Leaf 41 R-TOU-ND, shows on/off-peak delivery and SOS rates, and nothing marks it closed. The availability clause was not in the readable text. |
| 5027 ci_habit | Yes | PASS (weak) | The same PDF defines "Hourly Priced Service is a non-residential service for eligible customers" and lists the HPS rider at Leaf 113. The Leaf 113 text itself is not in the fetchable extract, which ends at Leaf 43a. |
| 3828 ci_habit | No | PASS | The Cloverland rates page shows GS1/GS3/LP/LP-Mining with flat energy plus demand only. The 8am-9pm window applies to demand measurement only. |
| 11479 ci_habit | Yes | PASS | The MGE 2026 price sheet lists Cg-4 and Cg-2 as "C&I Time-of-Use" with no closure note. Cg-3 is "Closed to new customers effective Jan. 1, 2021". |
| 18336 ci_habit | Yes | PASS | SWL&P EC5/EP3/EP5 have on-peak (9a-9p weekdays) and off-peak energy rates. No schedule is marked closed. |
| 9273 ci_habit | Yes | PASS | AES Indiana lists Rider 8 Off-Peak Service. The PDF (eff. 2026-07-27) bills 100% demand on-peak (6a-10p weekdays) and 50% on excess off-peak demand. This is a shifting-oriented design, so it counts under RUBRIC. Closure is not stated. |
| 4683 ci_habit | No | PASS | Cuyahoga Falls offers GSS/GSM/GSL/GSD only. On/off-peak is used only to set billing demand, and there is no TOU, interruptible or load-management rate. |
| 1167 ci_habit | Yes | PASS (weak) | supplier.bge.com segmentation doc names GS/GL/GLP/P/T "Time-of-Use". The document is undated and is not the tariff leaf. |
| 16609 ci_habit | Yes | PASS | SDG&E small-commercial table (eff. 2/1/25): TOU-A, TOU-A2, TOU-A3 and TOU-M all have time-differentiated energy prices. |
| 6395 ci_habit | Yes | PASS | Flathead XGS01, IND01 and IRR01 have on/mid/off-peak energy rates (page has the 2026-06-01 increase). The commercial peak hours are not defined on the page. |
| 9336 ci_habit | Yes | PASS | CORE Rates & Regulations Jan 2026: the Optional TOU Rider is "available to existing and new Consumers" on SG1/SG3/I/C/S/LPS. ET and FPT are frozen. |
| Unknown cells (5027 ci_dispatch, 4110 res_dispatch, 3762, 15270 x2, 11171, 6958) | Unknown | PASS | Unknown is never counted as a miss. The stated reasons are consistent. |

### Additional findings in scan_AUDIT (outside the report table)

| Item | Result | Evidence |
|---|---|---|
| Delmarva DE (5027) res_dispatch, Energy Wise Rewards paused? | CONFIRMED paused / FAIL on data | energywiserewards.delmarva.com/de-enroll says: "we are pausing the program on May 31, 2026 while the Delaware Public Service Commission reviews proposed changes." programs.csv:269 correctly has `Closed to new`. However, `scan_AUDIT.csv` row 5027 sets **res_dispatch=Yes**, sourced to a 2018 EWR T&C PDF. The scan therefore refills the cell to Yes and presence.csv shows Yes, which contradicts the refill agent's own note and the rule change. It should be Unknown (or No, if no other DE device-control program is open; the DLC 2.0/BYOD programs in PSC Docket 25-1554 are proposed only). |
| ComEd (4110) ci_habit = No | FAIL (pre-existing) | `scan_AUDIT.csv` writes ci_habit=No with no src, although its own note says comed.com is unreadable, which violates the schema rule "No only when you looked". ComEd offers Rate BESH hourly (wholesale-indexed) pricing to commercial customers (comed.chooseev.com/commercial/faq), which is RTP and counts as C&I time-based. The value was already No at HEAD. Should be Yes. |

## C. programs.csv:689 (PowerShare Storage, SC)

| Item | Result | Evidence |
|---|---|---|
| eligible_assets=Battery, storage_eligible=Yes | PASS | The cited Duke release (2026-05-27) covers a "qualifying energy storage system" and "battery storage systems". The values ($120/kW, +$30/kW renewable-charged, $3.50/kW-mo, $0.10/kWh) and the nonresidential segment match. The launch is August 2026; the Active status is plausible as of 2026-10-12. |
| Attribution to Duke Energy Carolinas, LLC | FLAG (unsupported) | The cited release, investors.duke-energy.com, theenergymag.com and energiesmedia.com all say only "Duke Energy" in South Carolina, which DEC and DEP both serve. No fetched page names DEC. The SC PSC DMS filings (Docket 2026-138-E, "Initial Comments of DEC and DEP") are robots-blocked. The program likely applies to both DEC and DEP, so the row should carry both utilities (or a DEP twin row) once the PSC docket confirms it. Confidence is Secondary as written. |

## Offline audit (`python3 scripts/audit.py`)

| Check | Result | Note |
|---|---|---|
| A1 | FAIL | 5 ERCOT TDUs (Oncor, CenterPoint, TNMP, AEP TX Central/North) have empty `customers` in hifld_over10k.csv. This is identical at HEAD, already known, and not caused by this change. |
| A2, A3, A4, A5, A7, A8 | PASS | 993 targets, 0 missing; 0 unjoined; 0 cross-state; 0 Yes without a URL; 0 OTHER; 49/49 states covered. |
| A6 | NOT RUN | Offline. |

## Verdict
(A) PASS. (B) PASS on all 18 cells in the report table, but 2 defects in the same file: Delmarva DE res_dispatch=Yes (program paused) and ComEd ci_habit=No (Rate BESH exists). (C) Asset fields PASS; the DEC-only attribution is unsupported.
