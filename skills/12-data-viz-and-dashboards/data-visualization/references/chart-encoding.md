# Reference: Perceptual Encoding & Accessible Charts

Why one chart reads instantly and another forces decoding. Knaflic's lessons (see `SKILL.md`)
say *what* to do; this reference gives the **perceptual ranking that explains why**, plus the
**accessibility floor** every chart must clear. Page-level dashboard composition (zones, drill,
real-time) belongs to the sibling **`dashboard-and-data-product-design`** — this file is about a
*single chart's* encoding and legibility.

Sources: Cleveland & McGill, *Graphical Perception* (JASA, 1984); Mackinlay, *Automating the
Design of Graphical Presentations* (ACM ToG, 1986); Munzner, *Visualization Analysis & Design*
(CRC, 2014); Ware, *Information Visualization* (Morgan Kaufmann, 2004). Accessibility floor:
`doctrine/references/wcag-2.2-criteria.md`.

---

## 1. The perceptual accuracy ranking (Cleveland–McGill / Mackinlay)

People decode some visual channels accurately and others poorly. Encode the **most important
quantity in the most accurate channel available**. Ranked **most → least accurate** for
*quantitative* (magnitude) data:

| Rank | Channel | Typical chart | Decode accuracy |
|---|---|---|---|
| 1 | **Position on a common scale** | Bar (shared baseline), dot plot, scatter | Best — use for the headline number |
| 2 | **Position on non-aligned scales** | Small multiples, side-by-side panels | Very good |
| 3 | **Length** | Bar length, slope of a line | Good |
| 4 | **Angle / slope** | Slopegraph, line direction | Moderate |
| 5 | **Area** | Bubble, treemap, square area | Poor — readers under-estimate big areas |
| 6 | **Volume / 3-D depth** | 3-D bar/pie | Very poor — never use for magnitude |
| 7 | **Colour intensity / saturation** | Heatmap, choropleth | Poor for exact values; ok for ordered "more/less" |
| 8 | **Colour hue** | Categorical series colour | **Not quantitative** — hue carries *identity*, not amount |

**Operational rule:** the more accurately a quantity must be compared, the higher up this list its
encoding must sit. A pie chart fails because it forces **angle + area** (ranks 4–5) onto the data's
single most important comparison; replacing it with a sorted horizontal bar moves that comparison
to **position on a common scale** (rank 1). This is the perceptual *reason* behind the SKILL's
"avoid pie / avoid 3-D / prefer bars" rules — not taste.

## 2. Match the channel to the data *type*

Encoding accuracy depends on what the data **is**:

| Data type | Use accurate channels | Avoid |
|---|---|---|
| **Quantitative** (amounts, ratios) | Position, length | Hue (carries no magnitude) |
| **Ordinal** (ranked: low/med/high) | Position, ordered single-hue intensity ramp | Multi-hue rainbow (no inherent order) |
| **Categorical / nominal** (identity) | Hue, shape, position in small multiples | Intensity (implies a false order) |

Two corollaries the SKILL already states, now grounded:
- **Hue is categorical, intensity is ordinal.** A single-hue light→dark ramp reads as a quantity;
  a rainbow does not (no perceptual ordering of hues), which is why heatmaps beat rainbow scales.
