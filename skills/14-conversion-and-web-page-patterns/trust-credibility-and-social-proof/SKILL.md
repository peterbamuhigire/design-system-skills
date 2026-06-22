---
name: trust-credibility-and-social-proof
description: Use when designing the trust / proof / credibility section of a page in isolation — testimonials and reviews, customer logo strips, ratings and aggregate-usage numbers, security/privacy cues (SOC 2, ISO 27001, encryption, GDPR), trust badges, founder/team credibility, guarantees, certifications, press/awards, and case-study proof. Covers authentic, ATTRIBUTED proof (name + role + company + face), the credibility hierarchy (what to lead with when proof is strong vs thin), the trust-signal catalog, and where each signal earns its placement. Honest persuasion only — forbids fabricated testimonials, borrowed logos, invented "★★★★★ — anonymous," fake review counts, and any fake scarcity/urgency. Pairs with landing-page-and-conversion-design (which composes this section into the whole page) and design-ethics-and-anti-dark-patterns.
status: active
metadata:
  portable: true
  category: 14-conversion-and-web-page-patterns
  compatible_with:
    - claude-code
    - codex
---

# Trust, Credibility & Social Proof
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

> Proof only works when it is believed. Fabricated or anonymous proof, once suspected, drives trust
> *below* having no proof at all. This skill designs the trust/proof section as an **authored,
> honest** instrument: real people named and attributed, security and privacy cues that are true,
> a credibility hierarchy that leads with the strongest *real* signal you have, and not a single
> manufactured one. Per `doctrine/design-doctrine.md` §0, the moat is looking *authored and
> trustworthy by skilled human hands* — a faked trust badge reads as exactly the opposite the
> moment it is noticed, and it is noticed.

<!-- dual-compat-start -->
## Use When

- You are designing the **trust / social-proof / credibility section in isolation** — the
  testimonials block, the customer logo strip, the ratings/usage row, the security-and-privacy cues,
  the certifications/press/awards strip, or a case-study proof panel.
- A page **converts poorly because the visitor doesn't believe the claim** — the value prop is clear
  but there is a **credibility gap**, and you need to choose and arrange the right proof to close it.
- You have **real proof to deploy** (named testimonials, true metrics, genuine logos, real
  certifications) and need the credibility hierarchy: what to lead with, what to subordinate, where
  each signal earns placement.
- Proof is **genuinely thin** (a new product) and you need the honest substitutes — founder
  credibility, transparent methodology, a real guarantee — instead of fabricating proof.
- Someone is reaching for a **fake review count, a borrowed logo, an anonymous "★★★★★", a "trusted by
  millions" with no source, or "10,000+ users" you can't back** — STOP and use the authenticity rules
  here.

## Do Not Use When

- You are building the **whole landing/marketing page** (hero, value prop, mechanism, objections,
  CTA hierarchy) — use `14-conversion-and-web-page-patterns/landing-page-and-conversion-design`. That skill
  *composes* this proof section into the page spine; this skill details the proof section itself.
- The task is the **ethics gate / dark-pattern audit across the whole experience** (fake scarcity,
  confirmshaming, forced continuity, roach-motel) — use
  `00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns`. This skill stays within the
  proof section and defers the cross-cutting ethics catalog there; it only forbids the proof-specific
  dark patterns (fabricated/anonymous proof, fake counts, fake scarcity).
- You only need the **wording** of a testimonial pull-quote or a badge label — use
  `10-content-design-and-ux-writing/ux-writing-and-microcopy`, then return here for selection and
  placement.
- The proof is a **data exhibit / KPI dashboard** (charts of real metrics) — use
  `12-data-viz-and-dashboards`. This skill handles proof *as persuasion in a marketing context*,
  not analytical dashboards.

## Required Inputs

- **The credibility gap.** The specific doubt this section must answer: *"is it real?"*, *"is it for
  someone like me?"*, *"is it safe with my data?"*, *"will it actually deliver?"* Different doubts
  need different signals — name the doubt before choosing the proof.
- **The real proof inventory you are allowed to use.** A list of what genuinely exists *and is
  cleared*: which customers will be named, which quotes are real and attributed, which metrics are
  defensible and internally sourced, which certifications are actually held, which logos belong to
  *paying* customers. If a logo isn't a real customer or a metric can't be backed, it is **out**.
- **Who the visitor is.** Proof from someone *like the visitor* (same role, sector, size)
  out-converts a famous-but-irrelevant name. You cannot match the proof without knowing the audience.
- **The privacy/security posture** when relevant — what certifications, encryption, data-residency,
  and compliance facts are *true and current* (not aspirational), so security cues are honest.

## Workflow

### 0. Name the doubt, then pick the proof type that answers it
Map the credibility gap (above) to the signal class in `references/trust-signal-catalog.md`. *"Is it
real / do others use it?"* → social proof (testimonials, logos, usage numbers). *"Is it for someone
like me?"* → matched testimonials + named case studies. *"Is my data safe?"* → security/privacy cues.
*"Will it deliver?"* → guarantees, results metrics, certifications. Don't spray every badge — deploy
the signal that answers *this* visitor's *actual* doubt.

