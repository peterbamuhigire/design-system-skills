# Lean UX Validation: Test the Idea Before You Build It

Parent skill: [`../../SKILL.md`](../../SKILL.md) (`design-audit`).

**When to read:** before any feature is designed or built — when a stakeholder or user asks for a
feature, when a research session is being planned, when a design change needs a success metric,
or when a backlog must be ordered. Companion for running the sessions themselves:
`skills/05-ux-process-research-and-psychology/ux-research-and-usability-testing`.

Acknowledgement: shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

---

## 1. Inputs and outputs

| Input | Why it is needed |
|---|---|
| The request as stated (feature, complaint, idea) | Raw material to reframe as a problem |
| Who is asking and who would use it | Defines the market segment to test |
| Current metrics and funnel data, if any | Baseline for success criteria |
| Budget and time box for validation | Decides which experiment is affordable |
| For premium or high-price offers: sales stage, price band, buyer roles | Changes what counts as evidence (section 5) |

**Output:** a validation record (for example `docs/ux/lean-validation-YYYY-MM-DD.md`) containing
the hypothesis, ranked assumptions, experiment chosen and why, pre-set success threshold, result,
and the build / change / stop decision.

## 2. Working stance

- **A feature is a hypothesis, not a deliverable.** Write "We believe [change] for [segment] will
  cause [measurable behaviour]; we will know when [metric] reaches [threshold] by [date]." If the
  last clause cannot be written, the work is not ready to design.
- **Diagnose pain before prescribing.** Treat the team as clinicians: observe symptoms, ask where
  it hurts, diagnose, prescribe, monitor, adjust. Users describe pain; they do not write the
  prescription.
- **Data says what, research says why.** Quantitative data locates the problem; observation and
  interviews explain it. Use both.
- **Short, cross-functional cycles.** Designers, engineers and the product owner test together;
  hand-offs between silos lose the evidence.
- **An unbuilt bad feature is money kept.** Invalidating an idea early is a successful outcome,
  not a failure.
- **Research is not optional for lack of time.** A week of observation is cheaper than rebuilding
  a shipped feature.

## 3. Procedure

1. **Reframe the request as a user problem.** Ask "why?" until you reach the pain. Never lock in
   the requested solution at this step.
2. **Validate in strict order: problem, then market, then product** (decision table 4.1). Do not
   test a product with a market that has not been shown to share the problem.
3. **Write the hypothesis and design the test first.** State the metric to move, how it will be
   measured and the success threshold (section 6) before any sketch.
4. **Write design stories** in behavioural form: "A member who is unsure of her loan balance can
   find it within one screen of opening the app."
5. **List and rank assumptions** (section 4.2). Test the riskiest one first.
6. **Try to invalidate cheaply.** Choose the cheapest experiment that could prove the riskiest
   assumption wrong (decision table 4.3).
7. **Generate options in a short silent session** — at most 15 minutes; everyone writes alone,
   then reads aloud; no voting during generation.
8. **Decide.** Plot options on expected return (vertical) against expected cost (horizontal), with
   cost estimates from engineering. Choose; indecision is itself a common cause of product
   failure.
9. **Sketch rapidly and disposably** — states and flows, not only screens — and show sketches to
   four or five people straight away.
10. **Build an interactive prototype only when warranted**: the interaction is complex, or a
    mistake would be expensive to fix after build.
11. **Test, then iterate.** Assume the first design is wrong. Run five users, change, run five
    more.
12. **Record the decision** (build, change, stop) against the pre-set threshold. A feature is done
    when it moves its metric, not when it ships.

Steps 1, 3, 8 and 11 are never skipped.

## 4. Decision rules

### 4.1 Validation layer

