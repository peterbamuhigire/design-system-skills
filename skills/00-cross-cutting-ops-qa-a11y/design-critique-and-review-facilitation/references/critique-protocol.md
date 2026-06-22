# Reference: Critique Protocol — the session structure + feedback frameworks

This is the operating manual for running a design critique / design review. It carries the session
agenda and timings, the three feedback frameworks and when to use each, the taste-vs-requirement
split rule, the single-decider + decision-capture model, the psychological-safety practices, and the
live-vs-async decision. It operationalises `doctrine/references/creative-selection-and-taste.md` for
the *human session*; it does not duplicate the EVALUATE skills' findings rubrics.

> **Standing rule (from the doctrine spine):** **No critique without a concrete artifact to react
> to.** A demo, screens, a prototype, a redline — something real. Critiquing a verbal description or
> a mock-of-a-mock is "arguing about whose imaginary puppy is cuter"
> (`doctrine/references/creative-selection-and-taste.md` rule 1). If there is no artifact, the
> facilitator's job is to send it back to be built, not to run the meeting.

---

## 1. Roles

| Role | Holds | Does NOT |
|---|---|---|
| **Author / maker** | Presents the artifact, states the ask, asks clarifying questions, captures, decides on author's-call items | Defend reflexively, "win" the room, or take feedback as personal |
| **Facilitator** | Owns the frame, time, framework discipline, safety, and the decision log | Inject their own design opinions as the decider (unless they *are* the decider — keep the hats separate) |
| **Reviewers (3–6)** | Give feedback in the announced framework, tagged taste vs requirement | Vote on taste, pile on, or critique the person |
| **Decider (one)** | Makes the taste calls after input; owns decisiveness | Outsource a taste decision to a vote, a metric, or seniority |

Keep the roster small. More reviewers ≠ better feedback; it means more taste noise and a longer
meeting. The decider is **one named person** for this piece of work — every review has *a* decider
(Kocienda). "A decider" is not "an all-powerful mercurial boss"; it is *one accountable judgement*,
and access to the room is earned by making the work better, not by org-chart rank.

---

## 2. The session agenda (live)

A focused crit runs **30–60 min** on one piece of work. Timings are for a 45-min slot; scale to fit.

| # | Move | Time | What happens |
|---|---|---|---|
| 0 | **Frame** | 3 min | Facilitator states the session goal. Author states the **ask**: stage, the **1–2 questions** to answer, the audience/context, and **what is locked / out of scope**. Written at the top of the capture doc. |
| 1 | **Present** | 5 min | Author walks the **concrete demo** briefly — what it is, the path through it — then *stops and listens*. No long rationale-as-defence. |
| 2 | **Clarify** | 5 min | Reviewers ask *only* clarifying questions (no judgement yet). This is rung 1 of the ladder; it prevents critiquing a misunderstanding. |
| 3 | **Feedback** | 20 min | Reviewers give feedback in the **announced framework** (§3), each item **tagged taste or requirement** (§4). Facilitator keeps the shape and the safety. |
| 4 | **Decide** | 8 min | The **decider** resolves the open questions; author takes author's-call items. Each becomes a **decision-log entry** (§6). |
| 5 | **Close** | 4 min | Read back the decisions. Name the **next demo** to build (not the next debate) and any **"live-on-it"** items to dogfood before re-deciding. |

**Rule:** feedback (move 3) never starts before the frame (move 0) and clarify (move 2). Skipping
the frame is the number-one cause of unproductive crits.

---

## 3. The feedback frameworks (announce one, use it)

Announce *which* framework the session is using so everyone gives feedback in the same shape. Choice
depends on the **stage** of the work.

### 3a. I-like / I-wish / what-if  — *early / exploratory work*
Each reviewer offers, in this order:
- **I like…** — what is working and should be protected (name strengths first; a crit that only
  attacks loses the room and tells no one what *not* to break).
