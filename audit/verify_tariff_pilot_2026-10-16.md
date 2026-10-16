# Verify: tariff pilot rows, SMUD (16534), Ameren Missouri (19436), SCE (17609) sample, 2026-10-16

Independent check of `data/raw/tariffs/pilot_tariffs.csv` and `pilot_periods.csv` against each row's `source_url`, fetched with WebFetch on 2026-10-16. No data edited. 14 fetches/searches in total. curl to these hosts was blocked by the proxy (403), so I read the values from WebFetch text extraction, not from raw PDF text.

## Result

**Field accuracy: 98/101 = 97.0%.** Every price, fixed charge, demand value, hour window, tier boundary and effective date matches the source. All 3 failures are classification or structure problems, not wrong numbers:

1. **Ameren 1(M) default flag is backwards.** Sheet 54.4 says: "New customers or new accounts with an advanced meter, or existing accounts that have had an advanced meter for six months, shall be placed directly on the Evening/Morning Saver rate". Sheets 54.4 and 54.7 also call it "the default Evening/Morning Saver plan". Sheet 54 limits Anytime to non-AMI customers, or to AMI customers only until Evening/Morning Saver applies, or by election. Fix: `1(M) Evening/Morning Saver` should be is_default=Yes, and `1(M) Residential Anytime` should be blank, with a note that it is the default only for non-AMI meters.
2. **The Ameren 1(M) Evening/Morning Saver is_default field is blank** but should be Yes. This is the same finding as item 1, scored on the second row.
3. **The Ameren 1(M) Ultimate Saver demand charge is missing from the data columns.** `demand_flat_usd_per_kw` is blank. The note holds the correct values ($9.28/kW Jun-Sep, $3.83/kW Oct-May, on max 1-hour demand 6am-10pm, any day; Sheet 54.13). A bill engine reading only the data columns will leave out the demand charge, which is material on this rate. The schema needs seasonal demand support, for example a `demand_flat` column per season or a demand-periods table.

Coverage check: every schedule below covers each day_type's 12x24 grid exactly once (tier 0). No gaps or overlaps.

## SMUD (16534): 38/38 PASS, 4 more fields not scored

Sources: 1-R-TOD.ashx, 1-R.ashx and CI-TOD1.ashx, all Res. 25-06-15, sheets effective 2025-06-20. The rows use the Jan 1 2026 price column. I cross-checked against smud.org/Rate-Information/Residential-rates and the Commercial Rate Guide (effective Jan 1 2026).

| Schedule | Field | Data | Source | Result |
|---|---|---|---|---|
| RT02 | Fixed (SIFC) | 27.00/mo | $27.00 (Jan 1 2026) | PASS |
| RT02 | Sum peak, wkdy 17-20 | 0.3765 | 0.3765 | PASS |
| RT02 | Sum mid, wkdy 12-17, 20-24 | 0.2139 | 0.2139, noon-midnight excl. peak | PASS |
| RT02 | Sum off, wkdy 0-12 and all weekend | 0.1550 | 0.1550 | PASS |
| RT02 | Non-sum peak, wkdy 17-20 | 0.1776 | 0.1776 | PASS |
| RT02 | Non-sum off | 0.1285 | 0.1285 | PASS |
| RT02 | Seasons, hours | Jun-Sep / Oct-May | Jun 1-Sep 30 / Oct 1-May 31 | PASS |
| RT02 | Tiers / demand | none / none | none / none | PASS / PASS |
| RT02 | Effective date | 2026-01-01 | Jan 1 2026 price column | PASS |
| RTL1 | Fixed | 17.00 | $17.00 | PASS |
| RTL1 | Energy (5 prices) | .4154/.2514/.1920/.2148/.1654 | same | PASS x5 |
| RTL1 | Hours, tiers, demand, effective | as RT02 / none / none / 2026-01-01 | same; RTL1 available from Jan 1 2026 | PASS x4 |
| RF01 | Fixed | 27.00 | $27.00 | PASS |
| RF01 | Summer / non-summer energy | 0.2189 / 0.1371 | 0.2189 / 0.1371 | PASS x2 |
| RF01 | Seasons, tiers, demand, effective | Jun-Sep / none / none / 2026-01-01 | same | PASS x4 |
| CITS-0 | Fixed | 42.00 | $42.00 | PASS |
| CITS-0 | Max demand | 2.389 $/kW | $2.389 | PASS |
| CITS-0 | Sum peak wkdy 16-21 / sum off | 0.3246 / 0.1465 | same | PASS x2 |
| CITS-0 | Non-sum peak wkdy 16-21 / off / off-peak saver 9-16 all days | 0.1540 / 0.1346 / 0.1244 | same; saver applies every day 9am-4pm | PASS x3 |
| CITS-0 | Hours, tiers, peak_kw_max 20, effective | as coded / none / 20 / 2026-01-01 | same | PASS x4 |

