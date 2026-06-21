# RTL Mirroring Rules — what flips, what does NOT, and how

**Scope:** the canonical rule for converting a left-to-right (LTR) layout to right-to-left (RTL —
Arabic, Hebrew, Persian/Farsi, Urdu) and back. Read this before mirroring anything. The single
most common amateur RTL bug is mirroring something that must not mirror (a play button, a chart,
a clock, a logo). This file exists to prevent that.

> **Principle:** RTL is not a horizontal flip of the whole screen. It is a flip of the *reading
> and navigation axis*, while real-world-anchored and inherently-LTR content stays put. Decide
> per element, not per screen.

---

## 1. The one discipline that does 80% of the work: logical properties

Author the layout in **logical** (flow-relative) properties so it flips by changing one attribute
(`dir="rtl"`), instead of physical (left/right) properties that you would have to re-edit.

| Physical (do NOT use for direction) | Logical (use this) |
|---|---|
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `padding-left` / `padding-right` | `padding-inline-start` / `padding-inline-end` |
| `left:` / `right:` | `inset-inline-start` / `inset-inline-end` |
| `text-align: left` / `right` | `text-align: start` / `end` |
| `float: left` / `right` | `float: inline-start` / `inline-end` |
| `border-left` / `border-right` | `border-inline-start` / `border-inline-end` |
| `border-top-left-radius` (corner) | `border-start-start-radius` |
| `width` (in flow contexts) | `inline-size` |
| `transform: translateX(8px)` | direction-aware: `translateX(calc(8px * -1))` in RTL, or use logical layout instead of transform |

Flexbox/Grid already follow `dir` when you use `start`/`end` for `justify-*`/`align-*` and avoid
`row-reverse` hacks. Set `dir` on `<html>` (or the nearest container for a mixed-direction island).

**`top`/`bottom`, `margin-block-*`, vertical things do NOT change** — RTL only flips the
*inline* (horizontal) axis, not the *block* (vertical) axis.

---

## 2. What MIRRORS (flips horizontally in RTL)

| Element | Why it flips |
|---|---|
| **Reading & text alignment** | Text reads right-to-left; default alignment becomes right. |
| **Page/content flow & columns** | First column is now on the right; reading order reverses. |
| **Navigation order** | Menus, tabs, breadcrumbs run right-to-left; the "first" item is rightmost. |
| **Back / forward, next / previous** | "Back" points right (→ becomes ←); "next" points left. |
| **Breadcrumb separators** | `Home > Shop > Item` becomes `Item < Shop < Home`. |
| **Progress / steppers / sliders (value direction)** | Progress fills from the right; "0→100" runs right-to-left. |
| **Carousel / pager advance direction** | "Next slide" moves the opposite way; dots reverse. |
| **Directional / movement icons** | Arrows, chevrons, "send/share/reply", indent/outdent, list bullets' side, undo/redo, "expand to the side" carets. |
| **Drawer / sidebar side** | A left drawer opens from the right. |
| **Toggle / switch "on" position** | The "on" end moves to the start side (right in RTL). |
| **Float of labels, badges, close (×) buttons** | Move to the mirrored corner. |
| **Slide / swipe / drawer motion direction** | Enter/exit animations invert (coordinate with motion skill). |
| **Form field label→input flow, checkbox/radio side** | Label leads from the right; control sits on the start side. |

---

## 3. What does NOT mirror (stays exactly as in LTR) — the critical list

Mirroring any of these is a **bug**. They are anchored to physical reality, to inherently-LTR
notation, or to brand.

