# Independent verification: audit dollar and presence fixes (2026-10-12)

Scope:
- 31 program rows in `audit/fixlog_dollars_2026-10-12.json`, checked against `data/processed/programs.csv`.
- 12 presence flips in `data/raw/presence_scan/scan_AUDIT.csv` and `docs/data/presence.json`.

Method:
- All pages were fetched with WebFetch only. No Wayback was used.
- I did not edit any dataset file.

## A. Transcription check (fixlog new value vs programs.csv vs auditor correct_value)

Every non-`last_verified` fixlog entry for programs.csv was compared against the CSV. All 31 rows matched exactly. Each row has exactly one match on utility_name + program_name.

| # | Utility / program | CSV == fixlog new | Matches auditor correct_value | Issue |
|---|---|---|---|---|
| 1 | Ameren IL, Rider CGR | Yes | Yes (verbatim) | Auditor wording "valid only through 2024-12-31" is itself wrong (see B) |
| 2 | Consumers, AC Peak Cycling | Yes | Yes | none |
| 3 | Consumers, DG (Inflow-Outflow) | Yes | Yes | Minor: event_limits "DG cap raised to 4% of peak load" is not on the new source page |
| 4 | NSP-MN, Saver's Switch | Yes | Yes | event_limits "max 300 control hours/yr, ~2-7pm" probably carried over from the old Colorado DSM doc. It is unverified for MN |
| 5 | Xcel CO, SG | Yes | Yes, plus "flat demand $9.66/kW" | The $9.66 is real (it is on OpenEI). Problem: source_url still points to the May-2024 brochure, not to where the figures came from |
| 6 | Xcel CO, PG | Yes (values withdrawn) | Yes | none |
| 7 | Xcel CO, S-EV | Yes (values withdrawn) | Yes | Stale figures remain: peak_offpeak_rates still holds the 2024-brochure base energy rates (12.636c/2.528c/6.319c/1.264c, ECA 4.185c/2.092c), from the same vintage that was withdrawn |
| 8 | PacifiCorp, Irrigation Load Control | Yes | Yes | none |
| 9 | PacifiCorp ID, Sched 136 | Yes | Yes | source_url is still the RMP page, which says "Proposed, under review". That contradicts status=Active |
| 10 | PSE, Sch 307 | Yes | Yes | none |
| 11 | FPL, CILC-1 | Yes | Yes | none |
| 12-13 | NYSEG Term-DLM / Auto-DLM | Yes | Yes | none |
| 14-16 | HECO / HELCO / MECO TOU-RI | Yes | Yes | none |
| 17-19 | Shift and Save x3 | Yes | Yes | none |
| 20-22 | ARD TOU G/J x3 | Yes | Yes | none |
| 23-24 | Sched J/P Oahu, Hawaii Island | Yes | Yes | none |
| 25 | **Sched J/P Maui County** | Yes | **No** | Auditor said 57.38c (J) and $21.20/kW + 49.41c (P) are **Molokai**. The fix stored them as **Lanai**, and stored Lanai's figures as Maui's. See B |
| 26-28 | Commercial EV-J/EV-P x3 | Yes | Yes | none |
| 29-31 | SCE TOU-D 4-9PM / 5-8PM / PRIME | Yes | Yes | none |

Units: no unit was lost in any row (c/kWh, $/kW, $/kW-yr and $/mo are all retained).

## B. Source re-check of the judgment-call rows

