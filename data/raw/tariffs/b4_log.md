# Phase B batch 4 log (2026-10-16)

Output: b4_tariffs.csv (30 schedules), b4_periods.csv (120 rows). Validation: every schedule x day_type covers 12x24 exactly once (ALL OK). Fetch counts are approximate (PDF/HTML downloads plus searches).

## 20885 Withlacoochee River Elec Coop (FL, HIFLD FL) - ~4 fetches
Captured RR (residential, 2 tiers) and GS (<=49 kW). Source: FL PSC rate filing 02427-2025 (effective 5/1/2025). Gaps: no residential TOU/EV found; fuel adjustment and riders not on the tariff sheet (not coded); LP demand schedule not coded; wrec.net rate pages 404; no later revision checked.

## 10857 Lee County Electric Coop (FL) - ~3 fetches
Captured RS (3 tiers), GS, GSD (>20 kW). Source: LCEC Tariff Vol. 3 PDF (rate sheets effective 1/1/2024). Gaps: PCA/tax adjustment not coded; RSL load-management rate closed to new customers (not coded); GSD-O (load factor) not coded; no TOU/EV rate.

## 18304 Sumter Electric Coop / SECO (FL) - ~2 fetches
Captured RS, RS-TOU, GS, GSD. Source: SECO rate tariff PDF (cover Oct 1 2025; sheets effective May 1 2025). Gaps: WPCA current factor not stated; RS-LM load management and public EV charging (sheet 9.3) not coded; LGSD/GSDI not coded.

## 3660 PUD No 1 of Clark County (WA) - ~5 fetches
Captured residential flat ($19 basic, 8.79 c/kWh), Schedule 34, Schedule 434. Source: Clark Public Utilities rates web page. Caveats: curl returned 403, content read via WebFetch (summary, not raw text); no tariff PDF found; no electric effective date on page; residential schedule number not stated. Gaps: Schedules 134/234 (second tier, >100 kW) and off-peak demand special-contract option not coded; no residential TOU listed.

## 3916 Cobb EMC (GA) - ~12 fetches
Captured residential R-12 Standard, Fixed, NiteFlex (TOU with 400 kWh free super off-peak), SmartChoice R-14 (peak-notification charge coded in demand_flat); commercial CS-14 Rate 30, Rate 14T (experimental TOU), CEV1 (EV charging). Source: cobbemc.com 2026 schedule PDFs (effective 1/1/2026). Gaps: Even Bill (budget plan), Seniors SP-12, Rate 40 (not read), DG schedule not coded; PCA factor not stated; Printable rate table PDF is stale (differs from schedules) and was not used.

## 10421 Knoxville Utilities Board (TN) - ~12 fetches
Captured RS, RS-TOU, GSA tier 1 (<=50 kW and <=15,000 kWh), GSA-TOU tier 1. Source: kub.org/uploads PDFs, latest revision numbers found by probing (RS_1203, RS-TOU_77, GSA_118, GSA-TOU_77; rates inclusive of PPA effective 9/1/2026; there was no index page link). Gaps: GSA tiers 2-3 (>50 kW) and GSA-TOU tiers 2A/2B not coded; holidays not coded; PPA changes periodically.

## 20404 AEP Texas North (TX, HIFLD TX) - ~6 fetches
Delivery only (competitive supply; no price-to-compare). Captured Residential Service and Secondary <=10 kW. Source: AEP Texas Tariff for Retail Delivery Service (compilation dated Sept 29 2026; sheet first effective 10/1/2024). Riders (TCRF, EECRF, DCRF, etc.) not coded; PUCT all-in volumetric figures given in note. Gaps: Secondary >10 kW (demand schedule, distribution $7.148/kW NCP) not coded; no TOU delivery rate.

## 3408 City of Chattanooga / EPB (TN) - ~12 fetches
Captured RS Base Rate Plan, Night Shift (NRS), Time Shift (TRS), GSA tier 1, GSA 50-1,000 kW. Source: EPB rate schedule PDFs (header Effective October 2024). Note: older "BRANDED_*" PDFs on static.epb.com carry different, stale rates (e.g. 9.095 c/kWh) and were not used; the Oct 2024 schedule rates reconcile with EPB's web page total (base + ~$0.029 fuel adj as of 11/1/24). TVA fuel cost adjustment not coded (varies monthly). Gaps: Second Space Night Shift (TSRS), EVC EV charging schedule, GSAC, TDGSA and larger schedules not coded.
