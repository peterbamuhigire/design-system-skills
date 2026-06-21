# Reference: Accessible DOCX Tags (WCAG-aligned)

Operationalises `doctrine/references/wcag-2.2-criteria.md` for Word documents. A `.docx` carries
a tag/structure tree that screen readers (and the PDF it exports to) rely on. AA is the floor for
all Chwezi work. Do these *while* formatting — accessibility and good structure are the same
work, not a separate pass.

---

## The DOCX accessibility checklist

| # | Requirement | How (Word / python-docx) | WCAG criterion |
|---|---|---|---|
| 1 | **Set document language** | Review → Language → Set Proofing Language (and default); `w:lang` in styles | 3.1.1 Language of Page |
| 2 | **Real heading structure** | Apply Heading 1–4 styles bound to outline levels — never bold runs | 1.3.1 Info & Relationships |
| 3 | **No skipped heading levels** | H1 → H2 → H3 in order; don't jump H1 → H3 | 1.3.1, 2.4.10 |
| 4 | **Descriptive document title** | File → Info → Properties → Title (also used by AT and the browser tab on export) | 2.4.2 Page Titled |
| 5 | **Alt text on meaningful images** | Right-click image → View Alt Text → concise description; mark decoratives **Decorative** | 1.1.1 Non-text Content |
| 6 | **Tables: header row + simple grid** | Table Properties → Row → "Repeat as header row"; no merged/nested cells | 1.3.1 |
| 7 | **Logical reading order** | Inline (not floating) images/tables; content order = visual order | 1.3.2 Meaningful Sequence |
| 8 | **Meaningful link text** | "see the 2026 plan", never "click here" / bare URL | 2.4.4 Link Purpose |
| 9 | **Lists as real lists** | Use List Bullet/Number styles, not "- " typed by hand | 1.3.1 |
| 10 | **Contrast** | Body ≥ **4.5:1**; large text (≥ 18.66 pt bold / ≥ 24 pt) & UI rules ≥ **3:1** | 1.4.3 Contrast |
| 11 | **Colour not the only cue** | Don't signal a heading/status by colour alone — also size/weight/text | 1.4.1 Use of Colour |
| 12 | **TOC from styles** | Generate from Heading styles; gives AT a navigable outline | 2.4.5 Multiple Ways |
| 13 | **No info in headers/footers only** | Critical content lives in the body (header/footer regions are often skipped by AT) | 1.3.1 |

---

## Contrast quick-reference (this skill's palette)

| Foreground / background | Ratio | Passes |
|---|---|---|
| `#1A1A1A` Ink on white | 17.4:1 | AAA body |
| `#5A5A5A` Muted on white | 7.0:1 | AAA small text — captions/footers safe |
| Brand accent on white (text) | **must verify ≥ 4.5:1** | check per document; darken for text if it fails |
| White on brand accent (header fill) | **must verify ≥ 4.5:1** | else use Ink text on the accent-tint |

Design with **APCA** for real legibility, **certify with the WCAG 4.5:1 / 3:1 ratios** — APCA is
the WCAG 3.0 *draft*, not yet normative (`doctrine/references/wcag-2.2-criteria.md`).

---

## Verify before shipping

1. **Word Accessibility Checker** (Review → Check Accessibility) — resolve **all Errors** and
   review Warnings. Errors = missing alt text, missing table headers, merged cells, no language.
2. **Manual tab/outline pass** — navigate by heading (the Navigation pane shows the real tree);
   if a heading is missing from it, it was hand-formatted, not styled — fix it.
3. **Export check** — if a PDF is also delivered, export with "Document structure tags for
   accessibility" ON so the tag tree carries into the PDF, and fonts embed
   (`doctrine/references/embedding-by-format.md`).

Per WebAIM, the overwhelming majority of documents fail these basics — passing this checklist is
a genuine quality differentiator, exactly as the doctrine's "looks human-made" moat intends.
