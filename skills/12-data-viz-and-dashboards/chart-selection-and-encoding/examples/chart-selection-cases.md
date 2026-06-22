# Worked Example: Right Chart for the Message — Six Selection Cases

One case per message-family, each shown **wrong chart → right chart**, routed through the
**data-type × message** logic in `references/chart-fit-decision.md`. The perceptual *why* (the
position > length > angle > area > hue ranking) is cited from the sibling
`data-visualization/references/chart-encoding.md` §1 — this example is about the *type-selection*
decision, not the drawing craft. Accessibility cites `doctrine/references/wcag-2.2-criteria.md`.

Copy the **reasoning pattern**, not the numbers. No lorem.

---

## Case 1 — Comparison: pie → sorted horizontal bar

**Data:** revenue share across 6 regions (EMEA 31, AMER 27, APAC 19, LATAM 12, MEA 7, ANZ 4).
**Message family:** *comparison* — "which region is biggest, and how do they rank?"

**Wrong — pie chart.** The ranking comparison is forced onto **angle + area** (ranks 4–5, the
worst-decoded channels). EMEA 31 vs AMER 27 is near-indistinguishable as wedges; a colour legend
adds a matching tax.

**Right — sorted horizontal bar, direct-labelled.**
```
EMEA   ████████████████████████████ 31%
AMER   █████████████████████████ 27%
APAC   █████████████████ 19%
LATAM  ███████████ 12%
MEA    ██████ 7%
ANZ    ███ 4%
```
Routing: *categorical × comparison* → sorted bar. The comparison moves to **position on a common
scale** (rank 1); sorting makes rank instant; bars start at **zero** (length honesty). Hand to
`data-visualization` for grey-base + one-accent emphasis.

---

## Case 2 — Trend: dual-axis combo → two panels on one x-axis

**Data:** monthly revenue ($M) and conversion rate (%) over 12 months.
**Message family:** *trend* — "how do both move over the year?"

**Wrong — bars (revenue) + line (rate) on a secondary y-axis.** **Dual-axis is banned**: choosing
the two scales lets you manufacture any crossover (non-expressive, Mackinlay). The reader must
also work out which series maps to which axis.

**Right — two panels sharing one x-axis** (small multiples, rank 2):
```
Revenue $M   ▁▂▃▃▄▅▅▆▇▇██
Conv. rate % ▃▃▄▄▄▅▅▅▆▆▆▆     ← same 12 months beneath, one shared time axis
```
Routing: *temporal × trend, 2 series of different units* → split panels, not one chart. Each
series keeps an honest scale; the reader compares shapes over the same time with no axis puzzle.

---

## Case 3 — Distribution: stacked bar of averages → histogram + box plot

**Data:** support-ticket resolution times (minutes) for 2,000 tickets across 3 teams.
**Message family:** *distribution* — "how is resolution time spread, and where do teams differ?"

**Wrong — a bar chart of each team's *average* resolution time.** A mean hides the shape: a team
with a fat tail of 6-hour tickets can show the same average as a tight, predictable team.
Averages answer a *comparison* question, not a *distribution* one.

**Right — a histogram** for the overall shape, and **side-by-side box plots** to compare teams:
```
Team A  ├──[  ▮▮▮  ]────┤      (tight, low median)
Team B  ├────[ ▮▮▮▮ ]──────┤   (wider spread)
Team C  ├──[ ▮▮ ]──────────●   (long upper tail / outliers)
```
Routing: *quantitative × distribution, compare groups* → histogram (one var) + box/violin
(compare). Now spread, median, and outliers are visible — the actual message.

---

## Case 4 — Part-to-whole: pie → 100% stacked bar

**Data:** budget split across 4 cost centres, this year vs last year.
**Message family:** *part-to-whole* — "what share does each take, and did the mix shift?"

**Wrong — two pie charts side by side.** Comparing a slice *between* two pies means comparing two
angles across charts — almost impossible. Part-to-whole **never routes to pie**
(`chart-fit-decision.md` §3).

**Right — two 100% stacked bars** (one per year), shared 0–100% scale:
```
Last yr  [ Eng 45% | Sales 25% | Ops 20% | G&A 10% ]
This yr  [ Eng 40% | Sales 30% | Ops 20% | G&A 10% ]
```
Routing: *categorical × part-to-whole, two periods* → 100% stacked bar. Both ends share a common
baseline, so each share is on **position**; the Sales growth and Eng shrink read directly.

---

## Case 5 — Relationship: grouped bar → scatterplot

**Data:** 40 stores, each with marketing spend and monthly sales.
**Message family:** *relationship* — "does more spend go with more sales?"

**Wrong — a grouped bar chart** of spend and sales per store. 40 stores × 2 bars = 80 bars; the
*co-movement* of the two variables is invisible because bars encode each variable separately.

**Right — a scatterplot**, spend on x, sales on y, one dot per store:
```
sales │            ·   ·
      │        · ·   ·
      │     ·  ·  ·
      │  · ·  ·
      └─────────────────── spend
```
Routing: *two quantitative vars × relationship* → scatter. Both variables map to **position**
simultaneously; the upward cloud shows the correlation, and outliers (high spend, flat sales) pop.

---

## Case 6 — Geographic: 3-D prism map → flat choropleth

**Data:** infection rate per 100k across 30 districts.
**Message family:** *geographic* — "which districts are worst hit?"

**Wrong — a 3-D "prism" map** extruding each district by its value. Depth/volume (rank 6) is the
worst magnitude channel; tall front prisms **occlude** shorter ones behind them, and the tilt
distorts area — the message is literally hidden.

**Right — a flat 2-D choropleth**, single-hue light→dark ramp keyed to *rate* (normalised, not
raw counts):
```
 ░░ low   ▒▒ med   ▓▓ high   ██ highest      (single-hue sequential)
```
Routing: *geographic × rate* → choropleth (normalised), flat 2-D only. Intensity is read as
ordered "more/less"; verify each step ≥ 3:1 from its neighbour and a backing data table for the
exact values (WCAG 1.1.1 / 1.4.11). Use graduated symbols instead if the message is *counts*.

---

## The selection reasoning pattern (reuse this, not the numbers)

For every chart, in order:
1. **What is the message family?** comparison · trend · distribution · part-to-whole ·
   relationship · geographic. The message — not the data shape — picks the chart.
2. **Route data-type × message → chart** via `chart-fit-decision.md`; reject any banned default
   and apply its replacement.
3. **Is the key comparison on the highest-accuracy channel?** (position > length > … > hue, per
   `data-visualization/references/chart-encoding.md` §1.)
4. **Is the encoding honest?** zero baseline for bars; no dual-axis fabrication; clipped scales
   labelled and position-only.
5. **Action title + annotation** state the so-what.
6. **Accessible?** non-colour cue on every distinction; ≥3:1 marks / ≥4.5:1 text; CVD-safe
   palette; text alternative / data table.

Each "right" choice is an *authored, stated* decision with a reason — the doctrine's moat — not
the tool's reflexive default.
