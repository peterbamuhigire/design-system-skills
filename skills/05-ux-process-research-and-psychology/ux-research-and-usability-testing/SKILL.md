---
name: ux-research-and-usability-testing
description: Use when planning or running UX research — user interviews, surveys, usability tests (moderated or unmoderated), card sorts, tree tests, diary studies — and when synthesizing findings into decisions. Routes here for research plans, screeners, interview guides, usability-test protocols, task scenarios, affinity/synthesis, severity rating, and turning evidence into design/product decisions (research-to-decision). Pick this when someone asks "how do we test this", "talk to users", "are we building the right thing", "why are users dropping off", or needs a defensible study instead of opinion.
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# UX Research and Usability Testing

<!-- dual-compat-start -->
## Use When
- You need to choose a research method and cannot tell which one answers the question (generative vs. evaluative, attitudinal vs. behavioural, qual vs. quant). Use `references/research-method-selector.md`.
- You are running user interviews, contextual inquiry, surveys, card sorts, tree tests, or diary studies and need a defensible plan, screener, and guide.
- You are running a usability test — moderated or unmoderated — and need a real protocol: tasks, success criteria, think-aloud, severity rating. Use `references/usability-test-protocol.md`.
- You have raw research notes and must synthesize them into findings and then into **decisions** (not a report that gets shelved).
- A stakeholder is asserting a user "fact" with no evidence, or a design debate has stalled on opinion and needs data to break the tie.

## Do Not Use When
- The work is applying cognitive/behavioural theory or heuristics to a design (Nielsen, Norman, Gestalt, biases, cognitive load) → use the sibling `ux-psychology`.
- The work is the end-to-end product/discovery process, RACI, and rituals → use the sibling `enterprise-ux-process`.
- The work is purely writing interface copy, microcopy, or error messages → use group 10 `ux-writing-and-microcopy` / `error-empty-and-system-messaging`.
- The work is building the prototype that the test will run on → use group 05 `wireframing-and-prototyping`.

## Required Inputs
- **The decision the research must inform.** Every study starts from a decision that is currently being made on a guess. No decision → no study.
- The research question(s), stated so they can be answered with evidence, and what you currently believe (the assumption being tested).
- The target user / segment, and access to them (recruiting source, screener constraints, incentive budget).
- The artifact under test where the method is evaluative: live product, prototype, wireframe, IA, or competitor.
- Timeline and constraints (how many participants, moderated vs. unmoderated, remote vs. in-person, regulatory/consent constraints).

## Workflow
1. **Anchor to a decision.** Write the decision, the question, and the current assumption in one line each. If you cannot name the decision the result will change, stop — you are doing research theatre. This is the research-to-decision spine; everything traces back to it.
2. **Select the method.** Use `references/research-method-selector.md` to pick on two axes — *generative vs. evaluative* and *attitudinal (what they say) vs. behavioural (what they do)*. Behaviour beats opinion when they disagree. Prefer the cheapest method that actually answers the question; do not run a survey to answer a "why".
3. **Plan the study.** Write a one-page plan: decision, question, method, participants (number + screener), tasks/topics, success metrics, schedule, and what result would change the decision in each direction. Pre-committing the decision rule prevents post-hoc rationalisation.
4. **Recruit honestly.** Screen for real target users; screen *out* friends, colleagues, and people who can guess the hypothesis. State the incentive. Get informed consent and recording permission in writing — non-negotiable for any session.
5. **Run the session.** For usability tests follow `references/usability-test-protocol.md` exactly: neutral intro, realistic task scenarios (never instructions that name the UI element), think-aloud, no leading or rescuing, observe behaviour first and ask "why" after. For interviews: open questions, past-behaviour over hypotheticals ("tell me about the last time…"), embrace silence, never pitch.
6. **Capture observations, not conclusions.** Record what happened (quote, action, where they got stuck) separately from your interpretation. Tag each with the participant ID so a claim can be traced to evidence later.
7. **Synthesize.** Cluster observations into themes (affinity mapping). For usability issues, rate severity (frequency × impact × persistence) so the team fixes the right things first. Quantify where honest to (task success rate, time, error count, SUS); never fabricate precision from a 5-person sample.
8. **Convert findings to decisions.** For each theme write: the finding → the evidence (participant count + quotes) → the recommended decision → confidence. Close the loop back to step 1. A finding with no recommended action is incomplete.
9. **Apply the doctrine lens.** Research is also how you defend that the product looks *authored*, not templated (`doctrine/design-doctrine.md` §0). Usability findings that surface "this feels generic / I didn't trust it" are slop signals (`doctrine/references/ai-slop-taxonomy.md`), not just nuisance comments — escalate them.
10. **Check accessibility coverage.** If the test never included a keyboard-only, screen-reader, low-vision, or motor-impaired participant, state that as a known gap; pair findings with `doctrine/references/wcag-2.2-criteria.md` before claiming the experience "works for users".

## Anti-Patterns
- **Research theatre** — running a study whose result cannot change any decision. The most common and most expensive mistake.
- **Leading the witness** — "Don't you find this easy?", naming the button in the task, nodding at the answer you want. Invalidates the data.
- **Rescuing the participant** — jumping in the moment they struggle. The struggle *is* the finding.
- **Asking people to predict their behaviour** — "Would you use this?" / "How much would you pay?" Self-reported future behaviour is near-worthless; ask about the last real instance instead.
- **Confirmation harvesting** — recruiting fans, cherry-picking the quote that fits the roadmap, ignoring the disconfirming participant.
- **Sample-size theatre** — reporting "80% of users" from 5 people, or running 30 sessions when 5 would have surfaced the same top issues (Nielsen's diminishing-returns curve).
- **The shelved report** — a 40-slide deck with no recommended decision. Findings without "so we should…" are inert.
- **Opinion laundering** — presenting a designer's preference as a "research finding" with no traceable evidence.

## Outputs
- A one-page research plan (decision → question → method → participants → success criteria → decision rule).
- A screener and a moderation guide / interview guide.
- A usability-test protocol with task scenarios and pre-stated success criteria.
- A synthesis: themes, severity-rated issues, quantified metrics where honest, traced to participant evidence.
- A research-to-decision summary: each finding paired with a recommended decision and a confidence level.

## Examples
- See `examples/research-plan-and-synthesis.md` — a real, worked study for an onboarding flow: the plan, the moderated unmoderated mix, the raw observations, the affinity synthesis with severity ratings, and the research-to-decision table that changed the roadmap. Never lorem.

## References
- `references/research-method-selector.md` — choose the method by generative/evaluative × attitudinal/behavioural; cost vs. answer-fit.
- `references/usability-test-protocol.md` — a real moderated + unmoderated protocol: tasks, think-aloud script, success criteria, severity rating, SUS.
- `doctrine/design-doctrine.md` — §0 Mission (the authored-not-templated moat) and the Anti-Slop Charter; usability findings are evidence the product reads as human-made.
- `doctrine/references/ai-slop-taxonomy.md` — the interface/product slop tells; "feels generic / didn't trust it" findings map here.
- `doctrine/references/wcag-2.2-criteria.md` — accessibility coverage gate; a study without disabled participants is incomplete, not done.
- Sibling skills: `05-ux-process-research-and-psychology/ux-psychology` (theory to apply), `enterprise-ux-process` (the surrounding process), `wireframing-and-prototyping` (what you put under test).
<!-- dual-compat-end -->