| Row | Source fetched | Verdict | Finding |
|---|---|---|---|
| Xcel CO SG | OpenEI 69bda768... | **INCONCLUSIVE** (figures CONFIRMED) | **Figures:** OpenEI confirms S&F $91.79, energy $0.04771, flat demand $9.66, and TOU demand periods 1 and 2 at $19.79 and $27.14. **Mapping:** the month grids show period 1 only. The flattened 288-character weekday string has a single central run of period 2, which suggests period 2 ($27.14) = summer (Jun-Sep, per the PSCo tariff definition) and period 1 ($19.79) = winter. Confidence is medium. **Unconfirmed:** whether $9.66 adds to these charges. The OpenEI record is titled "Secondary General Service Time-Differentiated Demand Charge", so it may be a variant of SG. **Other sources:** the PSCo tariff PDF on xcelenergy.com is the 2021 edition (S&F $39.62), so it is unusable. **source_url:** the 2024 brochure is not appropriate. Use the OpenEI URL until the current PSCo tariff can be read |
| PacifiCorp ID Sched 136 | IPUC press release, RMP page | CONFIRMED (figures and status) | Order 36845 (Nov 14, 2025) approved a time-differentiated export credit rate averaging 4.2c/kWh, in place until the update filing on 2028-07-01. The RMP page is stale ("Proposed, ~4c, eff. 2025-10-01"). Change source_url to the IPUC release |
| Xcel MN Saver's Switch | MN 2022 booklet, MN rate book Section 5 | CONFIRMED for 2022; INCONCLUSIVE for current | The booklet says "Save 15% on your summer electric energy charges (June-September)". The mn.my page renders with JS only. The MN rate book text is truncated before Sheet 5-97, but Sheet 5-4.3 still refers to the rider's "percent discounts". This is weak support that the rider is current. The row's own caveat is accurate |
| **HECO Maui Sched J/P** | efs_2026_10.pdf, cross-checked against the TOU-RI Sched R baselines | **WRONG** | The extracted J/P blocks carry Sched R first-tier rates of 44.59c, 60.71c and 58.42c. These match the TOU-RI page's Sched R for Maui (44.6), Lanai (60.7) and Molokai (58.4). Correct values: **Maui** J $15.31 + 40.83c, P $29.44 + 37.54c. **Lanai** J $15.31 + 62.27c, P $29.44 + 60.00c. **Molokai** J $15.31 + 57.38c, P $21.20 + 49.41c. This agrees with the auditor's Molokai attribution, and with September's $21.20 Molokai P demand charge and its month-over-month continuity |
| FPL CILC-1 | bus-eff-jan-2026.pdf | CONFIRMED | CILC-1(G): max demand $5.67, firm on-peak $14.17, load-control on-peak $3.73 |
| **Ameren IL Rider CGR** | aiel59rdcgr.ashx (Sheet 59.003, eff. 2025-04-21) | **WRONG** (validity wording) | The $300/$250 values are confirmed. But the tariff says they apply "prior to December 31, 2024 or until" the effective date of the new compensation tariff under 220 ILCS 5/16-107.6(c), "whichever is later". The sheet was re-filed under PA 103-1066 and is effective 2025-04-21, so the values are not limited to 2024. Also, "competitive" refers to ICC-declared competitive delivery classes (DS-3/DS-4), not geographic areas |
| Consumers DG | utility DG page | CONFIRMED | Credited at the power supply rate including transmission (C.11.3). Since 2024-02-27, credits apply to all electric charges. No c/kWh figure is given |
| PSE Sch 307 | elec_sch_307.pdf | CONFIRMED | From 2026-01-29: 53.2445 / 10.8197 / 33.5186 / 10.8197 c/kWh |
| SCE TOU-D-4-9PM | sce.com TOU page | CONFIRMED | 59/33/44/33/50/32/36c. Baseline credit $0.09, BSC $0.79/day, HPWH allocation 1.9/2.6 kWh/day |
| HECO TOU-RI (Maui County row) | tou-ri-rate-history | CONFIRMED | Oct 2026, on/mid/off (Sched R): Maui 55.5/30.8/54.5 (44.6). Lanai 71.6/49.2/68.4 (60.7). Molokai 66.9/45.8/66.9 (58.4) |

## C. The 12 flipped presence cells (src from docs/data/presence.json)

