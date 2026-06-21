# Phase 0.3 — The `examples/` Convention

The single biggest competent→world-class gap (audit dimension scored **22/100**): **not one of
37 skills ships a worked example.** This phase mandates them.

## What counts as a "worked example"
A concrete, applied artifact in the skill's `examples/` folder that *demonstrates the skill's
output*, not more prose. Acceptable forms:
- A real applied **spec** (e.g. a full type scale with px/rem values; a token JSON; a colour ramp in OKLCH).
- A **before/after** (a slop version → a fixed version, with the reasoning).
- A **sample artifact** (a CSS `@font-face` block; a component state matrix; a grid template; a deck outline; a DOCX style table).
- A worked **decision** (the stated typeface+colour+reason for a named brief).

## Definition (add to `CONTRIBUTING.md`)
> Every **craft** skill (one that produces a design artifact) MUST ship at least one file under
> `examples/`. Audit/process skills SHOULD ship a worked example (a sample audit, a filled
> template). The example must be specific and reusable — never lorem/placeholder.

## Edits
1. **`CONTRIBUTING.md`** — add an "Examples are mandatory" section with the definition above and
   the acceptance check.
2. **`skills/_TEMPLATE/`** — add `examples/example-1.md` stub with a comment explaining the
   requirement, and add a `## Examples` pointer line to `_TEMPLATE/SKILL.md`'s body.
3. **Discovery contract** — note in README that a craft skill without `examples/` is incomplete.

## Backfill tracking
This phase only *establishes* the convention; backfilling examples into the existing 37 happens
during their hardening (Phase 1 `02-p0-ten-hardening.md` and Phase 2/3). Add a checklist file
`docs/plans/hardening-june/examples-backfill-tracker.md` listing all skills with a ☐/☑ per skill.

## Acceptance
`CONTRIBUTING.md` + `_TEMPLATE` updated; tracker created; the rule is stated and checkable.
**Effort: S.**
