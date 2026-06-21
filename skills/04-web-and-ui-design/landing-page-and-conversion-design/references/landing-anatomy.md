# Landing Page Anatomy

The section spine of a converting landing page, what each section must answer, and the placement
rules. Conversion is a *sequence of answered questions* — the order is load-bearing. Reorder only
with a stated reason.

> This is structure, not styling. The look is governed by `distinctive-by-design` and
> `doctrine/design-doctrine.md` — never the convergent SaaS template (Inter + indigo gradient +
> centred hero + three-feature-icon row).

---

## The question sequence

A first-time visitor arrives with questions, asked in a near-fixed order. Each section exists to
answer the next one. Skip an answer and the visitor stalls there.

| # | Section | The visitor's question | What it must contain |
|---|---|---|---|
| 1 | **Hero** | "What is this and is it for me?" | Value-prop headline, supporting subhead, primary CTA, one credibility anchor |
| 2 | **Value / outcome** | "What do I actually get?" | The concrete transformation, framed as *their* outcome |
| 3 | **Mechanism / how it works** | "How does it work — is the promise believable?" | Enough of the *how* to make the claim credible; 2–4 steps |
| 4 | **Social proof** | "Do people like me trust this?" | Attributed testimonials, real logos, ratings, case numbers |
| 5 | **Objection handling** | "What's the catch / why might this not work for me?" | The top 2–3 real objections answered (price, effort, risk, lock-in) |
| 6 | **Closing CTA** | "Okay — how do I start?" | Restated value + the same primary action |

Short or warm-traffic pages may collapse 2–3 or 4–5, but the *logic* (claim → outcome →
believability → proof → objections → ask) must still run in order.

---

## 1. The hero (the most important screen on the page)

The hero must do four things in roughly one viewport:

- **Headline = the value proposition**, not a brand tagline. State the concrete outcome for *this*
  visitor in their words. "Close the books in 2 days, not 9" beats "The modern finance platform."
- **Message match.** The headline echoes the promise of whatever brought the visitor here (the ad
  creative, the email subject, the search query). A mismatch here is the single largest conversion
  leak — the visitor feels they clicked the wrong thing and bounces.
- **One primary CTA**, value-stating, the brightest element in the viewport.
- **One credibility anchor** — a real proof token visible above the fold: a named-logo strip, a
  rating with a count, a true usage number ("2,400 finance teams"). Borrow trust before you ask.

**Above-the-fold budget.** Do not crowd the hero with everything. One headline, one subhead, one
CTA, one proof token, and (optionally) one authored product image. The hero's job is to earn the
*scroll*, not close the deal.

**Cold vs warm traffic changes the hero:**
- **Cold** (visitor doesn't know you): the headline carries more explanation; the proof anchor
  matters more; expect a longer page.
- **Warm** (clicked an ad they already understood): the headline can be more direct/aspirational;
  the page can be shorter; the CTA can come faster.

---

## 2–3. Value and mechanism

- **Lead with outcome, support with feature.** Every feature is phrased "X *so that* you can Y."
  A feature wall with no "so that" is a spec sheet, not a value proposition.
- **Mechanism builds belief.** A 2–4 step "how it works" makes a bold promise believable. It is not
  documentation — it is just enough to remove "this sounds too good / too vague."

---

## 4–5. Proof and objections (composed from `trust-credibility-and-social-proof`)

- **Proof** answers "people like me trust this." Pull the testimonial/logo/rating/security-cue
  treatment from `trust-credibility-and-social-proof` (P1). This skill places it; that one details
  it. All proof must be real and attributable (see `conversion-credibility.md`).
- **Objection handling** is where conversions are won late. List the *real* top 2–3 reasons this
  specific visitor hesitates and answer them plainly — price, switching effort, risk, lock-in,
  security. A short honest FAQ or a fair comparison table. Pre-empting the objection beats letting
  it end the visit silently.

---

## CTA placement rules

- **Identical, repeated primary CTA.** Same label, weight, and colour role at the hero, after proof,
  and at the close. Repetition without variation — the visitor learns one button.
- **Frequency by page length.** Short page: hero + close. Long page: hero + after proof + close,
  optionally a sticky CTA on scroll once the hero CTA leaves the viewport.
- **One focal point per screen.** In any given viewport the primary CTA is the brightest,
  highest-contrast element. Secondary actions are text links, never co-equal buttons.
- **Minimise the ask at the CTA.** Fewest fields the conversion truly needs; defer the rest to after
  the click (`onboarding-and-first-run-design`).

---

## Page-length decision

There is no universal right length — length follows the *decision weight* and traffic temperature:

- **High-consideration / cold / expensive / risky** → longer page: more proof, more mechanism, more
  objection handling. The visitor needs to be convinced.
- **Low-consideration / warm / cheap / low-risk** → shorter page: get to the CTA fast; too much
  page introduces doubt and friction.

Make the call explicitly and state it; don't default to "long because that's what the template had."

---

## Accessibility & performance are part of the anatomy

- The **hero is the LCP element** (`doctrine/references/web-performance-budgets-2026.md`) — keep it
  light, reserve space for its media to protect CLS. A slow first screen is abandoned before the
  value prop is read.
- The **CTA is a real focusable control** with a visible focus ring, ≥24×24px target (SC 2.5.8),
  sufficient contrast, never colour-only (`doctrine/references/wcag-2.2-criteria.md`). An
  inaccessible CTA is an un-clickable CTA — a direct conversion loss.

---

## Sources / authority

Structure and composition trace to human design and conversion literature — not to an AI tool's
suggestion (`doctrine/design-doctrine.md` §2 asymmetry rule). The question-sequence logic reflects
long-standing direct-response and information-scent practice; the *look* is governed by the engine's
typography and composition references (`pairing-principles.md`, `type-scale-and-spacing.md`).
