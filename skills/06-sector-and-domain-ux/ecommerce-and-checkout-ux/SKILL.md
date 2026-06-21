---
name: ecommerce-and-checkout-ux
description: Use when designing, building, reviewing, or rescuing a retail/e-commerce buying journey — product-listing pages (PLP), product-detail pages (PDP), the cart/basket, the checkout flow (guest-first, minimal fields), payment and address entry, and the post-purchase trust surface (returns, refunds, order status). Covers conversion-grade retail UX done HONESTLY: guest checkout before account creation, total-cost transparency before the pay button, real stock/scarcity, and a symmetric cancel/return path. Strictly anti-dark-pattern — forbids sneak-into-cart, hidden costs, drip pricing, pre-checked add-ons/insurance, forced account creation, forced continuity/subscription traps, fake scarcity and confirmshaming. Run distinctive-by-design first; use form-ux-design for field anatomy; pair with design-ethics-and-anti-dark-patterns and landing-page-and-conversion-design.
status: active
metadata:
  portable: true
  category: 06-sector-and-domain-ux
  compatible_with:
    - claude-code
    - codex
---

# E-commerce & Checkout UX
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

> A store has one job: let a specific shopper find the right thing, believe it's the right thing,
> and pay for it with zero friction and zero trickery — then trust you enough to come back. This
> skill gives the surface-by-surface architecture (PLP → PDP → cart → checkout → payment →
> post-purchase) and the conversion craft that converts *because the path is clear and the price is
> honest*, never because the shopper was rushed, confused, or opted-in without consent. The
> doctrine's Mission applies in full: a store that opens in Inter on a generic grid of identical
> cards tells the shopper no one authored it — and a hidden £4.99 "service fee" at step four tells
> them no one respects them. Both lose the sale and the repeat custom.

<!-- dual-compat-start -->
## Use When

- You are building or rebuilding any part of a **retail buying journey**: a category/search
  **PLP**, a **PDP**, the **cart/basket**, the **checkout flow**, **payment/address** entry, or the
  **post-purchase** surface (order confirmation, status, returns/refunds).
- A funnel **leaks** and you need to diagnose *where shoppers abandon* — usually the cart→checkout
  seam (surprise costs, forced sign-up) or the payment step (too many fields, no trust cues).
