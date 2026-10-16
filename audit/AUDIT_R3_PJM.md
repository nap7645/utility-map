# AUDIT R3 presence re-audit: PJM

Seed 20261016. Sample audit/samples_r3/PJM.json (20 items). Results audit/results_r3/PJM.json. Method: cited URL first, then at most one utility-site search/replacement; WebFetch/WebSearch only. NOT_DONE: 0.

| Set | Confirmed | Refuted | Inconclusive | Rate (excl. inconcl.) | Bar | Pass |
|---|---|---|---|---|---|---|
| Yes | 5 | 1 | 2 | 5/6 = 83.3% | 95% | FAIL |
| No | 11 | 0 | 1 | 11/11 = 100.0% | 90% | PASS |

Counting inconclusive as not-confirmed: Yes 5/8, No 11/12. Small n (~10 per set): one miss moves the rate ~10 pts.

## Items

| idx | eia_id | utility | cell | claimed | verdict | evidence | note |
|---|---|---|---|---|---|---|---|
| 0 | 84 | A&N Electric Cooperative | ci_dispatch | Yes | CONFIRMED | https://www.anec.com/your-account/anec-rates/ | Rates page lists Schedule CS-1 (Curtailable Service Rider) under Non-Residential. SOURCE DEFECT: cited cs-1.pdf blocked by robots (unreadable to fetcher); replace with rates page. |
| 1 | 9575 | Jackson Energy Cooperative | res_dispatch | Yes | INCONCLUSIVE | https://www.jacksonenergy.com/energy-efficiency-programs | EKPC page shows SimpleSaver (thermostat/AC, up to $20/yr credits) for unnamed 'participating co-ops'. Jackson's own EE page lists no load-control program; Jackson absent from 2012 Kentucky Living SimpleSaver co-op list; Jackson DSM-1 DLC tariff page cancelled 2019. Participation not shown; leans No. |
| 2 | 963 | Atlantic City Electric Co (ACE) | res_habit | Yes | INCONCLUSIVE | https://www.atlanticcityelectric.com/SmartEnergy/InnovationAndTechnology/Pages/ElectricVehicleProgram.aspx | Cited page and /evsmart render JS-only (no text). NJ BPU 5/24/2023 order shows ACE proposed off-peak BGS EV energy credit eff. 6/1/2023 (not a full TOU); approval paragraphs not visible. Need tariff PDF check. |
| 3 | 14711 | Pennsylvania Electric Co (Penelec) | ci_dispatch | Yes | REFUTED | https://www.firstenergycorp.com/save_energy/save_energy_pennsylvania/pennpower/for_your_business/commercial-industrial-demand-response.html | Cited page (2017 release) and current C&I DR page/FAQ: 'The DR Program is only offered to customers of Met-Ed, Penn Power and West Penn Power'; dated 2017-2020, last mod 2021. Penelec excluded. Phase V (2026-31) plan not checked. DATA DEFECT also: state=OH, Penelec is PA. |
| 4 | 12515 | Midwest Electric, Inc. | res_dispatch | Yes | CONFIRMED | https://midwestrec.com/rebates | Midwest Electric (midwestrec.com) Cool Returns AC switch ($100 + $5/mo Jun-Sep credit), water heater load-mgmt switch required. SOURCE DEFECT: cited Buckeye 'about' page shows no program; replace URL. |
| 5 | 4622 | Cumberland Valley Electric | res_dispatch | Yes | CONFIRMED | https://cumberlandvalley.coop/smart-thermostat | CVE page: '$100 rebate through our SimpleSaver program'; EKPC page shows SimpleSaver thermostats/CAC with up to $20/yr participation credits. Kentucky Living lists CVE as SimpleSaver co-op. Recommend citing CVE page. |
| 6 | 20477 | City of Westerville (Westerville Electric Division) | res_dispatch | Yes | CONFIRMED | https://www.westerville.org/services/electric/programs/community-energy-savings-program | Smart thermostat DR program, launched, residents can opt in (BYOD). |
| 7 | 6194 | Farmers RECC | ci_dispatch | Yes | CONFIRMED | https://www.farmersrecc.com/rates-business | Business rates page lists Interruptible Service Tariff, Voluntary Interruptible Service Tariff, Commercial Direct Load Control Tariff. SOURCE DEFECT: cited EKPC EE page is residential; replace URL. |
| 8 | 4117 | Community Electric Cooperative | res_habit | No | CONFIRMED | https://www.comelec.coop/your-account/rates/ | Only Schedule A Residential; no TOU/EV/demand/CPP. Nav has 'Beat the Peak' link (undescribed; typically voluntary peak alerts, not a rate). |
| 9 | 3329 | Chambersburg Electric Department (Borough of Chambersburg) | res_habit | No | CONFIRMED | https://ecode360.com/29119315 | Residential 201/211/218 flat energy charge only. |
| 10 | 21244 | Southside Electric Cooperative | ci_dispatch | No | CONFIRMED | https://www.sec.coop/energy-services-and-programs/energy-services-programs-savings-programs/ | No C&I interruptible/DR on programs page; site search found none. (Res smart-thermostat DR exists; not this cell.) |
| 11 | 3329 | Chambersburg Electric Department (Borough of Chambersburg) | ci_dispatch | No | CONFIRMED | https://ecode360.com/29119315 | No interruptible/curtailable/DR provisions. Note: Schedule HV has time-of-day option (relevant to ci_habit, not sampled). |
| 12 | 16558 | City of Salem Electric Department | ci_dispatch | No | CONFIRMED | https://salemva.gov/DocumentCenter/View/2525/Electric-Rates-PDF | Schedules list has no interruptible/curtailable/DR. |
| 13 | 4065 | City of Columbus, Division of Power | ci_habit | No | CONFIRMED | https://www.columbus.gov/files/sharedassets/city/v/15/services/public-utilities/dop-rates.pdf | Commercial schedules flat/demand only; no TOU/RTP. |
| 14 | 3291 | Central Virginia Electric Cooperative | ci_habit | No | INCONCLUSIVE | https://www.mycvec.com/account/rate-schedules/ | No TOU named, but Schedule LPM (Large Power Market Service, >=5 MW, member commits to market purchases) may be market/RTP pass-through; Appendix A not readable. Re-check LPM terms. |
| 15 | 17564 | South Kentucky RECC | res_habit | No | CONFIRMED | https://psc.ky.gov/tariffs/electric/South Kentucky RECC/Tariff.pdf | Classes of Service: Schedule A only residential; no TOU/ETS/EV/demand. (Residential DLC program R-33..R-36 exists - dispatch, not habit.) |
| 16 | 19856 | Vineland Municipal Electric Utility | res_dispatch | No | CONFIRMED | https://utilities.vinelandcity.org/rate-tariffs/ | Residential Rate 01 only; no DR/load control. |
| 17 | 5625 | Easton Utilities Commission | ci_dispatch | No | CONFIRMED | https://eastonutilities.com/wp-content/info/electric-tariff.pdf | Tariff classes R/GS-S/GS-L/GS-P, riders USP/ER/RGGI; no interruptible/DR. Site search found no DR program. Tariff text partly truncated. |
| 18 | 13208 | City of Naperville Electric Utility | res_habit | No | CONFIRMED | https://www.naperville.il.us/services/electric-utility/your-electric-service/electric-rates/ | Residential flat customer + energy charge, demand N/A; site search found no TOU/EV rate. |
| 19 | 16558 | City of Salem Electric Department | res_dispatch | No | CONFIRMED | https://salemva.gov/192/Electric | No residential load control on electric page or rates PDF. |

## Defects

| eia_id | cell | issue | fix | URL |
|---|---|---|---|---|
| 84 | ci_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.anec.com/your-account/anec-rates/ |
| 9575 | res_dispatch | inconclusive | re-check (see note) | https://www.jacksonenergy.com/energy-efficiency-programs |
| 963 | res_habit | inconclusive | re-check (see note) | https://www.atlanticcityelectric.com/SmartEnergy/InnovationAndTechnology/Pages/ElectricVehicleProgram.aspx |
| 14711 | ci_dispatch | wrong value (Yes) | set No; update source_url | https://www.firstenergycorp.com/save_energy/save_energy_pennsylvania/pennpower/for_your_business/commercial-industrial-demand-response.html |
| 14711 | ci_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.firstenergycorp.com/save_energy/save_energy_pennsylvania/pennpower/for_your_business/commercial-industrial-demand-response.html |
| 12515 | res_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://midwestrec.com/rebates |
| 6194 | ci_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.farmersrecc.com/rates-business |
| 3291 | ci_habit | inconclusive | re-check (see note) | https://www.mycvec.com/account/rate-schedules/ |
