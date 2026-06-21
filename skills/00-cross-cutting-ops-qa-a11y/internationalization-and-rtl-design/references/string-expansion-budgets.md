# String Expansion Budgets — real % growth by language, and locale formatting

**Scope:** how much horizontal/character space a translated string needs relative to its English
source, and how numbers/dates/currency/percent change shape by locale. Use these budgets to size
containers *before* translation exists — never a single flat guess.

> **The core mistake this file prevents:** budgeting one flat "+30%" for everything. Short UI
> strings (buttons, labels, menu items) routinely grow **+200–300%**; long paragraphs grow far
> less; CJK *contracts*. Budget by **length band**, not one number.

---

## 1. Expansion is inversely proportional to source length

The shorter the English source, the larger the percentage growth (a 1-word label has no slack to
average out a long compound word in another language). Industry/IBM-style guidance:

| English source length | Recommended space to reserve (worst case) |
|---|---|
| Up to **10 characters** (most buttons, labels, menu items) | **+200% to +300%** (i.e. 3–4× the width) |
| **11–20 characters** | **+180%** (≈ 2.8×) |
| **21–30 characters** | **+160%** |
| **31–50 characters** | **+140%** |
| **51–70 characters** | **+170%**… use **+70%** as a practical paragraph average |
| **Over 70 characters** (running text/paragraphs) | **+30% to +35%** |

So: a 6-character button (`"Save"`, `"Submit"`) must tolerate ~3× its width; a 300-character
paragraph only needs ~+35%.

---

## 2. Worst-case expansion by target language (vs English source)

Use the higher end for short strings, the lower (running-text) figure for paragraphs.

| Target language | Typical running-text expansion | Notes / worst case on short strings |
|---|---|---|
| **German** | +30% to +35% | Long compound nouns can blow a single label by +100%+ (`Settings`→`Einstellungen`, `Cancel`→`Abbrechen`). |
| **Finnish** | +30% to +40% | Agglutinative; long words, few spaces to wrap on. |
| **Dutch** | +25% to +35% | Compounds, like German. |
| **Russian / Cyrillic** | +20% to +30% | Plus wider glyphs. |
| **French** | +15% to +30% | `Save`→`Enregistrer`, `Settings`→`Paramètres`. |
| **Spanish / Italian / Portuguese** | +15% to +30% | Romance verbosity. |
| **Polish / Czech** | +20% to +30% | Plus diacritics affecting line-height. |
| **Greek** | +10% to +20% | — |
| **Arabic** | ~+25% on average, but **variable** | RTL; also taller line-height; some strings contract. |
| **Hebrew** | often similar or slightly shorter | RTL; budget for tall diacritics. |
| **Japanese / Chinese (CJK)** | **−10% to −30% (CONTRACTS)** | Fewer characters, but each is *wider/taller* — budget **height/line-height**, not width; min font sizes are larger for legibility. |
| **Korean** | roughly neutral to slight contraction | Mind line-height. |
| **Thai / Khmer** | width-neutral, but **no spaces** | Cannot wrap on spaces; needs special line-breaking; tall stacking diacritics raise line-height. |

> **CJK is not "negative expansion you can ignore."** It contracts *width* but demands larger
> minimum glyph sizes and more *vertical* room. Plan rows/line-height, not just columns.

---

## 3. Practical budgeting rules

1. **Buttons, labels, nav, menu items, tooltips, badges:** reserve **2.5–3×** the English width, OR
   let them wrap to two lines. Never fix their width to the English string.
2. **Form labels & helper text:** allow wrapping; do not assume single line.
3. **Paragraphs / descriptions:** reserve **+35%** height; they wrap naturally, so width matters less.
4. **Tables:** the worst case — narrow columns + short headers. Allow header wrap, min-width per
   column, or a responsive card fallback. German/Finnish headers break tables most often.
5. **Truncation:** last resort only; always pair with full text on hover/focus/`title`.
6. **Vertical rhythm:** raise line-height for Arabic, Thai, Devanagari, Vietnamese (stacked
   diacritics) — a Latin-tuned line-height clips them.

---

## 4. Pseudo-localization — test expansion with zero translations

Generate a fake locale that simulates the worst case before any translator is hired:

- **Accent every letter** (`Settings` → `Ŝéttîngs`) → exposes characters your font/encoding can't render.
- **Pad length ~+40%** (or per §1 band) → exposes tight boxes and clipping.
- **Bracket each string** (`[!! Settings !!]`) → makes any truncation/clipping instantly visible.
- Optionally **reverse to fake-RTL** to smoke-test direction.

If the UI survives pseudo-localization, it will survive most real translations.

---

## 5. Formatting that changes by locale (number / date / currency / percent)

**Never hand-roll these.** Use the platform i18n API: web `Intl.NumberFormat` /
`Intl.DateTimeFormat`; ICU/CLDR-backed APIs on other platforms. CLDR is the canonical data source.

### Numbers
| Locale | 1234567.89 renders as |
|---|---|
| en-US / en-GB | `1,234,567.89` |
| de-DE | `1.234.567,89` (period groups, comma decimal) |
| fr-FR | `1 234 567,89` (narrow-no-break-space groups, comma decimal) |
| ar-EG | `١٬٢٣٤٬٥٦٧٫٨٩` (Arabic-Indic digits, own separators) |
| en-IN | `12,34,567.89` (lakh/crore grouping — 2-then-3) |

### Dates
| Locale | 2026-03-09 conventionally |
|---|---|
| en-US | `3/9/2026` (M/D/Y) |
| en-GB / most of EU | `09/03/2026` (D/M/Y) |
| ja-JP / zh-CN / ISO | `2026/03/09` or `2026年3月9日` (Y/M/D) |
> The same `03/09` is **two different dates** across US vs UK — always format via the API, and
> prefer unambiguous formats (month name or ISO) in data-sensitive contexts. Also: 12h vs 24h
> clock, first day of week (Sun vs Mon), and non-Gregorian calendars (Hijri, etc.) are locale-driven.

### Currency
- Symbol **position** and spacing differ: `$1,234.56` (en-US) vs `1.234,56 €` (de-DE) vs
  `CHF 1’234.56` (de-CH) vs `١٬٢٣٤٫٥٦ ر.س` (ar).
- `$` ≠ USD (also CAD, AUD, MXN…). Show the **ISO 4217 code** (USD, EUR, UGX, KES) where ambiguity
  matters. Use `Intl.NumberFormat(locale, { style: 'currency', currency: 'EUR' })` — it places the
  symbol correctly for the locale.

### Percent & units
- `style: 'percent'` and `style: 'unit'` in `Intl.NumberFormat` handle `50 %` vs `50%` spacing and
  metric/imperial unit display per locale. Do not concatenate `+ "%"` manually.

### Names, addresses, plurals
- **Names:** family-name-first in many locales; don't assume "First Last" or split into two fields rigidly.
- **Addresses:** field order, postal-code format, and presence/absence of state vary — use a
  flexible address model, not a US-shaped form.
- **Plurals:** languages have **1–6 plural categories** (Arabic has 6: zero/one/two/few/many/other;
  English has 2). Use **ICU MessageFormat `plural`** — never `if (n === 1)`.

---

## Provenance
Expansion bands follow IBM Globalization / W3C i18n and CLDR-aligned industry guidance; formatting
follows Unicode CLDR and the ECMAScript `Intl` (ECMA-402) API. Per the Chwezi design doctrine,
sizing space and formatting data are design constraints from the first layout, not a late retrofit.
