# Phase B batch 9 log (2026-10-16)

Files: b9_tariffs.csv (27 schedules), b9_periods.csv (157 rows). Validation: 12x24 coverage per schedule/day_type/tier, one price per period id, numeric min_bill: ALL OK.

## United Power (19499, CO) - ~5 fetches
Captured: R1 (default), RTD1, RDP1, RD1 residential; C1, CTD1 small commercial. Sources: 2026 residential rate-page PDF and Jan 2026 redlined tariff PDF (new = second value in redline).
Gaps: PCA (wholesale power cost adjustment) values not read; Saturday on-peak (Mon-Sat peak) not representable in weekday/weekend split; no separate commercial rate-page PDF found (guessed URLs 404), commercial taken from tariff redline.

## Black Hills Colorado Electric (56146, CO) - 3 fetches
Captured: RS-1 (tiered), RS-TOU (pilot), SGS-N, SGS-TOU (400-customer cap). Source: full CO PUC No. 11 tariff PDF (sheets effective Mar-May 2025).
Gaps: ECA/DSMCA/GRSA riders not read; tariff compiled PDF may predate later sheet revisions; SGS-Large (10-50 kW) same rates as SGS-N, not coded separately.

## UNS Electric (19728, AZ) - 6 fetches
uesaz.com blocked by Cloudflare for curl; link list via WebFetch, PDFs from docs.uesaz.com worked. Captured: ERRES, ERREST, ERSOTE (EV), EGSGS, EGSGST. Not coded: demand TOU residential (ERRESD/ERRESDT/ERRDTT/ERDSOTE) and SGS demand (EGSGSD/EGSGSDT) - lower priority/closed? (availability not checked).
Gaps: sheets effective 2024-02-01; newer rate case not verified; PPFAC excluded; holidays not coded.

## Gainesville Regional Utilities (6909, FL) - 4 fetches
Captured: residential regular, GS non-demand, GS non-demand TOU (FY26 sheets eff. 2025-10-01). No residential TOU/EV on residential sheet. Fuel adjustment $0.035/kWh excluded.

## Cumberland EMC (4624, TN) - 7 fetches
Captured: RS, GSA (<=50 kW), by TVA season using three monthly sheets. No residential TOU/EV found. Fuel charge excluded; SRS not coded; GSA demand-charge threshold not stated.

## Snapping Shoals EMC (17832, GA) - 5 fetches
Captured: residential regular, GS. No TOU/EV found on site. PCA excluded; FlexPay prepaid not coded. Rate sheets effective 2024-01-01.

## North Georgia EMC (13716, GA) - 5 fetches
Captured: RS (22), TRS (32 TOU), GSA 1 (40/41). TMFC excluded. TOU hours from ngemc.com/time page; no tariff PDF text for hours.

## First Electric Coop (6342, AR) - 4 fetches
Captured: Rate 1/51, Rate 2. Cost of Energy / Cost of Debt Adjustment values not published. No TOU/EV found; effective date blank (schedule updated 06/26).
