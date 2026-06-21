# Checkout & Retail Flow Patterns (honest conversion, zero dark patterns)

The surface-by-surface playbook for a retail buying journey, and the ethics line that runs through
all of it. A store may *persuade* — with clarity, real proof, honest scarcity, and a genuine
guarantee — but it may never *coerce or deceive*. The test for any technique is the same as for a
landing page: **"Does it still work if the shopper fully understands what I'm doing?"** If yes, it
is persuasion. If it only works because they were rushed, confused, or opted-in without noticing, it
is a dark pattern and is banned.

> Why this is doctrine, not preference: `doctrine/design-doctrine.md` §0 — the moat is looking
> *authored and trustworthy by skilled human hands.* A store that hides a fee until step four, or
> auto-renews a subscription with a buried cancel, reads as exactly the opposite the moment the
> trick is noticed (and it is noticed — at the bank statement, at the chargeback, in the review).
> Retail dark patterns also invite refunds, chargebacks, churn, one-star reviews, and regulatory
> action (FTC "click-to-cancel," EU Consumer Rights / Omnibus directives on drip pricing and fake
> reviews, UK DMCC Act). They convert the wrong shoppers and cost more than they earn.

This file cites `doctrine/references/interaction-anti-patterns.md` (entries **B1, B2, B3, C3, C4,
D6**) and the doctrine throughout. Read alongside `form-ux-design` for field mechanics.

---

## The retail spine — answer the shopper's questions in order

| Surface | The question it answers | The one job |
|---|---|---|
| **PLP** (listing/search) | "Do you have something for me, and which one?" | Findability + honest comparison |
| **PDP** (detail) | "Is *this* the right thing, and what if it's not?" | Believable decision + one clear add action |
| **Cart** (basket) | "What am I buying and what will it really cost?" | Honest, complete, editable running total |
| **Checkout** | "How do I pay, with the least effort?" | Guest-first, minimum fields, no surprises |
| **Payment/address** | "Is my money safe and is this the final amount?" | Real trust cues + final total = charged amount |
| **Post-purchase** | "Did it work, when does it arrive, and can I return it?" | Confirmation + status + symmetric returns |

The *sequence* is load-bearing. Each surface earns the right to the next.

---

## §PLP — Product Listing Page

**Card decision data (each card carries only what drives the choice):** real product image, name,
the *real* current price, rating/review count, and the key variant or availability signal. Keep the
grid scannable; resist cramming every spec onto the card.

- **Price honesty.** Show the real price. A struck-through "was" price appears **only if it was
  genuinely the prior selling price** for a real period — fake "RRP" anchoring is deceptive (EU
  Omnibus / UK DMCC explicitly target this).
- **Filters/sort match the catalog**, not a generic template. Filters reflect the shopper's real
  decision attributes (size, colour, price band, brand, in-stock). Active filters show as removable
  chips; never silently reset a selection. Persist filter/scroll state on back-navigation.
- **Sponsored items are labelled.** If any placement is paid, mark it clearly — a disguised ad is a
  dark pattern (`interaction-anti-patterns.md`; doctrine).
- **Scarcity on cards is real and live only.** "Only 2 left" is a *helpful* signal when true; an
  invented count that resets on reload is banned (see §Dark-pattern table).
- **Performance.** The first row of product images is the LCP element — keep them light, reserve
  space to protect CLS (`doctrine/references/web-performance-budgets-2026.md`).

---

## §PDP — Product Detail Page

**Above-the-fold decision set:** zoomable real imagery (multiple angles), name, honest price *with
the all-in cost knowable* (tax-inclusive where the market expects, shipping at least estimable), a
variant picker, and one clear primary action.

- **Variant picker tells the truth.** Only in-stock size/colour combinations are selectable;
  out-of-stock combinations are visibly marked, not silently broken — never let a shopper pick a
  phantom variant and discover it later (a metaphor/feedback failure, and a trust hit).
- **One primary action: Add to cart / Buy now.** Wishlist, share, compare are visibly subordinate —
  one primary action per view (`interaction-anti-patterns.md` **B3**; **D6** Oceans of Buttons).
- **"Add to cart" does exactly and only what it says.** It never silently adds a warranty, an
  add-on, a subscription, or a second item — that is **sneak-into-cart** (banned).
