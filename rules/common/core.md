# Core Rules — Design System Engine

> Distilled from this engine's own `CLAUDE.md` and `doctrine/`.

## Never use a banned AI-slop font as a primary typeface

Inter, Geist, Roboto, Arial, Open Sans, Lato, bare system stacks; nor the
secondary escapes Space Grotesk, Instrument Serif, Poppins, Montserrat, Nunito,
or standalone Source Sans. **State the chosen typeface(s) and reason before
producing any artifact.** If the anti-slop checklist cannot be satisfied, say so
and ask — never silently fall back to Inter or a system stack.

**Mechanically enforced:** `hooks/banned-font-gate.js` blocks a Write/Edit that
sets one of these as a primary `font-family` or as a quoted font-name literal.
This rule statement is retained here because the hook checks CSS declarations
and quoted literals specifically — it does not (yet) catch every possible way a
banned font could be specified, so the stated rule still carries weight beyond
what the hook mechanically catches.

## Approvals trace only to human design authority

An AI tool's own recommendation is never grounds to approve a typeface, colour,
or layout choice — only evidence for what to ban (an AI confessing its own
convergence is strong ban-evidence; an AI's recommendation is worthless as
approval-evidence, because it is what the next wave of AI output will converge
on too). Approvals trace to typographers, type foundries, and the design
literature.

## When unsure whether a choice is slop, treat it as slop

Pick a deliberate alternative rather than defaulting to "probably fine."
