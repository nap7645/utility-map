# LMP history notes (Rank 1 layer 2)

Built 2026-10-19. Year 2025, day-ahead hourly only. Reproduce: `python3 scripts/lmp_pull.py` then `python3 scripts/lmp_zone_map.py`. Raw (filtered) cache in `data/lmp_cache/` (gitignored, ~10 MB; re-runs skip cached files; log in `data/lmp_cache/pull.log`).

## Outputs
- `data/processed/lmp_summary.csv`: 49 rows (market, zone, year), all n_hours = 8760, no duplicate keys. Columns: stats ($/MWh), `summer_h00..h23` (Jun-Sep) and `winter_h00..h23` (Dec-Feb of 2025), `tz`, `source`. Hour-of-day = local clock hour-beginning in `tz`; daily spread = max-min of the 24 DA hours per local calendar day.
- `data/processed/lmp_zone_map.csv`: all 514 territories (eia_id in hifld_over10k) with presence.json rto in the 7 markets; 383 have a zone, 131 blank. Columns include method, confidence, source_url, `has_price_data`, notes.

## Sources and method (all free public downloads, no keys)
| Market | Zones in summary | Source |
|---|---|---|
| NYISO | A-K (11 zones) | mis.nyiso.com public damlbmp zone CSV (monthly zips) |
| ISO-NE | 8 load zones + internal hub | iso-ne.com/histRpts/da-lmp daily CSV (LOAD ZONE, HUB rows) |
| ERCOT | 8 LZ_* + HB_* hubs (15) | ERCOT NP4-180 Historical DAM Load Zone and Hub Prices via `gridstatus.Ercot.get_dam_spp` |
| CAISO | DLAP PGAE, SCE, SDGE, VEA | OASIS SingleZip PRC_LMP, market DAM, LMP_TYPE=LMP |
| MISO | 8 trading hubs | docs.misoenergy.org `YYYYMMDD_da_expost_lmp.csv`, Type=Hub nodes ending `.HUB` |
| SPP | SPPNORTH_HUB, SPPSOUTH_HUB | portal.spp.org file-browser `da-lmp-by-settlement-location` |
gridstatus 0.36.0 was installed but only used for ERCOT: its NYISO path uses http:// (blocked by the sandbox proxy) and its PJM path needs a key. Direct URLs were simpler and equal in coverage.

## Validation done
- No duplicate (market, zone, year); n_hours = 8760 for all 49 (DST handled via UTC; NYISO fall-back hour disambiguated, ISO-NE `02X` hour handled).
- Spot check: NYISO zone J June mean recomputed from the raw zip equals the cache (48.23). Values plausible against known 2025 patterns (ISO-NE ~$66, NYISO ~$53-56, ERCOT hubs ~$33, MISO hubs $33-44).
- NOT done: second-agent independent recompute per RANK1 section 2 "Check"; zone map not reviewed against ISO documents.

## Missing / caveats
- **PJM: no price data.** Data Miner 2 API requires a (free) subscription key; none available. `lmp_pull.py` has an UNTESTED PJM branch that activates when `PJM_API_KEY` is set. Zone map still gives PJM transmission zones (66/112 mapped) with `has_price_data=No`.
- **MISO: hubs only, no zonal/LRZ price.** The public DA ex-post file has hub rows and thousands of pnodes but no zonal aggregate. Zone map assigns the nearest hub (method state_default/name_match, confidence low-medium). Treat as context, not the settlement price.
- **SPP: two hubs only.** Public file has no load-zone aggregates; map uses hub by region (low confidence).
- **ERCOT:** DAM settlement point prices (LZ_*, HB_*), not LMP; includes hubs. Zone map covers only utilities I could place from public geography (28/59); co-ops spanning zones left blank.
- **ISO-NE:** MA is three zones; National Grid MA (Mass Electric), Narragansett and most MA munis left blank or low confidence. Narragansett (RI) also left blank (serves RI zone plus some MA); RI zone is the likely default if you want it filled.
- **NYISO:** utilities spanning zones (NiMo, NYSEG, ConEd Westchester) get the dominant zone, confidence low/medium; no flag column beyond notes.
- **CAISO:** munis inside IOU areas are mapped to the IOU DLAP with confidence low; their own settlement points may differ. Turlock ID, Bear Valley blank (outside CAISO BAA or no DLAP). VEA DLAP priced but no CA territory mapped to it.
- Some presence.json `rto` values look wrong and were left blank with a note: Indiana Michigan Power (PJM-AEP, tagged MISO), Mississippi Power (tagged MISO). HIFLD state is HQ state for some IOUs (Ameren Illinois = MO, JCP&L = OH), so IOUs are matched by name first.
- Zone-map methods: `iso_table` used where I applied the ISO/TO service-area table from knowledge, not from a downloaded ISO file; source_url points to the ISO landing page, not a table. Re-verify the high-value rows (top IOUs) against ISO documents before relying on them.
- Day-ahead only; no real-time or 5-min. Single year (2025); one year understates tails (scarcity events, e.g. ERCOT >$500 hours = 4 in DA).
- Non-RTO regions: no LMP, left blank per RANK1 decision 3.
- Hour-of-day in MISO is prevailing Eastern converted from the reports' fixed EST;

## Corrections (verify_lmp_2026-10-19.md)
- Narragansett (13214) now mapped to .Z.RHODEISLAND (high).
- NYSEG spans zones A, C-H (not B-G); ConEd also serves parts of G and H (default J kept).
- ERCOT hours > $500/MWh range 4-11 by zone; raw cache is ~5.8 MB.
