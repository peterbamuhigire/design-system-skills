# Book-informed design-system engineering synthesis

Status: adopted on 2026-09-14 after inspecting the supplied original books.

## Practices to standardise

### Keep one authored source of truth

Store design decisions in a versioned, reviewable token source. Generate
platform outputs from it; do not maintain competing hand-edited CSS, JavaScript,
design-file, and documentation copies. Each token should have a stable name,
type, description, semantic purpose, and ownership where that information
changes adoption or safe evolution.

Use three layers deliberately:

1. primitives for raw values;
2. semantic tokens for roles such as surface, text, border, focus, and action;
3. component tokens for component-specific decisions and states.

Aliases and semantic mappings should express intent, not conceal arbitrary
values. Record transformations, supported platforms, generated-file ownership,
and the compatibility/deprecation path for changed tokens.

### Design the component contract around scenarios and states

For each reusable component, document the intended user jobs, variants,
responsive behaviour, interaction states, validation/error behaviour,
accessibility semantics, content constraints, and implementation boundaries.
Use a state matrix rather than relying on a screenshot of the happy path.
Include loading, empty, disabled, focus-visible, error, success, overflow,
long-content, and interruption states when relevant.

### Make adoption measurable

Track whether consuming products use the official tokens, components, docs,
and generated packages; whether exceptions are recorded; and whether users can
complete the relevant scenario with acceptable accessibility and performance.
An adoption scorecard should identify the owner, sample, baseline, target,
review date, and corrective action. Visual fidelity alone is not adoption.

### Handoff behaviour, not only appearance

Design handoff must connect component intent to tokens, DOM semantics,
interaction rules, content, responsive constraints, and testable acceptance.
If a behaviour is not demonstrated or verified, mark it unassessed rather than
implied by a static mock-up.

## Deliberate exclusions

- The book's example typography is not imported; this engine's typeface
  constraints and project context remain authoritative.
- A token file format is not treated as a W3C Standard merely because a
  community specification exists. Use the current official status when
  selecting an interchange format.
- Tool-specific workflows are optional adapters, not the design-system
  contract.

## Sources

- Michael Mangialardi, Design Systems for Developers: Learn How to Code Design
  Systems That Scale.
- Drew Hoskins, The Product-Minded Engineer.
- Adrienne Braganza, Looks Good to Me: Constructive Code Reviews.

## Currentness note

The W3C Design Tokens Community Group's 2025.10 report describes a JSON
interchange format but explicitly states it is not a W3C Standard. Treat that
status as a verification point, not a marketing claim:
https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
