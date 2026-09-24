# Cultural Adaptation Beyond Translation

Parent skill: [`../SKILL.md`](../SKILL.md) (`internationalization-and-rtl-design`).

**When to read:** when a product moves into a new culture or community, not only a new language;
when a design team from one context designs for another (for example a Nairobi or London team
designing for rural Uganda); when icons, colours, imagery, names, forms, trust signals or
interaction conventions were chosen by the designers' own habits; and before a localisation
review signs off a market launch.

Translation and locale formatting are owned by the parent skill and
`string-expansion-budgets.md`. This file covers what translation does not fix: meaning,
convention, social norms and trust. Low-literacy and low-bandwidth decisions live in
`inclusive-and-assistive-design/references/low-literacy-low-bandwidth-and-emerging-market-design.md`.

---

## 1. Principles

1. **Culture is not the same as country.** A profession, an ethnic community, a religious group,
   an age cohort or a remote community can each carry their own conventions. Define the cultural
   group by shared practice, not by a flag.
2. **Dimension models are hypotheses, not verdicts.** National-culture scores (power distance,
   uncertainty avoidance, individualism) can suggest questions to test. They must never be used
   to stereotype a person or to skip research.
3. **Needs, values and capabilities, at three levels.** For each design decision ask what the
   individual needs, what their household or family expects, and what their community permits or
   rewards. Many East African decisions (school fees, health, land, savings) are family or group
   decisions even when one person holds the phone.
4. **Adapt meaning, then words.** A correctly translated screen can still be wrong if its images,
   examples or metaphors carry the wrong meaning.
5. **Co-design with the community, and let them own the result.** Decisions about symbols,
   language and representation of a community belong substantially to that community.

## 2. Cultural adaptation audit

Walk every screen and asset through the table. Record Keep / Adapt / Replace with evidence and who
confirmed it (a named local reviewer, a test session). Anything confirmed only by the design team
is `NOT_ASSESSED`.

| Area | Question | Typical failure | Adaptation route |
|---|---|---|---|
| Icons and metaphors | Does each icon's meaning survive here? | Mailbox, piggy bank, shopping trolley, owl, thumbs-up used as if universal | Test icons with the target group; prefer local objects (a phone, a receipt slip, a market stall) and always pair with a word |
| Colour meaning | Do status and brand colours carry intended meaning? | Assuming red = danger and green = success everywhere; party-political colours in a civic product | Never let colour carry meaning alone; check political and religious associations with local reviewers before choosing brand and status colours |
| Imagery and people | Do people see themselves, with dignity? | Stock images of other countries; poverty imagery; staged "happy farmer" clichés | Commission or select locally, with consent; see `photography-art-direction` |
| Names and forms | Can people enter their real names, places and identifiers? | "First name / Last name" forced; surname assumed to be family name; required postcode | Single full-name field or flexible fields; district/sub-county/village pickers; national ID formats validated with current registry rules |
| Numbers, money and dates | Are formats correct and unambiguous for this locale? | Decimals shown for UGX; "03/09" read two ways | Use CLDR-backed formatting (parent skill); show ISO currency code at commit; month names for high-stakes dates |
| Time and sequence mappings | Do direction and order match local mental models? | Timelines, sliders and "next" arrows assumed to run left to right for every script and group | Check reading direction and how time and progress are spoken about locally; test mapping-sensitive controls |
| Address and location | Can people describe where they are? | Street-address-only fields where landmarks are the norm | Landmark field, map pin, and "near" descriptions |
| Social conventions | Does the interaction respect local etiquette? | Casual tone to elders; assuming a woman will speak to a male provider; public display of sensitive status | Tone map per audience (`voice-tone-and-content-style-guide`); provider-choice options; private-by-default states |
| Trust signals | What makes this trustworthy here? | Western-style security badges and testimonials | Known institutions, licensing, physical presence (agent, branch, school), named people, clear fees |
| Calendar and cycles | Do deadlines follow local rhythms? | Monthly billing where income is seasonal (harvest) or school-term based | Term-based, harvest-based or weekly plans where evidence supports them |
| Humour, idiom and examples | Do examples land, or offend? | Imported jokes, sports, food and holiday examples | Local examples written by or with native speakers |

## 3. Locale formatting facts to design around (East Africa)

Verified with Node.js 24.8.0 `Intl` (ICU/CLDR data) on 2026-09-24; re-verify when the runtime or
CLDR version changes:

