# Phase B log, batch 2 (2026-10-16)

HIFLD state corrections: Metropolitan Edison is Pennsylvania (not OH); I&M captured for Indiana (largest state; Michigan not captured).

## Entergy Arkansas (814), ~5 fetches
Captured: RS (default), REMT (optional TOU), SGS (small C&I, demand). Base rates only; Energy Cost Recovery Factor/Sched 17 riders excluded. Gaps: REMT open-to-new status unstated; no small-C&I TOU; 2026 rate case pending (not applied); tariff sheets dated 2019/2021.

## PSO (15474), ~6 fetches
Captured: RS (default), RSTOD, RSEV, GS. Gaps: GSTOD (sheet 15) and PL/PLTOD not retrievable (package PDF text truncated at 100k chars); GS tier boundaries depend on max kW (tier_max blank); RSTOD winter tier labeling ambiguous in source; RS-VPP/DR not in tariff.

## NIPSCO (13756), ~4 fetches
Captured: Rate 611 (RS), Rate 621 (GSS). Gaps: no TOU/EV residential rate in TOC; Appendix A riders not read; rate pages index 620/626 not read. Note energy 20.5c/kWh printed flat (single rate), taken as read.

## I&M (9324), ~6 fetches
Captured: R.S. (Indiana). Gaps: R.S.-TOD, TOD2, PEV, R.S.-D, G.S., G.S.-TOD (sheets 5-13) fall past the truncated PDF text (~109k chars); Sheet 44 riders not read; Michigan not captured.

## DP&L / AES Ohio (4922), ~8 fetches (aes.com vault host blocked by robots; aes-ohio.com mirror worked)
Captured: D17 and D18 distribution (delivery only), G10 Standard Offer residential, residential heating, secondary (generation only). Gaps: D19 Secondary distribution (fetch failed), riders D27-D41 rates, no TOU tariff in D2 index.

## Duke Energy Ohio (3542), ~7 fetches: BLOCKED
Only the PUCO tariff index was readable (RS sheet 30, ORH 31, TD-CPP 32, TD 33, DS 40, DM 43; all listed eff. 2023-01-03). Rate sheets and the SSO price not retrievable (duke-energy.com errors, PUCO PDF text truncated). No rows.

## West Penn Power (20387), ~9 fetches, and Metropolitan Edison (12390), ~3 fetches (both PA, FirstEnergy PA)
Captured only default-service PTC (generation) for residential and commercial, Jun 1-Nov 30 2026, from FE PA Supp. 36 (PUC filing). Distribution RS/GS-Small rates and TOU rider not retrievable (fe-pa-retail-tariff.pdf text truncated before p.61; PUC/URDB searches yielded nothing usable). PTC may have changed with Supp. 40 (eff. 2026-10-01). Dec 2025 PTC pages (WP res 10.948c, Met-Ed res 12.968c) superseded.
