# Verify: Phase B tariff batches 6, 7, 8 (2026-10-16)

Independent check of `data/raw/tariffs/{b6,b7,b8}_{tariffs,periods}.csv` against `plans/TARIFF_SCHEMA.md` and each sampled row's `source_url`. 10 fetches (8 curl + 1 HTML curl + 1 WebFetch for anaheim.gov, which returns a Cloudflare page to curl as logged). No data edited.

## Structural checks (all rows, all three batches)

| Check | b6 | b7 | b8 |
|---|---|---|---|
| tariffs header == pilot_tariffs.csv (21 cols, same order) | PASS | PASS | PASS |
| periods header == pilot_periods.csv (10 cols, same order) | PASS | PASS | PASS |
| Every row has header column count | PASS | PASS | PASS |
| 12x24 coverage, tier 0, each schedule x day_type, exactly once | PASS (50/50 groups) | PASS (50/50) | PASS (40/40) |
| Higher-tier groups have no duplicate cells | PASS | PASS | PASS |
| Both day_types present for every schedule with periods | PASS | PASS | PASS |
| Orphan period rows (no tariff row) | none | none | none |
| Tariff rows with no period rows | none | none | Dakota Electric `46 General Service (demand)` (kW-blocked energy, logged) |
| Same period id + tier = same price | PASS | PASS | PASS |
| Same price split across several ids (info) | none | none | none |
| min_bill numeric or blank | PASS | PASS | PASS |
| effective_date YYYY-MM-DD or blank | PASS | PASS | PASS |

## Sample: 9 schedules, field accuracy against source

| # | Batch | Schedule | Fixed | Energy rates | Periods / hours | Tiers | Demand | Eff. date | Composition note | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | b6 | Duke Energy Kentucky RS (19446) | PASS $14.75 | PASS $0.126104 all kWh | PASS flat | PASS none | PASS none | PASS 2026-01-02 (21st Rev. Sheet 30, Case 2025-00024) | PASS base only; ESM/DSMR/FAC/PSM riders listed, not added; min charge = customer charge (min_bill 14.75 PASS); no res TOU/EV in index confirmed (only DT/TT) | PASS |
| 2 | b6 | Lakeland RSX-1 Shift to Save (10623) | PASS $15.25 | PASS on 0.14904, off 0.01678 | PASS Apr-Oct M-F 12-21; Nov-Mar M-F 6-10,18-22; weekends off (sheet "6:01-10:00" etc. = hour-ending, coded 6-10 correctly) | PASS none | PASS none | PASS 2026-10-01 | PASS fuel 0.057387/0.042488 TOU and env 0.0018506 listed, excluded. Nit: min_bill blank here while RS row = 15.25 on the same sheet (sheet states no min for either; RS value comes from tariff Sheet 7.0) | PASS |
| 3 | b6 | Connexus Residential Time-of-Day (689) | PASS $16.50 | PASS 0.2250 / 0.1330 / 0.0725 | PASS peak 16-20 M-F; int 8-16 M-F, 8-20 Sat/Sun; off rest | PASS none | PASS none | PASS 2026-01-01 (Rev. 8, 12-11-2025) | PASS PCA rider + surcharge rider noted, not added; holidays = weekend pattern (not coded) | PASS |
| 4 | b7 | Anaheim TOU-2 (590) | PASS $8.00; min = customer charge PASS | PASS summer on 0.3320 / off 0.1665; winter on 0.3125 / off 0.1615 / super-off 0.1200 | PASS summer Jul-Oct; on 16-21 weekdays; winter super-off 8-16 weekdays, 0-16 & 21-24 weekends; weekend 16-21 winter = off-peak (correct) | PASS none | PASS none | PASS 2024-05-01 (Res. 2024-022) | PASS RSA (PCA on kWh >10/day, EMA all kWh) noted, not included | PASS |
| 5 | b7 | Modesto EV-D pilot (12745) | PASS $32.00 | PASS winter on 0.22401, partial=off 0.14324; summer on 0.31235 / partial 0.20192 / off 0.14513 | PASS on 17-20 M-F, partial 13-17 & 20-23 M-F, weekends off; summer May-Sep | PASS none | PASS none | **FLAG** coded 2026-07-01 from footer "Revised 7/01/26"; the sheet's only "Effective" line is January 1, 2025 (D row uses 2025-01-01 from same convention). Disclosed in note; recommend 2025-01-01 for consistency | PASS bundled, CARES/experimental status noted | PASS (eff. date flag) |
| 6 | b7 | Great Lakes Energy A (38084) | PASS $50.05 ($15.98 add'l meter noted) | PASS $0.14742 | PASS flat | PASS none | PASS none | PASS 2025-11-01 (bills on/after; issued 2026-04-14) | PASS EO surcharge $0.00316/kWh (D-2.10) and PSCR excluded, listed. Nit: note says "Power Cost Recovery"; tariff term is PSCR. min_bill 50.05 = Monthly Charge PASS | PASS |
| 7 | b8 | Chugach Residential South (3522) | PASS $12.79 | PASS 24.2488 c = 0.242488 (16.182+5.095+1.662+0.128+0.929+0.1338+0.069+0.05) | PASS flat | PASS none | PASS none | PASS 2026-10-01 ("in effect as of October 1, 2026") | PASS all-in total, component list matches page; 2% Anchorage undergrounding excluded | PASS |
| 8 | b8 | Delaware EC R (5070) | PASS $28.00; min = service charge PASS | PASS 0.0214+0.000178+0.1016-0.0015 = 0.121678 (first 700); 0.101678 (over 700) | PASS flat, 12-month rate | PASS tier 0 max 700, tier 1 unlimited | PASS none | PASS 2024-07-01 (meter readings on/after) | PASS delivery+RRF+supply+PCA summed as stated | PASS |
| 9 | b8 | Riverside D-TOU (16088) | PASS $14.93 (2026 col) | PASS all 10 2026 values (winter 0.1728/0.2764, 0.1382/0.2212, off 0.1253; summer 0.2304/0.3686, 0.1497/0.2395, off 0.1253) | PASS summer Jun-Sep on 14-19, mid 6-14 & 19-23; winter on 16-21, mid 6-16 & 21-23; off 23-6; every day | PASS 135/250 winter, 330/550 summer; off-peak tiers identical price, coded untiered (OK) | PASS none | PASS 2026-01-01 (2026 column; sheet adopted eff. 2024-01-01) | PASS reliability/network charges and renewable adder in note; min_bill blank justified (customer+reliability+network varies). Nit: Public Benefits Charge surcharge (Special Cond. 4) not mentioned | PASS |

## Summary

- Structure: all checks PASS across b6/b7/b8 (140 tier-0 groups covered 12x24 exactly once; no period-id price conflicts; min_bill numeric or blank everywhere).
- Sample: 9/9 schedules PASS on fixed charge, energy rates, hours, tiers, demand, composition. One effective-date flag (Modesto EV-D: 2026-07-01 revision date vs stated "Effective January 1, 2025"; disclosed in note).
- Nits (no data error): Lakeland RSX-1 min_bill blank vs RS 15.25; Great Lakes "PCR" should read "PSCR"; Riverside note omits Public Benefits Charge.
