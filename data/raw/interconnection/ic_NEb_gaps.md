# NEb (NH, VT, ME) interconnection — gaps and notes

## NH
- Sources read: En 900 (gc.nh.gov/rules/state_agencies/en900.html, eff 2026-04-27), Puc 900 (gc.nh.gov/rules/state_agencies/puc900.html, eff 2020-09-14), HB 1718 = Laws 2026 Ch. 309 (approved 2026-07-10), Eversource NH net-metering and application pages. Order 27,074 PDF 404s at the PUC link; its content is taken from the CPCNH and Clean Energy NH summaries (Secondary). The fee schedule was confirmed on Eversource's page (Primary for Eversource).
- MID-TRANSITION: En 901.02(b) says net-metering interconnection "shall be governed by the rules established in En 1000", but no En 1000 is posted on gc.nh.gov (404). So the Puc 904-908 interconnection provisions are assumed to still govern small generators. Unverified.
- grid_charging_allowed: the rule is explicit only from 2027-01-01 (Ch. 309). The contingency on HB 1742 changes only which RSA paragraph number (XXIV vs XXV) is used, not the substance. The PUC has not yet set compensation terms for storage exports; expect a docket in 2027.
- Battery added to an existing NEM system: Puc 904.06 requires written notice and re-certification when capacity increases or the inverter is replaced. Whether adding storage alone changes NEM 2.0 / legacy (pre-2017 standard tariff) status is not addressed in En 900 or Puc 900: Unclear. From 2027 the statute says storage does not affect size eligibility, which suggests no loss of status, but no rule text says so.
- ic_fast_track_kw left blank: NH has no Fast Track tier as such. The simplified tier covers <=100 kW.
- Standby charges: none found in state rules; left blank.

## VT
- Source read: Rule 5.100 PDF (eff 2024-03-01), Primary. Sections 5.137 (storage), 5.129(B) (12-month credit expiry), 5.129(D) (500 kW limit), 5.126 (production meter and adjustors), 5.109 (amendments), 5.131 (interconnection under 5.500).
- NOT VERIFIED: the 2026 biennial update values ($0.2071 blended rate; -$0.05/-$0.05/-$0.07/-$0.08 siting; REC -$0.04). They come from the program-chunk lead (GMP/VEC tariff rows), because puc.vermont.gov/document/2026-biennial-update-net-metering-program could not be fetched (tool outage / session limit).
- NOT READ: Rule 5.500 interconnection (fast-track and simplified thresholds, fees, timelines, disconnect, insurance, storage and non-export provisions). The VT state row leaves the ic_* columns blank except the 15 kW registration tier.
- Battery added to an existing NM system: 5.137 applies to pre-existing systems too. 5.109 requires an amended CPG only for 'substantial changes', and a material modification under 5.500 needs utility approval first. The rule does not say whether adding storage is a substantial change or resets adjustors/vintage: Unclear.

## Run status (2026-09-26, first run) — INCOMPLETE, stopped by the web-tool session limit
- Done: NH and VT state rows.
- NOT DONE (a relaunch should resume here): the ME state row (MPUC Ch. 324 interconnection; Ch. 313 NEB kWh-credit and tariff-rate programs; LD 1986 / 2025 successor reforms). All 9 utility delta rows are also not done: Eversource NH (PSNH), Unitil Energy Systems, Liberty (Granite State Electric), NHEC (member-regulated check; transactive rate pilot), GMP (BYOD/ESS vs net metering; ESS/BYOD sunset 2026-09-30), BED, VEC, CMP, Versant.
- Leads already noted for the utility pass: Liberty NH runs a battery program in which batteries export at the net-metering rate during monthly peak events (NH Bulletin 2026-05-20, and the Liberty battery-storage page in chunk_NE_rest.csv). Under Ch. 309, utility-controlled charging is the statutory exception to charge-only-from-solar. VEC: credits expire after 12 months, siting charge for apps from 2026-08-01 (vermontelectric.coop/net-metering). GMP BYOD tariff requires grid charging, so check how GMP reconciles this with Rule 5.137 (probably separate metering / no NM credit on battery export).
- Helper script _neb_helpers.py in this folder (append-only csv.writer) can be reused or deleted.


