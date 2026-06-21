# Reference: Print-Ready PDF Preflight Checklist

The gate every designed PDF passes **before it ships**. A bankable document fails the moment a font
substitutes or an exhibit prints muddy. Run this top to bottom. Cites
`doctrine/references/embedding-by-format.md` (PDF), `wcag-2.2-criteria.md`, and the Chwezi anti-slop
charter.

Mark each: ✅ pass · ⚠️ fix · n/a.

---

## 1. Fonts (the non-negotiable)

- [ ] **All fonts embedded.** Open the PDF → Properties/Document → Fonts: every face shows
      "Embedded" or "Embedded Subset". *Zero* "not embedded" entries.
- [ ] **Subsetted** to keep file size down (`embedding-by-format.md`: subsetting cuts a font 80–90%).
- [ ] The generating tool **embeds rather than references system fonts** — verify, don't assume
      (`embedding-by-format.md` §PDF). HTML-to-PDF and DOCX→PDF are the common offenders.
- [ ] **No banned font** anywhere (`ai-slop-banned-fonts.md`). If a substitute slipped in (Arial,
      Calibri, Inter), a font failed to embed — fix the source, don't accept the substitution.
- [ ] Licence permits embedding for distribution (`doctrine/references/licensing-and-embedding.md`;
      group 01 OFL baselines and Fontshare faces are fine to embed).

## 2. Colour

- [ ] **Colour space matches output:** **sRGB** for screen-only PDF; **CMYK** for a print/bureau job.
      RGB images in a CMYK job shift colour — convert first.
- [ ] Accent/brand colour is **one consistent value** across cover, dividers, rules (no drift between
      RGB hex and a CMYK build of the "same" colour).
- [ ] If printing **mono**, check the document still reads with colour removed (test grayscale export);
      don't rely on colour alone to carry meaning (`wcag-2.2-criteria.md`: non-colour cues).
- [ ] Rich black for large solids in print (e.g. C60 M40 Y40 K100), not 100K alone, where the bureau
      requires it.

## 3. Images & exhibits

- [ ] Raster images **≥ 300 dpi** at placed size for print (≥ 150 dpi acceptable screen-only). No
      upscaled screenshots.
- [ ] Charts/diagrams placed as **vector** (PDF/SVG/EPS) where possible — they stay crisp at any zoom.
- [ ] Every exhibit has a **number, caption, and source note** (`examples/exhibit-page-layout.md`).
- [ ] Exhibit colours survive the print method (test the mono case if mono printing).

## 4. Page geometry & print mechanics

- [ ] **Trim size** correct and consistent (A4 / Letter) on every page.
- [ ] **Bleed (3 mm)** present on all full-bleed elements (covers, image dividers); **crop marks**
      included if the bureau requires them. None of this for screen-only PDFs.
- [ ] **Margins/gutter** correct for binding (inside margin wider if bound — see
      `proposal-section-architecture.md` §2).
- [ ] Dividers fall on **recto** pages in a bound document; blank versos inserted intentionally.
- [ ] **No content in the bleed/trim danger zone** (keep live text ≥ 5 mm inside trim).

## 5. Pagination & navigation

- [ ] **Page numbers** correct: roman in front matter, arabic in body; none on cover/dividers.
- [ ] **Running header/footer** carries section + page + confidentiality line; absent on cover and
      dividers.
- [ ] **TOC and List of Exhibits page numbers match** the actual pages (regenerate after final edits).
- [ ] **Internal links / bookmarks** (TOC entries, cross-references) resolve if it's an interactive PDF.

## 6. Accessibility (tagged PDF) — `wcag-2.2-criteria.md`

- [ ] PDF is **tagged**; **reading order** is logical (heading → body → exhibit, not visual-position
      order).
- [ ] **Headings** are real tags (H1–H4), not just big text — enables screen-reader navigation.
- [ ] **Alt text** on meaningful images/exhibits; decorative images marked as artifacts.
- [ ] **Document title & language** set in metadata.
- [ ] Body text contrast ≥ **4.5:1**; large text/graphical objects ≥ **3:1** (design with APCA,
      certify with the WCAG ratio).

## 7. Final file hygiene

- [ ] **PDF/A** (archival) or **PDF/X** (print) conformance if the recipient requires it.
- [ ] File size reasonable (subset fonts, downsample over-300-dpi images for screen builds).
- [ ] **Metadata** clean: title, author, no leftover "Document1"/template author; no tracked changes
      or comments leaked from the DOCX source.
- [ ] Filename is professional and versioned ("Client_Proposal_v3_FINAL_2026-06.pdf").
- [ ] Opened and **eyeballed on a different machine / device** than it was built on — the real test
      that embedding worked.

---

**Ship rule:** any ⚠️ in §1 (fonts) or §6 (accessibility, for bankable/public work) blocks shipping.
Everything else is fix-before-send.