- You are asked to "lift conversion" and the instinct (yours or a stakeholder's) is reaching for a
  countdown timer, a pre-ticked insurance add-on, an auto-renewing "membership," or a free-shipping
  threshold that quietly slips an item into the basket — **STOP** and apply the anti-dark-pattern
  rules here instead.
- You need to specify **guest-first checkout**, total-cost transparency, address/payment field
  minimisation, or a returns/trust surface that earns the next purchase.

## Do Not Use When

- The task is a **marketing/landing page** ending at a single CTA, not a purchase flow — use
  `04-web-and-ui-design/landing-page-and-conversion-design`. That skill *ends* at the click; this
  one owns everything after it.
- The task is **generic form field anatomy, validation, or wizard mechanics** in isolation — use
  `04-web-and-ui-design/form-ux-design`. This skill *composes* those patterns into the retail
  context (it does not re-teach label placement or the five field states — it cites them).
- The task is the **ethics framework / dark-pattern taxonomy itself**, independent of retail — use
  `06-sector-and-domain-ux/design-ethics-and-anti-dark-patterns` (the paired skill). This skill
  applies that doctrine to the specific retail dark patterns; that one is the general catalog.
- The task is **only the button/error wording** — use
  `10-content-design-and-ux-writing/ux-writing-and-microcopy`, then return here for placement.

## Required Inputs

- **The catalog reality.** Roughly how many products, how they are categorised, what attributes
  matter for filtering (size, colour, price, brand), and whether variants exist (a shirt in S/M/L ×
  3 colours). You cannot design a PLP filter or a PDP variant picker for a catalog you haven't seen.
- **The true total cost structure.** Every component the shopper will pay: item price, tax/VAT
  (inclusive or added?), shipping tiers, any genuine fees. This is non-negotiable input — the
  honest-pricing rule below cannot be applied without it. If fees are "to be decided later," flag
  that the design will surface them early *by construction*.
- **The fulfilment and returns truth.** Real delivery options/times, the real returns window and
  process, who pays return postage. The trust surface must state what is actually true.
- **Payment methods and any account/identity constraint.** Which methods (card, wallet, BNPL,
  mobile-money), and whether anything *genuinely* requires an account (vs. wanting one for
  marketing — those are different, and only the first justifies gating).

## Workflow

### 0. Run the pre-flight, then commit the store's ONE distinctive idea
Run `04-web-and-ui-design/distinctive-by-design` first — it gates the build. A storefront is a
high-convergence surface: the reflexive output is Inter + a uniform grid of identical white cards +
a generic "Add to cart" + an indigo accent, indistinguishable from every template. Commit ONE
authored organising idea (a signature display face for product titles, an editorial PLP rhythm that
breaks the uniform grid, an authored photography POV, a distinctive but legible price treatment) per
`doctrine/design-doctrine.md` §0 and `pairing-principles.md`. State it before any markup. No banned
fonts; design around real product data, never lorem.

### 1. PLP — let them find and compare honestly (see `references/checkout-flow-patterns.md` §PLP)
- **Scent + scan.** Each card carries the load-bearing decision data: real product image, name,
  price (the *real* price, with any "was" price only if genuinely the prior price), rating, and key
  variant/availability signal. Don't bury price; don't fake a crossed-out "RRP."
- **Filters and sort that match the catalog**, not a generic set. Filters must reflect the
  shopper's real decision attributes; show active filters as removable chips; never reset their
  selection silently. Keep results honest — sponsored items, if any, are **labelled** (disguised
  ads are a dark pattern, ref `interaction-anti-patterns.md` and the doctrine).
- **No fake urgency on cards.** "Only 2 left" appears only when it is *true and live*. Real
  low-stock is a legitimate, helpful signal; an invented one that resets on reload is banned.

### 2. PDP — earn the "Add to cart" with truth (see `references/checkout-flow-patterns.md` §PDP)
- **The decision set above the fold:** real imagery (zoomable, multiple angles), name, honest price
  *with the all-in cost knowable* (tax-inclusive where the market expects it; shipping at least
  estimable), variant picker with **only in-stock combinations selectable** (or clearly marked
  out-of-stock — never let them pick a phantom), and a single clear primary action.
- **One primary action: Add to cart / Buy.** Secondary actions (wishlist, share) are visibly
  subordinate (ref `interaction-anti-patterns.md` B3 — one primary action per view). The "Add to
  cart" must do *exactly and only* what it says — it never silently adds a warranty, an add-on, a
  subscription, or a second item (sneak-into-cart, banned).
- **Believability content:** real specs, real delivery estimate, real returns terms, real reviews
  (with the genuine distribution, not only 5-stars). Answer *"is this the right thing and what
  happens if it's not?"* on the page, not after payment.

### 3. Cart — show the true running total, add nothing unasked (see `references/checkout-flow-patterns.md` §Cart)
- **Line items the shopper actually chose** — never a pre-added accessory, insurance, or "popular
  add-on" ticked by default (pre-checked opt-in + sneak-into-cart, both banned).
- **The running total is honest and complete-as-knowable:** subtotal, then tax and shipping shown
  or clearly estimated *here*, not sprung at the final step. If shipping needs a postcode, ask for
  it in the cart so the total isn't a surprise later (drip pricing / hidden costs, banned —
  `interaction-anti-patterns.md`, doctrine §"Hidden costs").
- **Free-shipping / threshold nudges are honest:** "£6 from free shipping" is fine; auto-adding a
  filler item to cross the threshold is theft-by-friction. Edit-quantity and remove must be obvious
  and reversible (a removed item is undoable — ref `interaction-anti-patterns.md` C3).

### 4. Checkout — guest-first, minimal fields (see `references/checkout-flow-patterns.md` §Checkout)
This is the conversion-critical seam. Apply `form-ux-design` for field mechanics; apply these
retail rules on top:

- **Guest checkout is offered first and given equal or greater visual weight than "Sign in / Create
  account."** A forced-registration wall before purchase is the single highest cart-abandon cause
  and a banned pattern (ref `interaction-anti-patterns.md` B1 "Forced Sign-Up", doctrine). Offer
  account creation *after* the order, as a one-tap "save these details" using data they already
  entered — never as a gate.
- **Minimum field set.** Ask only what fulfilment and payment truly need. Use `autocomplete`
  attributes, address lookup/autofill, correct input types and mobile keyboards, single-column,
  labels above (ref `form-ux-design` Rules 1–5; `interaction-anti-patterns.md` B2 Form Friction).
  Default billing = shipping with a single toggle to differ.
