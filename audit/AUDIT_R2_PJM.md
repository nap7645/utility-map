# Round-2 presence re-audit: PJM

Seed 20261015. Sample: audit/samples_r2/PJM.json (20 items). Auditor: independent r2 agent, 2026-10-15. Method: cited source_url first, one replacement search; WebFetch/WebSearch only.

## Rates

| Claimed | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. (as miss) | Bar | Pass |
|---|---|---|---|---|---|---|---|---|
| Yes | 8 | 7 | 1 | 0 | 87.5% | 87.5% | 95% | FAIL |
| No | 12 | 7 | 3 | 2 | 70.0% | 58.3% | 90% | FAIL |

Note: small n; one miss moves the Yes rate by >10 pts in PJM/NYISO.

## Items

| idx | eia_id | utility | cell | claimed | verdict | correct | evidence |
|---|---|---|---|---|---|---|---|
| 0 | 17564 | South Kentucky RECC | ci_dispatch | Yes | CONFIRMED | Yes | https://psc.ky.gov/tariffs/electric/South Kentucky RECC/Tariff.pdf |
| 1 | 40224 | Central Electric Cooperative | res_dispatch | Yes | CONFIRMED | Yes | https://www.central.coop/load-management-program |
| 2 | 3542 | Duke Energy Ohio | ci_dispatch | Yes | CONFIRMED | Yes | https://dam.assets.ohio.gov/image/upload/puco.ohio.gov/empliibrary/files/docketing/tariffs/Electric/Duke%20Energy%20Ohio%20-%20Electric/PUCO%2019%20Schedules%20of%20Rates,%20Classifications,%20Rules%20andRegulations.pdf |
| 3 | 5070 | Delaware Electric Cooperative | ci_dispatch | Yes | REFUTED | No | https://www.delaware.coop/btp |
| 4 | 40222 | Valley Rural Electric Cooperative | res_dispatch | Yes | CONFIRMED | Yes | https://www.valleyrec.com/content/demand-response-details |
| 5 | 6442 | Fleming-Mason Energy Cooperative | ci_dispatch | Yes | CONFIRMED | Yes | https://psc.ky.gov/tariffs/electric/Fleming-Mason RECC/Cancelled Tariff Pages/2026/Schedule IS - Interruptible Service/05-01.pdf |
| 6 | 3503 | Choptank Electric Cooperative | res_dispatch | Yes | CONFIRMED | Yes | https://www.choptankelectric.coop/sites/default/files/CL%20Choptank_August%202026.pdf |
| 7 | 733 | Appalachian Power Co (AEP - Virginia) | res_habit | Yes | CONFIRMED | Yes | https://www.appalachianpower.com/clean-energy/electric-cars/virginia-off-peak |
| 8 | 17044 | Shelby Energy Cooperative | res_habit | No | CONFIRMED | No | https://psc.ky.gov/tariffs/Electric/Shelby Energy Cooperative, Inc/Tariff.pdf |
| 9 | 18085 | South Central Power Company | ci_habit | No | CONFIRMED | No | https://www.southcentralpower.com/your-account/member-rates/ |
| 10 | 7908 | Hagerstown Light Department | res_dispatch | No | CONFIRMED | No | https://www.hagerstownmd.org/153/Tariffs |
| 11 | 18498 | Taylor County RECC | res_habit | No | CONFIRMED | No | https://psc.ky.gov/tariffs/Electric/Taylor County RECC/Tariff.pdf |
| 12 | 6442 | Fleming-Mason Energy Cooperative | res_habit | No | REFUTED | Yes | https://psc.ky.gov/tariffs/electric/Fleming-Mason%20RECC/Cancelled%20Tariff%20Pages/2026/Schedule%20RSP-TOD%20-%20Residential%20and%20Small%20Power%20-%20Time%20of%20Day/05-01.pdf |
| 13 | 6194 | Farmers RECC | res_habit | No | REFUTED | Yes | https://psc.ky.gov/tariffs/electric/Farmers RECC/Tariff.pdf |
| 14 | 4065 | City of Columbus, Division of Power | res_habit | No | CONFIRMED | No | https://www.columbus.gov/files/sharedassets/city/v/15/services/public-utilities/dop-rates.pdf |
| 15 | 1886 | Blue Grass Energy Cooperative | res_habit | No | REFUTED | Yes | https://psc.ky.gov/tariffs/electric/Bluegrass%20Energy%20Coop.%20Corp/Cancelled%20Tariff%20Pages/2026/GS-3%20(Residential%20and%20Farm%20Time-of-Day%20Rate)/05-01.pdf |
| 16 | 7558 | Grayson RECC | res_habit | No | CONFIRMED | No | https://psc.ky.gov/tariffs/Electric/Grayson RECC/Tariff.pdf |
| 17 | 7908 | Hagerstown Light Department | res_habit | No | CONFIRMED | No | https://www.hagerstownmd.org/153/Tariffs |
| 18 | 84 | A&N Electric Cooperative | res_dispatch | No | INCONCLUSIVE | - | https://www.anec.com/energy-efficiency/energy-efficiency-programs/ |
| 19 | 14251 | Owen Electric Cooperative | res_habit | No | INCONCLUSIVE | - | https://psc.ky.gov/tariffs/electric/Owen%20Electric%20Cooperative,%20Inc/Cancelled%20Tariff%20Pages/2024/Schedule%201-B2%20-%20Farm%20and%20Home%20-%20Time%20of%20Day/09-01.pdf |

