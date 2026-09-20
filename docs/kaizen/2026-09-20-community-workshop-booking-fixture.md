# Community workshop booking fixture

Status: implementation fixture for the six-book Kaizen wave
Purpose: provide one bounded product slice that exercises requirements, inclusive components, visual hierarchy, usability testing, data storytelling, tokens, and design-system adoption together.

## Brief

Audience: a community-program coordinator booking a room and reviewing attendance capacity.
User job: find an available workshop slot, reserve it, recover from validation or network failure, and understand current capacity.
Business outcome: reduce booking errors and make operational capacity visible without requiring training.
Primary decision: can the coordinator confidently submit a valid reservation?
Secondary decision: which slot or workshop needs operational attention?

## Required state and event matrix

| Area | Normal | Alternative | Failure | Recovery | Evidence |
|---|---|---|---|---|---|
| Search/filter | matching slots | no filters / long names | no results | clear filters | keyboard, narrow width, empty-state copy |
| Booking form | valid date, time, attendees | optional notes | invalid capacity, network failure | preserve input, focus first error, retry | semantic fields, labels, live status |
| Confirmation | reservation summary | edit before submit | duplicate or stale slot | return to form with preserved values | focus placement, status announcement |
| Capacity view | comparison by slot | partial data | missing or delayed data | show last-updated context | chart decision, text alternative |
| Responsive layout | desktop | narrow/mobile | overflow or clipped actions | linearized reading/order | visual render and keyboard traversal |
| Motion | state transition | reduced-motion preference | unsolicited movement | static equivalent | reduced-motion evidence |

## Visual and interaction decisions

- Start with structure and hierarchy in grayscale; add semantic colour only after the primary booking action, errors, and secondary metadata are legible.
- Use semantic token roles for action, danger, focus, surface, and radius; component styles must not bypass semantic roles without a recorded reason.
- Keep the form's primary action visually dominant while preserving a distinct cancel/destructive treatment.
- Keep essential help in the page or field context, not only in a tooltip.
- Use native controls where they satisfy the task; add custom behavior only when the requirement and evidence justify it.
- Make empty, loading, success, error, and recovery states first-class content.

## Usability test card

Research question: where does a coordinator hesitate or make an error while reserving a slot?

Recruitment: three to five people who have performed event or room scheduling, or a documented proxy when direct access is unavailable.

Neutral task: “You need to reserve a room for the next community workshop for 18 attendees. Find a suitable slot, submit the booking, and tell us what you would do if the slot became unavailable.”

Observe: first interpretation, control discovery, hesitation, invalid input, recovery strategy, confidence, and whether the confirmation communicates the outcome.

Facilitation constraints: do not explain the intended control, do not correct the participant during the task, obtain consent before recording, and separate observed facts from interpretation.

Fix/retest rule: fix the smallest high-impact issue, repeat the same task, and report directional evidence. Do not claim statistical improvement from this sample.

## Capacity chart card

Decision: which workshop slot should the coordinator investigate first?

Big Idea: one slot is approaching capacity while the remaining slots have materially more room.

Encoding: position/length for capacity comparison, restrained colour only to highlight the attention-worthy slot, direct labels, last-updated context, and a text summary that carries the same decision.

Declutter pass: remove decorative marks, redundant legends, unnecessary precision, and gridlines that do not support the comparison.

Acceptance: an independent reviewer can state the highlighted slot and the reason for attention without reading a separate legend.

## Design-system extraction

Candidate patterns: field group, validation message, status/live region, empty state, confirmation summary, capacity comparison, primary/secondary/destructive action roles.

Extraction rule: promote a pattern only when the fixture or a second real consumer demonstrates stable structure, meaningful variation, and a maintenance owner. Record rejected abstractions rather than forcing reuse.

Consumer proof: render the fixture from the token example, validate the evidence manifest, exercise update and rollback behavior, and record the consumer's changed dependency/version.

## Acceptance gate

This fixture is not release-ready until it has:

1. a completed problem/outcome brief;
2. a state/content matrix;
3. semantic, keyboard, responsive, and reduced-motion evidence;
4. a token-to-render trace;
5. a usability observation and fix/retest record, or an explicit NOT_ASSESSED result;
6. a chart decision and text alternative;
7. an independent review;
8. retained evidence references with integrity checks; and
9. a dated owner and rollback path.
