# Reference: Creative Selection & Taste (the production method behind the Mission)

The doctrine Mission says *the moat is looking human-made* — make an authored, non-convergent
choice. That states the **what**. This reference states the **how**: the actual production
method by which skilled human work gets made, so our skills produce *authored* work rather than
generated mean. It is the process-side companion to the Mission (§0) and the sourcing-authority
asymmetry rule (§2) of `design-doctrine.md`.

**Source:** Ken Kocienda, *Creative Selection: Inside Apple's Design Process During the Golden
Age of Steve Jobs* (2018) — first-hand method from the engineer who built the iPhone keyboard
and co-built Safari. We extract the *method*; we discard the Steve-Jobs theatre (moods, the
all-powerful mercurial decider) as memoir, not practice.

---

## The core method — creative selection

Authored work is not produced by a big-bang build, nor by writing a spec and executing it. It is
produced by a **demo → feedback → next-demo loop**: a continuing progression of concrete working
demos, each a deliberate variation on the last, with feedback as the selection pressure that
decides which variation survives. Converge on a demo, let the feedback cause a fresh divergence,
converge again. Taste — a skilled human's judgement — does the selecting. Iteration does the
converging.

This is a Darwinian variation/selection engine, not brainstorming and not A/B testing. It is the
machine that reliably produces the authored choices the Mission demands.

---

## The five working rules

1. **The working demo is the unit of progress.** Progress is measured in *real, running
   artifacts*, not abstractions. Never hold a design discussion without a concrete thing to react
   to — the anti-pattern is "arguing about whose imaginary puppy is cuter," debating paper
   mock-ups and specs with nothing real in the room. A mockup-of-a-mockup is not a demo. (This is
   the same logic by which `distinctive-by-design` bans lorem-ipsum: *placeholder text produces
   placeholder design.*) Build the smallest real artifact that proves the one idea, then react to
   *it*.

2. **Live on it (dogfood your own work).** You cannot judge a refinement from a single review.
   The team *used the build daily* — "I lived on the software" — to feel whether the choices added
   up over time. Refinement is **longitudinal**, not a one-shot critique. If you have not lived on
   the thing, you have not yet earned an opinion about whether it works.

3. **Concrete over abstract.** Decide on specific, real instances — *this* colour, *this* duration,
   *this* word — not vague directions ("make it feel more premium," "punch it up"). A direction is
   not a decision. The demo forces the abstraction down to something you can actually choose
   between.

4. **Know whether you face an algorithm or a heuristic.** Some decisions can be *codified* into a
   rule with an objective arrow of improvement that always points one way — faster page load is
   simply better; this is an **algorithm**. Other decisions — an animation's duration, a signature
   colour, a swipe threshold — have a real value but *no objective arrow*; they can be resolved
   **only** by demo + taste + time. These are **heuristics**. Knowing which kind of decision you
   are facing is itself a craft skill: the failure is using an algorithm (a metric, a test) to
   settle a question that is actually a heuristic.

5. **Edit for less.** Answer hard questions by removing the need to ask them (Miller's 7±2:
   fewer places to look is *measurably* faster, not merely tidier). The strongest move is often
   subtraction — one keyboard instead of several, the removed suggestion bar — not addition.

---

## The "41 shades of blue" lesson — taste is not outsourceable

The canonical illustration. Google famously A/B-tested 41 shades of blue for a link colour and
shipped the winner. Kocienda's critique: A/B testing has a tiny dynamic range — it picks the best
of the options it was *handed* — and its true cost is the far-better design that conviction and
refinement would have reached. *"Google factored out taste. At Apple we never would have dreamed
of it… we picked one and moved on."*

The defensible reading — keep this nuance or we mis-teach it — is **not** "metrics are bad" or
"never measure." It is: **do not let a metric make a taste decision for you, and do not let
measurement displace conviction and refinement.** A taste decision (a heuristic) outsourced to a
number is an abdication of authorship.

**This is the sourcing-authority asymmetry rule (§2), restated on the process side.** Outsourcing
a taste decision to an A/B metric is the *same error* as outsourcing a font or colour choice to an
AI recommend-list:

- A taste decision must trace to a **skilled human's conviction**, not to a number and not to a
  model's pick.
- A metric and an AI recommend-list are both ways of laundering the choice out of human hands —
  one to the median of a test population, the other to the median of training data. Both converge
  on the mean; the Mission exists to push *away* from the mean.
- Measurement and AI suggestions are admissible as **evidence to inform** the decision; neither is
  ever **authority for the decision**.

When a metric or a model agrees with your taste, note it as convergence — not as endorsement.

---

## The chain: inspiration → decision → craft → taste → empathy

Authored work runs along a chain, not a checklist. **Inspiration** seeds the idea; the working
**demo** forces a concrete **decision**; **craft** builds the smallest real thing that proves it;
**taste** selects among the variations the loop produces; **empathy** keeps the selection anchored
to the person who will use it. Every link is human judgement applied to a concrete artifact — which
is exactly what a templating tool or a recommend-list cannot do, and exactly what makes the result
look human-made.

(Kocienda frames the full set as inspiration, collaboration, craft, diligence, decisiveness,
taste, empathy — explicitly *not* a scorecard but a distillation: everything counts, no detail is
too small.)

---

## Which skills apply this doctrine

This reference states the principle; the following skills operationalise it and should cite it:

- **`04…/distinctive-by-design`** — insert the demo/iteration loop *between* "state the ONE
  decision" and "build"; treat composition/heuristic calls as demo-and-taste decisions, not metric
  decisions; apply "edit for less" and "idea before execution."
- **`05…/demo-driven-design-process`** *(planned)* — the dedicated process skill that
  operationalises this loop end-to-end (the demo-fidelity ring, "live on it," the decider model,
  the algorithm/heuristic lens). Must *operationalise* this ref, not duplicate it.
- **The critique / process skills** — `00…/design-critique-and-review-facilitation` and
  `05…/heuristic-evaluation-and-design-critique`: enforce "no critique without a concrete artifact
  to react to," carry the algorithm-vs-heuristic axis as a critique lens, and treat "live on it"
  as a longitudinal-review caveat.
- **`product-design-audit`** — use the algorithm/heuristic lens and the "41 blues" test to catch
  taste decisions that have been abdicated to a metric or an AI recommend-list.
- **`02…/brand-visual-identity` + `color-system-and-palette`** — the "41 blues" reasoning is the
  named argument for choosing a signature colour by **conviction, not by test**.
