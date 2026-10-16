# Phase B log, batch 3 (2026-10-16)

## 61432 Central Coast Community Energy (3CE), CA (PG&E-area, generation only) - CAPTURED, ~7 fetches
Residential E-1, E-TOU-B/C/D, EV-A/B, EV2-A, E-ELEC; commercial B-1, B-6, BEV1/BEV2S/BEV2P. 3CChoice column only (Prime/Flex not coded). SCE-area sheets not captured. Holidays not coded.

## 15263 Potomac Edison, MD - PARTIAL, ~8 fetches
Residential R (SOS) and R-TOU captured (dist+trans+SOS summed). Gaps: small-commercial Schedule G / C rates (rate-schedule pages beyond the fetch tool's text cap, ~120k chars); EV rider / MFH-EV rates; SOS admin charge not folded in. State (MD) per recollection.

## 12825 NorthWestern Energy, MT - NOT CAPTURED, ~9 fetches
Tariff PDFs (REDS-1, GSEDS-1) unreadable (no text layer); rates-at-a-glance.xlsx binary. Only datum: MT PSC 2026 summary, Jan-2026 residential: service chg $4.20/mo, total $0.151864/kWh (supply $0.076505); supply rate changes monthly and decreased 2026-10-01, so not coded (would be stale/estimate). No small-commercial or TOU numbers found.

## 10005 Evergy Kansas South, KS - NOT CAPTURED, ~7 fetches
Found Evergy Kansas CENTRAL rate-area rates (ks-central-rates.pdf, eff 2025-10-01: RS $15.25, RD, TOU, RTOU-2, SGS $27.49) but the doc states these are the Central rate area; no Kansas South rate-area residential/SGS sheets reachable (evergy.com tariff PDFs behind a captcha). Not coded to avoid mislabeling. Central rates available if the Central/South equivalence is confirmed.

## 40051 Texas-New Mexico Power, TX - NOT CAPTURED, ~9 fetches
Current retail tariff PDF (tnmp.com ...(20260901).pdf, and 58964 version) text truncated before Chapter 6 rate tables. Only third-party figures seen (retailer pages, conflicting: $7.56 vs $7.85 fixed), not coded.

## 7601 Green Mountain Power, VT - PARTIAL, ~7 fetches
Rate 1, Rate 6 (default C&I), Rate 8 (demand) at 2026-10-01 coded. Rate 11 TOU tariff row only (peak window "8 consecutive hours between 1-9pm Mon-Fri", exact hours not in tariff; no period rows, so TOU price validation skipped). Rates 9, 14, 22, 72, 74 not found at Oct-2026 values (website figures seen were older: Rate 22 and 74 summaries stale). No small-commercial TOU option found.

## 13780 Northern States Power (Xcel) MN - NOT CAPTURED, ~7 fetches
Only rate book found (Me_Section_5.pdf) is the 2024 vintage (eff 2024-01-01 / 2024-05-01, Residential A01 $6.00 + $0.13069 summer, A02 TOD, A08 EV, A72 TOU pilot, small general A10 and A12 TOD); superseded by later rate case, so not coded. Current 2026 rate book not located.

## 14154 Orange & Rockland, NY - PARTIAL, ~8 fetches
SC1 standard and SC1 TOU captured from O&R pages (undated, possibly pre-2025-04-01 rate order). TOU tariff row has no period rows (weekend treatment unstated). SC2 small commercial delivery rates not found. Price-to-compare table (SC1/SC2 monthly) fetched but row labels garbled; not coded. EV second-meter option not coded.

Validation: all schedule+day_type with period rows cover 12x24 exactly once ("ALL OK"). Tariff rows without period rows: GMP Rate 11, O&R SC1 TOU.
