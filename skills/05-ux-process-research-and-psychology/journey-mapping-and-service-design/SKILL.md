---
name: journey-mapping-and-service-design
description: Use when modelling a user's or customer's end-to-end experience across touchpoints and channels — building evidence-based personas, journey maps / experience maps, service blueprints (frontstage + backstage + support processes), Jobs-To-Be-Done (JTBD) statements, and alignment diagrams — and when turning that map into a ranked list of design opportunities. Routes here for "map the journey", "customer journey map", "experience map", "service blueprint", "frontstage/backstage", "JTBD", "jobs to be done", "persona", "where are the pain points", "alignment diagram", or "turn research into opportunities". Pick this when the unit of design is the *whole experience over time*, not a single screen.
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# Journey Mapping & Service Design

<!-- dual-compat-start -->
## Use When
- You need an **evidence-based persona** — a research-grounded archetype with goals, context, and jobs — not a demographic stock photo invented to justify a roadmap.
- You must map a user's or customer's **experience over time** across stages, touchpoints, and channels: a current-state journey map, a future-state map, or a broader **experience map** (organisation-agnostic, before a specific product exists).
- You are designing or fixing a **service**, not just a UI — you need a **service blueprint** that ties what the customer sees (frontstage) to the staff actions, systems, and processes that deliver it (backstage + support), separated by the **line of visibility**.
- You need to express what the customer is fundamentally trying to accomplish as **Jobs-To-Be-Done** ("when I ___, I want to ___, so I can ___") so the design serves the job, not the feature.
- You have research and a map and must produce an **alignment diagram** (research → map → opportunities) and a **ranked opportunity backlog** that the team can act on.

## Do Not Use When
- You are running the interviews, surveys, or usability tests that *feed* the map → use the sibling `ux-research-and-usability-testing` (that skill gathers the evidence; this skill structures it over time). The two pair — see Workflow steps 1 and 8.
- You are designing a single screen's structure, fidelity, or flow → use the sibling `wireframing-and-prototyping` (a wireflow is one touchpoint's mechanics; a journey map is the experience around it).
- You are applying cognitive/behavioural theory or heuristics to a design (biases, cognitive load, Gestalt, Nielsen) → use `ux-psychology`.
- You are defining the end-to-end product/discovery operating model, RACI, and rituals → use `enterprise-ux-process`.

## Required Inputs
- **The decision or problem the map must inform.** A map with no decision behind it is a poster. Name it: *which* journey, for *whom*, to resolve *what* (drop-off? a broken hand-off? a new service we are scoping?).
- **Evidence.** Research notes, interviews, support tickets, analytics funnels, frontline-staff input, complaint logs. Personas and emotion curves invented without evidence are slop (see Anti-Patterns).
- **The actor and the scope.** *Who* the journey belongs to (one persona, named), and the start/end boundary — where the journey begins (often before your product) and where it ends (often after).
- **For a blueprint:** the people, systems, channels, and back-office processes that deliver the service — including the parts the customer never sees.
- **The channels and touchpoints** in play (app, web, phone, in-person, SMS, third parties), because cross-channel seams are where experiences break.

## Workflow
1. **Anchor to a decision and a persona.** State the decision the map will inform and *whose* journey it is. Build the persona from evidence per `references/journey-map-templates.md` §Persona — goals, context, jobs, real quotes, and the research behind each. If you cannot cite evidence for a persona trait, mark it an assumption to validate (route to `ux-research-and-usability-testing`). No invented personas.
2. **Frame the Jobs-To-Be-Done.** Before mapping the *how*, state the *why* as JTBD: "When [situation], I want to [motivation], so I can [outcome]." The job is stable; the solution is not. Use `references/journey-map-templates.md` §JTBD. The journey then serves the job, so opportunities are judged by "does this advance the job", not "is this a nice feature".
3. **Choose the map type.** Journey map (one persona, one scenario, your service exists), experience map (broader, organisation-agnostic, problem space before a solution), or service blueprint (you must change *how the service is delivered*, not just the interface). `references/journey-map-templates.md` §Choosing the map names which to use when. Picking the wrong artifact is the most common waste.
4. **Lay the spine: stages and actions.** Break the journey into the actor's **stages** (their mental phases, named in their words — not your funnel), then the **actions/touchpoints** within each. Use representative content and real touchpoint names; never lorem, never generic "Awareness → Consideration → Decision" if the real journey isn't that.
5. **Add the experience layers.** For each stage capture: what they're **doing**, **thinking**, **feeling** (the emotion curve, justified by a quote or datapoint — not a decorative squiggle), the **touchpoint/channel**, and the **pain points & moments of truth**. An emotion curve with no evidence under each peak/trough is decoration; cite the source.
6. **For a service, blueprint it.** Add the swimlanes below the **line of interaction**: frontstage staff actions, the **line of visibility**, backstage staff actions, the **line of internal interaction**, and support processes/systems. Use `references/service-blueprint.md`. The value of a blueprint is precisely the backstage failure points the customer never sees but always feels — find them.
7. **Mark the seams and moments of truth.** Cross-channel hand-offs, waits, and ownership gaps (where no team owns the step) are where services fail. Flag each on the map. A blueprint that hides the hand-offs has skipped its only real job.
8. **Build the alignment diagram and rank opportunities.** Turn every pain point / unmet job into an opportunity, traced back to its evidence (research → map → opportunity — the alignment-diagram spine). Rank by **impact on the job × frequency × feasibility**. Use `references/journey-map-templates.md` §Opportunity backlog. An opportunity with no evidence behind it, or a pain point with no opportunity in front of it, is incomplete.
9. **Apply the doctrine lens.** A journey where the customer says "it felt generic / I didn't trust it / it looked like everyone else's" is a **slop signal** in experience form (`doctrine/design-doctrine.md` §0, `doctrine/references/ai-slop-taxonomy.md`) — the moat is the experience reading as *deliberately authored*. Escalate those troughs as design opportunities, not nuisance comments.
10. **Check accessibility and channel-equity coverage.** If the map assumes one happy channel and never models the keyboard-only, screen-reader, low-bandwidth, low-literacy, or offline-fallback path, state that as a known gap and pair with `doctrine/references/wcag-2.2-criteria.md` before claiming the journey "works for everyone".

