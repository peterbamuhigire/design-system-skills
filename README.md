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
│   ├── 01-typography-and-fonts/   ← seeded (4 skills)
│   ├── 02-document-formatting/    ← migration target
│   ├── 03-web-and-ui-design/      ← migration target
│   ├── 04-color-and-visual-identity/   ← migration target
│   ├── 05-layout-grid-and-data-viz/    ← migration target
│   └── 06-mobile-ui-ux/           ← migration target
├── fonts/                         ← premium drop-in folders (binaries gitignored) + MANIFESTs
├── governance/design-quality-gate.md
└── integration/integration-plan.md   ← the trigger block other engines paste in + migration log
```

## Status

- **v0.1.0** — engine scaffolded; typography group seeded; doctrine written; font taxonomy and
  manifests in place. Groups 02–06 are **migration targets** — design skills will be moved here
  out of the other engines (see `integration/integration-plan.md`).

## Integration

Each domain engine carries the one-line trigger block from `integration/integration-plan.md`.
Reference model — nothing is mirrored. Clone this repo on every device so the reference always
resolves.

## Provenance

Doctrine distilled from the Chwezi design library (`Downloads\graphix_markdown`): Bonneville,
*The Big Book of Font Combinations*; Segall, *Complete Guide to Choosing Fonts*; Gingerich and
Paduraru on UI/UX fundamentals; Neil, *Mobile Design Pattern Gallery* — plus the Chwezi
"Font Usage Instructions for AI Coding Tools."
