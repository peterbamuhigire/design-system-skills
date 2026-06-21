# Worked example: An embedding spec for one font across web, DOCX, and PDF

A complete, copy-real application of `font-embedding-and-licensing` end to end for **one chosen
display face**, taken through all three embedding targets that carry different licence and size
consequences: **web** (woff2 `@font-face`, variable, `font-display`), **DOCX** (embed + subset), and
**PDF** (embed, never reference). Each target states its own licence check and its file-size impact.

This continues the Maduuka brief from
`skills/01-typography-and-fonts/font-selection-and-pairing/examples/applied-type-scale.md`, so the
faces are already chosen and stated — here we only *load* them, per the skill's division of labour.

---

## The chosen faces (already decided upstream)

| Role | Face | Licence basis | Source |
|---|---|---|---|
| Display / headings | **Clash Display** (700) | **Fontshare** — free to use **and** embed; raw file **not** redistributable | `premium-font-scan` of `fonts/03-modern-product-grotesque/` (MANIFEST grants embed, denies file-ship) |
| Body | **Hanken Grotesk** (400) | **OFL 1.1** — use, embed **and** redistribute all permitted | OFL baseline |

This is pairing **S2** from `references/pairing-catalog.md`. The two licences are deliberately
*different*, so the licence check below changes per format — which is the whole point of this example.

