# UK and East African Punctuation and Locale Defaults

Parent skill: [`../SKILL.md`](../SKILL.md) (`fine-typesetting-and-typesetting-qa`).

**When to read:** when a document has no house style, when writers and designers disagree about
punctuation, or when a document mixes English with Kiswahili, Luganda or French. The client's own
style guide always wins; these are the agency defaults for English-language work in Uganda,
Kenya, Rwanda, Tanzania and neighbouring markets, which generally follow British conventions.
Authority: *New Hart's Rules* (Oxford University Press) for British practice; the French
conventions below are standard French typographic practice. Confirm any client- or
publisher-specific rule before release.

---

## 1. House-style sheet (fill one per document)

| Item | Agency default | Alternative the client may choose |
|---|---|---|
| Spelling | British (-ise, colour, programme, centre, licence as noun) | Oxford -ize spelling; record it if chosen |
| Primary quotation marks | Single curly quotes, double for a quote within a quote | Double first, single nested |
| Punctuation with closing quotes | Outside, unless it belongs to the quoted words | None for British work; US "inside" style is not used |
| Parenthetical dash | Spaced en dash ( – ) | Unspaced em dash (—); never both in one document |
| Ranges | Unspaced en dash (2025–2026, 09:00–17:00) | "from … to …" in running prose |
| Dates | 23 September 2026 (no ordinal, no comma) | 23/09/2026 in tables; ISO 2026-09-23 in data exports |
| Times | 2.30 pm or 14:30 | One style per document |
| Currency | ISO code, space, figure: UGX 50,000; KES 1,200; RWF 10,000; TZS 25,000; USD 1,500 | Local symbol (USh, KSh) only if the client uses it consistently |
| Large numbers | Comma thousands separator, full stop decimal: 1,250,000.50 | Spell out "million" in prose: UGX 4.5 million |
| Per cent | "per cent" in running prose; % in tables and charts | % throughout for data-heavy documents |
| Abbreviations | No full stop after contractions (Dr, Mr, Ltd); full stops in e.g. and i.e. or none, per house choice | Record the choice |
| Serial (Oxford) comma | Only where it prevents ambiguity | Always, if the client prefers |
| Capitals in headings | Sentence case | Title case for formal institutional clients |

## 2. Quotation handling

- British order: 'The board approved the plan', she said. (Comma outside, because it is not
  part of the quotation.)
- When a complete quoted sentence ends the sentence, the full stop may sit inside:
  He wrote: 'We will deliver in March.'
- Long quotations (roughly more than 40 words) are displayed as block quotes without quotation
  marks.

## 3. Names, places and languages

- Spell names of people, places, institutions and currencies exactly as the owner spells them.
  Paste from the approved source; never retype.
- Kiswahili and Luganda text rarely needs diacritics, but it does need correct word division.
  Use a hyphenation dictionary for the language, or switch hyphenation off for that text.
- Mark each language in the file (Word language setting, HTML `lang`) so spell-check,
  hyphenation and screen readers behave.
- French text for Rwanda, Burundi and DRC:
  - guillemets « » with a non-breaking thin space inside;
  - a non-breaking thin space before ; : ! and ?;
  - accented capitals are kept (É, À);
  - decimal comma and space thousands separator in French-language documents (1 250 000,50),
    unless the client specifies otherwise.

## 4. Titles and forms of address

- Honorifics and protocol lines in speeches and formal documents follow the client's protocol
  office. Do not "correct" protocol order for style.
- Keep official names of ministries, agencies and statutes exactly as gazetted.

## 5. Checks before release

1. One spelling variant throughout (search for -ize/-ise and -or/-our pairs).
2. Quote marks all curly and of the chosen primary style.
3. No mixed dash styles; ranges use en dashes.
4. Dates, times and currency follow the sheet.
5. Language tags set for every non-English passage.
