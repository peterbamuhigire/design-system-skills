# Book Study 06 — MS Office productivity books (Word 2024, Advanced Excel, Excel 2019)

**Books:** *Microsoft Word 2024: The Most Updated and Complete Guide* (Charles Sherer);
*Advanced Excel for Productivity* (2016); *Excel 2019 Advanced Topics*.
**Studied against:** `skills/13-presentations-and-documents/docx-report-and-document-formatting/SKILL.md`
and the group-13 gap-list rows (#56 `xlsx-and-financial-model-presentation` P1, #58
`template-and-master-system-design` P2).
**Date:** 2026-06-21 · **Verdict headline:** these are **tool-mechanics how-to books, not
design-craft books** — mine the thin design-relevant seam, exclude the rest. CHANGE
`docx-report-and-document-formatting` only at the margins; **BUILD `xlsx-and-financial-model-presentation`
now (CONFIRM P1)** sourced from the *Advanced Excel* book's real strengths, NOT from the two
weak/dated others.

---

## (a) Genuinely DESIGN-relevant capabilities vs non-design mechanics to exclude

### WORD 2024 (Sherer)

**Design-relevant (but shallow):** three style types (paragraph/character/linked) + Modify-Style
+ Style Sets (Classic/Elegant/Fancy/Modern); Themes (theme colours, theme fonts = heading/body
pairs); templates (.dotx, Organizer copy-styles); **tables** (table styles, border/shading, text
direction, AutoFit, merge/split, picture-behind — its best-covered design topic); **page layout**
(margins, gutter, *mirror margins* for two-sided, **section breaks** Next/Continuous/Even/Odd,
orientation, page borders, page colour/gradient — genuinely useful for long-form structure);
headers/footers (galleries, per-section, Quick Parts building blocks); typography controls (line/
paragraph spacing, indents, multi-level lists); ornamental (drop caps, watermarks, text boxes,
cover pages).

**Critically — what the "2024" book is MISSING despite the title:** **no automatic Table of
Contents** (only the Navigation pane), **no captions/figure numbering**, and **no accessibility
at all** — no alt text, no Accessibility Checker, no screen-reader/semantic-heading guidance. It
also names **no genuinely-2024 feature** (no Aptos default, no Copilot/Designer, no Modern
Comments); it openly says Word is "essentially unchanged." The only "new" things it flags are
Focus Mode and the Editor pane (both pre-2024).

**Exclude as non-design mechanics:** mail merge, track-changes/comments, field codes/calculations,
macros/VBA, ribbon basics, file management, spelling/grammar/thesaurus/translation, find-replace,
bookmarks, forms, online video.

### ADVANCED EXCEL FOR PRODUCTIVITY (2016) — the one with real design seam

**Design-relevant and reasonably authoritative:**
- **Number formatting for exhibit-grade tables (its strongest section):** consistency as a
  professionalism signal; custom-format notation (`0` required vs `#` optional digit; units via
  `0 "cars"`; **three-part `positive;negative;zero`** masks; **parentheses + red for negatives**;
  leading-zero/zip special formats); date masks (`mmm yyyy`); **financial convention — `$` on the
  top row and totals only**, omitted on interior rows to cut visual noise.
- **Visual hierarchy via colour convention:** **blue font = hard-coded inputs/assumptions, black =
  formulas** (the standard model-readability tell); **Center Across Selection** instead of Merge
  (keeps navigation/copy intact); alignment, wrap via Alt+Enter, Group for collapsible clusters,
  **hide gridlines** for a cleaner exhibit, never hide rows (Lehman/Barclays cautionary tale).
- **Chart styling:** combo charts + secondary axis, legend/axis/title formatting, gap-width,
  distinct colour for actual-vs-projected, trendlines with R², **axis-integrity rules** (don't start
  Y above zero; avoid 3D as "weird and hard to read"; avoid stacked-line as "misleading"), paste
  formatting across charts for consistency, bubble charts.
- **Print/page layout for exhibits:** Page Break Preview, fit-to-page (with a readability caveat),
  margin trims, Center on Page, multi-block print areas, tab colour-coding.
- **Excel Tables** (Ctrl+T): banded shading, header filters, structured references (treated
  functionally more than as design).
- **Conditional formatting as encoding — but THIN:** only a colour-scale-on-a-sensitivity-table
  heatmap example + duplicate-highlight. **No data bars, no icon sets, no multi-rule guidance, no
  palette/colour-perception/accessibility.**

**Exclude:** formulas/functions, pivot tables, Power Query, macros/VBA, data validation,
what-if/Solver/Goal-Seek, lookups, financial calculation mechanics.

### EXCEL 2019 ADVANCED TOPICS — essentially design-irrelevant

Almost **zero** presentation content: charts deferred to "another book," conditional formatting is a
**glossary entry only**, table styles/themes are one sentence, **no** number-formatting / print-layout /
sparklines sections. It is a pure data-mechanics text (formulas, macros, what-if, pivots, import,
protection). **It adds nothing design-relevant the *Advanced Excel* book does not already cover
better.** Use it only to confirm what to exclude.

---

## (b) CRITICAL — version currency and design-vs-tooling

