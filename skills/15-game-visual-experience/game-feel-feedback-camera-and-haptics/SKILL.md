---
name: game-feel-feedback-camera-and-haptics
description: Use when tuning a game action through anticipation, response, impact, timing, animation, VFX, audio-visual coordination, camera, hit-stop, particles, haptics, reduced-motion, sensory alternatives, or intensity settings. Use micro-interactions-and-feedback for ordinary UI controls.
metadata:
  portable: true
  category: 15-game-visual-experience
  compatible_with:
  - claude-code
  - codex
---

# Game Feel, Feedback, Motion, Camera, and Haptics

Make player actions legible, responsive and satisfying through tunable, truthful feedback that preserves control, comfort and performance.

<!-- dual-compat-start -->
## Use When

- A movement, combat, traversal, interaction, puzzle or learning verb feels weak, unclear, delayed or overwhelming.
- Animation, VFX, audio, camera, time effects, particles and haptics must coordinate around player action and consequence.
- Camera motion, shake, zoom, hit-stop, aim assist feedback or sensory-intensity settings need a system.

## Do Not Use When

- The task is ordinary button/toggle feedback in a non-game UI; use `micro-interactions-and-feedback`.
- The task is product-wide non-game transition law; use `motion-design`.
- The task is HUD/menu information architecture; use `game-ui-hud-and-diegetic-interfaces`.
- The task is static visual pillars/assets; use `game-art-direction-and-visual-development`.
- The task is physics, animation, camera or VFX code; route the approved spec to software specialists.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Verb, input, state machine, authority, timing and failure model | Game design/engineering | yes | Prevents feedback from lying |
| Camera, animation, VFX, audio, haptic and performance constraints | Discipline owners | yes | Defines available channels and budgets |
| Cohorts, access needs, sensory risks and intensity policy | Product/accessibility | yes | Governs alternatives and comfort |
| Versioned prototype/build and target devices | Engineering/QA | required for tuning claims | Makes latency, frame and sensory evidence observable |

## Workflow

1. Select one verb and map anticipation, input recognition, start, continuous state, contact/commit, result, recovery, cancel and failure. Stop if the underlying rule or authority is ambiguous.
2. State the response target and feedback purpose for each phase: control confirmation, trajectory, danger, timing, impact, reward, error, recovery or learning explanation.
3. Allocate channels—pose/animation, VFX, world deformation, UI, audio, camera, time and haptic—by consequence. Keep at least one non-colour, non-audio and non-haptic path where meaning is critical.
4. Specify parameters rather than adjectives: delay, duration, curve, amplitude, frequency, falloff, radius, camera axis, shake envelope, time scale, particle count and cancel/recovery behaviour.
5. Provide intensity tiers and alternatives: off/reduced/default where appropriate, reduced motion, flash safety, stable horizon/reticle, camera-shake control, haptic-off, audio-caption and non-spatial feedback.
6. Test latency, control preservation, camera visibility, frame pacing, interruption, repeated exposure and interaction with HUD, narrative, learning, saving and stopping states on target devices.
7. Tune one variable set at a time, retain before/after build identity and failed variants, and use player-observed evidence for “satisfying,” “clear,” “comfortable,” or “fair” claims.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Feedback begins before authoritative result | Signal input/attempt, not success | The game lies about state or reward |
| Camera effect obscures aim, threat, landing or horizon | Reduce, relocate, stabilise or disable by setting | Spectacle removes control or causes discomfort |
| Many channels fire at once | Rank by gameplay consequence and remove redundant noise | Impact becomes sensory clutter |
| Meaning depends on motion, colour, sound or haptic alone | Add an equivalent channel and setting | Players miss critical state or cannot opt out |
| Build/device/player evidence is absent | Return a parameterised hypothesis and test plan | Taste is reported as measured game feel |

## Capability Contract

Read access to verb/state, build, device, access and discipline contracts is required. Editing is limited to authorised design/tuning artefacts. A runnable build and target-device capture are required for response/performance claims; participant testing, implementation and production mutation need separate authority.

## Degraded Mode

Without a build, provide a channel-and-parameter specification marked unverified. Without stable frame pacing or authority semantics, disable timing-sensitive polish and use clear immediate state cues. Without sensory evidence, default to lower intensity and preserve off/reduced controls.

## Anti-Patterns

- “Juice everything.” Fix: spend sensory intensity according to gameplay consequence and player choice.
- Camera shake as universal impact. Fix: protect targeting, horizon, navigation and an off/reduced setting.
- Success haptic or flourish before authority. Fix: distinguish attempt, pending, confirmed and rejected states.
- Hit-stop that steals control or breaks online authority. Fix: define scope, ownership, cancel and network-safe behaviour.
- Motion, colour, sound or haptic as the only critical cue. Fix: create redundant, configurable feedback.
- Tuning from memory across unlabelled builds. Fix: retain parameter sets, captures, devices, failures and player evidence.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Verb feedback and channel map | Animation, VFX, audio, camera, UI and engineering | Each phase has truthful purpose, owner, priority and alternative |
| Parameter/intensity specification | Implementers and accessibility | Default, reduced/off, interruption, recovery and budget values are testable |
| Tuning evidence log | QA, product and SRS | Build/device, parameters, captures, player observations, failures and residual risk are retained |

## Examples

- `examples/paddle-impact-feedback-spec.md` — a worked action-feedback specification with camera, VFX, audio, haptic, reduced-intensity and evidence decisions.

## References

- `references/game-feel-tuning-contract.md` — verb phases, channel priority, parameter schema and evidence method.
- `../../08-motion-and-interaction/motion-design/SKILL.md`, `../../08-motion-and-interaction/micro-interactions-and-feedback/SKILL.md`, and `../../07-mobile-ios-android-cross-platform/touch-gesture-and-haptics/SKILL.md` — shared motion, feedback and haptic doctrine.
- `../../../doctrine/references/wcag-2.2-criteria.md` — motion/flash/accessibility floor.
<!-- dual-compat-end -->
