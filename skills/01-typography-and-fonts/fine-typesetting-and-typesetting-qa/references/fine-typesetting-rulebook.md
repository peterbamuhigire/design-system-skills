# Fine Typesetting Rulebook

Parent skill: [`../SKILL.md`](../SKILL.md) (`fine-typesetting-and-typesetting-qa`).

**When to read:** before setting paragraph and character styles for any long document, and again
when running the QA pass in section 7. Each rule is a default with the condition under which a
deliberate exception is allowed. Rules are paraphrased practice from human design authorities
(Adams, Dawson, Foster and Seddon, *Graphic Design Rules*, Frances Lincoln, 2012, revised edition;
Bringhurst, *The Elements of Typographic Style*). Numbers are working defaults, not standards;
test them on the rendered page.

**Face choice is out of scope here.** Source books sometimes recommend era-specific faces or free
font services. Never adopt that advice. Faces come only from `font-selection-and-pairing`, the
engine catalogue and the banned list in `doctrine/references/ai-slop-banned-fonts.md`.

---

## 1. Hierarchy: one change per level

1. Fix the body style first: one face, size, weight, colour and case.
2. For each level above body, change exactly **one** attribute: size, weight, colour or case.
3. For a further level, change a different single attribute, or take a clearly larger step of the
   same attribute. Stop when the reader can tell levels apart at a glance.
4. Test: squint at a spread. If you can count more than four distinct text "greys", there are too
   many levels.

| Level | Example change from body (body = 10.5/15 pt text face, black, sentence case) |
|---|---|
| Subhead (H3) | Same size, bold only |
| Section head (H2) | Larger size only (for example 14 pt), same weight as body |
| Chapter head (H1) | Larger again (for example 24 pt), same face |
| Running label or kicker | Small capitals or capitals with +50 to +100 tracking, same size as body |

**Exception:** posters, event graphics and expressive campaign work may break this rule when
controlled noise is the concept. Record the reason in the design rationale.

## 2. Family and style gates

- **Economy:** normally one serif and one sans per project, each with a defined role. Never pair
  two faces that are nearly the same (two old-style serifs, two neutral grotesques); the result
  looks like an error.
- **Completeness:** the body family needs a true italic, a real bold and every weight the
  hierarchy uses. Check before the editor asks for italics the family lacks.
- **No fakes:** no slanted roman as italic, no stroked or synthesised bold, no horizontal or
  vertical scaling, no filter effects on type. Use real condensed, extended or bold cuts.
- **Display cuts at display sizes only;** they are drawn for large sizes and may lack full
  character sets.
- **Scripts and novelty faces** never carry body copy. Kern script lines by metrics, then by eye.
- **Free fonts** are checked for complete character sets, kerning and licence before commitment;
  broken free fonts tend to surface at final PDF stage.

## 3. Spacing

| Item | Default | Adjust when |
|---|---|---|
| Leading (body) | About 120 per cent of type size | Large x-height or long measure: more; small x-height or short measure: less |
| Leading consistency | Constant within a paragraph | Never vary leading to fit copy |
| Body tracking | Zero | Move within about +/-25 thousandths of an em, only to repair a bad break |
| Negative tracking | Display sizes only | Never so tight that letters touch |
| Kerning | Font metrics below about 14 pt | Kern headlines and display lines manually; watch pairs without vertical side stems (A, T, V, W, Y) |
| Word spacing (justified) | Desired 100 per cent; allowed range set in the style | Tighten or widen the range only after hyphenation is set |
| Leading for projection | Slightly more open than print | Too open and list items look unrelated |

## 4. Paragraph shape

1. **Rag (ragged-right):** the second line should not be much shorter than the first; the
   penultimate line should be longer than the last. Avoid a regular zig-zag of long-short lines.
2. **Weak line endings:** avoid ending a line on a one- or two-letter word ("a", "is", "it", "to")
   when a break can be moved. Read the paragraph aloud to catch them; bind with a non-breaking
   space where the tool allows.
3. **Hyphenation thresholds:** minimum word length 7 characters; at least 4 before and 3 after the
   break; no more than two consecutive hyphenated lines (Bringhurst); never hyphenate a proper
   name, a URL or the last word of a paragraph.
4. **Ragged-right default:** no hyphenation. **Exception:** short measures with long words (for
   example narrow sidebar columns, Kiswahili or technical text).
5. **Justified text:** avoid on short measures. Fix rivers with hyphenation first, then with small
   tracking moves. Keep letter-spacing at 0 per cent. Never use "justify all lines" as a default.
6. **Widows and orphans:** define the terms in the house style, because usage varies. Working
   definitions for this engine: an **orphan** is a lone word or short final line ending a
   paragraph, or a paragraph's first line stranded at the foot of a column; a **widow** is a
   paragraph's last line carried alone to the top of the next column or page. Eliminate both.
   Fix order: tracking within limits, then a soft return, then ask the editor to cut or add.
7. **Paragraph separation:** indent **or** add space, never both. Do not indent the first
   paragraph of a section, the paragraph after a heading or the paragraph after a break. Set the
   indent in the paragraph style (about one em), never with tabs or spaces.
