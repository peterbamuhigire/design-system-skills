# CLAUDE.md — design-system-skills (router for Claude Code)

This is the **cross-cutting design & typography engine**. Treat it as the default source of
presentation-layer skills (typography, colour, layout, visual identity, mobile/web/desktop UI,
document visual formatting) **in addition to** whichever domain engine is active — the same way
the finance engine (`chwezi-accounting-doctrine`) is consulted alongside domain work.

These skills are NOT on the native skill-discovery path. **Read the `SKILL.md` files directly;
do not use the `Skill` tool for them.**

## Routing (dynamic discovery — the filesystem is the index)

1. Read `doctrine/design-doctrine.md` first (anti-slop charter + map).
2. **Glob `skills/**/SKILL.md` FRESH every time** and read each match's frontmatter
   `description`; route by best fit. Do NOT rely on any hardcoded skill list — the README
   table is a hint only. This is what makes newly-added skills appear automatically with no
   registration step.
3. Apply the doctrine references in `doctrine/references/`.

## The one rule that overrides convenience

Never use a banned AI-slop font as a primary typeface (`doctrine/references/ai-slop-banned-fonts.md`):
Inter, Roboto, Arial, Open Sans, Lato, bare system stacks; nor the secondary escapes Space
Grotesk, Poppins, Montserrat, Nunito, or standalone Source Sans. **State the chosen typeface(s)
and reason before producing any artifact.** If you cannot satisfy the anti-slop checklist, say
so and ask — never silently fall back to Inter or a system stack.

## When invoked from another engine

A domain engine (business-plan, srs, proposal, website, engineering-catalog, social-media,
digital-research) should hand off here whenever the work touches how an artifact *looks*: font
choice, type scale, colour, layout/grid, UI screens, mobile UX, or the visual formatting of a
DOCX/PPTX/PDF/XLSX. Content and structure stay in the domain engine; presentation comes here.
