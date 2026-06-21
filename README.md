# design-system-skills

> *The anti-AI-slop design engine — typography, colour, layout, and UI that look made by skilled human hands, not a template.*

**Cross-cutting design & typography engine for the Chwezi skill-engine family.**
Owner: Peter Bamuhigire / Chwezi Core Systems (chwezicore.com) · Licence: MIT (code/docs;
font binaries are not committed — see `fonts/`).

This repo is the **single source of truth** for the presentation layer — typography, colour,
layout, visual identity, and the anti-AI-slop doctrine — across every Chwezi engine that emits
a rendered artifact (documents, websites, software/app UI). It is modelled on the finance
engine (`chwezi-accounting-doctrine`): **consult it IN ADDITION to** whichever domain engine is
active. Unlike the finance engine it is **referenced, not mirrored** — design skills live only
here, so each domain engine's skill count stays low.

---

## How to use this engine (router)

These skills are **not** on Claude Code's native discovery path. Read the `SKILL.md` files
directly; do not use the `Skill` tool for them.

1. **Always start here:** read `doctrine/design-doctrine.md` (the anti-slop charter + map).
2. **Then pick the skill** by globbing `skills/**/SKILL.md` and reading the match:

| You are… | Go to |
|---|---|
| Choosing/pairing/embedding fonts | `skills/01-typography-and-fonts/` |
| Choosing colour / building brand & visual identity | `skills/02-color-brand-and-visual-identity/` |
| Grids, spacing, composition, responsive layout | `skills/03-layout-grid-and-composition/` |
| Designing web / app / desktop UI (craft) | `skills/04-web-and-ui-design/` |
| UX research, process & psychology | `skills/05-ux-process-research-and-psychology/` |
| Sector/vertical UX (healthcare, legal, fintech…) | `skills/06-sector-and-domain-ux/` |
| Mobile (iOS / Android / cross-platform) | `skills/07-mobile-ios-android-cross-platform/` |
| Motion & interaction | `skills/08-motion-and-interaction/` |
| Design systems, tokens & handoff | `skills/09-design-systems-tokens-and-theming/` |
| Content design & UX writing | `skills/10-content-design-and-ux-writing/` |
| Imagery, illustration & art direction | `skills/11-imagery-illustration-and-art-direction/` |
| Charts, dashboards & data products | `skills/12-data-viz-and-dashboards/` |
| Presentations & documents (decks, DOCX/PDF/XLSX) | `skills/13-presentations-and-documents/` |
| Accessibility, QA, ethics, performance (**co-activates with every group**) | `skills/00-cross-cutting-ops-qa-a11y/` |

3. **Follow the doctrine references** in `doctrine/references/` — they are the canonical rules
   the skills cite.

> **The router table above is convenience only — it is NOT the source of truth.** See the
> discovery contract below.

---

## Discovery contract (how new skills are picked up — flawlessly, with zero registration)

This engine is **self-indexing**. To find the right skill you (or any consuming engine) MUST:

1. **Glob `skills/**/SKILL.md` fresh, every time.** Never rely on a cached or hand-maintained
   list — the tables in this README, `CLAUDE.md`, and the trigger block are *hints*, not the
   index. The filesystem is the index.
2. **Read each candidate's frontmatter `description`** and route by best match to the task.

**Adding a skill is therefore a one-step operation:** drop a folder at
`skills/<NN-group>/<skill-name>/SKILL.md` with valid frontmatter (copy `skills/_TEMPLATE/`).
No registry to update, no router edit required, no consumer-engine change. The next glob finds
it automatically. New groups work the same way — create `skills/<NN-newgroup>/` and it is
discovered on the next glob. See `CONTRIBUTING.md`.

The only hard requirement for flawless pickup: **every skill has well-formed frontmatter**
(`name` + a specific, trigger-rich `description`). The template enforces this.

---

## Layout

```
design-system-skills/
├── README.md                      ← this router       CLAUDE.md · AGENTS.md (dual-compat)
├── doctrine/
│   ├── design-doctrine.md         ← always-load charter
│   ├── references/                ← banned list, font groups, pairing, type scale, embedding, licensing
│   └── examples/
├── skills/                        ← 13 groups + 1 cross-cutting (co-activates)
│   ├── 00-cross-cutting-ops-qa-a11y/   (2)  ← accessibility, QA, audits — always-on
│   ├── 01-typography-and-fonts/        (4)
│   ├── 02-color-brand-and-visual-identity/ (4)
│   ├── 03-layout-grid-and-composition/ (1)
│   ├── 04-web-and-ui-design/           (8)
│   ├── 05-ux-process-research-and-psychology/ (2)
│   ├── 06-sector-and-domain-ux/        (3)
│   ├── 07-mobile-ios-android-cross-platform/ (2)
│   ├── 08-motion-and-interaction/      (1)
│   ├── 09-design-systems-tokens-and-theming/ (0 — Phase 1)
│   ├── 10-content-design-and-ux-writing/     (0 — Phase 1)
│   ├── 11-imagery-illustration-and-art-direction/ (0 — Phase 1)
│   ├── 12-data-viz-and-dashboards/     (1)
│   └── 13-presentations-and-documents/ (1: deck-system w/ 8 variant examples; + docs in Phase 1)
├── fonts/                         ← premium drop-in folders (binaries gitignored) + MANIFESTs
├── governance/design-quality-gate.md
└── integration/integration-plan.md   ← the trigger block other engines paste in + migration log
```

## Status

- **v0.2.0 (2026-06-21)** — live and populated: **37 skills** across 6 groups; full doctrine
  (Mission, anti-slop charter, sourcing-authority asymmetry, AI-slop taxonomy, banned list,
  font groups, pairing, type scale, embedding, licensing, system-font fallbacks); font taxonomy
  + manifests; discovery contract + `_TEMPLATE` + `CONTRIBUTING.md`.
- **v0.4.0 — Hardening Phase 1 COMPLETE (2026-06-21).** On the 14-group taxonomy (Phase 0),
  authored all **23 P0 skills** — real DOCX/PDF document formatting, design tokens + component
  library + dev handoff, accessibility (WCAG 2.2), i18n/RTL, performance-as-UX, design-QA,
  dark-mode, accessible-colour, responsive layout, navigation/IA, landing/conversion, states,
  UX research, wireframing, cross-platform mobile, UX-writing, messaging, photography art-
  direction, iconography, dashboards — each with references + a worked example. Hardened the
  **P0-ten** existing skills with 2026 standards (Liquid Glass, Material 3 Expressive, OKLCH,
  View Transitions, spring physics, APCA). **52 skills** across 14 groups. Drives off the audit
  in `docs/initial-analysis/` (51/100). **Next: Phase 2** — the P1 wave
  (`docs/plans/hardening-june/phase-2-p1-wave/`).

## Integration

Each domain engine carries the one-line trigger block from `integration/integration-plan.md`.
Reference model — nothing is mirrored. Clone this repo on every device so the reference always
resolves.

## Provenance

Doctrine distilled from the Chwezi design library (`Downloads\graphix_markdown`): Bonneville,
*The Big Book of Font Combinations*; Segall, *Complete Guide to Choosing Fonts*; Gingerich and
Paduraru on UI/UX fundamentals; Neil, *Mobile Design Pattern Gallery* — plus the Chwezi
"Font Usage Instructions for AI Coding Tools."
