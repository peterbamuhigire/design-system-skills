# Worked Example — Maduuka onboarding journey: persona → JTBD → map → opportunities

A worked, evidence-based **current-state journey map** for **Maduuka**, a B2B inventory app for
small East-African retailers. It builds on the research study in the sibling skill
(`ux-research-and-usability-testing/examples/research-plan-and-synthesis.md`): new-account
activation (first product added within 24h) had stalled at **38%**, and a mixed-methods study
found the loss was *not* "too many steps" — it concentrated at the **phone-OTP step (−39%)** and
a smaller bleed at the add-product step. This map structures that evidence over time and turns it
into a ranked opportunity backlog.

Every persona trait and emotion point below traces to that study (participant IDs `P1–P5`
moderated, `U1–U15` unmoderated, plus the analytics funnel). Nothing here is invented to fit a
roadmap.

---

## 1. Evidence-based persona

**Amina — runs a 2-staff hardware shop in Kampala**

| Field | Value | Evidence |
|---|---|---|
| Role | Owner-operator, hardware & building supplies, 1–10 staff. | Recruited segment (study screener). |
| Context | Serves customers at the counter while setting up the app on a mid-range Android over patchy mobile data; frequent interruptions. | Observed, P2/P4 sessions. |
| Goals | Stop running out of fast-moving stock; stop tracking it on paper/WhatsApp. | "I lose customers when I don't know the cement is finished." — P3 |
| Job (JTBD) | See §2. | Derived from goals + behaviour. |
| Pain today | Paper book is unreliable; finds out stock is out only when a customer asks. | P1, P3, U-notes. |
| Real quote | "Why do you need my number? I just want to see if this works first." — P2 (at OTP step). | Verbatim, moderated. |
| Behavioural axes | New to inventory software; high interruption; low tolerance for setup friction before seeing value. | Study synthesis. |
| Confidence / gaps | Goals & OTP friction: **high** (5 moderated + funnel). Long-term retention drivers: **assumed** — validate later. | Honest gap; route to research. |

---

## 2. Jobs-To-Be-Done

> **When I close my shop at night, I want to know which products are nearly out, so I can restock
> before I lose a sale tomorrow.**

- **Functional:** know what's low and restock in time.
- **Emotional:** feel in control, not anxious about surprise stock-outs.
- **Social:** look reliable to regular customers ("they always have what I need").

Every opportunity below is judged against this job — not against "is this a nice feature".

---

## 3. The journey map (stage × layer)

Stages are in Amina's words, not Maduuka's funnel labels. The emotion score (−2 … +2) cites
evidence at every peak and trough.

| Stage → | "Heard about it, worth a try?" | "Just let me in" | **"Why my number?"** | "Set up my shop" | "Add my first stock" | "Is it actually helping?" |
|---|---|---|---|---|---|---|
| **Doing** | Hears from a supplier; installs app. | Creates account (name, password). | Hits **phone OTP** screen; waits for SMS. | Picks shop type; skips payments. | Tries to add first product. | Checks if low-stock alerts appear. |
| **Thinking** | "Could this replace my book?" | "Quick, I have a customer waiting." | "Is this safe? Why do they need this?" | "Which type fits a hardware shop?" | "How do I enter a price + count?" | "Will it warn me before I run out?" |
| **Feeling** | +1 (curious) | 0 (impatient) | **−2 (suspicion + SMS never arrives)** | −0.5 (mild confusion) | **−1 (add-product form unclear)** | +1 (relief, *if* they reach it) |
| **Evidence** | P1, P5 quotes. | U-timings: median 40s. | **Funnel −39% here**; P2/P4 "why my number"; SMS delayed on one network. | P3 unsure which type. | Funnel −11%; U5/U9 abandoned form; ≤3-min criterion missed. | P3, P5 valued alerts once seen. |
| **Touchpoint / channel** | Word of mouth → app. | App. | App **+ SMS (cross-channel seam)**. | App. | App. | App + (future) SMS alert. |
| **Pain / moment of truth** | — | — | **Moment of truth + seam:** trust ask before value; SMS dependency on a third party / weak network. | Ownership unclear: shop-type list doesn't include "hardware". | Form labels/units unclear; no example. | The payoff that should have come first. |