### 1. Build the credibility hierarchy — lead with your strongest REAL signal
Order proof by persuasive weight *for this audience*, strongest first (full ranking in
`references/trust-signal-catalog.md` §Credibility hierarchy):

1. **A named, attributed testimonial from someone like the visitor**, with a result — the single
   strongest signal. Name + role + company + (face when permitted) + a concrete outcome.
2. **A real, defensible aggregate number** — "2,400 finance teams", "average close time fell 9.1 →
   2.4 days" — stated precisely and internally sourced.
3. **Genuine customer logos** (only paying customers) and **third-party ratings** (real G2/Capterra
   score with the real review count linked).
4. **Security/privacy cues** when data-safety is the doubt — true certifications (SOC 2 Type II,
   ISO 27001), encryption-in-transit/at-rest facts, GDPR posture, each linking to evidence.
5. **Founder/team credibility, press, awards, certifications** — supporting, not leading, unless the
   audience buys on authority (regulated sectors, high-consideration B2B).

Lead with #1 if you have it; fall back down the list to the strongest signal you can *honestly*
field. Never promote a fabricated signal up the hierarchy to fill a gap.

### 2. Make every testimonial authentic and attributed (the non-negotiable)
Per `references/trust-signal-catalog.md` §Authenticity and the engine ethics posture:

- **Attribution is mandatory** — name + role + company, a face where the person consented. An
  anonymous "★★★★★ — A happy customer" reads as invented and *lowers* trust below no testimonial.
- **Never fabricate** a testimonial, a rating, a logo, a review count, or a metric. Using the logo of
  a company that is not a customer is dishonest and legally exposed (passing-off / false
  endorsement).
- **Real numbers, stated precisely**, internally sourced and defensible. "Reduced support tickets
  34%" beats "dramatically reduced tickets" — and you must be able to back it.
- **Disclose paid/affiliate relationships** (FTC and equivalents). Plain disclosure *increases*
  credibility; hidden sponsorship destroys it.
- **Show, don't just claim** where possible — a real screenshot, a named case study with numbers, a
  verifiable rating link beats an adjective.

### 3. Make security & privacy cues honest and verifiable
A trust badge that doesn't link to evidence is decoration, and a badge for a certification you don't
hold is fraud. Per `references/trust-signal-catalog.md` §Security & privacy:

- Show **only true, current** certifications/compliance (SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR) —
  each **linking to evidence** (the report request, the certificate, the policy), not a static image.
- State concrete data facts where they reassure: encryption in transit and at rest, data residency,
  the cancellation/data-deletion path. Vague "bank-level security" with nothing behind it is the
  security-cue equivalent of an anonymous testimonial.
- Place security cues **where the doubt arises** — next to the form, the payment step, the data-import
  CTA — not buried in a footer if the data fear is the conversion blocker.

### 4. When proof is genuinely thin — honest substitutes, never fabrication
A new product has no testimonials yet. The honest moves (full list in
`references/trust-signal-catalog.md` §Thin-proof):

- Lead with **founder/team credibility** (real bio, real track record) and **transparent methodology**
  ("here is exactly how it works").
- Offer a **real, strong guarantee** or a genuine free tier — honest risk reversal substitutes for
  proof you don't have.
- Use **real early-stage framing** if true — "join the first 100", "early access" — which is honest
  and can itself be attractive.
- **Never** invent a testimonial, borrow a logo, or post a fake review count to fill the gap. The
  honest thin-proof section out-converts the padded one that gets caught.

### 5. Hold accessibility and performance — proof is content, not decoration
- **Accessibility (`doctrine/references/wcag-2.2-criteria.md`):** testimonial faces need real `alt`
  text (or `alt=""` if purely decorative and the name is in text); a star rating must not be
  colour-only — pair it with the numeric value and a text label (SC 1.4.1); badge contrast meets the
  UI-component floor (3:1); any "verified review" link is a real focusable control with a visible
  focus ring. Don't lock proof behind hover (interaction-anti-patterns E3).
- **Performance (`doctrine/references/web-performance-budgets-2026.md`):** logo strips and headshots
  are image weight — serve sized, compressed AVIF/WebP with width/height set to reserve space (protect
  CLS); lazy-load below-the-fold proof; don't pull a heavy third-party review widget that tanks INP.

### 6. Distinctiveness — the proof section is a slop magnet too
Run `04-web-and-ui-design/distinctive-by-design` thinking here as well: the convergent default is a
centred "Loved by teams everywhere" heading over a grey logo strip and three identical quote cards
with round avatars. Authored proof looks specific — real faces, a quoted result pulled large, an
asymmetric layout, the brand's own type carrying the pull-quote. Avoid the templated three-equal-card
testimonial row as a reflex (per `doctrine/references/interaction-anti-patterns.md` D1 flat hierarchy:
the *result* in the quote should be the largest thing, not the avatar).

### 7. Specify, then build
Produce a proof-section spec (see `examples/credibility-section-spec.md`): the named doubt, the
chosen signals in hierarchy order, the real attributed content for each, the placement, the
accessibility/perf treatment, and the authenticity checklist completed.

## Authenticity & Trust Checklist (run before building)

