# Worked example: design-engine and product improvement

## Baseline

Target: a game character-selection screen and the design-system route that produced it.
Evidence: desktop and mobile renders, grayscale render, keyboard traversal, contrast check,
asset brief, and current skill-tree validation.

Raw diagnostic score: 72/100.
Reported audit score: 65/100 (hard-capped).
Confidence: medium; controller and screen-reader evidence is not yet available.

## Finding and experiment

Finding: three character cards have equal visual weight and similar silhouettes, so role and
choice are difficult to distinguish at the intended camera distance.

Experiment: preserve the token system but vary silhouette, value grouping, pose direction, and
role cue in three thumbnail alternatives. Test recognition with five representative viewers and
keyboard focus states. Hypothesis: a clearer silhouette/value hierarchy will reduce role-selection
errors without increasing decoration or cognitive load.

Stop condition: if recognition does not improve or accessibility worsens, roll back to the prior
variant and select a different cue.

## Plan to 95/100

| Gap | Owner | Evidence | Acceptance |
|---|---|---|---|
| Missing far-distance readability | gesture-silhouette-and-story-composition | Grayscale thumbnails and viewer responses | Role identified at intended scale by at least 4 of 5 viewers |
| Missing keyboard and screen-reader proof | accessibility-wcag-2-2-compliance | Manual traversal and announcements | All choices reachable, named, and state-announced |
| No recorded standard | design-system maintainers | Reference update and routing test | New rule is linked from the owning skills and validator passes |
