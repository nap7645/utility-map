# Verify: Phase B tariff batches 4, 5, R (2026-10-16)

Independent check of `data/raw/tariffs/{b4,b5,bR}_{tariffs,periods}.csv` against `plans/TARIFF_SCHEMA.md` and each sampled row's `source_url`. 10 downloads (9 sources + FE PA retail tariff for the Penn Power TOU rider and RS delivery cross-check). No data edited.

## Structural checks (all rows, all three batches)

| Check | b4 | b5 | bR |
|---|---|---|---|
| tariffs header == pilot_tariffs.csv (21 cols, same order) | PASS | PASS | PASS |
| periods header == pilot_periods.csv (10 cols, same order) | PASS | PASS | PASS |
| Every row has header column count | PASS | PASS | PASS |
| 12x24 coverage, tier 0, each schedule x day_type, exactly once | PASS (60/60 groups) | PASS (68/68) | PASS (22/22) |
| Higher-tier cells a subset of tier-0 cells | PASS | PASS | PASS |
| Both day_types present for every schedule with periods | PASS | PASS | PASS |
| Orphan period rows (no tariff row) | none | none | none |
| Tariff rows with no period rows | none | none | AEP TX SVC >10 kW, TNMP SS >5 kW, Duke OH DS (all demand-only, logged) |
| "Same period id = same price" (per period + tier) | **FAIL**: 4 schedules reuse period 0 across seasons with different prices (below) | PASS | PASS |
| min_bill numeric (as in pilot, b1-b3) | PASS | PASS | **FAIL (consistency)**: TNMP x3 hold text `customer + metering charge` (should be 7.56 / 8.15 / 17.66); Duke OH x5 hold text (`$8.00 (customer charge)` etc.) |

Period-id reuse in b4 (fix: give the second season its own period id):
- 3916 Cobb R-12 Standard: period 0 tier 1 = 0.09 (Nov-Apr) and 0.125 (May-Oct).
- 3916 Cobb CS-14 Rate 30: period 0 tier 1 = 0.090725 (Nov-Apr) and 0.11229 (May-Oct).
- 10421 KUB RS: period 0 = 0.12513 (Jun-Sep) and 0.12472 (other months).
- 10421 KUB GSA tier 1: period 0 = 0.14399 (Jun-Sep) and 0.14358 (other months).

## Sample: 9 schedules, field accuracy against source