- **A real progress signal** on a multi-step checkout (or a single-page accordion), so the shopper
  knows how many steps remain. Inline, solution-bearing validation — never a late "card invalid"
  wipe.
- **No surprises before the pay button:** the final total (items + tax + shipping + any fee) is
  shown *in full* adjacent to the pay action, with the delivery date and the returns/cancellation
  terms one glance away.

### 5. Payment & address — trust at the moment of money (see `references/checkout-flow-patterns.md` §Payment)
- **Recognised payment methods up front** (wallets/express pay that skip address entry are a
  legitimate friction-cut — Apple/Google Pay, mobile-money where regional). Express pay must still
  show the full total before confirming.
- **Trust cues that are real:** the padlock/secure-checkout signal, recognised card/wallet marks,
  and a clear statement of what is charged and when. For any saved-card or wallet, the charge is
  exactly the displayed total — no padding.
- **Address entry minimised** via lookup; format and validate per locale; show errors inline next
  to the field. Card fields use the right input mode, auto-detect card type, and never block paste.

### 6. Subscriptions, warranties & add-ons — opt-IN, symmetric exit (see `references/checkout-flow-patterns.md` §Continuity)
- **Every recurring charge, warranty, insurance, or add-on is unchecked by default and the shopper
  opts in deliberately** (pre-checked = banned). State the renewal price, the cadence, and the
  cancel path *at the point of opt-in*.
- **Forced continuity is banned.** A "free trial" that auto-charges must say so plainly up front,
  remind before charging, and offer a cancel that is **as easy as the sign-up** (no roach motel —
  ref `interaction-anti-patterns.md` C4 Trap, doctrine "Forced continuity" / "Roach motel").

### 7. Post-purchase — returns, refunds, status, the trust that earns the next sale (see `references/checkout-flow-patterns.md` §Post-purchase)
- **Order confirmation** states what was bought, the all-in amount charged, the delivery estimate,
  and the returns window — no dead end (ref `interaction-anti-patterns.md` C3).
- **Returns/refunds are findable and symmetric:** initiating a return is no harder than buying was;
  the policy is stated in plain language *before* purchase, not hidden. A genuine, clearly-stated
  returns policy is one of the strongest *honest* conversion levers in retail.
- **Order status** is visible without a support ticket; status changes are communicated; refunds
  confirm timing in writing.

### 8. Specify, then build
Produce a surface-by-surface spec (see `examples/checkout-flow-spec-worked.md` for the shape): per
surface — purpose, the real content/fields, the type/space treatment, the one primary action, the
total-cost treatment, and the trust cue. Run the checklist below before any markup.

## Anti-Dark-Pattern Checklist (run before building — every item must pass)

1. **Guest checkout offered first**, equal-or-greater weight than account creation; no
   forced-registration wall before purchase (B1).
2. **Total cost shown in full before the pay button** — items + tax + shipping + every fee; nothing
   sprung at the final step (no drip pricing / hidden costs).
3. **Cart contains only what the shopper explicitly chose** — no sneak-into-cart, no auto-added
   filler to hit a free-shipping threshold.
4. **All add-ons, warranties, insurance, and subscriptions are unchecked by default** — opt-in only,
   with price/cadence/cancel stated at opt-in (no pre-checked opt-ins).
5. **Any recurring charge states terms up front, reminds before charging, and cancels as easily as
   it signs up** (no forced continuity, no roach motel).
6. **Scarcity/urgency is real and live** — true stock counts and genuine deadlines only; nothing
   resets on reload (no fake scarcity/urgency).
7. **Decline/opt-out wording is neutral** — "No thanks," not "No, I don't want to save money" (no
   confirmshaming).
8. **Sponsored/ad placements in PLP are labelled** — never disguised as organic results.
9. **Minimum field set**, autocomplete/address-lookup, single-column, labels above, inline
   validation; billing=shipping default (B2 form friction).
10. **One primary action per surface**; "Add to cart"/"Pay" does exactly and only what it says (B3).
11. **Returns/refund policy stated in plain language before purchase**, and initiating a return is
    no harder than buying (no dead end, symmetric exit).
12. **Checkout passes WCAG 2.2** — focusable controls, visible focus, ≥24×24px targets (SC 2.5.8),
    sufficient contrast, never colour-only for stock/error/required state.
13. **No convergent default** — type/colour/layout pass `distinctive-by-design` (no Inter + uniform
    white-card grid + indigo accent as a reflex).