- **Don't double-encode for decoration.** Mapping the same variable to both length *and* hue adds
  ink without adding information (chart-junk, per the doctrine's Anti-Slop Charter).

## 3. Expressiveness & effectiveness (Mackinlay's two laws)

- **Expressiveness** — the encoding must state *all and only* the facts in the data. Example
  violation: a bar chart with a non-zero baseline *expresses* a false ratio (the Fox News 460%-vs-
  13% case in the SKILL). Length encodings therefore **require a zero baseline**; position
  encodings (line, dot) may use a clipped scale if labelled.
- **Effectiveness** — among expressive options, pick the one highest on the §1 ranking for the
  most important variable. This is the formal version of "choose the easiest-to-read chart."

## 4. Pre-attentive processing (why hierarchy works in <250 ms)

A small set of channels are processed *pre-attentively* — the eye finds the odd one out before
conscious thought (Ware). The usable ones for charts: **hue, intensity, size, orientation,
position, enclosure, added marks.** Design implication, matching SKILL Lesson 4:
- Push everything to a neutral grey **first**, then promote exactly one element with **one**
  pre-attentive channel. One pop = instant focus; five pops = no focus.
- Pre-attentive search only works on **one** channel at a time. If the highlight must survive
  greyscale printing or colour-blind vision, pair the colour pop with a **second, non-colour**
  channel (weight, label, marker) — see §5.

## 5. Accessible charts — the non-colour-cue rule

Colour alone must **never** be the only carrier of meaning (WCAG 1.4.1 Use of Colour). ~8% of men
have red–green colour-vision deficiency. Every chart must pass these, per
`doctrine/references/wcag-2.2-criteria.md`:

### Redundant (non-colour) encoding — always
- **Direct labels** instead of a colour legend (also a declutter win — SKILL Lesson 3).
- **Line charts:** vary **dash pattern / marker shape / line weight**, not just hue, when ≥2
  series must be told apart in greyscale.
- **Categorical fills:** add **texture / pattern / a leading icon or label**, or simply reduce to
  the one series that matters and grey the rest.
- **Positive vs negative:** never rely on red/green. Use **blue (positive) + orange (negative)**
  *and* a sign or directional arrow (SKILL's backup-cue rule).

### Contrast (the measurable floor)
- **Graphical objects & UI components** that convey meaning — bars, lines, key points, the legend
  swatch — need **≥ 3:1** against their background and against *adjacent* data marks (WCAG 1.4.11).
- **Text** in titles, axis labels, annotations, data labels — **≥ 4.5:1** (≥ 3:1 for large text
  ≥24px / ≥18.66px bold) (WCAG 1.4.3).
- Adjacent slices/segments/series that touch must be **≥ 3:1 from each other**, not just from the
  background — otherwise the boundary disappears.
- **Design with APCA** for real perceptual legibility, then **certify with the WCAG ratio** for
  conformance (it is the conformance test; APCA is the WCAG 3.0 *draft* tool).

### Colour-vision safety
- Test every palette in a **deuteranopia/protanopia simulator** before shipping.
- Prefer a **colour-blind-safe categorical set** (e.g. Okabe–Ito 8-colour, or ColorBrewer
  "colorblind-safe" sets). For ordered data use a **single-hue sequential ramp**, never rainbow.
- Source the actual scales from the sibling
  `02-color-brand-and-visual-identity/color-system-and-palette` (it owns categorical/sequential
  ramp construction and the contrast gate); this file owns *how the chart uses them*.

### Beyond colour — the rest of the a11y floor for charts
- **Text alternative:** every chart needs an informative `alt`/caption stating the takeaway, and
  ideally an accessible **data table** behind it (WCAG 1.1.1). The action title is the start of it.
- **Keyboard & tooltips:** interactive points/tooltips must be reachable by keyboard and expose
  name/role/value (4.1.2); tap/hover targets ≥ **24×24 px** (2.5.8).
- **Motion:** entrance/transition animation honours `prefers-reduced-motion`; nothing flashes
  >3×/s (2.3.1/2.3.3).
- **Reflow:** the chart stays usable at **320px width / 200% zoom** (1.4.10/1.4.4) — see
  `responsive-mobile-charts.md` for how to re-encode rather than shrink.

## 6. Encoding decision checklist

- [ ] Most important quantity is on the **highest-ranking channel** available (position > length > … > hue).
- [ ] Channel matches data **type** (quantitative→position/length; ordinal→intensity ramp; nominal→hue).
- [ ] Length encodings (bars) have a **zero baseline**; clipped scales are position-only and labelled.
- [ ] Exactly **one** pre-attentive pop carries the focus; everything else is neutral grey.
- [ ] Meaning never depends on colour alone — **a non-colour cue** (label, dash, shape, pattern, sign) backs every colour distinction.
- [ ] Data marks ≥ **3:1** vs background and vs adjacent marks; chart text ≥ **4.5:1**.
- [ ] Palette passed a **colour-blind simulator**; sequential data uses a single-hue ramp, not rainbow.
- [ ] Chart has an informative **text alternative / data table**; interactive targets keyboard-reachable and ≥ 24×24px.
