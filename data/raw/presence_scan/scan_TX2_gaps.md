# Gaps — scan_TX2.csv (TX municipals + non-ERCOT utilities)

Search budget and per-utility depth were limited; the following need a follow-up pass.

## RTO corrections / uncertainties (fix cluster notes)

- **Deep East Texas Electric Cooperative (4975)** and its G&T **East Texas Electric
  Cooperative (ETEC)** had a partial withdrawal from MISO with transmission assets
  transferred to **SPP**, FERC-approved 6/14/2019, effective 7/1/2019 (SPP filing
  ER19-1137). The cluster notes' "East Texas co-ops → MISO" shortcut is stale for this
  co-op; set `rto=SPP` unless a closer look shows otherwise.
- **Jasper-Newton EC (9668)** — also an ETEC/Golden-Spread-adjacent member; some sources
  describe it as straddling ERCOT/MISO. Marked SPP as Secondary; needs a direct look at
  jnec.com or an SPP/MISO filing naming this co-op specifically.
- **Sam Houston EC (16613)** — confirmed 99% MISO via Entergy transmission, <1% ERCOT.
  This one is solid (Primary, own PURPA page + public reporting).
- **Bowie-Cass (2049), Rusk County (16461), Panola-Harrison (14424)** — rto=SPP is an
  inferred cluster pattern (Northeast/East Texas co-ops), not confirmed per-co-op against
  a balancing-authority source. Own rate pages exist (bcec.com, rcelectric.org, phec.us)
  but were not opened.
- **Lyntegar EC (11364)** — rto left as Unknown. Golden Spread G&T member in the
  Lubbock/South Plains area; PUC filings reference historical SPP→ERCOT load-transfer
  applications for this cluster (same dynamic as Lubbock's 2023-24 ERCOT move and South
  Plains EC's ERCOT/SPP split). Needs a direct source.
- **Lamb County EC (10625)** — rto=SPP by Panhandle/Golden-Spread pattern, not verified
  against a balancing-authority source.
- **South Plains EC (17561)** — confirmed split ERCOT (Rolling Plains members) / SPP
  (Lubbock-area members) via the co-op's own outage-map page; recorded as
  `rto=ERCOT/SPP split`.

## Unknown/Unverified presence cells needing a real look

Most of the small munis and co-ops below have `Unknown` in one or more program cells
because their own rate/program pages were not opened (time/budget), not because a
program doesn't exist:

- Floresville (FELPS), Weatherford (WMUS), Bowie-Cass EC, Rusk County EC,
  Panola-Harrison EC, Deep East Texas EC, Jasper-Newton EC, Deaf Smith EC, Lamb County EC,
  Lyntegar EC, San Marcos (SMEU — site is JS-rendered and returned no content via fetch),
  Garland (GP&L — same JS-rendering issue on gpltexas.org).
- Lubbock (LP&L): now a TDU-only entity post-2024 ERCOT transition; `res_dispatch` for an
  LP&L-run (EE-rider) program was not found — worth checking whether LP&L still runs one,
  and whether ERCOT ERS/Load Resource participation should be logged as a distinct
  ERCOT-level row rather than folded into this utility's ci_dispatch.

## Confirmed via the utility's own page (safe to build on)

Austin Energy, CPS Energy, Xcel/SPS, Sam Houston EC, Bryan (BTU), Denton (DME, partial —
commercial TOU schedule seen but not the full tariff), Brownsville (BPUB), New Braunfels
(NBU), Upshur Rural EC, Kerrville (KPUB), Greenville (GEUS — commercial TOU/Primary
Voltage option confirmed).
