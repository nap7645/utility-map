# Phase B retry log, batch R (2026-10-16)
Validation: ALL OK (every eia_id+schedule+day_type with period rows covers 12x24 once). Schedules with no energy rows: AEP TX SVC>10 kW, TNMP SS>5 kW, Duke OH DS (demand-only on sheet). Files: bR_tariffs.csv, bR_periods.csv (14 tariff rows).

## 3278 AEP Texas Central (TX) - CAPTURED, ~4 fetches
curl of aeptexas.com tariff PDF (Eff Sept 29 2026) gave full text (373 pp). Residential, SVC<=10 kW, SVC>10 kW delivery rates (sheet rev. first effective bills on/after 2024-10-01). Delivery only; rider values (TCRF, EECRF, DCRF, TC-3, etc.) not read. No TOU/EV rate in tariff. Gap: rider totals.
## 40051 Texas-New Mexico Power (TX) - CAPTURED, ~3 fetches
tnmp.com Retail Tariff (58964) full text via pdftotext (rate sheets eff 2026-09-13, Rev 14). Residential, SS<=5 kW, SS>5 kW delivery. Gap: rider values (SBF, TCRF, DCRF, EECRF, HCRF, RCE, IS); NM not captured. Note the earlier-seen retailer-page $7.56 fixed matches 1.70+5.86.
## 3542 Duke Energy Ohio (OH) - CAPTURED (distribution only), ~5 fetches
duke-energy.com 403; used PUCO-hosted P.U.C.O. Electric No. 19 consolidated PDF (268 pp). RS, TD, TD-CPP (availability unconfirmed), DM, DS distribution charges eff 2023-01-03. Gaps: SSO supply riders (RC/RE etc. values in file are 2024-25 vintage, not coded), ORH skipped (blocks relative to demand), file may predate any later rate change, holidays not coded, TD-CPP critical-peak price not in periods.
## 12825 NorthWestern Energy (MT) - CAPTURED (bundled, incl. tax), ~5 fetches
Tariff PDFs are image-only, but the rates-at-a-glance.xlsx parses (sheet dated 2026-10-15): Residential, GS-1 Secondary Non-Demand, GS-1 Secondary Demand. Rates include taxes and the monthly-varying supply component. Gap: no TOU (RSGTOUD-1 demo expired 2014); effective_date blank; demand eligibility threshold unread.
## 10005 Evergy Kansas South (KS) - NOT CAPTURED, ~7 fetches
evergy.com / bcg.evergy.com return 403 "Page Blocked" or captcha to cloud IPs (curl and WebFetch); archive.org snapshot unavailable. CURB (curb.kansas.gov) publishes only Evergy Kansas Central and Metro rate histories (Central residential 2026: $15.25, 9.126c/kWh etc.), not South. Nothing coded.
## 13780 Northern States Power MN (MN) - NOT CAPTURED, ~7 fetches
Only rate book retrievable (Me_Section_5.pdf) is still the 2024 vintage (latest sheet eff 2024-06-07; A01 $6.00, 13.069c summer/11.364c other); superseded by rate case E002/GR-24-320 (interim rates 2025, final later). Current 2026 rate book not found (rate_books page links not resolvable). Not coded. Xcel filed 2026-10-09 a Customer Rate Stability Plan (base rates held 2027-28 if approved).
