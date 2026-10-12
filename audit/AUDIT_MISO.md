# MISO audit — independent source re-verification

Date: 2026-10-02. Auditor: independent agent (did not build the dataset; no researcher notes or other audit files read). Sample file: `audit/samples/MISO.json`, seed **20261002**, 120 items (top bucket = 5 largest MISO utilities: DTE, Consumers, NSP-MN, Ameren Missouri, Ameren Illinois, 100% checked; plus a stratified sample).

## Method
- Presence Yes: opened the cited `*_src` fresh with WebFetch; CONFIRMED only if the page itself shows that kind of program for that segment and that it's currently offered. If the cited page was dead or wrong, I searched the utility's own site once for a replacement (CONFIRMED with the replacement URL when one was found; the source fix is listed below).
- Presence No: searched the utility's own rate/tariff/program pages (and G&T where relevant). CONFIRMED = nothing found on readable pages; REFUTED = found one (URL given).
- Program rows: checked name, category, $ value and units, status, and eligibility against the cited source_url (or utility tariff). A row is REFUTED if any field is wrong or the source_url doesn't show the claim. wrong_dollar=true only when a $ figure is wrong or stale, not just unsupported by the source.
- Tools: WebFetch/WebSearch only (no curl, no Wayback). JS-only pages (mn.my.xcelenergy.com), 403s and robots blocks were scored INCONCLUSIVE unless another readable page on the utility's own site settled the item.
- Item-level results: `audit/results/MISO.json`.

## Rates vs bars

| Group | n | CONFIRMED | REFUTED | INCONCLUSIVE | Confirmed % (incl. inconcl. in denom.) | Confirmed % (excl. inconcl.) | Bar | Result |
|---|---|---|---|---|---|---|---|---|
| Presence Yes | 24 | 21 | 2 | 1 | 87.5% | 91.3% | >=95% | FAIL |
| Presence No | 19 | 13 | 6 | 0 | 68.4% | 68.4% | >=90% | FAIL |
| Program rows | 77 | 62 | 12 | 3 | 80.5% | 83.8% | log all | n/a (errors logged) |

Wrong $ figures: **4 in top bucket** (bar 0, so **FAIL**), 2 in sample bucket. Top-bucket items: 51, 55, 57, 80.

**MISO fails 3 of 3 bars**: Yes 91.3% excluding inconclusive (bar 95%), No 68.4% (bar 90%), top-bucket wrong $ = 4 (bar 0). The No failures cluster in the top 5 IOUs' C&I cells: 5 of the 6 refuted Nos are top-bucket C&I cells where the utility plainly offers a business TOU or DR program.

## Item table