| Layer | Question | Evidence that it is validated | Consequence of skipping |
|---|---|---|---|
| Problem | Is there a real, specific, painful problem? | Several people in one group independently describe the *same specific* pain, and it is severe enough that they would pay or change behaviour to remove it | You build a good solution to a problem nobody has |
| Market | Is the segment specific and large enough? | You can find at least five people with near-identical problems; the segment is narrow ("SACCO treasurers in Wakiso reconciling mobile-money deposits by hand"), not broad ("finance people") | Findings contradict each other because you tested several markets at once |
| Product | Does *this* solution solve *that* problem for *that* segment? | Target behaviour reaches the pre-set threshold in a show-not-tell test | You cannot tell whether the idea or the execution failed |

If fewer than five matching people can be found, the market definition is wrong: narrow or
redefine it before continuing.

### 4.2 Assumption ranking

Score each assumption 1-3 on **impact if wrong** and 1-3 on **current uncertainty**; multiply.

| Score | Action | Consequence of a wrong call |
|---|---|---|
| 6-9 | Test before any design work | Building on an untested fatal assumption |
| 3-4 | Test alongside early sketches | Late rework if it fails |
| 1-2 | Accept; monitor after launch | Wasted research budget if tested first |

### 4.3 Experiment choice

| Assumption type | Cheapest adequate experiment | What it measures | Wrong choice and its cost |
|---|---|---|---|
| The problem exists and how people work around it | Contextual inquiry: watch five target users do the real task in their setting; stay silent; ask open questions | Actual workflow, interruptions, workarounds | A survey here produces opinions about an imagined workflow |
| Pain with an incumbent product | Competitor test: recruit four or five users of a rival product (for example through low-cost ads) and watch them use it | Frustrations people already pay to live with | Asking non-users yields hypothetical complaints |
| Demand for an offer that does not yet exist | Landing-page test: describe the offer as if it exists with a buy, pre-order or sign-up action; drive low-cost traffic | Click-through and sign-up rate against threshold | Building the product first costs months to learn the same |
| Demand for a feature in an existing product | Fake button (feature stub): place the entry point where the feature would live; on tap, explain it is coming and optionally capture interest | Tap rate among exposed users | If even users who demanded it do not tap, building it wastes the build |
| Whether a design is usable | Prototype test with five users, one realistic task each | Completion, time, errors, hesitation | Describing the idea instead measures the user's imagined version |
| Quick read on a flow with no budget | Guerrilla test: a small incentive (a soda, airtime) for ten minutes in a café, taxi stage or campus; one task; only the data a real user would have; observe silently | Gross usability failures | Testing only friends and colleagues gives biased approval |
| Confirming a pattern already seen qualitatively | Survey | Prevalence across the segment | Surveys used for discovery miss what nobody thought to ask |
| Choosing between two working variants at volume | A/B test | Difference in a pre-set metric | Too little traffic gives noise; see section 6 |

## 5. Premium and high-price offers

Clicks are weak evidence when the buyer is a committee or the price is high. Count stronger
commitments: qualified meetings booked, diagnostic or assessment requests, completion of a
budget-fit form, quality of replies, introductions to other stakeholders, and paid pilots. Also
test buyer credibility signals, willingness to pay, the proof the buyer will demand, friction in
the sales cycle, and whether each conversation ends in a concrete next-step commitment.

## 6. Evidence thresholds and metrics

- **Set the threshold before the test.** Name the metric, the measurement method, the size of
  change and the window, e.g. "15% increase in completed loan applications within 30 days,
  statistically significant". Record it in the validation record.
- **Qualitative sample:** five participants per round; new patterns rarely appear after five or
  six. Iterating in several rounds of five beats one large round.
- **Quantitative significance:** tiny counts are not results. Three conversions against six is
  noise; run until the sample supports a significance test, or treat the outcome as unverified.
- **Look for movement in several metrics together.** One metric alone can mislead.
- **Reject vanity metrics.** For every metric ask which business goal sits behind it. A metric
  that rises while revenue, retention or task success stays flat is vanity (for example, a
  reminder that raises app opens but not repayments made).
- **Know the limits of A/B testing.** It finds the best of the variants supplied and can trap the
  team on a local maximum; it cannot explain *why* a variant fails. Pair it with observation, and
  do not use it to settle taste decisions (see `doctrine/references/creative-selection-and-taste.md`).
