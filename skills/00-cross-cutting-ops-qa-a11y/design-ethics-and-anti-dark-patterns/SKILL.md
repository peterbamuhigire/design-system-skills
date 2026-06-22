---
name: design-ethics-and-anti-dark-patterns
description: Use when you need the cross-cutting ethics gate for an interface — the deceptive-pattern (dark-pattern) catalogue and the honest-design guardrails that apply to ANY flow, not one surface. Covers the named pattern families — sneaking (sneak-into-basket, hidden costs / drip pricing), urgency (fake scarcity, resetting countdowns), misdirection / confirmshaming, forced action (forced continuity, roach motel), nagging, and obstruction — each with its honest swap; plus consent UX, default ethics, the "would you be comfortable if the user saw this?" test, and a light note on the legal angle (GDPR consent, CCPA, the EU/UK/US deceptive-pattern rules and FTC). Use it to audit a flow for dark patterns, to choose the honest alternative when a stakeholder reaches for a coercive one, or as the ethics reference the conversion skills defer to. Pairs with ecommerce-and-checkout-ux and trust-credibility-and-social-proof, which name this as the ethics catalog; for a full scored product review use product-design-audit.
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
    - claude-code
    - codex
---

# Design Ethics & Anti-Dark-Patterns
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

> A dark pattern (the regulators now say "deceptive pattern") is an interface built to make the user
> do something they would not have chosen with full information and a clear head. It is the exact
> inverse of the doctrine's Mission: where authored design is the signature of a skilled human acting
> *for* the user, a dark pattern is design turned *against* them. It works once and is then resented —
> and increasingly it is illegal. This skill is the cross-cutting ethics gate: the catalogue of the
> coercive patterns, the honest swap for each, and the consent/default rules that keep a flow on the
> right side of the line. Every conversion skill in the engine defers here.

<!-- dual-compat-start -->
## Use When

- You are running the **ethics / dark-pattern pass over a whole flow or product** — onboarding,
  sign-up, checkout, cancellation, a permissions/consent dialog, a paywall — and need the named
  pattern families to detect against and the honest alternative for each.
- A stakeholder (or your own instinct) is **reaching for a coercive lever** — a resetting countdown,
  a pre-ticked add-on, a "are you sure you want to miss out?" decline button, a cancel flow designed
  to be hard — and you need to **refuse it and offer the honest equivalent** that still converts.
- You are designing **consent UX, defaults, or an opt-in/opt-out** and need the rule for what an
  ethical default and a genuine (freely-given, specific, informed, unambiguous) consent looks like.
- A conversion/retail/trust skill has **deferred its cross-cutting ethics question here** (e.g.
  `ecommerce-and-checkout-ux`, `trust-credibility-and-social-proof`) and you need the general
  catalogue rather than the surface-specific rule.
- You want the **"would you be comfortable if the user saw this?" test** applied to a design decision,
  with the light legal-exposure note (GDPR, CCPA/CPRA, EU/UK consumer law, FTC) attached.

## Do Not Use When

- You are designing the **specific retail buying journey** (PLP → PDP → cart → checkout → payment →
  post-purchase) — use `06-sector-and-domain-ux/ecommerce-and-checkout-ux`. That skill *applies* this
  catalogue to the retail surfaces (sneak-into-basket, drip pricing, forced continuity in a cart);
  this one is the general doctrine it defers to.
- You are designing the **trust / social-proof section** and the question is fabricated vs. authentic
  proof — use `14-conversion-and-web-page-patterns/trust-credibility-and-social-proof`. It forbids proof-specific
  fakery (anonymous "★★★★★", borrowed logos, fake review counts) and defers the cross-cutting scarcity
  rule here.
- You need a **full scored, skill-routed product audit** across surfaces and platforms — use
  `00-cross-cutting-ops-qa-a11y/product-design-audit`; it runs this ethics lens as one dimension.
- The behavioural detection you need is a **usability anti-pattern, not an ethics one** (mystery-meat
  nav, idiot-box modals, dead ends) — that is `doctrine/references/interaction-anti-patterns.md`
  directly. Some entries overlap (B1 Forced Sign-Up, C4 Trap); this skill adds the *intent-to-deceive*
  framing and the honest swap.

## Required Inputs

- **The flow and its goal, stated honestly.** What is the business outcome (a sale, a sign-up, a
  retained subscriber) *and* what is the user actually trying to do? A dark pattern is exactly the gap
  between those two being closed by coercion instead of value. Name both.
- **The decisions the user makes in the flow** — every opt-in, default, consent, charge, and exit.
  Each is a place a dark pattern can hide; you cannot audit what you have not enumerated.
