# Verify: rider files riders_1.csv / riders_2.csv (2026-10-19)

Independent check of `data/raw/tariffs/riders_1.csv` (311 rows) and `riders_2.csv` (160 rows), 471 rows total, 50 eia_ids. 18 fetches: 14 curl + `pdftotext -layout`, all HTTP 200; 3 WebFetch (CenterPoint, SCE and GMP pages, which are JS/HTML); 1 extra curl (Potomac Edison tariff, for the double-count check). No data edited. Scratch: `/tmp/claude-0/-home-claude/d3bb9943-e471-564e-8107-8a9b626f8977/scratchpad/vrid/`.

## 1. Structural

| Check | Result |
|---|---|
| Header: 13 cols, exact order, both files | PASS |
| usd_per_kwh / usd_per_month / usd_per_kw numeric or blank | PASS (0 non-numeric) |
| eia_id present in some `*_tariffs.csv` | PASS (50/50) |
| rate_schedule exact match to the eia_id's tariff rate_schedule or ALL/ALL-RES/ALL-C&I | **FAIL, 3 rows**: 19446 (Duke Energy KY) uses `RS` / `DS`; tariff rows are `RS Residential Service` / `DS Secondary Distribution Voltage`. These won't join. |
| Duplicate (eia_id, rate_schedule, rider_name) | PASS (0) |
| tier | All `Primary` |
| Rows with all three value fields blank | 49. These are placeholders (`(not found)`, `(none: included)`, `(base rate update)`) or percentage riders whose % lives only in `note` (e.g. 814 TA, 15474 IRA/TCR, 4922 D29/D36/D41, 12390/20387/14716 DSIC, 20404 ITR, 12199 interim 26.118%, 14232 interim 19.16%). A loader has to skip them, and percentage riders are currently unmodeled. |
| source_url blank | 4 rows (19436 `(not found)`, 14154 `(info)` gross-receipts, 3542 `(not found)`, 14626 `(none: included)`). All are informational, so this is minor. |
| applies_months format | Inconsistent: `all` (3408 x4), `Jan-Dec`, `Jul-Jun`, `Sep-Dec,Jan-Aug`, `Dec`. `all`, `Jul-Jun` and `Sep-Dec,Jan-Aug` don't follow the periods-file `Mon-Mon` convention. Normalize them to `Jan-Dec`. |
| Value with blank effective_date | 29 rows (e.g. all CenterPoint, because the page states no date). Acceptable as long as `note` says so, which it does. |

### Double-counting vs energy_usd_per_kwh

I read the tariff-row notes for every eia_id that has a valued rider (keyword + "include/exclude" scan, then manual reading of hits). Nearly every case is explicitly excluded in the tariff note: Oncor, CenterPoint, AEP TX, Ameren MO FAC/EEIC, Empire FAC, Lakeland fuel/env, TECO fuel/SPC/CETM, CEI South Appendix riders, APCo, PCIA, WPCA. DESC (17539) correctly records only the DER $/month, and fuel/DSM/storm/pension stay inside energy, as the rate8.pdf sheet confirms. Exceptions:

| eia_id | Rider | Issue | Verdict |
|---|---|---|---|
| 15263 Potomac Edison MD | Residential SOS administrative charge 0.00400 | Tariff Sec. 1(v) says "Residential SOS **includes** an administrative charge of $0.00400 per kilowatt-hour". The tariff row's SOS $0.10824/$0.10209 therefore already contains it, so adding the rider double-counts 0.4 c/kWh. The tariff note itself says "unclear if embedded". | CONFIRMED double count (high confidence). Drop the rider or set it to 0 with a note. |
| 18454 TECO RS | Fuel first-1000 0.03210 **and** over-1000 0.04210 as two flat rows | Same rider split by tier with no tier key. A loader that sums riders charges 7.42 c/kWh fuel. | CONFIRMED schema double count. |
| 18454 TECO GST | Fuel on-peak 0.03822 + off-peak 0.03376 | Split by TOU period with no period key. | CONFIRMED schema double count. |
| 10623 Lakeland RSX-1, GSX-1 | Fuel On-Peak 0.057387 + Off-Peak 0.042488 | Same problem as TECO GST. | CONFIRMED schema double count. |
| 14154 O&R SC19 TOU | MSC "peak/off-peak" 0.09764 | Only the peak value is stored as a flat rate; off-peak 0.09039 appears only in the note. This overstates TOU supply. | CONFIRMED (overstatement, not a double count). |
| 14716 Penn Power | USC 1.236 c | Tariff says "USC shall be included in the distribution charges of the monthly bill". This is bill presentation, and the 5.480 c RS distribution rate is the base sheet rate. | Not a double count (PLAUSIBLE OK). |

