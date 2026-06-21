# Reference: Exhibit & Print Layout — turning a worksheet into a hand-out exhibit

How to lay an `.xlsx` sheet out so it prints (or exports to PDF) as a clean board/lender hand-out,
not a worksheet screenshot. Presentation only — page setup, print area, fit/legibility, headers,
greyscale survival, tab navigation. Authority: `doctrine/design-doctrine.md` and
`doctrine/references/wcag-2.2-criteria.md`. Print-for-exhibit seam sourced from *Advanced Excel for
Productivity* (2016).

---

## 1. Decide the exhibit footprint first

- **Medium sets the format:** a one-page board exhibit (often **A4/Letter landscape**) vs a
  multi-page appendix (portrait, repeating headers) vs an on-screen-only review (no print layout
  needed). State it before formatting — it drives orientation, decimals, and density.
- **One idea per printed page.** If the sheet carries two stories, split into two print areas /
  two exhibits. A printed exhibit the reader must rotate or squint at has failed.

## 2. Print area & page-break control

- **Set an explicit Print Area** (Page Layout → Print Area → Set) — never rely on Excel's "used
  range", which drags empty formatted cells into the print.
- **Page Break Preview** (View) to see and drag breaks; insert manual breaks so a block never splits
  mid-table. For multiple non-contiguous blocks, select them and set a multi-area print area (each
  prints on its own page).
- **Repeating header rows/columns:** Page Layout → Print Titles → "Rows to repeat at top" (and
  "Columns to repeat at left") so every printed page of a long table carries the header and the row
  labels. (This is the print analogue of a frozen header.)

## 3. Scale to fit — with a legibility floor

- Fit-to-page is fine **only down to a legibility floor**: keep the effective printed text **≥ ~8 pt**
  (≈ 90–100% scale for a normal sheet). Below that, **do not shrink further** — instead:
  - reduce columns (hide-for-print via a print-only summary, or remove non-essential detail),
  - split across pages with repeating headers, or
  - switch to landscape / a larger trim.
- Prefer **"Fit all columns on one page"** (width = 1 page, height = automatic) for wide schedules,
  rather than "fit sheet on one page", which crushes a long sheet illegibly.
- Avoid Excel's automatic scaling surprising you — set the scale explicitly and check Print Preview.

## 4. Centre, margins, and the page frame

- **Centre on page** horizontally (Page Setup → Margins → "Horizontally") so the exhibit sits
  framed, not jammed to the top-left. Centre vertically only for a short one-pager.
- **Trim margins** modestly (e.g. 0.5–0.7 in) to give the table room, but keep a clear white frame —
  margins stay free of data (the doctrine white-space rule).
- **Gridlines off in print** (Page Layout → Sheet Options → Print: uncheck Gridlines) unless the
  table genuinely needs them; rely on your deliberate hairline rules instead.

## 5. Header / footer = the exhibit's metadata

Set a real header/footer (Page Layout → Print Titles → Header/Footer) carrying:

- **Header:** the **exhibit/title** ("Exhibit 3 — FY2026 KPI Summary") and the **entity**; optionally
  a logo (left) — kept small.
- **Footer:** **source & as-of date** ("Source: Management accounts; as of 31 May 2026"),
  **page x of y** (`&[Page] of &[Pages]`), a **confidentiality / draft** marker where relevant
  ("Private & Confidential — Draft"), and the file/sheet reference for traceability.
- This is what separates a circulated exhibit (must stand alone) from a live-review sheet — every
  printed page states what it is, where the data came from, and as-of when.

## 6. Survive greyscale (print-safe palette)

- Board packs and lender files are frequently printed **black-and-white**. Any colour distinction
  (conditional formatting, actual-vs-forecast, RAG status) **must still read in greyscale** — which
  is exactly why every encoding carries a **non-colour cue** (shape, the number, +/− sign, dashed
  vs solid). Test with Print Preview → greyscale.
- Tinted fills chosen for AA contrast on screen also tend to survive greyscale; saturated rainbow
  fills collapse into indistinguishable greys — another reason to avoid them.

## 7. Workbook navigation — tab colour-coding

- **Colour-code worksheet tabs** by role for a multi-sheet model handed over live: e.g. inputs one
  hue, outputs/exhibits another, working/detail a muted grey, a cover/contents sheet a distinct
  accent. Keep it to the same restrained palette (2–3 hues), and pair the colour with a clear
  **tab name** (the non-colour cue), in a logical left-to-right order (cover → summary → detail).
- Put a **cover / contents sheet** first with the exhibit list and as-of date so a printed or shared
  workbook orients the reader immediately.

## 8. Print/exhibit QA checklist

- [ ] Explicit **print area** set (not the used range); manual page breaks so no table splits badly.
- [ ] **Repeating header rows/columns** on every page of long tables.
- [ ] Scale set **explicitly**, effective text **≥ ~8 pt**; wide sheets fit width = 1 page, not crushed.
- [ ] **Centred on page**, clean margins, gridlines off in print.
- [ ] Header (exhibit title + entity), footer (source, as-of date, page x of y, confidentiality).
- [ ] Palette **survives greyscale**; every colour cue has a shape/number/sign backup.
- [ ] Tabs **colour-coded + named** in logical order; a cover/contents sheet leads.
- [ ] Print Preview checked on the target trim **and** in greyscale before sending.
