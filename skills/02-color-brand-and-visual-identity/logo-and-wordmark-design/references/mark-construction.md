# Reference: Mark Construction — geometry, grid, lettering, and encoding the device

This is the *how* behind workflow steps 1–4 of `logo-and-wordmark-design`: how to fix a mark in
geometry so it is reproducible from rules (Rand), how to draw or specify a wordmark cut, and how
to make the geometry actually *carry* the distinctive device — Janoff's interactive wit / small
surprise, or the encoded USP — rather than decorate around it.

A mark you can only ship as a single exported PNG is not a mark; it is a screenshot. A mark
exists when a skilled hand could redraw it from the written rules alone.

---

## 1. Encode the device into the form (do this first — idea before execution)

The geometry exists to carry **one** idea. Decide which, then make the construction serve it.

### A. Interactive wit / a small surprise (the FedEx-arrow move)
A detail the viewer *discovers* — a dual reading, a figure/ground flip, a glyph substitution.

- **Negative-space carrier.** Reserve a counter or the gap between two forms to *be* the second
  reading (FedEx: the arrow lives in the space between E and x). Construct the two positive
  forms first; tune their spacing until the negative shape resolves cleanly. The surprise must
  be **inevitable once seen and invisible until seen** — if it needs a caption, it failed.
- **Substitution carrier.** Replace one element with a meaningful one (I♥NY: a heart for
  "love"). The substituted form must sit on the same optical grid as what it replaces so the
  lockup still reads as a unit.
- **Dual-reading silhouette.** One outline that reads as two related things depending on
  attention. Resolve it at silhouette stage (step 2 of the skill), never by adding detail.

Rule: the wit is **earned through one device**, metaphorical/subliminal, **never literal**
(Janoff). One surprise. A second "clever" detail cancels the first and reads as busy.

