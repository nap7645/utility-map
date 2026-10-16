# Verify: presence rescan applied 2026-10-15

Independent verifier. Inputs: `audit/rescan/applied_2026-10-15.json` (268 decisions), `audit/rescan/batch_1..6.csv` (299 raw answers), `audit/rescan/rescan_1..6.json` (299 targets), `data/raw/presence_scan/scan_AUDIT.csv`, `docs/data/presence.json` vs `HEAD`. Rubric: `audit/RUBRIC.md` "What counts". 34 web fetches. Nothing in the repo was edited except this file.

## 1. Policy (b): TVA PowerFlex dropdown = participating LPC -> FAIL

Fetched https://energyright.com/business-industry/demand-response/powerflex/ (2026-10-15):

- The "Local Power Company" dropdown has 154 options: "TVA Direct Serve Customer" plus 153 LPCs. That is the whole TVA LPC roster. It includes every LPC checked (Dayton, Dickson, Benton County, Bolivar, NES) and also Bowling Green, Cullman EC and Starkville.
- The page has no open or closed status, no LPC opt-in list and no availability caveat. Eligibility is contract demand of at least 1 MW with at least 500 kW average on-peak interruptible demand. It describes the program as "from TVA EnergyRight and your local power company".
- For comparison, the TVA Smart Thermostat Rewards page (greatergrid.com LPC FAQ) does publish an opt-in list, and it has only 63 LPCs. TVA programs do vary by LPC, and TVA publishes the list when they do.

Verdict: FAIL. A listing in a dropdown that contains every LPC says nothing about any one LPC, so it does not show that the program is open to that LPC's C&I customers. Batch 6 was right: the page names no participating LPCs. Under the rubric ("a currently open program naming this utility"), these cells should be Unknown. The other option is to treat PowerFlex as a uniform TVA-wide program-level source, applied the same way to all 153 LPCs and labelled as program-level. Today these cells are Yes for some LPCs and something else for others, which is not consistent.

Cells affected: the 25 ci_dispatch cells where batch 6 said Unknown but Yes was kept (11222, 11789, 12293, 12330, 12470, 12988, 13027, 13550, 13933, 14455, 15016, 15141, 15293, 15507, 16223, 16930, 16949, 17047, 17694, 18643, 19162, 19266, 19574, 19898, 20228), plus the batch 1 and 5 Yes cells that rest on the same dropdown (for example 241, 1578, 1936, 4920, 5148). These 25 plus 6 SKIP rows in batch 2 account for the 31 targets missing from `applied_2026-10-15.json` (299 - 268).

## 2. Sample check

The sample covers all 13 applied No->Yes, all 9 applied Yes->No, 10 random applied No->Unknown, and 5 random batch-5 Yes->Yes. The random draws used `random.Random(11).sample` over the list sorted by (eia_id, cell).

