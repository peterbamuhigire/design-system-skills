# Using Personas in Decisions: Primary Selection, Scope Arbitration and Scenario Honesty

Parent skill: [`../SKILL.md`](../SKILL.md) (`journey-mapping-and-service-design`).

**When to read:** after evidence-based personas exist (built per `journey-map-templates.md` §1)
and the team must decide *whose* experience a design is optimised for, settle "but what if a user
wants..." arguments, or write scenarios that drive design. This file covers using personas; it
does not replace building them from research.

---

## 1. Choosing the primary persona for a role

A product role (for example "merchant", "loan officer", "claims assessor") often has two to four
candidate personas. Designing for all of them equally produces an averaged user who matches no
one.

**Procedure**

1. List the candidate personas for the role, each with its top goals and context constraints.
2. For each candidate, ask: *if we design specifically for this persona, does the design still
   work acceptably for the others?*
3. The primary persona is the one whose design **at least works** for the others while a design
   aimed at any other would **fail** the primary. Usually this is the persona with the hardest
   constraints (lowest bandwidth, most interruptions, least training, highest stakes).
4. Name secondary personas and the minimum they need (a setting, a shortcut, an alternate path),
   and state who is deliberately not served.
5. Record the choice and its evidence in the design brief; revisit when research changes.

| Decision | Rule | Failure caused by the wrong choice |
|---|---|---|
| Several personas share a role | One primary per role, others served by additions | An averaged "composite" design that satisfies none |
| Two personas need incompatible layouts | Split the role (separate surfaces or modes) rather than compromise | A cluttered screen carrying both workflows |
| Evidence for the primary is thin | Label it a proto-persona and schedule validation before high-fidelity work | Confident design built on a fictional centre |
| The sponsor wants to design for "everyone" | Show the averaging failure on one screen and ask which user loses | Scope creep disguised as inclusiveness |

Accessibility is not an edge case to be traded away: disability, low literacy and low bandwidth
needs are requirements across every persona (see `doctrine/references/wcag-2.2-criteria.md`).

## 2. Arbitrating feature and edge-case arguments

Use the primary persona as the arbiter when a review stalls on hypothetical users.

1. Restate the proposal as "Does [primary persona] need this to achieve [goal] in [context]?"
2. If yes, with evidence, design it into the main path.
3. If only a secondary persona needs it, place it off the main path (settings, secondary action,
   assisted channel).
4. If no persona needs it and the only justification is "someone might", park it in the backlog
   with the question to research. Do not design for unnamed users.
5. If the "edge case" is a safety, legal, accessibility or financial-loss scenario, it is not
   optional: it becomes an error, recovery or guard state regardless of frequency.

A smaller group who find the product excellent is worth more than a large group who find it
merely tolerable; broadening the main path to cover every hypothetical dilutes it for the primary.

## 3. Writing scenarios that are honest

Scenarios turn a persona into design direction. Write them as short stories: a person, in a
situation, facing a problem, reaching (or failing to reach) an outcome.

1. Start from a real, observed frustration, with the setting and constraints that made it hard.
2. Write the current-state story first, ending in the actual failure.
3. Write the future-state story with the product, keeping the same constraints.
4. **Honesty check:** if everything goes smoothly, the network never drops, the user never
   hesitates, and the story ends perfectly, discard it and rewrite. Perfect stories describe the
   users we wish we had.
5. Include at least one complication (interruption, missing document, wrong entry) and show
   recovery.

## 4. Keeping personas in the room

- Designers substitute themselves for the user by default. Counter it by naming the persona in
  every review ("Would Aisha find this?"), not "the user".
- Keep the persona one or two pages; post the primary persona's name, context and top goal where
  the team works and at the top of each design review agenda.
- Any stakeholder may challenge a design by naming a persona goal it fails; the burden of proof
  then sits with the design.

## 5. Worked example (original): MTN MoMo merchant portal

Role: merchant using a web portal to view collections and request settlement. Candidates from
field research in Kampala and Mbarara: (A) a wholesale shop owner reconciling hundreds of small
payments nightly on a shared laptop; (B) a boutique owner checking a few payments on a phone
between customers; (C) a finance officer at a supermarket chain exporting statements.

Designing for C (exports, dense tables) fails B on a phone. Designing for A (fast reconciliation
of many small items, interruption-tolerant, works on a shared device) still works for B if the
mobile view leads with today's total and last five payments, and for C if export is a secondary
action. Primary: A. Secondary: B (mobile summary), C (export). Not served in this release:
multi-branch consolidation (backlog, with research question).

Arbitration in review: "What if a merchant wants to chart monthly trends?" Neither A nor B
reported it; C would use an export. Parked with a research question, not added to the dashboard.

## 6. Checks

- [ ] Each role has one named primary persona with recorded evidence and rationale.
- [ ] Secondary personas' minimum needs and the not-served group are stated.
- [ ] Every scenario includes a complication and recovery; none reads as frictionless.
- [ ] Hypothetical-user requests are resolved against a named persona or parked with a research
      question.
- [ ] Safety, legal, accessibility and loss scenarios are designed regardless of frequency.

---

**Evidence/currentness (accessed 2026-09-24):** method guidance only; no versioned standards or
statistics are claimed. WCAG 2.2 is the current W3C Recommendation (w3.org/TR/WCAG22).

Sources: Branson (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly
Experience*; Cooper, Reimann, Cronin and Noessel (2014) *About Face: The Essentials of Interaction
Design*; Synechron (2018) enterprise UX guidance for financial services and insurance.