The schema needs a `period`/`tier` key (or tier_max_kwh + TOU id) for split riders. Until then, these rows shouldn't be summed blindly.

## 2. Sample: 13 utilities, value / units / sign / effective date

| # | Utility (eia) | Rows checked | Source finding | Result |
|---|---|---|---|---|
| 1 | Oncor (44372) | TCRF 0.021669/0.013382, EECRF 0.001487/0.000055, DCRF 0.005755/0.006208, RCE 0.000086, IS 0.003633/0.002878, MG 0.001027/0.000606 (Dec) | Sheet 6.1 Rev 53 eff 2026-10-04 (TCRF); EECRF eff 2026-03-01; DCRF Sheet 6.4 Rev 12 eff 2026-10-04; IS Sheet 6.7 eff 2026-08-01, runs through Dec 2026; MG Dec-only, 2025-12-01. All exact. | PASS |
| 2 | CenterPoint Houston (8901) | All 20 rows (TCRF 0.029265/0.012204, DCRF, EECRF, NDC, TEEEF, RCE, SRC II, ADFIT II (neg), IRA, RRC) | Rates page values match exactly, signs included. Page shows no effective date, as noted. | PASS |
| 3 | Ameren Missouri (19436) | FAC 0.00445 secondary | Sheet 72.x: FAR 0.00421 x VAF_SEC 1.0560 = 0.00445, issued 2026-07-30, eff 2026-10-01 | PASS |
| 4 | Appalachian Power VA (733) | S.U.T., S.B.B.R. (neg), F.F.R., T-RAC, E-RAC, G-RAC, Sch 15 and Sch 231 | Select Schedule Charges 2026-09-24: all exact, including -0.01489/-0.01342 | PASS (the sheet calls itself "illustrative") |
| 5 | Tampa Electric (18454) | Fuel, SPC, CETM for RS/RSVP/GS/GST | Jan-2026 insert: all exact. The storm surcharge ended Aug 2026, so excluding it is correct. | PASS on values. Possibly stale: fuel factors from Jan 2026, and no mid-course correction was checked. Tier/period double count above. |
| 6 | Dominion SC (17539) | DER charge $1.00/mo (Rate 8), $4.98 (Rate 9/16) | rate8.pdf: "$1.00 per account per month"; fuel $0.03949, DSM, pension and storm "included in the energy charge" | PASS |
| 7 | MGE (11479) | Fuel credit -0.03561 (Rg-1/Rg-2A), -0.03522 (Cg-5) | Sheet E-1.3.0: credits for Oct 1-31 2026, schedule groups match, sign correct | PASS. Caveat: a one-month value with applies_months blank, so annual use is an extrapolation. |
| 8 | Penn Power (14716) | USC 1.236c, EE&C 0.189/0.296c, SMT $0.03/$0.20, DSS 0.116/(0.080)c, DSIC 2.40%, SPVRC 0 | All exact (USC eff 2026-01-01; EE&C/DSS eff 2026-06-01; SMT eff 2026-01-01; DSIC eff 2026-10-01) | PASS. Minor: SPVRC effective_date 2025-06-01, but the 2026-06-01 sheet also shows $0.00000. |
| 9 | SCE (17609) | `(none: included)` | Page: "rates shown reflect ... both delivery and generation", "Other charges will appear on the bill", 79c/day BSC. Prices are rounded (30c/39c). | PLAUSIBLE. No rider amounts are published on the page. |
| 10 | CEI (3755) | AER 0.000169, GCR1 0.009846, PIPP 0.32567c | Tariff: AER 0.0169c, GCR1 0.9846c (GCR2 0), PIPP 0.32567c first 833,000 kWh | PASS |
| 11 | AEP Texas North (20404) | TCRF 0.017194/0.009298, EECRF 0.001101/0.000810, DCRF 0.003660/0.005594, RAR (0.001329)/(0.001857), TEEEF 0.00083/0.00063 | Consolidated AEP Texas tariff, eff 2026-09-29: exact. Base 0.032966 + riders ~0.0215 ≈ PUCT North all-in ~0.056, so the riders are consistent with the North division. | PASS |
| 12 | Lakeland (10623) | Fuel 0.047, Env 0.0018506, TOU fuel 0.057387/0.042488 | Rate sheet eff 2026-10-01: exact | PASS on values. Period double count above. |
| 13 | O&R (14154) | ECA total SC1 (0.00032), SC19 (0.00034) | Statement 175 eff 2026-10-01: exact, components match note | PASS |