## Anti-Patterns
- **The invented persona.** A stock-photo archetype with made-up demographics and a cute name, built to rationalise a decision already made. Personas not traceable to research are confirmation laundering.
- **The decorative emotion curve.** A smooth sad-to-happy squiggle with nothing under each peak/trough. If a low point has no quote, ticket, or metric beneath it, it is fiction.
- **Happy-path-only journeys.** Mapping only the smooth path and omitting errors, waits, recovery, and the channel switch — hiding exactly the moments where the experience breaks.
- **The wall-poster.** A beautiful laminated map with no decision, no owner, and no opportunity backlog. It gets framed and never changes anything (the experience-scale cousin of the shelved research deck).
- **Blueprint with no backstage.** A "service blueprint" that only redraws the frontstage screens and never models staff actions, systems, or the line of visibility — so the failures that live backstage stay invisible.
- **Stages in your words, not theirs.** Forcing the customer's lived experience into the company's funnel labels, which hides where their mental model and your process diverge.
- **Map as the deliverable.** Treating the artifact as the goal. The map is a means; the **ranked opportunities** are the output. No opportunities → unfinished.
- **One persona, one channel, one ability.** Mapping the median user on the best device and calling the service designed.

## Outputs
- One or more **evidence-based personas** (goals, context, JTBD, real quotes, traceable to research).
- A set of **JTBD statements** framing the journey by outcome, not feature.
- A **journey map / experience map**: stages (in the actor's words) × layers (doing / thinking / feeling / touchpoint / pain & moments of truth), with an evidence-justified emotion curve.
- Where a service is involved, a **service blueprint**: frontstage / line of visibility / backstage / support processes, with seams and failure points marked.
- An **alignment diagram + ranked opportunity backlog**: each opportunity traced to evidence and scored by impact × frequency × feasibility.

## Examples
- See `examples/journey-map-and-opportunities.md` — a worked, evidence-based current-state journey map for **Maduuka** (a B2B inventory app for small East-African retailers): the persona, the JTBD, the stage-by-stage map with an evidence-backed emotion curve, the cross-channel seams, and the ranked opportunity backlog traced back to research. Representative content throughout — never lorem.

## References
- `references/journey-map-templates.md` — the persona template, the JTBD format, the journey-vs-experience-map decision, the stage × layer map grid, the emotion-curve evidence rule, and the alignment-diagram / opportunity-backlog scoring model.
- `references/service-blueprint.md` — the blueprint swimlanes (frontstage, line of visibility, backstage, line of internal interaction, support processes), how to find backstage failure points, and how a blueprint differs from and extends a journey map.
- `doctrine/design-doctrine.md` — §0 Mission (the authored-not-templated moat) and §2 Anti-Slop Charter; an experience that "feels generic / untrustworthy" is a slop signal at journey scale.
- `doctrine/references/ai-slop-taxonomy.md` — the slop tells; map "felt generic / didn't trust it" troughs here and escalate them as opportunities.
- `doctrine/references/wcag-2.2-criteria.md` — accessibility/channel-equity gate; a single-channel, single-ability map is incomplete, not done.
- Sibling skills: `05-ux-process-research-and-psychology/ux-research-and-usability-testing` (gathers the evidence this map structures), `wireframing-and-prototyping` (the touchpoint mechanics within the journey), `ux-psychology` (theory behind the emotion curve), `enterprise-ux-process` (the surrounding operating model).
<!-- dual-compat-end -->
