---
name: internationalization-and-rtl-design
description: Use when designing or building any UI, document, or layout that will ship in more than one language, script, or region — or that might. Triggers on right-to-left (RTL) languages (Arabic, Hebrew, Persian/Farsi, Urdu), bidirectional text, logical vs physical CSS properties, mirroring a layout, translation/string expansion overflow, truncation, locale-aware number/date/currency/percent formatting, pluralization, ICU MessageFormat, `dir="rtl"`, `lang` attributes, font coverage for non-Latin scripts, or any request to "localize", "internationalize", "make it work in Arabic", "add RTL support", "handle long German strings", or "format dates/currency by locale". Co-activates with EVERY design group — layout, typography, components, forms, navigation, content — never assume English-LTR-only.
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
    - claude-code
    - codex
---

# Internationalization & RTL Design (i18n)

This skill makes a Chwezi artifact **survive translation and direction change without a
redesign**. It treats locale (script direction, string length, number/date/currency format,
font coverage) as a **design constraint present from the first layout decision** — not a
late-stage retrofit. The cheapest i18n is the layout that was never hard-coded to English-LTR
in the first place.

Internationalization (i18n) is the engineering/design work that *makes* localization possible;
localization (l10n) is the per-locale translation/adaptation. This skill owns i18n: the
direction-agnostic, length-tolerant, locale-formatted layout. It co-activates with every group
because direction and expansion touch grids, type, components, forms, and copy alike.

<!-- dual-compat-start -->
## Use When
- Designing or building any UI/document that **ships in, or could later ship in,** more than one
  language — especially if one is **RTL** (Arabic, Hebrew, Persian/Farsi, Urdu) or a CJK script.
- A request mentions RTL, `dir="rtl"`, bidirectional/bidi text, mirroring, logical CSS
  properties, string/translation expansion, overflow/truncation in another language, locale
  number/date/currency/percent formatting, pluralization, ICU MessageFormat, or `lang`.
- Auditing an English-only layout for translation-readiness *before* strings are sent out.
- Choosing or pairing fonts that must cover non-Latin scripts (Arabic, Hebrew, CJK, Cyrillic,
  Devanagari) — coordinate with `01-typography-and-fonts/font-selection-and-pairing`.

## Do Not Use When
- The work is purely the **wording** of one English string → `10-content-design-and-ux-writing/ux-writing-and-microcopy`
  (this skill sizes the *space* a string needs and formats data, it does not write copy).
- The work is purely **font licensing/embedding** mechanics → `01-typography-and-fonts/*`
  (this skill names the *coverage* requirement; that group owns the file/licence).
- The work is **general responsive breakpoints** unrelated to language → `03-layout-grid-and-composition/responsive-and-adaptive-layout`
  (though string expansion is a sibling cause of overflow — cross-reference it).
- The work is **WCAG conformance** generally → `accessibility-wcag-2-2-compliance` (this skill
  cites it for `lang`/`dir` and reflow, but does not own the audit).

## Required Inputs
- The **target locales** (or "unknown / might expand later" — design defensively then).
- Which targets are **RTL** and which scripts are in play (Latin, Arabic, Hebrew, CJK, Cyrillic…).
- Whether the artifact is UI (web/app), a document (DOCX/PDF/PPTX), or both.
- The longest expected strings, or permission to budget from `references/string-expansion-budgets.md`.
- Locale formatting needs: dates, times, numbers, currency, percentages, units, names, addresses.

## Workflow

### A. Direction & layout (build it direction-agnostic)
1. **Set language and direction at the root.** `<html lang="ar" dir="rtl">` (or `dir="auto"`
   where mixed). The `lang` attribute is also an accessibility requirement (WCAG 3.1.1) —
   see `accessibility-wcag-2-2-compliance` and `doctrine/references/wcag-2.2-criteria.md`.
2. **Use logical, not physical, properties — everywhere.** Replace `margin-left` →
   `margin-inline-start`, `padding-right` → `padding-inline-end`, `left:` → `inset-inline-start`,
   `text-align: left` → `text-align: start`, `float: left` → `float: inline-start`. Logical
   properties flip automatically with `dir`; physical ones do not. This single discipline does
   ~80% of RTL mirroring for free. See `references/rtl-mirroring-rules.md`.
