---
name: ux-psychology
description: Cognitive psychology for premium web design. Gestalt principles, Nielsen's 10 heuristics, Norman's 3 design levels, System 1/2 thinking with cognitive biases, Branson's three HCI paradigms (Building/HIP/Design Thinking), working-memory rules (Miller 7±2, chunking, stacking, cognitive load), four-stage cognitive affordance discipline (Presence/Visibility/Recognizability/Intelligibility), and Deacon's three levels of UX scope. Use for premium $20k+ websites to justify quality and prevent common psychological UX mistakes.
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# Ux Psychology
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- A design or layout needs grouping/hierarchy diagnosed through Gestalt lenses (proximity, similarity, common region, closure, continuity).
- You must justify or defend UX quality on a premium $20k+ build, naming the principle a choice rests on rather than asserting taste.
- A flow feels confusing or high-friction and you need a cognitive-load read: Miller's 7±2, chunking/stacking, Sweller's intrinsic vs. extraneous load.
- An interaction's affordances are unclear and you want the four-stage discipline — Presence, Visibility, Recognizability, Intelligibility — applied to controls and signifiers.
- You need to map a screen against Nielsen's 10 heuristics or Norman's three levels (visceral/behavioral/reflective) and turn each gap into a concrete change.
- Aligning stakeholders on which HCI paradigm (Building / HIP / Design Thinking) a decision belongs to, or declaring UX scope (Single Interaction / Journey / Relationship) in a proposal.
- Spotting System 1/2 friction or dark patterns that erode trust on a conversion path.

## Do not use when
- You need to run usability sessions, interviews, or analyze test results — use `05-ux-process-research-and-psychology/ux-research-and-usability-testing`.
- You want a structured heuristic walkthrough or design critique deliverable — use `05-ux-process-research-and-psychology/heuristic-evaluation-and-design-critique` (this skill supplies its psychology vocabulary, not the critique format).
- The work is visual/brand differentiation or component-level UI patterns — use `03-web-and-ui-design/distinctive-by-design`, `interaction-design-patterns`, or `motion-design`.
- You only need a non-psychological correctness check (copy, accessibility audit, performance).

## Required inputs
- The specific screen, flow, or interaction under review (mockup, URL, or described artifact) — concrete enough to point at named elements.
- The user goal and decision context for that screen, so cognitive-load and affordance judgments are anchored to a real task.
- Brand, audience, regional, and conversion context that determines whether a psychological tradeoff is acceptable.

## Workflow
1. Read the artifact and the decision context before applying rules.
2. Use only the parts of the preserved guidance that matter to the current task.
3. Review or revise the work using this skill as a focused quality lens.
4. Return actionable changes or acceptance criteria instead of abstract theory.

## Quality standards
- Recommendations must be concrete enough to apply immediately.
- Changes should improve consistency, usability, or credibility without flattening the brand.
- The standard should support downstream implementation rather than slow it down.

## Anti-patterns
- Do not apply every rule mechanically when only a subset is relevant.
- Do not give generic critique with no change implications.
- Do not override project reality with taste-based preferences alone.

## Outputs
- Revisions, review findings, acceptance criteria, or quality guidance tied to the artifact under review.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

## Examples

- `examples/psychology-critique-worked.md` — a worked critique of one real screen (a coffee-subscription checkout) through named psychology lenses: Gestalt grouping, Nielsen's heuristics, Norman's affordances/signifiers, cognitive load (Miller/Sweller), and Hick's/Fitts's law. Each finding pairs the principle with the design change it implies; ends with a findings-to-changes table.

## References

- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter; psychological quality is part of looking deliberately human-made, not templated.
- `doctrine/references/ai-slop-taxonomy.md` — the interface/product slop tells whose cognitive cost this skill explains.
- Sibling skills: `03-web-and-ui-design/distinctive-by-design`, `03-web-and-ui-design/interaction-design-patterns`, `03-web-and-ui-design/motion-design`.
- `references/legacy-guidance.md` — Gestalt, Nielsen, Norman, Krug; **+ working-memory rules + four-stage cognitive affordance** (added 2026-05-04). Read only the specific files under `references/` that match the task.
- `references/three-paradigms-of-hci.md` — Building / HIP / Design Thinking; cockpit-voice example for stakeholder alignment
- `references/three-levels-of-ux-scope.md` — Single Interaction / Journey / Relationship — declare in every proposal

