---
name: wireframing-and-prototyping
description: Use when sketching, wireframing, or prototyping a flow or feature before high-fidelity design or build — choosing the right fidelity (paper sketch, lo-fi wireframe, mid-fi greybox, hi-fi mockup, clickable/coded prototype), building wireflows that chain screens to user decisions, deciding when a clickable prototype is worth it, and avoiding the trap of jumping straight to pixel-perfect comps. Routes here for "wireframe this", "prototype the flow", "lo-fi vs hi-fi", "wireflow", "should I make this clickable", "rapid concept sketch", or "what should we prototype before we build".
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# Wireframing & Prototyping

<!-- dual-compat-start -->
## Use When
- You need to design a screen, flow, or feature and must decide **how rough or finished** the
  artifact should be — a paper sketch, a lo-fi wireframe, a mid-fi greybox, a hi-fi mockup, or a
  clickable/coded prototype.
- You are mapping a multi-screen flow and need a **wireflow** — wireframes wired together by the
  user's decisions and the system's responses (not just a static screen inventory).
- A stakeholder asks to "see it working" and you must decide whether a **clickable prototype**
  earns its cost, and at what fidelity.
- You want to validate structure, hierarchy, or a flow **before** investing in visual design,
  tokens, or front-end code.
- You need to hand a tested concept to high-fidelity design or to dev, with the open questions
  resolved at the cheapest possible fidelity.

## Do Not Use When
- You are running interviews, surveys, or moderated usability tests, or synthesising research into
  decisions → use `ux-research-and-usability-testing` (this skill produces the **stimulus** you
  test; that skill runs the **test**). The two are designed to pair — see Workflow step 5.
- You are past structure-validation and producing the final visual design, tokens, or
  component specs → use group 09 (`design-tokens-and-naming`, `component-library-architecture`,
  `design-handoff-and-dev-spec`).
- You are designing one component's full state coverage (empty/error/loading) → use
  `empty-error-and-loading-states` (group 04). Wire those states *into* the wireflow here; spec
  them there.
- You are choosing typefaces, palettes, or doing pixel craft — that is premature at wireframe
  fidelity and is its own slop risk (see Anti-Patterns).

## Required Inputs
- The **goal of the artifact**: what decision or risk this wireframe/prototype must resolve
  (structure? flow? feasibility? desirability? a specific interaction?). Fidelity follows from this.
- The **user task(s) and entry points** the flow must cover, ideally from research (personas, top
  tasks, JTBD). Without these you are decorating, not designing.
- The **audience for the artifact**: yourself (think-tool), the team (align), a test participant
  (validate), or a client/exec (sell). Audience sets the minimum viable fidelity.
- Known constraints: platform, key content/data, must-have steps, and any hard system responses
  (errors, async waits) that change the flow.

## Workflow
1. **State the artifact's job, then pick the lowest fidelity that does it.** Name the one decision
   the artifact must resolve and choose the *cheapest* rung of the fidelity ladder that resolves it.
   Higher fidelity is not better — it is slower to make, harder to change, and biases reviewers
   toward polish over structure. See `references/fidelity-ladder.md` for what each rung is for and
   when it is the right one.
2. **Wireframe the screens at that fidelity.** Lay out content blocks, hierarchy, and controls — not
   colour, not final copy, not real type. Use real-ish content (counts, labels, lengths) so the
   layout is honest; use greyboxing and placeholder rectangles for media. Respect the doctrine's
   **anti-slop** rule even here: a wireframe still makes *deliberate* layout choices (grid, reading
   order, primary action) rather than reflexively dropping evenly-spaced cards
   (`doctrine/design-doctrine.md` §2).
3. **Wire the screens into a wireflow.** Connect each screen to the next via the user's **decision**
   and the system's **response**. Branch on the real forks: success vs error, empty vs populated,
   first-run vs return, happy path vs recovery. A flow that only shows the happy path hides exactly
   the risk you are prototyping. See `examples/wireflow-example.md`.