3. **Mirror the layout, but know what does NOT mirror.** The reading axis, navigation, progress,
   and most directional icons flip; but media playback controls, clocks, charts with a time
   x-axis, phone numbers, code, and brand logos generally do **not**. Apply the full
   what-mirrors-vs-doesn't table in `references/rtl-mirroring-rules.md` — getting this wrong is
   the #1 amateur RTL mistake (mirroring a play button or a line chart).
4. **Handle bidirectional (bidi) runs.** LTR fragments inside RTL text (URLs, emails, numbers,
   Latin brand names, code) need isolation — use `<bdi>`, `unicode-bidi: isolate`, or the
   Unicode isolate marks — or punctuation and digits will jump to the wrong end.
5. **Mirror motion and gesture.** Slide-in/out, carousel advance, swipe-to-dismiss, and
   back-navigation directions invert in RTL. Coordinate with `08-motion-and-interaction`.

### B. Expansion & contraction (give every string room to grow)
6. **Budget expansion from real data, never eyeball it.** Short UI strings can grow **+200–300%**
   from English; running text averages **+30–35%** for German/Finnish, with CJK *contracting*.
   Use the per-language, per-length table in `references/string-expansion-budgets.md` — never a
   single flat "+30%" guess, which under-budgets buttons and over-budgets paragraphs.
7. **Design layouts that flex, not fixed boxes.** Avoid fixed-width buttons/nav/labels and
   single-line assumptions. Let containers wrap to a second line; reserve vertical space.
   String expansion is a sibling of responsive overflow — pairs with
   `03-layout-grid-and-composition/responsive-and-adaptive-layout`.
8. **Truncate honestly, and only as a last resort.** If truncation is unavoidable, ellipsis +
   full text on hover/focus/`title`; never truncate so hard the label is ambiguous. Prefer
   wrapping. Test with the longest budgeted string AND a pseudo-localized string.
9. **Pseudo-localize before any real translation exists.** Render `[!!! Ŝéttîngs ñññ !!!]` —
   accented to expose missing Unicode handling, bracketed to expose clipping, padded ~+40% to
   expose tight boxes. This catches most i18n layout bugs with zero translation cost.
10. **Never concatenate sentences from fragments.** Word order differs per language. Use whole,
    parameterized messages (ICU MessageFormat) so translators control order; never build
    `"You have " + n + " items"`. Handle plurals with ICU `plural` categories (languages have
    1–6 plural forms, not just one/many).

### C. Locale formatting (let the platform format data)
11. **Format numbers, dates, currency, percent via the locale API — never hand-roll.** Use
    `Intl.NumberFormat` / `Intl.DateTimeFormat` (web), `ICU`/`CLDR`-backed APIs elsewhere.
    Decimal/grouping separators, date order (DMY vs MDY vs YMD), 12/24-hour, currency symbol
    position, and digit shaping (Arabic-Indic digits) are all locale-driven. See
    `references/string-expansion-budgets.md` §"Formatting that changes by locale".
12. **Currency: symbol, position, and code.** `1 234,56 €` vs `$1,234.56` vs `١٬٢٣٤٫٥٦`. Show the
    ISO code (USD/EUR/UGX) where ambiguity matters. Never assume `$` = USD.
13. **Choose fonts that cover the target scripts.** A Latin-only face renders tofu (□) for
    Arabic/CJK. Specify a script-complete family or an explicit fallback stack; respect the
    doctrine's anti-slop and licensing rules — coordinate with
    `01-typography-and-fonts/font-selection-and-pairing` and `doctrine/references/font-groups-and-usage.md`.
    Watch line-height: Arabic and Devanagari need more vertical space than Latin.

### D. Verify
14. **Test in a real RTL locale + a long-expansion locale + a CJK locale + pseudo-locale.** Walk
    the flow: nothing clipped, mirrored correctly (and the no-mirror set NOT mirrored), bidi runs
    correct, numbers/dates/currency formatted right, no tofu, focus/reflow still pass at 200%/320px.
