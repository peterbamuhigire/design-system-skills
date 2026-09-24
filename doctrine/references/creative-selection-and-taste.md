# Reference: Creative Selection & Taste (the production method behind the Mission)

Parent: [`../design-doctrine.md`](../design-doctrine.md) — process-side companion to the Mission
(§0) and the sourcing-authority asymmetry rule (§2).

**When to read:** before running a design iteration, a critique, or any decision where a metric,
test or AI suggestion is being offered as the reason for a visual or interaction choice.

The Mission says the moat is looking human-made: make an authored, non-convergent choice. That is
the *what*. This reference is the *how* — the production method by which skilled human work gets
made, so that our skills produce authored work rather than the generated mean.

---

## 1. The core method: the demo-selection loop

Authored work does not come from a single large build, nor from writing a specification and
executing it. It comes from a **demo → feedback → next-demo loop**:

1. Build the smallest working demo that expresses one idea.
2. Show it to the people whose judgement matters and collect concrete reactions.
3. Make a deliberate variation that responds to the feedback.
4. Select: a skilled person's taste chooses which variation survives.
5. Converge, let the next round of feedback open a fresh divergence, converge again.
6. Capture the converged decision (section 5) and stop when further variation no longer improves
   the thing.

Variation plus selection, repeated. Taste does the selecting; iteration does the converging. This
is neither brainstorming (no concrete artefact) nor A/B testing (selection handed to a metric).
It is the mechanism that reliably produces the authored choices the Mission demands. The
step-by-step running procedure lives in
`skills/05-ux-process-research-and-psychology/demo-driven-design-process/references/demo-loop-and-fidelity.md`.

---

## 2. The five working rules

Other skills cite these by number; keep the numbering stable.

1. **The working demo is the unit of progress.** Progress is measured in real, running
   artefacts, not in abstractions. Never hold a design discussion without a concrete thing to
   react to; debating two people's imagined versions of a screen settles nothing. A mock-up of a
   mock-up is not a demo. (The same logic makes `distinctive-by-design` ban lorem ipsum:
   placeholder text produces placeholder design.) Build the smallest real artefact that proves
   the one idea, then react to *it*.

2. **Live on it.** A refinement cannot be judged in a single review. Use the build in daily work
   for days, not minutes, to feel whether the choices add up over time. Refinement is
   longitudinal. Until you have lived on the thing, you have not earned an opinion on whether it
   works.

3. **Concrete over abstract.** Decide on specific instances — *this* colour value, *this*
   duration, *this* word — not directions such as "make it feel more premium". A direction is not
   a decision; the demo forces the abstraction down to options you can actually choose between.

4. **Know whether you face an algorithm or a heuristic.** Some decisions have an objective arrow
   of improvement that always points one way — a faster page load is simply better; these are
   **algorithms** and can be codified or measured. Others — an animation's duration, a signature
   colour, a swipe threshold — have a best value but no objective arrow; they are settled only by
   demo, taste and time. These are **heuristics**. Classifying the decision is itself a craft
   skill. The failure is settling a heuristic with an algorithm's tool (a metric, a test).

5. **Edit for less.** Answer hard questions by removing the need to ask them. Fewer places to look
   is measurably faster, not merely tidier (working memory actively holds only about four chunks —
   Cowan 2001). The strongest move is often subtraction: one input instead of three, a removed
   option, a merged screen.

### Decision table

| Decision in front of you | Class | How to settle it | Consequence of the wrong tool |
|---|---|---|---|
| Page weight, load time, contrast ratio, tap-target size | Algorithm | Measure against the threshold | Arguing taste over a measurable fact wastes time and ships a slower or failing product |
| Signature colour, typeface, easing curve, animation duration, tone of a label | Heuristic | Demo variations, live on them, a named person decides | A metric picks the mean of what was supplied; the product converges on generic |
| Which of two flows lets users finish a task | Mostly algorithm | Usability test with success criteria | Taste alone ships a flow people cannot complete |
| Whether a working flow *feels* right after a week of use | Heuristic | Live on it, then decide | A one-off review misses cumulative friction |

---

## 3. Taste is not outsourceable

The standard illustration is Google testing 41 shades of blue for a link colour — Kocienda's
one-line verdict: "Google factored out taste." An A/B test has a narrow dynamic range: it picks
the best of the options it was handed, and its hidden cost is the better design that conviction
and refinement would have reached.

Keep the nuance, or the lesson is mis-taught. It is **not** "metrics are bad" or "never measure".
It is: **do not let a metric make a taste decision for you, and do not let measurement displace
conviction and refinement.** A heuristic decision outsourced to a number is an abdication of
authorship.

This is the sourcing-authority asymmetry rule (§2) restated on the process side. Outsourcing a
taste decision to a test metric is the same error as outsourcing a font or colour choice to an AI
recommend-list:

- A taste decision must trace to a skilled human's conviction — not to a number, not to a model's
  pick.
- A metric and an AI recommend-list both launder the choice out of human hands: one to the median
  of a test population, the other to the median of training data. Both converge on the mean; the
  Mission exists to push away from the mean.
