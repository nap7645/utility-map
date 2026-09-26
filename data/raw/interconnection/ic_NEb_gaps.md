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

