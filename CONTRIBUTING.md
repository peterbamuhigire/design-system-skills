# Adding skills to design-system-skills (flawless auto-pickup)

This engine is **self-indexing**: consumers discover skills by globbing `skills/**/SKILL.md`
fresh and reading frontmatter. There is **no registry, index file, or router list to update.**
Adding a skill is one step.

## To add a skill

1. Copy `skills/_TEMPLATE/` to `skills/<NN-group>/<your-skill-name>/`.
2. Fill in the frontmatter — especially a **specific, trigger-rich `description`** (this is the
   only thing that decides whether the skill gets routed to; vague text = missed pickup).
3. Write the body (the `## Use When … ## References` sections). Cite `doctrine/references/*`
   for any canonical rule rather than restating it.
4. That's it. The next glob finds it — no edits to `README.md`, `CLAUDE.md`, the domain
   engines, or anything else.

## To add a new group

Create `skills/<NN-newgroup>/` and drop skills in it. It's discovered on the next glob. Add a
one-line row to the README router table only if you want the human-facing hint (optional — the
glob is authoritative).

## Premium fonts

Drop purchased font files into the matching `fonts/<group>/` folder (binaries are gitignored)
and record them in that group's `MANIFEST.md` (licence + embedding permission). The
`premium-font-scan` skill reads the MANIFEST automatically.

## Examples are mandatory (the convention)

Every **craft** skill (one that produces a design artifact) **MUST ship at least one file under
`examples/`** that demonstrates the skill's *output* — not more prose. Audit/process skills SHOULD
ship a worked example (a filled audit, a completed template). A craft skill without `examples/` is
**incomplete**.

A worked example is one of:
- a real applied **spec** (a full type scale with px/rem; a token JSON; an OKLCH colour ramp);
- a **before/after** (a slop version → the fixed version, with the reasoning);
- a **sample artifact** (a `@font-face` block; a component state matrix; a grid template; a deck
  outline; a DOCX style table);
- a worked **decision** (the stated typeface + colour + reason for a named brief).

Never use lorem/placeholder — examples must be specific and reusable. Track backfill in
`docs/plans/hardening-june/examples-backfill-tracker.md`.

## Rules every skill must follow

- Valid frontmatter (`name` + specific `description` + correct `metadata.category` = its group
  folder). Without it, pickup is unreliable.
- One concern per skill; name the sibling skill in `## Do Not Use When`.
- Never restate doctrine — cite `doctrine/references/*` (incl. `wcag-2.2-criteria.md` and
  `web-performance-budgets-2026.md` for any UI/web skill).
- Ship ≥1 `examples/` file (see above).
- Honour the anti-slop charter (`doctrine/design-doctrine.md`).
