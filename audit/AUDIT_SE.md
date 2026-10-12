# Audit: region SE

Auditor: independent agent, 2026-10-02. Seed: 20261002 (from audit/samples/SE.json). 105 items: 52 presence (20 top-bucket, 32 sample), 53 program rows (38 top, 15 sample). Top territories: FPL, Duke Energy Carolinas, Georgia Power, Duke Energy Florida, Duke Energy Progress.

## Method
Each item checked fresh with WebFetch/WebSearch (no curl, no Wayback, no researcher notes or other audit files). Presence Yes: cited URL opened; if dead/unreadable, one search on the utility's own site for a replacement. Presence No: utility site/tariff checked (and the TVA EnergyRight LPC list or G&T program for TVA distributors/co-ops). Program rows: name, category, $ value and units, status, eligibility, and source_url each checked. Sites that block fetching (duke-energy.com and its p-scapi CDN gave 403; dms.psc.sc.gov is blocked by robots.txt) are INCONCLUSIVE. Results: audit/results/SE.json.

Process note: the shared scratchpad was also being used by another region's auditor. Its helper script overwrote mine and read every b*.json in the scratchpad, so my SE batch files may briefly have been merged into audit/results/MISO.json under the wrong indices. I moved my files to a private folder and rebuilt SE.json from them. **Have someone check MISO.json for SE entries (e.g. Duke Solar Choice idx 61, Thomasville idx 25).**

## Rates vs bars
| Group | Confirmed | Refuted | Inconclusive | Rate incl. inconclusive | Rate excl. inconclusive | Bar |
|---|---|---|---|---|---|---|
| Yes | 23 | 0 | 10 | 69.7% | 100.0% | >=95% confirmed |
| No | 14 | 2 | 3 | 73.7% | 87.5% | >=90% confirmed |
| program | 25 | 16 | 12 | 47.2% | 61.0% | 0 wrong $ in top bucket |

- Presence Yes: 0 refuted. PASS excluding inconclusive (100%). FAIL including them (69.7%): 10 inconclusive, 7 of them Duke pages that are 403 or robots-blocked.
- Presence No: FAIL (87.5% excluding inconclusive, 73.7% including). The 2 refuted are LG&E and KU res_dispatch: both utilities run a BYOT thermostat program that is enrolling now.
- Program rows: 3 wrong $. One is in the top bucket (FPL CILC-1, idx 85), so the 0-wrong-$ bar FAILS. Sample bucket: Lakeland (95) and Alabama Power RTA (96).
- NOT_DONE: 0.

