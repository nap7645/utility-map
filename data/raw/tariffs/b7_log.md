# Phase B2 batch 7 log (2026-10-16)

## 12745 Modesto Irrigation District (CA) - CAPTURED, ~4 fetches
D (default), EV-D pilot TOU (EV owners only, experimental), GS-1 (default, <=20 kW), GS-2 (20-1,000 kW demand). Source: mid.org electric rates page PDFs. Gaps: DLS medical rate and CARES discount not coded; GS-TOU is 500-1,000 kW (not coded); power cost adjustment not on sheets. No residential non-pilot TOU.

## 19159 Tri-County Electric Coop (TX) - CAPTURED, 3 fetches
202.1 Residential (default), 202.2 General Service (default). Tariff Jan 2024; TCEC 2025 rate-adjustment page confirms unchanged totals. Gaps: no residential or small-commercial TOU/EV; PCRF/Brazos riders excluded.

## 38084 Great Lakes Energy Coop (MI) - CAPTURED, ~4 fetches
A (default), GS single-phase (default) and three-phase, from MPSC rate book (issued 2026-04-14, rates eff 2025-11-01). gtlakes.com blocked (403). Gaps: no TOU/EV; PSCR factor (D-1.00) and EO surcharge not included; A-S and EEH discount not coded.

## 18085 South Central Power Co (OH) - CAPTURED, ~5 fetches
R, SGS (default), MGS (50-350 kW). Base rates only ($0.026/kWh, $0.01 MGS): G&T pass-through (Rider B, monthly, no value on tariff) excluded - prices are materially understated vs all-in. No TOU/EV.

## 19898 Volunteer Energy Coop (TN) - CAPTURED, ~6 fetches
RS (default), GSA Part 1 (default), GSA Part 2 (50-1,000 kW). April 2026 sheets; TVA fuel cost excluded; seasons are billing months (Jun-Sep, Dec-Mar, Apr-May/Oct-Nov). vec.org blocks curl but PDFs downloadable. Gaps: no TOU/EV; SRS supplemental not coded.

## 590 City of Anaheim (CA) - CAPTURED, ~7 fetches
D (default), TOU-2, GS-1 Rate A (default), GS-1 Rate B (demand). anaheim.gov blocks curl (Cloudflare); read via WebFetch. Gaps: RSA adjustment not stated; DEV-D-EV closed; holidays not coded; page vs tariff 33.22/33.20 discrepancy (tariff used).

## 18445 City of Tallahassee (FL) - CAPTURED, ~4 fetches
RS (default), RST (optional TOU), GS (default, <25 kW). Filing is redlined scan; values read from page images. Non-fuel energy only (fuel/energy cost recovery excluded). Oct 2026 CPI revision not found. Gaps: GSD not coded (kWh-per-kW blocks), no small-commercial TOU.

## 17833 City Utilities of Springfield (MO) - CAPTURED, ~7 fetches
Residential, General Lighting (default small commercial), General Power (<200 kW, 3-phase). Used 'Thereafter' column (eff Cycle 1 Apr 2026). Per-kWh block "demand" component summed with energy. Fuel adjustment excluded. Gaps: no TOU/EV for res or small commercial found (TOU peak definition 8am-11pm M-F exists for larger classes only).
