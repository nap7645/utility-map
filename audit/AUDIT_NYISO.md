# NYISO audit (independent)

Date: 2026-10-02. Sample: `audit/samples/NYISO.json`, seed **20261002**, 113 items (40 presence, 73 program rows). Top-bucket territories: Con Edison, National Grid NY, LIPA/PSEG-LI, NYSEG, RG&E (100% of their sampled cells and rows).

## Method
Each item checked against the live cited page with WebFetch (no Wayback, no researcher notes, no other audit files). Presence Yes: confirmed only if the page shows that program type for that segment, currently offered; if the cited page did not show it, one replacement search on the utility's own site was done and the cell confirmed from the replacement (logged as a source defect). Presence No: utility business/residential rate and DR pages searched. Program rows: name, category, $ value/units, status, source checked against current documents (effective dates noted).

**Limitation:** the WebFetch weekly quota was exhausted after all top-bucket items were done. 32 sample-bucket items are NOT_DONE and 2 are INCONCLUSIVE for that reason. Top-bucket coverage is complete (78/78).

## Counts

| Group | CONFIRMED | REFUTED | INCONCLUSIVE | NOT_DONE |
|---|---|---|---|---|
| Yes | 19 | 0 | 2 | 6 |
| No | 0 | 1 | 0 | 12 |
| program | 55 | 4 | 0 | 14 |

## Rates vs bars

| Bar | Excl. inconclusive | Incl. inconclusive | Pass? |
|---|---|---|---|
| Yes confirmed >=95% | 19/19 = 100.0% | 19/21 = 90.5% | PASS (on checked items) |
| No confirmed >=90% | 0/1 = 0.0% | 0/1 = 0.0% | FAIL (1 of 1 checked No refuted; 9 sample No items NOT_DONE) |
| Program rows all fields correct | 55/59 = 93.2% | 55/59 = 93.2% | 4 rows refuted |
| 0 wrong $ in top bucket | 2 wrong | | FAIL |

Region cannot pass until the 34 NOT_DONE/INCONCLUSIVE sample items are checked and defects below are fixed and re-verified.

## Item table

