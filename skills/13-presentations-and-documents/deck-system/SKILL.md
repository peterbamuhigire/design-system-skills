---
name: deck-system
description: Design and write a world-class presentation deck — pitch, strategy, campaign proposal, credentials, board/investor update, monthly/quarterly/annual review. Owns the shared deck-craft discipline (narrative arc, slide economy, one-idea-per-slide, builds, presenter notes, visual system) and routes to the right purpose via its variant examples. Use whenever a slide deck / pitch / presentation (PPTX, Google Slides, Canva, or rendered) is the deliverable.
status: active
metadata:
  portable: true
  category: 13-presentations-and-documents
  compatible_with:
    - claude-code
    - codex
---

# Deck System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When
- Building any presentation deck — pitch, strategy, campaign proposal, credentials, investor/board
  update, or monthly/quarterly/annual review.
- A slide deck (PPTX / Google Slides / Canva / rendered) is the deliverable or part of it.

## Do Not Use When
- The deliverable is a long-form DOCX report or PDF proposal → use `docx-report-and-document-formatting`
  / `pdf-proposal-and-bankable-document-design` (Phase 1).
- The need is the typographic/colour system itself → use groups 01 / 02 (this skill *applies* them).

## Required Inputs
- The deck's **purpose** (pick the matching `examples/variant-*`), audience, the single decision or
  action you want, the content/evidence, and the brand (or a deliberate type+colour choice).

## Workflow
1. **Pick the variant.** Match the purpose to an `examples/variant-*.md` (initial-pitch, strategy,
   ai-strategy-presentation, campaign-proposal, credentials, monthly-report, quarterly-review,
   annual-review) — each carries its slide list, tone, and length.
2. **State the typography + colour first** (anti-slop charter): a distinctive display + refined body
   from groups 01/02; never a banned font. State the choice and reason before building slides.
3. **Build the narrative** (`references/presentation-frameworks.md`, `pitch-psychology.md`,
   `storytelling.md`): conclusion-first (Minto/SCQA), one idea per slide, action titles (the title
   is the takeaway), evidence beneath, a clear ask.
4. **Apply slide economy** — ruthless cuts, real size/weight extremes for hierarchy, a consistent
   grid, builds only where they aid comprehension, no bullet soup.
5. **Design the data** — route exhibits to `chart-selection-and-encoding` / `data-visualization`.
6. **Write presenter craft** — speaker notes, transitions, the spoken arc; rehearse-ready.
7. **Run the gates** — anti-slop (no template look, no stock gradients), accessibility (contrast,
   legibility at room distance), and `design-qa-and-pre-launch-review`.

## Anti-Patterns
- One template reused unthinkingly for every purpose (the slop the old 8 deck-skills risked).
- Title = topic instead of takeaway; bullet soup; 6 ideas per slide.
- Decorative builds/transitions; stock-gradient title slides; banned fonts.

## Outputs
- A deck spec: chosen variant, stated type+colour, slide-by-slide narrative with action titles,
  exhibit plan, and presenter notes — ready to build in PPTX/Slides/Canva.

## Examples
- `examples/variant-*.md` — the 8 purpose-specific deck blueprints (slide lists, tone, length).
  These ARE the worked examples for this skill.

## References
- `references/presentation-frameworks.md`, `references/pitch-psychology.md`, `references/storytelling.md`.
- `doctrine/design-doctrine.md` (Mission, charter), `doctrine/references/ai-slop-banned-fonts.md`,
  `pairing-principles.md`, `type-scale-and-spacing.md`, `wcag-2.2-criteria.md` (legibility).
<!-- dual-compat-end -->
