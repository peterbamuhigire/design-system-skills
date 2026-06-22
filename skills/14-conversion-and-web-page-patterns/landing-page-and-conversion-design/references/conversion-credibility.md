# Conversion-Credibility (honest persuasion, zero dark patterns)

The ethics line of this skill. A landing page may *persuade*; it may never *coerce* or *deceive*.
The distinction is simple: an honest lever still works when the visitor fully understands it; a dark
pattern works only because the visitor *doesn't*. This file lists the honest levers, the banned dark
patterns with honest swaps, and the proof-authenticity rules.

> Why this is doctrine, not preference: `doctrine/design-doctrine.md` §0 — the moat is looking
> *authored and trustworthy by skilled human hands.* A page that tricks the visitor reads as
> exactly the opposite the moment the trick is noticed (and it is noticed). Dark patterns also
> invite chargebacks, churn, refund demands, regulatory action (FTC/EU), and app-store/platform
> bans. They convert the wrong people and cost more than they earn.

---

## The honest conversion levers (use these)

| Lever | Why it works honestly | How to apply |
|---|---|---|
| **Specificity** | A true, concrete number survives scrutiny; a superlative doesn't. | "Cuts month-end close from 9 days to 2" not "revolutionary platform." |
| **Real, attributable proof** | Named people/companies are verifiable; the visitor trusts what they can check. | Name, role, company, ideally a face. Real logos of real customers. |
| **Risk reversal (real)** | Removes the visitor's downside, so the decision gets easier. | A genuine guarantee, real free tier, "no card required" — only if true. |
| **Transparency** | Showing price, renewal, and cancellation up front builds trust and filters for the right buyer. | Visible pricing; state renewal terms and the cancellation path. |
| **Information scent / message match** | The visitor feels understood when the page answers the question the ad raised. | Echo the click's promise in the headline. |
| **Reciprocity (real value)** | Giving genuine value first earns goodwill legitimately. | A real free tool, a useful guide, a working free tier — not a bait. |
| **Clear single focal action** | Reducing choices reduces paralysis — an honest cognitive aid. | One primary CTA, value-stating copy, one focal point per screen. |

The test for any lever: **"Does it still work if the visitor fully understands what I'm doing?"**
If yes, it's persuasion. If it only works because they're confused or rushed, it's a dark pattern.

---

## Banned dark patterns → honest swaps

Never ship the left column. If a stakeholder asks for one, refuse and offer the right column.

| Dark pattern (banned) | Why it's harmful | Honest swap |
|---|---|---|
| **Fake scarcity** — "Only 2 left!" that resets on reload | Lies about availability; destroys trust when caught | Show *real* stock/seat counts, or don't mention scarcity at all |
| **Fake urgency** — countdown timer that restarts each visit | Manufactured pressure based on a lie | Real deadlines only (a genuine campaign end date), or none |
| **"3 people are viewing this right now"** (invented) | Fabricated social pressure | Show *real* aggregate proof: "2,400 teams use this" |
| **Confirmshaming** — "No thanks, I hate saving money" | Manipulates via shame | Neutral decline: "No thanks" / "Maybe later" |
| **Pre-checked opt-ins / add-ons** | Opts the visitor in without consent | Unchecked by default; the visitor opts in deliberately |
| **Sneak-into-basket** — items added without action | Theft-by-friction | Add only what the visitor explicitly chose |
| **Forced continuity** — free trial auto-charges, cancel is buried | Charges people who forgot; refund/chargeback magnet | Remind before charging; make cancel as easy as signup |
| **Roach motel** — easy to get in, hard to get out | Traps users; breeds resentment and churn | Symmetric: cancel/downgrade in the same place you upgraded |
| **Disguised ads / fake "system" notices** | Deceives about what is clickable | Label ads; never fake an OS/system message |
| **Trick wording / double negatives on opt-outs** | Exploits misreading | Plain, single-direction wording |
| **Hidden costs** — fees appear only at the final step | Bait-and-switch | Show total cost (incl. fees/renewal) before the CTA |

The honest swap almost always converts *better over the lifetime of the customer*, because it
selects for buyers who actually want the product and keeps them.

---

## Proof-authenticity rules

Social proof only works if it is believed — and fabricated proof, once suspected, drives trust
*below* having no proof at all.

1. **Attribution is mandatory.** Name + role + company (+ face when permitted). "★★★★★ — A happy
   customer" reads as invented and lowers trust.
2. **Never fabricate** testimonials, ratings, logos, or metrics. Using a company's logo who isn't a
   customer is both dishonest and legally exposed.
3. **Real numbers, stated precisely** and sourced internally. "Reduced support tickets 34%" beats
   "dramatically reduced support tickets" — and you must be able to back it.
4. **Match the proof to the visitor.** A testimonial from someone like the visitor (same role,
   sector, size) outperforms a famous-but-irrelevant name.
5. **Show, where possible.** A real screenshot, a real result, a named case study with numbers beats
   an adjective.
6. **Disclose relationships.** Paid endorsements, affiliate links, and sponsored placements must be
   disclosed (FTC and equivalents) — and disclosure, done plainly, *increases* credibility.

---

## When proof is genuinely thin

A new product may not have testimonials yet. Be honest, not fabricated:

- Lead with **specificity and risk reversal** instead of social proof.
- Use **founder credibility** (real bio, real track record) or **transparent methodology** ("here's
  exactly how it works") as the trust anchor.
- Offer a **strong real guarantee** or free tier — honest risk reversal substitutes for proof you
  don't have yet.
- Say "early access" / "join the first 100" *if true* — real early-stage framing is honest and can
  itself be attractive.

Never invent a testimonial or borrow a logo to fill the gap. The thin-proof page that is honest
out-converts the padded page that gets caught.

---

## Sources / authority

The persuasion levers trace to the established influence and direct-response literature (Cialdini's
principles applied *ethically*, conversion-research practice); the dark-pattern taxonomy traces to
the deceptive-design research community and consumer-protection guidance (FTC, EU) — i.e. to human
authority and the design/ethics literature, never to an AI tool's recommendation
(`doctrine/design-doctrine.md` §2 asymmetry rule). This skill's posture: persuade with truth,
refuse coercion, and prefer the choice that looks — and is — authored and trustworthy.