- **Diagnose pain from behaviour:** watch users, talk to churned users, and read funnel
  drop-offs.

## 7. Session conduct rules

| Rule | In practice | Consequence of breaking it |
|---|---|---|
| Show, never describe | Put a prototype, stub or page in front of the person | People answer for an imagined product and say yes to end the conversation |
| Never ask "Would you use this?" | Observe what they do instead | Predictions of future behaviour are unreliable |
| Stay quiet | Do not explain or sell the concept | The session measures your pitch, not the design |
| No guided tour | Ask "Show me how you would…" | You learn nothing about discoverability |
| Follow up | "It was nice" → "What made it nice? What did you expect to happen?" | Vague praise recorded as evidence |
| Hear problems behind solutions | A request for X is a proposed solution; ask why until the pain is clear; one request may hide several distinct problems needing different designs | You build the requested feature and miss the actual need |

## 8. Backlog ordering

- Plot candidates on expected return against expected cost; high-return, low-cost items first.
- Prioritise removing the most painful friction for the highest-value users.
- Treat every request as a proposed solution to be traced back to its problem; the problem may
  have better solutions than the one requested.
- **Define the MVP as a limited product, not a poor one.** A limited product does a few things
  well, has a clear starting point, is not confusing, and is not so rough that it repels the
  target market. A poor product does many things badly and teaches nothing, because you cannot
  tell whether the idea or the execution failed.

## 9. Worked example: SACCO loan-balance reminders

A Kampala savings and credit co-operative asks for "WhatsApp reminders for loan repayments".

1. **Reframe:** why? Treasurers report late repayments; members say they do not know their
   balance or due date.
2. **Problem layer:** contextual inquiry with five members at the branch counter shows each
   phones the treasurer or queues to learn their balance. Same specific pain, repeated: problem
   validated.
3. **Market layer:** segment narrowed to members repaying by mobile money, not by salary check-off
   (check-off members never miss).
4. **Hypothesis:** "Showing balance and due date on the mobile-money confirmation SMS will raise
   on-time repayments among mobile-money members from 62% to 75% within two cycles."
5. **Assumptions ranked:** members read the confirmation SMS (impact 3 × uncertainty 3 = 9, test
   first); the core banking system can expose balances (3 × 1 = 3); members want WhatsApp
   specifically (1 × 2 = 2, accept for now).
6. **Experiment:** for one cycle, the treasurer manually adds the balance line to confirmations
   for 40 members (a stub; no build). On-time repayment in that group: 77%, against 61% in a
   matched group.
7. **Decision:** build the SMS balance line; drop the WhatsApp channel pending evidence. The
   original request would have built a new channel for a problem that one line of copy solved.

## 10. Checks before sign-off

- [ ] Request reframed as a problem; the requested solution not assumed.
- [ ] Problem, market and product validated in order, each with named evidence.
- [ ] Hypothesis and numeric success threshold written before design began.
- [ ] Assumptions ranked; the riskiest tested first with the cheapest adequate experiment.
- [ ] Participants are target users, not friends or colleagues.
- [ ] No session described the idea or asked "Would you use this?".
- [ ] Sample sizes support the claim (five per qualitative round; significance for quantitative).
- [ ] Metrics checked for vanity; more than one metric reviewed.
- [ ] MVP scoped as limited, not poor.
- [ ] Decision (build, change, stop) recorded against the threshold.

## 11. Common failures

Solving a problem that does not exist; aiming at a market that is too broad; describing instead of
showing; skipping research for lack of time; building before trying to invalidate cheaply;
sketching before the problem is understood; shipping a poor MVP and calling it lean; treating
feature requests as requirements; working in silos with hand-offs; testing only with friends and
colleagues.

---

Sources: Klein, L. (2013) *UX for Lean Startups*, O'Reilly (hypothesis-driven validation,
problem-market-product order, feature stub); Gothelf, J. and Seiden, J. *Lean UX*, O'Reilly
(hypothesis statements, assumption ranking). Synthesised and restructured for this engine; the
worked example is original.
