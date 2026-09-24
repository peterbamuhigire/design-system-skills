---
name: fine-typesetting-and-typesetting-qa
description: Use when setting or checking the fine detail of running text in a report, proposal, business plan, deck, brochure or long page - hierarchy steps, rag, hyphenation, widows, orphans, figures, quotes, dashes and UK or East African punctuation. Use font-selection-and-pairing to choose faces and editorial-and-long-form-layout for measure and grid.
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
  - claude-code
  - codex
---

# Fine Typesetting and Typesetting QA
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

This skill owns the invisible craft layer: the decisions a reader feels but rarely names, and the
QA pass that proves a document was typeset rather than typed. It sits after typeface choice and
after the page grid, and before release of any DOCX, PDF, PPTX, brochure or long web page.

<!-- dual-compat-start -->
## Use When

- A proposal, business plan, annual report, tender response, brochure, case study or long web
  page is about to ship and must read as professionally typeset.
- Headings look loud or muddled and you need a disciplined hierarchy (one change per level).
- Paragraph shape is poor: ragged edges that zig-zag, rivers in justified text, stranded single
  words, hyphenation that breaks short words, or lines that end on "a", "is" or "it".
- Characters are wrong: straight quotes, primes used as apostrophes, hyphens used for ranges,
  fake fractions, lining figures in running prose, or US punctuation in a British document.
- A reviewer asks for a typesetting QA pass or a house-style punctuation check before release.

## Do Not Use When

- No typeface has been chosen yet - run `font-selection-and-pairing` first. This skill never
  chooses faces; it sets the chosen faces well.
- The task is measure, baseline grid, sidenotes, figures or reading landmarks on a web page -
  use `editorial-and-long-form-layout`.
- The task is building Word styles, TOC fields or document tags - use
  `docx-report-and-document-formatting`, which calls this skill for its QA pass.
- The task is hunting AI typography tells (banned faces, timid scale) across a product - use
  `ai-slop-typography-audit`.
- The copy itself needs rewriting for tone or clarity - route to the content owner; this skill
  may flag a bad break but does not rewrite meaning.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Rendered output or source file (DOCX, PDF, PPTX, HTML, InDesign/Affinity export) | Document owner | yes | QA is judged on rendered lines, not on styles alone |
| Chosen faces and their available styles and OpenType features | `font-selection-and-pairing` hand-off | yes | Family completeness and figure options depend on the font files |
| House style: spelling variant, quote style, dash style, number and date format | Client style guide or agency default | yes | Locale rules differ; one convention per document |
| Output medium and alignment (ragged or justified; print or screen) | Brief | yes | Hyphenation and rag rules change with alignment and measure |
| Languages present (English, Kiswahili, Luganda, French) | Brief | conditional | Accents, hyphenation dictionaries and French spacing rules |

## Workflow

1. **Confirm inputs and house style.** Record the spelling variant, quote style, dash style,
   number/date/currency format and alignment. Where the client has none, apply the agency default
   in `references/uk-east-african-punctuation-and-locale.md` and say so.
2. **Gate the family.** Check that the body face has true italics, a real bold and the weights the
   hierarchy needs. Reject faux (slanted) italics, synthesised bold, horizontally or vertically
   scaled type and filter effects on text. Stop and return to `font-selection-and-pairing` if the
   family cannot support the document.
3. **Set the hierarchy with one change per level.** Fix the body style, then change exactly one
   attribute (size, weight, colour or case) for each level above it. Use a different single
   attribute, or a clearly larger step of the same attribute, for further levels. See
   `references/fine-typesetting-rulebook.md` section 1.
4. **Set spacing.** Leading starts near 120 per cent of body size and is adjusted for x-height;
   keep it constant within a paragraph. Tracking of body text stays near zero and moves only to
   repair a bad break. Kern display lines by eye (rulebook section 3).
5. **Shape paragraphs.** Apply the rag, hyphenation, justification, widow/orphan and paragraph
   separation rules in rulebook section 4. Build them into paragraph styles, not manual fixes.
6. **Correct characters and punctuation.** Figures, quotes, apostrophes, primes, dashes,
   ellipses, fractions, accents, emphasis and spacing (rulebook section 5 and the locale file).
7. **Check legibility thresholds** for the medium: reversed small type, coloured small type,
   all-caps passages and projected sizes (rulebook section 6). Hand print ink questions to
   `print-production-and-finishing`.
8. **Run the typesetting QA pass** (rulebook section 7) on the rendered output. Log each finding
   with page/line, rule, fix and owner. Re-render after fixes; never mark a finding closed from
   the source file alone.
