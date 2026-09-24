# Choosing a Design Lens: Efficiency, Cognition or Meaning

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-psychology`).

**When to read:** when a review stalls because people mean different things by "good design"
(one wants speed, another wants fewer errors, another wants the product to feel right), or when
turning a research source into design guidance for a specific surface.

## 1. Three lenses

| Lens | Question it answers | Evidence it trusts | Typical measure |
|---|---|---|---|
| Efficiency (engineering and human factors) | Can people get the work done quickly and without error? | Task analysis, error logs, time-on-task | Tasks completed, errors, time |
| Cognition (human information processing) | Does the design fit how people perceive, remember and decide? | Experiments and cognitive models (for example working-memory limits behind short menus) | Recall, recognition, decision time, load |
| Meaning (experiential or phenomenological) | What does using it mean to people socially, emotionally and culturally, including those at the margins? | Field study, interviews, observation of situated use | Themes, stories, whose experience is excluded |

The lenses are complementary. The meaning lens treats the few people who do not fit the pattern as
important signals, not noise.

## 2. Decision rules

| Surface or question | Lead lens | Also check with | Failure if the wrong lens leads |
|---|---|---|---|
| Back-office forms, ERP screens, POS checkout | Efficiency | Cognition (field grouping, error prevention) | "Delightful" flourishes slow cashiers at peak hours |
| Menus, navigation depth, dashboards, information density | Cognition | Efficiency | Overloaded menus and hidden options |
| Brand pages, landing pages, onboarding, moments of delight | Meaning | Cognition (legibility, load) | Efficient but forgettable, or culturally tone-deaf |
| Voice, avatars, characters, AI personas, imagery of people | Meaning | Efficiency (task success) | Stereotypes or exclusion baked into the product |
| Safety-critical alerts | Efficiency and cognition | Meaning (who is excluded or unsettled) | Missed alerts, or alerts that alienate some users |

## 3. Procedure for a disputed review

1. Ask each reviewer which question they are answering (section 1); write the lens beside each
   comment.
2. Decide the lead lens for this surface from section 2.
3. Resolve lead-lens comments first with its evidence; treat the other lenses as constraints.
4. Record any comment that shows a marginal group is excluded; it is never out of scope.

## 4. Example (original)

A Ugandan health ministry's SMS appointment reminder is reviewed three ways. Efficiency: shorten
the message and put date and time first; fewer missed appointments. Cognition: use the 12-hour
clock and the clinic's local name people already know. Meaning: the default voice line used a
male name and a formal register that some young mothers found intimidating; the team tests a
neutral sender name and friendlier wording with a small group before rollout. All three changes
ship; the efficiency measure (attendance) stays the lead success test.

Sources: Harrison, Tatar and Sengers (2007), "The Three Paradigms of HCI"; applied practice
discussed in Branson's UX/UI design guidance.
