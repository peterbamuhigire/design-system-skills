---
name: educational-and-childrens-game-experience
description: Use when a game for children or learners needs age-appropriate comprehension, scaffolding, learning-feedback separation, privacy/safety, stopping cues, guardian/teacher needs, accessible play, or non-exploitative engagement. Use onboarding-and-first-run-design for ordinary apps.
metadata:
  portable: true
  category: 15-game-visual-experience
  compatible_with:
  - claude-code
  - codex
---

# Educational and Children’s Game Experience Design

Design voluntary, age-appropriate play that supports a stated learning decision while keeping learning, enjoyment, safety, privacy and commercial evidence separate.

<!-- dual-compat-start -->
## Use When

- Children are an intended or likely audience, or a game claims a learning outcome.
- Comprehension, scaffolding, tutorials, feedback, stopping, guardian/teacher support, safety, privacy or purchases/ads must adapt by age and context.
- Educational content must remain playable without turning the game into a quiz wrapper.

## Do Not Use When

- The product is an ordinary adult app onboarding flow; use `onboarding-and-first-run-design`.
- The work is curriculum, pedagogy, clinical development or legal approval; require the accountable expert and use this skill only for game experience.
- The work is general HUD, art or game-feel craft without a child/learning concern; use the corresponding game specialist.
- Engagement telemetry is being used to claim learning; route to research design and require a learning measure.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Age range, contexts, languages, abilities and guardian/teacher role | Product/research | yes | Prevents an invented “child user” |
| Learning objective, prior knowledge, construct, limits and accountable expert | Education owner | required for learning claim | Defines what can be taught or assessed |
| Core loop, content, failure, stopping, social, privacy, ads and purchase model | Product/SRS | yes | Exposes safety and coercion risks |
| Consent-approved research plan and representative evidence | Research/ethics | required for observed claims | Protects children and limits inference |

## Workflow

1. Define cohorts by age/developmental context, language, ability, prior knowledge, play setting and guardian/teacher involvement. Stop if a single generic child cohort would change design or safety.
2. State the learning objective as observable performance, the evidence method, comparator/baseline, duration and transfer limit. Separate it from enjoyment, completion and retention.
3. Bind learning to the core verb: model, guided practice, feedback, variation, independent use and reflection. Keep instructions close to action and fade scaffolds only after demonstrated comprehension.
4. Design failure as recoverable information. Separate gameplay consequence, learning feedback, praise and assessment; avoid shame, public ranking, punitive grind and answer-pattern guessing.
5. Specify age-appropriate text, voice, icon, controller/touch, captions, sensory settings, reading support, pause/save/resume, stopping cues, guardian/teacher summaries and safe social boundaries.
6. Minimise data and social exposure. Treat ads, purchases, targeting, profiling and third-party SDKs as blocked until accountable privacy/legal/store review. Any permitted ad must be clearly identified, non-intrusive, age-appropriate, non-targeted as required, easy to close/decline and unable to interrupt play, learning, recovery or stopping.
7. Test comprehension, independent play, learning, delight, frustration, accessibility, stopping and guardian/teacher usefulness as separate questions under approved child-research safeguards. Record limitations and adverse signals.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Child succeeds only with an adult or persistent prompt | Keep/scaffold the support and test the intended independence level | Completion is misreported as comprehension |
| Engagement rises but learning, trust, stopping or wellbeing worsens | Reject or redesign the mechanic | Retention is treated as a child outcome |
| Error identifies misconception | Give actionable task-linked feedback and a safe retry | Praise, shame or generic correction teaches nothing |
| Ad, purchase, social or SDK child treatment is unresolved | Disable the surface and escalate to accountable review | Revenue or data collection outruns child safety |
| Cultural or educational authority is missing | Mark content provisional and block approval claims | A design team impersonates an expert or community |

## Capability Contract

Read access to age, learning, safety, privacy, culture and evidence artefacts is required. Planning and review are read-only by default. Do not recruit/contact children, collect data, run studies, publish, purchase, enable SDKs or claim educational/legal/cultural approval without explicit authority and accountable expert oversight.

## Degraded Mode

Without expert-defined learning objectives or child-safe research, provide only a provisional experience and test plan. Without privacy/store/legal or guardian decisions, disable ads, purchases, social and third-party data paths. Without representative-child evidence, mark comprehension, learning, delight, wellbeing and stopping `not assessed`.

## Anti-Patterns

- Quiz pasted onto unrelated play. Fix: make the learning construct part of the core verb and feedback loop.
- Completion equated with learning. Fix: specify the construct, measure, transfer limit and separate evidence.
- “Kid-friendly” as an age specification. Fix: define cohorts, prior knowledge, language, abilities and context.
- Endless rewards, streak loss or nagging. Fix: use voluntary mastery, clear session endings, pause/save and neutral return.
- Public shame, punitive failure or pay-to-win rescue. Fix: private actionable feedback, safe retry and fair non-paying paths.
- Child ads/SDKs enabled by default. Fix: fail closed until privacy, store, legal, content and device evidence passes.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Age/cohort and learning-experience contract | Product, education and design | Cohorts, verb, scaffolds, feedback, evidence and limits are explicit |
| Child safety, privacy, stopping and commercial gate | Accountable owners and release | Data, social, ads, purchases, safeguards and disabled defaults are decided |
| Child/learning study and evidence matrix | Research, SRS and QA | Comprehension, learning, enjoyment, access, wellbeing and stopping remain separate |

## Examples

- `examples/river-cue-learning-loop.md` — a worked learning loop with scaffolding, safe failure, stopping, guardian evidence and an ad hold.

## References

- `references/child-learning-experience-contract.md` — cohort, learning, scaffolding, safety, stopping, research and ad schemas.
- `../../05-ux-process-research-and-psychology/ux-research-and-usability-testing/SKILL.md` — evidence and consent discipline.
- `../../00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/SKILL.md` and `../../00-cross-cutting-ops-qa-a11y/inclusive-and-assistive-design/SKILL.md` — ethics and inclusion owners.
- `../../../doctrine/design-doctrine.md` and `../../../doctrine/references/wcag-2.2-criteria.md` — shared quality/access floor.
<!-- dual-compat-end -->
