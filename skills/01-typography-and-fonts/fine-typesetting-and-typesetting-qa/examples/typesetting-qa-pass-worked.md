# Worked example: typesetting QA pass on a co-operative annual report

An illustrative, fictional client used to show the method. Nothing here is a real organisation's
data.

## Brief

- **Document:** 2025 annual report of "Nakawa Teachers' Savings and Credit Co-operative" (a
  fictional Kampala SACCO), 32 pages, A4, printed digitally and circulated as PDF on WhatsApp.
- **Faces (already chosen through `font-selection-and-pairing`):** Source Serif 4 for text and
  headings, Public Sans for tables, labels and captions. Reason recorded there: an institutional
  serif that holds long reading for members, with a quiet sans for data.
- **Alignment:** ragged-right body, 11/15.5 pt, measure about 68 characters.
- **House style:** none supplied, so the agency default from
  `references/uk-east-african-punctuation-and-locale.md` applies and is marked for the
  chairperson's confirmation.

## Findings on pages 4-5 (chairperson's statement and financial highlights)

| # | Location | Rule | Before | Fix | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | p4 H1 | One change per level | H1 in the sans, bold, capitals, green, 28 pt | Serif, regular weight, sentence case, black, 26 pt: size is the only change | Designer | Closed after re-render |
| 2 | p4 H2 | One change per level | H2 bold and green and larger | Same size as body, bold only | Designer | Closed |
| 3 | p4 para 1 | No indent after heading | First paragraph indented and spaced | Indent removed; paragraphs separated by indent only | Designer | Closed |
| 4 | p4 para 3 | Rag | Second line stalled at about half the first line's length | One soft return moved in the style-safe way; rag re-checked | Designer | Closed |
| 5 | p4 para 5 | Weak line ending | Line ended on "a" before "record year" | Non-breaking space between "a" and "record" | Designer | Closed |
| 6 | p4 last line | Orphan (house definition) | "members." alone on the last line | Tracking -10 on the paragraph; single word pulled back | Designer | Closed |
| 7 | p4 | Quotes | Straight quotes around the motto "Save today, teach tomorrow" | Single curly quotes: 'Save today, teach tomorrow' | Designer | Closed |
| 8 | p4 | Punctuation with quotes | "…tomorrow," she said (comma inside) | 'Save today, teach tomorrow', she said | Editor | Closed |
| 9 | p4 | Dates | September 23rd, 2025 | 23 September 2025 | Editor | Closed |
| 10 | p5 table | Figures | Proportional oldstyle figures in the loans table | Tabular lining figures (`tnum`, `lnum`), decimal-aligned | Designer | Closed |
| 11 | p5 table | Currency | Ugx 1.2B, Shs 450m mixed | UGX 1,200,000,000 in the table; "UGX 1.2 billion" in prose | Editor | Closed |
| 12 | p5 | Ranges | 2023-2025 with a hyphen | 2023–2025 with an en dash | Designer | Closed |
| 13 | p5 caption | Faux style | Caption italic was the roman slanted by the layout tool (the sans had no italic installed) | Installed Public Sans Italic; re-exported | Designer | Closed |
| 14 | p5 pull quote | Hanging punctuation | Opening quote pushed the text in | Optical margin alignment on for pull quotes | Designer | Closed |
| 15 | p5 para 2 | Copy change needed | A widow ("growth.") could only be removed by cutting three words | Flagged to the editor with two cut options | Editor | Open, blocked on editor |

## House-style sheet issued with the report

| Item | Setting |
|---|---|
| Spelling | British (-ise) |
| Quotes | Single curly, double nested; punctuation outside unless part of the quote |
| Parenthetical dash | Spaced en dash |
| Dates | 23 September 2025; tables 23/09/2025 |
| Currency | UGX 1,200,000,000 in tables; UGX 1.2 billion in prose |
| Per cent | "per cent" in prose, % in tables |
| Headings | Sentence case |
| Status | Agency default; awaiting chairperson confirmation |

## Result

Fourteen of fifteen findings closed after re-render. One item stays open and blocks final print
until the editor chooses a cut. The QA log, the house-style sheet and the re-rendered pages are
attached to the release record. No claim is made about reader response; that has not been
measured.