- Measurement and AI suggestions are admissible as **evidence to inform** the decision; neither is
  ever **authority for** the decision.
- When a metric or model agrees with your taste, record it as convergence, not endorsement.

---

## 4. The chain of authored work

Authored work runs along a chain, not a checklist: **inspiration** seeds the idea; the working
demo forces a concrete **decision**; **craft** builds the smallest real thing that proves it;
**taste** selects among the variations the loop produces; **empathy** keeps selection anchored to
the person who will use it. Collaboration, diligence and decisiveness run alongside every link.
Every link is human judgement applied to a concrete artefact — which a template or a
recommend-list cannot supply, and which is why the result looks human-made. Treat the set as a
distillation (everything counts; no detail is too small), not as a scorecard.

---

## 5. Decision capture

A converged heuristic decision is fragile: without a record it is reopened by the next person who
prefers something else. For each one, record:

| Field | Content |
|---|---|
| Decision | The concrete value chosen (e.g. "toast visible 4 s", "brand green #1F6F4A") |
| Class | Algorithm or heuristic |
| Variations tried | The demos compared, with links |
| Evidence consulted | Metrics, tests, AI suggestions — labelled as evidence only |
| Decider | The named person whose taste settled it |
| Lived-on period | How long the team used it before confirming |
| Reopen trigger | What new evidence would justify reopening |

Procedure and template: `skills/05-ux-process-research-and-psychology/demo-driven-design-process/references/decision-capture.md`.

### Worked example

A Kampala clinic's booking app shows a toast after a patient books a slot. Engineering proposes
an A/B test of five durations on "fewest repeat taps". The designer classifies the question:
whether the toast is read at all is partly measurable, but how long it should stay so that it
feels calm rather than hurried is a heuristic. Three demos (2.5 s, 4 s, 6 s) are installed on
reception staff phones for a week. Staff report 2.5 s is missed when a patient is talking to them
and 6 s covers the next action. The design lead chooses 4 s, records the decision with the
repeat-tap data attached as supporting evidence, and sets the reopen trigger as "complaints of
missed confirmations from patients using screen magnification".

---

## 6. Which skills apply this doctrine

- **`04…/distinctive-by-design`** — insert the demo loop between "state the one decision" and
  "build"; treat composition calls as heuristic decisions; apply "edit for less" and "idea before
  execution".
- **`05…/demo-driven-design-process`** — the process skill that runs this loop end to end (demo
  fidelity, "live on it", the decider model, the algorithm/heuristic lens, decision capture). It
  operationalises this reference and must not duplicate it.
- **Critique and review skills** — `00…/design-critique-and-review-facilitation` and
  `05…/heuristic-evaluation-and-design-critique`: no critique without a concrete artefact (rule
  1); the algorithm-vs-heuristic axis as a critique lens (rule 4); "live on it" as a
  longitudinal-review caveat (rule 2).
- **`product-design-audit`** — use the algorithm/heuristic lens and the "41 blues" test to catch
  taste decisions abdicated to a metric or an AI recommend-list.
- **`02…/brand-visual-identity`, `color-system-and-palette`, `logo-and-wordmark-design`** — the
  "41 blues" reasoning is the named argument for choosing a signature colour or mark by
  conviction, not by test.

---

## 7. Checks

- [ ] Every design discussion had a concrete artefact on the table.
- [ ] Each open decision classified as algorithm or heuristic before a tool was chosen.
- [ ] No heuristic decision was settled by a test result or an AI suggestion alone.
- [ ] The chosen option was lived on before it was confirmed.
- [ ] Subtraction was tried before addition.
- [ ] The converged decision is captured with its decider and reopen trigger.
- [ ] The taste-bias self-check (section 8) was run by each reviewer.

---

## 8. Taste-bias self-check (added 2026-09-24)

Before approving or rejecting visual work, each reviewer answers:
1. Am I responding to this palette, face or layout because it fits the idea, brand, audience and
   channel, or because I personally like it?
2. Do I prefer this style only because it is familiar?
3. Am I open to layouts I have not seen before?
4. Would the audience find it appealing and clear?
5. Does it align with the brand's positioning and story?
6. Have I considered who is represented, and how power is shown?

Neither the designer's nor the client's personal taste sets the standard; the brand's positioning
sets the "taste level". Where a mood board is used to agree that level, follow the mood-board
policy in `skills/11-imagery-illustration-and-art-direction/art-direction-routes/references/direction-board-protocol.md`
(used early and once; never billed as a concept).

---

Sources: Kocienda, K. (2018) *Creative Selection*, St. Martin's Press (demo-selection loop,
algorithm-vs-heuristic distinction; method only — the memoir's anecdotes are not reproduced);
Miller, G. A. (1956) "The magical number seven, plus or minus two", *Psychological Review*;
Landa, R. (2022) *Strategic Creativity*, Routledge (self-check questions, paraphrased), reconciled
with Adams, S. et al. (2012) *Graphic Design Rules*, Frances Lincoln. The worked example is
original.
