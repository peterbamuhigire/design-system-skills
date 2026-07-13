# Design Engine Skill Authoring Standard

This is the local conformance contract for every active `skills/**/SKILL.md`. It applies the
canonical `skill-writing`, `skill-composition-standards`, and `skill-engine-audit` rules from the
`skills-web-dev` engine without copying their full bodies into this repository.

## Definition of a skill

A skill is a reusable procedure or standard. It is not an autonomous agent or a personality.
Keep runner-specific tool names, model names, and delegation syntax out of canonical skill text.
Describe required capabilities instead: read, search, edit, execute, network, or delegate.

## Required contract

Every active skill must declare:

1. `name` and a single-line trigger description beginning with `Use when`.
2. Positive triggers and explicit neighbour exclusions.
3. Required inputs, including who or what supplies them.
4. An ordered workflow with stop and recovery conditions.
5. Named outputs, consumers, evidence, and acceptance conditions.
6. A minimum capability contract and safe permission boundary.
7. A degraded mode for missing files, tools, rendering, research, or execution.
8. At least one decision table with the failure caused by the wrong choice.
9. Five concrete anti-patterns, each paired with a correction.
10. Directly linked references and at least one worked example for craft skills.

## Frontmatter

Use only `name`, `description`, `license`, `allowed-tools`, and `metadata`. The `name` must match
the skill directory. The description must stay under 350 characters, distinguish the closest
neighbour, and name the artefacts or user language that should activate the skill.

`metadata` must include:

```yaml
metadata:
  portable: true
  category: NN-group-name
  compatible_with:
  - claude-code
  - codex
```

## Progressive disclosure

Keep `SKILL.md` at 500 lines or fewer. Retain routing, decisions, workflow, safety, and output
contracts in the entrypoint. Move lengthy catalogues, examples, schemas, and implementation
detail to directly linked `references/` files. References must link back to their parent skill.

## Review and mutation boundaries

Analysis, audit, critique, and planning default to read-only. Editing requires an implementation
or remediation request. External publication, destructive actions, purchases, production
mutation, and claims of certification require separately stated authority and evidence.

## Release evidence

Run both local gates:

```powershell
python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
```

The first command may pass with documented baseline debt, but it must fail on any new defect.
Reduce the baseline whenever a cohort is normalised. The routing test must pass without waivers.

## Stop conditions

Stop and gather context when the requested artefact, audience, platform, source design, or
acceptance condition is missing and materially changes the result. Stop release when a required
render, accessibility check, licence check, source verification, or platform test is unavailable;
return the narrowest useful draft and name the missing evidence.