## 3. Stale-base flags raised by the rider agent

| Flag | Stored (tariffs/periods) | Source (fetched today) | Verdict |
|---|---|---|---|
| Oncor res base 0.025344 | periods 0.025344; fixed 4.23 | Sheet 1.1 Rev 11 eff **2026-06-01** (Docket 58306): Customer $1.48 + Metering $2.58 = **$4.06**/mo, Distribution **$0.036043**/kWh. Secondary <=10 kW: $0.031236/kWh, Metering $4.36. | Flag CONFIRMED. Stale by 1.07 c/kWh. Update the energy to 0.036043, fixed to 4.06, effective 2026-06-01. |
| CEI Rate RS 2009 base | $4.00 + 2.951c, eff 2009-05-01 (from CEI-**2025** file) | CEI-2026 tariff, eff **2026-03-01**: RS Service Charge **$6.50**, all kWh **4.8397c**. GS Service Charge **$10.00** + Capacity $26.6451 (first 5 kW) / $12.5319 per kW over 5 kW. | Flag CONFIRMED. The stored source_url points to the 2025 file. |
| GMP Rate 1 | $0.673/day + 0.23066/kWh (labeled eff 2026-10-01) | Rate-1-Residential.pdf, V.P.U.C. 10, "effective with bills rendered on or after October 1, 2026": **$0.660/day + $0.22639/kWh**. Rates page also: Rate 11 $0.876/day, 0.35949/0.15322; Rate 6 $0.822/day, 0.23017; Rate 8 $0.838/day, 0.24498/0.14790, $24.019/kW. All stored GMP values run ~1.9% high, consistently. | Flag CONFIRMED for Rate 1 (high confidence; the PDF is dated). Rates 6/8/11 are likely stale by the same ~1.9% (medium confidence; the rates page is undated). |

## Action list (for the data owner)
1. 19446: rename rate_schedule `RS` -> `RS Residential Service` and `DS` -> `DS Secondary Distribution Voltage`.
2. 15263: remove or zero the SOS admin rider (it's already embedded in the SOS rate).
3. TECO RS/GST, Lakeland RSX-1/GSX-1, O&R SC19 MSC: add a period/tier key, or move split values into periods. Don't sum them.
4. Normalize applies_months (`all`, `Jul-Jun`, `Sep-Dec,Jan-Aug` -> `Jan-Dec`).
5. Patch stale bases: Oncor (0.036043, $4.06), CEI RS ($6.50, 0.048397) and GS ($10.00 + capacity), GMP (Rate 1 0.660/0.22639; recheck 6/8/11).
6. Percentage riders (about 20 rows) carry their value only in `note`. They need a `pct` column or have to be left explicitly unmodeled.
