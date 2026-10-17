# b11 log (2026-10-16)

Captured rows: 11 schedules across 5 of 8 utilities. Validator: ALL OK (12x24 coverage per schedule/day_type).

- 8287 Hawaii Electric Light (HI): Schedule R (tiered, default), Schedule G. Source: HI PUC Effective Rate Summaries filing eff. 2026-09-01 (effective rates incl. ECRC/PPAC/RBA etc; monthly-changing). No open TOU: ARD TOU R/G, TOU-R, TOU-RI, TOU-EV, TOU-G all closed to new enrollments per HELCO tariff sheets (checked each). ~9 fetches.
- 3841 Coast Electric Power Assn (MS): 1Q, 61K (TOU), 2Q, 52I (TOU). PCA/TEA riders not numerically stated in tariff. ~3 fetches. Holiday off-peak not coded.
- 10376 Kissimmee Utility Authority (FL): RS (2-tier), GS. COPCA fuel charge not in tariff PDF. No residential or small-commercial TOU found (GSDT is >5,000 kWh/mo). ~6 fetches.
- 4432 Coweta-Fayette EMC (GA): residential flat, residential TOU, small commercial, from utility.org/electric-rates (eff. 2024-04-01) via WebFetch only (curl blocked by Cloudflare). Page tab labels inferred by block order; residential flat is_default left blank; electric-heat block not coded. Page date is 2024; no newer source found.

Not captured:
- 7294 City of Glendale (CA): glendaleca.gov returns Akamai 403 to curl and WebFetch errors on residential/small-business rate pages; the rate-adjustments page has only % increases. 6 tries, no tariff numbers read.
- 6182 Farmers Electric Coop (TX, Greenville): only a 2026 rate-change notice (eff. 2026-10-01, +7.77% single phase, no rate tables); no tariff published on site. 4 tries.
- 16613 Sam Houston Electric Coop (TX): samhouston.net fails TLS verification (incomplete cert chain, not bypassed), WebFetch blocked by robots.txt. 5 tries.
- 1149 Baldwin County EMC (AL): site publishes only the 2026 increase (+$2.00 basic service, +$0.00597/kWh residential, eff. 2026-03-01), not base rates; member handbook has no numbers. 5 tries.
