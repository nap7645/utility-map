# scan_SE1 gaps — North Carolina (43 utilities)

## Coverage summary
- res_habit: 21 Yes / 3 No / 19 Unknown
- res_dispatch: 16 Yes / 5 No / 22 Unknown
- ci_habit: 5 Yes / 38 Unknown (0 No)
- ci_dispatch: 5 Yes / 38 Unknown (0 No)
- rto: all 43 tagged `SERC-nonRTO` (no TVA distributors or MISO/PJM-adjacent co-ops found in this NC cluster; see Haywood/French Broad note below)
- ownership_type: 2 IOU (Duke Carolinas, Duke Progress), 24 Cooperative, 17 Municipal

C&I cells are the weakest coverage layer — most co-op and municipal sites surface residential
programs prominently but bury or omit commercial/industrial rate and DR program pages, and the
WebSearch budget ran out (200 calls/session) before those could be chased down systematically.

## WebSearch budget exhausted mid-run
The session's WebSearch tool hit its hard per-session cap partway through the co-op batch (right
after Edgecombe-Martin/Rutherford). All research from that point on (Fayetteville PWC through the
last 11 municipals) relied on direct `web_fetch` of guessed/known URLs only, with no query-engine
fallback. This is why the last ~11 municipal rows (Wilson, Concord, Gastonia, Rocky Mount,
Lexington, Statesville, Washington, Elizabeth City, Kinston, Monroe, Lumberton) are entirely
`Unknown` across all four cells — their own-domain electric-utility rate/program pages could not
be located by guessing URL patterns alone. **A follow-up pass with WebSearch available should
prioritize these 11 municipals first** — they are ElectriCities/NCEMPA members (confirmed
membership for Rocky Mount only; assumed for the rest by pattern) and likely run their own TOU
and/or load-management switch programs like Fayetteville, New Bern, Apex, and Greenville did.

## Notable finds worth flagging
- **Connect to Save** (NC's Electric Cooperatives' shared smart-thermostat/water-heater program,
  connecttosavenc.com) currently has an active 6-co-op roster confirmed directly from the
  program's own "Choose Your Co-op" dropdown: Carteret-Craven, Four County, Lumbee River, Pee Dee,
  South River, Tri-County. **Jones-Onslow EMC's participation is discontinued** (its
  connecttosavenc.com/coop/joemc page explicitly says so) — flagged and corrected in the row (do
  not assume the "4 founding co-ops" cluster-note framing is still accurate; it has since expanded
  to 6 and dropped Jones-Onslow). Brunswick EMC runs a lookalike program natively on its own
  domain (bemc.org/beat-peak) rather than through the shared connecttosavenc.com platform.
- **Name-collision traps hit and avoided**: "Blue Ridge Electric Cooperative" at blueridge.coop is
  a *South Carolina* co-op (Pickens, SC) — unrelated to our target, Blue Ridge Energy / Blue Ridge
  Electric Membership Corporation of Lenoir, NC (blueridgeenergy.com). Both surfaced in the same
  search results; only the NC domain was used for the row.
- **Haywood EMC and French Broad EMC (western NC)**: sources conflict on whether these still buy
  wholesale from NCEMC, or from Duke/Nantahala directly as the region plan hypothesized. Tagged
  `SERC-nonRTO` but flagged `Unverified`/`Secondary` on the rto call — worth a direct look at each
  co-op's PURPA filing or PSC docket to settle definitively. Blue Ridge EMC and the Connect-to-Save
  co-ops were more clearly confirmed as standard NCEMC full-requirements members.
- **Rutherford EMC** and **Edgecombe-Martin County EMC**: both checked directly and found to lack
  a residential TOU/demand rate (Rutherford) or a device-control program (Edgecombe-Martin) as of
  this scan — genuine `No`s, not just unresearched gaps.

## Could not verify
- All C&I cells for every co-op and municipal row except Fayetteville PWC (ci_habit=Yes) and
  Greenville Utilities (ci_habit=Yes via Coincident Peak commercial schedules) — C&I rate/program
  pages are usually a level or two deeper in these small-utility sites and were not reached within
  budget.
- res_habit for Halifax EMC, Tri-County EMC, Edgecombe-Martin, Wake Forest-adjacent municipals —
  rate schedules exist as PDFs that were not opened and read line-by-line.
- res_dispatch and both C&I cells for Apex (own load-management page exists by URL/title but the
  page body would not render for this fetcher — worth a direct re-fetch or browser-based check).
- Duke Energy Carolinas/Progress PowerPair capacity status (DEP reported at/near capacity in some
  secondary sources) was not independently re-verified against Duke's live enrollment tracker.
