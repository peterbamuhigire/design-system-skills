# Reference: Dark-Pattern (Deceptive-Pattern) Catalogue — pattern → why-harmful → honest swap

This is the cross-cutting **ethics catalogue** for the engine: the named deceptive patterns, grouped
into the seven families, each written so it can be checked against a live flow — *name → what it looks
like → why it harms the user → the honest swap*. It is the catalogue that `ecommerce-and-checkout-ux`
and `trust-credibility-and-social-proof` defer to, and the source the `design-ethics-and-anti-dark-
patterns` skill audits with.

**Naming note.** "Dark pattern" is the original term (Harry Brignull, 2010). Regulators and Brignull
himself now prefer **"deceptive pattern"** to avoid the colour connotation; the EU, FTC, and OECD use
"dark commercial pattern" / "deceptive design." This file uses *deceptive pattern* and *dark pattern*
interchangeably. The family taxonomy follows the widely-cited Brignull / Mathur et al. groupings,
aligned to `doctrine/references/interaction-anti-patterns.md` and the Chwezi Mission.

**The line.** A pattern is deceptive when the interface is built to make the user do something they
would **not** have chosen *with full information and a clear head* — i.e. it closes the gap between the
business goal and the user's goal by **coercion or concealment** instead of by value. Honest
persuasion (a clear value prop, real proof, a genuine deadline) is not a dark pattern; concealment,
trickery, asymmetry, and manufactured pressure are.

---

## Family 1 — Sneaking (slipping something past the user)

### 1.1 Sneak-into-basket
- **Looks like:** an item, warranty, "sample," insurance, or donation appears in the cart the user did
  not add — often injected by a checkbox on a *previous* page, or auto-added to cross a free-shipping
  threshold.
- **Why it harms:** the user pays for something they never chose; consent is manufactured by inertia.
  It is theft-by-friction and a top driver of chargebacks and lost trust.
- **Honest swap:** the basket contains **only what the user explicitly chose**. Cross-sells are
  offered as a clear, separately-confirmed add ("Add gift wrap? — No / Yes"), never pre-loaded. A
  free-shipping nudge states the gap ("£6 from free shipping") and lets the user decide.

### 1.2 Hidden costs / drip pricing
- **Looks like:** the headline price is not the real price — mandatory fees, "service charges," tax, or
  shipping are revealed only at the final step, dripped in one at a time so each feels small.
- **Why it harms:** the user invests effort on a false price and is ambushed at the commit point, when
  sunk cost makes them likely to pay anyway. Bait-and-switch.
- **Honest swap:** show the **all-in total before the commit point** — items + tax + shipping + every
  mandatory fee, adjacent to the pay/confirm action. If a cost needs an input (a postcode for
  shipping), ask for it early so the total is never a surprise. (Doctrine "Hidden costs"; `interaction-
  anti-patterns.md` B2.)

### 1.3 Hidden subscription / sneak-into-recurring
- **Looks like:** what reads as a one-off purchase silently enrols the user in a recurring charge, or
  the recurring nature is in greyed micro-copy.
- **Why it harms:** the user is billed indefinitely for something they thought was a single payment.
- **Honest swap:** any recurring charge is **stated plainly at the point of opt-in** — price, cadence,
  first-charge date, and the cancel path — and is opt-in, never default. (See Family 4.)

---

## Family 2 — Urgency (manufacturing time pressure)

### 2.1 Fake scarcity
- **Looks like:** "Only 2 left!", "Almost gone", "3 other people are looking at this" — invented or
  not tied to real inventory; the count resets or is identical for every product/visitor.
- **Why it harms:** rushes the user past deliberation with a lie; erodes trust the moment it is caught
  (and it is caught — users reload).
- **Honest swap:** show stock/scarcity **only when it is true and live**. Real low-stock is a genuinely
  helpful signal — drive it from real inventory. If you can't back the number, don't show it.

### 2.2 Fake / resetting countdown
- **Looks like:** a timer ("offer ends in 09:58") that restarts on reload, on the next visit, or runs
  perpetually; a "deal" deadline that never actually passes.
- **Why it harms:** manufactures a deadline that doesn't exist to force a rushed decision.
- **Honest swap:** a countdown is shown **only for a real, fixed deadline** that genuinely expires
  (a real sale end, a real slot-hold). When it ends, the offer actually ends.

### 2.3 High-demand / activity fabrication
- **Looks like:** "47 people booked this today", "selling fast" with no measurement behind it.
- **Why it harms:** false social pressure.
- **Honest swap:** if you show activity, it must be **measured and real**; otherwise omit it. (Cross-ref
  `trust-credibility-and-social-proof` — real attributed signals only.)

---

## Family 3 — Misdirection (steering away from the user's interest)

