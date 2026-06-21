# Reference: Algorithm vs Heuristic, and Capturing the Decision

This reference operationalises two parts of `doctrine/references/creative-selection-and-taste.md`:
the **algorithm-vs-heuristic** decision lens (working rule 4 + the "41 shades of blue" lesson) and
the discipline of **capturing the converged decision** so it survives. Read the doctrine reference
first; this is the procedure, not a restatement.

---

## 1. The first move: classify the decision

Before you run any loop, ask: **is this an algorithm decision or a heuristic decision?** They are
settled by *different procedures*, and using the wrong one is the root error of the whole craft.

### Algorithm — there is an objective arrow of improvement
The decision can be **codified into a rule** whose arrow always points one way. More of the good
thing is simply better, with no taste involved:

- page-load time (faster is better), tap count to complete a task (fewer is better), contrast ratio
  against WCAG (higher passes), error rate (lower is better), payload size, time-to-first-byte.

**Procedure:** measure, codify the rule, move on. A metric is the *right* authority here. You do not
need to "live on it" — read the arrow and act.

### Heuristic — a real value but no objective arrow
The decision has a genuinely better and worse answer, but **no metric points to it**. It can be
resolved *only* by demo + taste + time:

- an animation's duration, a signature colour, a swipe/scroll threshold, a tone of voice, the rhythm
  of a layout, where a confirmation appears, how long a toast lingers.

**Procedure:** run the demo loop (`references/demo-loop-and-fidelity.md`), live on it, and let the
**single decider select by conviction.** Time and taste are the authority here — a metric is not.

### The test
> Ask: *"If I had a number for this, would the number settle it?"*
> - **Yes, unambiguously** → algorithm. Codify it.
> - **No — even with the number I'd still need a skilled human to choose** → heuristic. Demo + taste.

The classic failure is **using an algorithm where a heuristic is required**: tuning an animation
duration by conversion rate, or A/B-ing a colour. The inverse failure is rarer but real: "debating
by taste" something with a hard objective arrow (load time) that should just be codified.

Many real decisions are **interleaved** — the photo-swipe is heuristic (does it feel right?) →
algorithm (frame budget) → algorithm (memory) → heuristic (the bounce at the end). Classify each
sub-decision separately; *"design is how it works"*, so you cannot bolt feel on after the engineering.

---

## 2. The "41 shades of blue" rule: metric/AI is evidence, never authority

Google A/B-tested 41 shades of blue for a link colour and shipped the winner. Kocienda's critique:
A/B testing has a **tiny dynamic range** — it picks the best of the options it was *handed* — and its
true cost is the far-better design that conviction and refinement would have reached.

> *"Google factored out taste. At Apple we never would have dreamed of it… we picked one and moved
> on."*

The defensible reading (keep this nuance or you mis-teach it) is **not** "metrics are bad" or "never
measure". It is:

- **A taste decision (a heuristic) must trace to a skilled human's conviction** — not to a number,
  and not to an AI recommend-list. Outsourcing it to either is an abdication of authorship.
- **A metric and an AI pick are both ways of laundering the choice to the mean** — one to the median
  of a test population, the other to the median of training data. The Mission exists to push *away*
  from the mean (`doctrine/design-doctrine.md` §0, §2 — the sourcing-authority asymmetry rule).
- **Measurement and AI suggestions are admissible as evidence to inform** a heuristic decision; **
  neither is ever authority for it.** When a metric or a model *agrees* with your taste, log it as
  **convergence — not endorsement.**

This is the §2 asymmetry rule restated on the process side: outsourcing a taste decision to an A/B
metric is the *same error* as outsourcing a font or colour to an AI recommend-list.

---

## 3. Convergence by taste — when to stop

The loop is done when **further variation stops improving the one thing** — and *taste*, not a target
number, tells you that. Signals you've converged:

- New variations make it different, not better; you find yourself trading one small loss for one small
  gain. (For an algorithm, convergence is objective: the arrow flattens.)
- Living on it stops surfacing annoyances.
- The single decider has conviction — can say in one sentence *why this one* and *what it beats*.

Then **"pick one and move on."** Holding the loop open past convergence is the polishing failure mode;
closing it before convergence is the first-that-works failure mode.

---

## 4. Capture the decision (the decision record)

Converging without recording *why* means the same argument gets re-litigated weeks later with no
memory of what was already tried and beaten. Capture every converged heuristic decision:

```
DECISION RECORD — <the one thing decided>
  Round/date:        <when it converged>
  Class:             algorithm | heuristic   (and why)
  Decider:           <the single person who selected>
  Chosen:            <the specific instance — this value / word / colour / threshold>
  Beat:              <the variations it was selected over>
  Conviction (why):  <one sentence — the human reason it won>
  Lived-on:          <how long / by whom>  (heuristics only)
  Evidence logged:   <any metric or AI signal — recorded as CONVERGENCE, not authority>
  Non-goals:         <what this decision deliberately did not address>
  Re-open if:        <the condition that would justify re-running the loop>
```

Rules for the record:
- The **Conviction** line is the load-bearing field — it is the authored human reason, the thing a
  templating tool or a recommend-list could never supply.
- Any metric or AI signal goes under **Evidence logged** and is explicitly marked *convergence, not
  endorsement* — never promote it to the reason.
- Keep the **Beat** field — knowing what was tried and rejected is what stops the re-litigation.
- A captured decision feeds the next loop, the critique skills, and group-09 handoff.

---

## The chain this protects
Authored work runs **inspiration → decision → craft → taste → empathy** — every link is human
judgement on a concrete artifact. Classifying the decision (algorithm vs heuristic) protects the
*decision* link; refusing to outsource to a metric/AI protects the *taste* link; capturing the record
keeps the chain auditable. See `doctrine/references/creative-selection-and-taste.md`.

**Source:** Ken Kocienda, *Creative Selection* (2018), via the doctrine reference.