| Locale | Currency sample for 1,450,000.5 | Short date for 3 September 2026 | Design consequence |
|---|---|---|---|
| `en-UG` | `USh 1,450,001` | `03/09/2026` | UGX shows no decimals; never display cents; day-first dates |
| `lg-UG` (Luganda) | `1,450,001 USh` | `03/09/2026` | Symbol follows the number; allow for it in layout |
| `en-KE`, `sw-KE` | `Ksh 1,450,000.50` | `03/09/2026` | Two decimals displayed |
| `sw-TZ` | `TSh 1,450,000.50` | `03/09/2026` | Two decimals displayed |
| `rw-RW` | `RF 1.450.001` | `2026-09-03` | Period as group separator; ISO-style short date |

Rules: never hard-code separators or symbol position; show the ISO code (UGX, KES, TZS, RWF) on
cross-border and confirmation screens; round according to the currency's minor units, and state
rounding when it changes an amount the user entered.

Language notes to verify per product: Uganda's Constitution (Article 6) names English as the
official language and Kiswahili as the second official language for uses Parliament prescribes;
everyday product language is frequently Luganda, Runyankore-Rukiga, Acholi, Lusoga, Ateso or
others depending on region. Choose languages from user research, not from national status alone.

## 4. Procedure

1. Define the cultural group(s) by practice and place, and name who in that group will review.
2. List every meaning-bearing element: icons, colours, images, examples, names, forms, tone,
   trust signals, calendar assumptions.
3. Run the audit (section 2) with at least one local reviewer; mark each element Keep / Adapt /
   Replace with the reviewer's note.
4. Test the riskiest adaptations (icons for critical actions, trust messaging, mapping-sensitive
   controls) with representative users, in their language, on their devices.
5. Record decisions in the design system as locale variants (tokens, icon sets, content
   patterns), not as one-off overrides.
6. Re-audit after any brand refresh or new-market launch.

## 5. Worked example (original): a savings-group ledger app across Uganda and Rwanda

A village savings and loan association (VSLA) app built first for groups in Masaka district is
extended to groups in Rwanda.

| Element | Uganda decision | Rwanda finding | Adaptation |
|---|---|---|---|
| Amounts | `USh 250,000`, no decimals | `RF` with period grouping | Locale formatting from CLDR; ISO code on share-out screen |
| Meeting cycle | Weekly meetings, share-out at year end | Same cycle, different local names for roles | Role labels from the group's own vocabulary, editable by the group |
| Lock-box icon | Tested well in Masaka | Recognised, but groups call it by a different name | Keep icon; replace label |
| Member list | Sorted by first name | Groups preferred membership number order, as in their paper ledger | Default sort follows the paper ledger the group already trusts |
| Trust | Photo of the group's own meeting place on the home screen | Same | Keep: familiar place, not stock imagery |

The finding that mattered most was the paper ledger: matching its order and terms let groups check
the app against the book they already trusted.

## 6. Premium versus generic output

| Generic | Senior |
|---|---|
| Translates strings and calls it localised | Adapts meaning, convention and trust, then translates |
| Uses national culture scores as design rules | Uses them as questions, confirmed by local research |
| Global stock imagery and icon sets | Locally tested symbols and commissioned imagery with consent |
| Hard-coded "Shs" and decimals | CLDR formatting, ISO code at commit, rounding stated |
| The design team decides what the community means | Community reviewers and co-designers sign off meaning |

## Evidence and currentness

Accessed 2026-09-24.
- Locale output: Node.js v24.8.0 `Intl.NumberFormat` and `Intl.DateTimeFormat` (bundled ICU/CLDR),
  run locally on 2026-09-24. Results can change with CLDR releases; re-run before specifying.
- Uganda Constitution, Article 6 (ULII consolidated text; Parliament of Uganda news on the
  Kiswahili Council). Current implementation status of Kiswahili in government services is
  `NOT_ASSESSED`.
- National ID validation rules and address registries: `NOT_ASSESSED`; confirm with the current
  issuing authority before specifying validation.
- Concept inputs: Lahiri, Prabhu and Schaffer (eds) (2026) *Innovative Solutions: Advanced User
  Experience Design*, 2nd edn, CRC Press (culturally appropriate responsible design;
  needs-values-capabilities at individual, family and community levels; participatory design
  with communities); Norman (2013) *The Design of Everyday Things*, Basic Books (cultural
  constraints and culturally variable mappings).