## Item table
| idx | bucket | utility | cell / program | claimed | verdict | evidence URL |
|---|---|---|---|---|---|---|
| 0 | top | Florida Power & Light Company | res_habit | Yes | CONFIRMED | https://www.fpl.com/rates/time-of-use.html |
| 1 | top | Florida Power & Light Company | res_dispatch | Yes | CONFIRMED | https://www.fpl.com/save/programs/on-call-program.html |
| 2 | top | Florida Power & Light Company | ci_habit | Yes | CONFIRMED | https://www.fpl.com/content/dam/fplgp/us/en/rates/pdf/bus-eff-jan-2026.pdf |
| 3 | top | Florida Power & Light Company | ci_dispatch | Yes | CONFIRMED | https://www.fpl.com/business/save/programs/oncall.html |
| 4 | top | Duke Energy Carolinas, LLC | res_habit | Yes | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 5 | top | Duke Energy Carolinas, LLC | res_dispatch | Yes | CONFIRMED | https://duke-energy.com/pmbattery |
| 6 | top | Duke Energy Carolinas, LLC | ci_habit | Yes | INCONCLUSIVE | https://www.duke-energy.com/business/billing/rates?jur=NC01 |
| 7 | top | Duke Energy Carolinas, LLC | ci_dispatch | Yes | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc |
| 8 | top | Georgia Power Company | res_habit | Yes | CONFIRMED | https://www.georgiapower.com/residential/rate-plans/nights-weekends.html |
| 9 | top | Georgia Power Company | res_dispatch | Yes | INCONCLUSIVE | https://georgiapower.com/tempcheck |
| 10 | top | Georgia Power Company | ci_habit | Yes | CONFIRMED | https://www.georgiapower.com/content/dam/georgia-power/pdfs/business-pdfs/tariffs/2025/rtp-da-12.pdf |
| 11 | top | Georgia Power Company | ci_dispatch | Yes | CONFIRMED | https://www.georgiapower.com/content/dam/georgia-power/pdfs/business-pdfs/DRC-1_Tariff.pdf |
| 12 | top | Duke Energy Florida, LLC | res_habit | Yes | INCONCLUSIVE | https://www.duke-energy.com/home/billing/rates/time-of-use |
| 13 | top | Duke Energy Florida, LLC | res_dispatch | Yes | CONFIRMED | https://www.duke-energy.com/home/products/energywise-home/switch |
| 14 | top | Duke Energy Florida, LLC | ci_habit | Yes | INCONCLUSIVE | https://p-scapi.duke-energy.com/-/media/pdfs/for-your-home/rates/rates-fl/gsd-1-01-01-2022-rate-schedule.pdf?la=en |
| 15 | top | Duke Energy Florida, LLC | ci_dispatch | Yes | INCONCLUSIVE | https://www.duke-energy.com/_/media/pdfs/for-your-home/bill-inserts-2020/06june/201326-fl-all-non-res-rate-update-june-2020.pdf?la=en |
| 16 | top | Duke Energy Progress, LLC | res_habit | Yes | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 17 | top | Duke Energy Progress, LLC | res_dispatch | Yes | CONFIRMED | https://www.duke-energy.com/home/products/energywise-home/smart-thermostat |
| 18 | top | Duke Energy Progress, LLC | ci_habit | Yes | INCONCLUSIVE | https://news.duke-energy.com/releases/new-duke-energy-program-helps-south-carolina-nonresidential-customers-lower-costs-while-supporting-a-growing-grid |
| 19 | top | Duke Energy Progress, LLC | ci_dispatch | Yes | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc |
| 20 | sample | Tri-State EMC | ci_habit | No | INCONCLUSIVE | https://www.tsemc.net/ |
| 21 | sample | Hart EMC | res_dispatch | No | CONFIRMED | https://www.hartemc.com/summer-energy-savings/ |
| 22 | sample | Upper Cumberland Electric Membership Cor | res_dispatch | No | CONFIRMED | https://www.ucemc.com/let-s-beat-the-heat-together/ |
| 23 | sample | Florida Public Utilities Company | res_habit | No | CONFIRMED | https://fpuc.com/wp-content/uploads/FPU-Electric-Tariff-eff.-03-20-2025_ADA_.pdf |
| 24 | sample | Louisville Gas & Electric | res_dispatch | No | REFUTED | https://lge-ku.com/demand-conservation |
| 25 | sample | Thomasville Utilities (Electric) | res_dispatch | No | CONFIRMED | https://thomasville.org/departments/utilities/electric |
| 26 | sample | Albany Utilities | ci_dispatch | No | CONFIRMED | https://www.albanyga.gov/City-Services/Utilities/Commercial-Rates |
| 27 | sample | Gainesville Regional Utilities | res_dispatch | No | CONFIRMED | https://www.gru.com/My-Home/Lower-My-Bill/Save-Energy |
| 28 | sample | Edisto Electric Cooperative | res_dispatch | Yes | CONFIRMED | https://energysmartsc.org/smart-thermostat/ |
| 29 | sample | Four County Electric Membership Corporat | res_dispatch | Yes | INCONCLUSIVE | https://connecttosavenc.com/coop/fcemc |
| 30 | sample | Middle Tennessee Electric | res_habit | Yes | CONFIRMED | https://mte.com/NiteFlex |
| 31 | sample | Santee Cooper (South Carolina Public Ser | res_habit | Yes | CONFIRMED | https://www.santeecooper.com/rates/ |
| 32 | sample | Tampa Electric Company | res_dispatch | Yes | CONFIRMED | https://www.tampaelectric.com/residential/saveenergy/energyplanner/ |
| 33 | sample | Shelbyville Power System | ci_dispatch | Yes | CONFIRMED | https://energyright.com/business-industry/demand-response/powerflex/ |
| 34 | sample | City of Wilson Electric Utility (Wilson  | ci_dispatch | Yes | CONFIRMED | https://www.wilsonnc.org/residents/all-departments/wilson-energy/electric/electric-rates |
| 35 | sample | Nashville Electric Service | res_dispatch | Yes | CONFIRMED | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 36 | sample | Plateau Electric Cooperative | res_dispatch | No | CONFIRMED | https://plateauelectric.com/service/energy-efficiency/ |
| 37 | sample | Tallahatchie Valley Electric Power Assoc | res_habit | No | INCONCLUSIVE | https://www.tvepa.com/ |
| 38 | sample | Tombigbee Electric Power Association | res_dispatch | No | CONFIRMED | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 39 | sample | Florida Public Utilities Company | ci_habit | No | CONFIRMED | https://fpuc.com/wp-content/uploads/FPU-Electric-Tariff-eff.-03-20-2025_ADA_.pdf |
| 40 | sample | Kentucky Utilities | res_dispatch | No | REFUTED | https://lge-ku.com/demand-conservation |
| 41 | sample | Cookeville Electric Department | res_dispatch | No | CONFIRMED | https://www.cookeville-tn.gov/209/Energy-Right-Program |
| 42 | sample | City of Concord Electric Systems | ci_dispatch | No | CONFIRMED | https://concordnc.gov/Departments/Electric-Systems/Rate-Schedules |
| 43 | sample | Lakeland Electric | res_dispatch | No | CONFIRMED | https://lakelandelectric.com/billing-and-payment/pricing-plans |
| 44 | sample | Marshall-DeKalb Electric Cooperative | res_dispatch | Yes | CONFIRMED | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 45 | sample | Tallahatchie Valley Electric Power Assoc | ci_dispatch | Yes | CONFIRMED | https://energyright.com/business-industry/demand-response/powerflex/ |
| 46 | sample | Blue Ridge Electric Cooperative | res_dispatch | Yes | CONFIRMED | https://energysmartsc.org/smart-thermostat/ |
| 47 | sample | Santee Cooper (South Carolina Public Ser | res_dispatch | Yes | CONFIRMED | https://newsroom.santeecooper.com/news/Santee-Cooper-Announces-Rewards-for-Smart-Thermostat-Customers/ |
| 48 | sample | Louisville Gas & Electric | ci_habit | Yes | INCONCLUSIVE | https://lge-ku.com/peak-time-rebates |
| 49 | sample | Rayle EMC | ci_dispatch | No | CONFIRMED | https://www.rayleemc.com/ |
| 50 | sample | Okefenoke REMC | ci_habit | No | INCONCLUSIVE | https://www.oremc.com/rates |
| 51 | sample | Jones-Onslow EMC | res_dispatch | No | CONFIRMED | https://connecttosavenc.com/coop/joemc |
| 52 | top | Duke Energy Carolinas, LLC | PowerPair | $0.36/W solar (max 10kW-AC; $3,600 cap) + $400/kWh battery ( | CONFIRMED | https://www.duke-energy.com/partner-with-us/trade-allies/residential/powerpair |
| 53 | top | Duke Energy Carolinas, LLC | Power Manager Battery Control | $6.50/kW x capability factor (~70.9%) monthly credit | INCONCLUSIVE | https://duke-energy.com/pmbattery |
| 54 | top | Duke Energy Carolinas, LLC | Residential Solar Choice (Rider RSC) | n/a | REFUTED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 55 | top | Duke Energy Carolinas, LLC | Net Metering Bridge Rate (Rider NMB) | n/a | REFUTED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 56 | top | Duke Energy Carolinas, LLC | Residential TOU with Critical Peak Pricing (R-TOU-CPP / Flex | n/a | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 57 | top | Duke Energy Carolinas, LLC | Residential Time-of-Use (R-TOU) | n/a | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 58 | top | Duke Energy Carolinas, LLC | Power Manager (AC/heat pump switch) | up to $150 upfront + $50/yr depending on devices enrolled | CONFIRMED | https://news.duke-energy.com/releases/new-year-bigger-incentives-as-temperatures-fall-in-the-carolinas-duke-energy-increases-financial-incentives-for-customer-energy-efficiency-and-demand-response-programs |
| 59 | top | Duke Energy Carolinas, LLC | Power Manager Smart Thermostat (BYOT) | $150 one-time enrollment credit | INCONCLUSIVE | https://www.duke-energy.com/home/products/power-manager/smart-thermostat |
| 60 | top | Duke Energy Carolinas, LLC | PowerShare (Rider PS) | $3.50-$5.00/kW-month capacity credit + $0.10/kWh curtailment | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc |
| 61 | top | Duke Energy Carolinas, LLC | Solar Choice Metering Tariff | n/a | CONFIRMED | https://ors.sc.gov/sites/scors/files/Documents/Consumers/Solar/ORS%20Duke%20Solar%20Choice%20Overview.pdf |
| 62 | top | Duke Energy Carolinas, LLC | PowerShare Nonresidential Load Curtailment Rider | capacity credit increased toward $5/kW-month per 2025-26 fil | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc |
| 63 | top | Duke Energy Progress, LLC | PowerPair | $0.36/W solar (max 10kW-AC; $3,600 cap) + $400/kWh battery ( | INCONCLUSIVE | https://www.duke-energy.com/partner-with-us/trade-allies/residential/powerpair |
| 64 | top | Duke Energy Progress, LLC | Residential Time-of-Use (R-TOU) | n/a | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 65 | top | Duke Energy Progress, LLC | Residential TOU with Critical Peak Pricing (R-TOU-CPP / Flex | n/a | CONFIRMED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 66 | top | Duke Energy Progress, LLC | Residential Solar Choice (Rider RSC) | n/a | REFUTED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 67 | top | Duke Energy Progress, LLC | Net Metering Bridge Rate (Rider NMB) | n/a | REFUTED | https://www.duke-energy.com/home/billing/rates/new-rates-nc |
| 68 | top | Duke Energy Progress, LLC | EnergyWise Home Smart Thermostat (BYOT) | $150 one-time enrollment credit + $50/yr renewal | INCONCLUSIVE | https://www.duke-energy.com/home/products/energywise-home/smart-thermostat |
| 69 | top | Duke Energy Progress, LLC | EnergyWise Home Switch (AC/heat pump control) | see current program incentive schedule | CONFIRMED | https://www.duke-energy.com/Home/Products/EnergyWise-Home/Switch |
| 70 | top | Duke Energy Progress, LLC | PowerShare (Rider PS) | $3.50-$5.00/kW-month capacity credit + $0.10/kWh curtailment | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc |
| 71 | top | Duke Energy Progress, LLC | Solar Choice Metering Tariff | n/a | INCONCLUSIVE | https://dms.psc.sc.gov/Attachments/Matter/27add76f-6553-4c71-a2ae-4b05c86d8e7e |
| 72 | top | Duke Energy Progress, LLC | New nonresidential demand-side program (2026 SC filing) | n/a | REFUTED | https://news.duke-energy.com/releases/new-duke-energy-program-helps-south-carolina-nonresidential-customers-lower-costs-while-supporting-a-growing-grid |
| 73 | top | Georgia Power Company | Nights & Weekends | On-peak $0.303/kWh; Off-peak $0.078/kWh | CONFIRMED | https://www.georgiapower.com/residential/rate-plans/nights-weekends.html |
| 74 | top | Georgia Power Company | Smart Usage | On-peak $0.146/kWh; Off-peak $0.016/kWh; Demand $12.44/kW-mo | CONFIRMED | https://www.georgiapower.com/residential/rate-plans/smart-usage.html |
| 75 | top | Georgia Power Company | Thermostat Energy Management Program (TEMP√ / Smart Thermost | $50 enrollment bonus (thermostat credit) | INCONCLUSIVE | https://georgiapower.com/tempcheck |
| 76 | top | Georgia Power Company | Resiliency Asset Service (RAS-1) + DER Demand Response Credi | not published in $/kW; credit = 100% of capacity value (util | REFUTED | https://www.georgiapower.com/content/dam/georgia-power/pdfs/business-pdfs/DRC-1_Tariff.pdf |
| 77 | top | Georgia Power Company | Customer-Sited Solar Plus Storage Pilot | Customer-directed: $15/kW upfront + $1.50/kWh discharged (LM | REFUTED | https://mgrid.org/?p=4825 |
| 78 | top | Georgia Power Company | RNR - Monthly Netting (legacy Net Metering Pilot) | n/a | CONFIRMED | https://www.georgiapower.com/content/dam/georgia-power/pdfs/residential-pdfs/residential-rate-plans/RNR-11.pdf |
| 79 | top | Georgia Power Company | RNR - Instantaneous Netting | avoided cost ~$0.027/kWh + $0.04/kWh adder = ~$0.067/kWh tot | CONFIRMED | https://www.georgiapower.com/content/dam/georgia-power/pdfs/residential-pdfs/residential-rate-plans/RNR-11.pdf |
| 80 | top | Florida Power & Light Company | FPL On Call (Residential) | $6/mo (1-2 A/C units Apr-Oct); $2.75/mo (elec heat Nov-Mar); | CONFIRMED | https://www.fpl.com/save/programs/on-call-program.html |
| 81 | top | Florida Power & Light Company | FPL On Call (Business) | $2/ton/month, Apr-Oct (7 months); e.g. 2x5-ton units = $140/ | CONFIRMED | https://www.fpl.com/business/save/programs/oncall.html |
| 82 | top | Florida Power & Light Company | Residential Time of Use Rate (RTR-1) |  | CONFIRMED | https://www.fpl.com/rates/time-of-use.html |
| 83 | top | Florida Power & Light Company | Net Metering (COG-1) |  | CONFIRMED | https://www.fpl.com/content/dam/fplgp/us/en/rates/pdf/electric-tariff-section10.pdf |
| 84 | top | Florida Power & Light Company | FPL EVolution Home | $36/mo full install or $27/mo equipment-only, plus off-peak  | CONFIRMED | https://www.fpl.com/electric-vehicles/for-drivers/evolution-home.html |
| 85 | top | Florida Power & Light Company | Commercial/Industrial Load Control (CILC-1) | base demand $5.67/kW credit; curtailment penalty $14.17/kW ( | REFUTED (wrong $) | https://www.fpl.com/content/dam/fplgp/us/en/rates/pdf/bus-eff-jan-2026.pdf |
| 86 | top | Duke Energy Florida, LLC | EnergyWise Home (Switch) | up to $141/yr | INCONCLUSIVE | https://www.duke-energy.com/home/products/energywise-home/switch |
| 87 | top | Duke Energy Florida, LLC | EnergyWise Home Battery Control |  | INCONCLUSIVE | https://www.duke-energy.com/home/products/energywise-home/battery-control |
| 88 | top | Duke Energy Florida, LLC | Residential Time-of-Use Rate | ~10c-20c/kWh depending on time of day (approx.) | INCONCLUSIVE | https://www.duke-energy.com/home/billing/rates/time-of-use |
| 89 | top | Duke Energy Florida, LLC | Net Metering (Rider RE) |  | CONFIRMED | https://www.energysage.com/local-data/net-metering/duke-energy/ |
| 90 | sample | Tampa Electric Company | Energy Planner (Residential TOU) | off-peak as low as 11.044c/kWh vs standard 14.235c/kWh | CONFIRMED | https://www.tampaelectric.com/residential/saveenergy/energyplanner/ |
| 91 | sample | Tennessee Valley Authority | PowerFlex | Not published; replaces Interruptible Power (IP5/IP30); high | CONFIRMED | https://energyright.com/business-industry/demand-response/powerflex/ |
| 92 | sample | Tennessee Valley Authority | Green Connect | N/A - facilitation program, not a PPA rate | CONFIRMED | https://www.tva.com/energy/valley-renewable-energy/green-connect |
| 93 | sample | GreyStone Power Corporation | General Service Seasonal Off-Peak (Rate 72, Schedule GS-SOFF | rate values not published in sources reviewed | REFUTED | https://www.greystonepower.com/sites/default/files/PDF/Rates/010522/General%20Service%20Seasonal%20Off%20Peak.pdf |
| 94 | sample | Middle Tennessee Electric | EV Ready (Level 2 charger install credit) | $50 bill credit | CONFIRMED | https://mte.com/EVReady |
| 95 | sample | Lakeland Electric | Demand Price Plan | Demand charge $6.69/kW (or $5.77/kW with Value of Solar Cred | REFUTED (wrong $) | https://lakelandelectric.com/billing-and-payment/pricing-plans |
| 96 | sample | Alabama Power Company | Residential Time Advantage (Rate RTA) | Summer/winter peak $0.302554/kWh; off-peak (economy) $0.1025 | REFUTED (wrong $) | https://www.alabamapower.com/content/dam/alabama-power/pdfs-docs/Rates/RTA.pdf |
| 97 | sample | EnergyUnited | Net Metering (Residential & Non-Residential) | credited at avoided cost rate; specific $/kWh not published  | REFUTED | https://www.energyunited.com/wp-content/uploads/2021/05/EU-Rate-Schedules_02012021_Net-Metering-Commercial.pdf |
| 98 | sample | Tennessee Valley Authority | Wholesale Time-of-Use Rate Structure (GSA/GSB/GSC/GSD, MSB/M | Not published in $/kWh here; varies by rate schedule and sea | REFUTED | https://www.tva.com/about-tva/tva-rates |
| 99 | sample | Kentucky Utilities | Optimized (Managed) EV Charging | $25 enrollment + $5/month while enrolled | CONFIRMED | https://greatergrid.com/enroll/programs/evs/lge-ku-ev/faq |
| 100 | sample | Dominion Energy South Carolina | Solar Choice Metering Tariff (Rider to Rate 5) | n/a | CONFIRMED | https://ors.sc.gov/sites/scors/files/Documents/Consumers/Solar/ORS%20Dominion%20Solar%20Choice%20Overview.pdf |
| 101 | sample | Orlando Utilities Commission | PeakSHIFT Plan (DemandLevel + Shift & Save) | DemandLevel fixed charges of $5, $10 or $15/mo based on mont | REFUTED | https://www.ouc.com/about/news/ouc-approve-peakshift-plan/ |
| 102 | sample | Clay Electric Cooperative, Inc. | Net Metering (avoided-cost buyback, QF-1) |  | REFUTED | https://www.clayelectric.com/rates |
| 103 | sample | Orlando Utilities Commission | Battery Storage Rebate | up to $2,000 one-time rebate (2019 pilot, first 50 customers | REFUTED | https://www.ouc.com/solutions-programs/savings/rebates/battery-storage/ |
| 104 | sample | Louisville Gas & Electric | Residential Time of Day - Demand Rate | Energy $0.06292/kWh; Base demand $4.32/kW; Peak demand $9.46 | CONFIRMED | https://lge-ku.com/residential/billing/time-of-day-rates |

## Defect list (proposed fixes)
Presence file: data/raw/presence_scan (scan CSV row = eia_id). Programs: programs.csv row number as given in the sample.

- **idx 14** [INCONCLUSIVE] Duke Energy Florida, LLC | presence eia_id=6455 cell=ci_habit: 403. Also GSD-1 (plain demand) would not qualify; 2022 sheet likely stale. Cite GSDT-1. **Fix:** replace source_url with a page/tariff that shows the claim. Evidence: https://p-scapi.duke-energy.com/-/media/pdfs/for-your-home/rates/rates-fl/gsd-1-01-01-2022-rate-schedule.pdf?la=en
- **idx 15** [INCONCLUSIVE] Duke Energy Florida, LLC | presence eia_id=6455 cell=ci_dispatch: 403; 2020 bill insert is a weak/stale source; cite IS-2/CS-2 tariff. **Fix:** replace source_url with a page/tariff that shows the claim. Evidence: https://www.duke-energy.com/_/media/pdfs/for-your-home/bill-inserts-2020/06june/201326-fl-all-non-res-rate-update-june-2020.pdf?la=en
- **idx 18** [INCONCLUSIVE] Duke Energy Progress, LLC | presence eia_id=3046 cell=ci_habit: Cited release is PowerShare Storage for DUKE ENERGY CAROLINAS SC, a DR program, not DEP C&I TOU. DEP LGS-RTP exists per search but PDF 403. **Fix:** replace source_url with a page/tariff that shows the claim. Evidence: https://news.duke-energy.com/releases/new-duke-energy-program-helps-south-carolina-nonresidential-customers-lower-costs-while-supporting-a-growing-grid
- **idx 24** [REFUTED] Louisville Gas & Electric | presence eia_id=11249 cell=res_dispatch: LG&E/KU BYOT currently enrolling; legacy Demand Conservation closed to new. **Fix:** Yes: BYOT smart thermostat program (enrolling) and Optimized EV Charging (managed via vehicle telematics). Evidence: https://lge-ku.com/demand-conservation
- **idx 40** [REFUTED] Kentucky Utilities | presence eia_id=10171 cell=res_dispatch: Same joint LG&E/KU BYOT; KU's own program row 418 (Optimized EV Charging) is a utility-controlled device program. **Fix:** Yes: BYOT smart thermostat program (enrolling) and Optimized EV Charging. Evidence: https://lge-ku.com/demand-conservation
- **idx 54** [REFUTED] Duke Energy Carolinas, LLC | programs.csv row 671 (Residential Solar Choice (Rider RSC)): Source page does not mention Rider RSC; program real but cited URL doesn't show it (row tagged Unverified). **Fix:** source_url should be Rider RSC tariff/Duke solar page. Evidence: https://www.duke-energy.com/home/billing/rates/new-rates-nc
- **idx 55** [REFUTED] Duke Energy Carolinas, LLC | programs.csv row 672 (Net Metering Bridge Rate (Rider NMB)): Source page does not mention Rider NMB or ~$0.11 flat rate/Jan 2027 deadline; unverifiable at cited URL. **Fix:** source_url should be Rider NMB tariff. Evidence: https://www.duke-energy.com/home/billing/rates/new-rates-nc
- **idx 60** [INCONCLUSIVE] Duke Energy Carolinas, LLC | programs.csv row 677 (PowerShare (Rider PS)): robots-blocked. NC row cites SC docket. $3.50/kW-mo + $0.10/kWh matches SC PowerShare Storage release, not verifiable for NC Rider PS. **Fix:** replace source_url with a page/tariff that shows the claim. Evidence: https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc
- **idx 66** [REFUTED] Duke Energy Progress, LLC | programs.csv row 683 (Residential Solar Choice (Rider RSC)): Cited page does not mention Rider RSC. **Fix:** source_url should be Rider RSC tariff. Evidence: https://www.duke-energy.com/home/billing/rates/new-rates-nc
- **idx 67** [REFUTED] Duke Energy Progress, LLC | programs.csv row 684 (Net Metering Bridge Rate (Rider NMB)): Cited page does not mention Rider NMB. **Fix:** source_url should be Rider NMB tariff. Evidence: https://www.duke-energy.com/home/billing/rates/new-rates-nc
- **idx 70** [INCONCLUSIVE] Duke Energy Progress, LLC | programs.csv row 687 (PowerShare (Rider PS)): robots-blocked; DEP NC row cites SC docket. **Fix:** replace source_url with a page/tariff that shows the claim. Evidence: https://dms.psc.sc.gov/Attachments/Matter/c60eaa90-4800-42dc-bf87-2f844a42c5cc
- **idx 72** [REFUTED] Duke Energy Progress, LLC | programs.csv row 689 (New nonresidential demand-side program (2026 SC filing)): Row is a placeholder misattributed to DEP; name, category, $, status all wrong. **Fix:** name: PowerShare Storage; utility: Duke Energy Carolinas (SC); category: DR-BYOD/DR-Curtailment; $120/kW one-time (+$30/kW renewable-charged) + $3.50/kW-mo + $0.10/kWh; status: approved 5/27/2026, operating Aug 2026. Evidence: https://news.duke-energy.com/releases/new-duke-energy-program-helps-south-carolina-nonresidential-customers-lower-costs-while-supporting-a-growing-grid
- **idx 76** [REFUTED] Georgia Power Company | programs.csv row 693 (Resiliency Asset Service (RAS-1) + DER Demand Response Credit (DRC-1)): Min 200 kW/premise, 1,000 kW aggregate, pilot: OK. '100% of capacity value' not in tariff; DR-BYOD category wrong for company-installed DER. **Fix:** Credit Value = levelized value of demand reduction from Company capacity price forecast (not stated as 100%); DER is Company-installed (not BYOD). Evidence: https://www.georgiapower.com/content/dam/georgia-power/pdfs/business-pdfs/DRC-1_Tariff.pdf
- **idx 77** [REFUTED] Georgia Power Company | programs.csv row 694 (Customer-Sited Solar Plus Storage Pilot): $ values match secondary report ($15/kW+$1.50/kWh, $45 LMI; $750/$1,000/kW). Cited PSC doc is a GSEA BYOD brief that shows none of it. **Fix:** status: approved by GA PSC Jul 2025 (Pilot); source_url should be approval/GP page. Evidence: https://mgrid.org/?p=4825
- **idx 85** [REFUTED, WRONG $] Florida Power & Light Company | programs.csv row 722 (Commercial/Industrial Load Control (CILC-1)): $5.67 is a max-demand CHARGE not a credit; $14.17 is firm on-peak demand charge not curtailment penalty. Name/category/status OK. **Fix:** Max demand charge $5.67/kW; firm on-peak demand $14.17/kW; load-control on-peak demand $3.73/kW (CILC-1(G), eff Jan 2026). Incentive = firm minus LC on-peak.. Evidence: https://www.fpl.com/content/dam/fplgp/us/en/rates/pdf/bus-eff-jan-2026.pdf
- **idx 93** [REFUTED] GreyStone Power Corporation | programs.csv row 712 (General Service Seasonal Off-Peak (Rate 72, Schedule GS-SOFF)): Not a time-of-day rate; 'off-peak' = Nov-May months. Row says values unpublished. **Fix:** category: seasonal-use rate (>=80% kWh in <=4 consecutive months), not TOU; rates ARE published: $17/mo + $0.085/$0.040/$0.035/$0.030 per kWh by kWh/kW tier; eff 6/1/2021. Evidence: https://www.greystonepower.com/sites/default/files/PDF/Rates/010522/General%20Service%20Seasonal%20Off%20Peak.pdf
- **idx 95** [REFUTED, WRONG $] Lakeland Electric | programs.csv row 736 (Demand Price Plan): Row has superseded 6/1/2026 values. Windows/holidays match. **Fix:** Eff 10/1/2026: demand $7.05/kW ($6.08 w/ Value of Solar); energy $0.02819/kWh; fuel $0.0470/kWh; customer $15.25. Evidence: https://lakelandelectric.com/billing-and-payment/pricing-plans
- **idx 96** [REFUTED, WRONG $] Alabama Power Company | programs.csv row 697 (Residential Time Advantage (Rate RTA)): 30.2554/10.2554 appear nowhere on cited sheet; winter peak is not equal to summer peak. **Fix:** Summer peak 25.0728c, winter peak 12.0728c, economy 10.0728c/kWh (June 2023 adj. on cited sheet); summer Jun-Sep 1-7pm CT, winter Nov-Mar 5-9am CT. Evidence: https://www.alabamapower.com/content/dam/alabama-power/pdfs-docs/Rates/RTA.pdf
- **idx 97** [REFUTED] EnergyUnited | programs.csv row 714 (Net Metering (Residential & Non-Residential)): Cited doc is commercial rider only; row claims residential too and omits Option A. **Fix:** segment: Non-Residential only; pilot max 10 customers; Option A retail credit + $3/kW standby, Option B avoided cost (Sched AC) no standby. Evidence: https://www.energyunited.com/wp-content/uploads/2021/05/EU-Rate-Schedules_02012021_Net-Metering-Commercial.pdf
- **idx 98** [REFUTED] Tennessee Valley Authority | programs.csv row 753 (Wholesale Time-of-Use Rate Structure (GSA/GSB/GSC/GSD, MSB/MSC/MSD)): Cited page shows none of the claimed schedules/TOU structure; no $ claimed. **Fix:** source_url should be TVA wholesale rate schedule document. Evidence: https://www.tva.com/about-tva/tva-rates
- **idx 101** [REFUTED] Orlando Utilities Commission | programs.csv row 734 (PeakSHIFT Plan (DemandLevel + Shift & Save)): $5/$10/$15 tiers correct; Proposed/pending is wrong. **Fix:** status: Active (approved 12/11/2024; DemandLevel effective Mar 2026); Shift & Save default opt-out from Jan 2027. Evidence: https://www.ouc.com/about/news/ouc-approve-peakshift-plan/
- **idx 102** [REFUTED] Clay Electric Cooperative, Inc. | programs.csv row 747 (Net Metering (avoided-cost buyback, QF-1)): Cited rates page and solar page show no QF-1 crediting or 100 kW cap; claims unverifiable at source. **Fix:** source_url should be Clay rate book/net-metering tariff. Evidence: https://www.clayelectric.com/rates
- **idx 103** [REFUTED] Orlando Utilities Commission | programs.csv row 733 (Battery Storage Rebate): '2019 pilot, first 50 customers, under evaluation' is stale; segment wrong. $2,000 cap correct. **Fix:** $150/kWh of storage, max $2,000; residential AND commercial interconnected solar customers; open; exports at community solar farm rate to 6/30/2030 then retail fuel rate. Evidence: https://www.ouc.com/solutions-programs/savings/rebates/battery-storage/

## Inconclusive (re-check by hand in a browser)
Duke (duke-energy.com 403 / dms.psc.sc.gov robots): idx 6, 7, 12, 14, 15, 18, 19, 53, 59, 60, 62, 63, 68, 70, 71, 86, 87, 88. Georgia Power TEMP thermostat (JS-only): 9, 75. Four County EMC Connect to Save (enrollment paused): 29. LG&E business TOD page unreadable: 48. Tri-State EMC no rate pages: 20. Tallahatchie Valley site cert error: 37. Okefenoke REMC rates page lists no schedules: 50.