| # | Batch | Schedule | Fixed | Energy rates | Periods / hours | Tiers | Demand | Eff. date | Composition note | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | bR | AEP Texas Central Residential (3278) | PASS $3.24 = $1.27 cust + $1.97 meter | PASS dist $0.032966; trans $0.0000 | PASS flat | PASS none | PASS none | PASS 2024-10-01 (sheet "Bills Rendered on or after October 1, 2024"; compilation Eff Sept 29 2026) | PASS delivery only, riders TC-3/NDC/TCRF/EECRF/DCRF/ITR/SRC/ADFIT/RAR/Mobile TEEEF/RCE listed, not added. Nit: "RCE (CMC credit for small commercial)" is boilerplate; the residential sheet has RCE but no CMC | PASS |
| 2 | bR | TNMP Residential (40051) | PASS $7.56 = $1.70 + $5.86 per ESI ID | PASS dist $0.046020; trans $0.00 | PASS flat | PASS none | PASS none | PASS 2026-09-13, Revision 14 (Page 92) | PASS delivery only; riders SBF/TCRF/DCRF/EECRF/HCRF/RCE/IS match sheet. min_bill is text, not 7.56 (schema consistency) | PASS (min_bill format FAIL) |
| 3 | bR | NorthWestern MT REDS-1 Residential (12825) | PASS $4.20 | PASS $0.15827 incl. tax ('Current Rate Sheet' row 7); reconciles with 'Rate Summary' components: supply 0.062738 + deferred 0.012176 + supply tax 0.005201 + CTC-QF 0.003187 + trans 0.01269 + dist 0.044983 + dist tax 0.012217 + trans tax 0.003062 + BPA -0.002133 + wildfire 0.002815 + USBC 0.001334 = 0.15827 | PASS flat | PASS none | PASS none | PASS blank (sheet dated 2026-10-15, no effective date stated) | PASS bundled supply+delivery+transmission incl. tax; tax $0.02048 = 0.005201 + 0.012217 + 0.003062 | PASS |
| 4 | b4 | KUB RS (10421) | PASS $20.50; min = BSC | PASS 0.12513 summer; 0.12472 winter and transition | PASS Jun-Sep vs rest (billing months) | PASS none | PASS none | PASS 2026-09-01 (PPA 1.442 c/kWh eff 9/1/2026; Resolution 1493 eff 4/1/2026) | PASS bundled, inclusive of current-month PPA | PASS values; **FAIL schema** (period id reuse) |
| 5 | b4 | Cobb EMC R-12 Standard (3916) | PASS $33.00; min $33 + PCA | PASS 0.083 / 0.090 winter; 0.083 / 0.125 summer | PASS Nov-Apr / May-Oct billing | PASS 1000 kWh | PASS none | PASS 2026-01-01 | PASS base only; PCA and taxes excluded | PASS values; **FAIL schema** (period id reuse) |
| 6 | b4 | EPB TRS Time Shift (3408) (choice) | PASS $9.81; min = customer charge | PASS on 0.17744 / off 0.08075, both seasons | PASS wkdy 15-19 Apr-Oct, 6-10 Nov-Mar, weekends off; 6 federal holidays not coded (noted); prevailing Eastern time | PASS none | PASS none | PASS 2024-10-01 ("Effective October 2024") | PASS base charges subject to TVA Adjustment Addendum, fuel adj not coded | PASS |
| 7 | b5 | MGE Rg-2A Residential TOU (11479) | PASS $0.49315/day; min = daily x days | PASS base 0.06255 + 0.07731 = 0.13986; winter P1/P2/P3 0.23632/0.23341/0.23781; summer 0.23656/0.24639/0.24092 (adders 0.09646/0.09355/0.09795, 0.09670/0.10653/0.10106) | PASS P1 10-13, P2 13-18, P3 18-21 Mon-Fri; summer Jun 1-Sep 30; holidays not coded (noted) | PASS none | PASS none | PASS 2026-01-01 (Sheet E-3.3.0, 3270-UR-126) | **FAIL**: note says rates are "per-kWh rates incl. fuel"; the tariff does not say that, and Sheet E-1.3.0 carries a separate fuel cost credit of $0.03561/kWh for Rg-1/Rg-2/Rg-2A (Oct 1-31, 2026; Cg-5 $0.03522) that is neither coded nor mentioned. Rg-1 rows (0.06255 + 0.12178 = 0.18433) are correct as base | FAIL (composition note) |
| 8 | b5 | Penn Power RS Price to Compare (14716) | PASS blank (supply only) | PASS 13.478 c/kWh (incl. 0.01% STAS); GS PTC 13.73 also PASS | PASS flat | PASS none | PASS none | PASS 2026-06-01 | PASS supply only, separate from RS delivery. TOU rider multipliers confirmed (FE PA tariff p.221, Penn Power res 1.6048 / 0.8744 / 0.6512; on-peak 2-9pm M-F, super off-peak 11pm-6am daily) and correctly not coded. "Next reset 2026-12-01" not stated on source (unverified). Note carries delivery-row boilerplate ("distribution charges effective 2025-01-01. Excludes riders...") that does not apply to a supply row. Cross-check RS delivery row: $11.00 + 5.480 c/kWh eff 2025-01-01 PASS | PASS |
| 9 | b5 | CORE A Residential (9336) (choice) | PASS $20.00; min = BSC | PASS $0.11550 all kWh | PASS flat energy | PASS none | PASS $5.47/kW on-peak 60-min, 4-8pm MT all days, year-round | PASS 2026-01-01, Resolution BR25-46 | PASS bundled, net of taxes/franchise fees. Omits WPCA rider (applies to all kWh, quarterly, no fixed value); recommend adding to note. Schema nit: demand in demand_tou_usd_per_kw_p0 but energy period 0 is all hours, so the 4-8pm window lives only in the note | PASS |

## Field accuracy summary

- 9 schedules x 7 fields = 63 field checks. 62 PASS, 1 FAIL (MGE Rg-2A composition note: unmentioned fuel cost credit).
- No dollar-value, hour, tier or date errors found in any sampled row.
- Schema defects: b4 period-id reuse (4 schedules); bR non-numeric min_bill (TNMP 3 rows, Duke OH 5 rows).
- Other observation (not sampled for values): IID (9216) rows are tier Primary, but b5_log says to treat them as page-level pending a tariff PDF; consider tier Secondary or a note flag.

## Fixes recommended (not applied)
1. b4_periods: Cobb R-12 and CS-14 May-Oct rows -> period 1; KUB RS and GSA Jan-May,Oct-Dec rows -> period 1.
2. bR_tariffs: TNMP min_bill -> 7.56 / 8.15 / 17.66; Duke OH min_bill -> numeric customer charge (8.00, 17.50, 8.00, 12.00), DS blank with text kept in note.
3. b5_tariffs MGE (Rg-1, Rg-2A, Cg-5): replace "incl. fuel" with "excludes monthly fuel cost credit/surcharge (Sheet E-1.3.0; Oct 2026 credit $0.03561/kWh residential, $0.03522 Cg-5)".
4. b5_tariffs CORE rows: add "WPCA rider (quarterly, per kWh) not included".
5. Optional: strip delivery boilerplate from Penn Power PTC note; drop "CMC credit" from AEP residential note; reconsider IID tier.
