# Worked Example: Good vs Bad Chart Encodings

Five real chart decisions, each shown **bad → good** with the perceptual and accessibility reason.
The reasoning cites `references/chart-encoding.md` (perceptual ranking, a11y floor) and the
`SKILL.md` lessons. This is the applied artifact the hardening plan requires — copy the *reasoning
pattern*, not the numbers.

Brief used throughout: a quarterly revenue review for a regional sales lead (the decision maker),
to be **circulated as a PDF** (audience controls pacing → label everything directly).

---

## Example 1 — Market share: pie → sorted horizontal bar

**Data:** share of revenue across 6 regions (EMEA 31, AMER 27, APAC 19, LATAM 12, MEA 7, ANZ 4).

**Bad — pie chart.**
```
        ╭───────╮
     ╱EMEA  AMER ╲      6 wedges, a colour legend off to the side,
    │  31%    27% │     percentage labels crammed on each slice.
     ╲APAC  LATAM╱
        ╰─MEA ANZ╯
```
Why it fails: the core comparison (which region is bigger?) is forced onto **angle + area**
(ranks 4–5 in `chart-encoding.md` §1) — the two channels people decode *worst*. EMEA 31 vs AMER 27
is nearly indistinguishable as wedges. A separate legend adds a colour-matching tax (SKILL Lesson 3).

**Good — horizontal bar, sorted descending, direct-labelled.**
```
EMEA   ████████████████████████████ 31%
AMER   █████████████████████████ 27%
APAC   █████████████████ 19%
LATAM  ███████████ 12%
MEA    ██████ 7%
ANZ    ███ 4%
```
Why it works: moves the comparison to **position on a common scale** (rank 1). Sorting makes rank
instant; labels sit at the bar end (no legend); bars start at **zero** so length is truthful
(Mackinlay expressiveness). One accent bar could highlight the region under discussion; the rest grey.

---

## Example 2 — Revenue trend: dual-axis combo → two stacked panels

**Data:** monthly revenue ($M) and conversion rate (%) over 12 months.

**Bad — bars (revenue) + line (rate) on a secondary y-axis.** The reader must first work out which
series maps to which axis, then mentally rescale. Dual-axis lets you *manufacture* any crossover by
choosing the two scales — it is non-expressive (it can imply a correlation that isn't in the data).

**Good — two panels sharing one x-axis** (small multiples, rank 2):
```
Revenue $M   ▁▂▃▃▄▅▅▆▇▇██
Conv. rate % ▃▃▄▄▄▅▅▅▆▆▆▆      ← same months beneath, one shared time axis
```
Each series keeps its own honest scale; the reader compares *shapes over the same time* without an
axis-matching puzzle. (SKILL: "label directly or split into two graphs.")

---

## Example 3 — Series colour: red/green only → colour + non-colour cue

**Data:** actual vs prior-year, two lines.

**Bad — green line "this year", red line "last year", legend only.** ~8% of men (red–green CVD)
see two near-identical muddy lines; in greyscale (this PDF may be printed) they're identical.
Violates **WCAG 1.4.1 (use of colour)** — meaning carried by hue alone.

**Good — blue solid "this year" + grey dashed "last year", both direct-labelled at the line end.**
```
This year  ───────────●  (blue, solid)
Last year  ─ ─ ─ ─ ─ ─○  (grey, dashed)
```
Two redundant cues — **hue *and* dash pattern *and* the end label** (`chart-encoding.md` §5). Survives
colour-blind vision and B&W print. Blue-positive / orange-negative would extend the same rule to
variance bars.

---

## Example 4 — "Health" scale: rainbow → single-hue sequential ramp

**Data:** a heatmap of revenue by region × month.

**Bad — rainbow (blue→green→yellow→red).** Hue has **no perceptual order** (`chart-encoding.md` §2),
so the reader can't tell whether green is more or less than yellow without constant legend trips;
rainbow also creates false banding at hue boundaries.

**Good — single-hue light→dark sequential ramp** (e.g. light→dark teal). Intensity *is* perceived
as ordered (rank 7, but used correctly for *ordinal* "more/less"), so darker = more reads without
the legend. Verify each step is **≥ 3:1** from its neighbour and the cell text is **≥ 4.5:1**
(WCAG 1.4.11 / 1.4.3); pull the actual ramp from the `color-system-and-palette` sibling.

---

## Example 5 — KPI tile: gauge → bullet graph (dashboard context)

**Data:** quarter-to-date revenue $4.2M against a $5.0M target, on a dashboard tile.

**Bad — speedometer gauge.** Huge ink for a single value, the needle angle is **angle encoding**
(poor), and the coloured arc (red/amber/green) carries the "are we ok?" judgement on **colour
alone**. Classic "dashboard decoration" slop (`ai-slop-taxonomy.md`).

**Good — bullet graph** (`references/dashboard-patterns.md` §3):
```
Revenue QTD                     ▎target
  ░░░░░▒▒▒▒▒▓▓▓▓▓█████████████  ┃        $4.2M / $5.0M
  poor    ok      good
```
One thrifty bar = actual (**length**, rank 3), a tick = target (**position**, rank 1 for the
"hit it?" judgement), greyscale bands = context. The bands are distinguishable **without colour**
(a11y), and it tiles consistently next to other bullet tiles (`dashboard-patterns.md` §4).

---

## The reasoning pattern (reuse this, not the numbers)

For every chart, ask in order:
1. **What is the single most important comparison?** → put it on the **highest-ranking channel**
   available (position > length > angle > area > hue).
2. **Does the encoding tell only the truth?** → zero baseline for length; no dual-axis fabrication
   (expressiveness).
3. **Does any meaning ride on colour alone?** → add a non-colour cue (label, dash, shape, sign).
4. **Will it survive greyscale, colour-blind vision, and 200% zoom?** → check ≥3:1 marks /
   ≥4.5:1 text; run a CVD simulator.
5. **Is exactly one thing highlighted?** → grey everything else; one pre-attentive pop.

Each "good" version above is an *authored* choice with a stated reason — the doctrine's moat —
rather than the tool's reflexive default.