## Defects

Value defects (cell must change):

- 5070 Delaware Electric Cooperative `ci_dispatch`: Yes -> No. Cited Beat the Peak page is residential only (batteries, Wi-Fi thermostats); R-LM is residential load mgmt and excludes C&I. No C&I interruptible/curtailable/DR found on delaware.coop via search. Confidence moderate. URL: https://www.delaware.coop/btp
- 6442 Fleming-Mason Energy Cooperative `res_habit`: No -> Yes. Schedule RSP-TOD residential TOD (on 13.7c / off 6.9c, open to all residential) eff 9/1/2024; re-issued in 5/1/2026 whole-tariff revision alongside RSP-ETS. Current sheet not directly viewed (Tariff.pdf fetch failed). URL: https://psc.ky.gov/tariffs/electric/Fleming-Mason%20RECC/Cancelled%20Tariff%20Pages/2026/Schedule%20RSP-TOD%20-%20Residential%20and%20Small%20Power%20-%20Time%20of%20Day/05-01.pdf
- 6194 Farmers RECC `res_habit`: No -> Yes. Current Farmers RECC tariff contains 'SCHEDULE R - TIME-OF-DAY - RESIDENTIAL SERVICE'; also Schedule RM Residential Off-Peak Marketing-ETS history. URL: https://psc.ky.gov/tariffs/electric/Farmers RECC/Tariff.pdf
- 1886 Blue Grass Energy Cooperative `res_habit`: No -> Yes. GS-3 Residential and Farm Time-of-Day Rate, available to all GS-1 consumers, eff 7/21/2025; re-issued in 5/1/2026 revision with all 17 schedules (incl. GS-1). Current sheet not directly viewed. URL: https://psc.ky.gov/tariffs/electric/Bluegrass%20Energy%20Coop.%20Corp/Cancelled%20Tariff%20Pages/2026/GS-3%20(Residential%20and%20Farm%20Time-of-Day%20Rate)/05-01.pdf

Source defects (value OK, cited URL does not show the claim; replace source_url):

- 17564 South Kentucky RECC `ci_dispatch`: replace with https://psc.ky.gov/tariffs/electric/South Kentucky RECC/Tariff.pdf
- 3542 Duke Energy Ohio `ci_dispatch`: replace with https://dam.assets.ohio.gov/image/upload/puco.ohio.gov/empliibrary/files/docketing/tariffs/Electric/Duke%20Energy%20Ohio%20-%20Electric/PUCO%2019%20Schedules%20of%20Rates,%20Classifications,%20Rules%20andRegulations.pdf
- 40222 Valley Rural Electric Cooperative `res_dispatch`: replace with https://www.valleyrec.com/content/demand-response-details
- 6442 Fleming-Mason Energy Cooperative `ci_dispatch`: replace with https://psc.ky.gov/tariffs/electric/Fleming-Mason RECC/Cancelled Tariff Pages/2026/Schedule IS - Interruptible Service/05-01.pdf
- 3503 Choptank Electric Cooperative `res_dispatch`: replace with https://www.choptankelectric.coop/sites/default/files/CL%20Choptank_August%202026.pdf

Inconclusive (needs human / browser check):

- 84 A&N Electric Cooperative `res_dispatch`: Cited Beat the Peak page is alert-only, but ANEC programs page links a 'Thermostat Program' (ODEC). Sister ODEC co-op Choptank reports this thermostat DR program launched (Aug 2026). Link label only, no terms visible. Lean REFUTED (likely Yes); verify ODEC page.
- 14251 Owen Electric Cooperative `res_habit`: Schedule I-B2 Farm & Home TOD open (eff 10/1/2021) until superseded 9/2024; current Tariff.pdf unfetchable so current status unverified. Lean REFUTED.

## Item notes

