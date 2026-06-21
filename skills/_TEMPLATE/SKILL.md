---
name: skill-name-in-kebab-case
description: Use when … (one or two sentences, TRIGGER-RICH — name the artifacts, contexts, and verbs that should route here, because consumers select skills by matching this text. Be specific; vague descriptions don't get picked up.)
status: active
metadata:
  portable: true
  category: NN-group-name
  compatible_with:
    - claude-code
    - codex
---

# Skill Title

<!-- dual-compat-start -->
## Use When
- Bullet the concrete situations that should trigger this skill.

## Do Not Use When
- Bullet the situations where another skill is the better match (name it).

## Required Inputs
- What the skill needs before it can run well.

## Workflow
1. Step-by-step, citing `doctrine/references/*` where a canonical rule applies.

## Anti-Patterns
- The mistakes this skill exists to prevent.

## Outputs
- What the skill produces.

## References
- `doctrine/design-doctrine.md` and the specific `doctrine/references/*` this skill relies on.
<!-- dual-compat-end -->
