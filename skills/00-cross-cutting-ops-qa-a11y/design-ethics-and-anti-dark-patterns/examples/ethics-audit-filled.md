# Worked Example — Ethics Audit of a Subscription Sign-up + Cancel Flow

A filled deceptive-pattern audit: find each dark pattern, name the harm, apply the honest swap.
Pairs with `ecommerce-and-checkout-ux` and `trust-credibility-and-social-proof`; uses the
catalogue in `references/dark-pattern-catalog.md`.

## Flow audited
"Streamio" media subscription: pricing page → sign-up → trial → billing → cancel.

| # | Dark pattern found | Category | Why it harms | Honest swap (the redesign) |
|---|---|---|---|---|
| 1 | "🔥 3 people are viewing this plan" + 09:58 countdown | **Fake urgency/scarcity** | Fabricated pressure; erodes trust when discovered | Remove. If a real deadline exists (promo ends), state the true date; otherwise no timer |
| 2 | Annual plan pre-selected + "Most popular" on the priciest tier with no basis | **Misdirection / false default** | Steers to higher spend by visual trick | Default to no pre-selection (or the plan that fits stated need); "Most popular" only if true, with the basis |
| 3 | Trial requires card; converts silently to paid; no reminder | **Forced continuity / hidden cost** | Surprise charge; the classic | Card optional for trial; **email 3 days before** it converts; state the charge date + amount up front |
| 4 | "No thanks, I don't want to save money" decline link | **Confirmshaming** | Manipulates via guilt | Neutral decline: "No thanks" / "Maybe later" |
| 5 | Add-ons (extra screens) pre-checked at checkout | **Sneak into basket** | Charges for unrequested items | Unchecked by default; opt-in only; itemised before pay |
| 6 | Cancel buried 5 levels deep; "downgrade" loops back to billing | **Obstruction / roach motel** | Easy in, hard out | Cancel reachable in ≤2 taps from account; same effort as sign-up; confirm once, no maze |
| 7 | Total hidden until final step (taxes/fees appear last) | **Drip pricing** | Decision made on a false number | Show all-in price (incl. tax/fees) at plan selection |

## Verdict & test
**7 deceptive patterns → NO-SHIP** until swapped. Applied the **"comfortable if the user saw the
intent?"** test to each — all 7 fail it; all 7 honest swaps pass. Legal note: several (hidden
subscription terms, obstructed cancel, pre-checked add-ons) are now restricted under EU
deceptive-pattern rules / FTC click-to-cancel — the honest swaps are also the compliant path.

After redesign: re-run the **`product-design-audit`** ethics dimension and `ecommerce-and-checkout-ux`
to confirm the flow converts on merit, not manipulation.

*Illustrative — copy the patterns and swaps, not the brand.*
