# Design Quality Gate

Run before declaring any artifact with type, colour, or layout "done." Mirrors the finance
engine's quality-gate pattern. A failed item blocks shipment until fixed or explicitly waived
(with a recorded reason).

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

## Mobile (when applicable)

- [ ] Platform conventions honoured (iOS HIG / Android Material), touch targets ≥ the platform
      minimum, safe areas / notch handled.

## Escalation

- [ ] If any gate cannot be met (no font file, no CDN, restrictive licence) the artifact was
      **not** silently downgraded — the limitation was stated and a decision requested.