If any item can't be satisfied (a stakeholder insists on a pre-checked add-on, fees can't be shown
early, "make cancel hard"), **refuse and offer the honest equivalent** — never quietly ship the
coercive version.

## Anti-Patterns

- **Forced account creation before checkout** — the highest-impact abandon driver; guest-first is
  non-negotiable (ref `interaction-anti-patterns.md` B1).
- **Drip pricing / hidden costs** — fees, tax, or shipping revealed only at the final step. Bait-
  and-switch; invites abandonment, chargebacks, and (in the EU/UK/US) regulatory action.
- **Sneak-into-cart** — items, warranties, or "samples" added without an explicit choice.
- **Pre-checked add-ons / insurance / opt-ins** — consent by inertia; banned regardless of revenue.
- **Forced continuity** — a "free trial" that auto-charges with a buried cancel (roach motel).
- **Fake scarcity / fake urgency** — invented "only 2 left" or countdowns that reset on reload.
- **Confirmshaming** the decline ("No thanks, I hate good deals").
- **A wall of equal-weight CTAs** on the PDP/cart — the buy action drowns (ref
  `interaction-anti-patterns.md` D6 / B3).
- **Too many fields, no autofill, late validation** at the payment step (ref B2).
- **The convergent storefront template** — Inter, a uniform grid of identical cards, generic
  "Add to cart," indigo accent. Looks unauthored; the Mission targets it.
- **A returns policy hidden until after purchase**, or a return process harder than the purchase
  was — a trust killer and a dead-end (C3).

## Outputs

- A **stated store/journey goal** and the committed distinctive idea (what + why + human authority),
  written before markup.
- A **surface-by-surface spec** (PLP → PDP → cart → checkout → payment → post-purchase): per surface
  the purpose, real content/fields, type/space treatment, single primary action, total-cost
  treatment, and trust cue — in the shape of `examples/checkout-flow-spec-worked.md`.
- A **completed Anti-Dark-Pattern Checklist** confirming guest-first, total-cost transparency, zero
  pre-checked/sneak/forced-continuity patterns, and a symmetric returns path.

## Examples

- `examples/checkout-flow-spec-worked.md` — a complete, build-ready surface-by-surface spec for a
  real store (a small specialty-coffee retailer): the PLP card and filters, the PDP variant picker
  and all-in price, the honest cart with early shipping, the guest-first single-page checkout with
  the minimum field set, the payment/trust step, the opt-in-only subscription, and the post-purchase
  returns surface — with the WCAG 2.2 and anti-dark-pattern constraints applied throughout.

## References

- `references/checkout-flow-patterns.md` — the surface-by-surface retail spine (PLP, PDP, cart,
  checkout, payment/address, continuity, post-purchase), the guest-first checkout pattern, the
  total-cost-transparency rule, the full retail dark-pattern catalog with honest swaps, and the
  field-minimisation rules. Cites `interaction-anti-patterns.md` and the doctrine throughout.
- `doctrine/design-doctrine.md` — the Mission (§0, "the moat is looking human-made and
  *trustworthy*"): conversion is downstream of an authored, honest store. The Anti-Slop Charter
  bans the convergent storefront template.
- `doctrine/references/interaction-anti-patterns.md` — the behavioural detection checklist this
  skill enforces: **B1 Forced Sign-Up**, **B2 Form Friction**, **B3 Vague/competing CTAs**, **C3
  Dead End / no recovery**, **C4 Trap / Forced Action**, **D6 Oceans of Buttons**.
- `doctrine/references/wcag-2.2-criteria.md` — checkout control focusability, target size (SC
  2.5.8), contrast, non-colour state for stock/error/required.
- `doctrine/references/web-performance-budgets-2026.md` — PLP/PDP imagery as LCP, CLS reservation
  for product media; a slow storefront is an abandoned one.
- Sibling skills: `04-web-and-ui-design/distinctive-by-design` (run first; gates the build),
  `04-web-and-ui-design/form-ux-design` (field anatomy, validation, the five field states — applied
  inside checkout), `04-web-and-ui-design/landing-page-and-conversion-design` (the page *before* the
  click; this skill owns *after*), `06-sector-and-domain-ux/design-ethics-and-anti-dark-patterns`
  (paired — the general ethics/dark-pattern doctrine this skill applies to retail),
  `10-content-design-and-ux-writing/ux-writing-and-microcopy` (button/error/empty wording).
<!-- dual-compat-end -->
