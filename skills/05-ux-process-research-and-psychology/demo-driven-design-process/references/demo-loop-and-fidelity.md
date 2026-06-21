# Reference: The Demo Loop & Demo Fidelity

This reference operationalises the **demo → feedback → next-demo loop** from
`doctrine/references/creative-selection-and-taste.md` (Kocienda's *Creative Selection*). The
doctrine reference states the principle; this states the *procedure*. Read the doctrine reference
first; do not duplicate it here — this is the how-to-run-it companion.

---

## 1. The loop, run end to end

Authored work is produced by a **continuing progression of concrete working demos**, each a
deliberate variation on the last, with feedback as the selection pressure that decides which
variation survives. The cadence is:

```
   converge ──▶ a working demo
       ▲              │
       │              ▼
   re-decide ◀── feedback (live-on-it / test)
       ▲              │
       │              ▼
   next demo ◀── deliberate divergence
```

> *"We habitually converged on demos, then allowed demo feedback to cause a fresh divergence."*

This is a **Darwinian variation/selection engine** — not brainstorming (no concrete artifact to
react to), not A/B testing (which only ranks options it was handed), not spec-then-execute (no
progression of variations). Variation supplies candidates; taste does the selecting; iteration does
the converging.

**One round =**
1. State the one decision this round resolves (concrete instance, not a direction).
2. Build the smallest real demo that proves it (inside the fidelity ring — §3).
3. Live on it / get feedback (§4).
4. The single decider selects the surviving variation by conviction.
5. Let the feedback cause the *next* deliberate variation.

Run rounds until variation stops improving the one thing — then **stop and move on**. Both failure
modes are real: stopping at the first demo that works (no refinement), and never stopping (polishing
past convergence). Decisiveness is part of the craft.

---

## 2. What makes something a *demo* (and what doesn't)

A demo is **real, running, concrete, and focused**:

- **Real** — an actual artifact, not a description of one. A mockup-of-a-mockup is not a demo; a
  slide *about* the interaction is not a demo. (This is the same logic by which the doctrine bans
  lorem-ipsum: *placeholder produces placeholder*.)
- **Running** — you can do the thing, not just look at a picture of the thing. For a heuristic
  (§ decision-capture), "running" is what lets you *feel* the choice over time.
- **Concrete** — it forces the abstraction down to a specific instance you can choose between:
  *this* 220 ms, *this* word, *this* threshold — not "snappier" or "more premium". A direction is
  not a decision.
- **Focused** — it proves *one* thing. Everything else is faked or omitted (§3).

**The anti-pattern it replaces: arguing about whose imaginary puppy is cuter** — a design discussion
with nothing real in the room, debating paper mock-ups and specs. Never hold the discussion without
a concrete thing to react to. If there is no demo, the first move is to build the smallest one, not
to argue harder.

---

## 3. The fidelity ring & non-goals (the Hollywood-backlot method)

You cannot build everything to the same fidelity, and you shouldn't try. The method (from Richard
Williamson's Konqueror demo):

1. **Draw the ring.** Draw a conceptual ring around the *one thing the demo must prove*.
2. **Build inside the ring at full fidelity.** This is the lamppost the actor leans on — it has to
   bear real weight. If the demo's job is to prove a swipe feels right, the swipe must be real.
3. **Fake or omit everything outside the ring.** This is the empty hat-shop facade on the backlot —
   it only has to look right from the camera's angle. Hard-code the data, stub the backend, screenshot
   the surrounding screens. Faking outside the ring is not cheating; it is what lets you build the
   inside at full fidelity *today*.
4. **Take extra care at the boundary** — where the real thing meets the fake, because that seam is
   where a demo most often breaks the illusion and derails the feedback.
5. **Write explicit goals AND non-goals before building.** The non-goals are load-bearing: they tell
   everyone in the room what *not* to react to ("this demo is not about the copy, the colour, or the
   empty state — only the timing"). Without stated non-goals, feedback scatters onto the scaffolding
   and the one idea never gets judged.

**The cardinal sin: faking the very thing the demo is supposed to prove.** If the ring is "does this
animation duration feel right", the duration must be real even if everything around it is cardboard.

> Pick the cheapest honest **fidelity rung** (paper → lo-fi → mid-fi → hi-fi → clickable/coded) with
> `wireframing-and-prototyping`. That skill chooses the fidelity of *one* artifact; this loop decides
> what each artifact in the progression must prove and runs the rounds. They are designed to pair.

---

## 4. "Live on it" — dogfooding as longitudinal refinement

You **cannot judge a heuristic from a single review.** A duration, a threshold, a tone, a layout
rhythm — these only reveal whether they "add up" through repeated, real use. So the team *used the
build daily*:

> *"I lived on the software."*

Rules of dogfooding:

- **Refinement is longitudinal, not a one-shot critique.** One look tells you if it's broken; it does
  not tell you if it's *right*. The annoyance that surfaces on day three is the signal you were after.
- **If you have not lived on the thing, you have not earned an opinion** about whether it works (for a
  heuristic). First impressions are admissible for obvious breakage, not for refinement calls.
- **Use the real demo for real tasks**, in real conditions — not a contrived run-through. The point is
  to feel the choice the way the user will.
- For an external feedback pass (you can't dogfood everything), route a real protocol through
  `ux-research-and-usability-testing` and fold findings back as the **next variation** — at the same
  cheap fidelity, before climbing.

Algorithm decisions (§ decision-capture) do not need living-on — their arrow is objective and can be
read off immediately. Living-on is the procedure specifically for heuristics.

---

## 5. "Edit for less" — subtraction as a first-class variation

The strongest next demo is often the one with something **removed**, not added:

- One keyboard instead of several; the *removed* suggestion bar; one path instead of three.
- Grounded in Miller's 7±2 — fewer places to look is **measurably faster**, not merely tidier.
- The discipline: **answer hard questions by removing the need to ask them.** When a round is stuck,
  try a variation that deletes the contested element entirely and live on *that*.

Subtraction is a deliberate divergence like any other — put it in the loop, don't treat addition as
the only direction variation can go.

---

## Source & relationship to doctrine
- **Operationalises:** `doctrine/references/creative-selection-and-taste.md` (the five working rules,
  the loop, the fidelity discipline, "live on it", "edit for less").
- **Grounded in:** `doctrine/design-doctrine.md` §0 (push away from the convergent mean) and §2 (the
  sourcing-authority asymmetry rule).
- **Source:** Ken Kocienda, *Creative Selection* (2018) — method extracted, Steve-Jobs theatre
  discarded as memoir per the doctrine reference.