- **Believability content on the page, not after payment:** real specs, a real delivery estimate, the
  real returns window/terms, and real reviews showing the genuine star distribution (curating to
  5-stars only, or planting reviews, is banned and now illegal in several markets).

---

## §Cart — Basket

The cart is where the shopper forms their cost expectation. Break that expectation later and you
lose the sale and the trust.

- **Only chosen line items.** Never a pre-added accessory, "popular add-on," insurance, or sample
  ticked by default (**pre-checked opt-in** + **sneak-into-cart**, both banned).
- **Honest, complete-as-knowable running total:** subtotal, then **tax and shipping shown or clearly
  estimated *here***, not sprung at the final step. If shipping needs a postcode/region, ask for it
  in the cart so the final total is not a surprise — surfacing costs only at the end is **drip
  pricing / hidden costs** (banned; doctrine "Hidden costs").
- **Threshold nudges are honest.** "£6 away from free shipping" is fine and helpful. Auto-adding a
  filler item to cross the threshold is **theft-by-friction** (banned).
- **Edit and remove are obvious and reversible.** Quantity change and remove are one action; a
  removed item is undoable (`interaction-anti-patterns.md` **C3** — no dead end, offer undo).
- **One clear path forward** ("Checkout") plus a quiet "continue shopping." Don't bury the proceed
  action; don't make it compete with three equal buttons.

---

## §Checkout — the conversion-critical seam

Apply `form-ux-design` for field anatomy, the five field states, validation timing, and labels-above.
Apply these retail rules on top.

### Guest-first is the rule (`interaction-anti-patterns.md` B1)
- **Guest checkout is offered first**, with **equal or greater visual weight** than "Sign in /
  Create account." A registration wall before purchase is the single highest cart-abandon driver and
  a banned pattern ("value before auth").
- **Account creation is offered *after* the order**, as a one-tap "save these details for next time"
  using data the shopper already entered (just set a password) — never as a gate, never as a
  pre-checked "create an account" buried in the flow.
- Returning shoppers can sign in, but it is an *option beside* guest, not a prerequisite.

### Minimum field set (`interaction-anti-patterns.md` B2)
- Ask **only what fulfilment and payment truly need.** Every extra field measurably depresses
  completion. No "how did you hear about us," no phone "just in case," no marketing opt-in framed as
  required.
- `autocomplete` attributes on every field; **address lookup/autofill**; correct `inputmode` and
  mobile keyboards (numeric for card/postcode); single-column; labels above (never placeholder-as-
  label); **billing = shipping by default** with one toggle to differ.
- **Inline, solution-bearing validation** on blur — never a late "your card is invalid" that wipes
  the form. Preserve entered data across errors (WCAG 2.2 **3.3.7 Redundant Entry**).

### A real progress signal & no end-surprises
- Multi-step checkout shows a true step indicator ("Step 2 of 3"); a single-page accordion shows all
  sections and which is active. The shopper always knows how much remains.
- **The final total is shown in full adjacent to the pay button** — items + tax + shipping + every
  fee — with the delivery date and the returns/cancellation terms one glance away. Nothing new
  appears *after* the pay button is pressed.

---

## §Payment & address — trust at the moment of money

- **Express/wallet pay up front** (Apple Pay, Google Pay, mobile-money where regional) is a
  legitimate friction-cut — it skips manual address/card entry. It must still **show the full total
  before confirming**.
- **Real trust cues:** a genuine secure-checkout signal (the lock is meaningful, not decorative),
  recognised card/wallet marks, and a plain statement of *what is charged and when*. The charge
  equals the displayed total — never padded.
- **Address minimised** via lookup; validated and formatted per locale; errors inline next to the
  field. Card fields auto-detect type, use the numeric input mode, and **never block paste** (paste-
  blocking on card or coupon fields is a hostile pattern).
- **No phantom fees at this step.** If a fee exists, it was already in the cart total (see §Cart).

---

## §Continuity — subscriptions, warranties, add-ons (opt-IN, symmetric exit)

- **Unchecked by default, always.** Every recurring charge, warranty, insurance, or add-on requires
  a deliberate opt-in. A pre-ticked box is **consent-by-inertia** (banned).
- **State the terms at the point of opt-in:** the price, the cadence (monthly/annual), the first
  charge date, and the cancel path — right there, not in a linked policy.
