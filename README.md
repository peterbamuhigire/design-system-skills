# design-system-skills

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
| Choosing fonts for any artifact | `skills/01-typography-and-fonts/font-selection-and-pairing/` |
| Auditing something for AI slop | `skills/01-typography-and-fonts/ai-slop-typography-audit/` |
| Checking for purchased premium fonts | `skills/01-typography-and-fonts/premium-font-scan/` |
| Loading/embedding a font into web/DOCX/PPTX/PDF | `skills/01-typography-and-fonts/font-embedding-and-licensing/` |
| Visually formatting a DOCX/PPTX/PDF/XLSX deliverable | `skills/02-document-formatting/` |
| Designing web / desktop UI | `skills/03-web-and-ui-design/` |
| Choosing colour / building visual identity | `skills/04-color-and-visual-identity/` |
| Grids, spacing, charts / data viz | `skills/05-layout-grid-and-data-viz/` |
| Designing mobile app UI/UX | `skills/06-mobile-ui-ux/` |

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
├── skills/
│   ├── 01-typography-and-fonts/   (4 skills)
│   ├── 02-document-formatting/    (8 skills)
│   ├── 03-web-and-ui-design/      (16 skills)
│   ├── 04-color-and-visual-identity/   (5 skills)
│   ├── 05-layout-grid-and-data-viz/    (2 skills)
│   └── 06-mobile-ui-ux/           (2 skills)
├── fonts/                         ← premium drop-in folders (binaries gitignored) + MANIFESTs
├── governance/design-quality-gate.md
└── integration/integration-plan.md   ← the trigger block other engines paste in + migration log
```

## Status

- **v0.2.0 (2026-06-21)** — live and populated: **37 skills** across 6 groups; full doctrine
  (Mission, anti-slop charter, sourcing-authority asymmetry, AI-slop taxonomy, banned list,
  font groups, pairing, type scale, embedding, licensing, system-font fallbacks); font taxonomy
  + manifests; discovery contract + `_TEMPLATE` + `CONTRIBUTING.md`.
- **Migration Phases 1–2 complete** — design skills consolidated here out of skills-web-dev,
  social-media-skills, website-skills, and digital-research-engine (see
  `integration/migration-manifest.md`). Per-group counts: 01 typography (4), 02 document-
  formatting (8), 03 web-and-ui (16), 04 colour-and-identity (5), 05 layout/data-viz (2),
  06 mobile (2).
- Remaining: Phase 3 (the clean `tailwind`/`avalonia` splits; `professional-word-output` merge).

## Integration

Each domain engine carries the one-line trigger block from `integration/integration-plan.md`.
Reference model — nothing is mirrored. Clone this repo on every device so the reference always
resolves.

## Provenance

Doctrine distilled from the Chwezi design library (`Downloads\graphix_markdown`): Bonneville,
*The Big Book of Font Combinations*; Segall, *Complete Guide to Choosing Fonts*; Gingerich and
Paduraru on UI/UX fundamentals; Neil, *Mobile Design Pattern Gallery* — plus the Chwezi
"Font Usage Instructions for AI Coding Tools."