**Reading the curve:** the deepest trough is the **OTP step** — a *trust* failure (asking for a
phone number before showing any value) compounded by a *cross-channel seam* (SMS delivery via a
third party over a weak network). This matches the funnel cliff exactly. The "too many steps"
hypothesis is wrong; the problem is **trust-before-value and a fragile channel hand-off**.

---

## 4. Cross-channel seam (mini service-blueprint slice)

The OTP trough is where the journey map alone is insufficient — the failure is **backstage**, so
one blueprint slice:

| Lane | At the OTP step |
|---|---|
| Physical evidence | OTP entry screen; the SMS (or its absence). |
| Customer action | Enters number, waits for code. |
| — line of visibility — | |
| Frontstage | "Code sent" confirmation. |
| Backstage | App calls SMS gateway; gateway routes via carrier. |
| Support process | **Third-party SMS gateway + carrier delivery** — variable latency, no retry surfaced, no owner watching delivery rates. |

**Backstage failure point:** SMS delivery is a single dependency with a hidden wait and **no team
owning its delivery rate** — invisible on the journey map, decisive in the funnel.

---

## 5. Alignment diagram → ranked opportunity backlog

Spine: **research → map → opportunity.** Every opportunity traces to evidence; scored by impact
on the JTBD × frequency × feasibility.

| # | Opportunity (How might we…) | Evidence | Impact | Freq | Feasibility | Priority |
|---|---|---|---|---|---|---|
| 1 | Defer the phone-number/OTP ask until *after* the user has added a product and seen value. | Funnel −39%; P2/P4 "why my number"; deepest trough. | **H** | **H** (all new users) | **M** | **1** |
| 2 | Make SMS delivery resilient: show a live "resend / call me instead" fallback and monitor delivery rate with an owner. | Backstage seam; SMS delayed on one carrier; no owner. | **H** | M | M | **2** |
| 3 | Add "Hardware / building supplies" to the shop-type list with a sensible default catalogue. | P3 couldn't find their type. | M | M | **H** | **3** |
| 4 | Redesign the add-product form: one pre-filled example, clear unit/price labels, inline help. | Funnel −11%; U5/U9 abandoned; ≤3-min missed. | **H** | **H** | M | **2** |
| 5 | Surface the low-stock alert payoff *earlier* (preview during setup) so the JTBD value lands before the friction. | P3/P5 valued alerts once seen; payoff comes last today. | **H** | M | M | **3** |

**Decision this map informs:** *Do not* cut the flow to one step (the PM's untested hypothesis).
Instead, **re-sequence for trust** (show value before asking for the number) and **harden the SMS
seam**. The map turned "make it shorter" into a defensible, evidence-traced backlog.

---

## 6. Coverage notes (doctrine & accessibility)

- **Slop signal escalated:** P2's "why do you need my number… I just want to see if this works"
  is the experience-scale tell of a generic, untrustworthy flow
  (`doctrine/references/ai-slop-taxonomy.md`); it is opportunity #1, not a nuisance comment —
  the authored, trustworthy experience is the moat (`doctrine/design-doctrine.md` §0).
- **Accessibility / channel-equity gaps stated, not hidden:** this map covers mid-range Android on
  patchy data with one low-vision participant (OS font scaling) from the source study. It does
  **not** yet model a screen-reader pass of the OTP/add-product forms, a feature-phone/USSD
  fallback, or low-literacy labelling. Those are known gaps to close against
  `doctrine/references/wcag-2.2-criteria.md` before claiming the onboarding "works for everyone".