| Utility | Cell | src | Verdict | Evidence |
|---|---|---|---|---|
| DTE Electric | ci_habit | BusinessElectricRates.pdf | CONFIRMED | Commercial TOU D3.11 (1-5pm), Primary TOU D14, D11 on/off-peak, R10 real-time LMP |
| Consumers | ci_habit | business time-of-use-rate-plan | CONFIRMED | Business "Time of Use" plan, cheaper nights and weekends |
| Consumers | ci_dispatch | business demand-response | CONFIRMED | C&I DR program, $20-25/kW summer and $8-9/kW other seasons, events 11am-7pm |
| Ameren Missouri | ci_habit | uecdsheet55rate2msgs (SGS 2(M)) | CONFIRMED | Optional Overnight Saver and Optional TOD service |
| Ameren Missouri | ci_dispatch | missouri/business/demand-response | CONFIRMED | C&I Demand Response Program (Enel X) |
| I&M Michigan | ci_habit | MI tariff book 2026-08-28 | CONFIRMED | GS-TOD, GS-TOD2, GS-CPP (verified from the table of contents; the tariff sheets themselves were cut off in the fetch) |
| LADWP | ci_habit | standard C&I rates | CONFIRMED | Rate B small commercial TOU and A-2B TOU, with high- and low-peak periods |
| United Power | ci_habit | 2026 rates PDF | CONFIRMED | Small Commercial TOU CTD1 (on-peak 22.49c 5-9pm). Coincident-peak CPS1/CPP1 and ITD rates |
| Black Hills CO | ci_dispatch | coe-rates-tariff_0.pdf | CONFIRMED | Interruptible Rider (p.79) and Voluntary Load Curtailment Rider (p.72) are in the table of contents, and LGS-S is "subject to the interruptible rider". The tariff PDF is dated 2019-10-10 |
| LG&E | res_dispatch | lge-ku.com/demand-conservation | CONFIRMED | Demand Conservation is closed to new enrollment, but the same page offers active residential BYOT smart-thermostat DR |
| KU | res_dispatch | same | CONFIRMED | same |
| Niagara Mohawk | ci_habit | Upstate-NY-Business Service-Rates | CONFIRMED | SC-3A Large General TOU with hourly supply pricing. EV Phase-In TOU rate |

Out of scope, but noticed: LADWP's `cds` and Niagara Mohawk's `cds` point to residential program pages. Those cells were not part of this fix.

## Corrections needed

1. `data/processed/programs.csv` (and the source chunk file `data/raw/program_chunks/chunk_AKHI.csv`), Maui Electric Co (Maui County), "Schedule J / Schedule P general service demand rates", `peak_offpeak_rates`:
   - Replace with: `Eff. 10/1/2026 (eff. 2026-10-01; adjusts monthly (see utility Effective Rate Summary)) Sched J: Maui $15.31/kW + 40.83c/kWh; Lanai $15.31/kW + 62.27c/kWh; Molokai $15.31/kW + 57.38c/kWh; Sched P: Maui $29.44/kW + 37.54c/kWh; Lanai $29.44/kW + 60.00c/kWh; Molokai $21.20/kW + 49.41c/kWh`
2. `programs.csv`, Ameren Illinois, Rider CGR, `incentive_value_usd`:
   - Replace the validity clause with: `values apply through the later of 2024-12-31 or the effective date of the new compensation tariff under 220 ILCS 5/16-107.6(c) (Sheet 59.003 eff. 2025-04-21)`.
   - Replace "competitive areas" with "competitive delivery classes (DS-3/DS-4)".
3. `programs.csv`, Xcel CO, Secondary General Service (SG), `source_url`:
   - Change to `https://openei.org/IURDB/rate/view/69bda768f0300279d30f154c` (or the current PSCo tariff sheet).
   - Optional: in `incentive_value_usd`, change "period/season mapping not confirmed" to "likely $27.14 summer Jun-Sep / $19.79 winter per OpenEI schedule; unconfirmed".
4. `programs.csv`, Xcel CO, S-EV, `peak_offpeak_rates`:
   - Withdraw the 2024 brochure energy rates (same staleness as the withdrawn demand and S&F figures). Alternatively, label them "eff. 2024-05-01 (stale)".
5. `programs.csv`, PacifiCorp, Net Billing Service (Schedule 136), `source_url`:
   - Change to `https://puc.idaho.gov/Fileroom/PublicFiles/Press/20251117Rocky Mountain Power 1117 Release.pdf.pdf`. The current RMP page still says "Proposed".
6. Minor:
   - NSP-MN Saver's Switch, `event_limits`: clear "max 300 control hours/yr...", or mark it unverified for MN.
   - Consumers DG, `event_limits`: the "4% of peak load" cap is not on the cited page.
