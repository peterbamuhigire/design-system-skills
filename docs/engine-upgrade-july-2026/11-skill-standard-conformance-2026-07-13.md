# Skill-Standard Conformance Upgrade — 2026-07-13

This is a working upgrade record, not a presentation report. It supersedes the contract and
routing conclusions in the earlier July scorecard where the machine evidence differs.

## Benchmark used

The repository was assessed against the canonical `skills-web-dev` routes:

- `skills/sdlc-meta/skill-writing/SKILL.md`
- `skills/sdlc-meta/skill-composition-standards/SKILL.md`
- `skills/sdlc-meta/skill-engine-audit/SKILL.md`
- mandatory `anti-ai-slop` production and `ai-slop-audit` review controls

The resulting local contract is `governance/skill-authoring-standard.md`.

## Evidence snapshot before judgement-heavy edits

The canonical scanner found 83 `SKILL.md` files including `_TEMPLATE`, with zero fully compliant.
The active catalogue contains 82 skills. Strong evidence already present:

- 82/82 active skills have a worked `examples/` directory.
- Every active skill has a matching frontmatter `name`.
- There are no duplicate skill names.
- All eight required font-category directories exist.
- The doctrine, anti-slop rules, cross-engine reference model, and domain taxonomy are unusually
  mature for a design instruction engine.

Blocking contract debt found before the upgrade:

| Finding | Count | Consequence |
|---|---:|---|
| Missing decision-rules section | 83/83 including template | Skills explain craft but do not consistently choose between alternatives |
| Missing capability contract | 68/83 | Review skills can blur read-only analysis with authorised mutation |
| Missing degraded mode | 62/83 | Unavailable renderers, devices, fonts, or evidence can become false confidence |
| Trigger/description failure | 76/83 | Overlong or non-trigger descriptions weaken discovery and neighbour separation |
| Input-contract failure | 80/83 | Upstream requirements are prose rather than composable artefact contracts |
| Fewer than five concrete anti-patterns | 29/83 | Some skills lack failure-mode depth |
| Invalid YAML frontmatter | 6/83 | A loader may skip high-value skills entirely |
| Over 500 lines | 1/83 | `data-visualization` needs progressive-disclosure extraction |

## Core diagnosis

The engine is strong as a design knowledge library and weaker as an executable instruction
system. Its doctrine, breadth, references, and examples can guide excellent work, but the older
skill shape often assumes an ideal context and a capable human reader. The July 2026 standard
requires each entrypoint to make routing, permissions, missing-evidence behaviour, outputs, and
acceptance explicit. That is the main gap; adding more design topics before fixing it would grow
the catalogue faster than its reliability.

The earlier July audit overemphasised render pipelines and Flutter depth. Those remain real P1/P2
gaps, but they are downstream of the P0 contract problem. A render pipeline cannot compensate for
a skill that routes ambiguously or declares release readiness without evidence.

## Changes implemented in this cohort

1. Added the local skill-authoring standard and linked it from both agent routers and contribution
   instructions.
2. Rebuilt `_TEMPLATE` around inputs, outputs, decision rules, capabilities, degraded mode,
   evidence, and acceptance conditions.
3. Added `scripts/validate_engine.py`, a regression baseline, and CI. Existing debt may decrease
   but cannot increase unnoticed.
4. Added 20 routing fixtures covering important neighbour collisions. Current result:
   precision@1 90%; precision@3 100%.
5. Added a design-delivery evidence template and changed the design quality gate from unchecked
   checklist assertions to evidence-backed `PASS`, `CONDITIONAL`, or `BLOCKED` verdicts.
6. Removed unsupported `status` frontmatter and repaired six invalid multiline descriptions.
7. Fully normalised the first seven high-risk active skills:
   `design-audit`, `design-qa-and-pre-launch-review`, `product-design-audit`,
   `accessibility-wcag-2-2-compliance`, `font-selection-and-pairing`,
   `design-tokens-and-naming`, and `design-handoff-and-dev-spec`.

## Final conformance result

All planned cohorts were completed across groups 00–14. Every active skill now includes a concise
neighbour-aware trigger, evidence-bearing input and output contracts, domain decision rules,
capability boundaries, degraded-mode and stop/recovery behaviour, non-empty workflow and quality
sections, and at least five concrete anti-patterns.

`data-visualization/SKILL.md` was reduced below the 500-line ceiling by extracting its narrative
and case-pattern depth into `references/data-storytelling-and-case-patterns.md`, which links back
to its parent.

Final measured state:

| Gate | Result |
|---|---:|
| Active skills | 82 |
| Local validator fully compliant | 82/82 |
| Canonical engine scanner fully compliant | 82/82 active skills |
| Canonical per-skill quick validation | 82/82 |
| Routing fixtures | 46 |
| Routing precision@1 | 89% |
| Routing precision@3 | 100% |
| Skills over 500 lines | 0 |
| Duplicate names | 0 |
| Missing font categories | 0 |
| Regression-baseline failures | 0 |

## Release position

The documented skill-contract debt is cleared. The zero-debt baseline now makes every new
structural or contract finding a CI regression. Future work on render regression, Flutter depth,
or additional exemplars is capability expansion, not deferred conformance repair.
