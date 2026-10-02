# Gaps — presence scan cluster W2 (Oregon, Montana, Wyoming)

32/32 targets have rows; validator passes (17 fields, all eia_ids present exactly once).
RTO is `WECC-nonRTO` on every row per the region plan (no organized market in this cluster).

## High-confidence findings worth flagging

- **PacifiCorp (14354)** — one HIFLD record covers Pacific Power (OR/WA/CA) and Rocky Mountain
  Power (UT/ID/WY). Confirmed Oregon residential TOU (Schedule 29), C&I Demand Response program,
  and Rocky Mountain Power's Wattsmart Battery VPP (incentives changed July 2026 in WY/ID).
- **Portland General Electric (15248)** — region reference case, all four cells Yes with
  Primary sources (Peak Time Rebates, Smart Battery Pilot, Energy Partner curtailment program).
- **Residential demand charges are more common in this region than expected** and count as
  `res_habit=Yes` per the schema's own vocabulary: confirmed at Flathead Electric (MT),
  Ravalli Electric (MT), Lower Valley Energy (WY, new Oct 2026), City of Gillette (WY),
  Missoula Electric's "Peak Charge" (MT), and Powder River Energy Corp / Midstate Electric /
  PRECorp's optional residential TOU rates (OR/WY).
- **Load-management / DR-unit programs on water heaters, AC, and irrigation** are common among
  Oregon/Montana co-ops supplied by BPA or their own G&Ts: confirmed at Central Electric
  Cooperative (OR) and Flathead Electric (MT); OTEC (OR) shows indirect evidence (billing
  calculator excludes "load management" programs) but no dedicated page was found.

## Could not verify — and why

- **Northern Wasco County PUD (13788)** — both candidate URLs (nwasco.org, nwascopud.org)
  returned empty content on fetch, and the WebSearch budget (200/200) was exhausted before this
  utility could be researched by search. All four cells `Unknown`. Needs a direct site visit or
  a fresh search budget.
- **Douglas Electric Cooperative (5327)** — found a block-rate energy-charge structure but could
  not confirm which customer class (residential vs. general/commercial) it applies to, nor find
  a TOU/DR program page, before the search budget ran out. All four cells `Unknown`.
- **Salem Electric (16555)** — rate schedule is published only as a PDF that returned no
  extractable text via fetch; no DR/dispatch program page found in site navigation. All four
  cells `Unknown`.
- **Ashland Electric Utility / City of Ashland (907)** — Electric Rates page and its linked PDF
  both returned no extractable content (likely JS-rendered or scanned). All four cells `Unknown`.
- **Consumers Power Inc (4743)** — cpi.coop rate/service pages returned empty content on fetch
  (JS-rendered site); general search found only an average cents/kWh figure, no tariff detail.
  All four cells `Unknown`.
- **High Plains Power (8566)** and **Lane Electric Cooperative (10681)** — rate schedules are
  PDF-only and did not yield extractable text; no dedicated DR/TOU program page found in site
  navigation. All four cells `Unknown` on both.
- **Mission Valley Power / USBIA (19603)** — small federally-owned tribal utility (CSKT/Flathead
  Reservation) with limited public program pages; an Operations Manual references an irrigation
  "curtailment" section (4.8) tied to the Flathead Indian Irrigation Project, not confirmed as an
  electricity load-control DR program. Mostly `Unknown`/`Unverified`.
- **NorthWestern Energy (12825)** — confirmed a residential TOU demonstration rate (Schedule
  RSGTOUD-1) and confirmed absence of a residential dispatch program (checked "Ways to Save"
  page directly), but could not find a C&I curtailable/TOU tariff page in the time available —
  `ci_habit`/`ci_dispatch` left `Unknown`, would need a direct tariff-book lookup.
- Several Oregon PUDs/co-ops (Central Lincoln PUD, Columbia River PUD, Umatilla Electric Coop,
  Emerald PUD, Coos-Curry, McMinnville Water & Light) have confirmed `No` on habit cells (flat
  rates, no TOU, no qualifying residential demand charge) but `res_dispatch`/`ci_dispatch` are
  mixed `No`/`Unknown` depending on how thoroughly the efficiency/conservation section could be
  reviewed before the search budget ran low.

## Search budget

WebSearch calls were exhausted (200/200) near the end of the run. The final ~5 targets
(Northern Wasco County PUD, Douglas Electric, High West Energy, Ravalli Electric, Forest Grove)
were researched using only `web_fetch` on direct URLs and prior search results already in
context — several came back thinner than the rest of the cluster as a result. A follow-up pass
with a fresh search budget would likely resolve most of the `Unknown` cells above, particularly
for the PDF-only tariffs (Salem Electric, High Plains Power, Lane Electric, Douglas Electric,
Consumers Power) which need either OCR/PDF text extraction or a direct phone/tariff-book check.

## fill3b pass (2026-10-02)
- Douglas Electric (5327): res_habit/ci_habit=No from dec.coop/rate-information (Sch 1,2,4,5,6,11-17; no TOU/off-peak). Dispatch cells not checked on program pages.
- High Plains Power (8566): 2022 Cowboy State Daily quote from CFO says no thermostat program (exploring DR) - news, not own site, so res_dispatch left Unknown.
- Ashland (907): commercial incentives page lists no DR/curtailment, but electric-rates PDF blocked; not enough for a No.
- Salem, Consumers Power, Lane, Northern Wasco: rate PDFs/sites not extractable or robots-blocked.