- [0] South Kentucky RECC ci_dispatch: SOURCE DEFECT: cited EKPC energy-efficiency page shows no C&I DR. Current SKRECC tariff (PSC, mod 9/24/2026) contains 'Direct Load Control Program - DSM - Commercial' (Sheet R-37); ISR rider not visible in current tariff class list. Confidence moderate.
- [1] Central Electric Cooperative res_dispatch: Water-heater DR unit interrupted at peak; electric-heat interruptible second-meter rate.
- [2] Duke Energy Ohio ci_dispatch: Cited PUCO 19 tariff index lists Rider PLM Peak Load Management Program (Sheet 87) and Rider DM-I Industrial Demand Management (Sheet 123, eff 1/3/23). Confirmed from index only; rider text not read. Cited URL now 302-redirects to dam.assets.ohio.gov (update link).
- [3] Delaware Electric Cooperative ci_dispatch: Cited Beat the Peak page is residential only (batteries, Wi-Fi thermostats); R-LM is residential load mgmt and excludes C&I. No C&I interruptible/curtailable/DR found on delaware.coop via search. Confidence moderate.
- [4] Valley Rural Electric Cooperative res_dispatch: SOURCE DEFECT: cited Allegheny CLMS page does not name Valley REC. Valley REC DR page: co-op-installed demand response unit on water heaters / heating-cooling equipment, $100 credit to new participants, enrolling.
- [5] Fleming-Mason Energy Cooperative ci_dispatch: SOURCE DEFECT: EKPC page shows no C&I DR. Schedule IS (250-20,000 kW interruptible, eff 9/1/2021) superseded 5/1/2026 in a whole-tariff revision (all 26 schedules incl. cover page re-issued); current Tariff.pdf unfetchable. Inference that IS persists; confidence moderate.
- [6] Choptank Electric Cooperative res_dispatch: SOURCE DEFECT: cited beat-peak page is an alert-only program. Aug 2026 Co-op Living: 'Choptank Electric Cooperative launched a Thermostat Program for eligible members with a Wi-Fi-enabled smart thermostat' (bill credits for summer reductions).
- [7] Appalachian Power Co (AEP - Virginia) res_habit: Tariff RS-PEV Off-Peak Residential EV, open ('Apply now'). Note state field OH for AEP-Virginia looks wrong (data issue, not this cell).
- [8] Shelby Energy Cooperative res_habit: Only residential off-peak marketing rate pages date to <=2011 (cancelled); no residential TOD/ETS/EV found in searches. Current tariff (eff 5/1/2026) rate-schedule section truncated in fetch. Confidence moderate.
- [9] South Central Power Company ci_habit: Member-rates page lists R, SGS, MGS, LGS, LP, Riders A/B, NB; none TOU/RTP/interruptible; LGS is a plain max-demand charge. Rate PDFs not individually read. Confidence moderate.
- [10] Hagerstown Light Department res_dispatch: Schedules R, C, PLH, OL, TP, SL + riders; no DLC/DR program; Rule 12 reliability interruption only.
- [11] Taylor County RECC res_habit: Current tariff: only Schedule A Residential Farm & Home (flat, eff 5/1/2026); R-1 Residential Marketing Rate cancelled 2024.
- [12] Fleming-Mason Energy Cooperative res_habit: Schedule RSP-TOD residential TOD (on 13.7c / off 6.9c, open to all residential) eff 9/1/2024; re-issued in 5/1/2026 whole-tariff revision alongside RSP-ETS. Current sheet not directly viewed (Tariff.pdf fetch failed).
- [13] Farmers RECC res_habit: Current Farmers RECC tariff contains 'SCHEDULE R - TIME-OF-DAY - RESIDENTIAL SERVICE'; also Schedule RM Residential Off-Peak Marketing-ETS history.
- [14] City of Columbus, Division of Power res_habit: Residential A and A-1 flat per-kWh, no TOU/EV/demand.
- [15] Blue Grass Energy Cooperative res_habit: GS-3 Residential and Farm Time-of-Day Rate, available to all GS-1 consumers, eff 7/21/2025; re-issued in 5/1/2026 revision with all 17 schedules (incl. GS-1). Current sheet not directly viewed.
- [16] Grayson RECC res_habit: Current tariff (eff 5/1/2026): Schedule 1 flat residential only; Schedule 3 off-peak 'RESERVED FOR FUTURE USE'; Schedule 10 Residential TOD (last eff 9/1/2024) cancelled 2026 and absent from TOC. Confidence moderate.
- [17] Hagerstown Light Department res_habit: Schedule R flat energy charge; no TOU/EV/CPP.
- [18] A&N Electric Cooperative res_dispatch: Cited Beat the Peak page is alert-only, but ANEC programs page links a 'Thermostat Program' (ODEC). Sister ODEC co-op Choptank reports this thermostat DR program launched (Aug 2026). Link label only, no terms visible. Lean REFUTED (likely Yes); verify ODEC page.
- [19] Owen Electric Cooperative res_habit: Schedule I-B2 Farm & Home TOD open (eff 10/1/2021) until superseded 9/2024; current Tariff.pdf unfetchable so current status unverified. Lean REFUTED.

## Systemic finding
Of the 7 sampled KY EKPC-member co-op `res_habit` = No cells (all with empty source_url, i.e. never looked up), 3 are refuted (Fleming-Mason, Farmers, Blue Grass), 1 is inconclusive and leans refuted (Owen), and 3 are confirmed (Shelby, Taylor County, Grayson). KY co-op tariffs on psc.ky.gov (`/tariffs/electric/<co-op>/Tariff.pdf` plus `Cancelled Tariff Pages/`) often carry residential time-of-day or ETS off-peak schedules. Every KY co-op `res_habit` No that has an empty source_url should be re-scanned against its PSC tariff. Caveat: Grayson dropped its Schedule 10 TOD in the 5/1/2026 rate case, so a 2026 "cancelled" page does not prove a schedule still exists. Fleming-Mason and Blue Grass were judged refuted because their entire tariff was re-issued on 5/1/2026; their current sheets were not opened directly (the fetch failed).
