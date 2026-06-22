---
name: onboarding-and-first-run-design
description: Use when designing the first-run / activation experience of a product — what a new
  user sees and does between their first open and their first real moment of value. Covers
  value-first sequencing (delay sign-up, let people try before they commit), progressive
  disclosure of features, the empty state AS onboarding, activation flows and setup checklists,
  coachmarks/tooltips/product-tours (used sparingly), permission-priming, and time-to-value /
  time-to-first-value optimisation. Triggers on "onboarding", "first run", "first-run experience",
  "activation", "getting started", "welcome flow", "product tour", "walkthrough", "coachmark",
  "tooltip tour", "setup checklist", "getting-started checklist", "aha moment", "time to value",
  "TTV", "TTFV", "new-user experience", "NUX", "empty state onboarding", or "sign-up wall".
  Forbids the Forced Sign-Up wall before any value, forced/unskippable tours, and feature-tour
  theatre that delays the first real action. Pairs with empty-error-and-loading-states (the
  first-run empty state) and landing-page-and-conversion-design (what happens after the CTA click).
status: active
metadata:
  portable: true
  category: 14-conversion-and-web-page-patterns
  compatible_with:
    - claude-code
    - codex
---

# Onboarding & First-Run Design — Time-to-Value, Not Time-to-Tour

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

> Onboarding has one job: get a brand-new user to their **first real moment of value** as fast and
> as honestly as possible — then teach the rest just-in-time, as they need it. The failure modes
> are well documented: a sign-up wall before any value ("a long sign-up form = a deleted app"), a
> forced multi-step tour the user taps through without reading, and a blank screen that explains
> nothing. The doctrine's Mission applies: a generic three-coachmark "Welcome!" overlay on an Inter
> gradient tells the user no one authored this. The empty state is your best onboarding canvas — use it.

<!-- dual-compat-start -->
## Use When

- You are designing the **first-run experience** of a product, feature, or workspace: what a new
  user sees and does between first open and first real value.
- You need to decide **when to ask for sign-up** — and the answer is almost always "after the user
  has seen worth," not "on first launch."
- You are designing an **activation flow**, a **getting-started checklist**, a **setup wizard**, or
  the **first-run empty state** of a key screen.
- Someone is reaching for a **forced product tour / coachmark sequence** to explain a confusing UI —
  STOP: fix the UI's discoverability first, then teach the *remainder* just-in-time and skippably.
- You are optimising **time-to-value (TTV) / time-to-first-value (TTFV)** — shortening the path
  from open to "aha."

## Do Not Use When

- The work is the **marketing landing page** that *precedes* the product — use
  `04-web-and-ui-design/landing-page-and-conversion-design`. That skill *ends* at the CTA click;
  THIS skill owns everything after it.
- You only need the **visual/interaction design of the first-run empty state in isolation** (skeleton
  geometry, illustration, motion) — that is `04-web-and-ui-design/empty-error-and-loading-states`.
  This skill *composes* the empty-state-as-onboarding into the larger activation arc; come here for
  the sequencing and the first-action choice, go there for the state's pixel craft.
- You need the **wording** of welcome copy, tooltips, checklist items, or empty-state prompts — use
  `10-content-design-and-ux-writing/ux-writing-and-microcopy` (and `error-empty-and-system-messaging`
  for empty/first-run copy). Route wording there; own placement, sequence, and behaviour here.
- The task is a **multi-step checkout/purchase flow** — use
  `06-sector-and-domain-ux/ecommerce-and-checkout-ux`. Onboarding ends at first value, not at payment.
- The task is **form field anatomy / validation** for the sign-up form itself — start at
  `04-web-and-ui-design/form-ux-design` (it owns the field set; come here for *when* and *whether*
  to show that form at all).

## Required Inputs

- **The activation moment ("aha").** The single, concrete action that first delivers real value to a
  new user (e.g. "sent their first invoice," "saw their data on a chart," "invited a teammate"). If
  you cannot name it in one sentence, you cannot design onboarding — find it first. This is the
  target every step must shorten the path to.
