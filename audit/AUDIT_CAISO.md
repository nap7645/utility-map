# AUDIT_CAISO: sampled source re-verification

- Region: CAISO (California). Sample: `audit/samples/CAISO.json`, **seed 20261002**, 97 items (top-5 utilities by customers at 100% + stratified sample). Results: `audit/results/CAISO.json`.
- Auditor run: 2026-10-02 (44 items) and resumed 2026-10-12 (remaining 53 NOT_DONE items + one retry of the INCONCLUSIVE item idx 67).
- Top-5 territories: PG&E (14328), SCE (17609), SDG&E (16609), 3CE (61432), City of Anaheim (590).

## Method
- Each cited `source_url` opened fresh with WebFetch. No researcher notes, `verify_*` or other `AUDIT_*` files used.
- CONFIRMED only when the page itself shows the claim. A menu label or marketing line is not enough.
- Presence **No** cells: searched the utility's own residential/business rate and DR pages (site-restricted WebSearch, then fetch).
- Program rows: checked name, category, $ value + units, status, URL.
- One replacement search on the utility's own site was allowed. When it was used, the item is marked as a **source defect** (correct claim, wrong or unreadable citation).
- INCONCLUSIVE = robots-blocked, unreadable or truncated document, or the page is silent on the claim. Counted separately.
- Presence cells: `data/processed/presence.csv` (and `presence_scan.csv` where the eia_id exists there), keyed by eia_id. Program "row" = physical line number in `data/processed/programs.csv`.

## Counts
| Group | N | Confirmed | Refuted | Inconclusive |
|---|---|---|---|---|
| Presence = Yes | 24 | 20 | 2 | 2 |
| Presence = No | 15 | 11 | 4 | 0 |
| Program rows | 58 | 45 | 7 | 6 |
| **Total** | 97 | 76 | 13 | 8 |

Top bucket only: Yes 14/1/1 (C/R/I); No 1/2/0; Programs 32/7/4.

## Rates vs bars
| Bar | With inconclusive in denominator | Excluding inconclusive | Pass? |
|---|---|---|---|
| Presence Yes confirmed >= 95% | 20/24 = 83.3% | 20/22 = 90.9% | **FAIL** |
| Presence No confirmed >= 90% | 11/15 = 73.3% | 11/15 = 73.3% | **FAIL** |
| 0 wrong $ in top bucket | 3 wrong $ (idx 45, 46, 47: SCE TOU-D rates) | - | **FAIL** |
| Program rows fully correct (informational) | 45/58 = 77.6% | 45/52 = 86.5% | log + fix all |

Note: `programs.csv` rows 588-590 already carry the corrected SCE values (59/33/44/33/50/32/36c, $0.09 credit, etc.) as of this run. The wrong-$ bar stays failed until a different agent re-verifies them.

