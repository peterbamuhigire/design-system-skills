---
name: game-visual-experience-orchestration
description: Use when a game needs its player fantasy and interaction loop routed into HUD, art direction, feedback, camera, input, accessibility, testing, and engine handoff. Use ordinary app UI skills for non-game software and the four game specialists for focused craft.
metadata:
  portable: true
  category: 15-game-visual-experience
  compatible_with:
  - claude-code
  - codex
---

# Game Visual-Experience Orchestration

Translate a game’s player promise into a coherent, testable visual and interaction experience without duplicating implementation, documentation, or shared design doctrine.

<!-- dual-compat-start -->
## Use When

- A game or playable prototype needs an end-to-end visual-experience direction.
- Player fantasy, core loop, controls, HUD, world readability, feedback, camera, accessibility, art production, and handoff must reconcile.
- Mobile, PC, console, web, 2D, or 3D presentations need one evidence-gated route.
- A game project needs the correct specialist stack rather than generic app UI guidance.

## Do Not Use When

- The task is a non-game app or website; route to groups 04, 07, or 14.
- The task is only HUD/menu/interface craft; use `game-ui-hud-and-diegetic-interfaces`.
- The task is only visual-development and asset-system direction; use `game-art-direction-and-visual-development`.
- The task is only response, impact, camera, motion, VFX, or haptics; use `game-feel-feedback-camera-and-haptics`.
- The primary audience is children or a learning outcome is claimed; pair with `educational-and-childrens-game-experience`.
- Game mechanics, architecture, production implementation, or SRS authoring is the main work; route to the software or SRS engine.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Player promise, fantasy, cohorts, core loop, failure and stopping model | Product brief or approved SRS | yes | Defines what the experience must communicate |
| Platforms, devices, input modes, camera and performance budgets | Technical owner | yes | Constrains presentation and evidence |
| Art, UI, audio, narrative, culture, learning, safety and business hypotheses | Accountable owners | conditional | Exposes specialist gates and unresolved authority |
| Build identity and available test evidence | Engineering and QA | required for pass claims | Separates documentation from observed results |

## Workflow

1. State the player promise, minute-to-minute loop, desired feelings, stopping points, and player cohorts. Stop if these conflict or are only slogans.
2. Map every loop step to player question, required information, input, world or interface response, failure/recovery, accessibility alternative, and evidence class.
3. Route craft: interface to `game-ui-hud-and-diegetic-interfaces`; world/asset system to `game-art-direction-and-visual-development`; response/camera to `game-feel-feedback-camera-and-haptics`; age/learning to `educational-and-childrens-game-experience`.
4. Co-activate the existing owners for typography, colour/contrast, iconography, illustration, motion, touch/haptics, localisation, ethics, inclusive design, research, tokens, handoff, app-store assets, and pre-launch QA.
5. Reconcile priorities across calm and intense states, couch and handheld distance, input modes, localisation expansion, sensory settings, device budgets, and non-intrusive commercial surfaces.
6. Produce a route-and-gate map with named owners, artefacts, dependencies, evidence, failed paths, stop decisions, and downstream implementation/SRS links.
7. Test the representative loop in a versioned prototype or build. A document proves intent only; device, player, learning, cultural, and release claims require their matching evidence.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Player cannot answer the next-action question | Increase world or HUD signal priority before adding decoration | Visual richness conceals the playable verb |
| Screen information competes with the world fantasy | Prefer in-world, contextual, or progressive presentation where comprehension survives | Immersion or readability is sacrificed without evidence |
| Cohorts or platforms require conflicting treatments | Share semantic intent; specify platform/cohort adaptations | Pixel parity creates inaccessible or non-native play |
| Monetisation interrupts play, learning, narrative, saving, recovery, stopping, or exit | Block the placement and redesign it for explicit choice or a predictable genuine break | Revenue logic damages agency, trust, or safety |
| Required build/device/player evidence is missing | Return a conditional specification and test plan | Documentation is misreported as observed quality |

## Capability Contract

Read/search access to product, SRS, design, technical, cultural and evidence artefacts is required. Review is read-only by default. Editing is limited to authorised design artefacts; builds, publication, purchases, production mutation, participant contact and external approval require separate authority.

## Degraded Mode

Without a stable player promise or representative loop, stop detailed craft and return the conflicting decisions. Without a build, device, participant, cultural reviewer, or learning study, produce a specification and evidence plan marked `not assessed`; never issue a release or outcome pass.

## Anti-Patterns

- App dashboard dressed as a game HUD. Fix: start from player questions, world context, input pressure, and viewing distance.
- Art-first direction with no playable readability contract. Fix: trace every visual pillar to verbs, threats, affordances, and budgets.
- “Game feel” used as unmeasurable polish. Fix: specify trigger, response, timing, intensity, alternative, and test.
- Accessibility added after the look is locked. Fix: include access modes and redundant cues in the first representative slice.
- Retention or ads overriding voluntary play. Fix: pair commercial hypotheses with agency, stopping, wellbeing, privacy, child-safety, and trust gates.
- One shared platform forcing both games into the same identity. Fix: share capabilities and evidence formats while preserving game-specific expression.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Game visual-experience route map | Product, design and technical owners | Every experience concern has one owner, neighbour, dependency and decision |
| Loop-to-presentation matrix | Specialist designers and QA | Each loop step has signals, inputs, feedback, alternatives, budgets and evidence |
| Visual-experience gate report | SRS, implementation and release teams | Claims are labelled by evidence class; blockers, failed paths and unassessed checks remain visible |

## Examples

- `examples/river-crossing-route-map.md` — a worked route for a child-led river-crossing encounter, including HUD, art, feedback, learning, ads, evidence and stop decisions.

## References

- `references/orchestration-contract.md` — ownership boundaries, loop-to-presentation schema, evidence classes and gate order.
- `../../../doctrine/design-doctrine.md` — authored-choice, typography, anti-slop and cross-cutting rules.
- `../../../doctrine/references/wcag-2.2-criteria.md` — shared accessibility floor; game-specific access still needs gameplay evidence.
<!-- dual-compat-end -->