| # | Bucket | Utility | Cell / program | Claimed | Verdict | $wrong | Evidence URL |
|---|---|---|---|---|---|---|---|
| 0 | top | DTE Electric Co | res_habit | Yes | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 1 | top | DTE Electric Co | res_dispatch | Yes | CONFIRMED |  | https://www.dteenergy.com/us/en/residential/save-money-energy/get-started-with/demand-response.html |
| 2 | top | DTE Electric Co | ci_habit | No | REFUTED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/business/service-and-price/pricing/BusinessElectricRates.pdf |
| 3 | top | DTE Electric Co | ci_dispatch | Yes | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 4 | top | Consumers Energy Co | res_habit | Yes | CONFIRMED |  | https://www.consumersenergy.com/residential/account-and-billing/rates/electric-rates-and-programs/rate-plan-options/time-of-use-rate-plans/critical-peak-pricing-program |
| 5 | top | Consumers Energy Co | res_dispatch | Yes | CONFIRMED |  | https://www.consumersenergy.com/residential/account-and-billing/rates/electric-rates-and-programs/rate-plan-options/time-of-use-rate-plans |
| 6 | top | Consumers Energy Co | ci_habit | No | REFUTED |  | https://www.consumersenergy.com/business/account-and-billing/rates/electric-rates-and-programs/rate-plans/time-of-use-rate-plan |
| 7 | top | Consumers Energy Co | ci_dispatch | No | REFUTED |  | https://www.consumersenergy.com/business/products-and-services/demand-response |
| 8 | top | Northern States Power Co - Minnesota ( | res_habit | Yes | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe-responsive/Company/Rates%20&%20Regulations/24-01-406-MN-Res-ElecRates-MN-Res-E-2002.pdf |
| 9 | top | Northern States Power Co - Minnesota ( | res_dispatch | Yes | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe-responsive/Programs%20and%20Rebates/Residential/22-08-604%20It%20Pays%20To%20Save%20Booklet_MN%202022.pdf |
| 10 | top | Northern States Power Co - Minnesota ( | ci_habit | Yes | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Regulatory/Regulatory%20PDFs/rates/MN/MNBusRateCard.pdf |
| 11 | top | Northern States Power Co - Minnesota ( | ci_dispatch | Yes | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 12 | top | Union Electric Company d/b/a Ameren Mi | res_habit | Yes | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 13 | top | Union Electric Company d/b/a Ameren Mi | res_dispatch | Yes | CONFIRMED |  | https://www.ameren.com/efficiency/programs/peak-time-savings |
| 14 | top | Union Electric Company d/b/a Ameren Mi | ci_habit | No | REFUTED |  | https://www.ameren.com/-/media/rates/missouri/non-residential/electric-rates/rates/uecdsheet55rate2msgs.ashx |
| 15 | top | Union Electric Company d/b/a Ameren Mi | ci_dispatch | No | REFUTED |  | https://www.ameren.com/missouri/business/demand-response |
| 16 | top | Ameren Illinois Company d/b/a Ameren I | res_habit | Yes | CONFIRMED |  | https://www.ameren.com/efficiency/programs/peak-time-rewards |
| 17 | top | Ameren Illinois Company d/b/a Ameren I | res_dispatch | Yes | CONFIRMED |  | https://greatergrid.com/enroll/programs/thermostats/ameren-il |
| 18 | top | Ameren Illinois Company d/b/a Ameren I | ci_habit | Yes | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/illinois/aiel21rdevcp.ashx |
| 19 | top | Ameren Illinois Company d/b/a Ameren I | ci_dispatch | Yes | CONFIRMED |  | https://www.enelnorthamerica.com/solutions/energy-solutions/demand-response/ameren-illinois-demand-response |
| 20 | sample | East Mississippi Electric Power Associ | res_habit | No | CONFIRMED |  | https://www.emepa.com/account/rates-fees-charges/ |
| 21 | sample | Southwestern Electric Cooperative | res_habit | No | CONFIRMED |  | https://www.sweci.com/electric-rates |
| 22 | sample | Pearl River Valley Electric Power Asso | res_habit | No | CONFIRMED |  | https://cdn.prod.website-files.com/5facf9cec837474d213527aa/677ff623304eab01772a8585_GeneralService.pdf |
| 23 | sample | Superior Water Light & Power Co (ALLET | ci_dispatch | No | CONFIRMED |  | https://www.swlp.com/CustomerService/ElectricRatesExtensionRules |
| 24 | sample | Alpena Power Company | res_dispatch | No | CONFIRMED |  | https://www.alpenapower.com/efficient-electric-heat-rates-residential/ |
| 25 | sample | Northern Indiana Public Service Co (NI | res_dispatch | No | CONFIRMED |  | https://www.nipsco.com/save-energy/residential/ac-cycling |
| 26 | sample | Watertown Municipal Utilities | ci_habit | No | CONFIRMED |  | https://www.watertownmu.com/wp-content/uploads/WMU_RateSheet_2026.pdf |
| 27 | sample | Marquette Board of Light & Power | res_habit | No | CONFIRMED |  | https://mblp.org/other-customer-information/ |
| 28 | sample | Lafayette Utilities System | ci_habit | No | CONFIRMED |  | https://www.lus.org/wp-content/uploads/2019/10/2017_Electric-Rates_Commercial_Large.pdf |
| 29 | sample | Runestone Electric Association | res_dispatch | Yes | CONFIRMED |  | https://www.runestoneelectric.com/energy-wise-programs/heating-cooling/ |
| 30 | sample | Stearns Electric Association | ci_dispatch | Yes | CONFIRMED |  | https://greatriverenergy.com/transmission-and-delivery/demand-response/member-cooperative-load-management-programs/ |
| 31 | sample | East Central Energy | res_dispatch | Yes | CONFIRMED |  | https://www.eastcentralenergy.com/water-heating-rebates |
| 32 | sample | Dahlberg Light & Power Company | res_habit | Yes | INCONCLUSIVE |  | https://dahlberglightandpower.com/ |
| 33 | sample | Alpena Power Company | ci_habit | Yes | REFUTED |  | https://www.alpenapower.com/electric-vehicle-rates-programs-business/ |
| 34 | sample | Duke Energy Indiana | res_dispatch | Yes | CONFIRMED |  | https://greatergrid.com/dei/faq?hsLang=en |
| 35 | sample | Brookings Municipal Utilities | res_dispatch | Yes | REFUTED |  | https://www.brookingsutilities.com/Services |
| 36 | sample | Bay City Electric Light & Power | ci_habit | Yes | CONFIRMED |  | https://www.baycitymi.gov/DocumentCenter/View/6126/2022-2024-BCELP-Electric-Service-Rate-Schedule-v2 |
| 37 | sample | City Water Light and Power (Springfiel | res_habit | Yes | CONFIRMED |  | https://www.cwlp.com/Departments/ElectricDeptHome/ElectricInformation/ElectricRates.aspx |
| 38 | sample | Thumb Electric Cooperative | ci_dispatch | No | CONFIRMED |  | https://www.tecmi.coop/rates-tariffs |
| 39 | sample | Presque Isle Electric & Gas Co-op | ci_habit | No | CONFIRMED |  | https://pieg.com/electric-rates/ |
| 40 | sample | Dixie Electric Power Association | res_habit | No | CONFIRMED |  | https://www.dixieepa.com/your-account/rates-fees/ |
| 41 | sample | Indiana Michigan Power - Michigan | ci_habit | No | REFUTED |  | https://www.indianamichiganpower.com/lib/docs/ratesandtariffs/Michigan/IM_MI_TB_Bk_19_2026_08_28.pdf |
| 42 | sample | Muscatine Power & Water (Board of Wate | res_habit | No | CONFIRMED |  | https://mpw.org/wp-content/uploads/MPW-Electric-Rates-07-01-2025.pdf |
| 43 | top | Ameren Illinois Company d/b/a Ameren I | Peak Time Rewards | 75 cents/kWh reduced (2022-23 program year; credit reset annually base | CONFIRMED |  | https://www.ameren.com/efficiency/programs/peak-time-rewards |
| 44 | top | Ameren Illinois Company d/b/a Ameren I | Peak Time Savings (Smart Thermostat) | $50 enrollment + $25/year / Active | CONFIRMED |  | https://greatergrid.com/enroll/programs/thermostats/ameren-il |
| 45 | top | Ameren Illinois Company d/b/a Ameren I | Commercial & Industrial Demand Response Program (E |  / Active | CONFIRMED |  | https://www.enelnorthamerica.com/solutions/energy-solutions/demand-response/ameren-illinois-demand-response |
| 46 | top | Ameren Illinois Company d/b/a Ameren I | Rider EVCP - DS-1 Residential Charging Program | $4/month credit (first 12 months); PCP delivery credit 2.0 cents/kWh s | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/illinois/aiel21rdevcp.ashx |
| 47 | top | Ameren Illinois Company d/b/a Ameren I | Rider EVCP - DS-2/DS-3/DS-4 Non-Residential Chargi | $15/month credit (DS-2, first 12 months); PCP credit 2.3 cents/kWh sum | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/illinois/aiel21rdevcp.ashx |
| 48 | top | Ameren Illinois Company d/b/a Ameren I | Rider NM - Net Metering |  / Active | REFUTED |  | https://www.ameren.com/illinois/residential/supply-choice/renewables/net-metering |
| 49 | top | Ameren Illinois Company d/b/a Ameren I | Hourly Supply Service (HSS) |  / Active | REFUTED |  | https://www.ameren.com/-/media/illinois-site/files/electricchoice/illinois-distributed-energy-rebate-application.ashx |
| 50 | top | Ameren Illinois Company d/b/a Ameren I | Rider PSP - Power Smart Pricing (with Rider RTP) | $2.25/month participation charge / Active | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/illinois/aiel26rdpsp.ashx |
| 51 | top | Ameren Illinois Company d/b/a Ameren I | Rider CGR - Customer Generation Rebate (Distribute | $300/kW DG + $300/kWh storage (residential); $250/kW DG + $250/kWh sto | REFUTED | Y | https://www.ameren.com/-/media/rates/files/illinois/aiel59rdcgr.ashx |
| 52 | top | Consumers Energy Co | Critical Peak Pricing Program | Off-peak/on-peak 17.0c/23c per kWh (non-event); event rate $1.00/kWh 2 | CONFIRMED |  | https://www.consumersenergy.com/residential/account-and-billing/rates/electric-rates-and-programs/rate-plan-options/time-of-use-rate-plans/critical-peak-pricing-program |
| 53 | top | Consumers Energy Co | Peak Time Rewards Program | $1/kW (per program hero) or $0.50/kWh (per PTR summary table) credited | CONFIRMED |  | https://www.consumersenergy.com/residential/account-and-billing/rates/electric-rates-and-programs/rate-plan-options/time-of-use-rate-plans/peak-time-rewards-program |
| 54 | top | Consumers Energy Co | Smart Thermostat Program | $50 enrollment + $25/summer thereafter / Active | CONFIRMED |  | https://www.consumersenergy.com/residential/account-and-billing/rates/electric-rates-and-programs/rate-plan-options/time-of-use-rate-plans |
| 55 | top | Consumers Energy Co | AC Peak Cycling Program | $32/yr bill credits (Jun-Sep, ~$5/mo) + sign-up Visa gift card / Close | REFUTED | Y | https://www.consumersenergy.com/residential/rates/electric-rates-and-programs/rate-plan-options/standard-rate-plan/ac-peak-cycling |
| 56 | top | Consumers Energy Co | PowerMIDrive Smart Charging Incentive | $10/mo credit up to $120 over 12 months per EV / Active | CONFIRMED |  | https://www.consumersenergy.com/residential/savings-and-clean-energy/electric-vehicles/smart-charging-incentive |
| 57 | top | Consumers Energy Co | Distributed Generation Program (Inflow-Outflow) | Export credit approx 6-12 cents/kWh (power supply component only; no d | REFUTED | Y | https://www.consumersenergy.com/residential/savings-and-clean-energy/renewable-energy/distributed-generation |
| 58 | top | Consumers Energy Co | Summer Rate (Default Residential TOU) | On-peak $0.245/kWh; off-peak $0.197/kWh (summer); flat $0.176/kWh non- | CONFIRMED |  | https://consumersenergy.com/summerrate |
| 59 | top | DTE Electric Co | Dynamic Peak Pricing Rate | Peak 10.800c non-capacity+6.398c capacity; mid-peak 5.579c+3.305c; off | INCONCLUSIVE |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 60 | top | DTE Electric Co | Smart Savers (BYOT Thermostat / Rush Hour Rewards  | $50 bill credit per year participated / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/residential/save-money-energy/get-started-with/demand-response.html |
| 61 | top | DTE Electric Co | Capacity Release Rider (Rider 12) | Discounted rate (amount unpublished) / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 62 | top | DTE Electric Co | Interruptible General Service Rate | Discounted vs standard D3 rate (amount unpublished) / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 63 | top | DTE Electric Co | Interruptible Supply Rate | Discounted vs standard D11/D6.2 rate (amount unpublished) / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 64 | top | DTE Electric Co | Interruptible Supply Rider (Rider 10) | Discounted vs D11/D6.2 (amount unpublished) / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 65 | top | DTE Electric Co | Metal Melting Rider (Rider 1.1) | Discounted vs D3/D4/D8/D11 (amount unpublished) / Active | CONFIRMED |  | https://www.dteenergy.com/us/en/business/service-request/pricing/demand-response.html |
| 66 | top | DTE Electric Co | CoolCurrents (Interruptible Space Conditioning Rat | Jun-Oct 7.367c/kWh; Nov-May 5.237c/kWh (power supply, combined capacit | REFUTED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/CoolCurrents.pdf |
| 67 | top | DTE Electric Co | Water Heating Service Rate (Controlled/Interruptib | 4.902c/kWh (power supply, capacity+non-capacity combined) vs standard  | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/save-money-and-energy/rebates-and-offers/water-heaters/WaterHeatingServiceRate.pdf |
| 68 | top | DTE Electric Co | DTE Smart Charge (managed EV charging) | $5/month incentive / Active | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pev/plug-in-electric-vehicles-pev/SmartChargeBrochure.pdf |
| 69 | top | DTE Electric Co | Electric Vehicle Rate | Peak (9a-11p weekdays) 17.359c/kWh; off-peak 4.340c/kWh (power supply, | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 70 | top | DTE Electric Co | Distributed Generation (post-2019) | Unpublished exact c/kWh (power-supply-component credit per MI PA 342 f | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 71 | top | DTE Electric Co | Net Metering (legacy) | Full retail rate credit / Closed to new enrollment | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 72 | top | DTE Electric Co | Overnight Savers Rate | Jun-Sep on 15.991c, off 10.784c, super-off-peak 6.852c per kWh (power  | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 73 | top | DTE Electric Co | Time of Day 11am-7pm Rate | Jun-Oct on 16.203c/kWh, off 5.456c/kWh; Nov-May on 13.687c/kWh, off 5. | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 74 | top | DTE Electric Co | Time of Day 3pm-7pm Rate | Summer (Jun-Sep) on 14.407c/kWh (capacity+non-capacity), off 8.709c/kW | CONFIRMED |  | https://www.dteenergy.com/content/dam/dteenergy/deg/website/residential/Service-Request/pricing/residential-pricing-options/ResidentialElectricRateCard.pdf |
| 75 | top | Northern States Power Co - Minnesota ( | AC Rewards for Business | Free ecobee3 lite installed + annual incentive (amount not published)  | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 76 | top | Northern States Power Co - Minnesota ( | Electric Rate Savings (Interruptible ≥50kW) | Contact for details / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 77 | top | Northern States Power Co - Minnesota ( | Peak Flex Credit | Not published (custom by commitment) / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 78 | top | Northern States Power Co - Minnesota ( | Peak Partner Rewards | $2.00/kW-month reservation + $1.35/kWh event performance / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 79 | top | Northern States Power Co - Minnesota ( | Saver's Switch (Business) | $5.00/ton/month June-September / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/PDF/Marketing/MN-ND-SD-Bus-Savers-Switch-Info-Sheet.pdf |
| 80 | top | Northern States Power Co - Minnesota ( | Saver's Switch (Residential) | $40/yr bill credit (Oct) + $100 one-time enrollment credit / Active | REFUTED | Y | https://www.xcelenergy.com/staticfiles/xe-responsive/Programs%20and%20Rebates/Residential/22-08-604%20It%20Pays%20To%20Save%20Booklet_MN%202022.pdf |
| 81 | top | Northern States Power Co - Minnesota ( | EV Accelerate At Home | Pay-as-you-go: $6.73/mo + 3.8c/kWh off-peak; Subscription: $38.81/mo i | INCONCLUSIVE |  | https://mn.my.xcelenergy.com/s/residential/ev-charging/incentives/evaah |
| 82 | top | Northern States Power Co - Minnesota ( | Optimize Your Charge (Fleet EV) | $50/yr per registered charger or vehicle for off-peak charging / Activ | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 83 | top | Northern States Power Co - Minnesota ( | Solar*Rewards / Net Metering | Solar*Rewards $0.03/kWh production paid annually (systems ≤20kW) / Act | REFUTED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Res-SR-Meter-Billing-Guide.pdf |
| 84 | top | Northern States Power Co - Minnesota ( | Battery Storage Incentive Program | $175/kWh up to $5,000 standard; $370/kWh income-qualified / Active | CONFIRMED |  | https://mn.gov/commerce-stat/energy/consumer/StorageIncentiveProgram_Xcel_08.07.24.pdf |
| 85 | top | Northern States Power Co - Minnesota ( | Dynamic Thermal Storage | 10% of install cost upfront + 5% of project cost annual bill credit /  | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/Marketing/Files/MN-Business-Program-Summary.pdf |
| 86 | top | Northern States Power Co - Minnesota ( | Residential Time-of-Use Rate | On-peak +; off-peak -; ratio ~2.7x summer / 2.2x winter / Active | INCONCLUSIVE |  | https://www.xcelenergy.com/staticfiles/xe-responsive/Billing%20&%20Payment/23-04-531%20MN%20TOU%20Information%20Sheet-final.pdf |
| 87 | top | Union Electric Company d/b/a Ameren Mi | Peak Time Savings (Smart Thermostat) | $50 enrollment + $25/year / Active | CONFIRMED |  | https://www.ameren.com/efficiency/programs/peak-time-savings |
| 88 | top | Union Electric Company d/b/a Ameren Mi | Residential Ultimate Saver Service | Demand charge $9.28/kW summer, $3.83/kW winter / Active | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 89 | top | Union Electric Company d/b/a Ameren Mi | Peak Time Savings - Electric Vehicles (Optiwatt ma | $50 enrollment + $100/year / Active | CONFIRMED |  | https://www.ameren.com/efficiency/programs/peak-time-savings-ev |
| 90 | top | Union Electric Company d/b/a Ameren Mi | Rider NM - Net Metering |  / Active | CONFIRMED |  | https://www.ameren.com/-/media/missouri-site/files/environment/solar/net-metering-tariff.pdf |
| 91 | top | Union Electric Company d/b/a Ameren Mi | Grandfathered Optional TOD (Time-of-Day) Rate Pilo |  / Closed to new enrollment | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 92 | top | Union Electric Company d/b/a Ameren Mi | Residential Evening/Morning Saver Service (default |  / Active | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 93 | top | Union Electric Company d/b/a Ameren Mi | Residential Overnight Saver Service |  / Active | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 94 | top | Union Electric Company d/b/a Ameren Mi | Residential Smart Saver Service |  / Active | CONFIRMED |  | https://www.ameren.com/-/media/rates/files/missouri/uecsheet54rate1mres.ashx |
| 95 | top | Northern States Power Co - North Dakot | Saver's Switch (Business) | $5.00/ton/month June-September / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/PDF/Marketing/MN-ND-SD-Bus-Savers-Switch-Info-Sheet.pdf |
| 96 | top | Northern States Power Co - South Dakot | Saver's Switch (Business) | $5.00/ton/month June-September / Active | CONFIRMED |  | https://www.xcelenergy.com/staticfiles/xe/PDF/Marketing/MN-ND-SD-Bus-Savers-Switch-Info-Sheet.pdf |
| 97 | sample | Lansing Board of Water & Light | Standard Residential Electric Service (RES1) | On-peak $0.1740/kWh; off-peak $0.1504/kWh; plus $22.50/month basic ser | REFUTED | Y | https://www.lbwl.com/customers/pay-bill/understanding-time-use-rates |
| 98 | sample | Duke Energy Indiana | EV Off-Peak Charging Credit Pilot | $50/quarter for 2 years ($400 total) / Active | REFUTED |  | https://illumination.duke-energy.com/articles/how-duke-energy-manages-ev-charging-helps-customers-save |
| 99 | sample | Indiana Michigan Power - Michigan | Distributed Generation (DG) Rider / Net Metering S | Rate/credit figures not published in accessible pages; NMS-1 available | CONFIRMED |  | https://www.indianamichiganpower.com/clean-energy/electric-cars/charge-at-home-michigan |
| 100 | sample | Entergy Louisiana LLC | Net Metering - Rider Schedule NM (grandfathered pr |  / Closed to new enrollment | CONFIRMED |  | https://www.entergylouisiana.com/wp-content/uploads/ell_elec_nm.pdf |
| 101 | sample | Superior Water Light & Power Co (ALLET | Controlled Space Heating (ED1/CSHS) | $0.0837/kWh vs standard $0.1393/kWh / Active | CONFIRMED |  | https://www.swlp.com/CustomerService/ElectricRatesExtensionRules |
| 102 | sample | Wisconsin Power & Light Co (Alliant En | Smart Hours - Electric Vehicles/Chargers | $25 enrollment (virtual Visa) + $25/season participated / Active | CONFIRMED |  | https://www.alliantenergy.com/ways-to-save/smart-hours/wisconsin |
| 103 | sample | Wisconsin Electric Power Co (We Energi | Smart Thermostat Rewards | $25 enrollment + $6.25/mo Jun-Sep ($50 yr 1); $25/yr thereafter / Pilo | CONFIRMED |  | https://www.we-energies.com/services/smart-thermostat-rewards-program |
| 104 | sample | Cleco Power LLC | Distributed Generation Service (net metering, pre- |  / Closed to new enrollment | CONFIRMED |  | https://www.cleco.com/residential-commercial/interconnections/distributed-generation |
| 105 | sample | Interstate Power and Light Company (Al | Inflow/Outflow Distributed Generation Tariff |  / Active | CONFIRMED |  | https://www.alliantenergy.com/-/media/alliant/documents/accountandbilling/ratesandtariffs/iowaelectricrates/inflowoutflowtariff.pdf |
| 106 | sample | Wisconsin Power & Light Co (Alliant En | Electric Interruptible Program (Cp-1/Cp-2) | Discount on electricity price for entire year (amount set in Cp-1/Cp-2 | CONFIRMED |  | https://www.alliantenergy.com/ways-to-save/interruptible-program/wisconsin-electric |
| 107 | sample | Entergy Arkansas LLC | Non-Legacy Net-Metering Service (NLN-M) | avoided cost rate redetermined annually (MISO/SPP LMP-based) / Active | CONFIRMED |  | https://www.entergyarkansas.com/wp-content/uploads/2025/06/eal_nln-m.pdf |
| 108 | sample | AES Indiana (formerly IPL) | CoolCents Direct Load Control |  / Active | CONFIRMED |  | https://www.aesindiana.com/sites/aesvault.com/files/2025-01/CoolCents-TC-Release-Form-AES-Indiana-Jan-2025.pdf |
| 109 | sample | Entergy Texas Inc | eMobility Solutions - CI Rider / DA Rider / EVCI ( | $250 Level 2 rebate; custom DC fast charger rebates / Active | CONFIRMED |  | https://emobility.entergy.com/assets/images/homepage/eMobility%20Solutions%20Rates%20and%20Riders.pdf |
| 110 | sample | WPPI Energy | Power Partner Rewards (formerly Bring Your Own Dev | $25 enrollment bill credit + $25/summer participated (up to $50 total) | REFUTED |  | https://www.renewwisconsin.org/psc-approves-wppis-bring-your-own-device-demand-response-program/ |
| 111 | sample | Midcontinent ISO | Demand Response Resource Type I (DRR-I) | Paid at real-time or day-ahead LMP for cleared MW reduction / Active | CONFIRMED |  | https://cpowerenergy.com/wp-content/uploads/2022/12/MISO-BPM-026-Business-Practices-for-DR.pdf |
| 112 | sample | Entergy New Orleans LLC | Virtual Power Plant Pilot (EnergyHub-managed resid | up to $600/yr per participating battery / Pilot | REFUTED | Y | https://lailluminator.com/2026/02/25/new-orleans-battery/ |
| 113 | sample | Lansing Board of Water & Light | Off-Peak Savers Standard Small Commercial Electric | Summer: on-peak $0.2976/kWh, off-peak $0.1388/kWh; Winter: on-peak $0. | CONFIRMED |  | https://www.lbwl.com/documents/2025-business-electric |
| 114 | sample | Ozarks Electric Cooperative | Net Metering | avoided cost per prior-year APSC filing; credits roll over monthly and | CONFIRMED |  | https://www.ozarksecc.com/net-metering |
| 115 | sample | Entergy Arkansas LLC | eMobility Solutions - CI Rider / DA Rider (fleet & | $250 Level 2 rebate; custom DC fast charger rebates / Active | CONFIRMED |  | https://emobility.entergy.com/assets/images/homepage/eMobility%20Solutions%20Rates%20and%20Riders.pdf |
| 116 | sample | Dixie Electric Membership Corp (DEMCO) | Residential Time-of-Use Rate |  / Active | CONFIRMED |  | https://demco.org/residential-time-use-rates |
| 117 | sample | CenterPoint Energy Indiana South (form | Smart Cycle (smart thermostat DR) | $75 one-time enrollment + $7.50/month (Mar-Nov) / Active | CONFIRMED |  | https://www.centerpointenergy.com/en-us/residential/save-energy-money/saving-energy/smart-cycle?sa=in |
| 118 | sample | Great River Energy | Interruptible Irrigation | Varies by member cooperative / Active | CONFIRMED |  | https://greatriverenergy.com/transmission-and-delivery/demand-response/member-cooperative-load-management-programs/ |
| 119 | sample | Midcontinent ISO | Electric Storage Resource (ESR) Participation Mode |  / Active | CONFIRMED |  | https://help.misoenergy.org/knowledgebase/article/KA-01336/en-us |

## Defect list (proposed fixes; dataset NOT edited)

Presence cells: `data/processed/presence.csv` (line no. incl. header) and the matching `data/raw/presence_scan/scan_*.csv` row. Program rows: `data/processed/programs.csv`, `row` = the sample's `row` field.

### Presence
| Item | File / line / cell | Current | Fix |
|---|---|---|---|
| 2 | presence.csv line 22, DTE ci_habit | No | Yes; src https://www.dteenergy.com/content/dam/dteenergy/deg/website/business/service-and-price/pricing/BusinessElectricRates.pdf (D3.11 Commercial TOU, D14 Primary TOU) |
| 6 | presence.csv line 21, Consumers ci_habit | No | Yes; src https://www.consumersenergy.com/business/account-and-billing/rates/electric-rates-and-programs/rate-plans/time-of-use-rate-plan |
| 7 | presence.csv line 21, Consumers ci_dispatch | No | Yes; src https://www.consumersenergy.com/business/products-and-services/demand-response |
| 14 | presence.csv line 201, Ameren MO ci_habit | No | Yes; src Rate 2M sheet (Optional Overnight Saver / Optional TOD) https://www.ameren.com/-/media/rates/missouri/non-residential/electric-rates/rates/uecdsheet55rate2msgs.ashx |
| 15 | presence.csv line 201, Ameren MO ci_dispatch | No | Yes; src https://www.ameren.com/missouri/business/demand-response |
| 41 | presence.csv line 143, I&M-Michigan ci_habit | No | Yes; src https://www.indianamichiganpower.com/lib/docs/ratesandtariffs/Michigan/IM_MI_TB_Bk_19_2026_08_28.pdf (GS-TOD, GS-TOD2, GS-CPP). Also check ci_dispatch (VCSR, DLMS riders) |
| 33 | presence.csv line 20, Alpena ci_habit | Yes | Set Unknown (or No after checking the MPSC #10 rate book); the cited business EV page only shows the residential PEV rate |
| 35 | presence.csv line 383, Brookings res_dispatch | Yes | Set Unknown; the cited Services page shows no load-control program |
| 32 | presence.csv line 79, Dahlberg res_habit | Yes | Cited homepage shows no rate; replace src with the PSC WI tariff (apps.psc.wi.gov returned 403) or set Unknown |
| 8 | presence.csv line 33, NSP-MN res_habit | Yes (src JS-only) | Replace src: https://www.xcelenergy.com/staticfiles/xe-responsive/Company/Rates%20&%20Regulations/24-01-406-MN-Res-ElecRates-MN-Res-E-2002.pdf |
| 9 | presence.csv line 33, NSP-MN res_dispatch | Yes (src = Colorado doc) | Replace src with an MN Saver's Switch page, e.g. MN It Pays To Save booklet |
| 10 | presence.csv line 33, NSP-MN ci_habit | Yes (src lacks TOU) | Replace src: https://www.xcelenergy.com/staticfiles/xe/Regulatory/Regulatory%20PDFs/rates/MN/MNBusRateCard.pdf |
| 34 | presence.csv line 121, Duke IN res_dispatch | Yes (src now Online Savings Store) | Replace src: https://greatergrid.com/dei/faq (Power Manager thermostat) or the Duke IN Power Manager page |
| 16 | presence.csv line 215, Ameren IL hifld_state | MO | Check: hifld_state is MO for EIA 56697; Ameren Illinois is IL (may be HIFLD polygon artifact) |

### Program rows
| Item | programs.csv row / field | Current | Fix |
|---|---|---|---|
| 55 | row 92 (Consumers Energy Co / AC Peak Cycling Program) | REFUTED | incentive_value_usd: '$32/yr + Visa gift card' -> '$5/mo bill credit Jun-Aug (existing participants only)'; source_url -> https://www.consumersenergy.com/residential/rates/electric-rates-and-programs/rate-plan-options/standard-rate-plan/ac-peak-cycling |
| 57 | row 94 (Consumers Energy Co / Distributed Generation Program (Inflow-O) | REFUTED | incentive_value_usd/structure: '6-12c, no T&D credit' -> 'outflow credited at power supply rate incl. transmission (tariff C.11.3); since 2024-02-27 applies to all bill charges'; source_url -> https://www.consumersenergy.com/residential/savings-and-clean-energy/renewable-energy/distributed-generation |
| 80 | row 175 (Northern States Power Co - M / Saver's Switch (Residential)) | REFUTED | incentive_value_usd: CO values ($40 Oct + $100) -> MN terms (15% off Jun-Sep energy charges per MN booklet; re-verify current); source_url -> an MN page |
| 51 | row 35 (Ameren Illinois Company d/b/ / Rider CGR - Customer Generation Rebate () | REFUTED | incentive_value_usd: Res/C&I split wrong -> '$300/kW DG + $300/kWh ESS (non-competitive supply), $250 (competitive/COGF/CRGP); values through 2024-12-31, post-2024 values per ICC'; source_url -> https://www.ameren.com/-/media/rates/files/illinois/aiel59rdcgr.ashx |
| 59 | row 96 (DTE Electric Co / Dynamic Peak Pricing Rate) | INCONCLUSIVE | (probable) incentive_value_usd: 'critical-peak 84.200c total' -> '84.200c critical-peak + 10.800c non-capacity = 95.000c' (card layout ambiguous; business card says 83.565c). Verify against D1.8 tariff sheet |
| 66 | row 103 (DTE Electric Co / CoolCurrents (Interruptible Space Condit) | REFUTED | incentive_value_usd: 7.367/5.237c not on source -> cite DTE tariff sheet or replace with 'up to 29% savings (cooling)' |
| 83 | row 178 (Northern States Power Co - M / Solar*Rewards / Net Metering) | REFUTED | incentive_value_usd: $0.03/kWh not on source -> cite MN Solar*Rewards program/tariff page |
| 86 | row 181 (Northern States Power Co - M / Residential Time-of-Use Rate) | INCONCLUSIVE | source_url (startribune, robots-blocked) -> Xcel MN TOU page; ratio 2.7x/2.2x unverified |
| 81 | row 176 (Northern States Power Co - M / EV Accelerate At Home) | INCONCLUSIVE | source_url JS-only; EVAAH prices unverified -> cite MN tariff sheet |
| 48 | row 32 (Ameren Illinois Company d/b/ / Rider NM - Net Metering) | REFUTED | source_url -> https://www.ameren.com/illinois/residential/supply-choice/renewables/net-metering |
| 49 | row 33 (Ameren Illinois Company d/b/ / Hourly Supply Service (HSS)) | REFUTED | source_url -> Rider HSS tariff sheet; eligibility DS-3+ |
| 97 | row 126 (Lansing Board of Water & Lig / Standard Residential Electric Service (R) | REFUTED | incentive_value_usd: on-peak $0.1740 -> $0.1778/kWh; drop $22.50 BSC or cite a source for it |
| 98 | row 54 (Duke Energy Indiana / EV Off-Peak Charging Credit Pilot) | REFUTED | program_status: Active -> Pilot (2022 launch, 2-yr credit; confirm whether ended); source_url -> utility page |
| 110 | row 238 (WPPI Energy / Power Partner Rewards (formerly Bring Yo) | REFUTED | program_name: 'Power Partner Rewards' unsupported -> 'Bring Your Own Device (BYOD)' unless WPPI page shows the brand; drop 'up to $50 total' |
| 112 | row 81 (Entergy New Orleans LLC / Virtual Power Plant Pilot (EnergyHub-man) | REFUTED | incentive_value_usd: 'up to $600/yr' not in source -> pilot $ unknown; expanded program upfront up to $10,000 res / $100,000 business |
| 108 | row 44 (AES Indiana (formerly IPL) / CoolCents Direct Load Control) | CONFIRMED | source_url (2016 press release) -> https://www.aesindiana.com/coolcentsr-air-conditioning-management |
| 44 | row 28 (Ameren Illinois Company d/b/ / Peak Time Savings (Smart Thermostat)) | CONFIRMED | source_url 302s -> https://greatergrid.com/enroll/programs/thermostats/ameren-il |
| 107 | row 7 (Entergy Arkansas LLC / Non-Legacy Net-Metering Service (NLN-M)) | CONFIRMED | incentive_value_usd: drop 'SPP' (tariff uses MISO LMP only) |

## Notes
- While I was working, a different agent wrote 9 Duke Energy entries (presence and program verdicts citing duke-energy.com) into `audit/results/MISO.json` under MISO indices 12-15, 17-19, 87 and 88. They don't belong to this sample. I overwrote them with my own verdicts and kept a copy in my scratchpad (`foreign_entries.json`). The other region's owner (likely SE) should check that its results file is complete.
- Inconclusive items: 32 (Dahlberg, PSC 403), 81 (Xcel EVAAH, JS-only), 86 (StarTribune, robots).
- NOT_DONE: 0.
