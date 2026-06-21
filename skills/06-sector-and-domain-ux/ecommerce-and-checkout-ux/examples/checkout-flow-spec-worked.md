# Worked Spec — "Kanjokya Coffee Roasters" buying journey (guest-first, honest, no dark patterns)

A complete, build-ready surface-by-surface spec for a small specialty-coffee retailer. Real product
data throughout (no lorem), the committed distinctive idea stated first, and every
Anti-Dark-Pattern Checklist item resolved inline. Use this as a fill-in template: replace the
content, keep the structure and the constraints.

---

## 0. Distinctive idea (committed before markup)

- **What:** product titles set in a warm humanist slab (e.g. **Roslindale** / a licensed editorial
  slab from the `02-editorial-literary` font folder if present), over a quiet humanist body
  (**Source Sans 3**) — paired, never monotype, no banned default. Prices set in the body face at a
  deliberate tabular weight, never shouted. PLP breaks the uniform-grid reflex with an editorial
  two-up "featured roast" band above the standard grid.
- **Why:** a specialty roaster sells craft and origin story; an authored, editorial type voice signals
  exactly that and separates the store from the convergent Inter-grid template (`doctrine/design-
  doctrine.md` §0; `pairing-principles.md`).
- **Human authority for the choice:** editorial slab + humanist body is a documented bookish pairing
  from the design literature, not an AI-recommend pick.
- **Palette intent:** warm roasted-bean neutrals (deep espresso `#3B2A1E`, cream `#F4EFE7`) with a
  single ripe-cherry accent `#B23A2E` for the one primary action only. Stock/error/success never
  ride on colour alone (text + icon too). All pairs gated on WCAG 2.2 contrast.

---

## 1. PLP — "Single-Origin Coffees"

| Element | Spec |
|---|---|
| Layout | Editorial "featured roast" two-up band, then a 3-col responsive grid (1-col mobile) |
| Card data | Real photo of the bag; name (*"Sipi Falls Washed AA"*); **real price £14.00/250g**; roast level chip; rating (4.6, 38 reviews); stock signal |
| Price honesty | No struck-through RRP unless genuinely a prior price. None used here. |
| Filters | Origin, Roast (light/medium/dark), Process (washed/natural/honey), Price band, *In stock* — matched to how coffee buyers actually decide. Active filters = removable chips; selection persists on back-nav. |
| Scarcity | "Last 3 bags" shown **only when live stock ≤ 3** — true and reload-stable. Most cards show no scarcity. |
| Sponsored | None. If a "roaster's pick" were paid placement it would be labelled. |
| Primary action | Card click → PDP. No "add to cart" on the card (variant choice needed first). |
| Perf | First image row is LCP; `loading=eager` on row 1, lazy below; fixed aspect-ratio box reserves space (CLS). |

**Checklist hits:** #6 real scarcity, #8 no disguised ads, #13 no convergent grid (editorial band +
authored type).

---

## 2. PDP — "Sipi Falls Washed AA"

| Element | Spec |
|---|---|
| Imagery | 4 real photos (bag, beans, brewed cup, origin), zoomable; multiple angles |
| Decision set above fold | Name; **£14.00 / 250g, VAT included** (UK expectation); "Delivery from £3.95, free over £30 — *est. shows in cart*"; variant picker; one primary action |
| Variant picker | Grind: Whole bean / Filter / Espresso / Cafetière. Size: 250g / 1kg. **Only in-stock combos selectable**; "1kg Espresso — out of stock" greyed with text, not silently broken |
| Primary action | **"Add to cart"** in the cherry accent — does *exactly* that. No auto-added subscription, sample, or kit. Wishlist + share are small text/icon, visibly subordinate |
| Believability | Tasting notes (real: blackcurrant, cola, brown sugar), altitude, process, roast date promise ("roasted to order, ships within 3 days"); **returns: "unopened bags returnable within 30 days, faulty coffee refunded — we pay postage"**; reviews show the **real** distribution (not 5-star only) |

**Checklist hits:** #1 (no gate), #3 (add = only chosen item), #10 (one primary action; "Add to cart"
does only that), #11 (returns stated before purchase), #12 (variant state has text + not colour-only).

---

## 3. Cart — running total, nothing unasked

```
Your basket
─────────────────────────────────────────────
Sipi Falls Washed AA · Filter · 250g    £14.00   [qty 1 ▾] [Remove]
Bugisu Natural · Whole bean · 1kg       £42.00   [qty 1 ▾] [Remove]
─────────────────────────────────────────────
Subtotal                                £56.00
Shipping (FREE over £30)                 FREE
Estimated VAT (incl. in prices)          —
─────────────────────────────────────────────
Total                                   £56.00
                       [ Proceed to checkout ]   ← cherry accent, single focal action
              continue shopping (quiet text link)
"Add a subscription and save 10%?" — UNCHECKED checkbox, terms shown on tick
```

- **Only chosen items.** No pre-added grinder, no "popular" sample ticked by default.
- **Honest total here.** Shipping resolved in the cart (postcode prompt if region-dependent); VAT is
  price-inclusive and stated. **Nothing new appears after the pay button.**
- **Threshold nudge honest:** if subtotal were £24, it would read *"£6 from free shipping"* — and
  would **not** auto-add a filler bag.
