# Phase B batch 1 log (2026-10-16)
Validation: ALL OK (every schedule+day_type with energy rows covers 12x24 once, tier 0). Schedule with no energy rows: CEI Rate GS (no per-kWh distribution charge on sheet).

## 44372 Oncor (TX) - ~9 fetches
Captured: residential delivery (fixed 4.23, distribution 0.025344). STALE: Oncor's own residential sheet ends 2025 (Sep-Oct 2025 column). Gaps: 2026 rates (tariff PDF text truncated before Chapter 6 on every offset), small commercial (Secondary <=10 kW), riders not added. No TOU/EV delivery rate exists/found.
## 8901 CenterPoint Houston Electric (TX) - 3 fetches
Captured: residential delivery (fixed 4.90, base 0.023240; riders in note; page has no effective date). Gaps: small commercial (page fetch failed), PUC tariff PDF excerpt lacked rates.
## 3046 Duke Energy Progress NC - BLOCKED
5 fetches (duke-energy.com rate pages and RES/R-TOUD PDFs) all returned client error. Nothing captured. Found URLs for retry: .../for-your-home/rates/electric-nc/r1ncscheduleresdep.pdf (RES), r2ncschedulertouddep.pdf (R-TOUD).
## 733 Appalachian Power - ~4 fetches
State changed to Virginia (largest; also WV). Captured RS, RS-SD, RS-TOD, RS-STOU, SGS, SGS Load Mgmt TOD (all effective 2025-01-01, bundled). Gaps: P.E.V. (EV) schedule terms, G.S., WV tariff, RS-E/closed schedules skipped, riders not added, holidays not coded.
## 3278 AEP Texas Central (TX) - 4 fetches
Tariff PDF (Sept 29 2026) text truncated before Chapter 6; Aug 28 URL errored. Nothing captured. Gap: residential and SVC<=10 kW delivery rates.
## 18454 Tampa Electric (FL) - 6 fetches
Captured RS, RSVP-1 (flat 9.435c; P4 price unread), GS, GST, GSD from tariff Section 6 (2026-01-01), base energy only, all-in insert totals in notes. RS fixed stored as $0.45/day. Gaps: RSVP-1 P4, GSDT/GSD-option, EV schedule not looked for in tariff beyond insert (none listed).
## 17539 Dominion Energy South Carolina - 8 fetches
Captured Rate 8, 5, 7, 9, 16 (effective July 2026, bundled). Inferred items flagged: Rate 8 block mapping and daily fixed. Gaps: Rate 2 (low use), Rate 6, Rate 28 (small GS TOU demand), EV rate; weekday/weekend for rates 5/7/16 coded same.
## 3755 Cleveland Electric Illuminating (OH) - 5 fetches
Captured delivery-only RS and GS base rates (sheets dated 2009-05-01; riders unread, may be reset by recent rate case) and SSO price to compare 0.091107 (effective 2025-06-01, likely superseded). Gaps: Summary Rider, Rider 114 generation, GS TOU, current PTC, any residential TOU.