9. **Record and hand back.** Return the QA log, the house-style sheet used and any items blocked
   on the editor (for example a cut needed to remove a widow).

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Measure is short (under about 40 characters) and text is justified | Switch to ragged-right, or widen the measure | Rivers and stretched word spaces make the page look amateur |
| Ragged-right body on a normal measure | No hyphenation by default; allow it only for short measures with long words | Hyphen ladders down the right edge distract from reading |
| Hyphenation is on | Minimum word 7 characters, at least 4 before and 3 after the break, no more than 2 consecutive hyphens | Short words split ("wa-ter") and the reader stalls |
| A heading level differs from its neighbour in several attributes at once | Reduce to one attribute change per level | Hierarchy reads as noise and the document looks word-processed |
| Body face lacks a true italic or bold the text needs | Stop and choose another family or restructure emphasis | Faux styles print as distorted shapes and embarrass the client |
| Numbers sit in tables or financial columns | Tabular lining figures, decimal-aligned | Columns wobble and totals are hard to check |
| Numbers sit in running upper-and-lower-case prose and the face has oldstyle figures | Oldstyle (text) figures | Lining figures shout inside sentences |
| House style is absent for a Ugandan, Kenyan, Rwandan or Tanzanian client writing in English | Apply British conventions from the locale file and record the default | US punctuation inside a British-spelled document looks careless |
| Fix requires cutting or rewriting copy | Flag to the editor; do not rewrite meaning | Designer silently changes an approved claim |

## Capability Contract

- Read access to the rendered output and source is required. Rendering or exporting is required to
  claim any line-level fix; without it findings stay provisional.
- Editing styles and characters is allowed only under an implementation request. Copy changes
  beyond punctuation and spacing need the content owner's approval.
- No network access is needed except to confirm current CSS feature support (marked as a check).

## Degraded Mode

- Without a renderer, run the character, punctuation and style checks on the source and mark rag,
  widow and river checks `NOT_ASSESSED`.
- Without the font files, mark figure style and family completeness unverified and block print
  release until the fonts are inspected.
- Without a house style, apply the agency default and record the assumption as a conditional
  item for client confirmation.

## Anti-Patterns

- Changing typeface, size, weight, colour and case together for every heading - correct by changing
  one attribute per level.
- Slanting the roman to fake an italic or stroking text to fake bold - correct by using the
  family's true styles or choosing a complete family.
- Justifying text on a narrow column and leaving rivers - correct with ragged-right or a wider measure
  and tuned word-spacing limits.
- Fixing every bad break with manual line returns in the source - correct in paragraph styles so
  the fix survives edits and reflow.
- Straight typewriter quotes and hyphens for ranges throughout a premium proposal - correct with
  typographer's quotes, apostrophes and en dashes.
- Both indenting and spacing paragraphs, and indenting the first paragraph after a heading - correct
  by choosing one separation method and never indenting after a heading.
- Setting long passages in capitals for "impact" - correct with size or weight contrast; keep
  capitals for short labels with added tracking.
- Adopting a book's era-specific font advice (for example a system sans "for screens") - correct by
  routing every face choice through the engine catalogue and banned list.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Typesetting QA log | Document owner, designer, editor | Every finding has location, rule, fix and owner; closed only after re-render |
| House-style sheet (spelling, quotes, dashes, numbers, dates, currency) | Writers, editors, designers | One convention per document; defaults marked where the client had none |
| Paragraph and character style settings (hyphenation, justification, figures) | Document or web implementer | Settings live in styles, not manual overrides |
| Items blocked on the editor | Content owner | Each item states why a copy change is needed |

## Examples

- `examples/typesetting-qa-pass-worked.md` - a filled QA pass on two pages of a Kampala savings
  and credit co-operative annual report: before/after hierarchy, rag and punctuation fixes, and
  the house-style sheet.

## References

- `references/fine-typesetting-rulebook.md` - hierarchy, family gates, spacing, paragraph
  shape, characters, legibility thresholds and the QA checklist, with tool settings.
- `references/uk-east-african-punctuation-and-locale.md` - British and East African house-style
  defaults, French spacing for Rwanda, Burundi and DRC work, numbers, dates and currency.
- `doctrine/design-doctrine.md`; `doctrine/references/type-scale-and-spacing.md` (scale ratios);
  `doctrine/references/ai-slop-banned-fonts.md` (face choice is never taken from a source book).
- Siblings: `font-selection-and-pairing`, `variable-fonts-and-opentype-features` (figure and
  fraction features), `editorial-and-long-form-layout`, `docx-report-and-document-formatting`,
  `pdf-proposal-and-bankable-document-design`, `deck-system`, `print-production-and-finishing`.
- Sources (human design authority): Adams, S., Dawson, P., Foster, J. and Seddon, T. (2012,
  revised edition) *Graphic Design Rules: 365 Essential Design Dos and Don'ts*, Frances Lincoln;
  Bringhurst, R. *The Elements of Typographic Style*, Hartley and Marks; *New Hart's Rules*,
  Oxford University Press.
<!-- dual-compat-end -->
