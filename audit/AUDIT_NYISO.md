# NYISO audit (independent)

Date: 2026-10-02, resumed 2026-10-12. Sample: `audit/samples/NYISO.json`, seed **20261002**, 113 items (40 presence, 73 program rows). Top-bucket territories: Con Edison, National Grid NY, LIPA/PSEG-LI, NYSEG, RG&E (100% of their sampled cells and rows).

## Method
Each item checked against the live cited page with WebFetch (no Wayback, no researcher notes, no other audit files). Presence Yes: confirmed only if the page shows that program type for that segment, currently offered; if the cited page did not show it (or was unreadable), one replacement search on the utility's own site was done and the cell confirmed from the replacement (logged as a source defect). Presence No: utility business/residential rate and DR pages searched. Program rows: name, category, $ value/units, status, source checked against current documents (effective dates noted).

**Resume 2026-10-12:** the 34 items left NOT_DONE (32) or INCONCLUSIVE (2) on 2026-10-02 were re-done by the same method. All 34 now have a verdict; 8 remain INCONCLUSIVE because the site cannot be read by the audit fetcher: jamestownnybpu.gov and freeportelectric.com rate pages return ROBOTS_DISALLOWED on every page (6 No cells), the NYISO Manual 38 PDF is robots-blocked (item 110), and the O&R standby SC number/charge structure is not on any readable page (item 111). cenhud.com pages return a bot-check interstitial except the TOU-billing page; Central Hudson items were resolved from that page, cenhudpeakperks.com, or the NYSERDA CBC PDF.

**Row/line convention (corrected):** the sample's `row` is the physical line number in `data/processed/programs.csv` (header = line 1), not "data row; file line = row+1" as the 2026-10-02 version said. Presence cells live in `data/processed/presence.csv` (the 2026-10-02 version wrongly labelled them `presence_scan.csv`); line numbers below are `presence.csv` lines. Row numbers in the earlier defect list were re-checked against the current files and corrected where they were off.

## Counts

| Group | CONFIRMED | REFUTED | INCONCLUSIVE | NOT_DONE |
|---|---|---|---|---|
| Yes | 27 | 0 | 0 | 0 |
| No | 6 | 1 | 6 | 0 |
| program | 65 | 6 | 2 | 0 |
| **Total (113)** | 98 | 7 | 8 | 0 |

## Rates vs bars

| Bar | Excl. inconclusive | Incl. inconclusive | Pass? |
|---|---|---|---|
| Yes confirmed >=95% | 27/27 = 100.0% | 27/27 = 100.0% | PASS |
| No confirmed >=90% | 6/7 = 85.7% | 6/13 = 46.2% | FAIL (1 refuted: NiMo ci_habit; 6 inconclusive: Jamestown, Freeport robots-blocked) |
| Program rows all fields correct | 65/71 = 91.5% | 65/73 = 89.0% | 6 rows refuted (log and fix) |
| 0 wrong $ in top bucket | 2 wrong (NYSEG Term-DLM, Auto-DLM) | | FAIL |
| 0 wrong $ in sample bucket (informational) | 0 wrong | | - |