## Run status (2026-09-26, resume run): COMPLETE
- Added the ME state row. Filled the VT Rule 5.500 blanks (ic_standard, fast-track tier, fee, study trigger, timeline, non-export). Verified the VT 2026 biennial values against the order (Case 26-0291-INV, 2026-05-29, ordering ¶1-7): $0.2071 blended; REC $0.00/-$0.04; siting Cat I/II -$0.05, III -$0.07, IV -$0.08 from 2026-08-01. The "verify" note is removed. Filled NH ic_fast_track_kw from En 1000.
- Added 8 utility rows: Eversource NH, Liberty, NHEC, GMP, BED, VEC, CMP, Versant. **No row for Unitil Energy Systems (NH)**: its NH net-metering page follows state rules and shows no deviation (absence = state default).
- The helper script _neb_helpers.py was already gone. Its leftover __pycache__ was removed.

## NH (new finding)
- **En 1000 exists now**: "Adopted Rules 7-17-26" (DOE DER interconnection procedures), found as a copy on Unitil's site (unitil.com/sites/default/files/2026-08/EN-1000-Rules.pdf). Contents: simplified process for inverter-based facilities <=50 kW nameplate / <=25 kW export; fast track for <=1 MW export; standard process for the rest. IEEE 1547-2018 / 1547.1-2020 and UL 1741 (2025 ed.). En 1013 limited/non-export methods. En 1004.04(d): the "addition of an energy storage device" to an existing DER goes through the utility's modification process, and exempt modifications skip the queue. NOT CONFIRMED: the effective date and whether it has been filed with OLS/posted on gc.nh.gov. The NH state row's Puc 904-908 cells (simplified <=100 kW, 10-business-day completeness, disconnect/insurance rules) may be superseded once En 1000 takes effect. Re-check next pass.

## ME
- Sources read: 35-A §3209-A (current through PL 2025 c. 430), Ch. 313 PDF on maine.gov (2019 text; the MPUC NEB page cites a later §3(J)(4), so Ch. 313 has been amended since and the amended text was NOT read), Ch. 324 as amended in Docket 2023-00103 (CMP-hosted copy; effective-date line blank in that copy), MPUC NEB page (tariff rates through CY2025), OPA LD 1777 release, CMP battery CNEBA + NEB FAQ, Versant NEB application.
- NOT READ: the 2025-12-17 tariff-rate orders (Dockets 2019-00197 / 2022-00185) with 2026-2046 rates; the Docket 2020-00332 advisory ruling itself (its content is taken from the CMP/Versant agreement text quoting it); PL 2025 c. 430 NEB project-charge amounts; §3209-B text.
- LD 1777 litigation: a Dec 2025 Foley Hoag post says MPUC delayed enforcing part of the statute while a federal court weighed a preliminary injunction. Outcome not checked.
- storage_counts_toward_cap: Unclear. No rule text found.
- Insurance tiers in Ch. 324 §15(F) skip inverter-based 1-2 MW (no amount stated in the text read).
- Retrofit on legacy NEB: the CMP FAQ says pre-2019-00197 agreements get a 20-year term when modified. PL 2025 c. 430 §1 says amendments after 2025-06-01 cannot extend the end date. These conflict, and how CMP applies them now is Unclear.

## VT utilities
- GMP: the "Solar with Battery Storage Requirements" PDF is a CAD drawing that rendered blank in both the fetch tool and the browser. The gross-meter/battery request form fetch returned empty. So how GMP meters battery exports against NM credit (Rule 5.137 compliance for BYOD grid-charging) is Unclear. BYOD availability ends 2026-09-30; no successor tariff found.
- BED: the posted tariff (eff 2024-08-01) still lists NM 2.6 siting adjustors (-$0.04 Cat I/II). A BED update for the 2026 biennial values was not found.
- VEC / BED / GMP: none says whether adding a battery to a pre-2017 NM system is a Rule 5.109 "substantial change". BED's tariff only says a pre-existing system loses status if capacity rises by more than 5% or 15 kW (amended on/after 2024-03-01).

## NH utilities
- Eversource NH: the Interconnection Standards for Inverters (<=100 kVA) PDF was not read. No battery charge-source rule was found on Eversource NH pages. grid_charging = Unclear (state Ch. 309 governs from 2027).
- NHEC: T&C Section X was read via the browser pane (the page body is JS-rendered). Storage is explicitly within "interconnection-facility", and no charge-source rule exists: Unclear. Whether Ch. 309 (RSA 362-A:9) binds NHEC's self-set tariff was not verified.
- Liberty: the battery pilot is closed. Grid-charged utility-dispatched exports credited at the NM rate are documented (Primary page). Nothing found for customer-owned batteries.
