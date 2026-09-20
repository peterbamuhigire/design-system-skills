# Six-book actionable study: design engine Kaizen

Date: 2026-09-20
Scope: C:\wamp64\www\design-system-skills
Method: local full-text study, paraphrased extraction, source locators, implementation mapping, and regression-oriented acceptance criteria.

This document records original synthesis from the six user-supplied Markdown books. It does not reproduce book text, figures, code, or branding. The supplied Markdown files are the source corpus; current accessibility, browser, framework, and standards claims remain subject to the engine's currentness gate.

## Source register

| ID | Supplied source | Use in this Kaizen |
|---|---|---|
| B01 | C:\Users\Peter\Desktop\inclusiz_markdown\_OceanofPDF.com_Software_Requirements_Essentials_Core_Practices_-_Karl_Wiegers (1).md | Requirements quality, elicitation, analysis, validation, change control |
| B02 | C:\Users\Peter\Desktop\inclusiz_markdown\Inclusive Components (Heydon Pickering) (z-library.sk, 1lib.sk, z-lib.sk).md | Semantic components, states, focus, progressive enhancement, content resilience |
| B03 | C:\Users\Peter\Desktop\inclusiz_markdown\Refactoring UI.md | Visual hierarchy, spacing, type, color, depth, imagery, empty states |
| B04 | C:\Users\Peter\Desktop\inclusiz_markdown\Rocket Surgery Made Easy The Do-It-Yourself Guide to Finding and Fixing Usability Problems (Voices That Matter) (Krug, Steve) (z-library.sk, 1lib.sk, z-lib.sk).md | Lightweight usability testing and fix/retest loops |
| B05 | C:\Users\Peter\Desktop\inclusiz_markdown\Storytelling with Data - Cole Nussbaumer Knaflic.md | Audience/action framing, chart choice, decluttering, visual attention, narrative QA |
| B06 | C:\Users\Peter\Desktop\inclusiz_markdown\_OceanofPDF.com_Design_That_Scales_-_Dan_Mall.md | Product-first design systems, pilots, extraction, governance, adoption metrics |

## B01 — Software Requirements Essentials

### Actionable principles

- Start with the problem, desired outcome, stakeholders, boundaries, constraints, decision authority, and success measures before choosing a visual solution.
- Elicit tasks, events, responses, data relationships, quality attributes, exceptions, and operational constraints; do not treat a happy-path feature sentence as a design brief.
- Analyse origin, dependencies, assumptions, conflicts, risks, decomposition, and verifiability. Record what is known, inferred, and unresolved.
- Use models, prototypes, prioritisation, and review to reduce uncertainty before a costly implementation.
- Validate requirements through peer review, conceptual checks, acceptance criteria, baselines, and controlled change. A syntactically valid artefact is not automatically release-ready.
- Tailor process weight to risk; do not turn a useful checklist into a bureaucracy tax for low-risk work.

### Applied to the engine

The engine now treats high-risk design work as a traceable chain:

problem/outcome → audience/task → design decision → token/component → state/interaction → evidence → release verdict

The delivery-evidence validator now rejects missing retained evidence, mismatched hashes, missing independent reviewers, any failed declared stage, and any failed declared check. This makes the requirements distinction between specified, verified, and accepted executable rather than merely advisory.

### Required future fixture

For a form, dialog, table, and dashboard slice, provide normal, alternative, error, recovery, accessibility, responsive, and performance scenarios. Missing scenarios remain NOT_ASSESSED.

## B02 — Inclusive Components

### Actionable principles

- Prefer native semantic controls where they provide the required behavior; expose state to visual users, keyboard users, and assistive technology.
- Model empty, loading, success, error, live-status, and focus-recovery states as part of the component contract.
- Keep navigation semantics distinct from application-menu semantics; do not put essential instructions only in tooltips.
- Treat tabs, collapsibles, sliders, tables, and cards as content-and-state systems, not isolated visual motifs.
- Preserve source order, keyboard access, touch usability, deep-link/fallback behavior, and meaningful labels across responsive variants.
- Test variable content: long labels, missing images, varied ratios, narrow widths, localization expansion, and no-JavaScript fallback.
- Do not cargo-cult historical ARIA, WCAG, browser, or screen-reader advice. Current WCAG 2.2, APG, browser behavior, and actual assistive-technology combinations are authoritative.

### Applied to the engine

The component and QA contracts are being expanded around state matrices, semantic-pattern choice, focus outcomes, content variation, and progressive enhancement. The research and practical design skills now link to this source study so that a generated component is expected to carry behavior and evidence, not only anatomy and CSS intent.

### Required future fixture

An accessible booking flow must test: native date/time controls where appropriate, validation timing, preserved input on error, keyboard focus after submit, live status, narrow layout, long names, empty availability, failure recovery, and reduced motion.

## B03 — Refactoring UI

### Actionable principles

- Work feature-first: establish the useful structure and hierarchy before polishing isolated details.
- Use grayscale and restrained choices to solve layout and hierarchy before colour distracts from the information architecture.
- De-emphasise secondary content rather than making every item compete; make labels, destructive actions, and primary actions semantically obvious.
- Treat spacing as a system of relationships. Adjust padding, grouping, density, and alignment together instead of nudging arbitrary pixels.
- Build a type scale for the product context, then tune weight, line-height, measure, numbers, and tracking for legibility.
- Use a small colour system with clear roles, contrast checks, temperature/association awareness, and explicit interaction states.
- Use borders, shadows, elevation, overlap, imagery, backgrounds, and empty states intentionally; reduce ornamental noise.
- When a screen feels generic, add product personality through coherent choices rather than random decoration.