| # | group | eia_id | utility | cell | applied | verdict | evidence / note |
|---|---|---|---|---|---|---|---|
| 1 | No->Yes | 11479 | MGE (WI) | res_dispatch | Yes | AGREE | thermostatrewards.com/ss/mge: MGE adjusts thermostats, Jun-Sep, live sign-up form |
| 2 | No->Yes | 20997 | Yellowstone Valley EC (MT) | res_habit | Yes | AGREE | Residential demand $2.00/kW. Caveat: applies to net-metering accounts only. The rubric counts a residential demand charge. |
| 3 | No->Yes | 3245 | Central Florida EC | ci_habit | Yes | AGREE | FL PSC 07014-2025: GST optional TOU, bills on or after 7/1/2025, not closed |
| 4 | No->Yes | 3245 | Central Florida EC | res_habit | Yes | AGREE | Same filing: RST optional residential TOU |
| 5 | No->Yes | 3660 | Clark Public Utilities (WA) | res_dispatch | Yes | AGREE | Optiwatt-managed EV charging events, pilot through 2026, 1,400-EV cap |
| 6 | No->Yes | 3687 | Clark Energy Coop (KY) | res_habit | Yes | AGREE | Schedule D off-peak marketing rate for Rate R, effective 5/1/2026 |
| 7 | No->Yes | 3757 | Clay Electric (FL) | ci_dispatch | Yes | AGREE | Rate INT/INT-T, 500 kW minimum, effective 1/1/2022, not closed |
| 8 | No->Yes | 3757 | Clay Electric (FL) | ci_habit | Yes | AGREE | GST/GSDT-LM/LGSDT-LM TOU schedules are in the rate book. The availability text did not extract. |
| 9 | No->Yes | 3757 | Clay Electric (FL) | res_habit | Yes | AGREE | Rate RT optional residential TOU, first-come first-served, effective 1/1/2023 |
| 10 | No->Yes | 4622 | Cumberland Valley Electric (KY) | res_habit | Yes | AGREE | Schedule I TOD, open to all eligible residential, effective 5/1/2026 |
| 11 | No->Yes | 6194 | Farmers RECC (KY) | res_habit | Yes | AGREE | Schedule R TOD Residential is in the current tariff (sheet effective 10/16/2014). No closure language. |
| 12 | No->Yes | 7646 | Greenwood CPW (SC) | res_habit | Yes | AGREE | E-EV Rate 2500, residential EV on/off-peak, effective 1/1/2026 |
| 13 | No->Yes | 9292 | Inter-County Energy (KY) | res_habit | Yes | AGREE | Schedule 1-A ETS off-peak marketing rate, effective 5/1/2026 |
| 14 | Yes->No | 11501 | Magic Valley EC (TX) | res_habit | No | AGREE | Flat $0.09187/kWh only |
| 15 | Yes->No | 12929 | South Central Indiana REMC | ci_dispatch | No | AGREE | Rates list of 21 schedules has no C&I interruptible or DR |
| 16 | Yes->No | 13216 | Nashville Electric Service | res_habit | No | AGREE | Residential and Supplemental only. TGSA/EVC are commercial. presence.json still shows Yes (see section 3). |
| 17 | Yes->No | 19293 | Southeastern Electric (SD) | res_habit | No | AGREE | Rate 310 tiered flat. The water-heater credit is DLC, which is dispatch. |
| 18 | Yes->No | 2056 | Bowling Green MU (KY) | res_dispatch | No | AGREE | Not on the 63-LPC Smart Thermostat list. The programs page lists no DR. |
| 19 | Yes->No | 3660 | Clark Public Utilities (WA) | res_habit | No | AGREE | Flat 8.79 c/kWh. EV managed charging is a credit-based control program, not a rate. presence.json still shows Yes (section 3). |
| 20 | Yes->No | 4618 | Cullman EC (AL) | res_dispatch | No | AGREE | Not on the 63-LPC list. The savings page has no DR. |
| 21 | Yes->No | 5394 | Dubois REC (IN) | ci_dispatch | No | AGREE | The LPS page has no interruptible or DR option |
| 22 | Yes->No | 689 | Connexus Energy (MN) | ci_habit | No | **DISAGREE -> Yes** | Business rate book Section III has an Off-Peak General Commercial Service Rider (on-peak weekday afternoons and evenings), a General Commercial Peak Period Rate, Controlled Off-Peak Energy Storage (C&I) and an EV Fleet pilot (peak/intermediate/off-peak). None is marked closed. The agent did not read the rate book. |
| 23 | No->Unk | 3266 | Central Maine Power | res_dispatch | Unknown | AGREE | The home page shows no DR. DR in Maine runs through Efficiency Maine, not CMP. |
| 24 | No->Unk | 6616 | Fort Pierce UA (FL) | res_dispatch | Unknown | AGREE | The rates page mentions no DR. The rate PDFs were not shown. |
| 25 | No->Unk | 3828 | Cloverland EC (MI) | res_dispatch | Unknown | AGREE | The rates page has a residential demand rate (habit) but no DR. Rate Book Part 3 is blocked by robots. |
| 26 | No->Unk | 9617 | JEA (FL) | res_dispatch | Unknown | AGREE | jea.com serves a human-verification wall |
| 27 | No->Unk | 6442 | Fleming-Mason (KY) | res_habit | Unknown | CANNOT_TELL | Policy (a) was applied correctly. Sibling EKPC co-ops (Clark, Cumberland Valley, Inter-County) all have TOD/ETS sheets reissued effective 5/1/2026, so a successor RSP-TOD is likely and this is probably Yes. The current Tariff.pdf fetch failed. |
| 28 | No->Unk | 6909 | Gainesville RU (FL) | res_habit | Unknown | AGREE | The cited PDF now returns 403/404. Only GS TOU was evidenced. |
| 29 | No->Unk | 18336 | Superior WL&P (WI) | ci_dispatch | Unknown | CANNOT_TELL | Not fetched. The source is a third-party aggregator, so No was unsupported either way. |
| 30 | No->Unk | 18006 | Starkville Electric (MS) | res_habit | Unknown | AGREE | No source. A No without the utility's own page is not allowed. |
| 31 | No->Unk | 7264 | Glades EC (FL) | res_habit | Unknown | AGREE | The 2021 PSC filing has only GS/LP/pump sheets |
| 32 | No->Unk | 40302 | NE Mississippi EPA | res_habit | Unknown | AGREE | No source |
| 33 | Yes kept | 4920 | Dayton Electric Dept (TN) | ci_dispatch | Yes | CANNOT_TELL | PowerFlex dropdown only (section 1) |
| 34 | Yes kept | 5763 | Elizabethton Electric (TN) | res_dispatch | Yes | AGREE | On the 63-LPC Smart Thermostat list |
| 35 | Yes kept | 9777 | BrightRidge (TN) | res_dispatch | Yes | AGREE | On the 63-LPC list |
| 36 | Yes kept | 5148 | Dickson Electric System (TN) | ci_dispatch | Yes | CANNOT_TELL | PowerFlex dropdown only (section 1) |
| 37 | Yes kept | 5399 | Duck River EMC (TN) | res_dispatch | Yes | AGREE | On the 63-LPC list |

