# Reference: Proposal & Bankable-Document Section Architecture

The structural skeleton of a designed PDF proposal/report: the section order, the page grid, the
margin system, the heading scale, and the front/back matter. Sourced from the consulting-deliverable
tradition (McKinsey/BCG document craft, Minto pyramid), the Chwezi anti-slop rules, and
`doctrine/references/type-scale-and-spacing.md`.

---

## 1. Section order (the bankable spine)

A reader on a credit/investment committee reads in this order: cover → executive summary → exhibits
→ (only then) the body. Architect for that, conclusion-first.

| # | Section | Page style | Notes |
|---|---|---|---|
| — | **Cover** | Full design, no header/footer, no page number | See `cover-and-divider-systems.md`. |
| i | **Front matter** — TOC, list of exhibits, confidentiality/disclaimer | Roman numerals (i, ii, iii) | TOC is generated, not hand-typed. |
| 1 | **Executive summary** | Divider + body | One page ideally; the whole argument in miniature. Conclusion first. |
| 2 | **Context / problem / mandate** | Divider + body | Why now, the situation, the question (SCQA). |
| 3 | **Approach / methodology / solution** | Divider + body | What you propose and how. |
| 4 | **The case** — analysis, financials, evidence | Divider + body + **exhibits** | The numbers live here; exhibits do the work. |
| 5 | **Implementation / workplan / timeline** | Divider + body | Phasing, milestones, team, governance. |
| 6 | **Commercials / investment ask** | Divider + body | Price, terms, the ask, returns. |
| 7 | **Risks & mitigations** | Divider + body | A bankable document names its risks honestly. |
| 8 | **About / credentials / team** | Divider + body | Proof you can deliver. |
| A+ | **Appendices & exhibit pack** | Divider + exhibit pages | Detailed schedules, full financials, CVs, references. |

> Drop sections that don't apply, but **keep the order**. A pure report compresses 5–7; a bankable
> credit paper expands 4 and 7.

---

## 2. The page grid (A4 default; mirror for Letter)

- **Trim:** A4 = 210 × 297 mm (Letter = 215.9 × 279.4 mm). State which.
- **Margins (asymmetric, for a binding gutter):**
  - Inside (gutter) **22 mm** · Outside **18 mm** · Top **20 mm** · Bottom **22 mm** (room for footer).
  - For screen-only (unbound) PDF, equalise inside/outside to **20 mm**.
- **Columns:** single body column is the bankable default. Add a **42 mm outer marginalia column**
  (with a 6 mm gutter) for pull-quotes, source notes, small exhibits, and side-notes — this margin
  column is the strongest "authored, not exported" signal.
- **Baseline grid:** set a **12 pt baseline grid**; body leading is a multiple of it so text aligns
  across columns and pages.
- **Spacing unit:** one base unit of **4 pt**; all vertical space is a multiple (4/8/12/16/24/36 pt),
  per `type-scale-and-spacing.md` §Spacing rhythm.

---

## 3. Heading & body scale (group 01 Editorial)

Built off a **16 pt** body on a **1.25** (major-third) ratio, with real jumps — never timid steps
(`type-scale-and-spacing.md`). Display face for H1–H2, body face for H3–H4 and text.

| Role | Size / leading | Weight | Tracking | Notes |
|---|---|---|---|---|
| **H1** (section title, on divider) | 49 / 54 pt | Display 600–700 | -0.01em | Largest mark in the section. |
| **H2** (sub-section) | 25 / 31 pt | Display 600 | -0.01em | |
| **H3** | 20 / 26 pt | Body 600 | 0 | |
| **H4 / run-in** | 16 / 26 pt | Body 700 | 0 | Bold lead-in, same size as body. |
| **Body** | 10.5–11 / 16 pt (≈1.5) | Body 400 | 0 | 10.5–11 pt prints better than screen's 16 px. |
| **Caption / source note** | 8.5 / 12 pt | Body 400 italic | 0 | Exhibit captions, footnotes, marginalia. |
| **Eyebrow / section number** | 9 / 12 pt | Body 600 | +0.06em UPPERCASE | "SECTION 04 · THE CASE". |

- Body **colour is near-black, not `#000000`** (e.g. `#1A1A1A`) to cut eye strain
  (`type-scale-and-spacing.md`).
- At most **~3 sizes per section** for coherence.
- Numbered headings (1, 1.1, 1.1.1) aid cross-reference in a bankable document — use them.

---

## 4. Front matter, TOC & lists

- **TOC:** generated from heading styles; dot-leaders to right-aligned page numbers; include section
  number + title + page. List H1 and H2 only (not H3+) unless the document is long.
- **List of exhibits:** a separate table — "Exhibit 4.2 — Sensitivity of DSCR to tariff … p.17".
  Lets the IC jump straight to the numbers.
- **Confidentiality / disclaimer line** on the front-matter page and in every footer for bankable
  work ("Strictly private & confidential — prepared for [Client], [date]").

---

## 5. Cross-references & exhibits in text

- Refer to exhibits by number in the body ("see Exhibit 4.2"), never "the chart below" — pagination
  shifts in PDF.
- Keep an exhibit and its first reference within a spread where possible.

See `cover-and-divider-systems.md` for the cover and divider pages, and `print-ready-pdf-checklist.md`
before export. Accessibility: tag the PDF and set logical reading order so headings, TOC, and
exhibits are navigable (`doctrine/references/wcag-2.2-criteria.md`).
