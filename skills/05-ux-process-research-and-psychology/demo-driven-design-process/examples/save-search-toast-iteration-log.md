# Worked example — Demo-driven iteration: the "saved-search confirmation"

A real, end-to-end run of the demo → feedback → next-demo loop for **one** small feature, showing the
fidelity ring and non-goals each round, the algorithm-vs-heuristic call, the taste decision and its
one-sentence conviction, convergence (by subtraction), and the captured decision record.

This deliberately picks up where `wireframing-and-prototyping`'s example leaves off. There, the team
validated the **flow** for "save a search and get notified" at lo-fi. The flow is settled. What is
*not* settled is one heuristic: **how the app confirms a save without yanking the user out of the
results they were scanning.** That is the one thing this loop refines.

> Context: a property-listings web app. A user filters listings (e.g. "2-bed, under £1,400, near a
> rail station"), then taps **Save this search**. We must confirm the save and offer to turn on
> notifications — without breaking their scan of the results.

---

## Round 0 — Frame the decision and classify it

**The one thing this loop resolves:** *the confirmation moment after "Save this search" — what the
user sees, where, and for how long.*

**Classify it (`references/decision-capture.md`):**
- "Does the save succeed / how long does the network call take?" → **algorithm** (objective arrow:
  faster, lower error rate). Out of scope for this loop — codified separately, target < 400 ms,
  optimistic UI.
- "Where the confirmation appears, how long it lingers, how it offers notifications, whether it
  interrupts the scan" → **heuristic.** No metric points to the right answer; it must be resolved by
  demo + taste + living on it. **This is the loop.**

**Single decider:** the product designer running the loop (earned the room by doing the work).
**Fidelity rung** (chosen with `wireframing-and-prototyping`): **hi-fi clickable**, because the whole
question is *feel and timing* — lo-fi cannot answer "does the wait feel broken / does it interrupt".

---

## Round 1 — Demo A: the modal dialog

**Fidelity ring:** the confirmation moment only.
**Non-goals (stated up front):** not the modal's copy wording, not the icon, not the empty-state of
the saved-searches list, not the notification backend — *only whether a centred modal is the right
shape for this confirmation.*

**Demo built (inside the ring, real & running):** on tapping **Save this search**, a centred modal
appears: "Search saved. Want alerts when new matches appear?" with **Turn on alerts** / **Not now**.
Everything outside the ring is faked — listings are hard-coded, the save is stubbed to succeed
instantly, the alerts toggle goes nowhere.

**Feedback — lived on it for two days of real searching:**
- The modal **dims the whole results page** and steals focus. Every save is a hard stop: you were
  mid-scan, and the app forces a yes/no before you can look at one more listing.
- Worse, it conflates two things — "your save worked" (certain, done) and "do you want alerts?"
  (a decision) — and blocks on the *decision* even when the user only wanted the *save*.

**Taste decision (Demo A → rejected):** *A confirmation that blocks the user's scan to ask a
secondary question is the wrong shape — the save is done; nothing should be modal about it.*
This points the next divergence: **non-blocking**, and **separate the certain fact from the optional
decision.**

---

## Round 2 — Demo B: the inline toast with both actions

**Fidelity ring:** still the confirmation moment; now testing a non-blocking surface.
**Non-goals:** not the exact colour, not the slide-in easing curve yet — *only whether a corner toast
that does not block the scan is the right shape, and whether the alerts offer can ride along in it.*

**Demo built:** a toast slides up bottom-left: "Search saved" with a small **Turn on alerts** link
and a close ✕. It does **not** dim the page; the user keeps scrolling listings underneath. It auto-
dismisses after **8 seconds**.

**Feedback — lived on it for three days:**
- Non-blocking is clearly right — you save, you keep scanning, the world doesn't stop. Big improvement
  over Demo A. Keep the toast shape.
- But **8 seconds is too long** — the toast sits there covering a listing card well after you've moved
  on; it feels like litter. (This is a *duration* — a textbook heuristic, **not** something to A/B.)
- The **Turn on alerts** link inside the toast is easy to miss while scrolling, and just as easy to
  fat-finger by accident. The toast is doing two jobs at once again — confirm + offer — and doing the
  second one poorly.

**Taste decision (Demo B → keep the toast, fix two things):**
1. *Shorten the linger* — find a duration that confirms without overstaying.
2. *Stop making the toast also carry the alerts decision* — it muddies a clean confirmation.
Conviction in one line: **the toast should do one job — say "saved" — cleanly and briefly.**

This is where **"edit for less"** (`references/demo-loop-and-fidelity.md` §5) enters: the strongest
next variation may be to *remove* the alerts action from the toast entirely.

---

## Round 3 — Demo C: tuning the duration (a pure heuristic sub-loop)

**Fidelity ring:** the toast's **linger duration** only.
**Non-goals:** not the toast's content, not its position — *only how long it stays.*

Someone proposes: *"let's A/B 2 s vs 4 s vs 6 s and ship whichever gets the most alert opt-ins."*
**Rejected on the spot** — that is the **41-shades-of-blue error** (`references/decision-capture.md`
§2): it would let a metric make a taste decision, and "alert opt-ins" isn't even what duration is
*for*. Duration is a heuristic: resolve by demo + taste + time.

**Demo built:** the same toast at **2.5 s**, **4 s**, and **6 s**, switchable, lived on for two days
each across real searches.
- 2.5 s — gone before your eye reaches it after a fast save; you doubt it saved.
- 6 s — overstays; back to feeling like litter.
- 4 s — long enough to register "saved", gone before it annoys.

**Taste decision:** **4 seconds.** Conviction: *long enough to be read, short enough to never become
litter.* Logged as a heuristic, decided by living on it — no metric consulted, none needed.

---

## Round 4 — Demo D: subtract the alerts action from the toast

**Fidelity ring:** how the alerts offer is made, now that it has left the toast.
**Non-goals:** not the alerts-settings screen design — *only where the "turn on alerts" offer now
lives so it stops competing with the confirmation.*

**Demo built (the subtraction):** the toast now says only **"Search saved"** (4 s, non-blocking,
bottom-left) — no action, nothing to mis-tap. The alerts offer moves to a **persistent, dismissible
inline banner at the top of the now-saved search's own page** ("Get alerted when new matches appear →
Turn on"), where the user lands when they later open the saved search deliberately, with attention to
spare.

**Feedback — lived on it for four days:**
- The save now feels **effortless and certain** — confirm and keep scanning, zero decisions forced.
- The alerts opt-in, offered *when the user is actually thinking about that saved search* rather than
  mid-scan, is both calmer and (anecdotally, in dogfooding) more likely to be taken — but that signal
  is logged as **convergence, not authority**: the move was chosen because separating the two jobs is
  *right*, not because a number told us to.
- Nothing further improves on living on it. **Converged.**

**Convergence call:** new variations now trade sideways, not up. Stop. Pick one and move on.

---

## The captured decision record

```
DECISION RECORD — Saved-search confirmation moment
  Round/date:        Round 4 (converged after 4 demos / ~11 days lived-on)
  Class:             heuristic  — feel/timing/placement; no objective arrow; settled by demo+taste+time
                     (the save's success/latency is a separate ALGORITHM decision, codified < 400 ms)
  Decider:           product designer (single decider for the loop)
  Chosen:            Non-blocking corner toast, content = "Search saved" only, 4 s linger, bottom-left.
                     Alerts opt-in moved OUT of the toast to a dismissible banner on the saved-search page.
  Beat:              (A) centred blocking modal; (B) toast carrying both confirm + alerts link;
                     (C) 2.5 s and 6 s linger durations; (pre-D) alerts action living inside the toast.
  Conviction (why):  The confirmation should do ONE job — say "saved" cleanly and briefly, without
                     stopping the scan or forcing a secondary decision. The alerts question belongs
                     where the user is actually thinking about that search, not mid-scan.
  Lived-on:          ~11 days total across rounds, real searches, by the designer (+2 teammates in R4).
  Evidence logged:   Dogfooding hinted higher opt-in when alerts moved off the toast — recorded as
                     CONVERGENCE, NOT authority. No A/B test run; an A/B on duration was proposed and
                     rejected as the 41-shades-of-blue error.
  Non-goals:         toast colour/easing, alerts-settings screen design, notification backend, copy
                     micro-wording — deferred to their own decisions.
  Re-open if:        we add a second save-like action that needs the same surface, or notification
                     volume changes the alerts-offer context.
```

---

## What this example demonstrates (mapped to the skill)
- **The loop, not a big-bang build:** four deliberate variations, each diverging from the last round's
  feedback — modal → toast-with-action → duration-tuned → subtracted. (Workflow steps 1–6.)
- **Fidelity ring + explicit non-goals every round** kept feedback on the one idea, not the
  scaffolding. (`references/demo-loop-and-fidelity.md` §3.)
- **Algorithm vs heuristic classified up front**, and the duration sub-decision defended *as* a
  heuristic when an A/B was proposed — the 41-shades-of-blue guard.
  (`references/decision-capture.md` §1–2.)
- **"Live on it"** did the judging — the day-three "litter" feeling, not a one-shot review, drove
  Rounds 2–3. (Longitudinal refinement.)
- **"Edit for less"** produced the winning move: *removing* the alerts action from the toast, not
  adding more to it. (`references/demo-loop-and-fidelity.md` §5.)
- **Taste selected by conviction**, with the metric-ish signal logged as convergence, not authority.
  (`doctrine/design-doctrine.md` §2.)
- **The decision was captured** so it cannot be silently re-litigated.

**References:** `doctrine/references/creative-selection-and-taste.md`; `doctrine/design-doctrine.md`
§0 & §2; this skill's `references/demo-loop-and-fidelity.md` and `references/decision-capture.md`.
Pairs with `wireframing-and-prototyping` (which validated the underlying flow at lo-fi before this
loop refined the confirmation moment).