- Remove is reversible (undo toast).

**Checklist hits:** #2 (full total before pay), #3 (only chosen), #4 (subscription unchecked), #6
(no fake scarcity), #10 (one primary action).

---

## 4. Checkout — guest-first, single-page, minimum fields

```
Checkout                                   Step 1 of 2: Details
─────────────────────────────────────────────
●  Check out as guest          ← offered FIRST, full weight, default-selected
○  Sign in            ○  Create account (offered AFTER order instead)

Contact
  Email address            [______________]  (for order confirmation only)

Delivery address
  Full name                [______________]
  Postcode    [______]  [Find address]   ← address lookup
  Address     [auto-filled, editable]
  ☑ Billing address same as delivery       ← default ON

[ Continue to payment ]                         order summary pinned alongside
```

- **Guest first**, default-selected, equal/greater weight than account creation. No wall (B1).
- **Minimum fields:** email + name + address only. No phone "just in case," no "how did you hear,"
  no required marketing opt-in.
- `autocomplete` on every field, address lookup, `inputmode` correct, labels above, single column,
  billing=shipping default (B2; WCAG 3.3.7 redundant entry — data preserved across any error).
- Validation inline on blur, solution-bearing ("Enter a valid UK postcode, e.g. SW1A 1AA").
- **Account creation** appears only on the confirmation screen: *"Save these details? Set a password —
  one tap."* Never a gate, never pre-checked.

**Checklist hits:** #1 (guest first), #9 (min fields, autofill, single column), #12 (WCAG: focus
ring, ≥24px targets, redundant-entry).

---

## 5. Payment & trust

```
Step 2 of 2: Payment              🔒 Secure checkout
─────────────────────────────────────────────
[  Pay with Apple Pay  ]  [  Pay with Google Pay  ]   ← express, skips re-entry
            — or pay by card —
  Card number   [____ ____ ____ ____]   (auto-detects type, paste allowed)
  Expiry [__/__]   CVC [___]
─────────────────────────────────────────────
Order total                              £56.00   ← equals the amount charged
Delivery: 2–4 working days · Returns: 30 days, we pay faulty postage
                       [ Pay £56.00 ]            ← amount on the button
```

- Real trust cues: meaningful lock, recognised card/wallet marks, "what is charged and when" plain.
- **The button states the exact amount.** No fee appears after pressing it.
- Express pay still shows the full total before confirming. Paste allowed on card field.

**Checklist hits:** #2 (total = charged, on the button), #11 (returns one glance away), #12 (WCAG).

---

## 6. Subscription (continuity) — opt-IN, symmetric exit

Only if the shopper ticked the cart's "subscribe and save 10%":
- Terms shown at the tick: *"£12.60/250g every 4 weeks. First charge today, next on [date]. **Cancel
  or skip any time in one tap from your account** — same place you started it."*
- Reminder email before each charge. Cancel = one tap, same number of steps as signup. **No roach
  motel** (C4; FTC click-to-cancel).

**Checklist hits:** #4 (opt-in, terms shown), #5 (reminder + easy cancel).

---

## 7. Post-purchase — confirmation, status, returns

- **Confirmation screen:** items + **£56.00 charged**, delivery estimate (2–4 days), returns window
  (30 days), order number, and the one-tap "save your details" account offer. No dead end (C3).
- **Order status** visible in account / via link — no support ticket needed; despatch + delivery
  updates emailed.
- **Returns:** initiate from the order page in the same number of steps the purchase took; policy is
  the *same* plain-language one shown on the PDP before purchase; refund confirmed in writing with
  timing. Symmetric exit.

**Checklist hits:** #11 (symmetric, findable returns; stated before purchase), #2 (charged = shown).

---

## Anti-Dark-Pattern Checklist — final pass (all PASS)

| # | Item | Status |
|---|---|---|
| 1 | Guest checkout first, no forced registration | PASS — guest default, account after order |
| 2 | Full total before pay; no drip pricing | PASS — total in cart and on the pay button |
| 3 | Cart = only chosen items; no sneak-in | PASS |
| 4 | Add-ons/subscription unchecked by default | PASS — subscription opt-in, terms on tick |
| 5 | Recurring charge: terms up front, reminder, easy cancel | PASS — one-tap symmetric cancel |
| 6 | Scarcity real and live only | PASS — "Last 3 bags" only when true |
| 7 | Neutral decline wording | PASS — "No thanks" |
| 8 | Sponsored placements labelled | PASS — none used; rule stated |
| 9 | Minimum fields, autofill, single column, labels above | PASS |
| 10 | One primary action; add/pay does only what it says | PASS |
| 11 | Returns stated before purchase; symmetric to buy | PASS |
| 12 | Checkout passes WCAG 2.2 (focus, ≥24px, contrast, not colour-only) | PASS |
| 13 | No convergent default (authored type + editorial PLP band) | PASS |

*Worked example for `ecommerce-and-checkout-ux`. Product data is illustrative-but-realistic, never
lorem. Cites `doctrine/references/interaction-anti-patterns.md` (B1/B2/B3/C3/C4/D6) and
`doctrine/design-doctrine.md` §0. Swap the content; keep the structure and the constraints.*
