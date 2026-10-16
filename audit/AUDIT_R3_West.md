# Audit R3 presence re-audit: West

Seed 20261016. Sample: audit/samples_r3/West.json (20 items). Results: audit/results_r3/West.json. Method: WebFetch/WebSearch, cited URL first, <=1 replacement search on utility's own site.

## Rates vs bars

| Claimed | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. as fail | Bar | Pass |
|---|---|---|---|---|---|---|---|
| Yes | 4 | 2 | 2 | 66.7% | 50.0% | 95% | FAIL |
| No | 12 | 0 | 0 | 100.0% | 100.0% | 90% | PASS |

## Items

| idx | eia_id | utility | cell | claimed | verdict | correct | evidence |
|---|---|---|---|---|---|---|---|
| 0 | 7222 | City of Gillette Utilities | res_habit | Yes | REFUTED | No | https://gillettewy.gov/files/assets/public/v/2/finance/documents/customer-service/utility_rates.pdf |
| 1 | 15248 | Portland General Electric | res_dispatch | Yes | CONFIRMED | Yes | https://portlandgeneral.com/save-money/save-money-home/smart-thermostat-program |
| 2 | 17166 | Sierra Pacific Power Co (NV Energy - North) | res_dispatch | Yes | INCONCLUSIVE | Yes | https://nvenergy.com/home/saveenergy/rebates/smart-thermostat/documents/ParticipationAgreement.pdf |
| 3 | 14224 | Otero County Electric Cooperative | res_habit | Yes | CONFIRMED | Yes | https://www.ocec-inc.com/rates |
| 4 | 13407 | Nevada Power Co (NV Energy - South) | ci_dispatch | Yes | INCONCLUSIVE | Yes | https://www.nvenergy.com/publish/content/dam/nvenergy/brochures_arch/save-with-powershift/smart-thermostat/business/EEDR-Application-Thermostats.pdf |
| 5 | 9336 | CORE Electric Cooperative | ci_dispatch | Yes | CONFIRMED | Yes | https://core.coop/cool-credits/ |
| 6 | 17470 | Snohomish County PUD | res_dispatch | Yes | REFUTED | No | https://www.snopud.com/save-energy/residential/peak-assist-program/ |
| 7 | 3660 | Clark Public Utilities | ci_dispatch | Yes | CONFIRMED | Yes | https://www.clarkpublicutilities.com/wp-content/uploads/2025/11/Clark-Public-Utilities-2025-DRPA-Final-Report.pdf |
| 8 | 10627 | Lakeview Light & Power | ci_habit | No | CONFIRMED | No | https://www.lakeviewlight.com/services/rates-fees/rates/ |
| 9 | 11135 | Logan City Light & Power | ci_habit | No | CONFIRMED | No | https://www.loganutah.gov/government/departments/light_and_power/rates.php |
| 10 | 3240 | Central Electric Cooperative | ci_habit | No | CONFIRMED | No | https://www.cec.coop/your-account/rates/rate-schedules/ |
| 11 | 4442 | Cowlitz PUD | res_dispatch | No | CONFIRMED | No | https://www.cowlitzpud.org/efficiency/residential-programs/ |
| 12 | 17839 | Springfield Utility Board (SUB) | res_dispatch | No | CONFIRMED | No | https://www.subutil.com/conservation/for-your-home/rebates-loans/smart-thermostat-rebates/ |
| 13 | 12744 | Modern Electric Water Company | res_dispatch | No | CONFIRMED | No | https://www.modernelectricwater.com/customer-information/rates/rate-schedule/ |
| 14 | 5086 | Delta-Montrose Electric Association (DMEA) | res_habit | No | CONFIRMED | No | https://www.dmea.com/rates |
| 15 | 40438 | Columbia River PUD | ci_dispatch | No | CONFIRMED | No | https://www.crpud.net/my-pud/rates-policies/current-rate-schedules-2/ |
| 16 | 7548 | Grays Harbor PUD | ci_dispatch | No | CONFIRMED | No | https://www.ghpud.org/customer-service/customer-rates-fees/ |
| 17 | 3739 | Clearwater Power Co | res_dispatch | No | CONFIRMED | No | https://www.clearwaterpower.com/energy-efficiency/rebate-program/ |
| 18 | 13758 | Northern Lights Inc | ci_habit | No | CONFIRMED | No | https://www.nli.coop/account-services/rates/ |
| 19 | 12744 | Modern Electric Water Company | ci_dispatch | No | CONFIRMED | No | https://www.modernelectricwater.com/customer-information/rates/rate-schedule/ |

## Defects (data fixes; not applied)

- presence: eia_id 7222 (City of Gillette Utilities), cell res_habit: Yes -> No. Cited ch.17 PDF and city rate sheet show only flat residential + all-electric residential (customer charge + kWh); demand rate is General Service only. No res TOU/demand/CPP/EV rate found. URL: https://gillettewy.gov/files/assets/public/v/2/finance/documents/customer-service/utility_rates.pdf
- presence: eia_id 17470 (Snohomish County PUD), cell res_dispatch: Yes -> No. Cited FlexResponse page: pilots no longer active (2021-2024). Replacement Peak Assist is behavioral (customer self-curtails, no device control) and starts Jan 2027. No current res device-control program found. URL: https://www.snopud.com/save-energy/residential/peak-assist-program/

## Source defects / inconclusive

- eia_id 15248 res_dispatch (CONFIRMED): SOURCE DEFECT: cited Smart Battery Pilot is full/closed to new participants. Replacement: residential Smart Thermostat Program open (1-3F adjustments during peak events). URL: https://portlandgeneral.com/save-money/save-money-home/smart-thermostat-program
- eia_id 17166 res_dispatch (INCONCLUSIVE): Cited page loads no program content. Undated participation agreement covers N. Nevada thermostat DR (rebate similar to OLM-AS) but does not show program currently open. URL: https://nvenergy.com/home/saveenergy/rebates/smart-thermostat/documents/ParticipationAgreement.pdf
- eia_id 13407 ci_dispatch (INCONCLUSIVE): SOURCE DEFECT: cited summary covers only Retrofit EE program, no DR. Replacement found only a 2018 business thermostat DR application (Nevada Power); no evidence program currently open. URL: https://www.nvenergy.com/publish/content/dam/nvenergy/brochures_arch/save-with-powershift/smart-thermostat/business/EEDR-Application-Thermostats.pdf
