# Chwezi Design Doctrine

**Version:** 0.1.0
**Owner:** Peter Bamuhigire / Chwezi Core Systems (chwezicore.com)
**Status:** active
**Scope:** Cross-cutting presentation-layer doctrine for every Chwezi engine that emits a
rendered artifact — documents (DOCX/PPTX/PDF/XLSX), websites, and software/app UI (web,
desktop, mobile). Consult this engine **in addition to** whichever domain engine is active,
exactly as the finance doctrine is consulted alongside domain work.

---

## 0. Mission — the moat is looking human-made

In the age of AI, almost anything *functional* can be generated cheaply. What will sell a
product is whether it looks **different, distinct, and the product of highly skilled human
hands.** Sameness is now free and worthless; deliberate, crafted distinctiveness is the moat.

Every skill in this engine exists to push output **away from the convergent AI mean** and toward
the unmistakable signature of a skilled designer who made specific, defensible choices. When two
options are equally "clean," prefer the one that looks *authored* — the one a templating tool
would never have produced. Restraint plus one strong, intentional choice beats five hedged,
safe ones. This mission outranks convenience every time.

---

## 1. Purpose

Typography, colour, layout, and visual identity are not domain concerns — they cut across
every engine. This doctrine is the **single source of truth** for how a Chwezi artifact
should look, so that the rule lives in one place and the domain engines (business-plan, srs,
proposal, website, engineering-catalog, social-media, digital-research) reference it rather
than each carrying its own drifting copy.

The prime directive: **forever remove "AI slop" from Chwezi products.** Every deliverable must
make a *deliberate, stated* visual choice — never a reflexive default.

---

## 2. The Anti-Slop Charter (read this every time)

AI tools converge on a small set of "safe default" fonts, colours, and layouts because those
defaults dominate their training data. Using them is the recognisable signature of
unconsidered, machine-generated work. A page or document that opens in Inter, on a generic
purple-to-blue gradient, with evenly-spaced cards, tells a discerning client that no one
thought about design. That undermines the premium positioning of the whole portfolio
(Maduuka, Medic8, KesiLex, BrightSoma, Longhorn ERP, and external client deliverables).

**The five non-negotiables:**

1. **State the choice before producing the artifact.** Name the typeface(s), the palette
   intent, and why they fit *this* artifact's context — before writing any code or generating
   any document. See `skills/01-typography-and-fonts/font-selection-and-pairing/`.
2. **Never use a banned default.** See `references/ai-slop-banned-fonts.md`. This includes the
   secondary "escape" fonts AI reaches for *after* being told to avoid the first list.
3. **Always pair, never monotype.** A single font (or a single weight, or a single size step)
   used for everything is itself a slop signal. See `references/pairing-principles.md`.
4. **Check the licence before embedding.** Embedding redistributes the file. See
   `references/licensing-and-embedding.md`.
5. **If you cannot satisfy the above, say so and ask** — never silently fall back to Inter or
   a bare system stack.

**Sourcing authority (the asymmetry rule).** Approvals — what fonts/colours/layouts we *choose*
— trace **only to human design authority**: typographers, type foundries, and the design
literature. **AI-vendor recommendations are never authority for what to use**, because an AI
tool's own picks are precisely what the next wave of AI output converges on — adopting them just
launders slop one step removed. AI-vendor sources are admissible **only as evidence of what to
avoid** (the AI confessing its own convergence). When a human-justified approved font also
happens to appear on an AI tool's recommend-list, note the convergence risk — do not treat the
AI nod as endorsement. See `references/ai-slop-banned-fonts.md` §Evidence basis.

---

## 3. How the engine is organised

| Path | What it holds |
|---|---|
| `doctrine/design-doctrine.md` | This charter — the always-load entry point. |
| `doctrine/references/` | The canonical rules: the AI-slop taxonomy, banned font list, font groups, pairing, type scale, embedding, licensing, and the device-common system-font fallback tier. |
| `doctrine/examples/` | Worked examples (good pairings, a slop-audit before/after). |
| `skills/01-typography-and-fonts/` | The font skills: selection & pairing, slop audit, premium-font scan, embedding & licensing. |
| `skills/02-document-formatting/` | Visual formatting of DOCX/PPTX/PDF/XLSX deliverables. |
| `skills/03-web-and-ui-design/` | Web and desktop UI visual design. |
| `skills/04-color-and-visual-identity/` | Palettes, brand identity, contrast. |
| `skills/05-layout-grid-and-data-viz/` | Grids, spacing, charts/data visualisation. |
| `skills/06-mobile-ui-ux/` | Mobile-specific UI/UX (iOS HIG, Android Material, touch, gestures, safe areas). |
| `fonts/<group>/` | Premium font files you purchase (gitignored) + a tracked `MANIFEST.md` per group. |
| `governance/` | The design quality gate. |
| `integration/` | The trigger block other engines paste in, plus the migration log. |

---

## 4. The font-folder protocol (standard-first, premium-when-present)

Every font skill follows the same two-tier rule:

1. **Baseline (always available):** the named standard fonts in `references/font-groups-and-usage.md`
   are OFL/Google-Fonts faces. They never need files shipped — they are named, fetched (web),
   or assumed installed, and are safe to embed.
2. **Premium (use when present):** before committing, **scan `fonts/<matching-group>/`** for a
   purchased family the user has dropped in. If a premium family is present *and* its MANIFEST
   permits the intended use, prefer it when it would make the product look better. Otherwise
   fall back to the named baseline. See `skills/01-typography-and-fonts/premium-font-scan/`.

The four groups in `fonts/` mirror the user's own `Downloads\Fonts` taxonomy exactly:
`1-Editorial-Authoritative`, `2-Developer-Technical`, `3-Startup-Product`, `4-Body-Workhorses`.

---

## 5. Integration (reference model)

Design skills live **only** in this engine. Each domain engine carries a one-line trigger
block (see `integration/integration-plan.md`) that says: *"Any typography / UI / visual
formatting / colour / layout work → consult `C:\wamp64\www\design-system-skills` (start at
its `README.md`), IN ADDITION to the active engine."* Nothing is mirrored — this keeps each
domain engine's skill count down and prevents drift. The engine is cloned on every device the
user works on, so the reference always resolves.

---

## 6. Versioning

Semver, tracked here in the header. Reference files and skills state their own provenance.
Breaking changes to the banned list or group taxonomy bump the minor version and are logged in
`integration/integration-plan.md`.
