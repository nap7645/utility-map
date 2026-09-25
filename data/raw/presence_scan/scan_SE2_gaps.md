# scan_SE2.csv — gaps and caveats

50/50 Georgia targets have rows. 42 rows carry at least one `Unknown` cell — mostly
`ci_habit`/`ci_dispatch`, the hardest cells to confirm from a public website because C&I
program details are often gated behind an account login or only available by calling.

## Why so many Unknowns

1. **WebSearch budget exhausted mid-run.** ~200 WebSearch calls were used getting through
   Georgia Power and the larger EMCs (Jackson, Cobb, Sawnee, GreyStone, Walton, Snapping
   Shoals, North Georgia, Flint, Coweta-Fayette, Colquitt, Central Georgia, Satilla, Blue
   Ridge Mountain, Carroll, Amicalola, Marietta) before hitting the cap right after starting
   on Okefenoke REMC / Hart EMC / Diverse Power / Habersham EMC. Every utility researched
   after that point was done with `web_fetch` against guessed/likely domains only, with no
   search fallback to find the right URL if a guess was wrong.
2. **Guessed domains that failed.** Several fetches to guessed URLs returned empty or
   errored (Jefferson EMC, Tri-County EMC (GA), City of East Point, City of Griffin, City of
   Lawrenceville, City of La Grange, City of Covington) — these are `Unknown` across all four
   cells with notes explaining the site was unreachable or JS-only, per the hard rule that
   unreachable sites get `Unknown`, never a guessed `No`.
3. **Co-ops that simply don't publish rates or programs online.** A meaningful number of
   smaller EMCs (Oconee, Ocmulgee, Crisp County Power Commission, Little Ocmulgee) have full
   working websites but no rate schedule published at all — "contact us for rate
   information" — and no dispatch/DR program described anywhere in their nav. These are
   `Unknown` for `res_habit`/`ci_habit` (can't rule out a program a phone call would reveal)
   but `No` for `res_dispatch` where the full site nav was reviewed and clearly has no
   thermostat/switch/curtailable program page.
4. **C&I load-management specifics that need a second page never fetched.** Little Ocmulgee
   EMC has an "Irrigation Application" page under its Business nav that was never opened —
   Irwin EMC's equivalent page turned out to describe a switch-controlled load-management
   rate, so the same could be true here, but it was left `Unknown` rather than assumed.

## Utilities fully `Unknown` (site unreachable/JS-only)

- Jefferson Electric Member Corp
- Tri-County Elec Member Corp (GA)
- City of East Point
- City of Griffin
- City of Lawrenceville
- City of La Grange
- City of Covington

## Notable corrections made during research (documented in the CSV `notes` column)

- **Snapping Shoals EMC**: a WebSearch AI summary claimed a residential TOU plan existed;
  the actual primary-source rate PDFs on ssemc.com showed only flat seasonal rates. Row was
  corrected to `res_habit=No`/`ci_habit=No` based on the primary document, not the search
  summary.
- **Carroll EMC (GA)**: a search result for "load management water heater" returned content
  from `cecpower.coop` (Carroll Electric Cooperative, **Arkansas**), not `carrollemc.com`
  (the Georgia EMC in this target list). That program was not credited to the Georgia
  entity; `res_dispatch=Unknown` with a note explaining the name collision.

## Confidence tier note

Georgia's EMCs are Oglethorpe Power (G&T) members, but Oglethorpe is generation-only and
does not run member programs the way TVA does for its distributors — so no G&T-level
shortcut was used for any Oglethorpe member; each was checked on its own site. The TVA
shortcut (rto=TVA, cite TVA EnergyRight) was used only for the three confirmed TVA
distributors in this batch (North Georgia EMC, Blue Ridge Mountain EMC, Tri-State EMC), per
the region plan.
