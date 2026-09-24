# Experiment-Aware Design Evaluation

Parent skill: [ux-research-and-usability-testing](../SKILL.md). Load this reference when a design
change will be judged by an online controlled experiment (A/B, multivariate, holdback), when a
designer must prepare variants for one, or when an experiment result is being used to justify a
design decision.

The experiment contract (hypothesis, metrics, power, stop rule) is owned by the SRS engine
(`07-agile-artifacts/05-saas-growth-experiment-doc`); the platform is engineering's. This file
covers the designer's part: choosing whether to experiment at all, designing variants that can
teach something, protecting the experience while the test runs, and reading the result honestly.

## 1. Experiment or not

| Question the team is asking | Method | Why not the other |
|---|---|---|
| Why do people fail at this step? | Moderated usability test (5-8 per segment) | An A/B test reports that they fail, not why |
| Is the flow usable by screen-reader and switch users? | Assistive-technology testing with disabled participants | Traffic splits rarely include enough of them to detect anything |
| Which of two finished, usable designs moves the agreed metric more? | A/B test | Lab sessions cannot estimate effect size |
| Is the new direction worth pursuing at all? | Learn-intent test with a feature-level metric, then usability sessions on the loser and winner | A launch-grade test wastes traffic on an unproven idea |
| Did the redesign keep helping after three months? | Holdback | A two-week test cannot see novelty decay |

Hard rule: accessibility, legibility and harm are not decided by conversion. A variant that fails
WCAG 2.2 AA does not enter the test, whatever it might win.

## 2. Designing variants that can teach

- **One hypothesis per variant.** Name the single mechanism the variant tests ("fee shown before
  confirmation reduces surprise"). A variant that changes copy, layout and colour at once can win
  without telling you which change mattered.
- **Minimum effective difference.** The change must be large enough to plausibly exceed the
  experiment's minimum detectable effect. Micro-tweaks on low-traffic screens produce
  "inconclusive", which teams misread as "no difference".
- **Product-experience invariants.** List what every variant must keep: navigation, account
  access, cart or basket, payment options, help, legal text, focus order. Removing an invariant makes
  the result invalid, not negative.
- **Collision check.** Compare your variant against every live test on the same screen or journey
  at every breakpoint. Two overlapping tests that each add width, banners or sticky elements can
  break the layout for users who receive both. Request the same experiment layer (mutually
  exclusive) when surfaces overlap.
- **Complete state coverage.** Each variant needs loading, empty, error, offline, long-content,
  RTL/translation-expansion and reduced-motion states designed, not only the hero state.

## 3. Variant QA before exposure

Treat each variant as a release candidate.

| Check | Evidence | If missing |
|---|---|---|
| Render per variant on the target device matrix (include a low-end Android on 3G for East African consumer products) | Screenshots or recordings named by variant and device | Mark `NOT_ASSESSED`; block launch |
| Control shows no treatment | Control screenshots | Block launch |
| Accessibility on each variant | Keyboard, screen reader, contrast and target-size checks | Block launch |
| Copy and translations final | Content sign-off per locale | Block launch |
| Performance budget | Field or lab INP, LCP, CLS against the budget in `doctrine/references/web-performance-budgets-2026.md` | Treat as a guardrail risk |

## 4. Design guardrails to request

Ask the experiment owner to include at least one experience guardrail alongside the business
metric: task completion or error rate on the changed step, support contacts for that journey,
rage-tap or back-navigation rate, and a performance guardrail (INP, not the retired FID). A
conversion win that raises support contacts or errors is a design failure awaiting discovery.

## 5. Reading results as a designer

| Result pattern | Design reading | Next step |
|---|---|---|
| Winner with guardrails flat | Mechanism plausibly confirmed | Ship; record the design principle learned, not just the screen |
| Winner, but effect decays by exposure day | Novelty; users clicked because it was new | Holdback or longer read before generalising the pattern |
| Inconclusive with adequate power | The change does not matter at this size | Stop polishing this lever; test a bigger mechanism |
| Inconclusive, underpowered | No information | Do not claim "users don't care" |
| Win on average, loss for a segment (new users, feature phones, a language) | Design serves one group at another's expense | Segment-specific design or reject; never ship a known regression silently |
| Sample ratio mismatch flagged | Result untrustworthy | Do not interpret; often a variant broke or redirected for some users |

Keep design intent distinct from verified output: an experiment verifies the metric effect in the
tested population and period, not that the design is accessible, legible on every device, or
on-brand. Those need their own evidence.

## 6. Anti-patterns and corrections

- Testing a colour change on a low-traffic settings page. Correction: test a mechanism on a
  high-traffic step, or use qualitative methods.
- Calling the variant "B" in the design file. Correction: name it by hypothesis.
- Removing the help link in the variant to "reduce clutter". Correction: invariants stay.
- Declaring a pattern universal after one win. Correction: replicate or holdback before it enters
  the design system.
- Shipping the winner without its unfinished error and empty states. Correction: complete states
  before exposure.

## 7. Worked example (original)

A Kigali-and-Kampala bus-ticketing app tests a seat map against a seat list. The designer names the
variants "visual-seat-choice" and "fast-list", lists invariants (price breakdown, MTN MoMo and
Airtel Money options, English/Kinyarwanda/Luganda switcher), and discovers the seat map collides
with a live promotion-banner test on small screens; both are moved to the same layer. Variant QA
on a low-end Android shows the seat map takes 1.8 s to become interactive, so an INP guardrail is
added. Result: seat map wins overall, but loses for users on the Luganda locale because seat labels
truncate. The team fixes labels and re-runs for that segment before full rollout.

## Evidence/currentness

Access date 2026-09-24. Verified: WCAG 2.2 is the current W3C Recommendation (12 Dec 2024
edition); INP replaced FID as a Core Web Vital (web.dev, 2024) — thresholds are taken from the
engine's current performance-budget doctrine, not restated here. NOT_ASSESSED: any specific
product's device matrix and traffic.

Sources: Nassery (2025) *Next-Level A/B Testing*; Kohavi, Tang & Xu (2020) *Trustworthy Online
Controlled Experiments*; Rohrer (NN/g) landscape of UX research methods.