- **The real facts behind any urgency, scarcity, price, or social signal** — is the stock count true
  and live? Is the deadline genuine? Is the "47 people viewing" measured or invented? Honesty is
  judged against the facts, so the facts are an input.
- **The cancellation / opt-out / data-deletion path** — symmetric exit is the single most-tested
  guardrail (and the most-regulated). If you cannot describe how the user *leaves*, that is the first
  finding.

## The deceptive-pattern families (detect → why-harmful → honest swap)

Full catalogue, with the regulator names and legal angle, in `references/dark-pattern-catalog.md`.
The seven families to walk a flow against:

1. **Sneaking** — slipping something past the user. *Sneak-into-basket* (an item/warranty/sample
   added unasked), *hidden costs / drip pricing* (fees, tax, shipping sprung only at the final step),
   *hidden subscription* (a one-off purchase that is quietly recurring). **Honest swap:** the basket
   holds only what was explicitly chosen; the **all-in total is shown before the commit point**;
   recurring terms are stated at opt-in. (Ref `interaction-anti-patterns.md`; doctrine "Hidden costs".)
2. **Urgency** — manufacturing time pressure. *Fake scarcity* ("only 2 left" that resets on reload),
   *fake / resetting countdowns*, invented "high demand." **Honest swap:** show urgency **only when it
   is true and live** — real stock, a real deadline. Real scarcity is a legitimate, helpful signal;
   invented scarcity is the banned one.
3. **Misdirection** — steering the eye/instinct away from the user's interest. *Confirmshaming* (a
   decline worded to shame: "No thanks, I like paying full price"), *visual interference* (the wanted
   choice de-emphasised, the upsell styled as the only button), *trick wording / double negatives*.
   **Honest swap:** the user's likely choice is **at least as easy and prominent** as the business's
   preferred one; decline copy is **neutral** ("No thanks"); no double negatives. (Ref B3, D6.)
4. **Forced action** — demanding something unrelated to proceed. *Forced continuity* (a free trial
   that auto-charges with a buried cancel), *roach motel* (easy in, deliberately hard out), *forced
   sign-up* (a registration wall before any value). **Honest swap:** **symmetric exit** — cancel is as
   easy as sign-up; trials announce the charge up front and remind before billing; value before auth,
   guest mode offered. (Ref B1, C4; doctrine "Forced continuity / Roach motel".)
5. **Nagging** — repeated, persistent interruption to wear the user down. The notification that
   re-asks every session, the "rate us" that won't take no, the cookie banner that re-prompts.
   **Honest swap:** ask **once**, honour the answer, make "no" stick; an interval before any re-ask,
   and a real "don't ask again."
6. **Obstruction** — making a path artificially hard to discourage it. A cancel buried behind a phone
   call, a maze of confirmations to delete an account, comparison/price info hidden. **Honest swap:**
   the friction to leave/decline/delete is **no greater** than the friction to join/accept/buy.
7. **Social-proof & interface deception** — *disguised ads* (sponsored styled as organic), *fake
   activity/testimonials*, *bait-and-switch*. **Honest swap:** label sponsored content; use only real,
   attributed proof (defer to `trust-credibility-and-social-proof`); the control does exactly and only
   what its label says.

## Workflow

1. **State the flow's honest goal and enumerate the user's decision points.** Write the business
   outcome and the user's actual job side by side; list every opt-in, default, consent, charge, and
   exit in the flow (Required Inputs). This is the surface the audit walks.
2. **Walk each decision point against the seven families.** For every opt-in/default/charge/exit, ask
   which family could hide there and check the facts (`references/dark-pattern-catalog.md`). Any match
   is a finding: record the pattern name, where it sits, the user harm, and the legal exposure.
3. **Apply the consent & default rules.** Every default must be the one an informed user would
   *choose*, not the one that maximises revenue by inertia. Consent must be **freely given, specific,
   informed, unambiguous, and as easy to withdraw as to give** (the GDPR test, which is also just good
   design). Pre-ticked boxes are never valid consent. See `references/dark-pattern-catalog.md` §Consent.
4. **Apply the comfort test to anything ambiguous.** For each questionable choice, ask: *"Would I be
   comfortable if the user could see exactly why this was designed this way — would I explain it to
   their face?"* If the honest explanation is "to trick you into not noticing / not leaving," it is a
   dark pattern. Reframe it as the honest swap.
