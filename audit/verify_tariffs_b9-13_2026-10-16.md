# Verify: Phase B tariff batches 9-13 (2026-10-16)

Independent check of `data/raw/tariffs/{b9..b13}_{tariffs,periods}.csv` against `plans/TARIFF_SCHEMA.md` and each sampled row's `source_url`. 10 fetches (all curl + `pdftotext -layout`, all HTTP 200 PDFs). Two further fetches (nhec.com/time-of-day-rates; Blue Ridge "new rate schedules" page) were attempted via WebFetch and failed (tool session limit), so those two claims are UNVERIFIED, not FAIL. No data edited.

## Structural checks (all rows, all five batches)

| Check | b9 | b10 | b11 | b12 | b13 |
|---|---|---|---|---|---|
| Rows (tariffs / periods) | 27 / 157 | 27 / 114 | 11 / 48 | 31 / 155 | 14 / 60 |
| tariffs header == pilot_tariffs.csv (21 cols, same order) | PASS | PASS | PASS | PASS | PASS |
| periods header == pilot_periods.csv (10 cols, same order) | PASS | PASS | PASS | PASS | PASS |
| Every row has header column count | PASS | PASS | PASS | PASS | PASS |
| 12x24 coverage, tier 0, each schedule x day_type, exactly once | PASS (54/54) | PASS (54/54) | PASS (22/22) | PASS (62/62) | PASS (28/28) |
| Higher-tier groups: no duplicate cells | PASS | PASS | PASS | PASS | PASS |
| Both day_types present for every schedule | PASS | PASS | PASS | PASS | PASS |
| Orphan period rows / tariff rows without periods | none / none | none / none | none / none | none / none | none / none |
| One price per (period id, tier) per schedule | PASS | PASS | PASS | PASS | PASS |
| min_bill numeric or blank | PASS | PASS | PASS | PASS | PASS |
| effective_date YYYY-MM-DD or blank; numeric fields numeric | PASS | PASS | PASS | PASS | PASS |

Script: `/tmp/claude-0/-home-claude/d3bb9943-e471-564e-8107-8a9b626f8977/scratchpad/vtb4/struct.py`.

## Sample: 10 schedules, field accuracy against source