- **I wish…** — a concern, phrased as a wish rather than a verdict ("I wish the primary action were
  easier to find").
- **What if…** — a generative provocation, *not* a mandate ("what if the summary came before the
  form?").

Use when the work is divergent and you want to keep it generative and safe. It is deliberately
non-prescriptive — it surfaces directions without handing the author solutions.

### 3b. Problem, not solution  — *most reviews; protects authorship*
Reviewers name the **problem they observed**, and **leave the fix to the author**:
- ✅ "On the error screen I couldn't tell which field failed." (problem)
- ❌ "Make the failed field's border red." (solution — pre-empts the author's craft)

Naming problems rather than dictating solutions keeps **authorship with the maker** (the person with
the most context), surfaces the *real* issue (the dictated fix often solves the wrong thing), and
avoids the room redesigning by committee. When a reviewer *does* have a solution, they offer it
explicitly as *one option*, after the problem — never as the verdict.

### 3c. Ladder of feedback  — *when concerns risk landing before understanding*
Climb the rungs in order; do not skip up:
1. **Clarify** — ask questions until you understand what you're looking at.
2. **Value** — say what is valuable / working (and *why*).
3. **Concerns** — raise concerns, ideally as questions ("how does this handle a returning user?").
4. **Suggestions** — only now, offer suggestions.

The ladder's discipline is that **concerns and suggestions come *after* understanding and value** —
so critique lands on the actual work, the author has heard their strengths first, and the session
doesn't open with an attack. Use it with junior makers, cross-discipline reviewers, or any high-stakes
review where safety is fragile.

> Whichever framework: **always name strengths, not only faults.** A critique that only lists
> problems reads as adversarial, loses the room, and fails to tell the team what to preserve.

---

## 4. Separate taste from requirement (the core discipline)

Every piece of feedback is one of two kinds. **Tag it out loud.** This is the
algorithm-vs-heuristic lens from `doctrine/references/creative-selection-and-taste.md`, applied to
feedback.

| | **Requirement** (algorithm) | **Taste** (heuristic) |
|---|---|---|
| **Definition** | Violates an objective standard; the arrow of improvement points one way | A real value, but **no objective arrow** — resolvable only by demo + taste + time |
| **Examples** | Contrast < 4.5:1; a broken red-route; a banned default font; over the perf budget; a stated brand rule | A signature colour; an animation duration; a word choice; a layout *feel* |
| **How it's settled** | **Non-negotiable** — straight to the decision log as a must-fix | **The decider's conviction** — input from the room, decided by one human, *never* by vote/volume/seniority |
| **Cite** | The objective standard (WCAG ratio, the budget number, the brand rule) | The decider's reasoning — and, if a metric/AI agrees, note it as *convergence, not endorsement* |

**Why this matters.** The failure mode is taste **smuggled in as requirement** ("that's just wrong"
about a colour) — and its mirror, a requirement **voted away** as if it were taste ("most of us like
it, ship it" over a failed contrast check). Tagging each item prevents both. And **never outsource a
taste decision to a tally or an A/B metric** — that is the "41 shades of blue" error on the process
side: a taste decision must trace to a skilled human's conviction, not to the median of a vote or a
test population (`doctrine/references/creative-selection-and-taste.md`; `doctrine/design-doctrine.md`
§2, the human-design-authority asymmetry rule).

---

## 5. Psychological safety (honesty and safety are not in tension)

A safe crit is *more* honest, not less — people only say the hard true thing when it won't cost them.
Practices:

- **Critique the work, not the person.** "This step asks for the address twice," not "you forgot the
  saved address." The artifact is on the table; the author is in the room as a colleague.
- **The author listens; doesn't defend.** Reframe the author's job as *gathering input to decide
  later*, not *winning now*. Reflexive defence kills the signal and the safety at once.
- **Strengths first, always** (every framework builds this in). It is honest *and* protective, and it
  tells the team what not to break.
- **No seagulls.** No swooping in to drop opinions and leave without engaging the context or owning a
  decision (Kocienda's *Seagull Manager*). Reviewers stay for the decision or send written feedback
  in advance.
- **Equal airtime.** The facilitator draws out quiet reviewers and curbs dominators; access to the
  room is earned by improving the work, not by rank or volume.
- **Separate the maker from the made.** Make explicit that iterating on a design is the *normal*
  path (creative selection = demo → feedback → next demo), so "change this" reads as the process
  working, not as failure.

---

## 6. Capture decisions, not comments (the deliverable)

Comments evaporate; **the decision log is the deliverable.** For every open question / piece of
feedback, record one resolution:

| Tag | Means | Record |
|---|---|---|
| **Decided** | The decider settled it now | What + who decided + one-line why (for taste, the conviction) |
| **Author's call** | The author owns the fix/choice | Owner + by-when |
| **Needs a demo / spike** | Can't decide without seeing it | The *variation to build* before the next round |
| **Parked** | Out of scope / later | The reason, so it isn't silently dropped |

Decision-log row shape:

```
| Q / Feedback | Kind (req/taste) | Resolution | Owner | Why (1 line) | Decider |
```

End the log with the **next demo** (the concrete thing to build for the next round) and any
**live-on-it** items (heuristic calls to dogfood over time, *not* to re-argue next meeting —
`doctrine/references/creative-selection-and-taste.md` rule 2). A crit that produced only comments and
no decisions was theatre; the test of a good crit is that the same argument does **not** reopen next
week.

---

## 7. Live vs. async — which to run

| | **Live (synchronous)** | **Async (written)** |
|---|---|---|
| **Best when** | Exploratory work; needs back-and-forth; safety is fragile; a decision is needed *now* | Distributed/time-zoned team; well-framed asks; a written record matters; smaller deltas |
| **Frame** | Spoken at the top, written to the doc | Written at the top of the thread (non-negotiable — async has no facilitator to repair a bad frame in real time) |
| **Feedback** | In the announced framework, spoken | In the framework's shape, **each comment tagged `[requirement]` / `[taste]`** |
| **Decider** | Decides in the room | Resolves each thread with a decision tag |
| **Risk** | Loudest-voice bias; no record unless captured | Tone is lost in text; threads sprawl; slower |
| **Mitigation** | Facilitator enforces airtime + captures | Tighter frame, explicit tags, a hard "decider resolves by <date>" |

**Async discipline:** the frame must be *more* explicit (no facilitator to course-correct live),
every comment carries its taste/requirement tag, and the decider closes each thread with a decision —
the thread summary *is* the decision log. Use async to widen who can contribute and to leave a record;
use live when the work needs real-time divergence and a same-session decision. Many teams do both:
async pre-reads, then a short live session for the contentious calls.

---

*Operationalises `doctrine/references/creative-selection-and-taste.md` (demo-grounded critique; the
algorithm-vs-heuristic split behind taste-vs-requirement; the single decider + decision capture; the
"41 shades of blue" taste-not-vote rule; "live on it") and `doctrine/design-doctrine.md` (the
human-design-authority asymmetry rule). The three feedback frameworks (I-like/I-wish/what-if;
problem-not-solution; ladder of feedback) are standard design-studio crit practice. Companion to the
EVALUATE skills `heuristic-evaluation-and-design-critique` and `design-audit`, which produce the
findings a crit may discuss.*
