# Data Storytelling And Case Patterns

Parent: [`data-visualization`](../SKILL.md).

Use this reference after the chart's question, data integrity, chart type, encoding, and accessibility
have been settled. It contains the narrative and common remediation patterns extracted from the
entrypoint for progressive disclosure.

## Tell A Story

### Why story works

- Stories engage emotion in ways facts cannot (McKee, HBR).
- Red Riding Hood test: 80–90% of adults recall the high-level story, illustrating story's memory power.
- Conventional bullet-point facts engage intellect; story can engage emotion and intellect together.

### Aristotle's three-act structure applied to data

| Act | Content | Data-presentation equivalent |
|---|---|---|
| Beginning (setup) | Setting, main character, imbalance, desired balance | Context: audience as hero, what changed, and what should happen |
| Middle (conflict) | Protagonist faces escalating challenges | Supporting data, comparison points, options, and recommendation benefits |
| End (resolution) | Climax and dramatic question answered | Clear call to action tied back to the beginning |

### Story construction questions

- What does the protagonist want to restore balance?
- What is the core need?
- What prevents them from achieving it?
- How would they act against the opposing forces?

### Conflict and tension

- A story where everything is rosy does not hold attention.
- Frame the work around the audience's real problem and stake.
- Duarte describes tension as the conflict between what is and what could be.

### Narrative order

- **Chronological:** take the audience through the analytical journey when process establishes
  credibility or matters to the decision.
- **Lead with the ending:** start with the action and then supply evidence when trust exists and the
  audience wants the “so what”.

Use the “Bing, Bang, Bongo” repetition framework:

1. Tell them what you will tell them.
2. Tell them.
3. Tell them what you told them, ending with the action.

### Spoken versus written narrative

- **Live:** keep the screen sparse so spoken explanation remains primary.
- **Written:** make the “so what” explicit on every section because the exhibit must stand alone.
- State the presentation structure up front.

### Four tactics for story clarity

1. **Horizontal logic:** slide or section titles alone tell the overarching story.
2. **Vertical logic:** title, visual, annotation, and text on one page reinforce the same claim.
3. **Reverse storyboarding:** list each finished page's main point and compare the sequence with the
   intended storyboard.
4. **Fresh perspective:** ask a reader without context to narrate what they see.

### Vonnegut's writing rules applied to data

1. Find a subject you care about.
2. Do not ramble.
3. Keep it simple.
4. Have the courage to cut.
5. Sound like yourself.
6. Say what you mean.
7. Treat readers as people who deserve a patient teacher.

## Case-Study Patterns

### Spaghetti graphs

1. Emphasise one line and mute the rest.
2. Separate series vertically as aligned small multiples.
3. Separate series horizontally with a common scale.
4. Separate and emphasise when both are needed.
5. Remove categories or periods that do not serve the question.

### Pie-chart alternatives

1. Use simple text when one or two values tell the story.
2. Use sorted bars for precise comparison.
3. Use a 100% stacked horizontal bar when part-to-whole remains necessary.
4. Use a slopegraph for change between two points.

### Animation for presentation and circulation

- For live presentation, reveal the graph progressively with simple appear/disappear builds.
- For circulation, provide one annotated visual containing the full evidence.
- Keep the final annotated state available for print and export.

### Preserve logical order

- Keep category order stable when telling several stories from one dataset.
- Reordering between views creates avoidable cognitive load.
- Change emphasis, not order, when shifting the story.