Region cannot pass until: the No-cell bar is met (6 robots-blocked No cells need a manual browser check; a single further refutation keeps it failing), the 2 top-bucket wrong-$ rows are fixed, and every defect below is fixed and re-verified by a different agent.

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
| 20 | sample | Fairport Electric (Fairport Municip | res_habit | No | CONFIRMED |  | https://cms9files.revize.com/fairport/electric/Billing/12-1-25%20Billing%20Sheet.pdf |
| 21 | sample | Jamestown Board of Public Utilities | res_habit | No | INCONCLUSIVE |  | https://www.jamestownnybpu.gov/156/Electric |
| 22 | sample | Central Hudson Gas & Electric Corp | ci_habit | Yes | CONFIRMED |  | https://www.cenhud.com/en/my-energy/my-energy-options/time-of-use-billing/ |
| 23 | sample | Rockville Centre Electric Departmen | res_dispatch | Yes | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BE0A68098-0000-C75A-A009-5F980FA12D2E%7D |
| 24 | sample | Jamestown Board of Public Utilities | ci_dispatch | Yes | CONFIRMED |  | https://www.publicpower.org/periodical/article/new-general-manager-jamestown-board-public-utilities-details-open-access-fiber-network-project-flex |
| 25 | sample | Freeport Electric (Village of Freep | ci_dispatch | No | INCONCLUSIVE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 26 | sample | Jamestown Board of Public Utilities | ci_habit | No | INCONCLUSIVE |  | https://www.jamestownnybpu.gov/156/Electric |
| 27 | sample | Orange & Rockland Utilities Inc (O& | ci_dispatch | Yes | CONFIRMED |  | https://www.oru.com/en/save-money/rebates-incentives-credits/new-york-customers/incentives-for-business-customers-ny/demand-response-incentives |
| 28 | sample | Rockville Centre Electric Departmen | ci_dispatch | Yes | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BE0A68098-0000-C75A-A009-5F980FA12D2E%7D |
| 29 | sample | Freeport Electric (Village of Freep | res_habit | No | INCONCLUSIVE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 30 | sample | Jamestown Board of Public Utilities | res_dispatch | No | INCONCLUSIVE |  | https://www.jamestownnybpu.gov/351/Reliable-Power |
| 31 | sample | Central Hudson Gas & Electric Corp | res_dispatch | Yes | CONFIRMED |  | https://cenhudpeakperks.com/ |
| 32 | sample | Fairport Electric (Fairport Municip | ci_habit | No | CONFIRMED |  | https://cms9files.revize.com/fairport/electric/Billing/12-1-25%20Billing%20Sheet.pdf |
| 33 | sample | Central Hudson Gas & Electric Corp | res_habit | Yes | CONFIRMED |  | https://www.cenhud.com/en/my-energy/my-energy-options/time-of-use-billing/ |
| 34 | sample | Plattsburgh Municipal Lighting Depa | ci_dispatch | No | CONFIRMED |  | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 35 | sample | Orange & Rockland Utilities Inc (O& | res_habit | Yes | CONFIRMED |  | https://www.oru.com/en/accounts-billing/your-bill/time-of-use |
| 36 | sample | Freeport Electric (Village of Freep | ci_habit | No | INCONCLUSIVE |  | https://www.freeportelectric.com/2180/Electric-Rates |
| 37 | sample | Rockville Centre Electric Departmen | res_habit | No | CONFIRMED |  | https://www.rvcny.gov/electric-department/pages/electric-rates |
| 38 | sample | Plattsburgh Municipal Lighting Depa | ci_habit | No | CONFIRMED |  | http://cityofplattsburgh.com/sites/cityofplattsburgh.com/files/municipal-lighting-department/TARIFF%20PAGES.pdf |
| 39 | sample | Rockville Centre Electric Departmen | ci_habit | No | CONFIRMED |  | https://www.rvcny.gov/electric-department/pages/electric-rates |
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
| 98 | sample | New York Independent System Operato | Behind-the-Meter Net Generation (BTM:NG) Resource - exclusio | Active | CONFIRMED |  | https://www.nyiso.com/documents/20142/49802416/DER-and-Aggregation-Participation-Model-FAQ.pdf/967117fb-8bbb-1916-651a-0f9dbe904780 |
| 99 | sample | New York State Energy Research and  | NY-Sun Megawatt Block PV Incentive | Active | REFUTED |  | https://www.nyserda.ny.gov/All-Programs/NY-Sun/Contractors/Dashboards-and-incentives |
| 100 | sample | New York Independent System Operato | Targeted Demand Response Program (TDRP) | Active | CONFIRMED |  | https://www.nyiso.com/documents/20142/3037451/9-Demand-Response.pdf |
| 101 | sample | Central Hudson Gas & Electric Corp | Bring Your Own Battery (BYOB) residential direct load contro | Proposed/pending | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/2026-01-22-Utility-DLM-Program-Overview.pdf |
| 102 | sample | Orange & Rockland Utilities Inc (O& | Residential Time-of-Use Rate | Active | CONFIRMED |  | https://www.oru.com/en/accounts-billing/your-bill/time-of-use |
| 103 | sample | New York Independent System Operato | ICAP Spot Market Auction - NYCA / Rest of State (upstate) UC | Active | CONFIRMED |  | https://icappublic.nyiso.com/ucap/public/auc_view_spot_detail.do?seasonId=705094&month=08/2026&display=Display |
| 104 | sample | New York State Energy Research and  | Residential Energy Storage Incentive (market rate) | Active | REFUTED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/Residential-and-Retail-Energy-Storage-Program-Manual.pdf |
| 105 | sample | Central Hudson Gas & Electric Corp | Targeted Demand Response (TDR) Program | Active | CONFIRMED |  | https://cenhudpeakperks.com/targeted-demand-response/ |
| 106 | sample | Orange & Rockland Utilities Inc (O& | Auto Dynamic Load Management (Auto-DLM) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B90B1368C-0000-C331-A0EC-CEBAF516BD9E%7D&DocTitle=OandR+2025+Vintage+Year+Term-+and+Auto-DLM+RFP |
| 107 | sample | New York State Energy Research and  | Retail Energy Storage Incentive (market rate) | Active | CONFIRMED |  | https://www.nyserda.ny.gov/All-Programs/Energy-Storage-Program/Developers-and-Contractors/Residential-and-Retail-Storage-Incentives/Retail-Incentive-Dashboard |
| 108 | sample | New York Independent System Operato | Dual Participation - NYISO Aggregation plus utility DR progr | Active | CONFIRMED |  | https://www.nyiso.com/documents/20142/49802416/DER-and-Aggregation-Participation-Model-FAQ.pdf/967117fb-8bbb-1916-651a-0f9dbe904780 |
| 109 | sample | Central Hudson Gas & Electric Corp | Value Stack (Value of Distributed Energy Resources / VDER) T | Active | CONFIRMED |  | https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf |
| 110 | sample | New York Independent System Operato | DER Aggregation - eligibility sizing rules (10 kW DER / 100  | Active | INCONCLUSIVE |  | https://www.nyiso.com/documents/20142/2923301/M-38-Aggregation-Final-v1-0.pdf/488117aa-43ec-85c3-423d-4aba592e5895 |
| 111 | sample | Orange & Rockland Utilities Inc (O& | Standby Service and Standby Service Rates (Service Classific | Active | INCONCLUSIVE |  | https://www.oru.com/en/save-money/using-private-generation-energy-sources/private-generation-tariffs |
| 112 | sample | Orange & Rockland Utilities Inc (O& | Term Dynamic Load Management (Term-DLM) | Active | CONFIRMED |  | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B90B1368C-0000-C331-A0EC-CEBAF516BD9E%7D&DocTitle=OandR+2025+Vintage+Year+Term-+and+Auto-DLM+RFP |

Per-item notes are in `audit/results/NYISO.json`.

## Defect list (programs.csv: physical file line; presence: data/processed/presence.csv file line)

### Errors (count against the bars)
1. **presence.csv line 390 (Niagara Mohawk, eia 13573), `ci_habit` = No -> Yes.** Src: https://www.nationalgridus.com/Upstate-NY-Business/Rates/Service-Rates (SC-3A Large General TOU with hourly supply; EV Phase-In Rate with TOU energy charges). Item 6. *Status 2026-10-12: presence.csv now shows Yes with this src; needs re-verification by a different agent.*
2. **programs.csv line 533 (NYSEG Term-DLM), `incentive_value_usd`** -> 'Incentive Rate cap $25.50/kW-yr (Nov 27 2025 RFP, 2027 vintage); actual payment set by accepted bid; $0.50/kWh performance'. Row carries RG&E's $26.25 and a reversed history. Src: https://www.nyseg.com/documents/d/nyseg/nyseg-term-and-auto-dlm-rfp. Item 90. wrong_dollar.
3. **programs.csv line 534 (NYSEG Auto-DLM), `incentive_value_usd`** -> same fix as #2. Item 91. wrong_dollar.
4. **programs.csv line 526 (NYSEG OptimizEV), `incentive_value_usd`** -> 'Baseline tier $25 one-time, Advanced tier $150 one-time; monthly reward = (default volumetric - TOU rate) x off-peak kWh when >=80% off-peak (e.g. $0.032/kWh)'. Remove 'per-kWh reward value is not published'. Item 86. (Earlier version said row 525.)
5. **programs.csv line 527 (RG&E OptimizEV)** -> same fix as #4 (RG&E FAQ). Item 87. (Earlier version said row 526.)
6. **NEW programs.csv line 495 (NYSERDA NY-Sun Megawatt Block PV Incentive), item 99.**
   - `source_url` is 404 -> https://www.nyserda.ny.gov/All-Programs/NY-Sun/Contractors/Dashboards-and-incentives
   - `program_category` = Storage-Incentive and `eligible_assets` = Solar+Storage are not supported: the schema defines Storage-Incentive as a BESS rebate, and the NY-Sun page does not mention storage. Either recategorize (no PV-incentive enum exists; raise with schema owner) or drop the row as out of scope. Keep it only if a NY-Sun storage adder is cited (e.g. the Long Island residential storage under the NY-Sun Upstate+LI manual).
   - `event_limits`: replace 'adders exist for affordable housing and low-to-moderate-income customers' with the adders the page lists: Community Adder, Inclusive Community Solar Adder, Statewide Solar for All Adder, Prevailing Wage Adder.
7. **NEW programs.csv line 490 (NYSERDA Residential Energy Storage Incentive), item 104.**
   - `event_limits`: 'from 3/1/2026 projects in National Grid, NYSEG and RG&E territory must also enroll in the utility BYOB program' -> 'incentive applications on or after 4/1/2026 in National Grid (ConnectedSolutions Battery) and NYSEG/RG&E (Energy Storage Solutions) territory must enroll in the utility DLM program; waived until 6/1/2026 if the storage manufacturer is not yet onboarded'.
   - Remove 'first-come first-served' (the manual states it for Retail only).
   - Add the manual as `source_url` (the dashboard page shows none of these rules): https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Energy-Storage/Residential-and-Retail-Energy-Storage-Program-Manual.pdf (April 2026).

### Source-URL defects (cell/value correct, cited page does not show it or is unreadable; replace `*_src`/`source_url`)
8. presence.csv line 390 NiMo `ci_dispatch_src` (residential battery page) -> https://www.nationalgridus.com/Upstate-NY-Business/Demand-Response/Electric-Demand-Response
9. presence.csv line 391 LIPA `res_dispatch_src` (CSRP FAQ, no device control) -> https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers
10. presence.csv line 392 NYSEG `ci_habit_src` (2019 PSC order) -> https://www.nyseg.com/smartenergy/understandyourusage/hourlypricingcommercial ; `ci_dispatch_src` (NYSERDA residential BYOB PDF) -> https://www.nyseg.com/smartenergy/businesssolutions/cidemandresponse/commercial-system-relief-program
11. presence.csv line 393 RG&E `ci_habit_src` -> https://www.rge.com/smartenergy/understandyourusage/hourly-pricing ; `ci_dispatch_src` -> https://www.rge.com/smartenergy/businesssolutions/cidr/commercial-system-relief-program
12. presence.csv line 395 O&R `ci_dispatch_src` (NYSERDA residential PDF; no C&I content) -> https://www.oru.com/en/save-money/rebates-incentives-credits/new-york-customers/incentives-for-business-customers-ny/demand-response-incentives (Smart Usage Rewards; confirmed 2026-10-12, item 27).
13. presence.csv line 394 Central Hudson `res_dispatch_src` (NYSERDA PDF: CH BYOB only 'launching later in 2026') -> https://cenhudpeakperks.com/ (Free Sensi Thermostat, BYOD, Outdoor Switch; confirmed 2026-10-12, item 31).
14. **NEW** presence.csv line 394 Central Hudson `ci_habit_src` (TOU application PDF; bot-blocked, residential-oriented) -> https://www.cenhud.com/en/my-energy/my-energy-options/time-of-use-billing/ (C&I hourly pricing mandatory for large, optional for medium; item 22). `res_habit_src` (EV-TOU page, bot-blocked to fetcher) is acceptable but the TOU-billing page is the readable source (item 33).
15. **NEW** presence.csv line 396 Jamestown BPU `ci_dispatch_src`: APPA article (2026-03-13) has a single GM line that C&I flex-rate agreements include 'demand response'. The cell stays Yes, but a primary BPU source (tariff or flex-rate agreement terms) should replace or supplement it (item 24).
16. programs.csv line 511 (PSEG-LI Smart Savers, item 76) source_url is a 2026 press release with no $ -> https://www.psegliny.com/saveenergyandmoney/greenenergy/peakload/smartsavers ($85 + $25/yr confirmed there). (Earlier version said row 503.)
17. programs.csv lines 459/460 (Con Ed CSRP/DLRP): CSRP-unplanned $6/$10 per kWh and $5/kW-mo adder appear only in the Con Ed 'smart usage program example' PDF; the adder trigger is 5+ events per season, not 'from month of 5th event'. Add that PDF as a second source and reword.
18. programs.csv lines 470/474/476/478 (Value Stack CBC for Con Ed/NiMo/NYSEG/RG&E) and **NEW line 480 (Central Hudson, item 109)**: CBC $ correct per the NYSERDA 2026 CBC PDF, but the cited utility pages do not show CBC (the Central Hudson page is bot-blocked). Cite https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/NY-Sun/2026-Utility-Published-Customer-Benefit-Contribution-Rates.pdf. (Earlier version said rows 470/472/474/476.)
19. **NEW** programs.csv line 538 (O&R Term-DLM, item 112): the claim '2027 vintage year currently solicited' is unsupported. The cited doc is the 2025-vintage RFP issued 2023-12-04, and no 2027 O&R RFP was found on oru.com. Cite the current O&R RFP or remove the claim. Same stale source on line 539 (Auto-DLM, item 106).

### Minor / staleness notes
- Line 468 (Con Ed SmartCharge NY, item 49): 'additional $35 Avoided Summer Peak bonus' duplicates the $35/mo; the 3-month bonus is $25.
- Line 521 (RG&E Smart Savings Rewards, item 82): the $20 is an e-gift card at RG&E, not a bill credit. The NYSEG/RG&E pages do not state 2026 status.
- Lines 488/489 BYOB 'Proposed/pending' (Con Ed item 64, Central Hudson item 101): based on the Jan 2026 NYSERDA deck saying 'launching later in 2026'; recheck status now.
- Lines 506/507 NYSEG/RG&E DLRP: status 'Active' but $0.00/kW-mo and zero enrollment; consider a status note. The annual report also gives CSRP performance $0.60/kWh after hour 4.
- Line 516 (NYSEG SC12 TOU): add eligibility >=35,000 kWh/yr.
- Con Ed standby rows/cells and LIPA ci_habit cite standby rates. These are valid time-differentiated designs, but the C&I TOU pages are stronger sources.
- **NEW** Line 563 (NYISO ICAP Spot ROS, item 103): the $ values for May-Sep 2026 match. In `event_limits`, 'Upstate ... roughly one quarter to one fifth of New York City capacity' holds only for May-Jun (0.24); the ratio is Jul 0.33, Aug 0.37, Sep 0.48. Reword. The Summer 2025 list omits September. The Winter 2025-26 and Summer 2025 values were not checked.
- **NEW** Line 509 (Central Hudson TDR, item 105): the page says $6.825/kW-mo; the row truncates to $6.82. The page does not show 'constrained program areas' or 'may not also participate in CSRP'. Add 'minimum 50 kW commitment; aggregator-enrolled payment set by aggregator'.
- **NEW** Lines 538/539 (O&R Term/Auto-DLM): `incentive_value_usd` is blank. The RFP gives a $1/kWh performance payment plus a pay-as-bid $/kW Incentive Rate; add both.
- **NEW** Line 491 (NYSERDA Retail Storage, item 107): the incentive applies to the first 4 h of duration, with hours 5-6 at 25% and nothing beyond 6 h. The IOU-rate value requirement is framed in the manual as a demand-charge or VDER use case.
- **NEW** Line 558 (NYISO TDRP, item 100): 'Manual 7 Section 6', the sub-load-pocket tie and the CSP advisory notification are not in the cited 2024 training deck. Cite EDRP Manual 7 directly.
- **NEW** Line 515 (O&R Standby, item 111, INCONCLUSIVE): neither readable O&R page shows 'Service Classification No. 25' or the contract-demand/as-used structure. Cite the tariff leaf.
- **NEW** presence.csv line 399 (Rockville Centre `ci_dispatch` = Yes, item 28): the support is a thermostat DSM program 'residential and small commercial' with 0 commercial enrollments in 2024-25. This is a weak fit to C&I dispatch; consider Unknown.
- **NEW** presence.csv line 400 (Plattsburgh): the cited tariff is the 2010 vintage (eff. 01/01/2010). The No cells are confirmed against it, but the current tariff should be cited if one exists.
- **Not checkable by fetcher (manual browser check needed):** presence.csv line 396 Jamestown res_habit/res_dispatch/ci_habit (items 21, 30, 26); line 398 Freeport res_habit/ci_habit/ci_dispatch (items 29, 36, 25); programs.csv line 570 NYISO DER sizing (item 110, M-38 PDF robots-blocked).
