# Verification of PJM + ERCOT audits (2026-10-12)

Scope: audits_PJM_ERCOT. Sources: audit/results/{PJM,ERCOT}.json, audit/samples/{PJM,ERCOT}.json.
Sampled items: all top-bucket REFUTED items, all wrong_dollar=true items, 4 random CONFIRMED items (random.Random(7).sample) and 3 random sample-bucket REFUTED items (same RNG, drawn next).
Each item's evidence_url was fetched once. Items that cite the same URL share one fetch: PSE&G Patch (9/11/48), energychoicematters (14/58), PA PUC DSRWG (15/56), AEP tariff book (18/19), Austin Commercial DR (19/48 ERCOT).
ERCOT REFS draw #83 duplicates MUST #83, so it is counted once.

## Table

| Region | idx | Item | Auditor | Verifier | Evidence (fetched) |
|---|---|---|---|---|---|
| PJM | 6 | Dominion VA ci_habit (claimed No) | REFUTED -> Yes | AGREE | GS-2T: voluntary non-res TOU, 30-500 kW, eff. 1/1/2025, no closure language |
| PJM | 9 | PSE&G res_dispatch (Yes) | REFUTED -> Unknown | AGREE | Patch article is dated 2010-07-07 and only mentions 2010 AC cycling |
| PJM | 10 | PSE&G ci_habit (No) | REFUTED -> Yes | AGREE | BGS-CIEP Sheet 82: hourly real-time PSEG-zone LMP; default for LPL-Sec >=500 kW / LPL-Pri / HTS, elective for HS/GLP/LPL<500. Sheets marked DRAFT, eff. 6/1/2026 |
| PJM | 11 | PSE&G ci_dispatch (Yes) | REFUTED -> Unknown | AGREE | Same 2010 Patch article; it has no C&I curtailment |
| PJM | 12 | PECO res_habit (No) | REFUTED -> Yes | AGREE | PECO 2025 PTC sheet: TOU option for R/RH since 9/1/2021; Mar-May 2025 rates 28.836/6.980/5.169 c (the auditor wrote super-off 5.194, which is the Jan-Feb value; minor) |
| PJM | 13 | PECO res_dispatch (No) | REFUTED -> Yes | AGREE | Flex & Save EV FAQ: PECO pauses/shifts residential EV charging at peak, $60/season up to $120/yr, runs through 5/31/2031 |
| PJM | 14 | PECO ci_habit (Yes) | REFUTED (unsupported) | AGREE* | The cited article covers UGI only and never mentions PECO |
| PJM | 15 | PECO ci_dispatch (Yes) | REFUTED (unsupported) | AGREE | The cited PUC doc is about 2007; no CPower, no current status |
| PJM | 18 | AEP Ohio ci_habit (No) | REFUTED -> Yes | AGREE | Oct 2026 tariff TOC: GS-TOU (221) eff. 4/10/2026, not closed; GS-TOD is marked "no new customers" |
| PJM | 41 | ComEd VLR $50-150/kW-yr | REFUTED, wrong $ | AGREE | Olivine page (2022): contract through 2027; no rate published |
| PJM | 42 | ComEd EV charger rebate | REFUTED (status) | AGREE | Qmerit: $1,000 / $2,500; "As of March 31st 2026 ... not accepting any more applications this year" |
| PJM | 48 | PSE&G AC Cycling | REFUTED (status) | AGREE | Same 2010 Patch article |
| PJM | 50 | PSE&G RS-TOU rates | REFUTED, wrong $ | AGREE | Compare page: summer 59.9/27.4/10.4, winter 38.5/26.5/10.5, RS 29.2/25.9 c/kWh. Matches the auditor |
| PJM | 54 | AEP Ohio NEM ~$0.11/kWh | REFUTED, wrong $ | AGREE | NEMS doc: credit = generation energy component; no $/kWh; no cash-out |
| PJM | 56 | PECO C&I DR (CPower) | REFUTED (unsupported) | AGREE | Same 2007 PUC doc |
| PJM | 58 | PECO Hourly default service | REFUTED (unsupported) | AGREE* | Same UGI-only article |
| PJM | 60 | Dominion Smart Thermostat Rewards $ | REFUTED, wrong $ | AGREE | $25 enroll, $50 instant rebate, +$25/yr; no 75% threshold |
| PJM | 61 | Dominion Non-Res Curtailment $ | REFUTED, wrong $ | AGREE | $36/kW-yr, paid monthly, typically >=100 kW, 10-20 events/yr |
| PJM | 65 | Dominion Net Metering terms | REFUTED (non-$) | AGREE | Year-end excess paid only under optional PPA at DOMZONE DA annual avg LMP; Off-Peak Plan credits are tier-locked |
| PJM | 68 | Dominion Off-Peak Plan rates | REFUTED, wrong $ | AGREE | 0.310059/0.151011/0.133130 summer; 0.270582/0.155396/0.149173 winter. Exact match to the auditor |
| PJM | 73 | Ohio Edison TOD rates | REFUTED, wrong $ | AGREE | Page (mod. 2026-08-25): 0.1119/0.0843/0.0560 summer, 0.1111/0.0862/0.0555 winter, SSO 0.072774 |
| PJM | 35 | Licking Valley RECC res_habit No | CONFIRMED | AGREE (low conf.) | Homepage has no TOU/TOD link; only Simple Saver, Heat Pump, and the KY PSC tariff link. The tariff itself was not checked |
| PJM | 19 | AEP Ohio ci_dispatch Yes | CONFIRMED | AGREE | IRP-L, IRP-E and Pilot DR Rider (475-1) are all eff. 4/10/2026 and none is closed |
| PJM | 40 | ComEd Peak Time Savings $1/kWh | CONFIRMED | AGREE | $1/kWh, Jun 1-Sep 30. The page is (c)2019, so the auditor's note about current status still applies |
| PJM | 69 | Dominion Sched 1P "Not published for new enrollment" | CONFIRMED | AGREE | Closed to new customers 5/16/1986; rates are listed (eff. 1/1/2026) for grandfathered customers |
| PJM | 23 | APCo (VA) res_dispatch (No) | REFUTED -> Yes | CANNOT_TELL | Article dated 2026-04-29 describes an APCo BYOT thermostat DR program, but it never names a state, so VA applicability is not shown |
| PJM | 82 | PJM Synchronized Reserve Tier1/Tier2 | REFUTED (stale name) | AGREE | FAQ: Tier 1/2 consolidated by RPF on 10/1/2022; no 30% / May-2023 adder in the doc |
| PJM | 74 | Pepco DC net metering 1:1 | REFUTED (unsupported) | AGREE | DOEE page states neither 1:1 retail credit nor carryover |
| ERCOT | 46 | Austin Energy Power Partner Battery $ | REFUTED, wrong $ | AGREE | "$75/kW each year based on the maximum device size..." (not per event); $500 rebate for PTO on/after 2/18/25; ~$324/yr example; "$750" appears only in the meta description |
| ERCOT | 75 | PEC Large Power TOU TCOS | REFUTED, wrong $ | AGREE | TCOS $6.11/kW or $0.020688/kWh; SA $150, PCC $6.74, TOU 16.1843/9.3169/4.3481 c confirmed |
| ERCOT | 83 | CoServ Summer Savings Rate | REFUTED, wrong $ | AGREE | Base on 21.0821 c / off 8.7209 c; Sept adjusted 20.5321/8.1709 (= the claimed values); winter base 12.3030 c |
| ERCOT | 48 | Austin Commercial DR $ | CONFIRMED | AGREE | Std 50/55/70, Fast 65/70/80, Fast ADR 265/270/280 per avg kW; min $25, max $76,000 |
| ERCOT | 19 | Austin Energy ci_dispatch Yes | CONFIRMED | AGREE | Same page; enrollment is invited |
| ERCOT | 57 | Oncor Winter C&I LM 2025-26 | CONFIRMED | AGREE | Max bid $35/kW, budget $800k; the season ended 5/31/2026, so "Active" is stale (the auditor already flagged this) |
| ERCOT | 6 | CenterPoint ci_habit No | CONFIRMED | AGREE | Delivery charges are flat, plus 4CP/NCP/billing-kVA demand charges; no TOU |
| ERCOT | 21 | Victoria EC res_dispatch (No) | REFUTED -> Yes | AGREE | Beat-The-Peak: provider raises thermostat setpoints up to 2F during load-shed events; enrollment and annual incentives |
| ERCOT | 85 | TBPP (Texas Energy Fund) status | REFUTED (status) | AGREE | TXSES 2/25/2026: rule proposed (Project 59024), applications not open; $1.8B and $500/kW confirmed |

