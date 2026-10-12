# AUDIT_PJM (independent re-verification, 2026-10-12; resumed same day)

**Seed:** 20261002 (audit/samples/PJM.json, 87 items: 40 presence [20 top-5-utility, 20 stratified], 47 program rows [32 top, 15 sample]).
**Status: COMPLETE.** First pass checked 35 items before fetch quota ran out; resume pass checked the remaining 52. No NOT_DONE items.

## Method
Rubric sec. 1 + "What counts". Presence: current value read from docs/data/presence.json (cells changed vs sample: ComEd rd Yes->Unknown, ComEd ch No->Yes, Cleveland Public Power ch Yes->Unknown). Yes = CONFIRMED only if the cited page shows a currently open program for that segment; one replacement search on the utility's site if the cited page failed (logged as source defect). No = CONFIRMED if the utility's own rate/DR pages show nothing; REFUTED if a program was found. Program rows: all 47 line numbers still match utility+program; checked name/category/$/status/URL; several rows now have blank incentive_value_usd vs the sample ('claimed changed'). WebFetch/WebSearch only. "REFUTED (unsupported)" = cited page readable but does not show the current program/value and the replacement search found none; an unsourced $ figure in a top row counts as wrong $. Unknown cells are not scored.

## Counts and rates vs bars
| Bucket | Confirmed | Refuted | Inconclusive | Rate C/(C+R) | Rate incl. inconcl. | Bar | Result |
|---|---|---|---|---|---|---|---|
| Presence Yes (current) | 14 | 6 | 1 | 70.0% (14/20) | 66.7% (14/21) | >=95% | **FAIL** |
| Presence No (current) | 11 | 6 | 0 | 64.7% (11/17) | 64.7% | >=90% | **FAIL** |
| Presence now Unknown | - | - | 2 (not scored) | - | - | - | - |
| Program rows, top bucket | 19 | 11 | 2 | 63.3% (19/30) | 59.4% (19/32) | 0 wrong $ | **FAIL: 6 wrong $** |
| Program rows, sample | 8 | 5 | 2 | 61.5% (8/13) | 53.3% (8/15) | log all | 1 wrong $ (row 350) |

Top-bucket No refutations are concentrated: 5/5 top-utility No cells were wrong (Dominion ch, PSE&G ch, PECO rh, PECO rd, AEP Ohio ch). Stratified-sample No cells: 11/12 confirmed.

Wrong $ in top-10 bucket (6): rows 272 (ComEd VLR), 326 (PSE&G RS-TOU), 354 (AEP Ohio NEMS, unsourced ~$0.11/kWh), 399 (Dominion Smart Thermostat Rewards), 400 (Dominion Non-Res Curtailment), 407 (Dominion Off-Peak Plan). Sample bucket: row 350 (Ohio Edison TOD, ~2x actual).