8. **Alignment systems:** do not mix centred and flush-left text in one layout; choose a
   symmetrical or an asymmetrical system (Tschichold's principle, as restated by Adams).
9. **Lists:** hang turnover lines so wrapped text aligns with the text, not with the bullet.
10. **Drop caps:** set the first few words after the drop cap in small capitals as a bridge into
    the text; align the cap to the baseline of its last line.
11. **Headings:** keep a heading with the next paragraph ("keep with next"); no heading as the
    last line of a column.

## 5. Characters and punctuation

- **Figures:** oldstyle (text) figures in upper-and-lower-case running text where the face has
  them; lining figures with capitals; tabular lining figures in tables, financial statements and
  anything that must align. Features: `onum`, `lnum`, `tnum`, `pnum` (see
  `variable-fonts-and-opentype-features`).
- **Optical balance:** a serif italic can read smaller than its roman at body size; check it and
  enlarge slightly (about half a point) only if the face needs it. A sans word inside serif text
  may need to be set slightly smaller so it does not shout.
- **Quotes and apostrophes:** typographer's (curly) quotes and apostrophes. Primes (straight) only
  for feet, inches, minutes and seconds. Watch elided years and words:
  ’26 takes an apostrophe (’), not an opening quote (‘).
- **Dashes:** unspaced en dash for ranges (2024–2026, pages 12–18, the Kampala–Jinja road); one dash
  style for parenthetical breaks per house style (see the locale file). Hyphens only inside words.
- **Ellipsis:** the single ellipsis character or three spaced points per house style; add a full
  stop after an ellipsis that ends a sentence only if the house style says so.
- **Emphasis:** italics, not underlining (underline means "link" on screen). Bold for
  navigation-level emphasis only.
- **One space** after a full stop.
- **Accents and diacritics:** spell names and places correctly, including French accents in work
  for Rwanda, Burundi and DRC. Copy and paste supplied names; never retype them.
- **Fractions:** use the font's fraction glyphs or the `frac` feature, never "1/2" built from
  full-size figures in finished text.
- **Capitals:** no long passages in capitals. Short capital labels get added tracking.
- **Hanging punctuation:** hang opening quotation marks and bullets outside the text edge on pull
  quotes and display lines (optical margin alignment in layout tools).

## 6. Legibility thresholds

| Situation | Rule |
|---|---|
| Small type reversed out of a dark solid in print | Avoid light weights and sizes around 6 pt; ink fill-in closes counters |
| Coloured small type in print | Build it with at least one process plate at 100 per cent so edges stay sharp |
| Body text in pure cyan, magenta or yellow | Do not; use black or a dark tone |
| Reversed text in general | Short doses only (headlines, labels, panels), not whole pages |
| Screen body text | Never smaller than the platform's readable default; see `doctrine/references/wcag-2.2-criteria.md` for contrast and resize |
| Projected slides | Test legibility from the farthest seat; see `deck-system` room guidance |

## 7. Typesetting QA pass (run on the rendered output)

Mark each item pass, fix, or n/a, and log page/line, rule, fix and owner.

1. At most one serif and one sans; full families with true italics and bolds.
2. No faux italic, synthesised bold, scaled type or effects on text.
3. Hierarchy changes one attribute per level; four or fewer text "greys".
4. Measure within 45–75 characters for body (see `editorial-and-long-form-layout`); leading about
   120 per cent, adjusted for x-height.
5. Paragraph separation by indent or space, not both; no indent after headings.
6. Rag: no stalled second lines, penultimate longer than last, no weak line endings.
7. Hyphenation: 7/4/3 thresholds, at most two consecutive, none in display text.
8. No widows or orphans under the house definitions.
9. Justified text (if any) has no rivers and no letter-spaced lines.
10. Figures: oldstyle in prose where available, lining with capitals, tabular in tables.
11. Curly quotes and apostrophes; primes only for units.
12. Locale punctuation, spelling, dates and currency follow the house-style sheet.
13. En dashes for ranges; one parenthetical dash style throughout.
14. Correct accents, real fractions, one space after full stops, italics for emphasis.
15. Hanging punctuation on pull quotes; headlines kerned.
16. Headings kept with the following paragraph; no stranded heading at a column foot.
17. Legibility thresholds for the medium pass (section 6).

**Ship rule:** any fail on items 1, 2 or 12 blocks a client-facing release. Other fails are
fixed before send unless the owner accepts them in writing.

## 8. Tool settings

| Tool | Where the rules live | Notes |
|---|---|---|
| Microsoft Word | Paragraph styles: widow/orphan control, keep with next, hyphenation zone and consecutive-hyphen limit, first-line indent; Font dialog: OpenType figure style where the build supports it | Word's own "widow/orphan control" covers single lines only; still inspect the render |
| InDesign or Affinity Publisher | Paragraph styles: hyphenation (min word, before/after, limit), justification ranges, keep options, optical margin alignment; character styles for figures | Use the paragraph composer for body text and check its results |
| CSS | `hyphens: auto` with a correct `lang` attribute; `font-variant-numeric`; `text-wrap: pretty` or `balance` for headings; `hanging-punctuation` | Support for `hyphenate-limit-chars`, `text-wrap` values and `hanging-punctuation` varies by browser. Check the current compatibility tables before relying on them and keep a readable fallback |
| PowerPoint or Google Slides | Master text styles with fixed sizes, spacing and bullet indents | Do not accept autofit shrinking body text below the room legibility size |
