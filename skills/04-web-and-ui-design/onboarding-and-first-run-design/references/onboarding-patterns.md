# Reference: Onboarding & First-Run Patterns

The canonical pattern catalog for the `onboarding-and-first-run-design` skill. Each pattern is
written to be applied against a real first-run flow: *what it is → when to use it → how to do it
right → the anti-pattern it replaces.* Every rule traces to human design authority and the engine's
doctrine — never to an AI tool's default "welcome flow" (which is precisely the convergent slop the
Mission exists to beat).

**Provenance.** Distilled from Theresa Neil's *Mobile Design Pattern Gallery* (2nd ed., 2014) —
the **Tutorials & Invitations** and **Anti-Patterns** chapters — and Bill Scott & Theresa Neil's
*Designing Web Interfaces* (2009) **Provide an Invitation** principle, updated to 2026 and aligned to
WCAG 2.2 and `doctrine/design-doctrine.md`. Cross-referenced with the engine's
`docs/book-study/02-interaction-patterns.md` and `doctrine/references/interaction-anti-patterns.md`.

The north star: **time-to-value, not time-to-tour.** Every pattern below is judged by whether it
shortens the path from first open to the user's first real moment of worth.

---

## 1. Value-first sequencing — deliver worth before asking for commitment

The foundational rule. It directly enforces `interaction-anti-patterns.md` **§B1 Forced Sign-Up**:
*"a long sign-up form = a deleted app"* — the single highest install-killer documented.

### The value-first ladder (prefer the top rung you can reach)

1. **Try-before-you-buy / guest mode** — the user does the valuable thing with **no account at all**.
   Best where any meaningful taste of value can be delivered anonymously (a calculator, a one-off
   document, a preview, a sample dataset). Save/sync/share is what later motivates the account.
2. **Deferred registration** — let the user work, then ask to sign up **at the moment identity is
   genuinely needed** (to save, sync across devices, pay, or send on their behalf). By then they have
   felt the worth, so the ask converts instead of repelling.
3. **OAuth / passkeys over a password form** — when you must create identity, one tap (Sign in with
   Apple/Google, a passkey) beats a multi-field registration. Ask the **minimum** set only.
4. **Minimum-field registration** — the floor. Only the fields the account truly needs *now*; defer
   everything else (profile, preferences, team setup) to after first value.

### The gate-decision rule

For each action in the first run, ask: **does this genuinely require identity?**
- **No** (browse, try, preview, compute, configure) → never gate it. Let the anonymous user do it.
- **Yes** (persist, sync, pay, send-as-user, invite) → gate **only that action**, at the point it is
  reached — and the user has already seen value, so the wall is a door, not a barrier.

**Personalise *after* the user is in, never before.** A "tell us about yourself" survey before any
value is the same anti-pattern in a different costume.

---

## 2. Empty-state-as-onboarding — the first screen teaches

The first screen a real new user sees is almost always **empty**. That is not a void to apologise for
— it is the highest-leverage onboarding surface the product owns (`interaction-anti-patterns.md` §C3
Dead End forbids the do-nothing empty state).

**A first-run empty state must:**
- **Explain the value in one line** — what will live here and why it matters.
- **Show exactly one primary action** — the path to the activation moment ("Create your first X",
  "Connect your data", "Invite a teammate"). Focus lands here.
- **Be authored** — an illustration or a real seeded preview in the brand's style, never a centered
  grey sad-face icon (`doctrine/design-doctrine.md` Anti-Slop Charter).
- **Distinguish first-run-empty from cleared/no-results-empty** — different cause, copy, and action.

**Seed sample/demo data where the product allows it.** Showing value on screen zero (a sample board,
a demo chart) beats an empty canvas — with a clear "this is a sample — add your own / clear samples"
affordance so it is never mistaken for the user's real data.

> Division of labour: this skill owns the **first-action choice and its place in the activation arc**;
> the *pixel craft* of the empty state (illustration, skeleton geometry, motion) belongs to
> `04-web-and-ui-design/empty-error-and-loading-states`. Compose, don't duplicate.

---

## 3. The getting-started checklist — visible, optional, short

For products whose activation is genuinely multi-step (connect data → invite → send first item), a
**getting-started checklist** makes progress legible and gives the user agency over order.

**Do it right:**
- **Cap it at a few high-value steps** (≈3–5). A 12-item checklist is friction dressed as guidance.
  Each item must map to real value, not setup theatre.
- **Let the user choose order** where possible; show **real completion state** (checked when actually
  done, not when merely viewed).
- **Always dismissable / collapsible** — it is a helper, never a wall. The product is fully usable
  with the checklist ignored.