**Agreement: 32 AGREE, 1 DISAGREE, 4 CANNOT_TELL. That is 32/33 = 97% of the cells that could be decided, and 32/37 = 86% of the sample.** By group:

- No->Yes: 13/13
- Yes->No: 8/9
- No->Unknown: 8/10 (2 CANNOT_TELL)
- Yes kept: 3/5 (2 CANNOT_TELL because of the PowerFlex policy)

### Disagreements and wrong values

| eia_id | cell | applied | correct | why |
|---|---|---|---|---|
| 689 Connexus Energy | ci_habit | No | **Yes** | Off-Peak General Commercial Service Rider and General Commercial Peak Period Rate are in rate book Section III (connexusenergy.com/download_file/view/d1a05b74-92f4-4884-9682-8e0047752047) |
| 689 Connexus Energy | ci_dispatch (not in sample) | Unknown in presence.json | **Yes** | The same rate book has a Partial Interruptible Credit Rider (curtail at least 100 kW). The No->Unknown change came from the defect fixlog, not from this rescan. |
| 4920, 5148 and all PowerFlex-only ci_dispatch Yes | ci_dispatch | Yes | **Unknown** (or a uniform program-level value for all TVA LPCs) | Section 1 |

## 3. Integrity

| check | result |
|---|---|
| `scan_AUDIT.csv` line endings | PASS. LF only: 0 CRLF in HEAD (33 lines) and 0 CRLF now (217 lines). Trailing newline is present in both. |
| `scan_AUDIT.csv` merged | PASS. `merge_region.py --tag AUDIT` dry run reports "216 already merged, 0 new, 0 updated". All 4 cells of the 216 rows match `presence_scan.csv`. |
| `presence.json` rebuilt | PASS. `build_presence.py` run in a scratch copy produces a `docs/data/presence.json` and a `presence.csv` that are byte-identical to the working tree. |
| `audit.py` offline | PASS. A1-A5 and A7-A8 pass. A6 (link check) not run because it needs network. The generated `AUTOMATED_latest.md` is identical to the committed one. |

### Why 23 Yes->Unknown shows as 21, and 9 Yes->No shows as 6

`build_presence.py` lets a scan fill only cells that are not already Yes from `programs.csv`. A Yes derived from a programs.csv row is never overridden. Five applied downgrades are blocked this way:

| eia_id | utility | cell | applied | presence.json | blocking programs.csv row |
|---|---|---|---|---|---|
| 5070 | Delaware Electric Coop | ci_dispatch | Unknown | Yes | "Beat the Peak", DR-Curtailment, segment All, Active (delaware.coop/btp) |
| 9576 | Jackson County REMC | res_dispatch | Unknown | Yes | "Smart Thermostat DR Pilot (with Hoosier)", DR-BYOT, status Pilot (Hoosier Energy news item) |
| 689 | Connexus Energy | ci_habit | No | Yes | "Controlled Off-Peak Energy Storage (C&I)", TOU-Rate, source nectarclimate.com. The Yes is correct (section 2) but rests on a third-party source. |
| 13216 | Nashville Electric Service | res_habit | No | Yes | "Time-of-Use Rate", segment Residential;SmallC&I;LargeC&I. The segment is wrong: TOU is TGSA (commercial) only. |
| 3660 | Clark Public Utilities | res_habit | No | Yes | "EV Managed Charging Program (pilot)" is tagged EV-Rate but is a control program, so it should be DR-BYOD. |

So 23 - 2 = 21 and 9 - 3 = 6. The coordinator's guess ("programs-derived Yes?") is correct. However, the target files mark only 9576 and 689 as `from_programs: true`. They mark 5070, 13216 and 3660 as `false`, so that flag is unreliable. To make these decisions take effect, fix the programs.csv rows:

- 13216: change the segment to C&I.
- 3660: recategorize to DR-BYOD. The res_dispatch Yes stays.
- 5070 and 9576: re-verify the row's status.

Changes in presence.json that are not part of this rescan: HEAD to current also includes 9 No->Yes, 4 Yes->No (3940, 19547, 8287, 11843), 5 Yes->Unknown, about 97 No->Unknown and 1 Unknown->Yes. All of these eia_ids appear in `audit/fixlog_defects_2026-10-15.json`, and the No->Unknown bulk is consistent with `INFER_NO = False`. They were not verified here.