## Defect list (file / row-or-eia_id / cell : fix)
1. data/processed/programs.csv row 272 (ComEd C&I VLR), incentive_value_usd/incentive_structure: '$50-150/kW-yr' is a generic PJM CSP value, unsupported by source -> blank (not published) and structure 'per-event performance payment' or cite ComEd VLR terms.
2. programs.csv row 326 (PSE&G RS-TOU), peak_offpeak_rates: -> 'summer on 59.9 / mid 27.4 / off 10.4 c; winter on 38.5 / mid 26.5 / off 10.5 c per kWh'; source https://nj.myaccount.pseg.com/myservicepublic/compare-rates-enroll.
3. programs.csv row 399 (Dominion Smart Thermostat Rewards), incentive_value_usd: -> '$25 enrollment (existing thermostat) or $50 instant rebate on new thermostat; +$25/yr participation'.
4. programs.csv row 400 (Dominion Non-Residential Curtailment), incentive_value_usd: -> '$36/kW-yr paid monthly' (>=100 kW, 10-20 events/yr).
5. programs.csv row 407 (Dominion Off-Peak Plan), incentive_value_usd + peak_offpeak_rates: -> summer 0.310059/0.151011/0.133130, winter 0.270582/0.155396/0.149173 $/kWh.
6. programs.csv row 273 (ComEd EV charger rebate), program_status: Active -> closed for 2026 (not accepting applications as of 2026-03-31, Qmerit); comed.com URL JS-only. Category EV-Rate questionable for a hardware rebate.
7. programs.csv row 324 (PSE&G Central AC Cycling) status + source: 2010 Patch article; no current evidence -> find pseg.com source or status Unknown.
8. programs.csv row 404 (Dominion Net Metering) export_compensation text: year-end purchase only via optional PPA at PJM DOMZONE annual avg DA LMP; not automatic 'avoided cost' payout.
9. programs.csv row 402 (Dominion EV Telematics): incentive is $40/yr gift card, Tesla-only, not bill credit; source_url -> https://charge.weavegrid.com/dominionenergy/.
10. programs.csv row 277 (ComEd DTOD EV credit) source_url: barchart page empty -> https://www.businesswire.com/news/home/20260211295140/en.
11. programs.csv row 276 (ComEd DG rebate): $250 large-C&I tier unverified; comed.com URL JS-only; confirm against Rider POGCS.
12. programs.csv row 406 (Dominion NEM standby): add 15 kW -> 20 kW AC threshold change 2026-07-01 (HB 1255); replace installer-blog source with tariff.
13. programs.csv row 408 (Dominion 1P): rates are published in the PDF; 'Not published' imprecise.
14. docs/data/presence.json eia 19876 (Dominion VA) ch: No -> Yes, chs https://www2.dominionenergy.com/-/media/pdfs/virginia/business-rates/schedule-gs2t.pdf (GS-2T non-residential TOU; verify current filing).
15. presence.json eia 15477 (PSE&G) rd and cd: Yes supported only by 2010 Patch article -> find current pseg.com source or set Unknown. Lead: flexpower.pseg.com (AutoGrid FlexSaver) for rd.
16. presence.json eia 4110 (ComEd) rd: now Unknown; CUB page says Central AC Cycling open ('sign up at any time') -> re-check for Yes with comed.com source.
17. presence.json eia 4110 rhs: comed.com PTS page JS-only -> repoint to https://hourlypricing.comed.com/about/.
18. presence.json eia 15477 (PSE&G) ch: No -> Yes; chs = PSE&G BGS-CIEP tariff sheet (hourly RT-LMP default supply, >=500 kW mandatory, elective for HS/GLP/LPL<500 kW; eff 6/1/2026) https://nj.pseg.com/-/media/pseg/public-site/documents/electric-bgs/draft-2026-bgs-auction-all-sheets-w-wm.ashx (replace with final sheet).
19. presence.json eia 14940 (PECO) rh: No -> Yes; rhs = https://www.peco.com/TOU (PECO TOU Pricing Option; 2025 PTC sheet lists peak/off/super-off PTCs).
20. presence.json eia 14940 (PECO) rd: No -> Yes; rds = https://www.peco.com/flexandsave (Flex & Save utility-managed EV charging, $60/season, through 5/31/2031; FAQ https://greatergrid.com/enroll/programs/evs/pecoflexandsaveev/faq).
21. presence.json eia 14940 (PECO) chs: energychoicematters article does not mention PECO -> cite PECO Procurement Class 3/4 hourly default service tariff sheet, else set ch Unknown.
22. presence.json eia 14940 (PECO) cds: c.2007 PUC DSRWG doc -> cite current PECO Act 129 C&I DR source, else set cd Unknown.
23. presence.json eia 14006 (AEP Ohio) ch: No -> Yes; chs = October_2026_Ohio_Power_Tariff_Book.pdf (GS-TOU, Sheets 221; verify sheet text).
24. presence.json eia 14006 (AEP Ohio) rds: repoint OCC page -> https://www.aepohio.com/savings/home/money-saving-programs/power-rewards/.
25. presence.json eia 733 (Appalachian Power VA) rd: No -> Yes after confirming VA eligibility of BYOT (appalachianpower.com article 2026-04-29, id=11886). Also state field shows OH for a VA utility - check.
26. presence.json eia 17044 (Shelby) rds -> https://www.shelbyenergy.com/simplesaver ; eia 3687 (Clark) rds -> https://clarkenergy.com/simplesaver (EKPC page does not show member participation).
27. presence.json eia 14251 (Owen) cds -> https://owenelectric.com/rates-and-tariffs (Schedule XV interruptible, $6.20-7.60/kW-mo); ch Unknown -> Yes (Schedules I-C and IIA Time of Day).
28. presence.json eia 20521 (Wheeling Power) cd: cited APCo WV rates page shows no DR rider and is APCo-only -> cite Wheeling tariff rider or set Unknown.
29. presence.json eia 13602 (Niles) rd: AMP program page lists no members; Niles site silent -> set Unknown unless subscription documented.
30. presence.json eia 4794 (Danville) cds: danvilleva.gov archive item robots-blocked and 2014 vintage -> find current source (inconclusive).
31. presence.json eia 12796 (Mon Power) state attribution PA for a WV utility - check join.
32. programs.csv row 351 (AEP Ohio Power Rewards) source_url: OCC page has no $ -> https://www.aepohio.com/savings/home/money-saving-programs/power-rewards/ ; event_limits: 'up to 16 events/yr, <=4 h'.
33. programs.csv row 354 (AEP Ohio NEMS) incentive_value_usd: '~$0.11/kWh' unsourced (WRONG $, top bucket) -> exact generation energy-component rate from current tariff or blank; basis text 'excess kWh x generation energy component, monetary carryforward, no cash-out' is correct.
34. programs.csv row 365 (PECO C&I DR) source_url/status: 2007 doc, no CPower -> current source or status Unknown.
35. programs.csv row 366 (PECO NM) source_url: installer blog -> PECO Rate RS-2 tariff sheet.
36. programs.csv rows 367 (PECO) and 373 (Penn Power) source_url: energychoicematters article covers UGI only -> PECO Class 3/4 hourly sheet; Penn Power -> https://www.firstenergycorp.com/content/dam/customer/Customer%20Choice/Files/PA/tariffs/FEPA-Supp-No-28-PTC-HPS-Rider-Changs-12-1-2025.pdf.
37. programs.csv row 350 (Ohio Edison TOD) incentive_value_usd + peak_offpeak_rates (WRONG $): -> summer midday peak $0.111900 / shoulder $0.084267 / off $0.055950; winter $0.111095 / $0.086182 / $0.055547 per kWh (illustrative, page mod 2026-08-25).
38. programs.csv row 370 (Penelec C&I DR): cited 2017 release covers Met-Ed/Penn Power/West Penn only, 2017-2020 -> fix attribution/status (Unknown/Closed).
39. programs.csv row 458 (PJM Sync Reserve) program_name: Tier 1/Tier 2 consolidated 10/1/2022 (cited FAQ) -> 'Synchronized Reserve (Real-Time)'; remove or source the '30% adder May 2023' claim.
40. programs.csv row 453 (PJM RPM DR): add https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf as price source ($329.17 confirmed).
41. programs.csv row 265 (Pepco DC NM) source_url: DOEE page generic -> Pepco DC net metering tariff.
42. programs.csv row 305 (Easton NM) incentive_value_usd holds '3.49 MW installed' (not a compensation value, not on page) -> 'net kWh billing; annual payout for banked excess'.
43. programs.csv row 343 (Duke Ohio Rider LM) source_url: 302 -> https://dam.assets.ohio.gov/image/upload/puco.ohio.gov/empliibrary/files/docketing/tariffs/Electric/Duke%20Energy%20Ohio%20-%20Electric/PUCO%2019%20Schedules%20of%20Rates,%20Classifications,%20Rules%20andRegulations.pdf (Sheet 76).
44. programs.csv row 290 (BGE Energy Savings Days): drop '(legacy Smart Energy Rewards structure)' - $1.25/kWh is current (2026 page).

