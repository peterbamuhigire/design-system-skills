# Worked example — mini brand identity: "Sonda"

A complete, applied mini style-guide produced by this skill for an invented but realistic
brand. It instantiates every required layer of `references/identity-system-spec.md` and ends
with a filled `references/brand-consistency-gate.md`. Use it as the shape your own deliverable
should take — not as a template to recolour.

**Brief.** Sonda is a soil-and-water sensor company for East African commercial farms.
It sells hardware probes plus a dashboard. Audience: agronomists and farm managers who
distrust gadgety, over-promising agritech. The brand must read as *instrument-grade*, not
*startup-shiny*.

---

## 1. Strategy

- **Essence:** *measured.*
- **Adjectives:** measured · field-rugged · plain-spoken · precise · unhurried.
- **Not-to-be-confused-with:** generic Silicon-Valley agritech (gradient logos, hero drones),
  consumer smart-garden gadgets, NGO project branding (busy, well-meaning, forgettable).
- **Audience:** agronomists and farm managers (primary); co-op procurement (secondary).
- **Surface set:** 16 px favicon → equipment label silk-screen → dashboard UI → one-page spec
  sheet (print) → embroidered field-cap. Must survive single-colour and dark.

Every choice below is justified against "measured" and the not-to-be-confused list.

## 2. Logo / mark

- **Primary lockup:** a custom **wordmark** "Sonda" in a humanist grotesque, drawn with a
  single distinguishing detail — the dot of a notional sensor reading sits as a small filled
  square tittle over the "i"-less name's leading edge, i.e. a 1×1 unit square baseline-marker
  before the **S**. Wordmark + marker share a baseline; gap = 0.5 cap-heights.
- **Monogram:** the marker-square + **S** only, for favicon, app icon, probe end-cap.
- **Clear-space:** = the height of the cap **S** on all sides. Expressed in mark-units, never px.
- **Minimum size:** wordmark 88 px / 22 mm; monogram 16 px favicon (verified legible — the
  square marker survives where a thin glyph would not).
- **Variants:** full-colour (Probe Green on Bone), single-colour positive (Field Ink on Bone),
  reversed (Bone on Field Ink), dark-mode (Bone on `--surface-900`). All exist and are legible.
- **Misuse set:** don't recolour the marker to the accent; don't add a sensor-wave swoosh;
  don't outline; don't set on a photo without the Field-Ink scrim; don't stretch; don't
  substitute a geometric-sans for the custom cut.

Why not generated: the mark is redrawable from memory in one colour (Rand), and uses one
governed element repeated (Vignelli — the square is mark, monogram tittle, and bullet glyph).
No AI mark — a generated "S + leaf" would carry the warped-glyph tell and read as every other
agritech logo.

## 3. Colour tie-in  *(construction → `../color-system-and-palette`)*

One owned signature: **Probe Green** — a desaturated, slightly olive green that reads as
*field instrument*, not *eco-marketing leaf*. Chosen because "measured" rejects the saturated
SaaS green and the off-system purple→blue gradient outright (doctrine §2).

| Role | Token | Value (OKLCH) | Use |
|---|---|---|---|
| Brand / signature | `--brand-600` | `oklch(0.55 0.09 145)` | the marker square, key data line, primary CTA |
| Ink | `--ink-900` (Field Ink) | `oklch(0.22 0.02 250)` | body text, wordmark mono variant |
| Surface light | `--surface-0` (Bone) | `oklch(0.97 0.01 95)` | warm off-white, not pure #fff |
| Surface dark | `--surface-900` | `oklch(0.20 0.02 250)` | dashboard dark mode |
| Accent | `--accent-500` (Clay) | `oklch(0.63 0.13 55)` | sparing — alerts/thresholds only, never a 2nd brand |
| State | success/warn/error | semantic ramp | derived in `color-system-and-palette`, APCA-certified there |

Construction, the full ramp (light+dark), and contrast certification are deferred to
`../color-system-and-palette`. Identity only assigns roles and names the owned colour.

## 4. Type tie-in  *(selection → `../../01-typography-and-fonts/font-selection-and-pairing`)*

