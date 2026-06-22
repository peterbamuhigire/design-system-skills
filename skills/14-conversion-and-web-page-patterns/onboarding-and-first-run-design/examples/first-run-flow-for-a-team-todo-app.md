# Worked example — first-run flow: "Cadence" (small-team task app)

A real, screen-by-screen first-run spec for a sample product. Not a template — an authored flow with a
**named activation moment**, a **value-first sign-up decision** (try anonymously; defer the account to
the save-across-devices moment), the **empty-state-as-onboarding** treatment, a **3-item getting-
started checklist**, exactly **one in-context coachmark**, and the escape/WCAG constraints applied.
Use this as the *shape* of the spec this skill produces.

---

## Product & brief

- **Product:** **Cadence** — a shared task board for small teams (3–15 people). Web + mobile.
- **Activation moment ("aha"):** **the user creates their first task and drags it to "Doing."** That
  is the first time the product's core value — a live, shared board — is visible and felt.
- **Audience & stage:** mixed. *Cold* (from a blog post, knows nothing), *warm* (referred), and
  *invited* (a teammate added them to an existing board — a different first run, §"Invited path" below).
- **First-run data reality:** a brand-new board is empty; Cadence can **seed a 3-card sample lane**
  ("Sample: plan a team offsite") so value is visible on screen zero.
- **Brand system (authored, stated before markup):** Cadence's distinctive idea is a **metronome /
  tempo motif** — a thin tick-rule down the left of each lane and a humanist-grotesque body paired with
  a single confident display face for board titles. Empty/welcome states use a hand-drawn metronome
  line-illustration in the brand stroke, **not** a stock "Welcome aboard 🚀" overlay. (Per
  `doctrine/design-doctrine.md` §0; explicitly NOT Inter + indigo gradient + three coachmarks.)

### Current vs target time-to-first-value
- **Old first run (rejected):** Sign-up wall → email verify → "tell us about your team" survey →
  empty board. ~6 steps / ~90s before any value, with the **Forced Sign-Up** install-killer up front.
- **Target:** **open → board with seeded sample → create first task → drag to Doing.** Aha in **≤2
  steps / under 20s**, **with no account required to get there.**

---

## The value-first sign-up decision (Workflow §2; `references/onboarding-patterns.md` §1)

Run the **gate-decision rule** over every first-run action:

| Action | Needs identity? | Decision |
|---|---|---|
| View the board / sample lane | No | Anonymous — no account |
| Create / edit / drag a task | No | Anonymous — **the aha happens with no sign-up** |
| **Save the board across devices / reload** | Yes | Gate here — deferred registration |
| Invite a teammate | Yes | Gate here |
| Get notifications | Yes (OS perm) | Prime in context (§permission below) |

**Ladder rung chosen:** **guest mode → deferred registration.** The user builds a real board
anonymously (held in local + a guest session). The account ask appears **only** when they do something
that genuinely needs persistence — and by then they've felt the value, so it converts.
**No Forced Sign-Up wall** (`interaction-anti-patterns.md` §B1).

---

## Screen-by-screen first run (cold/warm path)

### Screen 1 — Open → board, already valuable (no welcome modal)
- The user lands **directly on a board**, not a splash or a sign-up wall. A seeded **"Sample: plan a
  team offsite"** lane (3 cards across To-do / Doing / Done) shows the product working immediately.
- A single, quiet **first-run empty prompt** sits in the empty "To-do" column of the user's *own*
  lane (`empty-error-and-loading-states` owns its pixel craft; this skill owns the action):
  - One line of value: *"Your team's work, moving in real time."*
  - **One primary action:** **"Add your first task"** (focus lands here).
  - The metronome line-illustration in brand stroke — authored, not a sad-face icon.
- A discreet "Clear sample" affordance on the sample lane so it's never mistaken for real data.
- **No welcome modal, no tour, no "Welcome aboard 🚀."** The board *is* the welcome.

### Screen 2 — First task (the aha), guided by doing, not watching
- The user types a task and presses Enter — it appears as a card. **One in-context coachmark** (the
  only one in the whole first run) points at the new card: *"Drag me to **Doing** when you start."*
  - Triggered **the first time a card exists**, not on launch (just-in-time, §4).
  - **Skippable** — a visible "Got it" dismiss; the coachmark never blocks the board
    (`interaction-anti-patterns.md` §C4 Trap). Reduced-motion: the spotlight fades statically.
- The user drags the card to **Doing** → **activation moment reached, with no account.** A quiet,
  proportionate confirmation (the card settles with a single tick of the tempo motif) — **no confetti**
  for a routine action.

### Screen 3 — The deferred sign-up, at the moment it earns the ask
- Triggered **only** when the user reloads, leaves, or hits "Save / sync across devices" — i.e. the
  first action that genuinely needs identity.