## Item table
| idx | type | bucket | utility | cell / program | claimed | verdict | wrong $ | evidence |
|---|---|---|---|---|---|---|---|---|
| 0 | presence | top | Commonwealth Edison Company (ComEd) | res_habit | Yes | CONFIRMED |  | https://communications.comed.com/PTS |
| 1 | presence | top | Commonwealth Edison Company (ComEd) | res_dispatch | Yes (now Unknown) | INCONCLUSIVE |  | https://citizensutilityboard.org/?p=19023 |
| 2 | presence | top | Commonwealth Edison Company (ComEd) | ci_habit | No (now Yes) | CONFIRMED |  | https://comed.chooseev.com/commercial/faq |
| 3 | presence | top | Commonwealth Edison Company (ComEd) | ci_dispatch | Yes | CONFIRMED |  | https://olivineinc.com/project/commonwealth-edisons-c-i-vlr-program/ |
| 4 | presence | top | Virginia Electric & Power Co (Dominion | res_habit | Yes | CONFIRMED |  | https://www.dominionenergyptr.com/ |
| 5 | presence | top | Virginia Electric & Power Co (Dominion | res_dispatch | Yes | CONFIRMED |  | https://www.dominionenergy.com/virginia/save-energy/my-home/smart-thermostat-rewards |
| 6 | presence | top | Virginia Electric & Power Co (Dominion | ci_habit | No | REFUTED |  | https://www2.dominionenergy.com/-/media/pdfs/virginia/business-rates/schedule-gs2t.pdf |
| 7 | presence | top | Virginia Electric & Power Co (Dominion | ci_dispatch | Yes | CONFIRMED |  | https://www.dominionenergy.com/virginia/save-energy/targeted-sector-programs |
| 8 | presence | top | Public Service Electric and Gas Co (PS | res_habit | Yes | CONFIRMED |  | https://nj.myaccount.pseg.com/myservicepublic/time-of-use |
| 9 | presence | top | Public Service Electric and Gas Co (PS | res_dispatch | Yes | REFUTED |  | https://patch.com/new-jersey/wyckoff/pseg-help-conserve-energy-during-heat-wave |
| 10 | presence | top | Public Service Electric and Gas Co (PS | ci_habit | No | REFUTED |  | https://nj.pseg.com/-/media/pseg/public-site/documents/electric-bgs/draft-2026-bgs-auction |
| 11 | presence | top | Public Service Electric and Gas Co (PS | ci_dispatch | Yes | REFUTED |  | https://patch.com/new-jersey/wyckoff/pseg-help-conserve-energy-during-heat-wave |
| 12 | presence | top | PECO Energy Co | res_habit | No | REFUTED |  | https://azure-na-assets.contentstack.com/v3/assets/blt1b5616c79bacadb4/bltaabbb7780351dcd7 |
| 13 | presence | top | PECO Energy Co | res_dispatch | No | REFUTED |  | https://greatergrid.com/enroll/programs/evs/pecoflexandsaveev/faq |
| 14 | presence | top | PECO Energy Co | ci_habit | Yes | REFUTED |  | https://www.energychoicematters.com/stories/20250220c.html |
| 15 | presence | top | PECO Energy Co | ci_dispatch | Yes | REFUTED |  | https://www.puc.pa.gov/electric/pdf/dsr/DSRWG_Existing_DSR_Programs_PECO.pdf |
| 16 | presence | top | Ohio Power Company (AEP Ohio) | res_habit | Yes | CONFIRMED |  | https://www.aepohio.com/clean-energy/electric-cars/plug-in-electric-vehicle-rate |
| 17 | presence | top | Ohio Power Company (AEP Ohio) | res_dispatch | Yes | CONFIRMED |  | https://www.occ.ohio.gov/content/aep-ohios-power-rewards-smart-thermostat-program |
| 18 | presence | top | Ohio Power Company (AEP Ohio) | ci_habit | No | REFUTED |  | https://www.aepohio.com/lib/docs/ratesandtariffs/Ohio/October_2026_Ohio_Power_Tariff_Book. |
| 19 | presence | top | Ohio Power Company (AEP Ohio) | ci_dispatch | Yes | CONFIRMED |  | https://www.aepohio.com/lib/docs/ratesandtariffs/Ohio/October_2026_Ohio_Power_Tariff_Book. |
| 20 | presence | sample | Prince George Electric Cooperative | ci_dispatch | No | CONFIRMED |  | https://www.pgec.coop/rates |
| 21 | presence | sample | Central Virginia Electric Cooperative | ci_dispatch | No | CONFIRMED |  | https://www.mycvec.com/account/rate-schedules/ |
| 22 | presence | sample | Southern Maryland Electric Cooperative | ci_dispatch | No | CONFIRMED |  | https://www.smeco.coop/energy-efficiency/commercial-programs/small-business/ |
| 23 | presence | sample | Appalachian Power Co (AEP - Virginia) | res_dispatch | No | REFUTED |  | https://www.appalachianpower.com/community/caring/view?id=11886 |
| 24 | presence | sample | Hagerstown Light Department | ci_habit | No | CONFIRMED |  | https://www.hagerstownmd.org/153/Tariffs |
| 25 | presence | sample | Harrisonburg Electric Commission | res_dispatch | No | CONFIRMED |  | https://www.harrisonburgelectric.com/our-programs/ |
| 26 | presence | sample | City of Naperville Electric Utility | ci_habit | No | CONFIRMED |  | https://www.naperville.il.us/services/electric-utility/your-electric-service/electric-rate |
| 27 | presence | sample | Shelby Energy Cooperative | res_dispatch | Yes | CONFIRMED |  | https://www.shelbyenergy.com/simplesaver |
| 28 | presence | sample | Clark Energy Cooperative | res_dispatch | Yes | CONFIRMED |  | https://clarkenergy.com/simplesaver |
| 29 | presence | sample | Owen Electric Cooperative | ci_dispatch | Yes | CONFIRMED |  | https://owenelectric.com/rates-and-tariffs |
| 30 | presence | sample | Wheeling Power Co (AEP - West Virginia | ci_dispatch | Yes | REFUTED |  | https://www.appalachianpower.com/company/about/rates/wv |
| 31 | presence | sample | Atlantic City Electric Co (ACE) | res_dispatch | Yes | CONFIRMED |  | https://homeenergysavings.atlanticcityelectric.com/residential/energy-wise-rewards |
| 32 | presence | sample | City of Niles Municipal Electric | res_dispatch | Yes | REFUTED |  | https://www.amppartners.org/sustainability/programs/community-energy-savings-smart-thermos |
| 33 | presence | sample | Danville Utilities (City of Danville - | ci_dispatch | Yes | INCONCLUSIVE |  | https://danvilleva.gov/ArchiveCenter/ViewFile/Item/4422 |
| 34 | presence | sample | Cleveland Public Power | ci_habit | Yes | INCONCLUSIVE |  |  |
| 35 | presence | sample | Licking Valley RECC | res_habit | No | CONFIRMED |  | https://lvrecc.com/ |
| 36 | presence | sample | Nolin RECC | res_habit | No | CONFIRMED |  | https://nolinrecc.com/wp-content/uploads/2020/10/Tariff.pdf |
| 37 | presence | sample | Northern Virginia Electric Cooperative | ci_dispatch | No | CONFIRMED |  | https://www.novec.com/Save/Annual-Peak-Use-Reduction.cfm |
| 38 | presence | sample | Monongahela Power Co (FirstEnergy - We | res_dispatch | No | CONFIRMED |  | https://www.firstenergycorp.com/save_energy/save_energy_pennsylvania.html |
| 39 | presence | sample | Easton Utilities Commission | res_habit | No | CONFIRMED |  | https://eastonutilities.com/wp-content/info/electric-tariff.pdf |
| 40 | program | top | Commonwealth Edison Company (ComEd) | row 271: Peak Time Savings | $1.00/kWh saved during event hours | CONFIRMED |  | https://communications.comed.com/PTS |
| 41 | program | top | Commonwealth Edison Company (ComEd) | row 272: C&I Voluntary Load Reduction (VLR) / PJM Curtailmen | $50-150/kW-yr (typical CSP-enrolled PJM DR value) | REFUTED | Y | https://olivineinc.com/project/commonwealth-edisons-c-i-vlr-program/ |
| 42 | program | top | Commonwealth Edison Company (ComEd) | row 273: Electric Vehicle Charger and Installation Rebate | $1,000 standard rebate; up to $2,500 for income-qu | REFUTED |  | https://qmerit.com/blog/comed-ev-charger-rebate/ |
| 43 | program | top | Commonwealth Edison Company (ComEd) | row 274: Net Metering / CEJA Net Billing Transition | volumetric bill credit for exported energy | CONFIRMED |  | https://www.illinoissfa.com/wp-content/uploads/2024/11/Net-Metering-Changes-in-Illinois-%E |
| 44 | program | top | Commonwealth Edison Company (ComEd) | row 275: Hourly Pricing (Residential Real-Time Pricing Progr | Price = PJM real-time hourly LMP (avg of twelve 5- | CONFIRMED |  | https://hourlypricing.comed.com/about/ |
| 45 | program | top | Commonwealth Edison Company (ComEd) | row 276: Illinois Distributed Generation Rebate (Solar + Sto | $300/kW solar + $300/kWh storage (residential/smal | INCONCLUSIVE |  | https://www.citizensutilityboard.org/wp-content/uploads/2025/06/Solar-and-Storage-Rebates. |
| 46 | program | top | Commonwealth Edison Company (ComEd) | row 277: Delivery Time of Day (DTOD) Rate with EV Bill Credi | $2/vehicle/month bill credit for up to 24 months,  | CONFIRMED |  | https://www.businesswire.com/news/home/20260211295140/en |
| 47 | program | top | Commonwealth Edison Company (ComEd) | row 278: Scheduled Dispatch Virtual Power Plant (SDVPP) | capacity/dispatch payment for scheduled battery di | INCONCLUSIVE |  | https://icc.illinois.gov/downloads/public/filing/4/399541.pdf |
| 48 | program | top | Public Service Electric and Gas Co (PS | row 324: Central Air Conditioning Cycling Program | bill credit for enrollment | REFUTED |  | https://patch.com/new-jersey/wyckoff/pseg-help-conserve-energy-during-heat-wave |
| 49 | program | top | Public Service Electric and Gas Co (PS | row 325: Net Metering (NJ statewide) | 1:1 retail credit with annual true-up | CONFIRMED |  | https://nj.pseg.com/saveenergyandmoney/solarandrenewableenergy/netmetering |
| 50 | program | top | Public Service Electric and Gas Co (PS | row 326: Residential Service Time-of-Use (RS-TOU) | on ~35.2c high / mid / off ~6.7c per kWh (range ac | REFUTED | Y | https://nj.myaccount.pseg.com/myservicepublic/compare-rates-enroll |
| 51 | program | top | Ohio Power Company (AEP Ohio) | row 351: Power Rewards: Smart Thermostat Program | $75 instant rebate on eligible smart thermostat pu | CONFIRMED |  | https://www.aepohio.com/savings/home/money-saving-programs/power-rewards/ |
| 52 | program | top | Ohio Power Company (AEP Ohio) | row 352: Interruptible Power Rider - Expanded | bill credit/discount for curtailable load | CONFIRMED |  | https://www.aepohio.com/lib/docs/ratesandtariffs/Ohio/October_2026_Ohio_Power_Tariff_Book. |
| 53 | program | top | Ohio Power Company (AEP Ohio) | row 353: Plug-In Electric Vehicle (PEV) Rate | Whole Home (Tariff 048/807): on-peak 4.94410c/kWh, | CONFIRMED |  | https://www.aepohio.com/clean-energy/electric-cars/plug-in-electric-vehicle-rate |
| 54 | program | top | Ohio Power Company (AEP Ohio) | row 354: Net Energy Metering Service / Excess Generation Cre | ~$0.11/kWh (2025 Generation Energy Rider rate) for | REFUTED | Y | https://www.aepohio.com/lib/docs/cleanenergy/renewable/NetEnergyMeteringService2-10-2020.p |
| 55 | program | top | Ohio Power Company (AEP Ohio) | row 355: Residential Time-of-Use Rate | rate discount off-peak vs on-peak | CONFIRMED |  | https://www.aepohio.com/account/bills/programs/time-of-use |
| 56 | program | top | PECO Energy Co | row 365: Commercial & Industrial Demand Response Program | capacity/performance payment (administered via CPo | REFUTED |  | https://www.puc.pa.gov/electric/pdf/dsr/DSRWG_Existing_DSR_Programs_PECO.pdf |
| 57 | program | top | PECO Energy Co | row 366: Net Metering (PA statewide - AEPS) | 1:1 retail credit with periodic true-up | CONFIRMED |  | https://freedomforever.com/blog/net-metering-in-pennsylvania/ |
| 58 | program | top | PECO Energy Co | row 367: Default Service Hourly Pricing (Hourly SOS) | hourly LMP-indexed default service price passthrou | REFUTED |  | https://www.energychoicematters.com/stories/20250220c.html |
| 59 | program | top | Virginia Electric & Power Co (Dominion | row 398: Peak Time Rebates Program | $1.25 per kWh saved below weather-adjusted baselin | CONFIRMED |  | https://www.dominionenergyptr.com/ |
| 60 | program | top | Virginia Electric & Power Co (Dominion | row 399: Smart Thermostat Rewards | $25 first-summer enrollment + $10 for >=75% event  | REFUTED | Y | https://www.dominionenergy.com/virginia/save-energy/my-home/smart-thermostat-rewards |
| 61 | program | top | Virginia Electric & Power Co (Dominion | row 400: Non-Residential Curtailment Program | Not published (customized per facility Load Reduct | REFUTED | Y | https://www.dominionenergy.com/virginia/save-energy/targeted-sector-programs |
| 62 | program | top | Virginia Electric & Power Co (Dominion | row 401: EV Charger Rewards (Level 2 managed charging) | $125 equipment rebate (apply within 120 days of pu | CONFIRMED |  | https://www.chargingrewards.com/dominionenergy-ev/ |
| 63 | program | top | Virginia Electric & Power Co (Dominion | row 402: EV Telematics Rewards (WeaveGrid) | $40/year | CONFIRMED |  | https://charge.weavegrid.com/dominionenergy/ |
| 64 | program | top | Virginia Electric & Power Co (Dominion | row 403: Schedule 1EV - Residential Service with EV Charging | On-peak ES 6.879c(summer)/5.381c(winter); Off-peak | CONFIRMED |  | https://www.dominionenergy.com/-/media/content/rates-and-tariffs/pdfs/virginia/residential |
| 65 | program | top | Virginia Electric & Power Co (Dominion | row 404: Net Metering (Schedule 1/1G/1S/1T residential gener | 1:1 kWh credit at customer's applicable rate; exce | REFUTED |  | https://www.dominionenergy.com/virginia/renewable-energy-programs/net-metering |
| 66 | program | top | Virginia Electric & Power Co (Dominion | row 405: Virginia Shared Solar Program | Bill credit per subscribed kWh; minimum bill appli | CONFIRMED |  | https://www.dominionenergy.com/virginia/renewable-energy-programs/shared-solar-program |
| 67 | program | top | Virginia Electric & Power Co (Dominion | row 406: Net Metering Standby Charge (Schedules 1/1G/1S) | $2.79/kW distribution + $1.40/kW transmission stan | CONFIRMED |  | https://www.virtuesolar.com/2024/07/05/what-are-dominions-standby-fees/ |
| 68 | program | top | Virginia Electric & Power Co (Dominion | row 407: Off-Peak Plan | on $0.3105/kWh summer wkdy, $0.2710 winter wkdy; o | REFUTED | Y | https://www.dominionenergy.com/virginia/rates-and-tariffs/off-peak-plan |
| 69 | program | top | Virginia Electric & Power Co (Dominion | row 408: Schedule 1P - Residential TOU (Experimental) | Not published for new enrollment | CONFIRMED |  | https://cdn-dominionenergy-prd-001.azureedge.net/-/media/content/rates-and-tariffs/pdfs/vi |
| 70 | program | top | Virginia Electric & Power Co (Dominion | row 409: Schedule 1S - Demand TOU | Distribution demand $2.478/kW on-peak; Generation  | CONFIRMED |  | https://cdn-dominionenergy-prd-001.azureedge.net/-/media/content/rates-and-tariffs/pdfs/vi |
| 71 | program | top | Virginia Electric & Power Co (Dominion | row 410: Schedule 1T - Energy TOU | Distribution on-peak 8.0512c/off-peak 0.8440c; Gen | CONFIRMED |  | https://cdn-dominionenergy-prd-001.azureedge.net/-/media/content/rates-and-tariffs/pdfs/vi |
| 72 | program | sample | Duquesne Light Co | row 361: Net Metering | 1:1 retail credit | INCONCLUSIVE |  | https://duquesnelight.com/docs/default-source/default-document-library/currenttariff_107_2 |
| 73 | program | sample | Ohio Edison Company | row 350: Time-of-Day Option (Residential) (feature of Rider  | Summer: midday peak ~$0.21/kWh, shoulder ~$0.17/kW | REFUTED | Y | https://www.firstenergycorp.com/help/smart-meters/oh-smartmeter/time-varying-rate-option.h |
| 74 | program | sample | Potomac Electric Power Co (Pepco DC) | row 265: Net Metering (DC) | 1:1 retail credit | REFUTED |  | https://doee.dc.gov/service/solar-district |
| 75 | program | sample | PJM Interconnection | row 453: RPM Demand Resource (Limited/Extended Summer/Annual | Same cleared BRA price as generation capacity ($32 | CONFIRMED |  | https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-br |
| 76 | program | sample | Easton Utilities Commission | row 305: Net Metering | 3.49 MW net-metered solar capacity installed as of | REFUTED |  | https://eastonutilities.com/solar-and-net-metering/ |
| 77 | program | sample | Duke Energy Ohio | row 343: Rider LM - Load Management Rider | bill credit/discount for curtailable/controllable  | INCONCLUSIVE |  | https://dam.assets.ohio.gov/image/upload/puco.ohio.gov/empliibrary/files/docketing/tariffs |
| 78 | program | sample | Potomac Edison Co (FirstEnergy - Maryl | row 309: EV Driven - EV Time-of-Use Rate | $0.02/kWh discount off Electric Supply Charge for  | CONFIRMED |  | https://www.firstenergycorp.com/newsroom/news_articles/potomac-edison-incentivizes-electri |
| 79 | program | sample | Pennsylvania Electric Co (Penelec) | row 370: Commercial & Industrial Demand Response Program | financial incentive for curtailment (administered  | REFUTED |  | https://www.firstenergycorp.com/save_energy/save_energy_pennsylvania/for_your_business_pa/ |
| 80 | program | sample | UGI Utilities Inc - Electric Division | row 375: Default Service Hourly Pricing (Hourly SOS) | hourly LMP-indexed default service price passthrou | CONFIRMED |  | https://www.energychoicematters.com/stories/20250220c.html |
| 81 | program | sample | Appalachian Power Co (AEP - Virginia) | row 382: Residential Service - Smart Time of Use Plan | Critical on-peak 17.5c/kWh (Dec-Feb & Jun-Sep); on | CONFIRMED |  | https://www.appalachianpower.com/company/about/rates/va/rate-plans |
| 82 | program | sample | PJM Interconnection | row 458: Synchronized Reserve Market (Tier 1 and Tier 2) | Clearing prices vary by hour and reserve zone and  | REFUTED |  | https://www.pjm.com/-/media/DotCom/etools/markets-gateway/synchronized-reserve-deployment- |
| 83 | program | sample | Northern Virginia Electric Cooperative | row 391: EV-1 Electric Vehicle Rate | On-peak (6:01am-10:59pm) $0.11005/kWh vs standard  | CONFIRMED |  | https://www.novec.com/About_NOVEC/EV-1-NOVEC-s-Electric-Vehicle-Rate.cfm |
| 84 | program | sample | Pennsylvania Power Co | row 373: Default Service Hourly Pricing (Hourly SOS) | hourly LMP-indexed default service price passthrou | CONFIRMED |  | https://www.firstenergycorp.com/content/dam/customer/Customer%20Choice/Files/PA/tariffs/FE |
| 85 | program | sample | South Central Power Company | row 356: Net Billing (Excess Generation Purchase via Buckeye | rate set annually by Buckeye Power reflecting "tru | CONFIRMED |  | https://www.southcentralpower.com/faqs/does-south-central-power-company-use-net-billing-or |
| 86 | program | sample | Baltimore Gas and Electric Co (BGE) | row 290: Energy Savings Days (Peak Time Rebate / CPP add-on  | ~$1.25/kWh saved during peak events (legacy Smart  | CONFIRMED |  | https://bgesmartenergy.com/residential/earn-incentives/eventscentral/energy-savings-days |