- **Forced continuity is banned.** A "free trial" that converts to a paid plan must say so plainly
  *before* sign-up, **remind before the first charge**, and offer a **cancel as easy as the sign-up**
  was — same number of steps, same place (no **roach motel**; `interaction-anti-patterns.md` **C4**;
  FTC click-to-cancel). If a stakeholder asks to "make cancel harder," refuse.

---

## §Post-purchase — returns, refunds, status (the trust that earns the next sale)

- **Order confirmation** states what was bought, the all-in amount charged, the delivery estimate,
  and the returns window — a clear next step, never a dead end (`interaction-anti-patterns.md`
  **C3**).
- **Returns are symmetric and findable.** Initiating a return is no harder than buying was; the
  policy is in plain language and was **visible before purchase**, not hidden. A genuine, clearly
  stated returns policy is one of the strongest *honest* conversion levers in retail — it removes
  the shopper's downside.
- **Order status without a support ticket;** status changes communicated; refunds confirmed in
  writing with timing. Don't make the shopper chase their own money.

---

## Banned retail dark patterns → honest swaps

Never ship the left column. If a stakeholder asks for one, refuse and offer the right column.

| Dark pattern (banned) | Why it's harmful | Honest swap |
|---|---|---|
| **Forced account creation** before checkout | Highest abandon driver; coerces commitment before value | **Guest checkout first**; offer account *after* the order, one-tap |
| **Hidden costs / drip pricing** — fees/tax/shipping appear only at the final step | Bait-and-switch; abandonment, chargebacks, regulatory action | Show the **full total before the pay button**; estimate shipping in the cart |
| **Sneak-into-basket** — items/add-ons added without an explicit choice | Theft-by-friction | Add only what the shopper explicitly chose |
| **Pre-checked add-ons / insurance / warranty / opt-ins** | Consent by inertia | Unchecked by default; deliberate opt-in with terms shown |
| **Forced continuity** — free trial auto-charges, cancel buried (**roach motel**) | Charges people who forgot; refund/chargeback magnet | State terms up front, **remind before charging**, cancel as easy as signup |
| **Fake scarcity** — "Only 2 left!" that resets on reload | Lies about availability; trust collapses when caught | Show *real* live stock, or say nothing about scarcity |
| **Fake urgency** — countdown that restarts each visit | Manufactured pressure on a lie | Real campaign deadlines only, or none |
| **Fabricated social proof** — invented "12 people viewing," planted reviews, fake "verified" | Deceives; now illegal in EU/UK/US | Real aggregate numbers ("2,400 orders this month"); genuine review distribution |
| **Confirmshaming** the opt-out — "No thanks, I hate saving money" | Manipulates via shame | Neutral decline: "No thanks" / "Maybe later" |
| **Disguised ads** in PLP — sponsored items styled as organic | Deceives about what's paid | Label sponsored placements clearly |
| **Fake "was" prices / fake RRP anchoring** | Deceptive discount; targeted by EU Omnibus / UK DMCC | Strike through only a genuine prior price held for a real period |
| **Paste-blocking** on card/coupon fields; **trick double-negative** opt-outs | Friction-as-weapon; exploits misreading | Allow paste; plain single-direction wording |
| **Roach-motel cancellation** — easy to buy, hard to leave | Traps shoppers; breeds chargebacks and churn | Symmetric: cancel/return where and how you bought |

---

## The pre-build gate (mirrors the SKILL checklist)

Walk every surface against the **Anti-Dark-Pattern Checklist** in `SKILL.md`. Any match is a
finding; any unresolved finding is a no-go. The honest version of a retail flow is not only the
ethical one — across real measurement it is the *more durable* one: it converts the right shoppers,
who return, refer, and don't charge back.

---

*Companion to `doctrine/references/interaction-anti-patterns.md` (B1/B2/B3/C3/C4/D6) and
`doctrine/design-doctrine.md` §0. Retail-specific application of the engine's anti-dark-pattern
posture; pairs with `06-sector-and-domain-ux/design-ethics-and-anti-dark-patterns`. Patterns
evergreen; regulatory references current to 2026 (FTC click-to-cancel, EU Omnibus/Consumer Rights,
UK DMCC Act).*