### 3.1 Confirmshaming
- **Looks like:** the decline option is worded to shame or guilt — "No thanks, I don't want to save
  money", "No, I'll stay disorganised", a tiny grey "skip" beside a giant glowing "Yes!".
- **Why it harms:** emotional manipulation; coerces the opt-in by making "no" feel bad.
- **Honest swap:** **neutral decline copy** — "No thanks", "Not now", "Skip" — given equal legibility
  and reachability to the accept option. The user's no is respected, not punished.

### 3.2 Visual interference / false hierarchy
- **Looks like:** the choice that benefits the business is the bright primary button; the user's likely
  choice is a faint link or hidden; the cheaper plan is visually buried under the recommended one.
- **Why it harms:** exploits scan patterns to make the coercive choice the path of least resistance.
- **Honest swap:** the user's likely/beneficial choice is **at least as prominent** as the business's
  preferred one. One genuine primary action; secondaries visible, not hidden. (`interaction-anti-
  patterns.md` B3, D6.)

### 3.3 Trick wording / double negatives
- **Looks like:** "Uncheck this box if you do not want to not receive emails"; toggles whose on/off
  meaning is reversed or ambiguous.
- **Why it harms:** the user can't tell what they're agreeing to; consent is not informed.
- **Honest swap:** plain, positive phrasing; the state of every toggle/checkbox is unambiguous and its
  default is the user-protective one.

### 3.4 Disguised ads / sponsored-as-organic
- **Looks like:** an advertisement or sponsored listing styled to look like organic content, an
  editorial result, or a system control.
- **Why it harms:** the user acts on it believing it is neutral; deception about the nature of the UI.
- **Honest swap:** **label sponsored/ad content** clearly; keep it visually distinct from organic
  results and from system chrome.

---

## Family 4 — Forced action (demanding something unrelated to proceed)

### 4.1 Forced continuity
- **Looks like:** a free trial that **auto-converts to a paid charge** with no reminder; the card is
  taken up front and the cancel is buried.
- **Why it harms:** bills users who forgot or never intended to continue; revenue extracted from
  inattention rather than value.