| Element | Why it must NOT flip |
|---|---|
| **Media playback controls** (play ▶, pause, fast-forward, rewind, volume timeline) | Tied to the **time axis**, which always runs left→right. A flipped "play" pointing left is the signature RTL mistake. (Only previous/next *track* buttons mirror; the play head does not.) |
| **Progress/seek bar of audio/video** | Same — time goes left→right regardless of script. |
| **Clocks & analog time** | Time direction is physical, not linguistic. |
| **Charts/graphs with a time x-axis** | A line/area/bar chart over time keeps left=past, right=future. Flipping it inverts the data's meaning. (Charts of *non-temporal categories* in RTL may run right-to-left — decide by axis meaning.) |
| **Numbers themselves** | `1234` is written left-to-right even inside RTL text (digits are LTR). |
| **Phone numbers, credit-card numbers, IBANs** | LTR notation; mirroring scrambles them. |
| **Code, file paths, URLs, email addresses, hashtags, @handles** | Inherently LTR; isolate with `<bdi>`. |
| **Brand logos & wordmarks** | A mirrored logo is wrong/illegible; keep orientation. (Logo *position* in a header may move; its glyphs do not flip.) |
| **Checkmarks ✓, generic non-directional icons** (search 🔍, home, settings ⚙, heart, star, trash, camera) | No inherent direction; flipping just looks broken. |
| **Map directions / compass / real-world orientation** | Geography is physical. |
| **Musical notation, mathematical formulae** | Inherently LTR notation. |
| **"Powered by" / external-link ↗ glyph** | Convention; usually kept. |

> **Rule of thumb:** does the element point at the *flow of reading/navigation* (mirror) or at
> *physical reality / fixed notation / brand* (do not mirror)? When unsure, ask: "if I flip this,
> does its meaning invert?" If yes, do not flip it.

---

## 4. Icons: mirror the directional ones, leave the rest

- **Mirror:** arrows/chevrons, back/forward, next/prev, reply/forward, send, share, indent/outdent,
  bulleted-list alignment, "tilt"/skew directional glyphs, redo/undo.
- **Do NOT mirror:** search, home, settings, profile, trash, heart, star, camera, checkmark,
  play/pause/ff/rewind, hourglass/clock, volume, and any logo.
- Many icon sets ship an RTL variant or an `[dir=rtl] .icon { transform: scaleX(-1); }` hook —
  apply it **only** to the directional subset, never globally.

---

## 5. Bidirectional (bidi) text — isolating LTR runs inside RTL

Latin words, numbers, URLs, emails, and code embedded in RTL text will jump to the wrong end or
reorder punctuation unless isolated.

- Wrap each foreign-direction run in **`<bdi>`** (best for user-generated/dynamic content), or set
  **`unicode-bidi: isolate`** (CSS), or use Unicode isolate marks **U+2066/2067/2068 … U+2069**.
- For whole inputs of mixed content, `dir="auto"` lets the first strong character decide direction.
- Symptom you missed this: a price `‎$1,234.50` or a phone number lands on the wrong side, or a
  trailing `?`/`.` appears at the wrong end of a sentence.

---

## 6. Conversion checklist

1. Set `dir="rtl"` (and correct `lang`) at the root or island.
2. Confirm the layout uses **logical properties** throughout (grep for `left`/`right`/`margin-left`…).
3. Walk every element against §2 (should flip) and §3 (must not flip); log the decision.
4. Swap **only directional** icons; leave the non-directional set.
5. Add **bidi isolation** to every embedded LTR run (numbers, brands, URLs, code).
6. Invert **motion/gesture** directions (slide, swipe, drawer).
7. Check **line-height/spacing** for the RTL script (Arabic often needs more leading).
8. Verify numbers, dates, currency still format per locale (see `string-expansion-budgets.md`).
9. Re-test reflow at 200% / 320px (WCAG 1.4.10/1.4.4).

---

## Provenance
Aligned with W3C Internationalization (i18n) guidance, the Unicode Bidirectional Algorithm
(UAX #9), CSS Logical Properties & Values, and the Material/HIG bidirectionality guidance. Per the
Chwezi design doctrine (`doctrine/design-doctrine.md`), font choice for RTL scripts must still obey
the anti-slop and licensing rules — never silently fall back to a banned default for a "hard" script.
