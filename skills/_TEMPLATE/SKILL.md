---
name: skill-name-in-kebab-case
description: Use when a concrete task needs this procedure or standard. Name the artefact, user language, and closest neighbour that should route elsewhere.
metadata:
  portable: true
  category: NN-group-name
  compatible_with:
  - claude-code
  - codex
---

# Skill Title

One sentence defining the repeatable procedure and the decision it owns.

<!-- dual-compat-start -->
## Use When
- Bullet the concrete situations that should trigger this skill.

## Do Not Use When
- Bullet the situations where another skill is the better match (name it).

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Named input | User or upstream skill | yes | Decision it enables |

## Workflow

1. Step-by-step, citing `doctrine/references/*` where a canonical rule applies.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Concrete threshold or state | Required response | Consequence to avoid |

## Capability Contract

- State the minimum read, search, edit, execute, network, render, or delegation capabilities.
- Default reviews and audits to read-only. Require explicit authority before mutation or publication.

## Degraded Mode

- State the narrowest useful output when an input, renderer, browser, font, licence, or test is unavailable.
- Name unverified checks and block release when the missing evidence is material.

## Anti-Patterns

- Name at least five concrete mistakes and pair each with its correction.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Named output | Downstream role or skill | Observable proof of completion |

## Examples
- See `examples/` — every craft skill MUST ship ≥1 worked example (applied spec / before-after /
  sample artifact / worked decision). Never lorem. See `CONTRIBUTING.md`.

## References
- `doctrine/design-doctrine.md` and the specific `doctrine/references/*` this skill relies on
  (incl. `wcag-2.2-criteria.md` and `web-performance-budgets-2026.md` for UI/web skills).
<!-- dual-compat-end -->