### Applied to the engine

Practical UI guidance now references a feature-first, hierarchy-first, grayscale-first workflow. The token example now uses semantic danger and control-radius aliases, making a small but testable separation between primitive values, semantic roles, and component consumption. Token validation is structural and explicitly does not claim contrast or standards certification.

### Required future fixture

The workshop booking slice must show: a clear primary action, low-contrast secondary metadata, a visibly distinct destructive/cancel action, predictable spacing groups, a readable narrow-width type scale, and a useful empty state.

## B04 — Rocket Surgery Made Easy

### Actionable principles

- Qualitative observation answers where people struggle and why; quantitative measures answer how often and how much. Use each for its proper decision.
- Test early with sketches, prototypes, and incomplete flows. A small realistic task beats a polished but artificial demonstration.
- Recruit representative users or proxies, create realistic scenarios, avoid leading participants, and keep the facilitator neutral.
- Ask participants to think aloud without coaching them toward the intended control. Observe behavior, hesitation, errors, workarounds, and interpretation.
- Capture consent, privacy boundaries, task success, severe blockers, and notable quotes/paraphrases without overclaiming statistical certainty.
- Fix the smallest high-impact set, then retest. Usability improvement is a repeated loop, not a single certification event.
- Remote testing still needs a controlled script, clear recording/consent rules, and a way to observe the participant's actual interaction.

### Applied to the engine

The research skill now treats a lightweight usability loop as a normal design-engine output: research question, participant/task rationale, neutral scenario, observation log, severity, fix decision, retest result, and unresolved uncertainty. The engine must not invent user evidence; absent testing remains NOT_ASSESSED.

### Required future fixture

Run three to five task-oriented sessions against the workshop booking slice, record the first critical friction, apply one bounded change, and repeat the same task. Report this as directional evidence, not a population estimate.

## B05 — Storytelling with Data

### Actionable principles

- Identify the audience, the decision they must make, and the single Big Idea before selecting a chart.
- Choose visual encodings that match the comparison: position and length are generally easier to compare than area, colour, or decorative form.
- Remove clutter, unnecessary gridlines, redundant legends, excessive precision, and non-informative decoration.
- Use preattentive cues such as position, size, and restrained colour to focus attention; preserve accessibility and include textual/contextual alternatives.
- Use direct labels and action-oriented titles where they reduce interpretation cost.
- Storyboard the beginning, evidence, and conclusion; review the narrative in sequence and out of sequence.
- Test a chart with a real task and audience, not only by judging whether it looks polished.

### Applied to the engine

Chart selection is now paired with audience, action, Big Idea, decision context, chosen encoding, decluttering pass, accessibility alternative, and validation evidence. The chart skill must distinguish an analytical view from a decorative illustration and must preserve uncertainty instead of manufacturing precision.

### Required future fixture

For a booking operations chart, state the decision, define the comparison, choose a chart form, label the takeaway, remove non-essential marks, provide a text summary, and record whether a representative reviewer could answer the task.

## B06 — Design That Scales

### Actionable principles

- Treat a design system as a connected, versioned product with owners, users, consumers, maintenance, and a reason to exist.
- Pilot inside real product work; extract and reuse components after patterns prove useful. Avoid building a disconnected catalogue without a consumer.
- Use variation evidence to decide what deserves abstraction. Do not invent another layer merely because two examples look superficially similar.
- Governance should clarify what is covered, why it exists, who decides, when changes happen, where work is recorded, and how contribution/review/deprecation work.
- Prefer collaborative, browser-first iteration and early token decisions over rigid sequential handoff.
- Measure outcomes: task success, defects, accessibility failures, migration effort, reuse, confidence, contribution health, and maintenance cost—not only adoption counts.
- Documentation should lead with working examples and product context; a component inventory alone is not enablement.
- Aim for unity without forcing every product context into uniformity.

### Applied to the engine

The implementation plan's first rendered vertical slice and external-consumer proof are now explicit acceptance targets. The engine's token and evidence work supports versioned contracts, and the future metric register must distinguish measured outcomes from unverified aspirations.

### Required future fixture

The workshop booking slice must be rendered from the token example, reviewed as a real product flow, extracted into reusable patterns only where variation supports it, and exercised by an independent consumer fixture with installation, update, and rollback evidence.

## Integrated operating model

Every major design output should carry:

1. A concise problem/outcome brief and audience/action statement.
2. A state and content matrix, including failure and recovery.
3. A semantic/accessibility and responsive plan.
4. A token/component decision record with rationale and uncertainty.
5. A prototype or render evidence bundle.
6. A lightweight usability observation and fix/retest record when user-facing risk warrants it.
7. A release verdict that distinguishes schema validity, evidence completeness, and human acceptance.
8. An owner, change path, and metric plan.

## Adoption boundaries

Adopted now: original synthesis, source locators, evidence-gate hardening, label-blind routing evaluation, token structural guardrails, semantic token example improvements, responsive/interaction routing coverage, and implementation fixtures.

Not adopted as fixed doctrine: book-specific numerical targets, copied code or figures, historical accessibility claims without current verification, and aesthetic preference presented as objective truth.

Current implementation status: the first tranche is implemented and tested; rendered human review, real consumer migration, current browser/assistive-technology verification, and outcome baselines remain NOT_ASSESSED until their evidence is produced.