- **Celebrate completion proportionately** — a quiet confirmation, not confetti for connecting an
  account. Reserve any flourish for a moment that truly earns it.
- **Accessible** — completion shown by icon + text, not colour alone (WCAG 1.4.1); progress announced
  to screen readers (4.1.3).

**Anti-pattern:** front-loading every feature into a long wizard or checklist that *lengthens*
time-to-value — the opposite of the skill's purpose.

---

## 4. Progressive & just-in-time disclosure — teach as needed, not all at once

Do not explain the whole product on screen one. **Reveal capability at the moment it becomes
relevant.** (Scott & Neil, *Progressive Disclosure*; Neil, *let-the-user-do* > passive tour.)

- **Core path first.** Get the user to the aha on the simplest possible route; hide advanced options
  until they're needed.
- **Contextual hints over front-loaded tours** — a single tip on the screen where a feature lives, the
  first time the user arrives there, beats a six-slide tour on launch that's forgotten before it's
  relevant.
- **Learn-by-doing beats watching.** An interactive first task (the user actually sends the invoice,
  with light guidance) outperforms a passive walkthrough they tap through. Book-study 02: single-CTA
  transparency and let-user-*do* beat multi-step tours (Intuit Snap Payroll).

---

## 5. Coachmarks, tooltips & product tours — SPARINGLY, never as a UI fix

Overlay teaching is a **last resort**, not a default. **A UI that needs a tour to be usable has a
discoverability bug the tour is papering over** — fix the UI (labels, signifiers, sane defaults)
first, then teach only the genuinely non-obvious remainder.

### The sparing-use rules
- **One or two coachmarks at most**, on controls that are genuinely non-obvious — not a guided tour of
  the whole screen.
- **In-context trigger** — fire a hint the first time the user lands where the feature lives, not all
  at once on launch.
- **Always skippable, never trapping** — no forced, unskippable sequence; that is the **Trap / Forced
  Action** anti-pattern (`interaction-anti-patterns.md` §C4). A visible "Skip" / dismiss on every step.
- **Touch reality** — tooltips on **hover have no touch equivalent** (`interaction-anti-patterns.md`
  §E3; book-study 02 flags hover as the single biggest desktop-only hazard). Never hide essential
  first-run guidance behind hover; use tap-triggered or persistent hints on touch.
- **Reduced motion** — any spotlight/highlight/coachmark animation honours `prefers-reduced-motion`
  (WCAG 2.3.3); coachmark controls are focusable, ≥24px (2.5.8), and announced (4.1.3).

### Tour vs just-in-time — the decision
| Situation | Right pattern |
|---|---|
| One genuinely non-obvious control | A single in-context coachmark, skippable |
| Feature relevant only later | Just-in-time hint when the user reaches it |
| "The whole UI is confusing" | **Not a tour** — fix discoverability first |
| Multi-step activation | A getting-started checklist (§3), not a forced tour |
| You feel you *need* a 5-step tour | A design smell — simplify the first run instead |

---

## 6. Permission-priming — ask in context, after explaining why

Never fire an OS permission prompt (notifications, location, camera, contacts) cold on first launch —
a denied prompt is usually permanent. **Prime first:** an in-app explanation of *why* the permission
delivers value, shown **at the moment it's relevant** (when the user does the thing that needs it),
with the user choosing to proceed — *then* trigger the system prompt. This respects user agency and
dramatically improves grant rates without coercion. Asking before any value is the sign-up
anti-pattern wearing a permission dialog.

---

## 7. Time-to-value (TTV / TTFV) — the measure that judges every decision

- **Define the activation moment** ("aha") concretely — the first action that delivers real value.
- **Measure the path** to it: steps and seconds from open to aha for a cold new user.
- **Remove or defer** anything between open and aha that isn't essential: sign-up walls, tours,
  profile setup, permission prompts → push them past the aha (or cut them).
- **Re-measure.** Onboarding success is a *shorter* path to value, not a *prettier* tour. The shortest
  honest path to the first real win wins.

---

## How the skill uses this

- The **First-Run Checklist** in `SKILL.md` is the go/no-go gate; each item maps to a section here.
- §1 (value-first) and §5 (sparing tours) are the two hardest lines — they enforce
  `interaction-anti-patterns.md` §B1 (Forced Sign-Up) and §C4 (Trap / Forced Action) respectively.
- Read alongside `doctrine/design-doctrine.md` (Mission + Anti-Slop Charter — the welcome and empty
  states must look authored) and `empty-error-and-loading-states` (the first-run empty state's craft).

*Companion to `doctrine/references/`. Patterns evergreen; sources (Neil 2014, Scott & Neil 2009)
refreshed to 2026 — dead-platform specifics removed, WCAG 2.2 and doctrine alignment added.*
