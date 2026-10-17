# Phase B batch 8 log (2026-10-16)
Validation: each schedule+day_type covers 12x24 once; ALL OK (21 tariff rows, 98 period rows). Period ids: one per distinct price per schedule.

- 5202 Dixie Electric Membership Corp (LA): captured Res A, Comm B (delivery charge only; monthly Wholesale Power Charge not in tariff, excluded). Gap: experimental Res TOU RTU/RTUAE (on/shoulder kWh capped per month, odd structure) not coded; BTU closed. Fetches: 2 (LPSC tariff PDFs; one older Order U-35359 copy unused).
- 17684 Southwest Louisiana EMC (SLEMCO, LA): NOT captured. slemco.com has no tariff page; the only LPSC doc found is 2023 rate-case testimony (proposed rates, not tariff); nectarclimate blocked (403). Fetches: ~6.
- 3093 Carroll Electric Coop (AR): captured Rate 1 (res + C&I), Rate 2 three-phase C&I from carrollecc.com/rates + APSC tariff PDF. Effective date not stated (filing date only). No TOU/EV rate in tariff. Rate 3 (100-250 kW) skipped. Fetches: 3.
- 25177 Dakota Electric Assn (MN): captured Sch 31, EV-1, 41, 46 (no periods: kW-blocked energy), 54 (demand TOD). Sch 32 closed. RTA excluded. Fetches: 4.
- 3522 Chugach Electric (AK): captured Res + Small General for South and North districts (stated all-in totals). TOU pilot has no numeric rates published: gap. Fetches: 4.
- 5070 Delaware Electric Coop (DE): captured R, R-BTP, GS, GS-TOU from tariff revised Mar 2025 (delivery+supply summed incl. printed PCA -0.0015). EV riders are credit programs, not rates. Delaware.coop HTML 403; PDFs OK. Fetches: 6.
- 16088 City of Riverside (CA): captured D, D-TOU, A (flat <20 kW), 2026 column. Gaps: Sch EV closed to new; A demand-basis (20-150 kW) not coded; reliability/network flat charges in note only. Fetches: 6.
- 11292 City of Lubbock (TX): NOT captured. lpandl.com / ci.lubbock.tx.us / lubbockpower.com blocked (403/reset); WebFetch failed. LP&L is a delivery-only TDU in ERCOT. Fetches: 6.