4. **Add interactivity only where it buys validation.** Make it clickable only if the *transitions*
   or *timing* are part of what you must test (can users find the path? does the wait feel broken?).
   A click-through of lo-fi screens tests navigation; a hi-fi coded prototype tests feasibility and
   feel. Do not raise fidelity to add clicks you do not need — see the fidelity-vs-interactivity
   matrix in `references/fidelity-ladder.md`.
5. **Pair with research to test it.** The wireframe/prototype is the *stimulus*; route to
   `ux-research-and-usability-testing` to run the protocol (tasks, think-aloud, success criteria),
   then fold findings back as edits at the **same low fidelity** before climbing. Iterating cheap is
   the whole point — every loop you spend at lo-fi is a loop you did not spend redoing pixels.
6. **Promote, don't restart, when validated.** When structure and flow are settled, hand off to
   high-fidelity design (group 09 handoff/tokens/components) with the resolved questions annotated
   on the wireflow, so hi-fi work starts from answers, not from a blank canvas.

## Anti-Patterns
- **Starting in hi-fi.** Opening Figma in full colour with real type for an unvalidated flow. It
  costs 5× to change, and reviewers critique the gradient instead of the journey.
- **Fidelity theatre.** Making it *look* finished to impress, when the artifact's job was to resolve
  structure. Polish on an unvalidated flow is wasted polish — and reads as the AI "looks-done"
  default the doctrine exists to defeat (`doctrine/design-doctrine.md` §0).
- **Happy-path-only wireflows.** No error, empty, loading, or recovery branch — so the prototype
  validates nothing that was actually risky.
- **Lorem everywhere.** Fake even-length text hides real overflow, truncation, and hierarchy
  problems. Use representative content lengths.
- **Premature pixel craft.** Choosing fonts, palettes, shadows, or exact spacing at wireframe stage.
  Those are downstream decisions; deciding them here both wastes effort and locks in choices before
  the structure that should drive them exists.
- **Clickable for its own sake.** Spending days wiring micro-interactions when a paper sketch would
  have answered the question.
- **Never lowering fidelity to iterate.** Treating each test round as a reason to add polish instead
  of going *back down* to change structure cheaply.

## Outputs
- A fidelity decision: the chosen rung + the one sentence justifying it against the artifact's job.
- Wireframes at that fidelity (content blocks, hierarchy, primary action — greyboxed media).
- A **wireflow**: screens connected by user decisions and system responses, with the real branches
  (success/error/empty/first-run/recovery) shown.
- Optionally a clickable prototype, only where transitions/timing are part of what's being tested.
- A handoff packet: the validated wireflow + resolved/open questions, ready for group-09 hi-fi.

## Examples
- See `examples/wireflow-example.md` — a worked, branch-complete wireflow for a real feature
  ("save a search and get notified"), with the fidelity choice stated and justified, the screen
  inventory, the decision/response wiring, the error/empty/loading branches, and the
  pair-with-research test plan. Not lorem — representative content throughout.

## References
- `references/fidelity-ladder.md` — the five rungs (paper sketch → lo-fi → mid-fi greybox →
  hi-fi mockup → clickable/coded prototype): what each is *for*, when it is the right rung, what it
  cannot tell you, and the fidelity-vs-interactivity matrix.
- `doctrine/design-doctrine.md` — §0 (the "looks human-made" moat / no "looks-done" theatre) and
  §2 (the Anti-Slop Charter — deliberate layout choices apply even at wireframe stage).
- Pairs with `ux-research-and-usability-testing` (this group) — wireframe is the stimulus; that
  skill runs the test.
- For UI/web work that follows hi-fi promotion: `doctrine/references/wcag-2.2-criteria.md` and
  `doctrine/references/web-performance-budgets-2026.md` (validate target sizes, focus order, and
  perceived-performance waits that your wireflow's loading branches imply).
<!-- dual-compat-end -->
