# Phase B batch 10 log (2026-10-16)
Validation: ALL OK (27 tariff rows, 114 period rows; each schedule+day_type covers 12x24 once).
Common: riders/adjustments (PCA, WPCA, PSA, PCRF) not added; holidays not coded.

## 10704 Lansing BWL (MI) - ~5 fetches
Captured RES1 (default, on/off-peak), RESTOU, RES22 (EV), SC1, SCTOU. Source is the FY2027 hearing packet sheets marked "Proposed, effective 10/1/2026"; Board approval 2026-08-11 confirmed by BWL news release. Gaps: surcharge/rider schedule; final adopted tariff sheet not separately seen.
## 19490 United Cooperative Services (TX) - ~8 fetches
Captured 202.1 (res + non-res), 202.2 residential TOU (experimental, 500-member cap), 202.3 three-phase GS. Tariff effective 2024-11-01 (latest posted). Gaps: 202.6 three-phase TOU not coded, 202.3 min charge unread, PCRF/SCRF riders, newer tariff if any.
## 6022 EWEB (OR) - 5 fetches
Captured residential (delivery+energy summed) and Small General Service (WebFetch summary of non-residential page; not cross-checked against a PDF). Gaps: no effective date on commercial page, no TOU/EV rate exists on site, min bill not stated.
## 7752 GVEC (TX) - ~9 fetches
Captured G-1 (res + non-res) and G-3 from tariff PDF (eff 2025-11-01). Assumption flagged: G&T 0.085 taken from G-3 row of commercial page and 2023 notice, not stated for G-1. Gaps: current residential page blocked (403 to curl, fetch error), TOU (DG customers only) rates are images, not captured.
## 19281 Turlock Irrigation District (CA) - ~8 fetches
Captured DE, DT, CE, CT from tariff PDFs (2026 column, eff 2026-01-01). Gaps: PSA and surcharges; CT URL guessed by pattern and verified by download; other small schedules not listed.
## 13337 NPPD (NE) - ~9 fetches
Captured RS, RS-TOU, GS from tariff PDFs (eff 2026-01-01). Gaps: PCA rider, base-rate adjustment for LP/DS/GRT, GS demand schedule (large), no small-commercial TOU.
## 6411 Flint EMC (GA) - ~5 fetches
Captured FR-31, EVTOU-7, FSGS-34, FGS-26 from 2026 rates PDF (eff 2026-04-01). Gaps: WPCA, any Flint TOU beyond EV.
## 8786 Horry Electric Coop (SC) - ~5 fetches
Captured Rate 900 and Rate 912 (flat energy + peak-window kW charge; fixed is $/day). Gaps: rates page 403, no TOU energy rate found, WPCA, schedule list incomplete (guessed rate PDF URLs 404).
