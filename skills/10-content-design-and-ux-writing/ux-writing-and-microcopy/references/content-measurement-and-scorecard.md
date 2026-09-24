# Reviewing and Measuring Product Content

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-writing-and-microcopy`). Also used by
`voice-tone-and-content-style-guide` and `heuristic-evaluation-and-design-critique`.

**When to read:** when reviewing product copy against a rubric, choosing how to measure whether
copy works, or setting quality criteria for generated or dynamic content. Detection of generic
machine prose routes to the digital-research engine's writing skills.

## 1. Content review rubric (score each screen or message 0-2 per row)

Weight clarity and usability rows about twice as heavily as voice rows.

| Row | Question | Trace a failure to |
|---|---|---|
| Accessible | Readable, labelled, announced correctly, works at 200 per cent zoom? | WCAG 2.2 success criterion |
| Purposeful | Does every sentence help the person's task and the product goal? | Task analysis |
| Concise | Is anything there that does not help? (Concise is not the same as short.) | Editing pass |
| Conversational | Natural turn-taking in the person's words, not system terms? | Heuristic: match the real world |
| Clear | One meaning; terms consistent with the terminology list? | Heuristic: consistency |
| Voice | Matches each row of the product's voice chart? | `voice-tone-and-content-style-guide` |

A screen passes with no zero in an accessibility or clarity row and an overall weighted score of
at least three-quarters of the maximum. Record each failure with its trace so the fix is specific.

## 2. Choosing a measure

| Question | Method | Example measure |
|---|---|---|
| Which wording performs better? | Experiment (A/B) | Completion rate of the step |
| Why do people hesitate here? | Usability research | Observed confusion, paraphrased quotes |
| Is this obviously wrong? | Heuristic review | Rubric scores (section 1) |
| Does content help over time? | Product analytics | Onboarding pace, task completion, retention, repeat use, referrals, support-contact reduction |

Frame measures by goal, signal and metric (for example goal "members understand repayments",
signal "fewer repayment questions", metric "repayment-query contacts per 1,000 loans").

**Ethics check:** a metric that becomes a target can be gamed. Before optimising engagement ask
"how much is too much?" and do not write copy designed to drive compulsive use.

## 3. Generated and dynamic content

1. Define the problem the generated content solves and who is accountable for it.
2. Define "good": experts review a sample and write attributes of good, acceptable and
   unacceptable output.
3. Plan ethics, review duties and escalation.
4. Write prompts and templates; generate a test set.
5. Score the test set against the attributes; align and iterate; integrate with monitoring.

Quality attributes for generated content: helpful, accurate, harmless, auditable (you can trace
why it said what it said) and economical (shorter output costs less compute). Organise the
practice as principles, personality, patterns and practicalities.

## 4. Example (original)

A Nairobi pharmacy chain reviews its SMS refill reminders. Rubric: "Clear" scores zero because
"Rx due" is pharmacy jargon; "Accessible" scores one because the link text is a bare URL. Fix:
"Your blood-pressure tablets run out on Friday. Reply 1 to reserve a refill." Measure: refill
reservations per 100 reminders over six weeks, with opt-out rate as the guard metric.

Sources: rubric after Podmajersky, *Strategic Writing for UX* (content scorecard, generated-content
tenets, practice structure); usability heuristics after Nielsen; goal-signal-metric framing after
Rodden, Hutchinson and Fu's HEART framework (Google, 2010); Goodhart's law.