| # | Batch | Schedule | Fixed | Energy rates | Periods / hours | Tiers | Demand | Eff. date | Composition note | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | b9 | UNS Electric ERRES (19728) | PASS $17.00/mo | PASS 0.106249 / 0.125626 (delivery-energy + Base Power 0.073258; PPFAC "Varies" excluded) | PASS flat | PASS 0-400 / >400 | PASS none | PASS 2024-02-01 (Decision 79277) | PASS; min_bill blank correct (no minimum stated) | PASS |
| 2 | b9 | Black Hills CO RS-1 (56146) | PASS $8.77 | PASS 0.12159 / 0.15807, same summer/winter | PASS flat | PASS 0-500 / >500 | PASS none | PASS 2025-05-19 (2nd Rev. Sheet 6, C25-0351) | PASS ECA/DSMCA/GRSA excluded and named; CO864 0.13509 not coded; min = customer charge (8.77) PASS | PASS |
| 3 | b10 | Lansing BWL RES1 (10704) | PASS $23.00; min = BSC PASS | PASS on 0.17777 summer / 0.17409 winter, off 0.15040 both | PASS on 13-20 M-F; weekends off; summer Jun-Sep | PASS none | PASS none | PASS 2026-10-01 per sheet ("Proposed", Effective 10/1/2026); Board approval claim from news release not re-fetched | PASS; off-peak shared id 1 across seasons is correct (same price) | PASS |
| 4 | b10 | Turlock ID DT (19281) (choice) | PASS $26.00 (2026 col); min = customer charge PASS | PASS 2026 col: winter 0.2195/0.0987, summer 0.2383/0.1072 | PASS on 12-21 M-F; winter billing months Dec-May, summer Jun-Nov | PASS none | PASS none | PASS 2026-01-01 (2026 column) | PASS; holidays off-peak not coded, disclosed | PASS |
| 5 | b11 | Hawaii Electric Light Schedule R (8287) | PASS $13.14 (1-ph effective) | PASS 0.466365 / 0.504659 / 0.517217 (Effective Rates column) | PASS flat | PASS first 300, next 700 (cum. 1000), over 1000 | PASS none | PASS 2026-09-01 (supersedes 8/1/2026) | PASS; min_bill 28.56 (1-ph) PASS; GIF $1.33 excluded, disclosed. Effective rates include ECRC/PPAC and change monthly (disclosed) | PASS |
| 6 | b11 | Coast Electric 61K Res TOU (3841) (choice) | PASS $1.55/day | PASS on 0.35000, off 0.04100 | PASS summer Apr-Oct 15-18 M-F (HB 3pm-HE 6pm); winter Nov-Mar 6-8 (HB 6am-HE 8am), weekends off | PASS none | PASS $0.75/kW flat (max 15-min) | PASS 2024-01-01 | PASS PCA 13K and tax rider excluded; min_bill blank correct (formula: daily x days + demand) | PASS |
| 7 | b12 | Unitil R delivery (24590) | PASS $16.22 | PASS delivery 0.11372 | PASS flat | PASS none | PASS none | PASS 2026-09-01 | PASS delivery only stated; SBC 0.00778 and stranded (0.00003) excluded, named | PASS |
| 7b | b12 | Unitil R Fixed Energy Service (supply) | PASS blank | PASS 0.12061 (Feb-Jul 2026) / 0.14348 (Aug 2026-Jan 2027) | PASS Feb-Jul / Aug-Jan | PASS none | PASS none | PASS 2026-08-01 (FES period start). Nit: note text says "Effective Sep 1 2026" (copied from delivery row) | PASS; expired Feb-Jul value disclosed | PASS (nit) |
| 8 | b12 | NHEC TDF/TDN Whole-House TOD (13441) | PASS $29.00 Member Service Charge | PASS TDN 0.29736, TDF 0.18064 (Effective Billing Rate = delivery + access + SBC + Co-op Power) | UNVERIFIED on-peak 7-23 M-F (schedule PDF has no hours; nhec.com TOD page fetch failed) | PASS none | PASS none | PASS 2026-08-01 (approved 2026-06-24) | PASS bundled composition matches column sum | PASS (hours unverified) |
| 9 | b13 | Blue Ridge Energy Schedule R 1.1 (1889) | PASS $30.00 (1-ph); min = grid service charge PASS | PASS 4.59+6.73 = 0.1132 (Jun-Oct), 4.59+6.38 = 0.1097 (Nov-May) | PASS flat seasonal | PASS none | PASS none | PASS 2024-10-02 ("bills rendered after October 2, 2024"; same "after" convention as Singing River) | PASS WPCA Factor B excluded. UNVERIFIED: note's claim of new schedules for bills after 2026-11-03 (R $35.00, 4.35c + 7.25/6.87c); page slug says "october-3-2022", fetch failed. If accurate, row expires in ~3 weeks | PASS (note claim unverified) |
| 10 | b13 | Singing River RS-24 (17252) | PASS $35.00 | PASS 0.0948 | PASS flat | PASS none | PASS $1.50/kW (max 1-hr kW) | PASS 2026-10-07 ("bills rendered after October 7, 2026"; supersedes RS-23) | PASS PCA/env/regulatory riders excluded; tariff states no minimum, min_bill blank PASS. Rider values (calculator page) not re-fetched | PASS |

Also checked from fetched UNS ERRES / Unitil PDFs: nothing contradicting the ERREST or TOU-R rows was in scope; not field-audited.

## Summary

- Structure: all checks PASS across b9-b13 (220 tier-0 schedule x day_type groups cover 12x24 exactly once; no period-id price conflicts; headers identical to pilot; min_bill numeric or blank everywhere).
- Sample: 10/10 schedules PASS on every field verifiable from source. No FAIL.
- Unverified (fetch failed, not errors): NHEC TOD hours 7am-11pm M-F; Blue Ridge new-rate effective date (2026-11-03) and values.
- Nits: Unitil FES supply row note says "Effective Sep 1 2026" while effective_date = 2026-08-01 (field is right for supply). Blue Ridge R: if new schedules start with bills after 2026-11-03, re-pull then.