- **Honest swap:** state the auto-charge **plainly up front**, **remind before billing** (an email/in-
  app notice ahead of the charge), and make cancel **as easy as sign-up**. Better: a trial that simply
  *ends* (no card) or downgrades to free unless the user actively upgrades. (Doctrine "Forced
  continuity".)

### 4.2 Roach motel (easy in, hard out)
- **Looks like:** sign-up is one click; cancellation requires a phone call, a chat agent, a retention
  gauntlet, or is hidden across many screens.
- **Why it harms:** traps the user in a paid relationship by **asymmetry of effort** — the single
  most-regulated dark pattern (FTC click-to-cancel; CCPA symmetry rule).
- **Honest swap:** **symmetric exit** — if joining took N steps online, leaving takes ≤N steps online,
  by the same channel. No mandatory phone-call-only cancel for an online sign-up. (`interaction-anti-
  patterns.md` C4.)

### 4.3 Forced sign-up (wall before value)
- **Looks like:** "Create an account to continue" before the user has seen any of the product's worth.
- **Why it harms:** demands commitment before delivering value; the highest install/checkout-abandon
  driver.
- **Honest swap:** **value before auth** — browse/try first; **guest mode** offered; gate only the one
  action that genuinely needs identity; offer account creation *after*, reusing entered data.
  (`interaction-anti-patterns.md` B1.)

---

## Family 5 — Nagging (wearing the user down by repetition)

- **Looks like:** the same request re-fired every session — "enable notifications", "rate the app",
  "upgrade now", a cookie/consent banner that re-prompts after every "no"; persistent interruption of
  the user's actual task.
- **Why it harms:** converts by **attrition** — the user eventually says yes to make it stop, which is
  not real consent. It also degrades the core experience.
- **Honest swap:** **ask once, honour the answer.** Make "no" persist (a real "don't ask again");
  impose a meaningful interval before any re-ask; never block the task to re-ask. Tie a re-ask to a
  genuine moment of value, not a timer.

---

## Family 6 — Obstruction (making a path artificially hard)

- **Looks like:** the cancel/delete/downgrade/opt-out path is deliberately buried, gated behind extra
  confirmations, hidden in an unexpected place, or made to require contacting support; price or
  comparison information concealed to prevent shopping around.
- **Why it harms:** discourages a legitimate choice by friction rather than by reason — the user gives
  up. Overlaps with roach motel; obstruction is the broader "make the unwanted path hard" pattern.
- **Honest swap:** the friction to **leave / decline / delete / downgrade is no greater** than the
  friction to join / accept / buy / upgrade. Account deletion and data export are findable and direct.
  Comparison information is available, not hidden.

---

## Family 7 — Interface & social deception (bait-and-switch, fakery)

- **Looks like:** **bait-and-switch** (the user does one thing expecting result A and gets result B — a
  close button that opens an upsell, a "download" that installs something else); **fake testimonials /
  fabricated proof**; **fake "system" UI** (a fake notification badge, a fake error to drive an action).
- **Why it harms:** the interface lies about what it is or what an action does; the deepest breach of
  the user's trust in the UI itself.
- **Honest swap:** **every control does exactly and only what its label/affordance says.** Proof is
  real and attributed (defer to `trust-credibility-and-social-proof`). No fake system chrome, no fake
  errors, no decoy buttons.

---

## Consent UX (the rules a permission/opt-in dialog must pass)

Valid consent — the GDPR standard, which is also simply honest design — is:

1. **Freely given** — refusing is a real, penalty-free option; the service is not withheld for
   declining non-essential processing. "Accept or you can't use the app" is not free consent for
   non-essential data.
2. **Specific** — separate consent per purpose; no single "I agree to everything" bundling unrelated
   uses (analytics, ads, third-party sharing) into one switch.
3. **Informed** — the user is told who, what, why, and for how long, in plain language, *before* the
   choice — not in a linked 40-page policy.
4. **Unambiguous** — a clear affirmative action. **Pre-ticked boxes, opt-out defaults, and "continuing
   means you agree" are not valid consent.**
5. **As easy to withdraw as to give** — a one-click "reject all" / "withdraw" matching the one-click
   "accept all." Asymmetric consent dialogs (big "Accept all", buried "Manage → reject") are
   misdirection + obstruction, not consent.

**Consent theatre** (a dialog engineered to make "accept" the only easy path) ticks the legal box in
appearance only and is itself a deceptive pattern.

---

## Default ethics (the most powerful, most abused lever)

Defaults decide outcomes for most users, who never change them. Therefore:

- **The default is the choice an informed user acting in their own interest would make** — not the one
  that maximises revenue by inertia. Marketing emails **off** by default; data-sharing **off**;
  add-ons/insurance/donations **unchecked**; the cheapest fitting plan not pre-upgraded.
- **Opt-in for anything that costs the user money, privacy, or attention.** Opt-out defaults for those
  are coercion by inertia (and increasingly unlawful for personal data).
- A default that benefits the business *and* the user (e.g. autosave on) is fine — the test is whose
  interest the inertia serves.

---

## The comfort test ("would you be comfortable if the user saw this?")

For any decision you're unsure about, ask: **"Would I be comfortable explaining to this user's face
exactly why we designed it this way?"** If the honest explanation is some form of *"so you wouldn't
notice / so you'd find it too hard to leave / so you'd feel bad saying no"* — it is a dark pattern.
A complementary phrasing: *"Would this still work if it were fully transparent?"* Honest persuasion
survives transparency; a dark pattern depends on the user not seeing the mechanism.

---

## §Legal angle (kept deliberately light — flag, don't adjudicate)

Deceptive patterns are increasingly **illegal**, not merely unethical. Note exposure as reinforcement;
recommend counsel before a live launch. Headline regimes (as of 2026):

- **GDPR (EU/EEA) & UK GDPR** — consent must be freely-given/specific/informed/unambiguous and as easy
  to withdraw as to give (Arts. 4(11), 7); pre-ticked boxes invalid (*Planet49*). The **EDPB** has
  issued specific deceptive-design guidance for consent interfaces.
- **EU Digital Services Act (DSA), Art. 25** — bans dark patterns on online platforms outright; the
  **Unfair Commercial Practices Directive (UCPD)** and **Consumer Rights Directive** cover drip
  pricing, fake scarcity, and confirmshaming. The **Digital Fairness Act** is extending this.
- **CCPA / CPRA (California)** — explicitly defines and **prohibits dark patterns** in obtaining
  consent; the opt-out of sale/share must be **symmetric** (no harder than opt-in).
- **UK** — the **CMA** acts under consumer law; the **DMCCA 2024/25** strengthens powers over
  misleading urgency, drip pricing, and subscription traps.
- **US FTC** — enforces against deceptive design under §5; the **negative-option / "click-to-cancel"
  rule** requires cancellation to be at least as easy as sign-up; the **ROSCA** statute covers
  online subscriptions. State laws (e.g. California auto-renewal) add reminder/cancel duties.

**Posture:** lead with the *user harm* and the Mission; cite law as additional exposure. Do **not**
give definitive legal advice — flag the regime, recommend qualified counsel for anything shipping.

---

*Companion to `doctrine/references/interaction-anti-patterns.md` (the usability half) and
`doctrine/design-doctrine.md` (the Mission). Family taxonomy after Brignull (deceptivepatterns.org)
and Mathur et al. 2019; legal summary current to 2026 and intentionally high-level.*
