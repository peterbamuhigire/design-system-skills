# Worked Example — LTR → RTL conversion of a product-detail screen (Arabic, `dir="rtl"`)

A real, element-by-element conversion of an English (LTR) e-commerce **product-detail screen** to
Arabic (RTL). For every element it records the **decision** (mirror / no-mirror / bidi-isolate) and
the **reason**, so the rationale survives handoff. This is the template for any RTL conversion.

**Source screen (en):** a product page — top app bar with logo + search + cart, breadcrumb,
product image gallery, title, star rating, price, quantity stepper, "Add to cart" CTA, a 5-step
delivery progress tracker, an image carousel of related items, and a reviews list (with embedded
English brand names and dates).

**Root change:** `<html lang="en" dir="ltr">` → `<html lang="ar" dir="rtl">`. Everything below
assumes the layout was authored in **logical properties** (see `references/rtl-mirroring-rules.md`),
so most mirroring happens automatically; the table records what still needs a human decision.

---

## Decision table

| # | Element | LTR behaviour | Decision in RTL | Reason |
|---|---|---|---|---|
| 1 | **App-bar layout** | logo left, search center, cart right | **Mirror** — logo right, cart left | Navigation/reading axis flips. Handled free by logical props + flex `start/end`. |
| 2 | **Brand logo glyphs** | wordmark "Maduuka" | **No-mirror** | A flipped logo is wrong/illegible. Position moves (§1); glyphs do not flip. |
| 3 | **Search field** | icon left, text aligned left, placeholder LTR | **Mirror** field; **bidi-isolate** any Latin query | Field flips to right-aligned (`text-align: start`); a typed English term needs `dir="auto"`/`<bdi>` so it doesn't reorder. |
| 4 | **Search 🔍 icon** | — | **No-mirror** | Non-directional icon; flipping looks broken. |
| 5 | **Cart icon + count badge** | badge top-right of icon | **Mirror** badge to top-left corner | Badge corner is on the start side; `inset-inline-start`. Icon itself not flipped. |
| 6 | **Breadcrumb** | `Home > Shop > Shoes > Item` | **Mirror** order + **flip separators** | Runs `الرئيسية > المتجر …` right-to-left; the `>` chevrons become `<`. |
| 7 | **Back arrow (←)** | points left = "back" | **Mirror** to point right | Directional icon tied to navigation flow. |
| 8 | **Product title (long)** | one line in en | **Wrap-tolerant** | Arabic length is variable; allow 2 lines, raise line-height (Arabic needs more leading). |
| 9 | **Star rating ★★★★☆** | fills left→right | **Mirror** fill direction (start side) | Rating is a value scale along the reading axis → fills from the right. |
| 10 | **Numeric rating "4.2"** | `4.2` | **No-mirror digits**; may show Arabic-Indic `٤٫٢` | Digits are written LTR even in RTL text; locale may shape them via `Intl`. |
| 11 | **Price `$1,299.00`** | left-aligned, `$` prefix | **Re-align to start**; **re-format** + **bidi-isolate** | Number stays LTR (`<bdi>`); format via `Intl.NumberFormat('ar', {currency:'USD'})` → symbol/separators/position per locale; show `USD` code to disambiguate `$`. |
| 12 | **Quantity stepper `− 1 +`** | minus left, plus right | **Mirror** control order | The `−`/`+` and increment direction follow the reading axis → minus moves to the right. Digit in the middle stays LTR. |
| 13 | **"Add to cart" CTA** | 11-char en label | **Reserve ~2.5× width / allow wrap** | `أضف إلى السلة` plus expansion budget (short string → +200–300%, see `string-expansion-budgets.md`). Never fix CTA width to English. |
| 14 | **Delivery progress tracker (5 steps)** | fills left→right, step 2 active | **Mirror** — fills from the right | Progress is a value along the reading axis; start = right. Step labels right-aligned. |
| 15 | **"Order placed → Shipped → Delivered" chevrons** | → between steps | **Mirror** chevrons to ← | Directional connectors follow flow. |
| 16 | **Estimated-delivery date** | `03/09/2026` (US M/D/Y) | **Re-format by locale** | `09/03/2026` would be misread; format via `Intl.DateTimeFormat('ar')` (or month-name) — avoid ambiguous numeric date. |
| 17 | **Related-items carousel** | "next" advances left→right; dots L→R | **Mirror** advance direction + dot order + **invert slide motion** | Carousel advance and swipe gesture invert in RTL (coordinate with `08-motion-and-interaction`). |
| 18 | **Carousel ▶ play-auto-rotate control** | play glyph | **No-mirror** | Playback control is tied to the time axis — flipping a play button is the signature RTL bug. |
| 19 | **Reviews list** | left-aligned Arabic text, reviewer + date | **Mirror** alignment; **bidi-isolate** embedded items | Body becomes right-aligned. Reviews containing English product names, `@handles`, URLs, or `4.2/5` ratings get `<bdi>` so they don't jump ends. |
| 20 | **Reviewer phone (support block) `+1 415-…`** | LTR | **No-mirror**, isolate | Phone numbers are inherently LTR; mirroring scrambles them. |
| 21 | **"Powered by Stripe" footer + ↗** | ↗ external-link glyph | **No-mirror** glyph; mirror block position | Convention keeps ↗; the footer block position flips with layout. |
| 22 | **Image gallery thumbnails (vertical strip, left)** | strip on the left | **Mirror** to the right | `inset-inline-start` puts the strip on the start (right) side. |

---

## What this conversion proves

- **Most flips were free** because the layout used logical properties — the table is mostly
  *confirming* automatic behaviour and catching the **exceptions** (#2 logo, #4 search icon,
  #10/#11/#20 LTR numerics, #18 play control).
- **The dangerous decisions are the no-mirrors:** logo (#2), play control (#18), phone (#20),
  external-link glyph (#21), and all digits (#10/#11/#16). Mirroring any of these would be a bug.
- **Bidi isolation** (#3, #11, #19, #20) was needed wherever LTR content (numbers, English brand
  names, URLs, handles) sat inside RTL text.
- **Expansion** (#8 title, #13 CTA, #6 breadcrumb) forced wrap-tolerant, non-fixed-width
  containers — sized from `references/string-expansion-budgets.md`, not eyeballed.
- **Locale formatting** (#11 currency, #16 date, #10 digits) went through `Intl`, never hand-rolled.

## Verify (post-conversion)
1. Visual pass in `dir="rtl"`, `lang="ar"`: nothing clipped, mirrored set flipped, no-mirror set intact.
2. Numbers/dates/currency formatted via `Intl`; `$` disambiguated with `USD`.
3. Bidi runs read correctly (no jumped punctuation/numbers).
4. Arabic line-height legible; long Arabic title and CTA wrap, not clipped.
5. Carousel/back/stepper motion + gesture directions inverted.
6. Reflow still passes at 200% / 320px (WCAG 1.4.10/1.4.4); `lang`/`dir` set (3.1.1).

---

*Per `doctrine/design-doctrine.md`: the Arabic font here must cover the script AND obey the
anti-slop/licensing rules (`doctrine/references/font-groups-and-usage.md`) — no silent fallback to
a banned default just because Arabic is "harder" to set. Decision rules per
`references/rtl-mirroring-rules.md`; budgets/formatting per `references/string-expansion-budgets.md`.*