- **Word 2024:** mislabelled — content is ~2019-era, omits every real 2024/365 feature and, worse,
  omits TOC/captions/**accessibility**, which are exactly the things our DOCX skill treats as
  mandatory. **Net: weaker than our existing skill on the dimensions that matter.**
- **Advanced Excel (2016):** the *design-relevant* mechanics it covers (number-format syntax, chart
  formatting, print layout, model colour conventions) are **stable and still current** in 365 — the
  syntax has not changed. Its *gaps* (data bars, icon sets, sparklines, modern chart types,
  dynamic-array exhibits) are what must be supplemented from current docs.
- **Excel 2019:** dated *and* design-empty (no dynamic arrays, XLOOKUP, modern chart types, modern
  data types) — doubly unsuitable.
- **Design vs tooling, overall:** all three are **how-to-click books**. None teaches *why* — no
  hierarchy theory, no colour harmony, no typographic system, no accessibility rationale. They are
  useful as **mechanics references behind a design skill**, never as the design authority itself.
  Our doctrine remains the authority; these supply the button-level "how" for Excel exhibits.

---

## (c) ENGINE IMPACT

### 1. `docx-report-and-document-formatting` — CHANGE only at the margins (mostly REDUNDANT)

Our DOCX skill is **already stronger** than the Word book on every dimension the book covers, and
covers the three things the book omits entirely (real TOC from heading styles, numbered captions,
full WCAG tagging). So the book mostly **confirms** our skill by counter-example. Minor adds worth
folding in:

- **Mirror margins / gutter** for two-sided/bound print, and the **Even/Odd-page section-break**
  pattern for chapter-start parity — add a line to `references/docx-style-system.md` (the book's one
  genuinely useful, currently-unstated layout detail).
- **Building Blocks / Quick Parts** as the mechanism for reusable letterhead/header components — a
  one-line note, relevant to the future `template-and-master-system-design` (gap #58).
- Otherwise **REDUNDANT** — do not import the book's styles/themes/tables how-to; ours supersedes it.

### 2. `xlsx-and-financial-model-presentation` (gap #56, P1) — BUILD NOW (CONFIRM)

**Yes, build it now**, and source its *design* content from the **Advanced Excel** book's real
strengths plus current-doc supplements — explicitly **deferring all formula/pivot/model-calculation
mechanics elsewhere** (to a finance/engineering concern, per the Chwezi finance engine, not here).
The skill's DESIGN content:

- **Exhibit-grade number formatting:** custom masks, three-part positive;negative;zero, accounting
  parentheses + red negatives, `$`-on-first-and-total-rows convention, units-in-format, consistency
  as the professionalism rule.
- **Conditional formatting AS visual encoding:** color scales/heatmaps, **data bars, icon sets**
  (supplement the book's gap), when each encodes magnitude vs category vs threshold, paired with a
  legend, colour-blind-safe palettes (pull from group-12 data-viz + doctrine colour refs — the book
  is silent here).
- **Table & cell-style system:** named table styles, banded rows, the **blue-input/black-formula**
  colour convention, Center-Across-Selection over Merge, alignment/whitespace, **gridlines-off**
  exhibits, never-hide-rows.
- **Chart styling for exhibits:** combo/secondary-axis, axis-integrity (zero-baseline, no 3D, no
  stacked-line-as-trend), actual-vs-projected colour, sparklines (supplement), consistent formatting
  across a chart set.
- **Print/page layout for hand-out exhibits:** print area, fit-to-page with readability floor,
  Center-on-Page, headers/footers, tab colour-coding.
- **Anti-slop + accessibility tie-in:** tinted neutrals not pure grey, stated palette, contrast
  floors, no colour-only encoding — inherited from doctrine, which the books entirely lack.

This is a clean P1: a real gap (no spreadsheet skill exists), a credible source for the
*design* half, and a clean exclusion boundary (formula mechanics → finance engine).

### CONFIRM / CHANGE / REDUNDANT summary

- **CONFIRM (P1):** build `xlsx-and-financial-model-presentation` now — design content as above;
  formula/pivot/calculation mechanics explicitly deferred to the finance/engineering engine.
- **CHANGE (small):** `docx-report-and-document-formatting` gains mirror-margins/gutter + Even/Odd
  section-break note; Building-Blocks note toward the template-system skill.
- **REDUNDANT:** the Word book's styles/themes/tables how-to (ours is stronger); the entire **Excel
  2019** book; all formula/pivot/macro mechanics across all three.

---

## "extract-into" table

| From the books | Extract into | As what | Priority |
|---|---|---|---|
| Exhibit number-format syntax (3-part masks, accounting negatives, `$`-top/total convention) | **NEW** `xlsx-and-financial-model-presentation/references/number-formatting.md` | Number-format design reference | P1 |
| Conditional formatting as encoding (color scale) **+ supplement data bars/icon sets** | NEW xlsx skill — encoding section | Visual-encoding rules (book seed + current supplement) | P1 |
| Table/cell styles + blue-input/black-formula + Center-Across-Selection + gridlines-off | NEW xlsx skill — table/cell-style section | Exhibit table-design rules | P1 |
| Chart styling + axis-integrity (no 3D/stacked-line, zero baseline) + sparklines (supplement) | NEW xlsx skill — chart section (cross-ref group-12) | Spreadsheet chart-styling rules | P1 |
| Print/page-layout-for-exhibits (print area, fit-to-page, center-on-page, tab colour) | NEW xlsx skill — print/exhibit section | Print-ready exhibit rules | P1 |
| Mirror margins / gutter + Even/Odd section-break parity | `docx-report-and-document-formatting/references/docx-style-system.md` | Two-sided/bound layout note | P2 |
| Building Blocks / Quick Parts reusable components | toward `template-and-master-system-design` (gap #58) | Reusable-component note | P2 |
| Word styles/themes/tables/TOC/captions/a11y how-to | — | **EXCLUDE** — our DOCX skill already supersedes | — |
| All formula/pivot/macro/what-if mechanics; entire Excel 2019 book | — | **EXCLUDE** — non-design / finance-engine concern | — |
