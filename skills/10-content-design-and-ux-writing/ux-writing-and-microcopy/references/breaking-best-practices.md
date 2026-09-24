# Overriding a Writing Guideline

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-writing-and-microcopy`). Also cited by
`voice-tone-and-content-style-guide` and `error-empty-and-system-messaging`.

**When to read:** when a writing guideline (be concise, be scannable, avoid humour, front-load,
use sentence case) seems wrong for a particular screen or message, or when a stakeholder asks
why a rule was broken.

## 1. Inputs

- The guideline in question and where it comes from (style guide, heuristic, pattern library).
- The screen, the person's task and emotional state, and the business risk.
- Any evidence available: research notes, support tickets, test results, legal requirements.

## 2. Weigh the guideline's evidence

Guidelines rest on different kinds of evidence. The stronger the evidence behind a rule, the
stronger the case needed to break it.

| Evidence behind the rule | Strength | Example |
|---|---|---|
| Tested in this product with its users | Strongest | Short button labels raised completion in last quarter's test |
| Tested elsewhere and published | Strong, but check fit | Eye-tracking research on scanning |
| Trial and error by the team | Moderate | "Shorter errors got fewer support calls" |
| Common sense or practitioner consensus | Weakest | "Never use humour in errors" |

## 3. Decision rules

| Condition | Decision | Wrong-choice failure |
|---|---|---|
| The rule's assumption does not hold here (the "people scan" rule on a consent or loan-terms screen) | Override: write fuller copy that must be read | People agree to terms they did not understand |
| Following the rule harms the person (a rushed borrower needs to slow down) | Override: add explanation or a confirmation step | Speed is bought with harm and complaints |
| Following the rule harms the product or business (a missing reassurance line drives support calls) | Override with the business evidence | Cost moves from design to support |
| The rule clashes with the product voice (a youth brand's light line) | Override within the voice chart | Copy sounds like another brand |
| Accessibility, plain-language law or a regulator's wording applies | **Never override** | Exclusion or legal exposure |
| Only personal preference argues for the override | Keep the guideline | Inconsistency with no benefit |

## 4. Procedure

1. Name the guideline and its evidence strength (section 2).
2. Name the trigger from section 3 and the evidence for it.
3. Write the override copy; check it against the voice chart and accessibility rules.
4. Record: rule broken, trigger, evidence, owner and how success will be checked.
5. Review the record after the check; promote repeated overrides into the style guide.

Concise does not mean short: removing words must never remove the message the person needs.

## 5. Example (original)

A Kampala savings co-operative's app shows a single line, "Confirm loan", before disbursing a
loan. Support calls show members misunderstand the repayment schedule. The team overrides
"keep confirmations short": the screen now shows amount, fee, first repayment date and total to
repay in plain language, with the button "Confirm loan of UGX 800,000". Evidence: support
tickets; check: repayment-query calls over the next two months.

Sources: override triggers after Ben-David, *The Fundamentals of UX Writing*; evidence strength
and editing practice informed by Podmajersky, *Strategic Writing for UX*.