- **What genuinely requires identity** — and what does not. Most products can deliver a meaningful
  taste of value to an anonymous/guest user; only the actions that *truly* need an account (saving,
  paying, syncing across devices, sending on the user's behalf) should gate behind sign-up.
- **The new user's starting context** — cold (from an ad, knows nothing) vs warm (referred, already
  sold) vs invited (a teammate added them to an existing workspace). Each needs a different first run.
- **The real first-run data reality** — is the account genuinely empty, or can it be seeded with
  sample/demo data so the value is visible immediately? (Design around real content, never lorem.)
- **The brand's illustration/voice/type system** (or a note that none exists) so the welcome,
  empty states, and checklist are *authored*, not a stock "Welcome aboard!" with a rocket emoji.

## Workflow

### 1. Name the activation moment and measure the current path to it
Write down the one "aha" action and the current **time-to-first-value** (steps and seconds from open
to that action). Every later decision is judged by whether it *shortens* that path. If the current
first run inserts a sign-up wall, a tour, and a profile setup *before* the aha, those are the three
things to remove or defer.

### 2. Deliver value before asking for commitment (value-first; delay sign-up)
This is the spine of the skill and the doctrine's ethics line, and it directly avoids the **Forced
Sign-Up** anti-pattern (`doctrine/references/interaction-anti-patterns.md` §B1 — *"a long sign-up
form = a deleted app"*, the single highest install-killer).

- **Let the user *do* the valuable thing first**, anonymously or with the lightest possible identity.
  Gate **only** the action that genuinely needs an account — and at that point the user has already
  felt the worth, so the ask converts.
- Offer, in order of preference: **try-before-you-buy / guest mode**, **deferred registration**
  (ask after value), **passkeys / OAuth** over a password form, and the **minimum field set** when
  you must ask. Never a full registration form on first launch.
- **Personalise *after* the user is in**, not before — a "tell us about yourself" wall before any
  value is the same anti-pattern wearing a survey.
- See `references/onboarding-patterns.md` §1 for the value-first ladder and the gate-decision rule.

### 3. Make the empty state do the onboarding (empty-state-as-onboarding)
The first screen a real user sees is usually **empty** — that is not a void to apologise for, it is
the highest-leverage teaching surface the product has.

- The first-run empty state **explains the value in one line, shows one primary action** (the path to
  the aha), and prefers an **authored illustration or a real seeded preview** over a sad-face icon.
- Distinguish *first-run empty* (never had data — onboarding opportunity) from *cleared/no-results
  empty* (different copy, different action). Defer the visual/motion/skeleton craft to
  `empty-error-and-loading-states`; own the *first-action choice* and its sequence here.
- Prefer **seeding sample/demo data** so value is visible on screen zero, with a clear "this is a
  sample — add your own" affordance, where the product allows it.

### 4. Teach the rest progressively and just-in-time (progressive disclosure)
Do **not** front-load every feature. Reveal capability **as the user reaches the moment it matters**.

- Show the **core path first**; surface advanced features contextually, the first time they become
  relevant (a tip on the screen where the feature lives, not in a tour on screen one).
- Use a **getting-started checklist** for multi-step activation (e.g. connect data → invite a
  teammate → send first item): it makes progress visible, lets the user choose order, is **always
  dismissable**, and shows real completion state. Cap it at a few high-value steps — a 12-item
  checklist is friction, not guidance. See `references/onboarding-patterns.md` §2–3.
- Prefer **"let the user *do* it"** (interactive, learn-by-doing) over a **passive tour** they watch
  and forget. Doing beats watching (book-study 02: single-CTA transparency and let-user-*do* beat
  multi-step tours).

### 5. Use coachmarks, tooltips, and tours SPARINGLY — and never as a fix for a confusing UI
Overlay teaching is a **last resort**, not a default. A UI that needs a five-step tour to be usable
has a discoverability bug the tour is papering over — fix the UI first (labels, signifiers, sensible
defaults).

- When you *do* use overlay hints: **one or two coachmarks at most**, on genuinely non-obvious
  controls, triggered **in context** (the first time the user lands where the feature lives), and
  **always skippable** — never a forced, unskippable sequence (that is the **Trap / Forced Action**
  anti-pattern, `interaction-anti-patterns.md` §C4).
- Tooltips on hover are **desktop-only and have no touch equivalent** — never hide essential
  first-run guidance behind hover (book-study 02; `interaction-anti-patterns.md` §E3). Use tap/
  persistent hints on touch.
- Honour `prefers-reduced-motion` for any spotlight/coachmark animation (WCAG 2.3.3).
- See `references/onboarding-patterns.md` §4 for the sparing-use rules and the tour-vs-just-in-time
  decision.

### 6. Hold the line on accessibility, escapability, and honesty
- **Always provide an exit.** Every onboarding step — tour, checklist, wizard, modal welcome — is
  **skippable** and the product is fully usable without completing it (no **Trap / Forced Action**,
  `interaction-anti-patterns.md` §C4). Skipping carries no penalty.
- **No dark patterns at the gate.** No confirmshaming the "skip" ("No thanks, I don't want to be
  productive"), no pre-checked marketing opt-ins, no roach-motel ("one click to start, ten to leave").
- **Accessible first run** (`doctrine/references/wcag-2.2-criteria.md`): every onboarding control is a
  real focusable element with a visible focus ring and ≥24×24px target (SC 2.5.8); focus moves
  sensibly when a coachmark/step appears or dismisses (2.4.3); progress and step changes announce to
  screen readers (4.1.3); never colour-alone for checklist completion (1.4.1); reduced-motion path.

### 7. Specify, then build
Produce a first-run flow spec (see `examples/`): the named aha, the value-first sign-up decision, the
screen-by-screen sequence from open to aha, the empty-state-as-onboarding treatment, the checklist
(if any), where (and whether) any coachmark fires, and the WCAG/escape constraints. Run the checklist
below first.

## First-Run Checklist (run before building)

1. **Activation moment named** in one sentence; current time-to-first-value measured.
2. **Value before sign-up** — the user reaches a real taste of value *before* any registration wall;
   only identity-requiring actions gate (guest/OAuth/passkey/deferred preferred). No Forced Sign-Up.
3. **First-run empty state teaches** — one-line value + one primary action toward the aha; authored,
   not a sad-face icon; seeded sample data where possible.
4. **Progressive disclosure** — core path first; advanced features revealed just-in-time, not
   front-loaded; checklist (if used) ≤ a few high-value steps and dismissable.
5. **Coachmarks/tours used sparingly** — ≤1–2, in-context, on genuinely non-obvious controls, never
   as a substitute for fixing a confusing UI; no hover-only first-run guidance.
6. **Everything skippable** — no forced/unskippable step; product fully usable without finishing
   onboarding; no penalty for skipping (no Trap / Forced Action).
7. **No dark patterns** — no confirmshaming skip, no pre-checked opt-ins, no roach-motel.
8. **Accessible** — focusable controls, visible focus, ≥24px targets, sensible focus on step change,
   announced progress, not colour-only, reduced-motion path.
9. **No convergent default** — the welcome/empty/checklist are authored to the brand, not a stock
   "Welcome aboard 🚀" overlay on an Inter gradient (`doctrine/design-doctrine.md` §0).

If any item can't be satisfied (no clear aha, a stakeholder insists on a sign-up wall or a forced
tour), **say so and ask** — never quietly ship the install-killing or convergent version.

## Anti-Patterns

- **Forced Sign-Up — the wall before the value** (`interaction-anti-patterns.md` §B1). "Create an
  account to continue" on first launch, before the user has seen anything worth an account. The
  single highest install-killer; the skill exists primarily to prevent this.
- **Forced / unskippable tour** (`interaction-anti-patterns.md` §C4 Trap) — a multi-step coachmark
  sequence the user can't escape, blocking the product until they tap through it. They tap blindly,
  learn nothing, and resent it.
- **Tour-as-bandage** — using a product tour to explain a UI that is confusing because it's badly
  designed. Fix discoverability first; the tour is not the fix.
- **Front-loading every feature** — a 9-step wizard or a 12-item checklist that buries the one action
  that matters under setup theatre, lengthening time-to-value instead of shortening it.
- **The blank-void first screen** — an empty state that just says "Nothing here yet" with no value
  explanation and no first action. Wastes the best onboarding moment (`interaction-anti-patterns.md`
  §C3 Dead End).
- **"Tell us about yourself" before any value** — a profiling/personalisation wall that is the
  sign-up anti-pattern in a different costume.
- **Hover-only first-run hints** (`interaction-anti-patterns.md` §E3) — guidance that vanishes on
  touch and keyboard.
- **Confirmshaming the skip / dark patterns at the gate** — coercing completion with guilt copy,
  pre-checked opt-ins, or a roach-motel.
- **The generic welcome overlay** — "Welcome aboard! 🚀" on an Inter/indigo gradient with three
  identical coachmarks; the convergent default the Mission targets (`doctrine/design-doctrine.md`).

## Outputs

- A **stated activation moment** and a measured/target **time-to-first-value**.
- A **value-first sign-up decision**: what is anonymous/guest, what gates, and the chosen auth method.
- A **first-run flow spec** (screen-by-screen, open → aha) including the empty-state-as-onboarding
  treatment and the progressive-disclosure plan, in the shape of `examples/`.
- A **getting-started checklist** definition (if used) — items, order-freedom, dismissability,
  completion state.
- A **completed first-run checklist** confirming no Forced Sign-Up, no forced tour, full skippability,
  zero dark patterns, and WCAG 2.2 compliance.

## Examples

- `examples/first-run-flow-for-a-team-todo-app.md` — a full, real first-run spec for a sample product
  (a small-team task app, "Cadence"): the named aha, the value-first decision (try anonymously, defer
  sign-up to the save-across-devices moment), the screen-by-screen sequence, the empty-state-as-
  onboarding treatment, a 3-item getting-started checklist, the single in-context coachmark, and the
  escape/WCAG constraints applied. Not a template — an authored flow with stated decisions.

## References

- `references/onboarding-patterns.md` — the pattern catalog: the value-first ladder and gate-decision
  rule, empty-state-as-onboarding, the getting-started checklist pattern, progressive/just-in-time
  disclosure, the sparing-use rules for coachmarks/tooltips/tours, permission-priming, and the
  time-to-value method.
- `doctrine/design-doctrine.md` — the Mission (§0, "the moat is looking human-made") and the
  Anti-Slop Charter: the welcome, empty states, and checklist must look authored, never a stock
  "Welcome aboard" overlay.
- `doctrine/references/interaction-anti-patterns.md` — **§B1 Forced Sign-Up** (value before auth — the
  central rule this skill enforces), **§C4 Trap / Forced Action** (everything skippable), **§C3 Dead
  End** (the empty state offers a next action), **§E3 Desktop-Hover Dependency** (no hover-only
  first-run guidance).
- `doctrine/references/wcag-2.2-criteria.md` — focusable controls and visible focus, target size
  ≥24px (2.5.8), focus order on step change (2.4.3), live-region progress announcements (4.1.3),
  colour-not-alone (1.4.1), reduced motion (2.3.3) for coachmark/spotlight animation.
- Sibling `04-web-and-ui-design/empty-error-and-loading-states` — owns the **pixel craft** of the
  first-run empty state (illustration, skeleton, motion); this skill composes it into the activation arc.
- Sibling `04-web-and-ui-design/landing-page-and-conversion-design` — owns the marketing page that
  *precedes* the product; it ends at the CTA click, this skill begins there.
- `10-content-design-and-ux-writing/ux-writing-and-microcopy` and `error-empty-and-system-messaging` —
  own the **words** of welcome copy, tooltips, checklist items, and empty-state prompts.
<!-- dual-compat-end -->
