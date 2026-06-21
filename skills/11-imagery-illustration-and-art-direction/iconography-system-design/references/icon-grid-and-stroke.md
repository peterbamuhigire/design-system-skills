# Icon Grid & Stroke — construction reference

The real geometry of a typographic-grade icon system: the grid, the keylines, the stroke
system, the corner/cap/join language, the optical-balance corrections, and the small-size
pixel-fitting rules. Numbers below are stated on a **24px base grid** (the de-facto UI
standard); scale proportionally for other bases and re-snap to the pixel grid.

This reference is the canonical geometry for `iconography-system-design`. It exists so that a
glyph drawn next week sits on the same grid, at the same stroke, as one drawn today — which is
the whole point of a *system*. See `doctrine/design-doctrine.md` §2: state the choice, then
apply it everywhere.

---

## 1. The grid

| Element | Value (24px base) | Notes |
|---|---|---|
| **Artboard** | 24 × 24 px | The viewBox. Everything exports normalized to this. |
| **Outer padding (trim)** | 2 px each side | Reserves breathing room; nothing critical touches the edge. |
| **Live area** | 20 × 20 px | Where the glyph is drawn. (Some systems use 1px trim → 22×22; **pick one and state it**.) |
| **Pixel grid** | 1 px | All key edges and stroke centers snap to whole or half pixels. |

**Why padding matters:** without a reserved trim, a full-bleed square icon (image, stop)
renders visually *larger* than a circular one (clock) that naturally inset itself. The padding +
keyline system is what equalizes them.

### Keyline shapes (the size governors)

Place every glyph against **one** keyline so glyphs of different silhouettes read at the same
size. Typical keylines inside a 20px live area:

| Keyline | Size (px) | Use for glyphs that are… | Examples |
|---|---|---|---|
| **Square** | 18 × 18 | boxy, full | image, grid, stop, calendar |
| **Circle** | 20 Ø | round | clock, user-head, globe, record |
| **Rect (landscape)** | 20 × 16 | wide | document-wide, card, panorama |
| **Rect (portrait)** | 16 × 20 | tall | phone, document-tall, bookmark |

A circle keyline is **larger** (20) than the square keyline (18) on purpose — see optical-area
compensation (§4). Assign each glyph in the set to a keyline in the spec; an unassigned glyph
is an off-grid glyph.

---

## 2. The stroke system

| Property | Value (24px base) | Rule |
|---|---|---|
| **Nominal stroke** | **2 px** (≈ 1/12 of artboard) | **Constant across every glyph at a given size.** |
| **Corner radius (outer)** | 2 px | Inner radius = outer − stroke (so a 2px stroke with 2px outer ≈ 0–0.5px inner). State one value. |
| **Cap** | round *or* butt | Pick one (round = friendlier; butt = sharper). Apply everywhere. |
| **Join** | round *or* miter | Round joins pair with round caps; miter with butt. Don't mix. |
| **Terminal** | closed *or* open | If you adopt an open-terminal signature, apply it to every applicable glyph. |

**The constant-stroke law.** A busy glyph (e.g. *settings* gear) does **not** get a thinner
stroke to fit — you **simplify the glyph** (fewer teeth, larger negative space) until 2px fits
the live area. Thinning the stroke for one icon is the loudest "assembled from three libraries"
tell.

### Per-size scaling + hinting table

Stroke scales proportionally but must **snap to the pixel grid** so it stays crisp:

| Render size | Proportional stroke | **Hinted stroke (use this)** | Notes |
|---|---|---|---|
| 48 px | 4.0 px | 4 px | clean ×2 of base |
| 32 px | 2.67 px | 2.5 px | snap up |
| **24 px (base)** | **2.0 px** | **2 px** | master |
| 20 px | 1.67 px | 1.5 px | snap to half-pixel |
| 16 px | 1.33 px | 1.5 px (redrawn) | **redraw**, don't shrink — see §5 |

---

## 3. Corner, terminal & geometry language

- **One radius vocabulary.** Decide the outer corner radius (e.g. 2px) and the rule for where
  sharp vs rounded corners appear (e.g. *outer corners rounded, inner notches sharp*). Apply
  identically to every glyph.
- **Angle discipline.** Constrain diagonals to a small set (commonly **45° only**, or 45°/30°
  for arrowheads). A chevron, a "send" arrow, and a "share" node must share the same angle.
- **Counter sizes.** Interior holes (the eye of a *view* icon, the dot of a *info* icon) use a
  consistent minimum so they don't fill in at small sizes (≥ 2px at 24px base).

---

## 4. Optical balance — the corrections that matter

Mathematical (bounding-box) construction looks wrong. Compensate for perception:

### Area compensation
Shapes of equal bounding box are **not** equal perceived mass. Overshoot/inset to equalize:

| Shape | Correction vs a reference square | Why |
|---|---|---|
| **Square** | reference (e.g. 18px) | densest fill for its box |
| **Circle** | **+~10–12%** (e.g. 20Ø) | a circle vacates its corners, reads smaller |
| **Triangle** | **+~10–15%**, overshoot apex | even less area than a circle |
| **Horizontal bar** | match by thickness, not box | wide shapes read heavier |

### Optical centering
Center on the **visual center of mass**, not the bounding box:

- **Play triangle:** nudge **right** by ~1–1.5px (its mass sits left of bbox center).
- **Asymmetric glyphs** (speech bubble with a tail, magnifier with a handle): center the *body*,
  let the appendage overhang.
- **Caret/chevron:** balance the optical weight of the two arms, not the bbox.

### Stem & edge alignment
- Vertical/horizontal stems snap to the pixel grid so 1–2px strokes stay sharp.
- Equalize the **gap** in repeated elements (the bars of a list/menu icon are evenly spaced by
  eye, with equal end-padding to the live area).

Document each compensation per glyph in the set spec — undocumented optical fixes get
"corrected" back to math-grid by the next editor.

---

## 5. Small-size pixel-fitting (16–20px)

- **Redraw, don't shrink.** The 16px icon is a *new master*: drop non-essential detail,
  increase relative stroke (1.5px feels like 2px@24), open up counters so they don't fill.
- **Snap to whole/half pixels.** Stroke centers on whole or half pixels; key edges on whole
  pixels. Avoid 1px features that land on a fractional boundary and blur.
- **Test on a real background** at 1× and 2× DPR — a glyph that's crisp at 2× can mud at 1×.

---

## 6. Export & accessibility hooks

- **Normalize** every glyph to the 24px viewBox; strip editor metadata.
- **`currentColor`** — icons are monochrome by default and inherit text color (theming +
  dark-mode for free). No hard-coded fills.
- **Naming taxonomy** — `category-name[-modifier]`, kebab-case: `action-search`,
  `media-play`, `status-warning-fill`. No synonyms (`bin`/`trash`/`delete` → pick one).
- **A11y** — meaningful icon needs a label / `aria-label`; decorative icon is `aria-hidden`;
  the *control* around an icon meets the 24×24px target (WCAG 2.2 **2.5.8**); never carry
  meaning by color alone (**1.4.1**). See `doctrine/references/wcag-2.2-criteria.md`.

---

## Provenance
Geometry follows established icon-grid practice (24px UI grid, keyline shapes, optical
compensation) as documented in design-system iconography literature and applied per the Chwezi
anti-slop doctrine (`doctrine/design-doctrine.md`). Numbers are stated for a 24px base and are
the canonical values for `iconography-system-design`.
