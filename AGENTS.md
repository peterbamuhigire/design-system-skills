# AGENTS.md — design-system-skills

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

## Hard rules

- No banned AI-slop fonts as primary type (`doctrine/references/ai-slop-banned-fonts.md`).
- Always state typeface + reason before producing output.
- Always pair (display + body); use weight/size extremes; check licence before embedding.
- Premium font binaries are gitignored — scan `fonts/<group>/`, read its `MANIFEST.md`, fall
  back to the named OFL baseline when a premium family is absent or its licence does not permit
  the intended use.

## Relationship to other engines

Referenced, not mirrored. Domain engines consult this one IN ADDITION to their own work for any
presentation-layer concern. See `integration/integration-plan.md`.
