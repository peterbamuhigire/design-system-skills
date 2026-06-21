# Reference: Case-Study Structure — the evidence-anchored spine

*Sources: Sandler (2023) — Contrast, Data Storytelling, Show-Don't-Tell, Calls to Action; Andrew
Hinton, "The story is the thing," in *UX Storytellers: Connecting the Dots* (2010) — the
user-as-protagonist thesis; Gerry McGovern's top-tasks / "long neck" (via Rønjum, same anthology).*

> **The fence (governs this whole reference).** A case study is the *telling of real, authored,
> shipped work*. Every beat below must be **anchored to concrete evidence** — a working demo, a
> measured outcome, an actual decision you made. A beat you cannot evidence is fiction; cut it.
> No real artifact and no real outcome → **no case study** (only an imaginary puppy,
> `doctrine/references/creative-selection-and-taste.md` rule 1). Story never replaces the demo.

---

## The user is the protagonist; the product is a bit-player

The foundational framing (Hinton's "the story is the thing"): **stories are the foundation; data is
the abstraction we lay over them.** A product is **a bit-player in the user's own drama** — *they*
are the protagonist, and what you made must fit the contours of *their* story, not star in its own.

Practical consequences for a case study:
- **Cast the user, not the product, as the hero.** The arc is "what the user was trying to do and
  how their situation changed," not "what features we shipped." The product enters as the thing that
  fit their story.
- **Listen to the whole story before you frame it.** The unit of insight is the *person's narrative*
  with its context — not a decontextualised metric. A survey gives pie-charts; a story carries the
  context that makes the numbers mean anything (Data Storytelling: *a pie chart is not a story —
  turn numbers into people with stakes*).
- **Empathy is an input, not a garnish.** The "before" must be told from the user's point of view,
  with their real stakes, or the transformation will not land.

---

## The six-beat case-study spine

The reusable backbone for a written case study, a portfolio piece, or the narrative under a deck.
Each beat names **what it must contain** and **the evidence that anchors it**. (Map this onto a
chosen structure from `narrative-frameworks.md` — Three-Act, Pixar, etc. — which decides the
dramatic *shape*; this gives the *content* of the beats.)

| # | Beat | What it contains | Evidence that anchors it (mandatory) |
|---|---|---|---|
| 1 | **Problem (the before)** | The user's real, often wicked problem, in *their* terms. Open hard on it (Contrast). | The actual situation: research notes, a real user quote, the broken old flow, a baseline screenshot. |
| 2 | **Stakes** | Why it mattered — the cost of the status quo to the user and the business. | A baseline metric (drop-off %, time-on-task, support tickets, revenue lost), a quote, a named risk. |
| 3 | **Authored decision (the turning point)** | The *one* specific, defensible choice a skilled human made — the heuristic resolved by taste, not by a metric. The climax. | The decision artifact: the design itself, the rejected alternatives, *why* this one (the reasoning), the working demo that proved it. |
| 4 | **Before/after (the transformation)** | The delta the decision produced, shown side by side so it is *felt*. | Paired before/after screens or flows; the live demo; the comparison. |
| 5 | **Proof** | Evidence the outcome is real and attributable, not coincidence. | Post-change metrics vs. the §2 baseline; user quotes; usage data; the shipped, usable thing. |
| 6 | **CTA** | The single action this telling should produce for *this* audience. | The explicit ask, matched to the audience type (decide / fund / advocate / build on it). |

**The turning point is beat 3.** A design case study's climax is *the authored decision and why*,
not a feature tour. This is where the Mission is visible — show the choice a templating tool would
never have made, and the conviction behind it. If beat 3 is missing, you have a feature list, not a
case study.

---

## Anchoring rule — Show, Don't Tell

Every adjective must convert to evidence or be cut:

| Don't tell | Show (the evidence) |
|---|---|
| "We made onboarding intuitive." | "Time-to-first-action fell from 4m10s to 38s (n=1,240)." + the before/after screens. |
| "Users loved it." | A verbatim user quote + the retention curve after the change. |
| "A bold, distinctive design." | The actual design beside the convergent alternative we rejected, and why. |
| "It drove growth." | The attributed metric against the stated baseline, with the time window. |

If a claim has no evidence behind it, it is a darling — **kill it.** A shorter, fully-evidenced case
study beats a longer one padded with unbacked superlatives (and the padding is exactly the slop the
Mission rejects).

---

## Cut to top tasks (the long neck)

A handful of "top tasks" account for the overwhelming majority of what the audience came for; the
rest is a "long neck" of low-value detail. Content is expensive — *like fresh food, it goes off* —
and a case study that tries to record everything drowns the one thing that matters in "a cacophony
of countless voices."

So: **strip to the single through-line.** Decide the one thing this audience must take away, keep
only the beats and evidence that serve it, and cut the rest (Kill Your Darlings, Rule of Three).
A complete archive is not a case study; a *chosen* story is.

---

## Designing the close (Peak-End)

The audience remembers the **peak** and the **end**. So:
- Put the **strongest single evidence** (beat 5 proof, or the beat 4 before/after) at the peak.
- **End on the transformed state + the one CTA (beat 6)** — never trail off on a feature list,
  a methodology recap, or a thank-you slide. The last thing said is the thing remembered.

---

## The fence, applied to the spine

Walk the six beats and ask of each: *can I point to the real thing?* If beats 1–2 (problem/stakes)
are invented, you are manufacturing a struggle that did not happen. If beats 4–5 (before/after,
proof) cannot be evidenced, you are claiming an outcome you did not produce. Either failure means
**the story has exceeded the work** — stop and either find the real evidence or do not tell it. The
case study exists to make *true, authored* work legible and memorable; it is never a way to make
unbuilt or convergent work *sound* authored (`doctrine/design-doctrine.md` §0, §2;
`doctrine/references/creative-selection-and-taste.md`).
