# Reference: OpenType Features — Ligatures, Sets, Numerals, Caps, Fractions, and the CSS

OpenType features are typographic behaviours the foundry built into the font and that almost no
generated output ever switches on. Turning the right ones on — and choosing the **right numerals**
— is a cheap, high-signal way to make a UI look authored rather than defaulted. Each feature has a
four-letter tag; prefer the high-level CSS property where one exists, and fall back to
`font-feature-settings` only for `ssNN`, custom, or unsupported features.

> **Golden rule:** a feature only works if the font actually contains it. CSS never *creates*
> small caps, ligatures, or alternate digits — it only *activates* what is in the file. If nothing
> changes, the face doesn't ship that feature (or subsetting stripped it — see end).

---

## Numerals — the matrix that matters most

Digits have **two independent choices**. Getting these wrong is the most common data-UI bug.

**1. Spacing: tabular vs proportional**

| | Tag | Each digit's width | Use for |
|---|---|---|---|
| Tabular | `tnum` | equal (monospaced digits) | **tables, dashboards, KPIs, prices, timers, code, IDs** — columns stay aligned |
| Proportional | `pnum` | natural (a "1" is narrower than "8") | running prose, headlines |

**2. Height: lining vs old-style (text figures)**

| | Tag | Shape | Use for |
|---|---|---|---|
| Lining | `lnum` | all digits cap-height, sit on baseline | UI, all-caps, anything with capitals, technical contexts |
| Old-style | `onum` | varying heights with ascenders/descenders (3,4,5,7,9 dip) | literary/editorial **body** set in lowercase prose — digits blend with the text |

These combine: a financial table is `tnum lnum`; a magazine paragraph is `pnum onum`.

```css
/* high-level property — preferred */
.table-cell  { font-variant-numeric: tabular-nums lining-nums; }   /* aligned, cap-height */
.prose       { font-variant-numeric: proportional-nums oldstyle-nums; }
.code, .id   { font-variant-numeric: tabular-nums lining-nums; }

/* equivalent low-level, only if the property isn't honoured */
.table-cell  { font-feature-settings: "tnum" 1, "lnum" 1; }
```

**Defaults are a trap.** Most fonts default to proportional lining. A dashboard left at the default
shows jittering, mis-aligned numbers. **Tabular is the correctness default for any data layer** —
set it explicitly. Old-style numerals inside all-caps or UI chrome look like dropped digits — use
lining there.

## Ligatures

| Kind | Tag | Default? | Guidance |
|---|---|---|---|
| Standard | `liga` | on | leave on (fi, fl, ffi). Disable **only** in monospace/code where each glyph must be discrete. |
| Contextual | `clig` | on | leave on. |
| Discretionary | `dlig` | off | accent only (st, ct flourishes) — headlines/wordmarks, never body. |

```css
.code     { font-variant-ligatures: none; }              /* discrete glyphs for code */
.headline { font-variant-ligatures: discretionary-ligatures; }
```

## Contextual alternates (`calt`)

Swaps glyphs based on neighbours so shapes flow naturally (and, in some code faces, builds the
arrow/`=>` ligatures). On by default in most faces — keep it on. It is part of why script and
humanist faces look hand-set.

```css
.brand { font-feature-settings: "calt" 1; }   /* usually already on; assert if you rely on it */
```

## Stylistic sets (`ss01`..`ss20`) — adopt exactly one as a signature

A stylistic set is a foundry-curated bundle of alternate glyphs (a single-storey `a`, a
straight-leg `R`, a different `g`). They are **off by default** and there is no high-level property
— `font-feature-settings` only. The craft move is to adopt **one** set that fits the brand voice,
name it, and state why — not to flip them all on.

```css
/* Example: ss02 gives this grotesque a single-storey 'a' and a straight 'l' — our display voice */
.display { font-feature-settings: "ss02" 1; }
```

The meaning of each `ssNN` is face-specific — check the foundry's glyph sheet. Document which set
and what it changes so the choice is reproducible.

## Small caps (`smcp`, and `c2sc` for caps→small-caps)

Real small caps are drawn glyphs with their own weight and proportion. Use them for acronyms in
running text, labels, and refined section headers.

```css
.acronym { font-variant-caps: small-caps; }          /* lowercase → small caps */
.label   { font-variant-caps: all-small-caps; }       /* caps + lowercase → small caps */
```

**Never use faux small caps.** If the face lacks `smcp`, browsers synthesise them by shrinking the
capitals — the stroke thins and it reads as cheap. Only switch this on for faces that ship the
feature; otherwise leave caps at full size or pick a face that has it.

## Fractions (`frac`) and ordinals (`ordn`)

`frac` turns `1/2` typed as three characters into a single properly-drawn fraction — essential for
recipes, measurements, spec tables, pricing like `3 1/4 in`. `ordn` styles `1st`/`2nd` ordinals.

```css
.recipe   { font-variant-numeric: diagonal-fractions; }   /* 1/2 → ½-style */
.ordinals { font-feature-settings: "ordn" 1; }
```

## High-level property vs `font-feature-settings`

Prefer the property — it inherits and composes with the cascade. Reserve
`font-feature-settings` for `ssNN`, custom features, and anything with no property:

| Want | High-level property |
|---|---|
| numerals | `font-variant-numeric: tabular-nums oldstyle-nums …` |
| ligatures | `font-variant-ligatures: …` |
| small caps | `font-variant-caps: …` |
| fractions | `font-variant-numeric: diagonal-fractions` |
| stylistic set / custom | `font-feature-settings: "ssNN" 1` (no property exists) |

Caveat mirroring the axis rules: don't set the same feature through both mechanisms on one element,
and remember `font-feature-settings` lists are not additive across the cascade the way you might
expect — restate the features you need on the element that declares it.

## Subsetting caveat (ties to `embedding-by-format.md`)

Subsetting trims glyphs to shrink the file — good practice for DOCX/PPTX/web. But aggressive
subsetting tools can **drop the OpenType feature tables** (`smcp`, `ssNN`, `tnum`, `frac`) along
with unused glyphs. If you rely on small caps, a stylistic set, or tabular numerals, verify they
still render after subsetting and keep those features in the subset configuration.
