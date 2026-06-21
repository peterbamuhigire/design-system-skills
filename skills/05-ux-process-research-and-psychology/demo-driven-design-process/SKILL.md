---
name: demo-driven-design-process
description: Use when running the actual working process of refining a design or feature by iteration — driving the demo → feedback → next-demo loop (Kocienda's "creative selection" made operational), deciding what a demo must prove and what to deliberately fake (the fidelity ring + non-goals), "living on" / dogfooding a build to judge it over time, telling an algorithm decision (codify a rule, an objective arrow of improvement) from a heuristic decision (resolve by taste + time, never by a metric or AI pick), converging on an authored choice through rounds, and capturing the decision so it sticks. Routes here for "how do we iterate on this", "run the demo loop", "is this a taste call or a metric call", "what should this demo prove", "we keep redesigning and not converging", "should we A/B this", "let's dogfood it", "capture why we picked this". Pairs with `wireframing-and-prototyping` (that skill picks the fidelity of one artifact; this one runs the multi-round loop those artifacts move through).
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# Demo-Driven Design Process (Creative Selection, Operationalised)

<!-- dual-compat-start -->
## Use When
- You have an idea or a half-formed design and need to **refine it by iteration** — not produce
  one big-bang artifact and not write a spec and execute it, but run a **continuing progression of
  concrete working demos**, each a deliberate variation on the last, with feedback as the selection
  pressure that decides which variation survives.
- You must decide **what a given demo has to prove** and, just as important, what it is allowed to
  fake or omit — drawing the fidelity ring and writing the explicit **non-goals** before building.
- A choice is stuck — the team keeps re-arguing it, or keeps redesigning without converging — and
  you need to tell whether it is an **algorithm decision** (codify a rule; there is an objective
  arrow of improvement) or a **heuristic decision** (resolve only by demo + taste + time), and run
  the right procedure for each.
- Someone proposes settling a taste decision with an **A/B test, a metric, or an AI recommendation**,
  and you need to decide whether that is evidence (admissible) or authority (not).
- You need to judge whether the choices **add up over time**, not just in one review — i.e. you need
  to **live on the build / dogfood it** before earning an opinion.
- A round has converged and you need to **capture the decision** — what was chosen, what it beat,
  why, and on what evidence — so it is not silently re-litigated or lost.

## Do Not Use When
- You are choosing the **fidelity of a single artifact** (paper → lo-fi → mid-fi → hi-fi →
  clickable) or wiring one wireflow → use `wireframing-and-prototyping`. That skill produces *a*
  demo; **this** skill runs the *loop of demos* and decides what each must prove. They pair: pick
  the rung there, run the rounds here.
- You are running the **research protocol** itself (interviews, moderated tests, synthesis) →
  `ux-research-and-usability-testing`. That generates the *feedback*; this skill is the engine that
  *consumes* feedback to vary and re-decide.
- You are facilitating a **critique session** or running a heuristic evaluation as a one-off review
  → `design-critique-and-review-facilitation` / `heuristic-evaluation-and-design-critique`. Those
  are review events; this is the longitudinal build-loop they sit inside.
- You are making the **one distinctive aesthetic decision** for an artifact (the signature move) →
  `04…/distinctive-by-design`. That states the ONE decision; this skill is the loop you run to
  refine it after it is stated.

## Required Inputs
- **The one thing this loop is trying to get right** — stated concretely (this interaction, this
  threshold, this moment), not as a direction ("make it feel premium"). A direction is not a
  decision; the loop exists to force the abstraction down to something you can choose between.
- **A way to make a real, running demo** of that one thing — even at the lowest honest fidelity.
  Mock-ups of mock-ups, specs, and slides do not count (see Anti-Patterns: imaginary puppies).
- **A feedback source** — yourself living on it, a teammate, a test participant — and a **single
  decider** for each round (the person who selects the surviving variation; access to that room is
  earned by making the work better, not by rank).
- **The algorithm/heuristic call** for the decision at hand (see `references/decision-capture.md`),
  because it sets *how* the decision is allowed to be settled.

## Workflow
1. **Frame the one decision, and classify it.** Name the single thing this round must resolve, as a
   concrete instance. Then classify it: is it an **algorithm** (there is an objective arrow — faster,
   fewer taps, higher contrast-ratio — that always points one way → codify the rule and move on) or a
   **heuristic** (a real value but no objective arrow — a duration, a colour, a swipe threshold, a
   tone → resolvable only by demo + taste + time)? Getting this wrong is the root error: settling a
   heuristic with a metric is the "41 shades of blue" mistake
   (`doctrine/references/creative-selection-and-taste.md`). See `references/decision-capture.md` for
   the test.
2. **Draw the fidelity ring and write the non-goals.** Before building, draw a conceptual ring
   around the *one thing the demo must prove*. Build that at the highest fidelity it needs (the
   lamppost that bears the actor's weight); deliberately **fake or omit everything outside the ring**
   (the empty hat-shop facade); take extra care only at the boundary where the fake meets the real.
   Write the **explicit non-goals** — what this demo is *not* trying to show — so feedback lands on
   the idea and not on the scaffolding. Pick the cheapest honest fidelity with
   `wireframing-and-prototyping`. See `references/demo-loop-and-fidelity.md`.
3. **Build the smallest real, running artifact that proves it.** A demo is *real, running, concrete,
   and focused*. Build only inside the ring. The point is to have a concrete thing in the room to
   react to — never hold the design discussion about an imaginary artifact.
4. **Live on it / get feedback.** For a heuristic you cannot judge from a single look — **live on the
   build** ("dogfood" it) long enough to feel whether the choice adds up over time, or route a real
   feedback pass through `ux-research-and-usability-testing`. Refinement is **longitudinal**. If you
   have not lived on the thing, you have not yet earned an opinion about whether it works.
5. **Select by taste; let the feedback cause a fresh divergence.** The single decider selects the
   surviving variation by **conviction**, not by deferring to a number or an AI pick (metrics and AI
   suggestions are admissible as *evidence to inform*, never as *authority to decide* —
   `doctrine/design-doctrine.md` §2). Then let what you learned cause the **next** deliberate
   variation. Converge on a demo → diverge on the feedback → converge again. Prefer **subtraction**:
   the strongest next demo is often the one with something removed ("edit for less", Miller 7±2).
6. **Repeat until it converges — then stop.** Run rounds until further variation stops improving the
   one thing (taste, not a target number, tells you you're there). Resist both early-stopping (ship
   the first that works) and endless polishing. "We picked one and moved on" is a virtue once the
   loop has done its job.
7. **Capture the decision.** Record what was chosen, what variations it beat, *why* (the conviction
   in one sentence), the algorithm/heuristic class, and any metric/AI signal logged as **convergence,
   not endorsement**. This stops the choice being silently re-litigated and feeds the next loop. See
   `references/decision-capture.md` and `examples/save-search-toast-iteration-log.md`.

## Anti-Patterns
- **Arguing about imaginary puppies.** Holding a design discussion over specs, slides, or a
  mock-of-a-mock with nothing real and running in the room. Build the smallest real artifact that
  proves the one idea, then react to *it* (`doctrine/references/creative-selection-and-taste.md`).
- **Outsourcing a taste decision to a metric.** A/B-testing 41 shades of blue and shipping the
  winner — picking the best of the options you were *handed* and paying the opportunity cost of the
  far-better design conviction would have reached. A metric may *inform* a heuristic; it may never
  *decide* it. (Same error, restated: outsourcing the pick to an AI recommend-list — both launder
  the choice to the mean the Mission exists to escape.)
- **Using an algorithm where a heuristic is required (or vice-versa).** Tuning an animation's
  duration with a conversion metric; or "deciding by taste" something that has a hard objective
  arrow (load time) and should just be codified.
- **Demos with no ring.** Polishing everything to the same fidelity so feedback scatters across
  scaffolding instead of landing on the one idea; or, conversely, faking the very thing the demo was
  supposed to prove.
- **Reviewing once and calling it judged.** Shipping a heuristic off a single look without living on
  it — refinement is longitudinal; one critique is not enough signal.
- **Big-bang build / spec-then-execute.** Skipping the loop entirely: producing one large artifact
  from a written spec, with no progression of variations and no selection pressure.
- **Never converging.** Treating every round as a reason to add more, never letting taste call the
  loop done. Decisiveness is part of the craft.
- **Losing the decision.** Converging and then not capturing *why*, so the same argument is had again
  three weeks later with no record of what was already tried and beaten.

## Outputs
- A **classified decision**: the one thing being resolved + its algorithm/heuristic class + the
  procedure that follows from the class.
- A **demo plan per round**: the fidelity ring, the explicit non-goals, the cheapest honest fidelity.
- An **iteration log**: the progression of demos, the feedback each round, the taste call and its
  one-sentence conviction, and the convergence point — see the worked example.
- A **decision record**: what was chosen, what it beat, why, on what evidence (with any metric/AI
  signal logged as convergence, not authority), ready to hand to dev/critique/handoff.

## Examples
- See `examples/save-search-toast-iteration-log.md` — a real worked demo-driven iteration for one
  feature ("confirm a saved search without yanking the user out of their flow"): four demos, the
  feedback and the taste decision each round, the algorithm-vs-heuristic calls, convergence by
  subtraction, and the captured decision record. Representative content throughout — never lorem.

## References
- `references/demo-loop-and-fidelity.md` — the demo → feedback → next-demo loop run end to end; what
  makes a demo *real, running, concrete, focused*; the fidelity ring + non-goals (Hollywood-backlot)
  method for what to make real vs fake; "live on it" / dogfooding as longitudinal refinement.
- `references/decision-capture.md` — the algorithm-vs-heuristic test (when to codify a rule vs make a
  judgement call), the "metric/AI is evidence, never authority" rule, convergence-by-taste, and the
  decision-record template that captures what was chosen and why.
- `doctrine/references/creative-selection-and-taste.md` — the doctrine this skill operationalises
  (the five working rules, the "41 shades of blue" lesson, the inspiration→…→taste→empathy chain).
  This skill *operationalises* that reference; it does not duplicate it.
- `doctrine/design-doctrine.md` — §0 (the moat is looking human-made; push away from the convergent
  mean) and §2 (the sourcing-authority asymmetry rule — a taste decision traces to human conviction,
  never to a number or a model's pick).
- Pairs with `wireframing-and-prototyping` (pick one artifact's fidelity there; run the loop here)
  and feeds `design-critique-and-review-facilitation` / `heuristic-evaluation-and-design-critique`
  (each round's feedback pass) and group-09 handoff (the captured decision).
<!-- dual-compat-end -->