1. **The doubt is named** and each signal chosen answers it (no badge-spray).
2. **Credibility hierarchy** leads with the strongest *real* signal; nothing fabricated is promoted up.
3. **Every testimonial is attributed** — name + role + company (+ face with consent); zero anonymous
   "★★★★★".
4. **Zero fabrication** — no invented quotes, no borrowed/non-customer logos, no fake review counts,
   no unbackable metrics, no "trusted by millions" without a source.
5. **All numbers are precise and internally defensible** — and you can produce the source.
6. **Security/privacy cues are true, current, and link to evidence**; placed where the doubt arises.
7. **Paid/affiliate relationships disclosed** (FTC and equivalents).
8. **No fake scarcity/urgency** anywhere in the proof section ("only 2 left", "3 viewing now",
   resetting countdowns) — defers to `design-ethics-and-anti-dark-patterns`; never fabricated here.
9. **Accessibility** — ratings not colour-only, faces have correct alt, badges meet 3:1, links
   focusable, proof not hover-locked.
10. **Performance** — proof images sized/compressed/CLS-reserved; no INP-tanking review widget.
11. **No convergent default** — not a centred grey logo strip + three identical avatar cards by reflex.

If any item can't be satisfied (proof is thin, a stakeholder wants a borrowed logo or a fake count),
**say so and ask** — never quietly ship fabricated or anonymous proof.

## Anti-Patterns

- **Anonymous testimonials** — "★★★★★ — A happy customer", a quote with no name/role/company. Reads
  as invented; lowers trust below no testimonial.
- **Borrowed / non-customer logos** — a logo strip of companies that don't actually use the product.
  Dishonest and legally exposed.
- **Fabricated or unbackable numbers** — "trusted by millions", "10,000+ users", "★★★★★ (4,212
  reviews)" you can't source. One challenged number poisons every other claim on the page.
- **Decorative trust badges** — a SOC 2 / "secure" image that links nowhere, or a badge for a
  certification not actually held. Decoration at best, fraud at worst.
- **Fake scarcity/urgency masquerading as social proof** — "3 people are viewing this", "only 2 left"
  that resets on reload, a countdown that restarts each visit. Banned; route honest equivalents via
  `design-ethics-and-anti-dark-patterns`.
- **Avatar bigger than the result** — the round headshot is the largest element and the actual
  outcome is tiny caption text (flat-hierarchy failure, interaction-anti-patterns D1).
- **Badge-spray** — every certification and award dumped indiscriminately, answering no specific
  doubt and reading as insecure over-justification.
- **Security cues buried in the footer** when data-safety is the actual conversion blocker — place
  the cue where the fear arises (the form, the import step).
- **The convergent template** — centred "Loved by teams everywhere" + grey logo strip + three equal
  avatar cards. The reflexive proof section; the Mission targets it.

## Outputs

- A **named credibility gap** and the **proof signals chosen to close it**, in hierarchy order.
- A **proof-section spec** (per signal: the real attributed content, placement, type/space treatment,
  the accessibility and performance treatment) in the shape of `examples/credibility-section-spec.md`.
- A **completed authenticity & trust checklist** confirming every signal is real and attributed, with
  zero fabricated, anonymous, or fake-scarcity proof.

## Examples

- `examples/credibility-section-spec.md` — a full, real proof-section spec for a sample product
  (a small-clinic patient-records SaaS), showing the named doubt, the credibility hierarchy applied,
  real attributed testimonials, honest security/privacy cues placed at the point of fear, the
  thin-proof fallback discussion, and the WCAG/perf constraints — with the authenticity checklist
  completed.

## References

- `references/trust-signal-catalog.md` — the full catalog of trust signals (social proof, security &
  privacy cues, authority/credentials, guarantees, transparency), the credibility hierarchy (what to
  lead with), the authenticity rules, the thin-proof substitutes, and the placement guidance.
- `doctrine/design-doctrine.md` — the Mission (§0, "the moat is looking human-made and trustworthy"):
  fabricated proof reads as the opposite of authored the moment it is caught.
- `doctrine/references/interaction-anti-patterns.md` — D1 flat hierarchy (the result, not the avatar,
  is the focal element), D3 colour-only signalling (ratings), E3 hover-dependency (don't hover-lock
  proof).
- `doctrine/references/wcag-2.2-criteria.md` — non-colour rating state, image alt, focusable
  verified-review links, badge contrast.
- `doctrine/references/web-performance-budgets-2026.md` — proof images sized/compressed/CLS-reserved;
  avoid INP-tanking third-party review widgets.
- Sibling skills: `14-conversion-and-web-page-patterns/landing-page-and-conversion-design` (composes this proof
  section into the whole page; defers the testimonial/security-cue detail here),
  `00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns` (the cross-cutting dark-pattern
  catalog — no fake scarcity/urgency; this skill defers there and forbids only proof-specific fakery),
  `04-web-and-ui-design/distinctive-by-design` (the proof section is a slop magnet too),
  `10-content-design-and-ux-writing/ux-writing-and-microcopy` (testimonial pull-quote and badge
  wording).
<!-- dual-compat-end -->
