---
name: slop-doctrine-refresh-and-research-loop
description: Use when AI-slop definitions, banned fonts, visual tells, product-slop patterns, or anti-slop doctrine may have changed and the design engine needs a self-review pass coordinated with the digital-research engine before updating guidance.
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
    - claude-code
    - codex
---

# Slop Doctrine Refresh & Research Loop
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- A user says the definition of "AI slop" has changed.
- A font, visual style, layout trope, AI-image tell, or UI/product pattern may have become a new
  AI-default signal.
- Updating `ai-slop-taxonomy.md`, `ai-slop-banned-fonts.md`, `visual-product-slop-audit`, or
  `ai-slop-typography-audit`.
- A high-stakes public artifact needs a freshness check against current AI-slop norms.
- Another engine asks whether a design choice is merely popular, genuinely AI-converged, or still
  acceptable with a deliberate rationale.

## Do Not Use When

- You are auditing a specific image/UI only against the current checklist - use
  `visual-product-slop-audit`.
- You are only auditing type in a finished artifact - use `ai-slop-typography-audit`.
- The concern is written copy only - route to the digital-research engine's `anti-ai-slop` and
  `ai-slop-audit` skills.

## Required Inputs

- The doctrine, checklist, or artifact under review.
- The suspected changed tell, default, font, product trope, or market signal.
- The intended scope: typography, image/video, UI/product, brand, document, or cross-engine handoff.
- Whether the result is advisory, watchlist-level, or intended to change a hard ban.

## Workflow

1. **Load the local anti-slop doctrine**: `doctrine/design-doctrine.md`,
   `doctrine/references/ai-slop-taxonomy.md`, `doctrine/references/ai-slop-banned-fonts.md`, and
   `doctrine/references/living-slop-refresh-protocol.md`.
2. **Route research to the digital-research engine** before making doctrine changes. Load its
   `skills/source-evaluation/SKILL.md`,
   `skills/source-evaluation/references/evidence-discipline.md`, `skills/anti-ai-slop/SKILL.md`,
   and `skills/ai-slop-audit/SKILL.md`.
3. **Separate claims by evidence type**: primary/vendor/platform source, design-practitioner
   source, public incident, marketplace/template observation, social signal, or weak anecdote.
4. **Classify the change** using the protocol buckets: hard ban / critical tell, watchlist,
   contextual risk, or rejected claim.
5. **Translate only the design consequence** into this engine. Keep writing/cultural taxonomy in
   the digital-research engine and cross-cite it instead of duplicating it.
6. **Patch doctrine with a dated rationale** if the evidence warrants it. State observed shift,
   evidence grade, design consequence, scope, and date checked.
7. **Run the design quality gate** and verify every active `SKILL.md` still has an example when a
   new skill is added.

## Anti-Patterns

- Freezing a 2026 slop tell as permanent truth after models have moved.
- Adding hard bans from vibes, social screenshots, or a single anecdote.
- Treating AI-vendor design recommendations as approval authority.
- Copying the digital-research engine's writing guidance into this repo instead of referencing it.
- Updating a checklist without recording evidence strength and date checked.

## Outputs

- A slop-doctrine refresh note: observed shift, evidence grade, design consequence, scope, date
  checked, and changed files.
- Updated design doctrine/checklists when evidence supports a change.
- A rejected-claim note when the evidence is too weak for doctrine.

## Examples

- `examples/font-default-refresh-note.md` - classifies an emerging AI-default font signal and
  decides whether it becomes a hard ban, watchlist item, or rejected claim.

## References

- `doctrine/references/living-slop-refresh-protocol.md` - required update protocol.
- `doctrine/references/ai-slop-taxonomy.md` and `doctrine/references/ai-slop-banned-fonts.md` -
  design-engine slop doctrine.
- `visual-product-slop-audit` and `ai-slop-typography-audit` - artifact-level audits that consume
  the refreshed doctrine.
- Digital-research engine: `source-evaluation`, `evidence-discipline`, `anti-ai-slop`, and
  `ai-slop-audit` - source discipline and writing/cultural slop framing.
<!-- dual-compat-end -->