I did not score these 4 fields:
- **Hydro Generation Adjustment ($0.00).** The rates page confirms it is "currently $0.00/kWh". The tariff sheet itself gives no amount.
- **RTL1 note "<270 kWh/month".** The rates page states this limit; the tariff sheet lists only the 125 A panel limit. The note is correct per the rates page.
- **The 2027 price column is already published** (RT02 $27.80, peak 0.3878, and so on). Rows will need refreshing on 2027-01-01.
- **Holiday off-peak is not coded.** The rows note this. SMUD lists 11 holidays.

## Ameren Missouri (19436): 56/59 PASS

Sources: uecsheet54rate1mres.ashx (Sheets 54-54.15) and uecdsheet55rate2msgs.pdf (Sheet 55 7th Rev., effective 2025-06-01).

| Schedule | Field | Data | Source | Result |
|---|---|---|---|---|
| 1(M) Anytime | Fixed | 9.00 | $9.00 (+$0.19 Low-Income, noted) | PASS |
| 1(M) Anytime | Summer | 0.156 | 15.60c | PASS |
| 1(M) Anytime | Winter tier 0 <=750 / tier 1 | 0.1062 / 0.0714 | 10.62c first 750 / 7.14c over | PASS x3 (2 prices + 750 boundary) |
| 1(M) Anytime | Demand / effective | none / 2025-06-01 | none / Sheet 54 8th Rev. eff. 2025-06-01 | PASS x2 |
| 1(M) Anytime | is_default | Yes | **Blank.** Default only for non-AMI meters; Evening/Morning Saver is the default for new and AMI accounts | **FAIL** |
| 1(M) E/M Saver | Fixed | 9.00 | $9.00 | PASS |
| 1(M) E/M Saver | Summer off / on (9-21 all days) | 0.1524 / 0.1581 | 15.24c; +0.57c on-peak adder = 15.81c | PASS x2 |
| 1(M) E/M Saver | Winter off <=750 / >750 | 0.1045 / 0.0701 | 10.45c / 7.01c | PASS x2 |
| 1(M) E/M Saver | Winter on <=750 / >750 | 0.1073 / 0.0729 | +0.28c adder: 10.73c / 7.29c | PASS x2 |
| 1(M) E/M Saver | Hours, tier boundary, effective | 9-21 all days / 750 / 2026-06-01 | same; Sheet 54.4 7th Rev. eff. 2026-06-01 | PASS x3 |
| 1(M) E/M Saver | is_default | blank | **Yes** (Sheet 54.4 placement language) | **FAIL** |
| 1(M) Smart Saver A | Fixed | 9.00 | $9.00 | PASS |
| 1(M) Smart Saver A | Sum peak wkdy 15-19 / int / off 22-6 | .4051 / .1216 / .0767 | 40.51 / 12.16 / 7.67c | PASS x3 |
| 1(M) Smart Saver A | Win peak wkdy 6-8, 18-20 / int / off | .2169 / .0778 / .0635 | 21.69 / 7.78 / 6.35c | PASS x3 |
| 1(M) Smart Saver A | Hours, tiers, effective | as coded / none / 2026-06-01 | Sheet 54.8 hours; Sheet 54.7 5th Rev. eff. 2026-06-01 | PASS x3 |
| 1(M) Overnight A | Fixed | 9.00 | $9.00 ($1.50 non-AMI noted) | PASS |
| 1(M) Overnight A | Sum on / off; win on / off | .1839 / .0732; .1034 / .0631 | 18.39 / 7.32; 10.34 / 6.31c | PASS x4 |
| 1(M) Overnight A | Hours 6-22 all days, tiers, effective | as coded / none / 2025-06-01 | same; Sheet 54.10 3rd Rev. eff. 2025-06-01 | PASS x3 |
| 1(M) Ultimate | Fixed | 9.00 | $9.00 | PASS |
| 1(M) Ultimate | Sum on wkdy 15-19 / off; win on wkdy 6-8, 18-20 / off | .3413 / .0578; .1856 / .0511 | 34.13 / 5.78; 18.56 / 5.11c | PASS x4 |
| 1(M) Ultimate | Hours, effective | as coded / 2025-06-01 | same; Sheet 54.13 3rd Rev. eff. 2025-06-01 | PASS x2 |
| 1(M) Ultimate | Demand charge | blank (in note only) | $9.28/kW Jun-Sep, $3.83/kW Oct-May | **FAIL** (missing from data columns) |
| 2(M) SGS Std | Fixed (1-ph) | 13.46 | $13.46 (3-ph $25.73, noted) | PASS |
| 2(M) SGS Std | Summer / winter base | 0.1346 / 0.1005 | 13.46c / 10.05c | PASS x2 |
| 2(M) SGS Std | Winter seasonal-use block | not coded (noted) | 5.81c above 1,000 kWh and above a customer-specific threshold | PASS (correctly left blank under the "blank beats guess" rule) |
| 2(M) SGS Std | Demand, peak_kw_max 100, effective, is_default | none / 100 / 2025-06-01 / Yes | no demand charge; moves to 3(M) above 100 kW summer demand; Sheet 55 eff. 2025-06-01; standard rate | PASS x4 |
| 2(M) SGS Overnight | Fixed | 13.46 | $13.46 | PASS |
| 2(M) SGS Overnight | Sum on / off; win on / off | .1489 / .089; .0993 / .0633 | 14.89 / 8.90; 9.93 / 6.33c | PASS x4 |
| 2(M) SGS Overnight | Hours 6-22 all days, effective | as coded / 2025-06-01 | same; AMI only | PASS x2 |

