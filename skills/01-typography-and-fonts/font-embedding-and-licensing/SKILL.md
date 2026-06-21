---
name: font-embedding-and-licensing
description: Use when loading or embedding a chosen font into a specific output — woff2 + @font-face for web, embed-with-subsetting for DOCX/PPTX, default embedding for PDF, name-reference for XLSX — and when verifying the licence permits that embedding. Ensures the artifact renders as designed everywhere without breaching redistribution terms.
status: active
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
    - claude-code
    - codex
---

# Font Embedding And Licensing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- A typeface is chosen and must now be loaded/embedded into a web page, DOCX, PPTX, PDF, or
  XLSX so it renders correctly on machines that lack it.
- Verifying that an embedding is licence-compliant before shipping a client deliverable.

## Do Not Use When

- No font has been chosen yet — use `font-selection-and-pairing` first.

## Required Inputs

- The chosen typeface(s) and their licence basis (from `premium-font-scan`).
- The output format(s) and whether the artifact is distributed externally.

## Workflow

1. **Confirm the licence** permits embedding for this format and distribution
   (`doctrine/references/licensing-and-embedding.md`). If not, fall back to an OFL alternative
   and state the substitution.
2. **Load per format** (`doctrine/references/embedding-by-format.md`):
   - **Web:** woff2 + `@font-face` (or Google Fonts link); variable font where available;
     fallback listed *after* the chosen face; `font-display: swap`.
   - **DOCX / PPTX:** apply by name, embed, **subset** ("characters used only").
   - **PDF:** ensure the generator embeds rather than referencing system fonts.
   - **XLSX:** apply by name; for pixel-perfect branded output, deliver as PDF instead.
3. **Set the fallback** as a safety net, never as the design.
4. **Verify** the rendered artifact shows the intended face (not a substitute) and report file-
   size impact for embedded documents.

## Anti-Patterns

- Embedding a font whose licence forbids redistribution.
- Shipping DOCX/PPTX without subsetting (bloat) or PDF that references system fonts (substitution).
- Treating the fallback as the design.

## Outputs

- The artifact with the chosen font correctly loaded/embedded, licence-verified, with fallback
  and (for documents) subsetting applied.

## References

- `doctrine/references/embedding-by-format.md`, `licensing-and-embedding.md`.
<!-- dual-compat-end -->
