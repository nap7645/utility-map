# Gaps - chunk_AKHI (Hawaii + Alaska islanded utilities), verified 2026-09-29

Method note: the shell sandbox has no internet, so all reading was done with web_fetch/WebSearch. Hawaiian Electric pages are very large. They were read by grepping saved fetch output. HECO rate values come from the 9/1/2026 Effective Rate Summary filed with the PUC (efs_2026_09.pdf).

## Hawaiian Electric (Oahu / Hawaii Island / Maui County)
- **BYOD Plus**
  - The monthly credit is the customer's retail rate plus a "2-hour window supplemental rate". HECO does not publish the supplemental rate in c/kWh. The only figure is the example of about $52/mo for 5 kW x 2 hr.
  - The list of available 2-hour timeslots is not published.
  - The statewide 50 MW cap (split LMI / non-LMI) and the LMI upfront total of $800/kW come from secondary sources (alternateenergyhawaii, NCSU), not the HECO page.
  - The BYOD Plus page does not list a monthly $/kW capacity payment. Legacy BYOD Level 1 paid $5/kW-mo; whether BYOD+ keeps it was not verified.
- **Grid Services Purchase Agreement (GSPA)**
  - GSPA 2/3 (Swell "Home Battery Rewards"): HECO terminated them on 2025-01-29.
  - The "GS Interim Solution" (filed 2025-02-07) was not found as a customer program, and its approval status was not confirmed.
  - GSPA 1 (OATI) was extended to 2026-11-30. Its successor was not found.
  - No row was written for GSPA itself because there is no current customer-facing $/kW offer. The legacy GSPA upfront and monthly $/kW values were not found.
- **ConnectedSolutions-style BYOD event program (DPS Phase 4, Order 41445):** a PUC decision was expected by Dec 2025. No 2026 order or launched program was found.
- **BYOD Level 2 / Level 3 riders** (event-based, $5 and $10/kW-mo): never launched as far as found. They are recorded only inside the Level 1 row context.
- **Smart DER Tariff**
  - Battery grid-charging rules for the Export and Non-Export riders were not verified.
  - The 3-year rate reset (due around April 2027) was not found.
  - The "7-year lock-in" claim is from secondary sources only and was left out of the rows.
  - A separate Non-Export Rider row was not written because it has no compensation value.
- **Customer Self-Supply (CSS), Customer Grid-Supply (CGS) and NEM/NEM Plus** (all legacy, closed): pages were not read, so no rows. Grid-charging rules for CSS were not verified.
- **Shift and Save (ARD TOU R/G/J)**
  - Rates come from the Effective Rate Summary.
  - The Maui County pilot was excluded from the TOU Study (Order 40278). It is unconfirmed whether any Maui, Lanai or Molokai customers are actually on ARD TOU, even though the tariff rates exist.
  - PUC June 2025: TOU is not to become default "for the foreseeable future". The residential page says only Schedule R is open to new single-family customers.
- **TOU EV (residential EV rate):** closed to new customers. The rates for existing customers are not in the Effective Rate Summary and were not captured. Rows were written with rates blank.
- **EV-F** was terminated 2023-07-01, which is before 2025, so it was excluded.
- **EnergyScout**
  - Oahu only; closed to new participants.
  - Large-business $/kW credit not published.
  - No EnergyScout-type DLC was found on Maui or Hawaii Island. HECO metrics say "Hawaii Island does not currently have a DR program", so Fast DR is Oahu and Maui only.
- **Fast DR:** the $5 or $10/kW-month and $0.50/kW-per-hour figures are from search snippets. HECO's page confirms only "$6,000/yr for 50 kW". The Program Rules v6.0 PDF was not read.
- **State storage and resilience incentives**
  - Hawaii HB513 (35% battery-retrofit tax credit, up to $500k per system) was carried over to 2026. Enactment was not confirmed, so no row.
  - The existing HRS 235-12.5 RETITC (35%, $5,000 residential cap per PV system) was not written as a row. It is not utility-specific, and whether batteries count on their own was not verified.
  - No Hawaii Energy (PBF) battery rebate was found.

## Kauai Island Utility Cooperative
- **TOU:** no current TOU rate found. The 2016-17 solar TOU pilot ended. The KIUC tariffs page could not be re-fetched (fetch cache conflict).
- **Export options:** KIUC's proposed "Customer Self-Supply" and "Smart Export" (to replace the Schedule Q Non-Export and Export options) were found only in 2018 news. Current approval status and any export c/kWh are unverified.
- **Schedule Q:** the row uses the 2025 filed avoided cost. The rule that PV above the right-size limit must be paired with ESS of equal or greater rating is from a secondary source.
- **Batteries, DR, rates:** no KIUC battery incentive or DR program was found beyond the $200 Medical Device Power Backup rebate (Secondary, news). KIUC commercial demand rates were not captured (they are only in the xlsx rate data).

## Alaska (all utilities)
- **Statewide net metering:** 3 AAC 50.900-949 applies, with a 25 kW cap and excess credited at the non-firm/avoided-cost rate.
- **HB 164** (Governor's bill: retail-rate net metering for Railbelt utilities over 5 GWh, annual credit cycle): stalled in House Finance on 2026-04-01. It is **not law**.
- **No battery storage incentive, battery DR/VPP, or BYOD program** was found at any of the five Alaska utilities.
- **Heat pump rebates** were found but left out because no program_category fits:
  - Chugach: up to $900 residential / $1,500 commercial, max 2 per account (v2.2, Jan 2026).
  - Homer Electric: has a Heat Pump Rebate Program; the amount was not read.
  - MEA: education only.
  - AEL&P: Heat Pumps page not read, but Rate 92 heat pump service was captured.

**Per utility:**
- **Chugach:**
  - The TOU pilot rates come from the TOU FAQ (Sept 2026). Enrollment opens Oct 1 2026 and the pilot starts Jan 1 2027 (TA580-8).
  - The net-metering buyback uses the North District "Purchased Power Rates for Qualified Facilities" (6.831c secondary). It is assumed to be the Sheet 97 non-firm rate, but Sheet 97 itself was not read.
  - South District rates were not captured.
  - No DR or interruptible program for retail customers was found.
- **MEA:**
  - Off-Peak Thermal Storage is closed to new customers; the date it closed is unknown.
  - Off-peak hours for that rate are not on the rate sheet.
  - No DR program was found.
- **GVEA:**
  - The rates shown are interim (TA399-13 rate case).
  - The Residential TOU Pilot (three periods, up to 500 members) is proposed. Its hours, prices and approval status were not found.
  - The Controlled Load Shed Program is emergency rotating outages, not DR, so it was excluded.
  - GVEA's legacy SNAP production-incentive program was not checked for current status.
- **Homer Electric:** no TOU, EV rate or DR program was found. The EV page (homer.chooseev.com) was not read.
- **AEL&P:**
  - The net metering program and its credit rate were **not verified**. AEL&P's site has no net-metering page that could be found. HB 164 would have covered AEL&P, but it is not law.
  - The large interruptible special contracts (Greens Creek, Princess, Holland America at $0.11250/kWh proposed, TA540-542) were left out because they are not generally available.
