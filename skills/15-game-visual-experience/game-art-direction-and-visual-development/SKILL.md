---
name: game-art-direction-and-visual-development
description: Use when a game needs visual pillars, shape language, colour scripting, character/world readability, cultural motif governance, 2D/3D cohesion, VFX hierarchy, an asset bible, style scalability, performance-aware art, or engine handoff. Use illustration-style-and-systems for non-game illustration sets.
metadata:
  portable: true
  category: 15-game-visual-experience
  compatible_with:
  - claude-code
  - codex
---

# Game Art Direction and Visual-Development Systems

Turn the player fantasy into an authored, scalable visual system whose world, characters, assets and effects remain readable, culturally accountable and producible.

<!-- dual-compat-start -->
## Use When

- A game needs visual pillars, mood, shape language, colour script, world/character rules, material/lighting treatment, VFX hierarchy, asset bible, or style guide.
- 2D and 3D elements, UI and world art, characters and environments, or several vendors must form one coherent system.
- Art style must scale across content throughput, device budgets, store assets and localisation.

## Do Not Use When

- The task is a brand illustration set or one expressive image; use `illustration-style-and-systems` or `ai-image-generation-art-direction`.
- The task is functional game HUD/menu design; use `game-ui-hud-and-diegetic-interfaces`.
- The task is response timing, camera motion or haptic impact; use `game-feel-feedback-camera-and-haptics`.
- The task is 3D modelling, rendering, VFX implementation or engine optimisation; route to software specialists after this craft contract.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Player fantasy, themes, loop, narrative and gameplay readability needs | Product/SRS | yes | Anchors the visual system to play |
| Cultural/historical fact, fiction, consultation, permission and rights ledger | Research and accountable owners | conditional | Prevents unapproved appropriation or false authority |
| Platforms, cameras, performance budgets, content volume and team capability | Technical/production | yes | Makes the style scalable |
| Existing assets, brand/IP rules and store deliverables | Owners | conditional | Exposes reuse, rights and continuity constraints |

## Workflow

1. State three to five visual pillars as observable choices linked to player fantasy, verbs, emotions and exclusions; reject mood-board adjectives without operational meaning.
2. Establish gameplay readability: silhouettes, faction/role cues, affordances, threat hierarchy, navigation landmarks, value grouping and camera-distance checks.
3. Define shape, line, proportion, perspective, colour-role, lighting/material, texture/finish, animation and VFX hierarchy across characters, world, props and UI-world seams.
4. Create a colour script for emotional and gameplay progression while delegating palette construction and contrast verification to existing colour skills.
5. Separate historical/cultural fact, fiction and inspiration; record motif meaning, source, permitted use, named reviewer/rights owner, disagreement and unapproved treatments. Research alone is not permission.
6. Prove a representative asset ladder at near/far, calm/intense, 2D/3D and target-device budgets. Define LOD/simplification, reuse, variants, naming, source files and export/handoff.
7. Gate the asset bible and vendor briefs with originality, licence, cultural, accessibility, performance, cohesion and store-crop tests. Preserve rejected explorations and reasons.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| A style choice does not improve fantasy, readability or identity | Remove or narrow it | Ornament increases cost without player value |
| Cultural meaning or permission is unresolved | Quarantine the motif and request accountable review | Research is misrepresented as cultural authority |
| Detail fails at gameplay distance or target device | Simplify silhouette, value or material hierarchy | Showcase art becomes unreadable or unshippable |
| UI, VFX and world cues compete | Reserve channel, value, colour and motion priority by gameplay consequence | Every subsystem shouts and the player misses danger |
| Shared platform asset would erase a game’s identity | Share pipeline/schema, not the expressive asset | Reuse turns distinct IP into a generic skin |

## Capability Contract

Read/search access to approved product, cultural, rights, performance and asset sources is required. Editing/generation is limited to authorised visual artefacts. Do not assert cultural approval, licence clearance, performance, build integration or store acceptance without the accountable evidence.

## Degraded Mode

Without consultation/permission, use neutral placeholders and quarantine meaning-bearing motifs. Without target-device renders, provide a provisional asset bible and mark scalability/performance unverified. Without source files or rights, block production reuse and record the gap.

## Anti-Patterns

- Mood board as an art bible. Fix: define repeatable rules, boundaries, assets, tests and owners.
- Surface motifs copied without meaning or permission. Fix: maintain fact/fiction/consultation/rights records and accountable review.
- Portfolio detail at gameplay distance. Fix: test silhouette, value and effects in representative camera/build conditions.
- Every effect uses maximum brightness, size and motion. Fix: rank VFX channels by gameplay consequence.
- Mixed 2D/3D finish without a seam rule. Fix: define shared perspective, light, material, contour and compositing logic.
- Reuse confused with sameness. Fix: reuse pipelines and primitives while preserving game-specific pillars and authored assets.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Visual pillars and development bible | Art, narrative, UI and production | Rules are observable, reproducible and linked to gameplay |
| Asset/VFX hierarchy and scalability contract | Technical art, engineering and vendors | Representative assets pass distance, cohesion, budget and source-file checks |
| Cultural, rights and originality decision log | Accountable reviewers and release | Fact, fiction, permission, rights, disagreement and quarantine are explicit |

## Examples

- `examples/kitara-night-market-art-bible-slice.md` — a worked art-bible slice with pillars, readability, cultural quarantine, asset ladder and handoff.

## References

- `references/game-art-system.md` — pillar, readability, colour-script, asset-bible, VFX and cultural-control schemas.
- `../../11-imagery-illustration-and-art-direction/illustration-style-and-systems/SKILL.md` and `../../11-imagery-illustration-and-art-direction/iconography-system-design/SKILL.md` — neighbour craft owners.
- `../../../doctrine/design-doctrine.md` — authored visual choices, typography and anti-slop rules.
<!-- dual-compat-end -->