15. **Record the before/after decisions.** For an RTL conversion, log every element as
    mirror / no-mirror / bidi-isolate with the reason — use `examples/rtl-before-after.md` as the
    template so the rationale survives handoff.

## Anti-Patterns
- **Physical properties everywhere** (`margin-left`, `left:`, `text-align: left`) — guarantees a
  broken RTL layout and a full re-edit later. Logical properties from day one instead.
- **Mirroring things that must not mirror** — a flipped play/pause/fast-forward, a mirrored line
  chart with a time axis, a reversed clock, a backwards logo, mirrored phone numbers. The
  signature amateur RTL bug. See `references/rtl-mirroring-rules.md`.
- **A flat "+30%" expansion guess for everything** — under-budgets short labels/buttons (which
  grow 200%+) and over-budgets paragraphs. Budget by length band, per language.
- **Fixed-width buttons and single-line labels** — overflow or clip the moment a longer language
  arrives. Design flexible containers.
- **Hard truncation with no recovery** — ellipsis that hides meaning and offers no hover/full text.
- **Sentence-building by string concatenation** — `"Deleted " + n + " files"` is untranslatable;
  word order and plural rules break. Use ICU MessageFormat with `plural`.
- **Hand-rolled date/number/currency formatting** — `MM/DD/YYYY`, `$` hard-coded, `,` decimal
  assumed. Use `Intl`/CLDR. Forgetting Arabic-Indic digit shaping.
- **Latin-only fonts on a multi-script product** — renders tofu (□) for Arabic/CJK/Devanagari.
- **No bidi isolation** — Latin brand names, URLs, and numbers jump to the wrong end of RTL text.
- **"We'll add languages later"** with English-LTR-hard-coded layout — "later" becomes a rebuild.

## Outputs
- A **direction-agnostic layout** (logical properties, correct `lang`/`dir`, mirrored where
  appropriate, bidi-isolated where needed) that flips by changing one attribute.
- An **expansion-tolerant layout** sized from real per-language budgets, pseudo-localization-tested.
- **Locale-formatted** numbers, dates, currency, and percentages via the platform i18n API.
- A recorded **RTL/i18n decision sheet** (mirror / no-mirror / bidi / expansion per element)
  ready for handoff and for the `design-qa-and-pre-launch-review` gate.

## Examples
- `examples/rtl-before-after.md` — a **real worked LTR→RTL conversion** of an Arabic e-commerce
  product screen (header, search, breadcrumb, product card, rating, price, qty stepper, reviews,
  carousel), logging for each element whether it mirrors, stays put, or needs bidi isolation —
  and the reasoning behind each decision. Use it as the template for any RTL conversion.

## References
- [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md) — the cross-cutting
  charter; §3 places this skill in `00-cross-cutting-ops-qa-a11y` (co-activates with every group).
  The anti-slop §2 also governs font choice for non-Latin scripts — never fall back silently to a
  banned default just because a script is "hard".
- [`doctrine/references/wcag-2.2-criteria.md`](../../../doctrine/references/wcag-2.2-criteria.md)
  — `lang` of page/parts (3.1.1/3.1.2) and reflow at 320px/200% (1.4.10/1.4.4), which RTL and
  expansion both stress.
- [`doctrine/references/font-groups-and-usage.md`](../../../doctrine/references/font-groups-and-usage.md)
  — script coverage and pairing for non-Latin fonts.
- `references/rtl-mirroring-rules.md` — the definitive what-mirrors / what-does-NOT-mirror table,
  logical-property mapping, and bidi-isolation recipes.
- `references/string-expansion-budgets.md` — real per-language, per-length expansion percentages,
  and the locale-formatting (number/date/currency/percent) reference.
- Pairs with `01-typography-and-fonts/font-selection-and-pairing` (script coverage),
  `03-layout-grid-and-composition/responsive-and-adaptive-layout` (overflow is a sibling problem),
  `08-motion-and-interaction` (mirrored motion), and `accessibility-wcag-2-2-compliance`
  (`lang`/`dir`, reflow). Enforced one last time by `design-qa-and-pre-launch-review`.
<!-- dual-compat-end -->
