# Independent verification — presence-scan fill pass (2026-10-02)

## Method
- Input: 42 changed cells (4 Yes, 38 No) from `changes.json`; prior values all `Unknown` (confirmed via `git diff HEAD`). Prior-agent notes were not used as evidence.
- Each **Yes**: opened the cited URL and checked it shows a current program of the right kind and segment.
- Each **No**: fetched the utility's own rates and/or programs pages (and tariff PDFs where reachable), plus one targeted web search per utility for TOU, EV, demand-response, load-control, interruptible, and peak programs. For AECI members, checked whether AECI runs a member DR program (it does not: aeci.org/take-control-saver is EE rebates only).
- Verdicts: CONFIRMED (independent check agrees), REFUTED (a qualifying program found, URL given), INCONCLUSIVE (cited evidence doesn't show the claim and the primary source is unreachable).
- Flagged extra row: Greer CPW (7654) res_habit (pre-existing No, not part of the 42).
- No data files were edited.

## Results

| utility | eia_id | cell | claimed | verdict | evidence URL |
|---|---|---|---|---|---|
| City of Lexington (NC) | 10966 | ci_dispatch | Yes | CONFIRMED | https://lexingtonnc.gov/home/showpublisheddocument/4599/638584441326300000 (Rider LRC-1, non-res >=100 kW, utility-called Peak Management Days) |
| City of Rock Hill (SC) | 16195 | ci_habit | Yes | INCONCLUSIVE | https://cityofrockhill.com/home/showpublisheddocument/27630/637401655186830000 is a **glossary** that defines on-/off-peak periods. It has no rate, charge, or schedule name. The electric-rates page returns 403. The nectarclimate summary lists GS/GD/LG with no TOU. |
| People's Electric Coop (OK) | 14775 | ci_dispatch | Yes | CONFIRMED | https://www.peopleselectric.coop/faqs_category/load-management/ (non-res demand-billed curtailment, Jun 20 to Sep 9, 3–7 pm) |
| Northwestern Electric Coop (OK) | 13807 | res_habit | Yes | CONFIRMED | https://www.nwecok.coop/electric-vehicles (EV charging rate, 10 pm–5 am, L2 charger). The rider PDF is image-only, so the price differential was not read. |
| Independence P&L | 9231 | res_dispatch | No | CONFIRMED | https://www.independencemo.gov/government/city-departments/power-and-light/customers/residential-programs (rebates only) |
| Independence P&L | 9231 | ci_habit | No | CONFIRMED | https://www.independencemo.gov/sites/default/files/2023-11/MG4%20November%202023.pdf (also MG2: max 30-min demand, hours-use tiers, no TOU). This is a better src than the cited programs page. |
| Columbia Water & Light | 4045 | res_habit | No | CONFIRMED | https://www.como.gov/utilities/utility-rates/ (seasonal tiered and heat-pump rates only) |
| City of Nixa | 3634 | res_dispatch | No | CONFIRMED | https://www.nixa.com/departments/electric/ |
| City of Nixa | 3634 | ci_dispatch | No | CONFIRMED | https://www.nixa.com/services-programs/ ; https://nixa.com/wp-content/uploads/2024/12/2025-RATES-1.pdf |
| Owensboro MU | 14268 | res_dispatch | No | CONFIRMED | https://omu.org/programs/ |
| Owensboro MU | 14268 | ci_dispatch | No | CONFIRMED (caveat) | https://omu.org/electric-rates/ (no riders listed). The 07-2023 rate ordinance PDF was not read. |
| Henderson MP&L | 8449 | ci_dispatch | No | CONFIRMED | https://www.hmpl.com/programs.html |
| Southwest Electric Coop | 27238 | ci_dispatch | No | CONFIRMED | https://www.swec.org/rate-structure-fees |
| Citizens Electric Corp | 3600 | res_habit | No | CONFIRMED | https://www.cecmo.com/rates ("billed at a flat rate regardless of the time of day") |
| Citizens Electric Corp | 3600 | ci_habit | No | CONFIRMED | https://www.cecmo.com/rates |
| Platte-Clay Electric Coop | 15138 | ci_habit | No | **REFUTED** | https://pcec.coop/wp-content/uploads/2025/03/PCECRATES-03_2025.pdf. Schedules IND (LP500) and IND II (LP502) bill "Base Billing Demand = current month **coincident peak** demand" plus a seasonal coincident-peak component. That is a peak-shifting demand design, the same basis used for Lexington's CP schedules. This is a definitional call (see notes). |
| Howell-Oregon Electric Coop | 8934 | res_dispatch | No | CONFIRMED | https://www.hoecoop.org/dualfuelheat (customer thermostat switchover plus rebate; Peak Alert is notification only) |
| Three Rivers Electric Coop | 16751 | res_dispatch | No | CONFIRMED | https://www.threeriverselectric.com/rates (Peak Alert in 2022 news is notification only) |
| Crawford Electric Coop | 4524 | res_dispatch | No | CONFIRMED | https://crawfordelec.com/RatesCharges |
| Osage Valley Electric Coop | 14192 | res_dispatch | No | CONFIRMED | https://www.osagevalley.com/billing-center (residential demand billing is habit, not control) |
| Sac Osage Electric Coop | 16511 | res_dispatch | No | CONFIRMED | https://www.sacosage.com/rates (load-control language is on commercial Rate-1 only) |
| Macon Electric Coop | 11463 | res_dispatch | No | CONFIRMED | https://www.maconelectric.com/rates |
| Central Missouri Electric Coop | 3268 | res_dispatch | No | CONFIRMED | https://www.cmecinc.com/energy-savings ; https://aeci.org/take-control-saver (EE rebates, no control) |
| City of Lexington (NC) | 10966 | res_habit | No | CONFIRMED | https://lexingtonnc.gov/home/showpublisheddocument/4599/638584441326300000 (residential is Sch R/RO only; no res TOU/CP) |
| City of Lumberton (NC) | 11318 | res_habit | No | CONFIRMED | https://www.lumbertonnc.gov/DocumentCenter/View/856 (eff 2024-07-01) |
| City of Lumberton (NC) | 11318 | ci_habit | No | CONFIRMED | same |
| Florida Keys Electric Coop | 6443 | res_habit | No | CONFIRMED | https://www.fkec.com/your-account/billing-information-fees/ (Rate Codes 1–3 only) |
| Florida Keys Electric Coop | 6443 | res_dispatch | No | CONFIRMED | https://www.fkec.com/energy-efficiency/residential-rebate-program/ (thermostat rebate, no control) |
| Florida Keys Electric Coop | 6443 | ci_habit | No | CONFIRMED | https://www.fkec.com/your-account/billing-information-fees/ |
| Hastings Utilities | 8245 | res_dispatch | No | CONFIRMED | https://www.cityofhastings.org/departments/utilities/service-connection/rebates-and-incentives/incentives/ |
| Heart of Texas EC | 55982 | res_habit | No | CONFIRMED | https://www.hotec.coop/rates |
| Heart of Texas EC | 55982 | res_dispatch | No | CONFIRMED | https://www.hotec.coop/rates and search (no DR/4CP program found) |
| Heart of Texas EC | 55982 | ci_habit | No | CONFIRMED | https://www.hotec.coop/rates |
| Heart of Texas EC | 55982 | ci_dispatch | No | CONFIRMED | https://www.hotec.coop/rates |
| Bowie-Cass EC | 2049 | res_habit | No | CONFIRMED | https://www.bcec.com/account/rates-fees/residential-rates-fees/ |
| Bowie-Cass EC | 2049 | ci_habit | No | CONFIRMED | https://www.bcec.com/account/rates-fees/commercial-rates/ (PS/SC, LP-2 only) |
| Bowie-Cass EC | 2049 | ci_dispatch | No | CONFIRMED | same |
| Cowlitz PUD | 4442 | res_dispatch | No | CONFIRMED | https://www.cowlitzpud.org/efficiency/residential-programs/ (DR appears only as a CEIP planning target) |
| Douglas Electric Coop | 5327 | res_habit | No | CONFIRMED | https://www.dec.coop/rate-information (Sch 1 has basic and energy charges only) |
| Douglas Electric Coop | 5327 | ci_habit | No | CONFIRMED | same (Sch 2/5/6 have no TOU; Sch 16/17 are EV-station rates, not TOU) |
| Murray City Power | 13137 | res_habit | No | CONFIRMED | https://murray.utah.gov/DocumentCenter/View/14388 ("Peak/Off-Peak Season" is seasonal, not time-of-day) |
| Overton PD No. 5 | 14245 | res_dispatch | No | CONFIRMED | https://www.opd5.com/safety/opd5-smart-meters/ ("OPD5 does not. And we have no plans to do so.") |
| *Greer CPW (flagged, not in the 42)* | 7654 | res_habit | No (pre-existing) | **REFUTED** | https://www.greercpw.com/wp-content/uploads/2026/02/electric_110.pdf. Code 110 EV rate has On-Peak 4–8 pm, Off-Peak 11 pm–6 am, Standard otherwise. It is listed on https://www.greercpw.com/utilities/electricity/ (eff 2022-10-01, current 2026 sheet). |

## Rates
- **Yes:** 3 of 4 confirmed (75% of sampled), 0 refuted, 1 inconclusive (Rock Hill). Excluding the inconclusive cell: 3/3 = 100%. Pass bar is >=95% of sampled. The bar is **missed** if the inconclusive cell counts against it and met if it is excluded. Either way, the Rock Hill Yes has no qualifying source as written.
- **No:** 37 of 38 confirmed = **97.4%** (bar >=90%, **pass**), 1 refuted (Platte-Clay ci_habit, definitional), 0 inconclusive. Caveats: OMU ci_dispatch (ordinance PDF unread) and HOTEC cells (full tariff PDF not reachable; rates page plus search only).
- Flagged pre-existing cell: Greer res_habit No is refuted.

## Corrections needed
1. **7654 Greer CPW, res_habit: No → Yes.** src https://www.greercpw.com/wp-content/uploads/2026/02/electric_110.pdf (Code 110 EV TOU). Tier: Primary.
2. **16195 Rock Hill, ci_habit: Yes → Unknown.** The cited glossary shows no rate. Re-check when https://www.cityofrockhill.com/departments/utilities/electric-rates is reachable; the glossary strongly implies on-peak demand billing exists.
3. **15138 Platte-Clay EC, ci_habit: No → Yes.** src https://pcec.coop/wp-content/uploads/2025/03/PCECRATES-03_2025.pdf (Sch IND/IND II coincident-peak billing demand). This is a definitional call: if the lead rules that coincident-peak demand billing is not "shifting-oriented", set it back to No. Keep it consistent with Lexington's CP-based ci_habit=Yes.

## Side observations (not in scope, no action taken)
- Columbia (4045) res_dispatch=Yes rests on a "Res Load Management Discount" seen in a search snippet. A full read of como.gov/utilities/utility-rates/ found no residential load-management discount, only references to a "load control program" in the LGS rate. Recommend re-verifying.
- Platte-Clay LP1 references "interruptible hours and procedures", which is relevant to ci_dispatch (currently Unknown).
- Independence ci_habit src should point to the MG2/MG4 tariff PDFs rather than the commercial-programs page.
