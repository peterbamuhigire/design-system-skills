# Reference: Cover & Section-Divider Systems

The cover and the section dividers are where a PDF proposal earns or loses its "authored" reading in
the first two seconds. This file gives concrete, reusable systems — not a single template. Sourced
from the consulting-report and editorial-design traditions and the Chwezi anti-slop charter
(`doctrine/design-doctrine.md` §0, §2).

---

## A. Cover system

A bankable cover is **one strong typographic idea executed with restraint** — not five hedged
decorations. Pick ONE of the patterns below and commit.

### The four cover patterns

1. **Typographic / editorial** (default for bankable & consulting work).
   Full-page type on a flat ground. Title at hero scale (top-aligned to the grid, not centered),
   a thin rule, client + author marks, date/version. No image. Reads as confident and serious.
2. **Full-bleed image + overlay.**
   A single relevant, high-resolution image bleeds to all four trim edges (needs **3 mm bleed**).
   A solid or gradient **contrast overlay** (e.g. brand colour at 70–85% opacity, or a bottom-up
   dark scrim) guarantees text contrast ≥ 4.5:1 (`wcag-2.2-criteria.md`). Title sits in the
   protected zone.
3. **Banded / panel.**
   A strong colour band (top, bottom, or left third) carries the title; the rest is quiet. The band
   width aligns to the grid (e.g. the left band = the marginalia + first column).
4. **Framed / bordered.**
   A thin keyline frame inset from trim (e.g. 12 mm) with title centered on the optical (not
   geometric) center. Quietly formal — good for legal/board papers.

### Cover content blocks (every pattern carries these)

- **Document title** — hero scale (see worked values in `examples/proposal-cover-spec.md`).
- **Subtitle / descriptor** — one line below, body face.
- **Client mark** — "Prepared for [Client]" + logo if supplied.
- **Author mark** — your org name/logo + "Prepared by".
- **Meta line** — date, version, and **confidentiality** ("Private & Confidential") + a reference/
  document number for bankable work.
- **Optional confidence/status tag** — "Draft", "Final", "For Investment Committee".

### Cover anti-slop rules

- **No** centered-everything-on-a-blue-gradient cover — the #1 AI/template tell.
- **No** banned fonts; the title is the place the chosen display face must sing.
- Make the **hero-to-body jump real** (3×+); a title only slightly bigger than the byline is timid.
- Image covers: image must be **purposeful and ≥300 dpi at print size**, never decorative stock;
  always apply the contrast overlay before placing type.

---

## B. Section-divider system

Every numbered section opens on a **divider page** so the reader feels the document's structure. The
dividers must be **systematic** — the same construction, varying only by content — which is what
makes the set read as designed rather than assembled.

### Divider construction (pick one system, apply to all)

- **Number + title:** giant section number (`04`) at the top of the grid in the display face, the
  section title (H1, 49 pt) beneath, a thin full-width rule, and a one-line section abstract in the
  body face. No header/footer or page number on a divider.
- **Tab / progress:** a vertical or horizontal set of all section numbers down the margin, the
  current one highlighted in the accent colour — gives the reader a "you are here". Repeats on every
  divider.
- **Image-keyed:** a section-specific full-bleed image with overlay (same overlay system as the
  cover), title block in the protected zone — only if you have genuine, relevant imagery for each.

### Divider rules

- **Consistency over variety:** the divider for §1 and §8 differ only in number, title, abstract (and
  image, if image-keyed). Never restyle individual dividers.
- Carry the **accent colour** as the single recurring brand thread (section number, rule, or tab) so
  the document feels like one object.
- A divider is a **breath** — keep it sparse; the density belongs on the body and exhibit pages.
- Dividers always start on a **right-hand (recto) page** in a printed/bound document; insert a blank
  verso if needed.

---

## C. The recurring thread

Cover, dividers, headers, and exhibit frames should share **one** repeated element — usually the
accent colour applied to a rule or number, or a single keyline weight. That repetition is the cheap,
high-leverage signal that a human designed the whole document as a system.

See `examples/proposal-cover-spec.md` and `examples/exhibit-page-layout.md` for fully dimensioned
worked builds, and `print-ready-pdf-checklist.md` for bleed/overlay preflight.
