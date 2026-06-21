# Usability Test Protocol — a real, runnable protocol

This is a working protocol you can run as-is. It covers **moderated** (deep, why) and **unmoderated** (scale, how-many) tests, the task-scenario discipline, the moderator script, and how to score what you see.

---

## 0. Before the session — set up to be defensible

- **State the decision.** One line: what changes based on this test. (e.g. "Decide whether the new 3-step onboarding ships or rolls back to the 1-step form.")
- **Pre-state success criteria** for each task — *before* you watch anyone, so you can't move the goalposts.
- **Recruit real target users.** Screen out employees, friends, and anyone who can guess the hypothesis.
- **Get informed consent + recording permission in writing.** Non-negotiable. Tell them they can stop anytime and that you're testing the design, not them.
- **Include at least one access-needs participant** (keyboard-only, screen-reader, low-vision, or motor) per round, or explicitly log it as a coverage gap (`doctrine/references/wcag-2.2-criteria.md`).
- **n:** 5 participants per segment for qualitative problem-finding; 20+ if you intend to report success rates or SUS as numbers.

---

## 1. Moderator intro script (read it, near-verbatim)

> "Thanks for joining. This should take about 45 minutes. A few things first:
> **We're testing the design, not you — there are no wrong answers, and you can't hurt my feelings.** I didn't design this, so be totally honest.
> I'll ask you to do some tasks. As you work, **please think aloud** — say what you're looking at, what you expect, what's confusing.
> I'll mostly stay quiet so I can see how it really works for you. If you get stuck, that's useful data — try as you would at home before asking me.
> Is it OK if I record the screen and audio for the team? You can stop at any time. — Great. Any questions before we start?"

Then **one warm-up question** to relax them and gather context: "Before we look at anything — tell me about the last time you signed up for a new app. What was that like?"

---

## 2. Task scenarios — the discipline that makes or breaks the test

A task scenario gives the user a **realistic goal and context**, and **never names the UI**. The user has to find the path; that's the whole point.

| ❌ Instruction (invalidates the test) | ✅ Scenario (valid) |
|---|---|
| "Click the blue **Sign up** button, then enter your email." | "You've decided to try this app. Get yourself to the point where you have an account and can use it." |
| "Use the **filter** dropdown to show only unpaid invoices." | "Your accountant asked which invoices are still unpaid. Find that out." |
| "Open **Settings → Notifications** and turn off email alerts." | "You're getting too many emails from this app. Make them stop, but keep using the app." |

Rules for writing scenarios:
- Goal-based, not click-based. Give a *reason*, not a *route*.
- Use the user's own data/context where possible (their real invoices, their real goal).
- One clear end-state per task so success is unambiguous.
- Order tasks roughly as a real journey; put the riskiest task early while attention is fresh.

---

## 3. Moderating — what to do while they work

- **Stay quiet.** Let silence do the work; people fill it with their real reasoning.
- **Don't lead, don't rescue.** No "it's the button on the right." When they're stuck: "What are you trying to do right now?" / "What did you expect to happen?"
- **Echo, don't interpret.** "You paused there — what was going through your mind?"
- **Ask why *after* the action, not before.** Observe behaviour first; explanations second.
- **Never defend the design** or explain how it "should" work. If you're explaining, you've found a problem.
- **Park new questions** with the timestamp; ask in the debrief so you don't break flow.

Per task, log: **completion** (success / partial / fail / gave up), **time**, **errors / wrong paths**, **the exact moment and quote where they struggled**, and **assists given** (each assist = a failure).

---

## 4. Post-task & debrief

- After each task: "On a scale of 1 (very hard) to 5 (very easy), how was that? Why that number?" (Single Ease Question.)
- After all tasks, optionally run **SUS** (10 statements, 5-point agree/disagree) for a comparable 0–100 score over time.
- Debrief: "What was the most frustrating moment? … the best? … if you had a magic wand, what's the one thing you'd change?"
- Thank, pay the incentive, confirm how the recording will be used.

---

## 5. Unmoderated variant (for scale)

Same scenarios and success criteria, delivered through a remote tool. Differences:
- **No follow-up "why"** — so write a one-line written reflection prompt after each task ("In one sentence: what, if anything, was confusing?").
- **Pilot with 2 people first** — you can't clarify a confusing task mid-session, so the wording must be bulletproof.
- Use it to get **task success rate and time at n=20–50**, then run a few moderated sessions on the worst-scoring task to learn *why*.

---

## 6. Severity rating — fix the right things first

Rate every issue so the team triages by impact, not by who shouted loudest. Severity = a judgement combining three factors (after Nielsen):

- **Frequency** — how many participants hit it?
- **Impact** — how hard was it to overcome? (cosmetic → blocked the task)
- **Persistence** — once met, do users keep tripping on it, or learn around it?

| Rating | Meaning | Action |
|---|---|---|
| **0 — Not a problem** | Disagree it's an issue | Ignore |
| **1 — Cosmetic** | Noticed, no task impact | Fix if spare time |
| **2 — Minor** | Slowed them, recovered | Low priority |
| **3 — Major** | Caused failure or serious difficulty for several | High priority — fix before ship |
| **4 — Catastrophe** | Blocked the task / lost data / lost trust | Must fix — blocker |

Tie each rated issue to participant IDs and a quote, so a "Major" claim is traceable to evidence, not vibes.

---

## 7. Reporting honestly

- Report qualitative issues by **severity and participant count** ("4 of 5 failed task 2"), not invented percentages.
- Report quantitative metrics (success rate, SUS) only when n supports it; state n every time.
- Every issue → a recommended fix → a confidence level. An issue with no recommendation is half-done.
- Flag any finding that reads as "this felt generic / I didn't trust it" as a slop/credibility signal (`doctrine/references/ai-slop-taxonomy.md`), not a minor nit — it threatens the authored-not-templated moat (`doctrine/design-doctrine.md` §0).

---

## Provenance
Think-aloud, scenario discipline, the 5-user heuristic, and the 0–4 severity scale follow established UX practice (Nielsen Norman Group; Krug, *Don't Make Me Test*; Dumas & Redish). SUS is Brooke (1986). Authority traces to the human UX literature, never AI-tool recommendations (`doctrine/design-doctrine.md` §2).
