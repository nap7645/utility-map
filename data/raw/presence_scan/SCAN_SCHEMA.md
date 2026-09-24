# Presence scan — schema

Purpose: a has / doesn't-have flag per utility, NOT a full program catalog. Speed over depth.
The map colors each territory by these four cells. A wrong "No" is worse than an "Unknown" —
it tells a salesperson to skip a territory that may have opportunity. So: **only write "No" when
you actually looked at the utility's own website/tariff and found nothing.** If you couldn't
find the utility's site, or it was JS-only and unreadable, write "Unknown".

## Output: one CSV per cluster, `scan_<X>.csv`

Header, exactly:

```
eia_id,hifld_name,utility_name,hifld_state,rto,ownership_type,res_habit,res_habit_src,res_dispatch,res_dispatch_src,ci_habit,ci_habit_src,ci_dispatch,ci_dispatch_src,notes,last_verified,confidence
```

- **eia_id, hifld_name, hifld_state** — copy from the targets file exactly.
- **utility_name** — the name the utility actually uses today (e.g. `Great Lakes Energy Cooperative`, not the HIFLD string). Needed for future joins.
- **rto** — the wholesale market / balancing area the utility's load sits in. **Do this for every row; it is cheap and it gates everything.** Use one of:
  - RTO/ISO markets: `MISO` | `PJM` | `SPP` | `NYISO` | `ISO-NE` | `CAISO` | `ERCOT`
  - No organized market: `TVA` | `AECI` | `SERC-nonRTO` (Southeast vertically-integrated BAs: Duke, Southern, Santee Cooper, etc.) | `FRCC-nonRTO` (Florida) | `WECC-nonRTO` (West outside CAISO: BPA/PNW, Desert SW, Rockies, CA public power in their own BAs) | `Other-nonRTO`
  - `Unknown` only if you genuinely cannot determine it.
  Being in a state does not put a utility in that state's RTO. A G&T's membership usually determines its distribution co-ops' market (e.g. Wolverine → MISO; Buckeye → PJM; Big Rivers → MISO; East Kentucky Power → PJM; Hoosier → MISO; Wabash Valley → MISO/PJM split; Associated Electric → AECI; Dairyland → MISO; Great River → MISO; Basin → SPP/WECC/MISO mix; Oglethorpe → SERC-nonRTO). The region plan in `plans/` lists the regional G&Ts — check it.
- **ownership_type** — `IOU` | `Cooperative` | `Municipal` | `Federal/State`.

### The four cells — each is `Yes` | `No` | `Unknown`

| cell | means the utility offers, to that segment, at least one… |
|---|---|
| `res_habit` | residential price-signal program: time-of-use rate, real-time/hourly rate, critical-peak pricing or peak-time rebate, residential demand charge, or EV time-of-use rate |
| `res_dispatch` | residential program where the utility (or its contractor) controls a device: AC/water-heater switch, smart-thermostat program, bring-your-own-device/battery, VPP, off-peak/dual-fuel storage heating with utility control |
| `ci_habit` | commercial/industrial time-of-use, real-time pricing, or demand-charge-based rate designed for load shifting (a plain demand charge on every C&I rate does NOT count — it must be a shifting-oriented design or an optional TOU) |
| `ci_dispatch` | C&I interruptible / curtailable rider, load-management program, or aggregator-facing DR |

- **`*_src`** — a URL on the utility's own domain (or its regulator's) that shows the program exists. One URL per Yes. Required for every Yes. Optional for No (put the page you checked if you have it).
- **notes** — one line: anything odd. "TVA distributor — see TVA programs", "site unreachable", "closed program still listed", etc.
- **last_verified** — today's date, ISO format (YYYY-MM-DD)
- **confidence** — write ONE of these (the column name is kept for compatibility, the meaning is the evidence tier):
  - `Primary` — the `source_url` IS the source: the utility's own tariff sheet or program page, a regulator order/rule, an RTO manual, or a statute. Clicking it shows the claim.
  - `Secondary` — the `source_url` reports on the source: news, DSIRE/OpenEI, trade press, a G&T page describing a member's program, a PUC summary of a tariff.
  - `Unverified` — no usable link, or the link does not actually show the claim. Inferred from a state pattern or G&T membership.
  Older files use High/Medium/Low; `scripts/source_tier.py` maps those and the URL domain to the tier above. Prefer the new vocabulary.

## Shortcuts that are legitimate

- **TVA distributors** (TN and many KY/MS/AL/GA/NC/VA-border co-ops and munis): TVA runs the programs. Write `rto=TVA`, mark cells from TVA's residential/C&I offerings, cite TVA, note it. Do not research each one individually.
- **G&T-run programs**: co-ops served by a G&T (Great River Energy, Dairyland, Hoosier, Wolverine, East Kentucky Power, Wabash Valley, Buckeye, Basin, Minnkota, Associated Electric, Oglethorpe, Tri-State, Old Dominion, North Carolina EMC, and others) often run the *G&T's* load-management program. If the G&T runs it, cite the G&T and mark Yes for the member. That's accurate — the member's customers are enrolled.
- If a state's co-ops almost universally run a water-heater switch program (Minnesota, the Dakotas, Wisconsin), you may still need to confirm per co-op — but it's one page each.

## Hard rules

1. **Write with Python's `csv` module (`csv.writer`, default quoting).** Then re-read the file and assert every row has 17 fields. Previous research runs produced unquoted-comma CSVs that cost a repair pass. Do this check before you report done.
2. Write incrementally — first 10 rows to disk as soon as you have them, then append. Do not hold everything until the end.
   If the output file already exists (a previous run was cut off), read it and add only the targets not yet in it.
3. Never invent a URL. Never guess "Yes".
4. Every target in your list gets a row, even if every cell is `Unknown`.
