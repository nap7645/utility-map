# plans/ — buildout beyond MISO + PJM

## What's here

| File | Purpose |
|---|---|
| `PLAYBOOK.md` | **Read first.** The generic 5-phase recipe for onboarding any region, plus every rule learned the hard way on MISO/PJM. Region files are deltas against this. |
| `prompts/presence_scan.md` | Sonnet. Has/doesn't-have, 4 cells, whole >10k denominator. |
| `prompts/programs.md` | Sonnet. Full 22-column rows for load-bearing utilities. |
| `prompts/interconnection.md` | **Opus.** State rules + utility deltas. |
| `prompts/wholesale.md` | **Opus.** RTO market products a BTM asset can reach. |
| `rto_*.md`, `region_*.md` | Per-region deltas: denominator quirks, load-bearing utilities, program families, gotchas, cluster splits. |
| `../.claude/skills/utility-program-research/` | The skill. Any agent invoking it gets the schema-reading, incremental-write, source-tier, and validation loop without being told each time. |

Prompt templates use `{{placeholders}}` filled from the region file. The skill is what makes an
agent behave the same way whether you invoke it here or from a fresh session.

## Recommended sequence

Ordered by insight per token, not by size. The binding constraint is the monthly spend limit, so
sequence matters more than it would otherwise.

| # | Region | Territories >10k | Est. tokens | Why here |
|---|---|---|---|---|
| 0 | **MISO/PJM finish** | 145 remaining | ~0.9M | Clusters C/D/F never ran. Closes a region already 87% done — cheapest completion on the board. |
| 1 | **NYISO** | ~25 | ~1.0M | Smallest denominator in the country, densest value stack. Cheapest full region, and the VDER/standby structures will teach the economics engine things it needs regardless of where you sell. |
| 2 | **ISO-NE** | ~70 | ~1.4M | ConnectedSolutions is the largest residential-battery dispatch program in the US and the clearest existence proof for the whole thesis. GMP is the second. High signal per utility. |
| 3 | **CAISO** | ~60 | ~1.4M | Biggest storage market, most mature policy. Deferred to #3 only because the numbers churn fastest — do it *after* staleness surfacing exists, or it rots. |
| 4 | **Southeast** | ~150 | ~1.8M | Large denominator, low program density, no wholesale layer. Cheap per utility because so many are TVA distributors. Duke PowerPair and FPL On Call are worth having. |
| 5 | **ERCOT** | ~120 | ~1.5M | **Blocked on Phase 4 (aggregators).** The presence model assumes the polygon is the program provider; in ERCOT's competitive area it isn't. Doing this before the `ViaAggregator` state exists produces a map that is confidently wrong. |
| 6 | **West** | ~180 | ~2.1M | Three sub-markets, ten PUCs, no RTO. Most expensive per unit of insight. Xcel CO and APS/SRP are the parts worth having early if you need them sooner. |
| 7 | **SPP** | ~120 | ~1.4M | Thinnest DR market of the seven; no capacity market. OG&E SmartHours is the one real prize. Defer unless the business is selling in KS/OK/NE. |

**Full national coverage ≈ 10.5M tokens across ~55 agents.** Budget one failed agent in five —
that's observed, not padding.

## Two structural decisions to make before spending on #4–#7

1. **Aggregator layer (Phase 4) first?** It gates ERCOT entirely and improves every other region's
   `res_dispatch` accuracy. Roughly 1–2 agents. Arguably belongs at #1.
2. **Staleness surfacing.** CA export rates and ISO-NE program-year rates go stale in months. Until
   `last_verified` visibly ages in the UI, every region added is a future wrong answer. Cheap to
   build, and it's already on the debt list in `PLAN.md`.

## Kicking off a region

```
1. Read plans/PLAYBOOK.md and the region file.
2. Phase 0 by hand: HIFLD pulls per state → data/raw/hifld_over10k_<region>.csv → split into
   40–60-utility target files.
3. Fill the prompt template's {{placeholders}} from the region file. Launch clusters in parallel.
4. Each agent: invoke the utility-program-research skill, then do its cluster.
5. Merge, alias, build, push, then open the live map and click three utilities you know.
```

## Honesty note on the region files

The market-structure facts in each region file (who serves where, which programs exist, which
G&T serves which co-ops) are from model knowledge as of mid-2026 and are **not verified**. They
are there to make the first agent fast, not to be trusted. Every region file says this; the first
agent in each phase should correct the file as it goes. On MISO/PJM the agents corrected me twice
— Central EPA was TVA rather than Cooperative Energy, and the Maryland storage pilots turned out
to be utility-owned assets rather than BYOD tariffs.
