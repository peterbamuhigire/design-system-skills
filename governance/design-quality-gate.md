# Design Quality Gate

Run before declaring any artifact with type, colour, or layout "done." Mirrors the finance
engine's quality-gate pattern. A failed item blocks shipment until fixed or explicitly waived
(with a recorded reason).

For a meaningful change, record the gate evidence in
`templates/design-delivery-evidence.md`. A checked box without a linked render, measurement,
inspection result, or explicit N/A reason is not evidence.

## Routing and scope

- [ ] The selected skill owns the requested decision; the closest neighbour was considered.
- [ ] Artefact, audience, surfaces, states, constraints, and acceptance conditions are named.
- [ ] Client, audience, primary job, environment, stakes, and success measure are named.
- [ ] One purpose-fit visual/experiential thesis and three authored decisions are recorded.
- [ ] Missing context that would materially change the design caused a stop or a qualified draft.

## Premium authorship and originality

- [ ] The design language is derived from the client's product, content, audience, and domain
      rather than copied from a reference product.
- [ ] References are translated into principles; no distinctive competitor composition, gradient,
      copy, illustration language, or interaction has been reproduced without a separate rights
      and strategy decision.
- [ ] The work has one memorable, defensible signature choice that improves recognition or use;
      decoration that does not serve the job has been removed.
- [ ] Real or representative content has been used to judge hierarchy, density, rhythm, and fit.
- [ ] A concrete demo, render, or implemented slice has been reviewed through refinement; a
      moodboard or static hero alone is not premium evidence.
- [ ] Premium judgement is separated from measurable checks: taste and authorship are human
      decisions, while accessibility, performance, responsiveness, and task outcomes are gates.

## Typography

- [ ] Typeface(s) **named and justified** in one line, stated *before* the artifact was produced.
- [ ] No banned AI-slop font as primary (`doctrine/references/ai-slop-banned-fonts.md`), incl.
      the secondary escapes and bare system stacks.
- [ ] A deliberate **display + body pairing** — not one font for everything.
- [ ] Type scale uses a real ratio (≥1.25), with obvious size jumps and weight extremes.
- [ ] Line-height follows the inverse rule (×1.6 under 32pt; ×1.3–1.1 above).
- [ ] Body text is not pure black; not wide-tracked.

## Licensing & embedding

- [ ] Licence permits the intended use, including embedding where applicable.
- [ ] Premium (Fontshare) files are embedded into the output only — never committed or shipped raw.
- [ ] Format-correct loading: woff2/@font-face (web), embed+subset (DOCX/PPTX), default-embed
      (PDF), name-reference or PDF-instead (XLSX).
- [ ] Fallback set *after* — never instead of — the chosen face.

## Colour & layout (when present)

- [ ] No generic default gradient / template look; palette intent stated.
- [ ] Sufficient contrast (text and UI) for accessibility.
- [ ] Consistent spacing rhythm on a single unit; grid respected.

## AI-slop freshness (when applicable)

- [ ] If the task depends on a current AI-slop definition, font ban, or visual tell, the
      `slop-doctrine-refresh-and-research-loop` was run or the current doctrine was explicitly
      accepted as fresh enough for the artifact's risk level.

## Mobile (when applicable)

- [ ] Platform conventions honoured (iOS HIG / Android Material), touch targets ≥ the platform
      minimum, safe areas / notch handled.

## Escalation

- [ ] If any gate cannot be met (no font file, no CDN, restrictive licence) the artifact was
      **not** silently downgraded — the limitation was stated and a decision requested.

## Release evidence

- [ ] All required states and target surfaces were inspected, not inferred from one happy path.
- [ ] Empty, loading, error, recovery, success, keyboard, touch, reduced-motion, and long-content
      states were inspected where applicable.
- [ ] Rendered or implemented output was compared with the approved design where tooling exists.
- [ ] Unverified checks, residual risks, waiver owner, and next action are recorded.
- [ ] The final verdict is `PASS`, `CONDITIONAL`, or `BLOCKED`; `CONDITIONAL` cannot be described
      as production-ready.
