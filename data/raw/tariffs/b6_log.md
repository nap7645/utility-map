# Phase B log, batch 6 (2026-10-16)

Validation: every schedule + day_type covers 12x24 exactly once for tier 0; tariffs/periods schedule sets match; one period id per distinct price within a schedule; min_bill numeric or blank. "ALL OK" (25 schedules, 126 period rows).

Common caveat: base rates only; per-kWh riders/adjusters/fuel are listed in each note and NOT added (except where noted). Holidays not coded anywhere.

## Duke Energy Kentucky (19446), KY. ~4 fetches
Captured: RS Residential (default, flat), DS Secondary Distribution (C&I demand, tier 0 only). Source: KY PSC Tariff.pdf (duke-energy.com not needed).
Gaps: no residential TOU/EV rate in tariff index. DS energy blocks 2-3 are kWh-per-kW based, not codable. Riders ESM/DSMR/FAC/PSM amounts not read. GS-FL, EH, RT not coded.

## Montana-Dakota Utilities (12199), captured ND. ~9 fetches
Captured: Rate 10, Rate 16 (TOU), Rate 20, Rate 26 (TOU). NDPSC interim sheets eff 2026-09-01.
Gaps: 26.118% interim rate increase (PU-26-241) NOT applied, so billed rates ~26% above coded. Riders 55-59 not read. Rate 13 thermal storage, Rate 30 General not coded. Older URL (ND_Electric10.pdf) 404 and a 2022 PSC filing were discarded as stale.

## Greystone Power (7090), GA. ~6 fetches
Captured: Rate 1 RS, Rate 300 EV (whole-home TOU), Rate 3 SC. Tariffs effective 2021-06-01 (still posted).
Gaps: WPCA/ECCR/DSM/Wallet Watch/fee riders not read. General Service not coded.

## Connexus Energy (689), MN. ~5 fetches
Captured: Residential, Residential Time-of-Day, Small Commercial (rate book eff 2026-01-01).
Gaps: PCA rider not read. EV Subscription, EV off-peak (closed), General Commercial (kWh/kW blocks), EV Fleet pilot not coded.

## Otter Tail Power (14232), captured MN (62k customers vs 59k ND). ~12 fetches
Captured: M101, M241 RDC, M781 Off-Peak EV, M404 Small General. MN PUC tariff sheets.
Gaps: Interim increase eff 2026-01-01 (E017/GR-25-359) not in sheets, amount unknown, so rates may be understated. M781 penalty-period price interpretation ambiguous (flagged in note). TOD pilot closed, not coded. Riders not read. otpco.com/pricing page and TOD pilot PDF (empty download) partly unreadable.

## Walton EMC (20065), GA. ~6 fetches
Captured: Standard Residential Rate (only residential plan listed). Effective date not stated.
Gaps: commercial GS-12 not coded (energy blocks by kWh/kW, service $50; eff 2025-02-01 per page) -- no small-commercial row. Site blocks curl (403); content from WebFetch summaries (3 consistent reads). PCA not read.

## Magic Valley Electric (11501), TX. ~4 fetches
Captured: Residential ($28.25, $0.09187, 'as of Feb 2025'), General Service <50 kW ($34.00, $0.09187, undated).
Gaps: no tariff PDF found; schedule names/riders not on pages.

## City of Lakeland (10623), FL. ~8 fetches
Captured: RS Standard, RSD Demand, RSX-1 Shift to Save, GS, GSBD, GSX-1 (all <50 kW commercial). Rate sheets effective 2026-10-01.
Gaps: fuel ($0.047 / 0.057387 on-peak / 0.042488 off-peak) and environmental ($0.0018506) adders NOT included (listed in notes). Commercial demand peak window not stated. Hours for TOU from PSC tariff Sheet 7.1/7.4 (filed 12/2025).
