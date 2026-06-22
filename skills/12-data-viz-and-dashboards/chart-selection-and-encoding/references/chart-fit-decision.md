# Reference: Chart-Fit Decision — Data → Message → Chart

The routing logic this skill owns: given the **data type** and the **message**, land on a
concrete chart type, then verify the encoding and accessibility. The *why* behind the channel
ranking (position > length > angle > area > hue) lives in the sibling
`data-visualization/references/chart-encoding.md` (Cleveland & McGill, *Graphical Perception*,
JASA 1984; Mackinlay, ACM ToG 1986) — cite it; this file does not restate it. Accessibility
floor: `doctrine/references/wcag-2.2-criteria.md`.

---

## 1. The selection order (always this sequence)

1. **Message before data shape.** The same dataset becomes a different chart depending on what
   the reader must *see or do*. "Region A is biggest" (comparison) → bar. "Sales are climbing"
   (trend) → line. Classify the message into one of the six families in §2 **first**.
2. **Data type gates the encoding channel.** Quantitative → position/length. Ordinal →
   single-hue intensity ramp. Categorical/nominal → hue/shape/position-in-small-multiples.
   Temporal → position along a continuous x-axis. Geographic → position on a map.
3. **Pick the chart from the message × data-type cell** (§3 table).
4. **Verify honesty** (§4) and **accessibility** (§5) before drawing.

---

## 2. The six message families

| Family | The reader question it answers | Default winning chart |
|---|---|---|
| **Comparison** | "Which is bigger / how do these rank?" | Sorted **horizontal bar** (1 series); grouped/small-multiple bars (2–3 series) |
| **Trend (time)** | "Is it going up or down over time?" | **Line** (continuous); **slopegraph** (two periods); column (few discrete periods) |
| **Distribution** | "How are values spread / where do they cluster?" | **Histogram** (one variable); **box / violin** (compare distributions); **dot/strip** (small n) |
| **Part-to-whole** | "What share is each part of the total?" | **100% stacked bar** or **sorted bar**; treemap for nested/many parts — **never pie/donut** |
| **Relationship** | "Do these two (or three) variables move together?" | **Scatterplot** (2 vars); **bubble** (3rd var as size, sparingly); connected scatter for time |
| **Geographic** | "How does it vary by place?" | **Choropleth** (rate/normalised by region); **graduated-symbol** (counts); **flat 2-D map only** |

> A message can be compound ("trend, by region"). Resolve it by the *primary* question, then add
> the secondary dimension via small multiples or one emphasised series — not by stacking encodings
> onto one busy chart.

---

## 3. Data-type × message routing table

| Data type ↓ / Message → | Comparison | Trend (time) | Distribution | Part-to-whole | Relationship |
|---|---|---|---|---|---|
| **Quantitative, 1 series** | Sorted horizontal bar | Line | Histogram | Sorted bar / 100% stacked bar | — |
| **Quantitative, 2–3 series** | Grouped bar / small multiples | Multi-line (≤3) or small multiples | Box / violin (compare) | Stacked bar (totals + parts) | Scatter (2 vars) / bubble (3) |
| **Quantitative, many series** | Small multiples | Small multiples (avoid spaghetti) | Box plots / ridgeline | 100% stacked bar | Scatter-matrix |
| **Ordinal** (low/med/high) | Bar in natural order | Line if also temporal | — | 100% stacked bar (Likert) | — |
| **Categorical / nominal** | Sorted bar (hue = identity only) | — | Dot plot | 100% stacked bar | Mosaic (use sparingly) |
| **Temporal** | Column (few periods) | **Line** (the default) | — | Stacked area (sparingly) | Connected scatter |
| **Geographic** | Bar (if place is just a category) | Small-multiple maps over time | — | — | Bivariate choropleth (rare) |
| **Two numbers only** | **Simple big text**, not a chart | — | — | — | — |