| Role | Face | Tie-in note |
|---|---|---|
| Wordmark | custom humanist-grotesque cut | shares the body face's skeleton, drawn tighter |
| Display / headings | the paired grotesque (display weight) | agrees with the wordmark — one voice |
| Body / running | the pairing's humanist body workhorse | plain-spoken, high legibility on spec sheets |
| Mono / data | a workhorse mono | for probe readings, tables, dashboard figures — the brand *is* data, so it earns a mono |

Wordmark and headings deliberately **agree** (same family of skeleton); the mono deliberately
**contrasts** to flag "this is a measured value." Actual face names, pairing rationale, scale,
embedding, and licensing are decided in `font-selection-and-pairing`.

## 5. Supporting visual language

- **Spacing & geometry:** 8 pt rhythm; **2 px corner radius** everywhere (near-sharp =
  instrument, not soft consumer app). One radius, no exceptions.
- **Photography:** real probes in real soil, overcast flat light, no golden-hour glamour, no
  drone hero shots. People are real farm staff, shown working. Reject any waxy / impossible-
  physics AI imagery (`ai-slop-taxonomy.md` §1–2).
- **Iconography:** 1.5 px stroke, square caps, 2 px radius — matched to the wordmark's
  engineered feel. One system, no mixed stock sets.
- **Motion:** one signature — data values *count up* into place on load (≤200 ms); nothing else
  animates. Restraint = measured.

## 6. Voice-of-the-visuals

> Sonda looks like an instrument, not an app. It states a number plainly and lets the number do
> the talking. It is never loud, never gradient, never cute. When in doubt, remove decoration
> until only the measured fact remains.

**Do:** show a single hard data line in Probe Green on Bone, with one mono figure and clear units.
**Don't:** wrap the reading in a glowing card, a leaf icon, and a purple gradient header.

## 7. Applied mini style-guide (the deliverable, one screen)

```
┌──────────────────────────────────────────────────────────────┐
│  ■ Sonda                                  measured · precise   │  ← wordmark + marker, clear-space = cap-S
├──────────────────────────────────────────────────────────────┤
│  LOGO     primary ■ Sonda  ·  mono ■ Sonda  ·  rev (Bone/Ink) │
│           favicon ■S  ·  min 88px / 16px favicon              │
│  COLOUR   ●brand-600 Probe Green   ●ink-900 Field Ink         │
│           ○surface-0 Bone   ●surface-900   ●accent Clay(alert)│
│  TYPE     Wordmark/Display: paired grotesque                  │
│           Body: humanist workhorse   Data: mono               │
│  GEOMETRY 8pt rhythm · 2px radius · 1.5px icon stroke         │
│  PHOTO    real probes, flat light, real staff — no AI imagery │
│  VOICE    "an instrument, not an app — let the number talk"   │
└──────────────────────────────────────────────────────────────┘
```

This single panel is the artifact downstream surfaces (dashboard, spec sheet, cap, favicon)
must obey. Expand to a full brand book only if surface count grows.

---

## 8. Consistency Gate — filled  *(`references/brand-consistency-gate.md`)*

| Gate item | Result | Evidence |
|---|---|---|
| Logo: lockup, clear-space, min size on every surface | ☑ Pass | favicon 16 px monogram verified; clear-space = cap-S |
| Single-colour + dark-mode variants exist and are legible | ☑ Pass | positive/reversed/dark all specified in §2 |
| Colour: roles honoured, signature actually carried | ☑ Pass | Probe Green on marker, data line, CTA |
| No off-system gradient / stray accent | ☑ Pass | purple→blue gradient explicitly banned; Clay is alert-only |
| Type: identity pairing used, no slop "escape" font | ☑ Pass | wordmark/display/body/mono roles fixed |
| Imagery passes AI-slop visual checklist | ☑ Pass | real-staff/flat-light rule; AI imagery rejected |
| Memory test: redrawable essence after looking away | ☑ Pass | "■ + green + plain mono number" is the recallable core |

All items pass — system is internally consistent and ready to apply. Had any failed, the rule
is: fix before sign-off, do not ship a half-applied system.