| # | Bucket | Utility | Cell / program | Claimed | Verdict | $wrong | Evidence URL |
|---|---|---|---|---|---|---|---|
| 0 | top | Consolidated Edison Co of New York  | res_habit | Yes | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/standby-rates |
| 1 | top | Consolidated Edison Co of New York  | res_dispatch | Yes | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-residential-customers/bring-your-thermostat-and-get-85 |
| 2 | top | Consolidated Edison Co of New York  | ci_habit | Yes | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/standby-rates |
| 3 | top | Consolidated Edison Co of New York  | ci_dispatch | Yes | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-commercial-industrial-buildings-customers/smart-usage-rewards |
| 4 | top | Niagara Mohawk Power Corp (National | res_habit | Yes | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Home/Voluntary-Time-of-Use-Rate/Voluntary-Time-of-Use-Rate |
| 5 | top | Niagara Mohawk Power Corp (National | res_dispatch | Yes | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Home/ConnectedSolutions/BatteryProgram |
| 6 | top | Niagara Mohawk Power Corp (National | ci_habit | No | REFUTED |  | https://www.nationalgridus.com/Upstate-NY-Business/Rates/Service-Rates |
| 7 | top | Niagara Mohawk Power Corp (National | ci_dispatch | Yes | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response |
| 8 | top | Long Island Power Authority / PSEG  | res_habit | Yes | CONFIRMED |  | https://www.psegliny.com/timeofday |
| 9 | top | Long Island Power Authority / PSEG  | res_dispatch | Yes | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers |
| 10 | top | Long Island Power Authority / PSEG  | ci_habit | Yes | CONFIRMED |  | https://www.lipower.org/wp-content/uploads/2025/12/6.-Consideration-of-Approval-of-Tariff-Changes.pdf |
| 11 | top | Long Island Power Authority / PSEG  | ci_dispatch | Yes | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/csrp/faq |
| 12 | top | New York State Electric & Gas Corp  | res_habit | Yes | CONFIRMED |  | https://www.nyseg.com/account/understandyourbill/electricpricing/time-of-use-service-rate |
| 13 | top | New York State Electric & Gas Corp  | res_dispatch | Yes | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 14 | top | New York State Electric & Gas Corp  | ci_habit | Yes | CONFIRMED |  | https://www.nyseg.com/smartenergy/understandyourusage/hourlypricingcommercial |
| 15 | top | New York State Electric & Gas Corp  | ci_dispatch | Yes | CONFIRMED |  | https://www.nyseg.com/smartenergy/businesssolutions/cidemandresponse/commercial-system-relief-program |
| 16 | top | Rochester Gas & Electric Corp (RG&E | res_habit | Yes | CONFIRMED |  | https://www.rge.com/account/understandyourbill/pricing/time-of-use-rates |
| 17 | top | Rochester Gas & Electric Corp (RG&E | res_dispatch | Yes | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 18 | top | Rochester Gas & Electric Corp (RG&E | ci_habit | Yes | CONFIRMED |  | https://www.rge.com/smartenergy/understandyourusage/hourly-pricing |
| 19 | top | Rochester Gas & Electric Corp (RG&E | ci_dispatch | Yes | CONFIRMED |  | https://www.rge.com/smartenergy/businesssolutions/cidr/commercial-system-relief-program |
| 20 | sample | Fairport Electric (Fairport Municip | res_habit | No | NOT_DONE |  | https://cms9files.revize.com/fairport/electric/Billing/12-1-25%20Billing%20Sheet.pdf |
| 21 | sample | Jamestown Board of Public Utilities | res_habit | No | NOT_DONE |  | https://www.jamestownnybpu.gov/156/Electric |
| 22 | sample | Central Hudson Gas & Electric Corp | ci_habit | Yes | NOT_DONE |  | https://www.cenhud.com/globalassets/pdf/forms/tou-application.pdf |
| 23 | sample | Rockville Centre Electric Departmen | res_dispatch | Yes | NOT_DONE |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BE0A68098-0000-C75A-A009-5F980FA12D2E%7D |
| 24 | sample | Jamestown Board of Public Utilities | ci_dispatch | Yes | NOT_DONE |  | https://www.publicpower.org/periodical/article/new-general-manager-jamestown-board-public-utilities-details-open-access-fiber-network-project-flex |
| 25 | sample | Freeport Electric (Village of Freep | ci_dispatch | No | NOT_DONE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 26 | sample | Jamestown Board of Public Utilities | ci_habit | No | NOT_DONE |  | https://www.jamestownnybpu.gov/156/Electric |
| 27 | sample | Orange & Rockland Utilities Inc (O& | ci_dispatch | Yes | INCONCLUSIVE |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 28 | sample | Rockville Centre Electric Departmen | ci_dispatch | Yes | NOT_DONE |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BE0A68098-0000-C75A-A009-5F980FA12D2E%7D |
| 29 | sample | Freeport Electric (Village of Freep | res_habit | No | NOT_DONE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 30 | sample | Jamestown Board of Public Utilities | res_dispatch | No | NOT_DONE |  | https://www.jamestownnybpu.gov/351/Reliable-Power |
| 31 | sample | Central Hudson Gas & Electric Corp | res_dispatch | Yes | INCONCLUSIVE |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 32 | sample | Fairport Electric (Fairport Municip | ci_habit | No | NOT_DONE |  | https://cms9files.revize.com/fairport/electric/Billing/12-1-25%20Billing%20Sheet.pdf |
| 33 | sample | Central Hudson Gas & Electric Corp | res_habit | Yes | NOT_DONE |  | https://www.cenhud.com/en/my-energy/my-energy-options/time-of-use-billing/ev-time-of-use-rate/ |
| 34 | sample | Plattsburgh Municipal Lighting Depa | ci_dispatch | No | NOT_DONE |  | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 35 | sample | Orange & Rockland Utilities Inc (O& | res_habit | Yes | NOT_DONE |  | https://www.oru.com/en/accounts-billing/your-bill/time-of-use |
| 36 | sample | Freeport Electric (Village of Freep | ci_habit | No | NOT_DONE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 37 | sample | Rockville Centre Electric Departmen | res_habit | No | NOT_DONE |  | https://www.rvcny.gov/electric-department/pages/electric-rates |
| 38 | sample | Plattsburgh Municipal Lighting Depa | ci_habit | No | NOT_DONE |  | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 39 | sample | Rockville Centre Electric Departmen | ci_habit | No | NOT_DONE |  | https://www.rvcny.gov/electric-department/pages/electric-rates |
| 40 | top | Consolidated Edison Co of New York  | Commercial System Relief Program (CSRP) - Smart Usage Reward | Active | CONFIRMED |  | https://www.coned.com/-/media/files/coned/documents/save-energy-money/rebates-incentives-tax-credits/smart-usage-rewards/smart-usage-program-example.pdf |
| 41 | top | Consolidated Edison Co of New York  | Distribution Load Relief Program (DLRP) - Smart Usage Reward | Active | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-commercial-industrial-buildings-customers/smart-usage-rewards |
| 42 | top | Consolidated Edison Co of New York  | Term Dynamic Load Management (TERM-DLM) | Active | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-commercial-industrial-buildings-customers/smart-usage-rewards |
| 43 | top | Consolidated Edison Co of New York  | Auto Dynamic Load Management (AUTO-DLM) | Active | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-commercial-industrial-buildings-customers/smart-usage-rewards |
| 44 | top | Consolidated Edison Co of New York  | Standby Service Rates (SC 5 Rate III/IV; SC 8/9/12 Rate IV/V | Active | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/standby-rates |
| 45 | top | Consolidated Edison Co of New York  | Residential Time-of-Use Rate (with Summer Super-Peak) | Active | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/time-of-use |
| 46 | top | Consolidated Edison Co of New York  | Small Business Time-of-Use Rate | Active | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/time-of-use |
| 47 | top | Consolidated Edison Co of New York  | Large Business Time-of-Use Rate (demand-billed) | Active | CONFIRMED |  | https://www.coned.com/en/accounts-billing/your-bill/time-of-use |
| 48 | top | Consolidated Edison Co of New York  | Smart Thermostat Program (Bring Your Own Thermostat) | Active | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-residential-customers/bring-your-thermostat-and-get-85 |
| 49 | top | Consolidated Edison Co of New York  | SmartCharge New York (EV Drivers and Light-Duty Fleets) | Active | CONFIRMED |  | https://www.coned.com/en/save-money/rebates-incentives-tax-credits/rebates-incentives-tax-credits-for-residential-customers/electric-vehicle-rewards |
| 50 | top | Consolidated Edison Co of New York  | SmartCharge Commercial (Managed Charging for Station Operato | Active | CONFIRMED |  | https://www.coned.com/en/our-energy-future/electric-vehicles/commercial-electric-vehicle-charging-station-rewards |
| 51 | top | Consolidated Edison Co of New York  | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 52 | top | Consolidated Edison Co of New York  | Phase One Net Energy Metering (mass market) with Customer Be | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 53 | top | Niagara Mohawk Power Corp (National | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 54 | top | Niagara Mohawk Power Corp (National | Phase One Net Energy Metering (mass market) with Customer Be | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 55 | top | New York State Electric & Gas Corp  | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 56 | top | New York State Electric & Gas Corp  | Phase One Net Energy Metering (mass market) with Customer Be | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 57 | top | Rochester Gas & Electric Corp (RG&E | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 58 | top | Rochester Gas & Electric Corp (RG&E | Phase One Net Energy Metering (mass market) with Customer Be | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 59 | top | Long Island Power Authority / PSEG  | Net Energy Metering with Customer Benefit Contribution (mass | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 60 | top | Long Island Power Authority / PSEG  | Value Stack (VDER) Tariff - LIPA | Active | CONFIRMED |  | https://www.lipower.org/wp-content/uploads/2024/12/LIPA-Tariff-January-2025.pdf |
| 61 | top | Niagara Mohawk Power Corp (National | ConnectedSolutions - Bring Your Own Battery (BYOB) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Home/ConnectedSolutions/BatteryProgram |
| 62 | top | New York State Electric & Gas Corp  | Energy Storage Solutions Program (Bring Your Own Battery) | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 63 | top | Rochester Gas & Electric Corp (RG&E | Energy Storage Solutions Program (Bring Your Own Battery) | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 64 | top | Consolidated Edison Co of New York  | Bring Your Own Battery (BYOB) residential direct load contro | Proposed/pending | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 65 | top | Niagara Mohawk Power Corp (National | Commercial System Relief Program (CSRP) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response |
| 66 | top | Niagara Mohawk Power Corp (National | Distribution Load Relief Program (DLRP) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response |
| 67 | top | Niagara Mohawk Power Corp (National | Term Dynamic Load Management (Term-DLM) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response |
| 68 | top | Niagara Mohawk Power Corp (National | Auto Dynamic Load Management (Auto-DLM) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response |
| 69 | top | Niagara Mohawk Power Corp (National | Voluntary Time-of-Use Rate (SC-1 VTOU) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Home/Voluntary-Time-of-Use-Rate/Voluntary-Time-of-Use-Rate |
| 70 | top | Niagara Mohawk Power Corp (National | Optional Large Time-of-Use Rate (SC-1C) | Active | CONFIRMED |  | https://www.nationalgridus.com/Upstate-NY-Home/Voluntary-Time-of-Use-Rate/Voluntary-Time-of-Use-Rate |
| 71 | top | New York State Electric & Gas Corp  | Commercial System Relief Program (CSRP) | Active | CONFIRMED |  | https://www.nyseg.com/smartenergy/businesssolutions/cidemandresponse/commercial-system-relief-program |
| 72 | top | Rochester Gas & Electric Corp (RG&E | Commercial System Relief Program (CSRP) | Active | CONFIRMED |  | https://www.rge.com/smartenergy/businesssolutions/cidr/commercial-system-relief-program |
| 73 | top | New York State Electric & Gas Corp  | Distribution Load Relief Program (DLRP) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BC0746D9D-0000-CE30-88AD-5786AA5DCD01%7D&DocTitle=2026-04-08+NYSEG-RGE+Demand+Response+Annual+Report+Updated+REDACTED+(14-E-0423+et.+al.) |
| 74 | top | Rochester Gas & Electric Corp (RG&E | Distribution Load Relief Program (DLRP) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BC0746D9D-0000-CE30-88AD-5786AA5DCD01%7D&DocTitle=2026-04-08+NYSEG-RGE+Demand+Response+Annual+Report+Updated+REDACTED+(14-E-0423+et.+al.) |
| 75 | top | Long Island Power Authority / PSEG  | System Peak Relief Program (Commercial System Relief Program | Active | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/csrp/faq |
| 76 | top | Long Island Power Authority / PSEG  | Smart Savers Thermostat Program | Active | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers |
| 77 | top | Long Island Power Authority / PSEG  | Battery Storage Rewards Program | Active | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/GreenEnergy/SolarEnergy/EnergyStorageRewards |
| 78 | top | New York State Electric & Gas Corp  | Time-of-Use Service Class (SC-12) | Active | CONFIRMED |  | https://www.nyseg.com/account/understandyourbill/electricpricing/time-of-use-service-rate |
| 79 | top | New York State Electric & Gas Corp  | Standby Service (Service Classification No. 11) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B6D5D4D48-AC64-4CF9-9C0C-54C67295B62A%7D |
| 80 | top | Rochester Gas & Electric Corp (RG&E | Standby Delivery Service (Service Classification No. 14) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B6D5D4D48-AC64-4CF9-9C0C-54C67295B62A%7D |
| 81 | top | New York State Electric & Gas Corp  | Smart Savings Rewards Thermostat Program | Active | CONFIRMED |  | https://www.nyseg.com/smartenergy/rebatesandprograms/smartsavingsrewards |
| 82 | top | Rochester Gas & Electric Corp (RG&E | Smart Savings Rewards Thermostat Program | Active | CONFIRMED |  | https://www.rge.com/smartenergy/rebatesandprograms/smartsavingsrewards |
| 83 | top | Rochester Gas & Electric Corp (RG&E | Time-of-Use Service Class (SC-4) | Active | CONFIRMED |  | https://www.rge.com/account/understandyourbill/pricing/time-of-use-rates |
| 84 | top | New York State Electric & Gas Corp  | Hourly Pricing (Commercial) | Active | CONFIRMED |  | https://www.nyseg.com/smartenergy/understandyourusage/hourlypricingcommercial |
| 85 | top | Rochester Gas & Electric Corp (RG&E | Hourly Pricing (Commercial) | Active | CONFIRMED |  | https://www.rge.com/smartenergy/understandyourusage/hourly-pricing |
| 86 | top | New York State Electric & Gas Corp  | OptimizEV Residential Managed Charging Program | Active | REFUTED |  | https://www.nyseg.com/documents/40132/72042565/Final+NEVC005+NYSEG+OptimizEV+Residential+EV+MC+Program+FAQs.7.11.23.pdf/faae8ac1-639a-0182-ee20-d243d750ee9c?t=1689097614001 |
| 87 | top | Rochester Gas & Electric Corp (RG&E | OptimizEV Residential Managed Charging Program | Active | REFUTED |  | https://www.rge.com/documents/40137/72049582/Final+REVC005+RGE+OptimizEv+Residential+EV+MC+Program+FAQs.7.11.23.pdf/e45fc4b3-fb1f-d4c8-fe1a-e70873891ce0?t=1689098326178 |
| 88 | top | Long Island Power Authority / PSEG  | Time-of-Day Off-Peak Rate (standard residential TOD rate) | Active | CONFIRMED |  | https://www.psegliny.com/timeofday |
| 89 | top | Long Island Power Authority / PSEG  | Super Off-Peak Rate | Active | CONFIRMED |  | https://www.psegliny.com/timeofday |
| 90 | top | New York State Electric & Gas Corp  | Term Dynamic Load Management (Term-DLM) | Active | REFUTED | Y | https://www.nyseg.com/documents/d/nyseg/nyseg-term-and-auto-dlm-rfp |
| 91 | top | New York State Electric & Gas Corp  | Auto Dynamic Load Management (Auto-DLM) | Active | REFUTED | Y | https://www.nyseg.com/documents/d/nyseg/nyseg-term-and-auto-dlm-rfp |
| 92 | top | Rochester Gas & Electric Corp (RG&E | Term Dynamic Load Management (Term-DLM) | Active | CONFIRMED |  | https://www.rge.com/documents/d/rge/rge-term-and-auto-dlm-rfp |
| 93 | top | Rochester Gas & Electric Corp (RG&E | Auto Dynamic Load Management (Auto-DLM) | Active | CONFIRMED |  | https://www.rge.com/documents/d/rge/rge-term-and-auto-dlm-rfp |
| 94 | top | Long Island Power Authority / PSEG  | Time of Day Net Meter Bank Exchange | Active | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/solarenergy/todnetmeter |
| 95 | top | Long Island Power Authority / PSEG  | Standby Service (Service Classification No. 12) | Active | CONFIRMED |  | https://www.lipower.org/wp-content/uploads/2025/12/6.-Consideration-of-Approval-of-Tariff-Changes.pdf |
| 96 | top | Long Island Power Authority / PSEG  | Buyback Service (Service Classification No. 11) | Active | CONFIRMED |  | https://www.lipower.org/wp-content/uploads/2025/12/6.-Consideration-of-Approval-of-Tariff-Changes.pdf |
| 97 | top | Long Island Power Authority / PSEG  | Residential Charger Rebate Program | Active | CONFIRMED |  | https://www.psegliny.com/saveenergyandmoney/greenenergy/ev/residentialcustomers/chargerrebate |
| 98 | sample | New York Independent System Operato | Behind-the-Meter Net Generation (BTM:NG) Resource - exclusio | Active | NOT_DONE |  | https://www.nyiso.com/documents/20142/49802416/DER-and-Aggregation-Participation-Model-FAQ.pdf/967117fb-8bbb-1916-651a-0f9dbe904780 |
| 99 | sample | New York State Energy Research and  | NY-Sun Megawatt Block PV Incentive | Active | NOT_DONE |  | https://www.nyserda.ny.gov/All-Programs/NY-Sun/Contractors/Dashboards |
| 100 | sample | New York Independent System Operato | Targeted Demand Response Program (TDRP) | Active | NOT_DONE |  | https://www.nyiso.com/documents/20142/3037451/9-Demand-Response.pdf |
| 101 | sample | Central Hudson Gas & Electric Corp | Bring Your Own Battery (BYOB) residential direct load contro | Proposed/pending | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 102 | sample | Orange & Rockland Utilities Inc (O& | Residential Time-of-Use Rate | Active | NOT_DONE |  | https://www.oru.com/en/accounts-billing/your-bill/time-of-use |
| 103 | sample | New York Independent System Operato | ICAP Spot Market Auction - NYCA / Rest of State (upstate) UC | Active | NOT_DONE |  | https://icappublic.nyiso.com/ucap/public/auc_view_spot_detail.do?seasonId=705094&month=08/2026&display=Display |
| 104 | sample | New York State Energy Research and  | Residential Energy Storage Incentive (market rate) | Active | NOT_DONE |  | https://www.nyserda.ny.gov/All-Programs/Energy-Storage-Program/Developers-and-Contractors/Residential-and-Retail-Storage-Incentives/Residential-Dashboard |
| 105 | sample | Central Hudson Gas & Electric Corp | Targeted Demand Response (TDR) Program | Active | NOT_DONE |  | https://cenhudpeakperks.com/targeted-demand-response/ |
| 106 | sample | Orange & Rockland Utilities Inc (O& | Auto Dynamic Load Management (Auto-DLM) | Active | NOT_DONE |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B90B1368C-0000-C331-A0EC-CEBAF516BD9E%7D&DocTitle=OandR+2025+Vintage+Year+Term-+and+Auto-DLM+RFP |
| 107 | sample | New York State Energy Research and  | Retail Energy Storage Incentive (market rate) | Active | NOT_DONE |  | https://www.nyserda.ny.gov/All-Programs/Energy-Storage-Program/Developers-and-Contractors/Residential-and-Retail-Storage-Incentives/Retail-Incentive-Dashboard |
| 108 | sample | New York Independent System Operato | Dual Participation - NYISO Aggregation plus utility DR progr | Active | NOT_DONE |  | https://www.nyiso.com/documents/20142/49802416/DER-and-Aggregation-Participation-Model-FAQ.pdf/967117fb-8bbb-1916-651a-0f9dbe904780 |
| 109 | sample | Central Hudson Gas & Electric Corp | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | NOT_DONE |  | https://www.cenhud.com/en/my-energy/distributed-generation/programs-and-incentives/ |
| 110 | sample | New York Independent System Operato | DER Aggregation - eligibility sizing rules (10 kW DER / 100  | Active | NOT_DONE |  | https://www.nyiso.com/documents/20142/2923301/M-38-Aggregation-Final-v1-0.pdf/488117aa-43ec-85c3-423d-4aba592e5895 |
| 111 | sample | Orange & Rockland Utilities Inc (O& | Standby Service and Standby Service Rates (Service Classific | Active | NOT_DONE |  | https://www.oru.com/en/save-money/using-private-generation-energy-sources/private-generation-tariffs |
| 112 | sample | Orange & Rockland Utilities Inc (O& | Term Dynamic Load Management (Term-DLM) | Active | NOT_DONE |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B90B1368C-0000-C331-A0EC-CEBAF516BD9E%7D&DocTitle=OandR+2025+Vintage+Year+Term-+and+Auto-DLM+RFP |

Per-item notes are in `audit/results/NYISO.json`.

## Defect list (programs.csv rows are 1-based data rows; file line = row+1; presence_scan.csv given as file line)

### Errors (count against the bars)
1. **presence_scan.csv line 390 (Niagara Mohawk, eia 13573), `ci_habit` = No -> Yes.** Src: https://www.nationalgridus.com/Upstate-NY-Business/Rates/Service-Rates (SC-3A Large General TOU with hourly supply; EV Phase-In Rate with TOU energy charges). Item 6.
2. **programs.csv row 533 (NYSEG Term-DLM), `incentive_value_usd`** -> 'Incentive Rate cap $25.50/kW-yr (Nov 27 2025 RFP, 2027 vintage); actual payment set by accepted bid; $0.50/kWh performance'. Row carries RG&E's $26.25 and a reversed history. Src: https://www.nyseg.com/documents/d/nyseg/nyseg-term-and-auto-dlm-rfp. Item 90. wrong_dollar.
3. **programs.csv row 534 (NYSEG Auto-DLM), `incentive_value_usd`** -> same fix as #2. Item 91. wrong_dollar.
4. **programs.csv row 525 (NYSEG OptimizEV), `incentive_value_usd`** -> 'Baseline tier $25 one-time, Advanced tier $150 one-time; monthly reward = (default volumetric - TOU rate) x off-peak kWh when >=80% off-peak (e.g. $0.032/kWh)'. Remove 'per-kWh reward value is not published'. Item 86.
5. **programs.csv row 526 (RG&E OptimizEV)** -> same fix as #4 (RG&E FAQ). Item 87.

### Source-URL defects (cell/value correct, cited page does not show it; replace `*_src`/`source_url`)
6. presence_scan line 390 NiMo `ci_dispatch_src` (residential battery page) -> https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response
7. presence_scan line 391 LIPA `res_dispatch_src` (CSRP FAQ, no device control) -> https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers
8. presence_scan line 392 NYSEG `ci_habit_src` (2019 PSC order) -> https://www.nyseg.com/smartenergy/understandyourusage/hourlypricingcommercial ; `ci_dispatch_src` (NYSERDA residential BYOB PDF) -> https://www.nyseg.com/smartenergy/businesssolutions/cidemandresponse/commercial-system-relief-program
9. presence_scan line 393 RG&E `ci_habit_src` -> https://www.rge.com/smartenergy/understandyourusage/hourly-pricing ; `ci_dispatch_src` -> https://www.rge.com/smartenergy/businesssolutions/cidr/commercial-system-relief-program
10. presence_scan line 395 O&R `ci_dispatch_src` (NYSERDA residential PDF; no C&I content) -> O&R CSRP/DLRP page (not verified; item 27 INCONCLUSIVE).
11. presence_scan line 394 Central Hudson `res_dispatch_src`: NYSERDA PDF shows CH residential BYOB only as 'launching later in 2026' -> cite a currently offered program (e.g. Peak Perks thermostat) or recheck; item 31 INCONCLUSIVE.
12. programs.csv row 503 (PSEG-LI Smart Savers, item 76) source_url is a 2026 press release with no $ -> https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers ($85 + $25/yr confirmed there).
13. programs.csv rows 459/460 (Con Ed CSRP/DLRP): CSRP-unplanned $6/$10 per kWh and $5/kW-mo adder appear only in the Con Ed 'smart usage program example' PDF; adder trigger is 5+ events per season, not 'from month of 5th event'. Add that PDF as a second source / reword.
14. programs.csv rows 470/472/474/476 (Value Stack CBC for Con Ed/NiMo/NYSEG/RG&E): CBC $ correct per NYSERDA 2026 CBC PDF, but cited utility documents (e.g. Con Ed 2020 Value Stack components PDF) do not show CBC; cite the NYSERDA 2026 CBC PDF.

### Minor / staleness notes
- Row 468 (Con Ed SmartCharge NY, item 49): 'additional $35 Avoided Summer Peak bonus' duplicates the $35/mo; 3-month bonus is $25.
- Row 521 (RG&E Smart Savings Rewards, item 82): the $20 is an e-gift card at RG&E, not a bill credit. NYSEG/RG&E pages do not state 2026 status.
- Rows 487/488-type BYOB 'Proposed/pending' (Con Ed item 64, Central Hudson item 101): based on Jan 2026 NYSERDA deck saying 'launching later in 2026'; recheck status now.
- Rows 505/506 NYSEG/RG&E DLRP: status 'Active' but $0.00/kW-mo and zero enrollment; consider status note. Annual report also gives CSRP performance $0.60/kWh after hour 4.
- Row 78-type (NYSEG SC12 TOU): add eligibility >=35,000 kWh/yr.
- Con Ed standby rows/cells and LIPA ci_habit cite standby rates; valid time-differentiated designs, but the C&I TOU pages are stronger sources.
