# Demand-Test Pages and the Funnel Learning Matrix

Parent skill: [`../SKILL.md`](../SKILL.md) (`landing-page-and-conversion-design`).

**When to read:** when a landing page is built to *learn* whether an offer is wanted before the
product exists (or before a feature is built), and when planning what must be designed and
measured at each stage from first visit to active referral. For choosing between experiment types
in general, see `../../../00-cross-cutting-ops-qa-a11y/design-audit/references/lean-ux-validation/entrypoint.md`
§4.3; this file details the landing-page route and the stage-by-stage learning plan.

---

## 1. Demand-test page versus conversion page

| Aspect | Demand-test page | Production conversion page |
|---|---|---|
| Purpose | Test one hypothesis about the value proposition or segment | Convert qualified visitors efficiently |
| Lifespan | Days to a few weeks, then removed or rebuilt | Ongoing |
| Success | A pre-set threshold is met or missed; both outcomes are useful | Conversion rate improves over baseline |
| Honesty requirement | Visitors who act are told promptly and plainly what exists today | Claims match the shipped product |

A demand-test page still meets the parent skill's craft, accessibility and credibility bars: a
sloppy page tests the sloppiness, not the offer.

## 2. Procedure

1. **Write the hypothesis and threshold first.** "Among [segment], at least [x]% of visitors
   from [channel] will [action] within [window]." Record metric, method and window before launch.
2. **Pick the committing action.** Stronger commitment is stronger evidence: email or phone
   capture < booked call or demo < deposit, pre-order or signed pilot. For high-price or committee
   purchases, clicks alone are not evidence (see the lean-ux-validation reference §5).
3. **State the value proposition in the time of a short advert.** One headline, one supporting
   line, one proof or illustration of the outcome, one action. If it needs a paragraph, the
   proposition is not yet clear enough to test.
4. **Design the after-page.** The confirmation page says exactly what happens next, when, and
   what does not exist yet; offer a human contact for nervous visitors. This is where the
   test earns or loses trust.
5. **Build variants only for the question.** Vary one element per variant (proposition, segment
   message, price framing), not the whole page.
6. **Bound the campaign.** Fix budget ceiling, audience definition, channel, keywords or
   placements, start and end date. Record all of them; an unbounded campaign cannot be read.
7. **Measure and decide.** Record visits by source, action rate, cost per committed action, and
   referral or share rate. Compare against the threshold and decide persevere, pivot or stop.
   Small counts are not results; see the significance rule in the lean-ux-validation reference §6.

| Decision | Rule | Failure caused by the wrong choice |
|---|---|---|
| Weak action chosen for a high-price offer | Use a booked conversation, deposit or pilot | False demand signal; product built for curiosity |
| Several elements changed in one variant | One change per variant | A result with no explainable cause |
| Threshold set after seeing data | Pre-register it | Any result can be called success |
| Personal data collected | Minimum data, consent at capture, retention and deletion stated | Breach of data-protection law and trust |
| Test finished | Remove or clearly relabel the page; follow up everyone who acted | Visitors left believing a product exists |

**Data protection.** In Uganda, the Data Protection and Privacy Act, 2019 requires prior consent
for collecting personal data; collecting financial or health information is further restricted.
Capture only what the test needs, state purpose and retention next to the field, and route
anything beyond contact details to a privacy review. Equivalent laws apply in Kenya, Rwanda and
Tanzania; confirm the applicable law per market (`NOT_ASSESSED` here).

## 3. The funnel learning matrix

Replace "design the screens" with "design what each stage must achieve and what we must learn
there." Rows are engagement stages; columns are fixed.

| Stage | User is doing | Business needs | Functionality required | Measurable learning question |
|---|---|---|---|---|
| Visitor | Arriving from an advert, search, a shared link or an agent | Convey the proposition fast | Landing page, source tracking | Which source brings visitors who act? |
| Lead | Leaving a contact or starting sign-up | Capture consented contact | Form, consent notice, confirmation | What share of visitors from each source leave contact? |
| Trial user | Trying the core task | Show value in first use | Onboarding, first task, help | What share complete the core task in the first session? |
| Customer | Paying or transacting | Convert and retain | Payment, receipts, support | What share of trial users transact within 14 days? |
| Advocate | Recommending to others | Earn referrals | Share or referral mechanism, reviews | What share refer at least one person who signs up? |

**Measurability rule.** Every learning question must be answerable with a number from a named
source. "How excited were visitors?" is not measurable; "what share of visitors from WhatsApp
shares started sign-up?" is.

**Feature triage per stage.** Before a feature enters the "functionality required" column, score
user value (evidence of need), effort to build, and business value (differentiator or decoration).
Features scoring low on user value and business value leave the matrix.

## 4. Worked example (original): SME payroll add-on for a Kampala accounting app

Hypothesis: "At least 8% of SME owners reaching the page from a targeted social campaign in
Kampala will book a 15-minute setup call for a payroll add-on that files PAYE and NSSF
schedules, within 10 days." Committing action: booked call (not email), because payroll is a
monthly paid service. Page: headline on the outcome ("Payroll done and schedules ready before the
15th"), one screenshot mock of a completed payroll run, one action. After-page: "We are onboarding
the first 30 businesses in November; a named team member will call you within two working days."
Variants: one alternative headline on penalties avoided. Campaign: fixed budget ceiling, Kampala
business-owner audience, 10 days. Result: `NOT_ASSESSED` (illustrative plan). Statutory filing
deadlines must be confirmed with the finance engine before any public claim.

## 5. Checks

- [ ] Hypothesis, threshold, metric and window recorded before launch.
- [ ] Committing action matches the price and purchase process.
- [ ] After-page states honestly what exists and what happens next.
- [ ] Budget, audience, channel and dates bounded and recorded.
- [ ] Personal-data capture is minimal, consented and reviewed for the target market.
- [ ] Every funnel-matrix learning question is numeric and sourced.

---

**Evidence/currentness (accessed 2026-09-24):** Uganda Data Protection and Privacy Act, 2019 (Act 9
of 2019), ULII and Parliament of Uganda texts - prior consent requirement and special personal
data restrictions. Advertising-platform features, costs and benchmark conversion rates:
`NOT_ASSESSED`; none are claimed. Other East African data-protection laws: `NOT_ASSESSED`.

Sources: Levy (2015) *UX Strategy*, O'Reilly Media; Ries (2011) *The Lean Startup*; Gothelf and
Seiden (2021) *Lean UX*, 3rd ed.
