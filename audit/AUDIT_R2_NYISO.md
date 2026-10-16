# Round-2 presence re-audit: NYISO

Seed 20261015. Sample: audit/samples_r2/NYISO.json (8 items). Auditor: independent r2 agent, 2026-10-15. Method: cited source_url first, one replacement search; WebFetch/WebSearch only.

## Rates

| Claimed | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. (as miss) | Bar | Pass |
|---|---|---|---|---|---|---|---|---|
| Yes | 3 | 2 | 0 | 1 | 100.0% | 66.7% | 95% | PASS |
| No | 5 | 5 | 0 | 0 | 100.0% | 100.0% | 90% | PASS |

Note: small n; one miss moves the Yes rate by >10 pts in PJM/NYISO.

## Items

| idx | eia_id | utility | cell | claimed | verdict | correct | evidence |
|---|---|---|---|---|---|---|---|
| 0 | 14154 | Orange & Rockland Utilities Inc (O&R) | ci_habit | Yes | CONFIRMED | Yes | https://edge-c-dcxprod-web-enfbhbfkb2fghhey.a03.azurefd.net/-/media/files/oru/documents/rates/new-york/electric/ny-electric-tariff.pdf?rev=7d156d95789c428c90046b3bb0accedd&hash=FC7E6776540FC535D723523A31354456 |
| 1 | 3249 | Central Hudson Gas & Electric Corp | ci_dispatch | Yes | INCONCLUSIVE | - | https://www.cenhud.com/globalassets/pdf/save-energy/csrp-tariff-2025.pdf |
| 2 | 14154 | Orange & Rockland Utilities Inc (O&R) | res_dispatch | Yes | CONFIRMED | Yes | https://greatergrid.com/enroll/programs/thermostats/oru |
| 3 | 15145 | Plattsburgh Municipal Lighting Department (PMLD) | res_dispatch | No | CONFIRMED | No | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 4 | 15145 | Plattsburgh Municipal Lighting Department (PMLD) | res_habit | No | CONFIRMED | No | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 5 | 6775 | Freeport Electric (Village of Freeport) | res_dispatch | No | CONFIRMED | No | https://www.freeportelectric.com/2148/Green-Initiative |
| 6 | 5930 | Fairport Electric (Fairport Municipal Commission) | res_dispatch | No | CONFIRMED | No | https://www.village.fairport.ny.us/departments/electric_department/energy_conservation.php |
| 7 | 5930 | Fairport Electric (Fairport Municipal Commission) | ci_dispatch | No | CONFIRMED | No | https://cms9files.revize.com/fairport/electric/Billing/12-1-25%20Billing%20Sheet.pdf |

## Defects

Value defects (cell must change):

- none

Source defects (value OK, cited URL does not show the claim; replace source_url):

- 14154 Orange & Rockland Utilities Inc (O&R) `ci_habit`: replace with https://edge-c-dcxprod-web-enfbhbfkb2fghhey.a03.azurefd.net/-/media/files/oru/documents/rates/new-york/electric/ny-electric-tariff.pdf?rev=7d156d95789c428c90046b3bb0accedd&hash=FC7E6776540FC535D723523A31354456
- 14154 Orange & Rockland Utilities Inc (O&R) `res_dispatch`: replace with https://greatergrid.com/enroll/programs/thermostats/oru

Inconclusive (needs human / browser check):

- 3249 Central Hudson Gas & Electric Corp `ci_dispatch`: Cited PDF and centralhudson.com C&I DR page return bot-check interstitial. Piclo listing (updated 2025-09-30) says CH CSRP 'inactive or no longer accepting new applicants' (off-season; competed annually, Jun-Sep, enroll by May 1/Jun 1). Lean CONFIRMED (NY PSC-mandated CSRP/DLRP) but not verifiable on a utility page.

## Item notes

- [0] Orange & Rockland Utilities Inc (O&R) ci_habit: SOURCE DEFECT: cited EV Charging Rewards page is a driver-level managed-charging incentive, not a C&I rate. NY P.S.C. No. 3 tariff TOC: SC 20 General Secondary Optional TOU, SC 21 General Primary Optional TOU, Rider M Voluntary Day-Ahead Hourly Pricing. Replace source_url with oru.com NY electric tariff page.
- [1] Central Hudson Gas & Electric Corp ci_dispatch: Cited PDF and centralhudson.com C&I DR page return bot-check interstitial. Piclo listing (updated 2025-09-30) says CH CSRP 'inactive or no longer accepting new applicants' (off-season; competed annually, Jun-Sep, enroll by May 1/Jun 1). Lean CONFIRMED (NY PSC-mandated CSRP/DLRP) but not verifiable on a utility page.
- [2] Orange & Rockland Utilities Inc (O&R) res_dispatch: SOURCE DEFECT: cited NYSERDA DLM overview shows O&R BYOB only as 'launching shortly' (tentative go-live 2/15/2026). O&R Bring Your Own Thermostat (implementer enrollment page): residential/commercial NY+NJ, $85/thermostat + $25/yr, ENROLL buttons live.
- [3] Plattsburgh Municipal Lighting Department (PMLD) res_dispatch: Only SC 1 Residential (seasonal/block); no load control/DR/interruptible for residential.
- [4] Plattsburgh Municipal Lighting Department (PMLD) res_habit: SC 1 seasonal block rate; no TOU/EV/demand/CPP for residential.
- [5] Freeport Electric (Village of Freeport) res_dispatch: Green Initiative page lists fleet EVs, solar incentive, LED streetlights; no DR/thermostat/load control. Search of freeportelectric.com found none. Confidence moderate.
- [6] Fairport Electric (Fairport Municipal Commission) res_dispatch: Only rebate programs (appliance, heat pump, commercial, yard equipment) via IEEP; no DR/load control.
- [7] Fairport Electric (Fairport Municipal Commission) ci_dispatch: Classes 1-6 (eff 12/1/2025); no interruptible/curtailable/DR rider or credit for C&I.