\* AGREE that the cited source does not support the claim. However, the underlying fact is likely true: PA default service for large C&I (Procurement Class 3/4) is hourly-priced. Repoint the source to the PECO tariff or GSA page; do not flip the cell to No.

## Agreement rate

| Region | Items checked | AGREE | DISAGREE | CANNOT_TELL | Agreement (decisive) |
|---|---|---|---|---|---|
| PJM | 28 | 27 | 0 | 1 | 27/27 = 100% |
| ERCOT | 9 | 9 | 0 | 0 | 9/9 = 100% |

## PJM: the 5 big-utility "No" cells

The auditor's claim is **CONFIRMED**. All five cells are wrong and should be Yes:

| idx | Cell | Should say | Evidence | Confidence |
|---|---|---|---|---|
| 6 | Dominion VA ci_habit | Yes | Schedule GS-2T, voluntary non-res TOU | Med-high. Filing eff. 1/1/2025 on the www2 domain; a newer filing may supersede it, but no closure language |
| 10 | PSE&G ci_habit | Yes | BGS-CIEP hourly RT-LMP default supply | High. The 2026 sheets are DRAFT, but BGS-CIEP hourly pricing is long-standing |
| 12 | PECO res_habit | Yes | PECO TOU Pricing Option (R/RH), since 2021 | High |
| 13 | PECO res_dispatch | Yes | PECO Flex & Save managed EV charging (through 2031) | High, provided managed EV charging counts as res_dispatch (it is utility device control) |
| 18 | AEP Ohio ci_habit | Yes | GS-TOU (Sheets 221), eff. 4/10/2026, open | Med-high. Based on the TOC listing; rate terms not read |

## Disagreements

None. The only open item is PJM #23 (APCo VA res_dispatch). The cited article does not name a state. Keep the auditor's Yes only if an appalachianpower.com/save page shows that BYOT is offered in VA; otherwise set it to Unknown.

Minor notes, not disagreements:
- #12: the super-off-peak value quoted for Mar-May 2025 should be 5.169 c, not 5.194 c.
- #14/#58: the fact is likely true; only the source is defective.