Rules baked into the table:
- **1–2 numbers → simple text**, never a chart (Knaflic).
- **More than ~3 lines** on a trend chart → small multiples or emphasise one (spaghetti fix).
- **Part-to-whole never routes to pie/donut** — the share comparison lands on angle/area (worst
  channels). Use 100% stacked bar (consistent baselines both ends) or a sorted bar of the parts.

---

## 4. Banned default → correct replacement (and the honesty rule it serves)

| Banned default | Why it's wrong | Correct replacement |
|---|---|---|
| **Pie chart** | Ranking forced onto angle/area | Sorted horizontal bar (position) |
| **Donut chart** | Worse — arc-length comparison | Sorted horizontal bar |
| **3-D bar / pie** | Volume/depth skews magnitude; floor-panel chart-junk | Flat 2-D bar |
| **Dual-axis combo** | Two scales fabricate any correlation (non-expressive) | Two panels sharing one x-axis, **or** direct-label the 2nd series |
| **Gauge / speedometer** | Needle = angle (poor); arc judgement on colour alone | **Bullet graph** (length + target tick) |
| **Rainbow heatmap** | Hue has no perceptual order | Single-hue light→dark sequential ramp |
| **Stacked area, many bands** | Only the bottom band is on a common baseline | 100% stacked bar or small-multiple lines |
| **Non-zero bar baseline** | Expresses a false ratio (Fox-News 460%-vs-13%) | Zero baseline (mandatory for bars) |

### Axis & scale honesty (Mackinlay expressiveness)
- **Bars / length encodings: zero baseline, always.** No exceptions.
- **Line / dot (position): clipped scale is permitted** if clearly labelled and not over-zoomed —
  position encodes change truthfully without a zero baseline.
- **Dual-axis: banned.** The secondary y-axis lets you choose two scales that imply a relationship
  not in the data. Split into panels on a shared x-axis or label the second series directly.
- **Consistent intervals** on a time axis (never mix years with decades).

---

## 5. Accessibility gate for the chosen chart

Full floor in `data-visualization/references/chart-encoding.md` §5 and
`doctrine/references/wcag-2.2-criteria.md`. The minimum, restated as checks:

- **Non-colour cue on every colour distinction** (WCAG 1.4.1): direct label, dash pattern, marker
  shape, texture, or +/− sign. Blue (positive) + orange (negative), never red+green; add a sign or
  arrow.
- **Contrast:** data marks ≥ **3:1** vs background and vs adjacent marks (1.4.11); chart text ≥
  **4.5:1** (≥3:1 for ≥24px / ≥18.66px-bold) (1.4.3). Design with APCA, certify with WCAG.
- **Colour-vision safety:** Okabe–Ito / ColorBrewer colourblind-safe categorical sets; single-hue
  ramp for ordered data; test in a deuteranopia/protanopia simulator.
- **Text alternative:** informative caption/`alt` (action title seeds it) + backing data table
  (1.1.1); interactive points keyboard-reachable with name/role/value (4.1.2), targets ≥
  **24×24px** (2.5.8); honour `prefers-reduced-motion`, no flash >3×/s; usable at **320px /
  200% zoom**.

---

## 6. Selection decision checklist

- [ ] Message classified into one of the **six families** *before* choosing a chart.
- [ ] Chart picked from the **data-type × message** cell, not from the data shape alone.
- [ ] Key comparison sits on the **highest-accuracy channel** available (position > length > … > hue) — verified against `data-visualization/references/chart-encoding.md` §1.
- [ ] No **banned default** (pie, donut, 3-D, gauge, dual-axis, rainbow); replacement applied if it crept in.
- [ ] **Zero baseline** on every bar/length encoding; clipped scales are position-only and labelled.
- [ ] **No secondary y-axis** — split into panels or direct-label.
- [ ] **Action title** states the so-what; every axis titled; key point annotated directly.
- [ ] **No meaning rides on colour alone**; a non-colour cue backs every distinction.
- [ ] Contrast ≥ 3:1 marks / ≥ 4.5:1 text; palette passes a CVD simulator.
- [ ] **Text alternative / data table** present; interactive targets keyboard-reachable and ≥ 24×24px.
