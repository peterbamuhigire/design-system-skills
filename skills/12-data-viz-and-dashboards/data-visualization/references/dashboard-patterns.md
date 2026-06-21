# Reference: Charts-in-Dashboards Patterns

How an *individual chart* should behave when it lives inside a dashboard tile rather than standing
alone in a report. **Scope boundary:** page-level dashboard design — zone sequence, layout
archetypes, KPI tiering, drill-down, cross-filtering, real-time/streaming UX — is owned by the
sibling **`12-data-viz-and-dashboards/dashboard-and-data-product-design`**
(`references/dashboard-layout-patterns.md`, `references/kpi-hierarchy.md`). Read that for the page.
This file covers only the **per-chart** decisions inside a tile.

Grounding: Few, *Information Dashboard Design* (Analytics Press, 2006); Knaflic, *Storytelling with
Data* (the `SKILL.md` framework); perceptual ranking in `chart-encoding.md`.

---

## 1. The dashboard changes the chart's job

A report chart argues one explanatory story (Knaflic Lesson 6). A dashboard tile **monitors** —
it answers "is this normal?" at a glance, repeatedly, in a few square centimetres. Consequences:

- **One question per tile, one chart per question.** If a tile needs two messages, it is two tiles.
- **Glanceable first.** The tile must resolve in the 3–8 second window (SKILL Lesson 4) *without*
  a title read — the encoding does the work; the title confirms it.
- **Comparison is the value.** A number alone ("Revenue 1.2M") is nearly useless; a number against
  a **reference** (target, prior period, forecast) is the insight. Always encode the comparison.

## 2. Tile chart-type selection (small-space rules)

| Tile question | Chart | Why (per `chart-encoding.md`) |
|---|---|---|
| "What's the current value vs target?" | **Big number + delta + sparkline** | Position+length; sparkline gives trend in one line |
| "Up or down over time?" | **Sparkline / line** | Slope (rank 4) is enough for direction; cheap on space |
| "How do a few categories compare?" | **Horizontal bar, sorted** | Position on common scale (rank 1) |
| "Are we inside a healthy range?" | **Bullet graph** (Few) | Bar + reference marker + qualitative bands; beats a gauge |
| "Part-to-whole, 2–3 parts?" | **100% stacked horizontal bar** | Shared baselines both ends; avoids the donut |
| "Status across many items?" | **Status chips / small heatmap** | Pre-attentive intensity/enclosure; pair with icon (a11y) |

**Banned in tiles** (carry the SKILL anti-patterns into the small space): **gauges/speedometers**
(huge ink, one number — use a bullet graph), **donuts/pies**, **3-D anything**, **dual-axis**
combos, and **rainbow** status palettes. These are the classic "dashboard decoration" slop tells
named in `doctrine/references/ai-slop-taxonomy.md`.

## 3. Sparklines & bullet graphs (the two dashboard-native marks)

- **Sparkline** — a word-sized line, no axes, optional end-dot + end-value. Use for trend-at-a-
  glance beside a headline number. Keep it light grey; mark only the latest point. Never add
  gridlines or a legend (defeats the form).
- **Bullet graph** (Stephen Few's gauge replacement) — a single horizontal bar = actual value, a
  perpendicular tick = target, 2–3 grey background bands = qualitative ranges (poor/ok/good).
  Encodes value, target, and context in one glanceable, ink-thrifty mark. Make the bands
  greyscale-distinguishable (a11y) — they must not rely on colour alone (`chart-encoding.md` §5).

## 4. Consistency across tiles (the authored-vs-slop line)

The doctrine's moat is "looks human-made." On a dashboard that shows up as **ruthless
consistency**:

- **Same comparison treatment** everywhere — if one tile shows "vs target" with a delta chip, all
  comparable tiles do. Mixed comparison styles read as unauthored.
- **Same colour semantics** board-wide — one accent means one thing on every tile; status colours
  (and their non-colour cue) are identical across tiles. A colour that means "good" here and
  "selected" there is the cardinal dashboard inconsistency.
- **Same title position & chrome** (upper-left titles, same padding) — see the sibling's tile-chrome
  rules; the point here is the *chart inside* must align to the same baseline grid and not invent
  its own margins.
- **Shared axis ranges** when tiles will be compared — two trend tiles with different y-scales
  invite a false read; lock the scale or label the difference loudly.

## 5. Tile states are part of the chart (not an afterthought)

Every tile chart must define its **loading / empty / stale / error** appearance — the *page-level*
mechanics (skeletons, freshness timestamps, throttling) live in the sibling reference, but the
**chart-level** contract is:
- **Empty ≠ zero.** "No data" must look different from "the value is 0." Don't render a misleading
  flat-zero bar for missing data.
- **Stale data** must visibly mark itself (dim / "as of" note) — a confident-looking chart on old
  numbers launders staleness into false trust.
- **Reduced motion / stable layout** — value transitions honour `prefers-reduced-motion`; the tile
  must not reflow on refresh (per `wcag-2.2-criteria.md`).

## 6. Charts-in-dashboards checklist

- [ ] Tile answers **one** question with **one** chart; comparison/reference is encoded, not just the raw number.
- [ ] Chart resolves glanceably in 3–8s; encoding (not the title) carries the read.
- [ ] No gauge/donut/pie/3-D/dual-axis/rainbow in the tile.
- [ ] Sparkline/bullet-graph used where a headline trend or value-vs-target is the question.
- [ ] Comparison treatment, colour semantics, title position, and (where compared) axis ranges are **consistent across all tiles**.
- [ ] Status/health uses a non-colour cue (icon/shape/label) alongside colour (`chart-encoding.md` §5).
- [ ] Empty / stale / error states defined at chart level; reduced-motion honoured; no reflow on refresh.
- [ ] Page-level concerns (layout archetype, drill, cross-filter, real-time UX) deferred to **`dashboard-and-data-product-design`**.