## Defect list (refuted items)
| # | idx | File / row / cell | Claimed | Finding | Fix |
|---|---|---|---|---|---|
| D1 | 13 | presence.csv L408 + presence_scan.csv L169, eia 61432 (3CE), `res_dispatch` | Yes | Cited battery-rebate page: "3CE cannot control your battery system". VPP with Lunar Energy announced 2026-06-24, "anticipated to launch Fall 2026", no open enrollment. **Source defect** (replacement search used). | Set `No` (or `Unknown`) until the VPP is enrolling. Re-cite then. |
| D2 | 15 | presence.csv L411, eia 590 (Anaheim), `res_habit` | No | Anaheim rate book has TOU-2 Domestic Time-of-Use (4-9pm weekdays) and D-EV. Battery page anaheim.net/5730 requires "a Time of Use rate". | Set `Yes`. `res_habit_src` = Anaheim rate book (local.anaheim.net council attachment "Current Electric Rates, Rules and Regulations") or the anaheim.net/653 schedule page. |
| D3 | 17 | presence.csv L411, eia 590, `ci_habit` | No | Schedule TOU (commercial, >=500 kW, on-peak 4-9pm summer weekdays, eff 04-03-23). D-TOU-L and TES also exist. | Set `Yes`. `ci_habit_src` = same rate book. |
| D4 | 23 | presence.csv L429 + presence_scan.csv L183, eia 1192 (Banning), `ci_dispatch` | Yes | IW-1 "Interruptible Well Service" is for pumping water for the City's own water system. It has no interruption/notice/credit terms; the only related term is generator use during Flex Alerts. No other C&I DR found on banningca.gov. *Borderline.* | Set `No`, or keep `Yes` only with a note that it is a city-wells rate. Reviewer decision. |
| D5 | 28 | presence.csv L412, eia 16088 (Riverside), `ci_habit` | No | Schedule TOU, Large General & Industrial (>=150 kW), eff 1/1/2024: on-peak 12-6pm summer weekdays, 5-9pm winter weekdays. | Set `Yes`. `ci_habit_src` = riversideca.gov .../2024/Electric Schedule TOU - Effective 01-1-24 Final.pdf |
| D6 | 34 | presence.csv L412, eia 16088, `ci_dispatch` | No | Power Partner Program: businesses "voluntarily shed or shift a specific amount" of load on request, Jul-Oct. No payment shown. *Borderline under SCAN_SCHEMA.* | Set `Yes` (voluntary curtailment) with a note, or document in SCAN_SCHEMA that unpaid voluntary programs are excluded. Reviewer decision. |
| D7 | 45 | programs.csv L588 (SCE TOU-D-4-9PM), `peak_offpeak_rates`, `incentive_value_usd` | 58/34/46/34/51/33/37c; credit $0.10 | Page: 59/33/44/33/50/32/36c; baseline credit $0.09/kWh. **Wrong $ (top).** | Already updated in file. Needs re-verification by a different agent. |
| D8 | 46 | programs.csv L589 (TOU-D-5-8PM), same cells | 74/34/54/34/60/32/38c; $0.10 | Page: 72/34/51/34/55/32/37c; $0.09. **Wrong $ (top).** | Already updated. Re-verify. |
| D9 | 47 | programs.csv L590 (TOU-D-PRIME), `peak_offpeak_rates` | 59/26/40/26/56/24/24c | Page: 61/26/39/26/45/24/30c. **Wrong $ (top).** | Already updated. Re-verify. |
| D10 | 61 | programs.csv L613 (PG&E SmartAC), `program_status` | Active | "SmartAC is currently closed to new enrollments." | `program_status` = Closed to new enrollment. Optional: `incentive_value_usd` = $50 enrollment check. |
| D11 | 65 | programs.csv L617 (SCE SDP), `customer_segment` | Residential;SmallC&I | Cited page is residential only. | `customer_segment` = Residential (or cite SCE's business SDP page). |
| D12 | 69 | programs.csv L621 (SCE Charge Smart SoCal), `program_category`, `event_limits`/eligibility, `source_url` | EV-Rate; weavegrid.com/sce/charge-smart-socal | Managed charging, so the category is DR-DLC. Gateway Cities only, qualifying Tesla or ChargePoint/Emporia/Wallbox. "Up to three years" not shown. Old URL redirects. | `program_category` = DR-DLC. Add the geographic/device limits. `source_url` = https://charge.weavegrid.com/sce/. Drop "for up to three years" unless sourced. |
| D13 | 77 | programs.csv L629 (SCE TOU-GS-3/TOU-8), `source_url` | sce.com/regulatory/tariff-books/rates-pricing-choices | The index page does not show these schedules. The content is correct. **Source defect.** | `source_url` = https://www.sce.com/sites/default/files/custom-files/PDF_Files/Business/TOU-8_Rate_Fact_Sheet_072025_Accessible.pdf |

### Source defects on CONFIRMED items (claim true; citation should change)
| idx | File / cell | Issue | Fix |
|---|---|---|---|
| 24 | presence.csv, eia 14534 (Pasadena), `res_habit_src` | The municode URL renders no text. | https://pwp.cityofpasadena.net/wp-content/uploads/2025/09/Summary-Rates-2025_10.pdf (R-1/R-2 TOU option) |
| 29 | presence.csv, eia 17612 (BVES), `res_habit_src` | The index page has no residential TOU label. | https://www.bvesinc.com/assets/documents/rates/09012026/schedule-tou-ev1.pdf |
| 30 | presence.csv, eia 1050 (Azusa), `ci_habit_src` | ci.azusa.ca.us/575 is robots-blocked. | https://azusaca.gov/570/Commercial |
| 1 | presence.csv, eia 14328 (PG&E), `res_dispatch_src` | E-CBP is weak evidence for residential device control (from the 10-02 run). | The PG&E SmartAC page. Note that SmartAC is closed to new enrollment, so consider the PG&E ELRP A.4 battery page. |

### Inconclusive (not counted as misses; recheck by hand)
- idx 16, 79, 80, 81 (Anaheim): anaheim.net/5920, the DR FAQ and the battery application PDF are robots-blocked. idx 80: the page shows "Up to $3,000" with no $1,500 step-down from 7/1/2026. Verify the step-down or drop it. idx 81: the NEM 2.0 page does not show the "transition to wholesale" claim or the program status.
- idx 35 (Colton `res_habit`): the TOU calendar does not name a customer class, and the rates PDF is robots-blocked.
- idx 67 (SCE CPP "$50/yr"): retried; not found on sce.com.
- idx 82 (CAISO DMM AS prices): the fetch returns only the executive summary. Totals ($94.5M, $9/kW-yr, 53%) were confirmed; the per-product $/MW-h figures were not visible.
- idx 93 (SVP TOU Option): the cited D-1 PDF does not fetch. Also, a D-1 Domestic citation for a Res+C&I segment is suspect.

## Item table
| idx | bucket | utility | cell / program | claimed | verdict | evidence URL |
|---|---|---|---|---|---|---|
| 0 | top | Pacific Gas and Electric Co (PG&E) | res_habit | Yes | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-ELEC.pdf |
| 1 | top | Pacific Gas and Electric Co (PG&E) | res_dispatch | Yes | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-CBP.pdf |
| 2 | top | Pacific Gas and Electric Co (PG&E) | ci_habit | Yes | CONFIRMED | https://www.pge.com/en/account/rate-plans/peak-day-pricing.html |
| 3 | top | Pacific Gas and Electric Co (PG&E) | ci_dispatch | Yes | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr/emergency-load-reduction-program |
| 4 | top | Southern California Edison Co (SCE) | res_habit | Yes | CONFIRMED | https://www.sce.com/save-money/rates-financing/residential-rate-plans/time-of-use-plans |
| 5 | top | Southern California Edison Co (SCE) | res_dispatch | Yes | CONFIRMED | https://www.sce.com/save-money/savings-programs/ways-to-save-at-home/what-is-demand-response |
| 6 | top | Southern California Edison Co (SCE) | ci_habit | Yes | CONFIRMED | https://www.sce.com/business/rates-financing/rate-plans/critical-peak-pricing |
| 7 | top | Southern California Edison Co (SCE) | ci_dispatch | Yes | CONFIRMED | https://www.sce.com/factsheet/emergency-load-reduction-program |
| 8 | top | San Diego Gas & Electric Co (SDG&E) | res_habit | Yes | CONFIRMED | https://www.sdge.com/sites/default/files/regulatory/1-1-26%20Schedule%20TOU-DR1%20Total%20Rates%20Table.pdf |
| 9 | top | San Diego Gas & Electric Co (SDG&E) | res_dispatch | Yes | CONFIRMED | https://www.sdge.com/residential/savings-center/energy-saving-programs/reduce-your-use/demand-response-residential-programs/ELRP |
| 10 | top | San Diego Gas & Electric Co (SDG&E) | ci_habit | Yes | CONFIRMED | https://www.sdge.com/sites/default/files/elec_elec-scheds_al-tou.pdf |
| 11 | top | San Diego Gas & Electric Co (SDG&E) | ci_dispatch | Yes | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr/emergency-load-reduction-program |
| 12 | top | Central Coast Community Energy (3CE) | res_habit | Yes | CONFIRMED | https://3cenergy.org/rebates/hourly-flex-pricing-pilot/ |
| 13 | top | Central Coast Community Energy (3CE) | res_dispatch | Yes | REFUTED | https://3cenergy.org/rebates/residential-battery-rebate-program/ |
| 14 | top | Central Coast Community Energy (3CE) | ci_habit | Yes | CONFIRMED | https://3cenergy.org/rebates/hourly-flex-pricing-pilot/ |
| 15 | top | City of Anaheim Public Utilities | res_habit | No | REFUTED | https://local.anaheim.net/docs_agend/questys_pub/40932/40962/40963/41099/41102/2.%20Current%20Electric%20Rates,%20Rules%20and%20Regulations%20Rate%20Schedules%20and%20Rule%20Nos.%2026%20and%202941102.pdf |
| 16 | top | City of Anaheim Public Utilities | res_dispatch | Yes | INCONCLUSIVE | https://www.anaheim.net/5920/myPower-Savings |
| 17 | top | City of Anaheim Public Utilities | ci_habit | No | REFUTED | https://local.anaheim.net/docs_agend/questys_pub/40932/40962/40963/41099/41102/2.%20Current%20Electric%20Rates,%20Rules%20and%20Regulations%20Rate%20Schedules%20and%20Rule%20Nos.%2026%20and%202941102.pdf |
| 18 | top | City of Anaheim Public Utilities | ci_dispatch | No | CONFIRMED | https://local.anaheim.net/docs_agend/questys_pub/40932/40962/40963/41099/41102/2.%20Current%20Electric%20Rates,%20Rules%20and%20Regulations%20Rate%20Schedules%20and%20Rule%20Nos.%2026%20and%202941102.pdf |
| 19 | sample | Lassen Municipal Utility District | ci_habit | No | CONFIRMED | https://www.lmud.org/my-account/rates/ |
| 20 | sample | Silicon Valley Power (City of Santa Clara) | ci_dispatch | No | CONFIRMED | https://www.siliconvalleypower.com/businesses/save-money |
| 21 | sample | Riverside Public Utilities | res_dispatch | No | CONFIRMED | https://www.riversideca.gov/utilities/residents/our-energy/flex-alerts |
| 22 | sample | Bear Valley Electric Service, Inc. (Golden State Water) | ci_habit | Yes | CONFIRMED | https://www.bvesinc.com/customer-service/rates-regulations/general-rate-schedules |
| 23 | sample | City of Banning Electric Utility (BEU) | ci_dispatch | Yes | REFUTED | https://www.banningca.gov/DocumentCenter/View/9922/Interuptible-Well-Service-Rate-Schedule---Effective-January-1-2022 |
| 24 | sample | Pasadena Water and Power | res_habit | Yes | CONFIRMED | https://pwp.cityofpasadena.net/wp-content/uploads/2025/09/Summary-Rates-2025_10.pdf |
| 25 | sample | Riverside Public Utilities | res_habit | Yes | CONFIRMED | https://riversideca.gov/utilities/sites/riversideca.gov.utilities/files/pdf/rates-electric/2024/Electric%20Schedule%20DTOU%20-%20Effective%2001-1-24%20Final.pdf |
| 26 | sample | Lassen Municipal Utility District | ci_dispatch | No | CONFIRMED | https://www.lmud.org/customer-services/rebates/business-rebates/ |
| 27 | sample | Alameda Municipal Power | res_dispatch | No | CONFIRMED | https://www.alamedamp.com/407/Rebates-and-Incentives |
| 28 | sample | Riverside Public Utilities | ci_habit | No | REFUTED | https://www.riversideca.gov/utilities/sites/riversideca.gov.utilities/files/pdf/rates-electric/2024/Electric%20Schedule%20TOU%20-%20Effective%2001-1-24%20Final.pdf |
| 29 | sample | Bear Valley Electric Service, Inc. (Golden State Water) | res_habit | Yes | CONFIRMED | https://www.bvesinc.com/assets/documents/rates/09012026/schedule-tou-ev1.pdf |
| 30 | sample | Azusa Light & Water | ci_habit | Yes | CONFIRMED | https://azusaca.gov/570/Commercial |
| 31 | sample | Turlock Irrigation District (TID) | res_dispatch | Yes | CONFIRMED | https://www.tid.org/energysync/ |
| 32 | sample | Lassen Municipal Utility District | res_dispatch | No | CONFIRMED | https://www.lmud.org/customer-services/rebates/residential-rebates/smart-thermostat/ |
| 33 | sample | Alameda Municipal Power | ci_habit | No | CONFIRMED | https://www.alamedamp.com/DocumentCenter/View/1476/A2-Rate-Schedule-Effective-2025-7-1 |
| 34 | sample | Riverside Public Utilities | ci_dispatch | No | REFUTED | https://riversideca.gov/utilities/utilities/businesses/power-partners |
| 35 | sample | Colton Electric Utility | res_habit | Yes | INCONCLUSIVE | https://www.coltonca.gov/975/Time-of-Use-Calendar |
| 36 | sample | Lompoc Electric Utility | ci_habit | No | CONFIRMED | https://www.cityoflompoc.com/government/departments/utilities/utility-service-information/electric-rate-information |
| 37 | sample | Pasadena Water and Power | res_dispatch | No | CONFIRMED | https://pwp.cityofpasadena.net/smartthermostatrebate/ |
| 38 | sample | Lompoc Electric Utility | res_habit | No | CONFIRMED | https://www.cityoflompoc.com/government/departments/utilities/utility-service-information/electric-rate-information |
| 39 | top | Pacific Gas and Electric Co (PG&E) | Solar Billing Plan (Schedule NBT) | Active | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_NBT.pdf |
| 40 | top | Southern California Edison Co (SCE) | Solar Billing Plan (Net Billing Tariff) | Active | CONFIRMED | https://www.sce.com/residential/generating-your-own-power/solar-billing-plan |
| 41 | top | San Diego Gas & Electric Co (SDG&E) | Solar Billing Plan (Net Billing Tariff) | Active | CONFIRMED | https://www.sdge.com/solar/solar-billing-plan |
| 42 | top | Pacific Gas and Electric Co (PG&E) | Schedule E-ELEC - Residential Time-of-Use (Electric Home) | Base Services Charge (eff 2026-03-01): $0.19713/day Income Tier 1, ... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-ELEC.pdf |
| 43 | top | Pacific Gas and Electric Co (PG&E) | Schedule E-TOU-C - Residential Time-of-Use (Peak Pricing ... | Baseline credit $0.08140/kWh on baseline usage; Base Services Charg... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-TOU-C.pdf |
| 44 | top | Pacific Gas and Electric Co (PG&E) | Schedule EV2 (EV2-A) - Residential Time-of-Use for Plug-i... | Base Services Charge $0.19713 / $0.39688 / $0.79343 per day by inco... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_EV2%20(Sch).pdf |
| 45 | top | Southern California Edison Co (SCE) | Schedule TOU-D Option 4-9PM (TOU-D-4-9PM) | Baseline credit $0.10/kWh up to monthly baseline allocation; Base S... | REFUTED (wrong $) | https://www.sce.com/save-money/rates-financing/residential-rate-plans/time-of-use-plans |
| 46 | top | Southern California Edison Co (SCE) | Schedule TOU-D Option 5-8PM (TOU-D-5-8PM) | Baseline credit $0.10/kWh up to monthly baseline allocation; Base S... | REFUTED (wrong $) | https://www.sce.com/save-money/rates-financing/residential-rate-plans/time-of-use-plans |
| 47 | top | Southern California Edison Co (SCE) | Schedule TOU-D Option PRIME (TOU-D-PRIME) | Base Services Charge $0.79/day; no baseline credit | REFUTED (wrong $) | https://www.sce.com/save-money/rates-financing/residential-rate-plans/time-of-use-plans |
| 48 | top | Southern California Edison Co (SCE) | Schedule TOU-D Options A, B and T (discontinued TOU periods) | Closed to new enrollment | CONFIRMED | https://www.sce.com/save-money/rates-financing/residential-rate-plans/time-of-use-plans |
| 49 | top | San Diego Gas & Electric Co (SDG&E) | Schedule TOU-DR1 - Residential Time of Use Service | Baseline Adjustment Credit $0.10905/kWh up to 130% of baseline; Bas... | CONFIRMED | https://www.sdge.com/sites/default/files/regulatory/1-1-26%20Schedule%20TOU-DR1%20Total%20Rates%20Table.pdf |
| 50 | top | Pacific Gas and Electric Co (PG&E) | Emergency Load Reduction Program (PG&E, administered via ... | $2.00/kWh of measured load reduction (non-residential, per CPUC ELR... | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr/emergency-load-reduction-program |
| 51 | top | Southern California Edison Co (SCE) | Emergency Load Reduction Program (SCE) | $2.00/kWh of measured load reduction (non-residential, per CPUC ELR... | CONFIRMED | https://www.sce.com/factsheet/emergency-load-reduction-program |
| 52 | top | San Diego Gas & Electric Co (SDG&E) | Emergency Load Reduction Program (SDG&E) | $2.00/kWh of measured load reduction (non-residential, per CPUC ELR... | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr/emergency-load-reduction-program |
| 53 | top | Pacific Gas and Electric Co (PG&E) | Schedule E-BIP - Base Interruptible Program | 15-Minute BIP: Nov-Apr $10.60 (1-500 kW) / $11.20 (501-1,000 kW) / ... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-BIP.pdf |
| 54 | top | Pacific Gas and Electric Co (PG&E) | Underfrequency Relay (UFR) Program (rider to Schedule E-BIP) | $0.67/kW-month demand credit on average monthly summer on-peak / wi... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-BIP.pdf |
| 55 | top | Pacific Gas and Electric Co (PG&E) | Schedule E-CBP - Capacity Bidding Program | Active | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-CBP.pdf |
| 56 | top | Pacific Gas and Electric Co (PG&E) | Peak Day Pricing (PDP) | Active | CONFIRMED | https://www.pge.com/en/account/rate-plans/peak-day-pricing.html |
| 57 | top | Pacific Gas and Electric Co (PG&E) | Schedule E-OBMC - Optional Binding Mandatory Curtailment ... | $0 incentive; $6.00/kWh penalty for each kWh above the commitment | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_E-OBMC.pdf |
| 58 | top | Pacific Gas and Electric Co (PG&E) | Automated Demand Response (ADR) incentive | $200/kW for approved projects, up to 75% of eligible project costs | CONFIRMED | https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/business-programs.html |
| 59 | top | Pacific Gas and Electric Co (PG&E) | Automated Response Technology (ART) | Active | CONFIRMED | https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/automated-response-technology.html |
| 60 | top | Pacific Gas and Electric Co (PG&E) | SmartRate (residential critical peak pricing) | Active | CONFIRMED | https://www.pge.com/en/account/rate-plans/smartrate.html |
| 61 | top | Pacific Gas and Electric Co (PG&E) | SmartAC | Active | REFUTED | https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/smartac.html |
| 62 | top | Pacific Gas and Electric Co (PG&E) | WatterSaver | $50 gift card enrollment bonus plus $5 gift card credit for every m... | CONFIRMED | https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs.html |
| 63 | top | Southern California Edison Co (SCE) | Behind-the-Meter Optimization of Load Technology (BOLT) S... | Behind-the-meter batteries up to $400 each; electric vehicles up to... | CONFIRMED | https://www.sce.com/save-money/savings-programs/ways-to-save-at-home/what-is-demand-response |
| 64 | top | Southern California Edison Co (SCE) | Smart Energy Program (SEP) | $75 one-time sign-up credit plus up to $50/year in bill credits for... | CONFIRMED | https://www.sce.com/residential/demand-response/smart-energy-program |
| 65 | top | Southern California Edison Co (SCE) | Summer Discount Plan (SDP) | Up to $160/year in summer bill credits | REFUTED | https://www.sce.com/save-money/savings-programs/enroll-in-savings-programs/summer-discount-plan |
| 66 | top | Southern California Edison Co (SCE) | Capacity Bidding Program - Elect (CBP-E) and CBP-E Direct | Aggregator-determined for CBP-E; CBP-E Direct pays based on event p... | CONFIRMED | https://www.sce.com/save-money/savings-programs/enroll-in-savings-programs/capacity-bidding-program-elect |
| 67 | top | Southern California Edison Co (SCE) | Critical Peak Pricing (CPP) - residential and non-residen... | SCE states average savings around $50/year for residential particip... | INCONCLUSIVE | https://www.sce.com/save-money/savings-programs/ways-to-save-at-home/what-is-demand-response |
| 68 | top | Southern California Edison Co (SCE) | SmartShift Rewards | $100 enrollment reward plus $5 to $10 per month of participation (S... | CONFIRMED | https://www.sce.com/save-money/savings-programs/ways-to-save-at-home/what-is-demand-response |
| 69 | top | Southern California Edison Co (SCE) | Charge Smart - SoCal (managed EV charging, operated with ... | $50 sign-up bonus plus $50 annually for up to three years | REFUTED | https://charge.weavegrid.com/sce/ |
| 70 | top | San Diego Gas & Electric Co (SDG&E) | Schedule EV-TOU-5 - Domestic Time-of-Use for Households w... | Base Services Charge $0.79343/day standard, $0.39688/day CARE(DRAH)... | CONFIRMED | https://www.sdge.com/sites/default/files/regulatory/8-1-26%20Schedule%20EV-TOU-5%20Total%20Rates%20Table.pdf |
| 71 | top | San Diego Gas & Electric Co (SDG&E) | Emergency Load Reduction Program A.4 - residential batter... | Active | CONFIRMED | https://www.sdge.com/residential/savings-center/energy-saving-programs/reduce-your-use/demand-response-residential-programs/ELRP |
| 72 | top | San Diego Gas & Electric Co (SDG&E) | Power Saver Rewards (SDG&E residential ELRP A.6) | $1.00/kWh of measured incremental load reduction while the program ... | CONFIRMED | https://www.sdge.com/residential/savings-center/energy-saving-programs/reduce-your-use/power-saver-program |
| 73 | top | Pacific Gas and Electric Co (PG&E) | Schedule B-19 - Medium General Demand-Metered TOU Service... | Secondary voltage, eff 2026-03-01: Maximum Peak Demand Summer $46.1... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_B-19.pdf |
| 74 | top | Pacific Gas and Electric Co (PG&E) | Schedule B-19 Option S (storage rate option) | Secondary voltage, eff 2026-03-01: Maximum Peak Demand Summer $1.60... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_B-19.pdf |
| 75 | top | Pacific Gas and Electric Co (PG&E) | Schedule B-19 Option R (standalone storage and renewable ... | Secondary voltage, eff 2026-03-01: Maximum Peak Demand Summer $6.50... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_B-19.pdf |
| 76 | top | Pacific Gas and Electric Co (PG&E) | Peak Day Pricing rates on Schedule B-19 | PDP charge $0.90/kWh on all usage during a PDP event. PDP demand cr... | CONFIRMED | https://www.pge.com/tariffs/assets/pdf/tariffbook/ELEC_SCHEDS_B-19.pdf |
| 77 | top | Southern California Edison Co (SCE) | Schedules TOU-GS-3 and TOU-8 - non-residential demand-met... | Active | REFUTED | https://www.sce.com/sites/default/files/custom-files/PDF_Files/Business/TOU-8_Rate_Fact_Sheet_072025_Accessible.pdf |
| 78 | top | San Diego Gas & Electric Co (SDG&E) | Schedule AL-TOU - general service, demand-metered time-of... | Active | CONFIRMED | https://www.sdge.com/sites/default/files/elec_elec-scheds_al-tou.pdf |
| 79 | top | City of Anaheim Public Utilities | myPower Savings Program | up to $30 enrollment bill credit; $1.00/kWh reduced during event ho... | INCONCLUSIVE | https://www.anaheim.net/5920/myPower-Savings |
| 80 | top | City of Anaheim Public Utilities | Residential Energy Storage Rebate | up to $3,000/household (through 6/30/2026); up to $1,500/household ... | INCONCLUSIVE | https://www.anaheim.net/5730/Battery-Storage |
| 81 | top | City of Anaheim Public Utilities | Net Energy Metering 2.0 | Active | INCONCLUSIVE | https://www.anaheim.net/5587/NEM-20 |
| 82 | sample | California Independent System Operator | Ancillary Services (Regulation Up/Down, Spinning Reserve,... | DMM quantity-weighted average clearing prices ($/MW per hour), 2024... | INCONCLUSIVE | https://www.caiso.com/documents/2025-annual-report-on-market-issues-and-performance.pdf |
| 83 | sample | California statewide (CPUC / CEC / GO-Biz administered) | Demand Response Auction Mechanism (DRAM) | Terminated | CONFIRMED | https://www.utilitydive.com/news/demand-response-california-dram-der-distributed-energy-resources/715987/ |
| 84 | sample | California statewide (CPUC / CEC / GO-Biz administered) | Net Billing Tariff (NBT) - successor to net energy meteri... | Active | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/customer-generation/net-energy-metering-and-net-billing |
| 85 | sample | California Independent System Operator | Heterogeneous DER Aggregation (HDERA) with Distributed Cu... | Active | CONFIRMED | https://www.caiso.com/documents/business-requirements-specification-ferc-order-2222.pdf |
| 86 | sample | California statewide (CPUC / CEC / GO-Biz administered) | SGIP - San Joaquin Valley Residential budget | $1,100/kWh (CPUC rate table) | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/self-generation-incentive-program |
| 87 | sample | California statewide (CPUC / CEC / GO-Biz administered) | Power Saver Rewards (residential ELRP sub-program A.6) | $1.00/kWh for voluntary incremental residential load reduction | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr/emergency-load-reduction-program |
| 88 | sample | California Independent System Operator | FERC Order 2222 implementation status - CAISO DER Aggrega... | Active | CONFIRMED | https://www.caiso.com/documents/nov-5-2024-informational-filing-of-effective-date-ferc-order-no-2222-er21-2455.pdf |
| 89 | sample | Turlock Irrigation District (TID) | EnergySync | $50 enroll + $25 participation (up to $75/season) | CONFIRMED | https://www.tid.org/energysync/ |
| 90 | sample | California statewide (CPUC / CEC / GO-Biz administered) | Net Energy Metering 2.0 (legacy / grandfathered) | Closed to new enrollment | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/customer-generation/net-energy-metering-and-net-billing |
| 91 | sample | California Independent System Operator | WEIM / EDAM - access for customer-sited batteries in non-... | Active | CONFIRMED | https://www.caiso.com/documents/participationcomparison-proxydemand-distributedenergy-storage-forecastadjustment.pdf |
| 92 | sample | Silicon Valley Power (City of Santa Clara) | Net Energy Metering (NM1.0) | Active | CONFIRMED | https://www.siliconvalleypower.com/home/showpublisheddocument/58854/639080506621200000 |
| 93 | sample | Silicon Valley Power (City of Santa Clara) | Time of Use (TOU) Option | Active | INCONCLUSIVE | https://www.siliconvalleypower.com/home/showpublisheddocument/6253/639032058815300000 |
| 94 | sample | California statewide (CPUC / CEC / GO-Biz administered) | SGIP - Small Residential Storage budget (general market) | $150/kWh (CPUC rate table) | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/self-generation-incentive-program |
| 95 | sample | California Independent System Operator | Small utility opt-in gate and state aggregation rules for... | Active | CONFIRMED | https://www.caiso.com/Documents/May18-2023-OrderAcceptingComplianceFilingofFERCOrderNo2222-ER21-2455.pdf |
| 96 | sample | California statewide (CPUC / CEC / GO-Biz administered) | SGIP - Equity Resiliency budget | $1,000/kWh (CPUC rate table) | CONFIRMED | https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/self-generation-incentive-program |