> **The Fontshare rule (state it once, apply it everywhere):** a Fontshare face may be **embedded**
> into a built artifact (a web page's loaded woff2, a subsetted DOCX, an embedded PDF) because the
> reader receives a *rendered/embedded* product, not a reusable font file. What you may **not** do is
> ship the raw `Clash Display.otf`/`.woff2` as a standalone downloadable asset, commit it to a public
> repo, or hand the client the loose file. OFL (Hanken) has no such restriction — the raw file is
> freely redistributable. So Hanken is always safe; Clash needs the per-format "is this embed or
> redistribution?" question answered each time.

---

## Target 1 — Web (woff2 + `@font-face`, variable, `font-display`)

**Licence check.** A self-hosted woff2 served from your own origin is **embedding**, not
redistribution — the browser caches a rendered web-font, the user can't trivially reuse it as a
desktop font. Clash Display (Fontshare) is **permitted** here. Hanken (OFL) is permitted with no
caveat. The one thing that would breach the Fontshare terms is exposing the woff2 at a public,
directly-linkable path advertised *as a font download* — so serve it as a site asset, not a "fonts
to download" page.

**Settings.** Self-host (don't hotlink a CDN you don't control), use the **variable** woff2 so the
whole weight range is one file, and set `font-display: swap` so text paints immediately in the
fallback and swaps when the face arrives.

```css
/* One variable file per face — the entire weight range, not five static cuts */
@font-face {
  font-family: "Clash Display";
  src: url("/assets/fonts/clash-display.woff2") format("woff2-variations");
  font-weight: 200 700;           /* register the axis range */
  font-style: normal;
  font-display: swap;             /* paint fallback now, swap in Clash when ready */
}
@font-face {
  font-family: "Hanken Grotesk";
  src: url("/assets/fonts/hanken-grotesk.woff2") format("woff2-variations");
  font-weight: 300 900;
  font-style: normal;
  font-display: swap;
}

:root {
  --font-display: "Clash Display", "Hanken Grotesk", Georgia, serif; /* fallback AFTER the face */
  --font-body:    "Hanken Grotesk", system-ui, sans-serif;
  font-optical-sizing: auto;
}

h1, h2, h3 { font-family: var(--font-display);
             font-variation-settings: "wght" 700; }   /* drive weight from the variable axis */
body       { font-family: var(--font-body);
             font-variation-settings: "wght" 400; line-height: 1.6; }
```

Add a `preload` for the display face only (it blocks the hero), and let the body face load normally:

```html
<link rel="preload" href="/assets/fonts/clash-display.woff2" as="font"
      type="font/woff2" crossorigin>
```

**File-size impact.** Two **variable** woff2 files instead of ten static weights. Typical figures:
Clash Display variable woff2 ≈ **45–60 KB**, Hanken Grotesk variable woff2 ≈ **40–55 KB** — together
**~85–115 KB** transferred once, then cached. Shipping five static cuts of each (10 files) would land
nearer **250–350 KB**, so the variable approach roughly **halves** the font payload while *widening*
the available weight range. `font-display: swap` means this weight costs **0 ms of blocked first
paint**.

---

## Target 2 — DOCX (embed + subset)

**Licence check.** A Word document with **embedded** fonts carries the glyph data *inside the .docx*.
For a Fontshare face this is the borderline case, and the deciding factor is **subsetting**: an
*embed-and-subset* keeps only the glyphs actually used (a few hundred), which is an embedded rendering
aid, **not** a redistributable font — permitted. A *full embed without subsetting* ships the entire
font file inside the document, which is much closer to redistributing the file — avoid it for the
Fontshare face. So: **Clash Display → embed WITH "Embed only the characters used" ticked.** Hanken
(OFL) may be embedded either way, but subset it anyway for size. If the client needs to *edit and
re-typeset* freely with Clash on their own machines, that's a desktop-use question their own
Fontshare download covers — the embed in your deliverable does not grant it.

**Settings (Word → File → Options → Save):**

- ☑ **Embed fonts in the file**
- ☑ **Embed only the characters used in the document (best for reducing file size)** ← required for Clash
- ☐ Do *not* embed common system fonts (leave unticked; keeps the file lean)

If generating programmatically (e.g. python-docx + a post-process, or LibreOffice headless), set the
equivalent `EmbedFonts=true` **and** `EmbedOnlyUsedFonts=true`. Apply the faces by their exact family
name — `Clash Display` for Heading styles, `Hanken Grotesk` for Normal/body — so the embed matches
the named face and Word doesn't silently substitute Calibri.

**File-size impact.** A subsetted embed of a typical Latin display face adds roughly **40–90 KB** per
weight used; body + heading here ≈ **+120–180 KB** to the .docx. A *non-subsetted* full embed of the
same two families would add **400 KB–1 MB+** and re-raise the Fontshare redistribution concern — which
is exactly why subsetting is non-negotiable, not just a size nicety.

---

## Target 3 — PDF (embed, never reference)

**Licence check.** A PDF must **embed** the font outlines, never *reference* the reader's system
fonts. Embedding is permitted for both faces (Clash via the Fontshare embed allowance, Hanken via
OFL). The failure mode here isn't a licence breach — it's a **rendering** breach: a PDF that
references `Clash Display` instead of embedding it will silently substitute a system font on any
machine without Clash installed, destroying the branded headline. Most generators embed *with*
subsetting by default, which also keeps the Fontshare embed squarely on the "embedded, not
redistributed" side of the line.

**Settings by generator:**

- **LaTeX (`fontspec` + LuaTeX/XeTeX):** `\setmainfont{Hanken Grotesk}` /
  `\setsansfont{Clash Display}` — fontspec embeds and subsets the loaded faces automatically.
- **Chromium / headless print-to-PDF (`puppeteer`, `weasyprint`, wkhtmltopdf):** the woff2 from
  Target 1 is embedded into the PDF as a subset; verify it lands embedded (see check below).
- **Word/LibreOffice "Export to PDF":** enable **"Embed standard fonts"**; the subsetted DOCX embed
  carries straight through.
- **Adobe / Acrobat preflight:** set the PDF/X or PDF/A profile, which *forces* full embedding and
  will flag any referenced (non-embedded) font.

**Verify embedding (do this, don't assume):**

```bash
# Every font must read "(embedded subset)" — not just "(referenced)"
pdffonts maduuka-onepager.pdf
# Expected, e.g.:
#   name                  type        emb sub
#   ABCDEF+ClashDisplay   CID Type 0C yes yes      ← embedded + subset  ✅
#   GHIJKL+HankenGrotesk  CID Type 0C yes yes      ← embedded + subset  ✅
# A row showing "emb = no" for Clash Display = a referencing bug → re-export with embedding ON.
```

**File-size impact.** Subset-embedded outlines add roughly **30–80 KB** per face to the PDF
(comparable to the DOCX subset). A full (non-subset) embed would add **300 KB–1 MB+** per family. For
a branded one-pager, expect the two subset-embedded faces to add **~80–150 KB** total — a fixed,
one-time cost that guarantees the document renders identically on every device, which is the entire
reason a PDF is chosen over a DOCX/XLSX for pixel-perfect branded output.

---

## The cross-format summary

| Target | Mechanism | Clash (Fontshare) verdict | Why permitted | Size impact |
|---|---|---|---|---|
| **Web** | self-hosted variable woff2, `@font-face`, `font-display: swap` | ✅ embed | served as a site asset, not a font download | ~85–115 KB total (≈½ of static cuts) |
| **DOCX** | embed **+ subset** ("characters used only") | ✅ embed (subset) | subset = rendering aid, not a redistributable file | +120–180 KB subset (vs 400 KB–1 MB full) |
| **PDF** | embed outlines, **never reference**; verify with `pdffonts` | ✅ embed (subset) | outlines embedded, not the reusable font file | +80–150 KB subset |

**The one rule that never embeds and never ships:** the raw `Clash Display.woff2`/`.otf` as a
standalone, downloadable, or committed file. Hanken's raw file *may* be shipped (OFL), Clash's may
not (Fontshare) — but in all three targets above we only ever **embed**, so both faces are clear.

---

## Verification (run, per the skill's step 4)

1. ✅ Licence confirmed per format **before** shipping — web/DOCX/PDF all resolve to *embed*, which
   both OFL (Hanken) and Fontshare (Clash) permit; no raw Clash file is shipped or committed.
2. ✅ Web: variable woff2, self-hosted, `font-display: swap`, fallback placed **after** the face.
3. ✅ DOCX: "Embed only the characters used" ticked (mandatory for the Fontshare face); faces applied
   by exact name so Word can't substitute.
4. ✅ PDF: `pdffonts` shows **emb = yes, sub = yes** for both faces — embedded, not referenced.
5. ✅ File-size impact reported for each embedded document (DOCX +120–180 KB, PDF +80–150 KB).
6. ✅ Rendered output spot-checked on a machine **without** the fonts installed — the intended faces
   appear, not a substitute.

---

## References

- `skills/01-typography-and-fonts/font-embedding-and-licensing/SKILL.md` (the workflow this applies).
- `doctrine/references/embedding-by-format.md` (per-format loading mechanics).
- `doctrine/references/licensing-and-embedding.md` (OFL vs Fontshare embed/redistribute matrix).
- `skills/01-typography-and-fonts/font-selection-and-pairing/examples/applied-type-scale.md`
  (the upstream brief where Clash + Hanken were chosen and stated).
- `skills/01-typography-and-fonts/premium-font-scan/SKILL.md` (where the Fontshare MANIFEST permission
  was confirmed).
