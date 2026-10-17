# Phase B batch 12 log (2026-10-16)
Validation: ALL OK (31 tariff rows, 155 period rows; each schedule+day_type covers 12x24 once; one period id per distinct price per schedule; min_bill numeric or blank).
Common: fuel/power-cost riders (PSA, WPCA, PCRF, FCA, FAC) not added unless the tariff states a combined total; holidays not coded.

## 14289 Ozarks Electric Coop (AR) - 2 fetches
Captured AR Residential/General Service (coded for both sectors as separate schedule names, same rates) and Energy Flex Plan (residential pilot) from the Aug 2026 AR member handbook (rates eff 2026-06-01). Gaps: Oklahoma tariff, FAC/debt-reduction adjustment, Energy Flex effective date and new-customer availability; Energy Flex first-100-kWh tier read as on-peak kWh.
## 6235 Fayetteville PWC (NC) - 6 fetches
Captured RL, RLSWH, SPS, SPSWB from tariff PDFs (eff 2026-05-01). Gaps: PSA, 3-phase fixed charges (in notes), PWC TOU page blocked by Cloudflare, medium power not in scope.
## 19435 Union Power Cooperative (NC) - 4 fetches
Captured GS (res + non-res), RTS, GTS from rate schedule PDF (bills on/after 2024-04-01, latest posted). Gaps: newer revision may exist; WPCA; mid-month season boundaries (Apr 16/Oct 16) coded as whole months; CS/CTS three-phase not coded; PS prepaid not coded.
## 13441 New Hampshire Electric Coop (NH) - 4 fetches
Captured B, TDF/TDN, EVN/EVF, B2, B32, TDF2/TDN2 from Aug 2026 schedule of rates (effective billing rate = bundled). Gaps: TDF2/TDN2 hours assumed same as whole-house TOD (not stated for general); net-metering TOU rates, >400 A rates, demand classes not coded.
## 18976 Trinity Valley EC (TX) - 2 fetches
Captured Residential and Commercial Single Phase from tvec.net/rates (April 2026 column). Gaps: PCRF, prepaid, three-phase/large power, no TOU found.
## 9777 BrightRidge / Johnson City (TN) - 4 fetches
Captured RS, GSA 1, GSA 2 from October 2026 rate PDF. Total kWh rate includes monthly-varying FCA (Oct 2026 only). Gaps: no TOU rate found (EV charging flat $0.23897 + $100 base charge listed, not coded), GSA 2 eligibility range, GSA 3.
## 5399 Duck River EMC (TN) - 6 fetches (OCR of image PDF, checked visually)
Captured RS and GSA Part 1 (eff 2026-10-01), base energy only; FCA in notes. Gaps: no TOU/EV rate found (1 search), GSA Part 2/3 not coded.
## 24590 Unitil Energy Systems (NH) - 9 fetches (puc.nh.gov and some unitil.com pages blocked/dynamic)
Captured R (delivery only), R fixed energy service (supply only), TOU-R, TOU-EV-R, G2 (delivery only, demand), G2 supply-only, TOU-EV-G2 from unitil.com rate sheets (eff 2026-09-01). Gaps: Feb-Jul supply rate for TOU rows and supply rows uses the current-year 2026 value (resets Feb 1); variable energy service not coded; PUC tariff PDF 403.