Caveat: all Ameren energy prices exclude Rider FAC, EEIC and RESRAM. This is noted in the rows, and the sheets do not state the rider amounts. Effective all-in $/kWh will run higher, so modeled bill savings will be understated until the riders are added.

## SCE (17609): 2 random TOU period rows (seed 20261016), 4/4 PASS

Source: sce.com time-of-use-plans page, the row's source_url. The page states no effective date, so effective_date is blank in the data.

| Row | Field | Data | Source | Result |
|---|---|---|---|---|
| TOU-D-4-9PM, weekday, Jan-May, Oct-Dec, 0-8, 21-24, p3 | Price | 0.36 | Off-Peak 36c (27c after baseline credit) | PASS |
| same | Hours / day type | 0-8, 21-24, weekday | 12am-8am and 9pm-12am, weekdays and weekends | PASS |
| TOU-D-PRIME, weekend, Jan-May, Oct-Dec, 8-16, p4 | Price | 0.24 | Super-Off-Peak 24c | PASS |
| same | Hours / day type | 8-16, weekend | 8am-4pm, every day | PASS |

Limits on this check:
- The page values are rounded to whole cents and are not tariff-sheet values. I did not find a CPUC tariff sheet to cross-check them against.
- **SCE default status is still unknown.** California moved residential customers to TOU by default, and TOU-D-4-9PM is generally understood to be SCE's default (medium confidence, not confirmed on the source page). Confirm it before setting is_default.

## Are the SMUD and Ameren schedules current and open to new customers?

| Schedule | Current? | Open to new customers? | Default correct? |
|---|---|---|---|
| SMUD RT02 | Yes. Sheet eff. 2025-06-20, Jan 2026 prices, which the rates page shows as current | Yes. "Standard rate"; required for NEM1/SSR systems approved on or after 2018-01-01 | Yes |
| SMUD RTL1 | Yes. New from 2026-01-01 | Yes, if panel <=125 A and use <270 kWh/mo | Yes (optional) |
| SMUD RF01 | Yes | Yes, with no closure language. Not available to post-2018 NEM, SSR or storage customers. Required for non-communicating meters | Yes (optional) |
| SMUD CITS-0 | Yes. The Commercial Rate Guide (eff. Jan 1 2026) shows the same prices | Yes. It is assigned by demand (<=20 kW), with no closure language | Not confirmed. No source calls it "default"; it is the only metered TOD rate for <=20 kW, so "Yes" is reasonable |
| Ameren 1(M) Anytime | Yes (Sheet 54 eff. 2025-06-01, the latest rate case) | Yes, optional for AMI customers | **No.** Default only for non-AMI meters |
| Ameren 1(M) E/M Saver | Yes (eff. 2026-06-01) | Yes, all AMI customers | **No.** It should be the default |
| Ameren 1(M) Smart Saver A | Yes (eff. 2026-06-01) | Yes, AMI; excludes Community Solar Pilot participants | OK (optional) |
| Ameren 1(M) Overnight A | Yes | Yes | OK (optional) |
| Ameren 1(M) Ultimate | Yes | Yes. Available at election since 2021-01-01, with no closure language | OK (optional) |
| Ameren 2(M) Std / Overnight | Yes (eff. 2025-06-01) | Yes. Overnight Saver is AMI only. The Legacy TOD option is correctly left out | OK |

Closed options, correctly not coded:
- Ameren 1(M) grandfathered TOD pilot (Sheet 54.3, "no longer offered for new enrollees")
- SMUD RSMM (closed)
