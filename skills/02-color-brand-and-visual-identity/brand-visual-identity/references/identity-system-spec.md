# Identity System Spec — the real structure of a brand identity

A brand identity is a *system*, not a logo. This is the canonical structure that a mini
style-guide (the skill's Output) instantiates, and the structure a binding client guideline
should be read against. Specify each layer deliberately — every undefined slot is where
downstream contributors improvise and the identity drifts toward the convergent mean
(`doctrine/design-doctrine.md` §0, §2). Cross-check the finished system against
`references/brand-consistency-gate.md` before sign-off.

---

## 1. Strategy layer (governs everything below)

| Slot | What it fixes | Authored value (not a default) |
|---|---|---|
| One-word essence | The single idea the whole identity serves | e.g. "austere", "warm", "kinetic" |
| Adjective set (3–5) | The test every visual choice is run against | e.g. austere · precise · warm |
| Not-to-be-confused-with | The 2–3 named competitors you must look *unlike* | distinctiveness is relative (Neumeier) |
| Audience | Who it is *for* | primary + secondary |
| Surface set | favicon → billboard, light/dark, print/screen, single-colour, embroidered | drives every reproducibility rule |

Without this layer there is nothing to justify a choice *against*, so every later decision
defaults to "what looks safe" — i.e. the AI mean.

## 2. Logo / mark system

A mark is never one image. Specify the whole governed set:

| Element | Spec it carries |
|---|---|
| Primary lockup | mark + wordmark, exact relationship (alignment, gap in mark-units) |
| Secondary / stacked lockup | for narrow or square surfaces |
| Monogram / icon-only | favicon, app icon, avatar — the favicon-end legibility test |
| Clear-space | expressed in units *of the mark itself* (e.g. "= height of the cap O"), never px |
| Minimum size | smallest legible size per surface (e.g. 16 px favicon, 24 mm print) |
| Colour variants | full-colour, single-colour (positive + reversed), dark-mode |
| Misuse set | 4–6 explicit don'ts: don't recolour, distort, rotate, add effects, crowd, swap type |

Discipline references: Paul Rand (simple, distinctive, reproducible, earns meaning through
use — must be redrawable from memory in one colour); Massimo Vignelli (a small governed set
used consistently, not a sprawl of variants). **Never ship an AI-generated mark** — warped,
fused, or misspelled letterforms are the highest public-backlash slop tell
(`doctrine/references/ai-slop-taxonomy.md` §Visual tells, category 2).

## 3. Colour tie-in (construction deferred to `color-system-and-palette`)

Identity binds, it does not build. Assign **roles**, then name the one ownable colour:

| Role | Function | Example token |
|---|---|---|
| Brand / signature | the one colour the brand owns | `--brand-600` |
| Ink | primary text on surface | `--ink-900` |
| Surface | backgrounds, light + dark | `--surface-0`, `--surface-900` |
| Accent | sparing emphasis, never a second "brand" | `--accent-500` |
| State | success / warn / error / info | semantic, not decorative |

Pick **one** signature colour, state why it fits the essence, and ban the off-system
purple→blue gradient (doctrine §2 — the single most recognisable identity slop signal).
Construction, ramp, and contrast certification live in `../color-system-and-palette`.

## 4. Type tie-in (selection deferred to `font-selection-and-pairing`)

| Role | Face | Notes |
|---|---|---|
| Wordmark | may be custom-drawn or a customised cut | part of the *voice*, not just a heading |
| Display / headings | the pairing's display face | where it agrees or contrasts with the wordmark — state it |
| Body / running | the pairing's body workhorse | legibility first |
| Mono / data (if any) | for code, tables, figures | only if the brand needs it |

Record where the wordmark's letterforms and the running type deliberately agree or contrast.
Selection, pairing, scale, embedding, and licensing live in
`../../01-typography-and-fonts/font-selection-and-pairing`.

## 5. Supporting visual language (what separates authored from templated)

- **Spacing & geometry:** one spacing rhythm + one corner/edge language (sharp vs soft),
  applied everywhere. Grid lives in `../../03-layout-grid-and-composition`.
- **Photography:** framing, colour grade, subject treatment, real-vs-stock rule. Reject
  uncanny / waxy / impossible-physics AI imagery as brand content (`ai-slop-taxonomy.md` §1–2).
- **Illustration / iconography:** one coherent system — fixed line weight, corner radius,
  perspective. Not a marketplace of mismatched stock icons.
- **Motion (optional):** one or two signature behaviours, not decoration.

## 6. Voice-of-the-visuals

One short paragraph + one do/don't pair telling any future contributor *how the brand behaves
visually*. This is the gap between strategy and execution (Neumeier, *The Brand Gap*) — the
rule a templating tool can never infer, and the human-authority anchor of the system.

## 7. Governance

- Provenance: who authored the system, version, date.
- Sourcing authority: choices trace **only** to human design authority — never to an AI tool's
  "brand suggestions" (doctrine §2, sourcing-authority asymmetry).
- The **memory test**: could someone redraw the essence after looking away? If not, it is not
  yet ownable — sharpen one element.
- Sign-off requires a clean pass of `references/brand-consistency-gate.md`.

---

### Minimal vs full system

A *mini* style-guide (1–3 pages, the skill's default Output) covers layers 1, 2 (lockups +
clear-space + min size + variants + a short misuse set), 3 (roles + signature), 4 (roles),
5 (one line each), and 6. A *full* brand book expands every layer with exhaustive misuse
grids, co-branding rules, merchandise, and templates. Build the mini first; expand only when
the brand's surface count justifies it.
