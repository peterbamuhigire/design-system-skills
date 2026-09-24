# Content by Relationship Stage, Words-First Flows and Reading Patterns

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-writing-and-microcopy`). Also used by
`voice-tone-and-content-style-guide`, `error-empty-and-system-messaging` and
`journey-mapping-and-service-design`.

**When to read:** when planning which content a product needs across a customer relationship,
when designing a flow from its words before its screens, when deciding what goes first in a line
or block, and when writers need domain knowledge from experts.

## 1. Content by relationship stage

Every piece of product text serves two goals at once: the organisation's and the person's.
Name both at each stage; if either is missing, the text is not ready.

| Stage | Organisation aims to | Person aims to | Content that does the work |
|---|---|---|---|
| Discovery | Attract | Investigate | Search snippets, store listing, landing page, referral message |
| Decision | Convert | Verify, then commit | Prices and fees, proof, plan comparison, sign-up and payment text |
| Start | Onboard | Set up | Setup steps, permission requests, first-run guidance, empty states |
| Everyday use | Engage | Use | Titles, labels, buttons, descriptions, notifications |
| Trouble | Support | Fix | Errors, status messages, help, support replies |
| Loyalty | Transform the person's situation | Prefer, then champion (recommend to others) | Progress and milestones, receipts that show value, review and referral prompts |

Transformation comes from value the product delivers, not from flattering copy. Map these stages
onto the journey map (`journey-mapping-and-service-design`) so content owners are named per stage.

## 2. Words-first flow design

1. State the intention: what the person wants and what the organisation wants from this flow.
2. Act it out. One person plays the product as a courteous host; another plays a user with a
   real goal. Speak the exchange aloud and improvise until it is polite and efficient. Record it.
3. Write it as a two-column message thread: the product's lines on one side, the person's
   replies on the other.
4. Convert: product lines become titles, labels and descriptions; the person's lines become
   buttons, options and inputs.
5. Wireframe last, placing the agreed text into layout. "Conversational" means respecting
   turn-taking, not a casual register.

Best for sign-up, payment, booking, lending, support and chat or agent interfaces.

## 3. Reading patterns and what to do about them

| Pattern | Behaviour | Response |
|---|---|---|
| F-shape | Top lines read, then a scan down the left edge | Key word first in headings, list items and labels |
| Z-shape | Sparse pages: top left, across, diagonally down, across | Promise top left, action bottom right |
| Ping-pong | Eyes jump between paired columns (label and value, question and answer) | Keep pairs aligned, short, one idea per row |
| Lawnmower | Row by row across tables | Stable column order; scannable first cells |
| Bypassing | Lines starting with the same words are skipped | Vary first words; do not open every item with "You can" |

These are observed tendencies from eye-tracking research, not laws. Front-load meaning and make
each title and its call to action understandable read alone.

## 4. Working with subject-matter experts

The writer is the expert in product language, not in medicine, finance, law or agronomy.
1. Name the expert for each domain area and agree how and when to consult them.
2. Learn the field's conventions and regulated terms before drafting.
3. Draft against UX guidelines; the expert checks accuracy, the writer owns clarity and voice.
4. Escalate unresolved conflicts to the product owner.
5. Add agreed terms to the style guide's terminology list.
6. Zoom out: fit each set of strings to its template, since the structure around the words
   matters as much as the words.

For how strong a guideline's evidence is (testing, trial and error, consensus, common sense) and
when to override it, see `breaking-best-practices.md`.

## 5. Example (original)

A Kigali bus-ticket app designs seat booking words-first. In the role-play the "host" asks "Where
are you travelling, and on which day?"; the passenger answers "Musanze, Saturday morning". The
thread becomes the title "Where to, and when?", a destination field and a date chip row, before
any screen is drawn. The confirmation screen is checked for ping-pong reading: fare, seat and
departure are aligned label-value pairs.

Sources: two-goal stage model after Podmajersky, *Strategic Writing for UX* (virtuous cycle) and
the words-first role-play method from the same book; reading patterns from Nielsen Norman Group
eye-tracking studies as taught in Ben-David, *The Fundamentals of UX Writing*; expert
collaboration after Ben-David.