5. **Swap every finding for its honest equivalent.** Replace each detected pattern with the swap from
   the catalogue (transparency, symmetric exit, neutral decline copy, true scarcity, opt-in defaults).
   The honest version is the deliverable — never ship the coercive one and "flag it."
6. **Attach the legal note where relevant — lightly.** Where a finding maps to a named rule (GDPR
   consent / dark-pattern guidance, CCPA/CPRA opt-out and the "symmetry" rule, the EU Digital Services
   Act and UCPD, UK CMA/DMCCA, FTC "click-to-cancel" / negative-option), note it as *additional*
   exposure, not the primary reason — the primary reason is that it is wrong. See the catalogue's
   §Legal angle. Do not give definitive legal advice; flag and recommend counsel for live launches.
7. **Produce the ethics audit.** Write the findings → honest-redesign report (shape:
   `examples/ethics-audit-worked.md`): each pattern found, its family, evidence, harm, legal note, and
   the honest swap, ending with the consent/default verdict and the comfort-test summary.

## Anti-Patterns

- **Shipping the coercive version with a comment.** Detecting a dark pattern and leaving it in "because
  the team wants the numbers" — the swap *is* the job. If a stakeholder insists, refuse and state the
  honest alternative that still converts.
- **"Asymmetry of effort" in disguise.** A flow where joining is one tap and leaving is ten — even if
  no single screen is egregious, the *asymmetry itself* is the obstruction/roach-motel pattern.
- **Treating real scarcity as banned.** True, live "only 2 left" or a genuine sale deadline is honest
  and helpful — the ban is on the *invented* and *resetting* kind. Don't strip truthful urgency.
- **Consent theatre.** A cookie/permission dialog where "Accept all" is one button and "reject" is
  buried three clicks deep — that is misdirection + obstruction, not consent, regardless of the legal
  box it appears to tick.
- **Confusing this with the usability checklist.** `interaction-anti-patterns.md` detects *incompetent*
  UX; this detects *deceptive* UX (intent to mislead). Route accordingly; some entries pair.
- **Citing the law as the only reason.** "We can't because GDPR" trains teams to do the minimum legal.
  Lead with the user harm and the Mission; the legal note is reinforcement, not the argument.

## Outputs

- An **ethics / dark-pattern audit** of the flow: every detected pattern by family, with location,
  evidence, user harm, the light legal note, and the **honest swap** — in the shape of
  `examples/ethics-audit-worked.md`.
- A **consent & default verdict** confirming every default is the informed-user choice and every
  consent is freely-given/specific/informed/unambiguous/withdrawable.
- A **completed comfort-test summary** — the questionable decisions, each resolved to its honest form.

## Examples

- `examples/ethics-audit-worked.md` — a fully worked ethics audit of a real-ish flow (the sign-up →
  trial → cancellation journey of a habit-tracking SaaS, "Streaky"), finding the dark patterns across
  all seven families (drip-priced "pro" fee, pre-ticked annual-plan upsell, confirmshaming decline,
  forced-continuity trial with a roach-motel cancel, nagging notification opt-in, a disguised
  "recommended" ad), then the honest redesign of each, the consent/default verdict, the comfort-test
  pass, and the light legal note (GDPR consent, FTC click-to-cancel, EU UCPD). Concrete, no lorem.

## References

- `references/dark-pattern-catalog.md` — the full catalogue: each deceptive pattern (by the seven
  families) → why it harms the user → its honest swap, plus the consent-UX rules, the default-ethics
  rule, the "would you be comfortable if the user saw this?" test, and the §Legal angle (GDPR, CCPA/
  CPRA, EU DSA/UCPD, UK CMA/DMCCA, FTC negative-option) kept deliberately light.
- `doctrine/design-doctrine.md` — the Mission (§0): authored design acts *for* the user; a dark
  pattern is design turned against them and reads as exactly that once noticed.
- `doctrine/references/interaction-anti-patterns.md` — the behavioural detection checklist this skill
  shares a border with: **B1 Forced Sign-Up**, **B3 Vague/competing CTAs**, **C3 Dead End**, **C4 Trap
  / Forced Action**, **D6 Oceans of Buttons** — the usability half; this skill adds the intent-to-
  deceive half and the honest swap.
- Sibling skills: `06-sector-and-domain-ux/ecommerce-and-checkout-ux` and
  `14-conversion-and-web-page-patterns/trust-credibility-and-social-proof` (both **pair** with this skill and name it
  as the cross-cutting ethics catalog they defer to); `00-cross-cutting-ops-qa-a11y/product-design-audit`
  (runs this ethics lens as one scored dimension of a full product review).
<!-- dual-compat-end -->