### B. USP-encoding (the rainbow-stripes move)
The mark's defining visual feature *is* the product's differentiator (Apple stripes = the Apple
II's colour-on-TV). State the USP in one sentence, then make a geometric property carry it:

- Map the USP to a *structural* property — a count, a direction, a join, an aperture, a rhythm —
  not a picture. ("Multi-source" → three converging strokes; "open/transparent" → an open
  counter that other marks would close.)
- The encoded property must survive monochrome and reduction; if the USP only reads in colour
  or at large size, it is decoration, not encoding.

If neither device is present after construction, stop — the mark is generic. Return to
silhouette iteration.

---

## 2. Choose the construction system

Pick the system that fits the mark's character; state it explicitly so it is reproducible.

| System | When | What you record |
|---|---|---|
| **Modular grid** (square units) | Geometric, engineered, "instrument" feel | Unit size; every stroke/curve as N units; corner radii in units |
| **Circle-and-line (compass)** | Classical, humanist, organic curves | Circle radii and centres; tangent points; line angles |
| **Ratio-driven** (golden, √2, musical) | Marks claiming proportion/harmony | The ratio; which dimensions it governs; derivation order |
| **Type-derived** | Wordmark/monogram from an approved face | Source face + weight; which contours are kept vs redrawn |

Most marks mix two (e.g. circle-and-line for the glyph, a unit grid for spacing). Record the
primary system and where the secondary takes over.

### What "reproducible" requires (write all of these down)
- **Base unit** and the bounding construction (the box/circle the mark is built inside).
- **Key ratios** — stroke weight : cap-height, counter : stem, mark : wordmark scale.
- **Stroke contrast** — monoline, or thick/thin and where the modulation falls.
- **Corner/terminal language** — radius value(s), cut angles, whether joints are filleted.
- **Construction order** — what is drawn first and what is derived from it (so a redraw lands in
  the same place).

---

## 3. Optical corrections (the part a grid alone gets wrong)

Mathematical centring and equal measures look *wrong* to the eye. A mark that is only
geometrically correct reads as stiff or lopsided. Apply and record:

- **Overshoot.** Round and pointed forms must extend slightly past the flat-form baseline/cap
  line (typically ~1–2% of cap-height) or they look small. Circles, triangles, the apex of an A.
- **Optical centring.** The optical centre sits slightly *above* the geometric centre; a mark
  centred by maths sits low. Nudge up.
- **Joint thinning.** Where strokes meet (the crotch of a V, the junction of a Y, a curve into a
  stem), ink pools darker; thin the join so weight reads even.
- **Stroke compensation.** Horizontal strokes look heavier than verticals of equal width; thin
  horizontals slightly. Curves need a touch more weight than straights to match.
- **Spacing is optical, not metric.** Equal gaps between letters/elements look unequal; space by
  *area* of the gap, not by measured distance (tight around round forms, open around verticals).

Record each correction as a rule ("round forms overshoot the cap line by 1.5%"), so it survives
a redraw.

---

## 4. The wordmark cut

A wordmark is custom lettering, not "the name typed in a font" — even when it starts from one.

### If drawn from an approved face (the common, defensible path)
1. Name the source face and weight (from `font-selection-and-pairing`); it should share the
   brand display type's skeleton so the wordmark and headings read as **one voice**.
2. Record **what you change and why** — usually a small, deliberate set:
   - Tighten tracking below the face's default (display lettering sits tighter than text).
   - Redraw **one** distinguishing detail: a terminal, a connection, a single counter, the
     crossbar of an A/e/t. This is the ownable mark inside the wordmark — make exactly one.
   - Equalise optical spacing letter-by-letter (kerning by area, §3).
   - Resolve awkward pairs (e.g. a clashing rn/m, a too-open To) bespoke.
3. Lock cap-height, x-height, and any ascender/descender adjustment as fixed values.

### If fully custom
- Build on one construction system (§2); keep stroke logic consistent across all glyphs.
- Draw the hardest letters first (a, e, g, s, and any glyph carrying the device); derive the
  rest to match.
- Test the word as a **shape** (squint until letters blur) — the silhouette must read as
  balanced and as the brand, before any letter is "right" in detail.

### Discipline
- One distinguishing detail, repeated logic — not a different idea per letter (Vignelli).
- The wordmark must survive being set small and in one colour (§ reduction below).
- Never let the cut drift into a banned face's defaults (`ai-slop-banned-fonts.md`); never ship
  AI-generated lettering (misspell/warp/fuse tells, `ai-slop-taxonomy.md`).

---

## 5. Monogram / glyph extraction

The monogram is the seed of the favicon and app icon (see
`app-icon-and-favicon-system.md`) — design it as a deliberate form, not a crop of the wordmark.

- Build it from the mark's strongest single element + (optionally) one letter.
- It must hold the device if at all possible (the surprise/USP carried even in the reduced form).
- Construct it inside the icon's safe zone from the start, not by shrinking the lockup.

---

## 6. The reduction test (Janoff's scale-relater)

Before sign-off, verify the mark *relates to its own scale* — that it still reads as itself,
not a smudge, at the small end:

1. Render the monogram at **16 px** (favicon). Is the device still legible, or has the surprise
   collapsed? If it collapses, simplify the glyph until it survives — drop detail, don't shrink
   uniformly ("edit for less").
2. Render in **one flat colour** (no gradient, no shadow). The form must hold.
3. Print/preview in **pure black on white and white on black**. Counters must not fill in;
   thin joins must not break.
4. Squint test at full size: the silhouette alone should be recognisable.

A mark that fails reduction is unfinished, however good it looks at hero size. Janoff: a strong
mark survives reduction, works in one colour, and is redrawable from memory.

---

## 7. Hand-off

The construction record (systems, base unit, ratios, optical corrections, wordmark
modifications, monogram) is what `logo-and-wordmark-design` packages into the mark+lockup spec
and what `brand-visual-identity` references in its Consistency Gate. Keep it rule-based and
redraw-proof — that is the difference between an authored mark and an exported image.