- The ask is honest and minimal: *"Keep this board — sign in to save it and use it on every device."*
  with **OAuth / passkey first** (Sign in with Google/Apple), a single email field as fallback.
  No "tell us about your team" survey here — **personalise later**.
- **Skippable** ("Not now") — the user keeps working in the guest board; the ask returns next time the
  account is genuinely needed. No confirmshaming the skip; no pre-checked marketing opt-in.

### Getting-started checklist — 3 items, optional, post-aha
A collapsible checklist appears **after** the first task (never before value), capped at the three
high-value steps to a fully-activated team board (`references/onboarding-patterns.md` §3):

1. ✅ **Create your first task** (already done — checked on real completion, by icon + text not colour).
2. ⬜ **Invite a teammate** (the multiplayer aha — gates on account, links to deferred sign-up).
3. ⬜ **Set up notifications** (permission-primed — see below).

- **Dismissable / collapsible**; the board is fully usable with it ignored. Progress announced to
  screen readers (4.1.3). Completing all three shows a quiet "Your board's in rhythm" — not confetti.

### Permission-priming — notifications, in context
When the user taps checklist item 3 (or first @mentions a teammate), Cadence shows an **in-app primer**
first: *"Get a ping when a teammate moves your card — so you're never out of sync."* Only on
"Turn on" does it fire the **OS permission prompt**. Never cold on launch
(`references/onboarding-patterns.md` §6).

---

## Invited path (a teammate added them to an existing board)

A different first run — this user arrives *warm and into real data*:
- The invite link opens **straight onto the shared board with real cards**, their name pre-filled from
  the invite. The aha here is *seeing the live team board*, which is immediate.
- The account ask is the lightest rung (passkey/OAuth, one tap) because saving their place needs
  identity — but it comes **after** they see the board, not before.
- **No sample lane, no "add your first task" prompt** — that would be wrong for someone joining a
  populated board. (Different starting context → different first run, per Required Inputs.)

---

## First-Run Checklist — applied

1. **Activation moment named** — "create first task + drag to Doing"; old TTFV ~90s/6 steps → target
   <20s/2 steps. ✅
2. **Value before sign-up** — aha reached anonymously; account deferred to the save/sync moment;
   OAuth/passkey first. **No Forced Sign-Up.** ✅
3. **First-run empty state teaches** — one-line value + one action ("Add your first task"), authored
   metronome illustration, seeded sample lane. ✅
4. **Progressive disclosure** — core path (add → drag) first; invite/notifications revealed via the
   3-item checklist just-in-time, not front-loaded. ✅
5. **Coachmarks sparingly** — exactly **one**, in-context, skippable, on a non-obvious action (drag);
   no hover-only hint. ✅
6. **Everything skippable** — coachmark dismissable, checklist collapsible, sign-up "Not now"; board
   fully usable throughout. No Trap / Forced Action. ✅
7. **No dark patterns** — no confirmshaming skip, no pre-checked opt-in, no roach-motel. ✅
8. **Accessible** — focusable controls + visible focus, ≥24px targets (2.5.8), focus moves to the new
   card / dismiss on coachmark change (2.4.3), checklist progress announced (4.1.3), completion by
   icon+text not colour (1.4.1), reduced-motion spotlight (2.3.3). ✅
9. **No convergent default** — authored metronome motif + display/grotesque pairing; no Inter+indigo
   gradient, no generic welcome overlay (`doctrine/design-doctrine.md` §0). ✅

---

## Acceptance criteria (handoff-ready)

A developer/QA can check each:

- [ ] First launch lands on a **board with a seeded sample lane** — **no sign-up wall, no welcome
      modal, no tour** before any value.
- [ ] The activation moment (create task → drag to Doing) is reachable with **no account**.
- [ ] Account is requested **only** at the first identity-needing action (save/sync/invite), offers
      **OAuth/passkey first**, and is **skippable** ("Not now") with no penalty.
- [ ] Exactly **one** coachmark in the whole first run, in-context, skippable; **no hover-only** hints.
- [ ] Getting-started checklist ≤ 3 items, appears **after** first value, collapsible/dismissable,
      completion shown by icon+text (not colour alone), progress announced to screen readers.
- [ ] Notification permission is **primed in-app** before the OS prompt; never fired cold on launch.
- [ ] Invited-user path skips the sample lane and "add first task" prompt; opens straight on real data.
- [ ] No confirmshaming, no pre-checked opt-ins, no roach-motel.
- [ ] All onboarding controls ≥24px (2.5.8), focusable with visible focus; focus handled on coachmark
      and step changes (2.4.3); reduced-motion path for the tempo-tick/spotlight motion (2.3.3).
- [ ] Welcome/empty/checklist copy sourced from `10-content-design-and-ux-writing/ux-writing-and-
      microcopy` and `error-empty-and-system-messaging`.
