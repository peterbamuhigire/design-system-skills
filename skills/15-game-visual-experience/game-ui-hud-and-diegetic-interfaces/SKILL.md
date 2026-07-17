---
name: game-ui-hud-and-diegetic-interfaces
description: Use when designing game HUDs, menus, maps, inventory, dialogue, tutorials, pause/settings, save/load, failure/success, controller focus, touch, couch-distance, or diegetic interfaces. Use ordinary app UI skills for non-game task flows.
metadata:
  portable: true
  category: 15-game-visual-experience
  compatible_with:
  - claude-code
  - codex
---

# Game UI, HUD, Menus, and Diegetic Interfaces

Design game information and control surfaces around player attention, pressure, world context, input mode, and viewing distance.

<!-- dual-compat-start -->
## Use When

- A game needs a HUD, reticle, objective, map, inventory, dialogue, tutorial, pause/settings, save/load, failure, success, or lobby surface.
- Information must work across exploration, combat, learning, cutscenes, couch distance, handheld touch, keyboard/mouse, or controller focus.
- Diegetic, spatial, contextual, minimal, or conventional HUD choices need an evidence-based decision.

## Do Not Use When

- The surface is a non-game app, dashboard, form, or website; use group 04 or 07.
- The task is the game’s overall route; use `game-visual-experience-orchestration`.
- The task is world/character/VFX art direction; use `game-art-direction-and-visual-development`.
- The task is timing, impact, camera, haptic or response tuning; use `game-feel-feedback-camera-and-haptics`.
- The task is general typography, colour, icons, motion, tokens, component states or handoff; pair with the existing owning skill.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Player questions, game states, verbs, failure/recovery and stopping flow | Product/SRS | yes | Defines information priority and timing |
| Platform, device, viewing distance and input matrix | Technical/support policy | yes | Governs layout, focus, touch and readability |
| Content, localisation, access, save, privacy and commercial rules | Accountable owners | yes | Exposes complete states and prohibited interruption |
| Representative build or prototype | Engineering | required for observed pass | Enables focus, legibility and pressure testing |

## Workflow

1. Inventory every state and the player’s immediate questions: what matters now, what can wait, and what must persist.
2. Choose world-only, diegetic, spatial, contextual, minimal HUD, conventional HUD, or a deliberate hybrid for each information class; record failure and fallback.
3. Build the attention hierarchy for calm, traversal, dialogue, combat, tutorial, failure, success, pause, save/load and interruption states. Keep critical threats and consequences redundant.
4. Specify every surface and transition, including map, inventory, objectives, dialogue, tutorial, settings, controls, accessibility, localisation expansion, safe areas, couch/handheld scale, controller focus and touch alternatives.
5. Pair with the existing owners for type pairing/licensing, accessible colour, iconography, component states, touch/haptics, motion, UX writing, internationalisation, tokens and engineering handoff.
6. Place ads or offers only at explicit, predictable genuine breaks after the requested action completes; define disclosure, decline/close, cap/pace, focus, no-fill/offline/error, data/consent and kill switch. Block interruption of gameplay, learning, narrative, saving, recovery, pause-to-stop, and exit.
7. Validate with real content, representative intensity, target input modes, devices/viewing distances and affected players. Preserve build identity, failures and unassessed matrix cells.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Information is continuous and survival-critical | Keep it persistent or immediately recoverable with redundant cues | Minimalism hides state the player must act on |
| Information is occasional and low urgency | Reveal contextually or on request | HUD clutter competes with world and action |
| Diegetic treatment reduces legibility or access | Add an equivalent non-diegetic presentation | Immersion becomes an exclusion mechanism |
| Controller, touch and keyboard/mouse share a surface | Preserve semantic intent with input-specific focus and prompts | One input model is bolted onto another |
| Ad state conflicts with play, recovery, stopping, child safety or privacy | Block or disable the placement | A commercial surface becomes intrusive or unsafe |

## Capability Contract

Read access to game states, content, platform/input rules and approved visual systems is required. Prototype/build inspection is required for a pass. Editing is limited to authorised design artefacts; implementation, participant contact, external SDK configuration, publication and production changes require separate authority.

## Degraded Mode

Without full states, real content, target devices or input support, provide a provisional information architecture and state matrix. Use a clear conventional fallback when diegetic presentation cannot be verified. Keep ads disabled when disclosure, child/privacy treatment, focus, failure or kill-switch behaviour is unknown.

## Anti-Patterns

- Mobile app navigation transplanted into a game. Fix: organise around play states, attention pressure and input continuity.
- HUD stripped for screenshots. Fix: test comprehension and survival before removing persistent information.
- Diegetic interface at any cost. Fix: provide readable, accessible non-diegetic equivalents.
- Tiny controller text or touch-first couch UI. Fix: validate at actual distance and target size with each input mode.
- Tutorial overlays that freeze, narrate and point at every control. Fix: teach one verb through safe action, then verify transfer.
- Ad between failure and retry or inside pause/exit. Fix: preserve recovery and stopping; use only a genuine post-completion break.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Game information-priority and surface map | Product, UI and narrative | Every state answers player questions at the right urgency |
| HUD/menu/diegetic specification | Engineering and QA | Layout, states, focus, inputs, content, access, localisation and failure paths are explicit |
| Interface evidence matrix | Release and SRS owners | Target devices, viewing distances, input modes, player tasks, failures and ad states are recorded |

## Examples

- `examples/exploration-to-pause-interface-spec.md` — a worked multi-state HUD/menu design with controller, touch, localisation, accessibility and ad interruption decisions.

## References

- `references/game-interface-method.md` — information classes, presentation choices, state matrix and validation contract.
- `../../04-web-and-ui-design/component-states-and-interaction-fidelity/SKILL.md` — control-state fidelity.
- `../../07-mobile-ios-android-cross-platform/touch-gesture-and-haptics/SKILL.md` — touch and gesture alternatives.
- `../../09-design-systems-tokens-and-theming/design-handoff-and-dev-spec/SKILL.md` — implementation handoff.
- `../../../doctrine/design-doctrine.md` and `../../../doctrine/references/wcag-2.2-criteria.md` — shared craft and access floors.
<!-- dual-compat-end -->
