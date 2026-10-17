# Phase B log, batch 5 (2026-10-16)

Validation: every schedule + day_type covers 12x24 exactly once for tier 0 (higher tiers subset of tier 0 cells); tariffs/periods schedule sets match. "ALL OK" (34 schedules, 175 period rows).

## 3757 Clay Electric Cooperative, FL - CAPTURED, ~3 fetches (1 failed)
R (default, 2 blocks), RT (TOU), GS (default C&I), GST (TOU). Source is the FL PSC filing 03392-2025 (rates eff 2025-06-01); Clay's own RateBook0625.pdf has no rate tables in its text layer; clayelectric.com RateSummarySchedule1023.pdf is a 404. RT (~100 customers) and GST (~50) are experimental/at-Cooperative's-option, flagged in note. GST on-peak read as $0.185 (OCR spacing). Gaps: PCA / tax adjustment sheets 14.0, 15.0 not read; GSD demand rates not in scope.

## 5860 Empire District Electric (Liberty), MO - CAPTURED, ~9 fetches
TC-RG (default, AMI), NS-RG, TP-RG (500-customer cap), TC-GS (default), NS-GS, TP-GS (200 cap). Rate Set 1 of 3 phase-in sets (eff 2026-04-05) coded. Summer coded Jun-Sep (actual: first 4 billing periods from Jun 16). Off-peak $0.02 credit folded into off-peak prices. Excludes FAC. Old PSC No. 5 RG sheet (2016) and web page 14.031c were stale; tariff PDFs used. Gaps: residential EV tariffs and Smart Charge pilot not captured; holidays not coded.

## 40228 Rappahannock Electric Cooperative, VA - CAPTURED, ~7 fetches
A-1 (default), A-1-TOU, B-1 (default small C&I). Delivery + supply summed per tier/season. PCA +$0.03426/kWh (eff 2026-05-01) and other riders NOT included (listed in note). Gaps: no small-commercial TOU found; A-2 farm/civic schedule not captured; SC&C filed date Oct 2024 is the latest on REC's page.

## 9336 CORE Electric Cooperative, CO - CAPTURED, ~2 fetches
A (default, on-peak demand), AT (TOU energy + demand), C (demand), CT (demand + TOU rider), SG1 (default), SG1T, SG3, SG3T. Part III effective 2026-01-01. Gap: ET frozen TOU commercial schedule excluded (closed).

## 14716 Pennsylvania Power Co, PA - CAPTURED, ~7 fetches (HIFLD state OH wrong; PA)
RS delivery only, RS Price-to-Compare (13.478c, supply only), GS-Small delivery only, GS PTC (13.73c). Distribution rates from FE PA tariff Supplement 40 (Jan 2025 rates); older cached Retail Tariff PDF (Supp 2, Jan 2024) was stale and not used. Gaps: TOU default service rider is PTC x multiplier (res on-peak 2-9pm M-F x1.6048, off-peak x0.8744, super off-peak 11pm-6am x0.6512), so not coded; riders (DSIC etc.) not folded in; GS-Medium not in scope.

## 11479 Madison Gas & Electric, WI - CAPTURED, ~4 fetches
Rg-1 (default), Rg-2A TOU, Cg-5 (default small C&I). Cg-3 small C&I TOU closed since 2021; Cg-4 (>20-200 kW TOU with per-kW/day demand) not coded. Rg-2A hours sum dist + base + adders. Holidays not coded. Fixed charge in $/day.

## 9216 Imperial Irrigation District, CA - PARTIAL, ~4 fetches
Residential and Small General Service 2026 column only, from IID Rate Update page via WebFetch (iid.com returns 403 to curl; schedule PDFs not found; mrsc.org result was an unrelated utility). Step effective date and schedule numbers not stated, TOU/EV/demand schedules not captured. Treat values as page-level (tier 2) pending a tariff PDF check.

## 17633 SIGECO / CenterPoint Energy Indiana South, IN - CAPTURED, ~2 fetches
RS (default), RS-CPP (pilot eff 2026-10-07, CPP events not coded), SGS (default), DGS-1. Energy + fuel + variable production summed (all stated in the rate schedule). Appendix A-L adjustments excluded. Gap: no residential TOU/EV schedule in tariff other than the CPP pilot.
