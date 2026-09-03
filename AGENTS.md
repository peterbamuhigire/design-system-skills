# AGENTS.md — design-system-skills

## Universal agent integration

See `.skills-engine/engine-manifest.yaml` for the declarative contract used by the optional universal coordination package. The router and domain SKILL.md files remain authoritative.

The package may read the router, discover skills, inspect Git, and run only declared checks. Missing evidence is NOT ASSESSED; writes, pulls, publication, submissions, ledger/filing changes, deployment, or control changes require explicit approval.

## Mandatory Digital Research currentness gate for Kaizen

Every Kaizen audit, skill edit, reference update, validator change, and
standardisation decision MUST begin with the Digital Research Engine at
`C:\wamp64\www\digital-research-engine`. Read its `source-evaluation` and
`source-verification` skills and the currentness gate reference
`docs/continuous-improvement/kaizen-currentness-gate.md`.

Before admitting any standard, policy, law, technology, platform capability,
software version, command, security control, benchmark, or lifecycle claim,
record source scope, publication/version date, access date, freshness class,
review date, support status, and uncertainty. Use current authoritative
primary sources; quarantine stale/ambiguous/unsupported claims and mark them
`NOT_ASSESSED`. Books are durable concept inputs only.

The shared control plane is adapted to visual and document work in
[`docs/control-plane-adoption.md`](docs/control-plane-adoption.md); the central
registry is `C:\wamp64\www\skills-web-dev\docs\engine-control-plane.json`.

Cross-cutting design & typography engine. Compatible with Claude Code and Codex-style agents.
Mirror of the guidance in `CLAUDE.md`, kept for dual-compat tooling.

## Protocol

1. **Entry:** read `doctrine/design-doctrine.md`.
2. **Select:** glob `skills/**/SKILL.md` **fresh every time** and route by frontmatter
   `description` (the filesystem is the index — never a cached list; this is how new skills are
   picked up with zero registration). The README table is a hint only. Do not use a `Skill`
   tool — read the files directly.
3. **Apply:** follow the `doctrine/references/` rules the skill cites.
4. **Gate:** before declaring an artifact done, run `governance/design-quality-gate.md`.

For skill creation, normalisation, or review, also read
`governance/skill-authoring-standard.md`. Run the local validator and routing smoke test after
any skill, frontmatter, router, doctrine, or governance change.

## Hard rules

- No banned AI-slop fonts as primary type (`doctrine/references/ai-slop-banned-fonts.md`).
- Always state typeface + reason before producing output.
- Always pair (display + body); use weight/size extremes; check licence before embedding.
- On a new device or after pulling font-taxonomy changes, ensure the eight required
  `fonts/<category>/` directories exist before scanning or adding files. The category names are
  fixed team contract; individual font choices inside them may differ by device.
- Premium font binaries are gitignored — scan `fonts/<category>/`, read its `MANIFEST.md`, fall
  back to the named OFL baseline when a premium family is absent or its licence does not permit
  the intended use.

## Relationship to other engines

Referenced, not mirrored. Domain engines consult this one IN ADDITION to their own work for any
presentation-layer concern. See `integration/integration-plan.md`.

## Skill-engine release commands

For visual changes, validate the machine-readable delivery record with
`python -X utf8 scripts/validate_design_delivery_evidence.py tests/fixtures/design-delivery/manifest.json`;
missing renders or required checks block a `PASS` verdict.

```powershell
python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
```

The baseline is zero-debt: all 89 active skills currently pass the local contract. The validator
derives the active count from `skills/**/SKILL.md`; any new finding is a CI regression and must be
fixed before release.

When the sibling-engine workspace is available, also inspect declared external handoffs with
`python -X utf8 scripts/validate_cross_engine_routes.py --workspace-root <workspace-parent>`.
Missing sibling repositories are reported as `NOT ASSESSED`, not as a pass; the local route gate
remains independently runnable from this repository.

## PORTFOLIO CRAFT CONTRACT

Load `C:\wamp64\www\chwezi-engine-agents\docs\operations\portfolio-craft-standard-2026-09-04.md` when available. Design in perceptible slices: frame the user job and visual thesis, choose one component or flow, inspect the surrounding system and real content, make one purposeful change, render it in context, check hierarchy, states, contrast, motion, input, and responsive behaviour, refine, and record the visual proof. Every typeface, colour, spacing, asset, radius, shadow, and animation needs a product reason; remove decorative defaults. Do not generate a complete polished-looking system without reviewing its actual screens or artefacts. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing render, device, accessibility, content, or reviewer evidence is `NOT ASSESSED`, never a pass.
