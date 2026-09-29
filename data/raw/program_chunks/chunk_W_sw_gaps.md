# Gaps - chunk_W_sw (CO/AZ/NM non-RTO; 13 utilities, 86 rows, verified 2026-09-28)

Utility names follow scan_W3/scan_W4 exactly (Longmont is "Longmont Power & Communications" in the scan; the El Paso NM and UNS strings are as in scan_W4).

## Scan corrections found
- Black Hills Energy (Colorado Electric): scan credited res_dispatch to "Demand Controller". That program page is South Dakota only. The CO Residential Demand Response Program is reported (search summary, not re-confirmed on a primary page) as discontinued 31 Dec 2025. No active CO residential DR found; no C&I curtailable rider found.
- Longmont: scan notes a thermostat DR pilot "launching fall 2026". The only page found is an April 2022 press release (ecobee, 200 customers, $50 + $25). No current-year DR page found. Logged as a 2022 Pilot row.
- Trico: TODP is a Time of Day Pumping (>=10 HP) tariff, not a general commercial TOU. RS2TOU is FROZEN (closed to new since 2017); the tariff PDFs are 2017 vintage and pre-date the 1 Jan 2026 rate case (ACC Decision 81550).
- PNM: the Rate 1B PDF cited is the 23rd revision (2024, Adv. Notice 616), closed to new customers since 15 Jan 2024. A newer residential TOU/TOD structure may exist after the 2026 rate case; current 1A (27th rev) shows only the WHEV pilot. Rate 2B is the current 26th revision (Adv. Notice 651).
- SSVEC and Trico rate PDFs and the RT tariff are 2017 rates; SSVEC 2026 rate case outcome not confirmed.

## Not verified / blank cells
- CSU: The Energy Wise business rate sheet ($/kW demand charge values) not read; only the residential rate sheet (as of 1 Jul 2026). The CSU net-metering restructure was approved 22 Sep 2026 (Gazette); the exact effective date and final tariff numbers (search snippets: $1.00/day Grid Access Charge, A&F on-peak $0.3089 summer / $0.1544 winter) are not from a primary source. CSU legacy NM export credit value not found. CSU storage program (planned ~Mar 2027) has no published incentive. CSU joined SPP in spring 2026 per Gazette; rto tagged WECC-nonRTO per instructions.
- Holy Cross: net metering / export credit rate (Renewable Energy Net Metering Service - Optional Tariff) not extracted; Power+FLEX page shows $10.60/kW-month now (scan noted $10.30 plus an alternative TOU battery incentive; the alternative was not on the page - possibly retired). Peak Time Payback source page is accordion-based; values read from page text.
- CORE: TOU rate $ values and non-residential demand $/kW not extracted (rate schedule PDF not read); no battery incentive or EV rate found; "Small QF not available with battery charging" is only in a search summary.
- United Power: Battery Pilot page (unitedpower.com/battery) returned "Page Not Found" on 2026-09-28; details (Generac/Lithion/Sol-Ark, monthly credit by size, 70% dispatch) come from search snippets only -> Unverified, credit $ unpublished. Net metering annual cash-out rate and commercial/C&I rates not extracted. EV smart-charging rate details beyond RTD1 not extracted.
- Black Hills CO: net metering buyback rate not found (120% sizing cap only); no storage incentive found (only Colorado state tax credit mentioned in third-party results); rate review filed 12 Jun 2026 proposes new rates Mar 2027 (residential +8.8%); TOD rates cited are from the 2025 fact sheet.
- Fort Collins: Peak Partners program page (fcgov.com) redirects to the city home; $50 install fee is from a search summary. Efficiency Works Flex incentive amounts (beyond $50 enrollment from a search summary) not read. Commercial TOD/demand rates and Platte River rates not captured. Flex EV shown as coming soon.
- Poudre Valley REA: tariff dollar values (ATOU etc.) are lost in the PDF text; on/off-peak $0.188/$0.05464 appears only in a search snippet. Battery Rewards program NOT found on pvrea.coop (scan/Nectar claim unconfirmed) - no row emitted. Power Peak Rewards annual credit amount not extracted. NP avoided-cost value not extracted.
- Longmont: no commercial/C&I rates read; no storage incentive or EV rate found.
- SSVEC: no residential DR/thermostat program, no battery/storage incentive found; export rate $0.071165/kWh is a proposal quoted by a third-party blog (Net Zero Solar), not the ACC decision. GT/PT demand and energy values not extracted.
- Trico: RS2TOU-replacement current TOU rate not found; net-metering $0.03659/kWh avoided-cost true-up is from a search summary. No battery incentive besides on-bill loan.
- UNS: RCP page still lists $0.0680 for Oct 2024-Sep 2025 (current 2025-26 rate not seen); residential TOU (non-demand) and EV TOU values not read (uesaz.com/time-of-use, docs.uesaz.com Sheet 110); no residential DR program (ACC removed pilot) per scan; no storage incentive found.
- PNM: Rider 24 net metering PDF unreadable (empty text) so the export row rests on a third-party summary (Unverified); no PNM residential/commercial battery incentive or VPP found; 3B/3C/4B and Rider 8 interruptible values not extracted; Smart Home Charging and charger rebate amounts are Secondary (search summaries).
- El Paso Electric NM: NM commercial TOD/Schedule 24 and any NM thermostat/DR program not found; "EV Rate Plans" (whole-house EV rate) values not read; NM net-metering credit $ not published beyond "fuel and purchased power adjustment".

## Checked absences (no row emitted)
- No residential battery/VPP program found for CORE, Black Hills CO, Longmont, SSVEC, Trico (TEMP thermostat only), UNS, PNM, El Paso Electric NM.
- Fort Collins/Platte River: no separate Platte River BYOB battery VPP found beyond the utility battery incentive.
