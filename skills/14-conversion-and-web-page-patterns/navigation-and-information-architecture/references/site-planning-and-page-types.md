# Site Planning and Page-Type Contracts

Parent skill: [`../SKILL.md`](../SKILL.md) (`navigation-and-information-architecture`).

**Load when:** a website (not an app shell) is being planned from scratch or rebuilt, and the team
must turn a brief into a page inventory before any sitemap, navigation or layout work; or when a
single page type (About, Contact, FAQ, 404, service detail) needs a design contract.

This file covers the step *before* `ia-patterns.md` (it produces the inventory that IA organises)
and the page types *other than* conversion landing pages, which belong to
`landing-page-and-conversion-design`. Copy for each page type belongs to website-skills
`content-writing`; this file fixes what each page must *contain and look like*.

---

## 1. Inputs

| Input | Who supplies it | If missing |
|---|---|---|
| Outcomes the site must produce (enquiries, bookings, donations, applications, fewer support calls), each with a measure | Client owner | Stop. A site without a measurable outcome cannot be prioritised |
| Jobs the site must do (catalogue, booking desk, publisher, support desk, credential) | Client and strategist | Infer a draft, mark it as an assumption, confirm before the sitemap |
| Audience segments and the problem each brings, in their own words | Discovery interviews, support logs, search terms | Run five short interviews or read the last 50 enquiries |
| Key facts visitors need before acting (price range, hours, location, payment methods, service area) | Front-desk or sales staff | Ask staff to list the ten questions they answer most |
| Content owner and update rhythm | Client | Exclude any page type that needs a rhythm nobody owns |

## 2. Procedure: brief to page inventory

1. **Separate outcomes from jobs.** "More clinic bookings" is an outcome; "an online booking
   desk" is a job. Every page in the final inventory must serve at least one outcome through one
   job. Pages that serve none are cut, however conventional.
2. **List audience problems, then the content that answers each.** One row per problem. The
   answering content becomes page candidates. Use the visitors' vocabulary for the row labels;
   those labels later seed navigation labels (`ia-patterns.md` section 5).
3. **Write the message list flat.** Before any structure, list every message the site must carry.
   Then mark each message as: its own page, a section of a page, or a repeated site-wide fact.
4. **Rank the key facts.** Have one insider and three real prospects rank them independently.
   The top three become persistent elements (header, footer or a fact strip on every relevant
   page), not content buried on one page.
5. **Assign page types** from section 3. One topic per page. Split a page when it carries two
   decisions; merge pages when a visitor would need both to make one decision.
6. **Apply the ownership filter.** A blog, news area, events list or careers board is included
   only if a named person will update it on a stated rhythm. A stale dated-content area signals
   neglect more loudly than its absence.
7. **Phase the inventory.** Mark each page launch, phase 2 or cut. A deliberate small launch beats
   a large site with thin pages.
8. **Hand the inventory to IA.** Group it with `ia-patterns.md`, choose navigation with
   `nav-pattern-catalog.md`, then test with a tree test before any visual design.
9. **Test three times:** the draft inventory with prospects (can they say where they would look?),
   the mock-up (first-click test), the first working build (task test on a real phone).

## 3. Page-type contracts

Each contract lists what the page must hold, its layout rule, and the generic output it replaces.

| Page type | Must contain | Layout rule | Generic output to reject |
|---|---|---|---|
| Home | Who you are, what you do, for whom and where, in one line; the two or three primary routes; one or two actions; one slot built to change (current offer, next event) | Directs traffic; it is not an About page. Message survives with images off. Holds a "one in, one out" rule so it does not accrete | Hero slogan with no noun, three icon cards, auto-rotating carousel, every section of the site summarised |
| Service or product detail | One service per page: who it is for, the outcome, what is included, price or price basis, how to start, proof specific to this service | Decision content above proof; one primary action repeated at the end | A shared "Services" page with six paragraphs and one form |
| Service hub (overview) | Two or three sentences per item, each linking to its detail page | Scannable list or equal tiles; no detail content duplicated | A hub that becomes a second, weaker detail page |
| About | Why the organisation exists, told as a short story; the people a customer will meet, with real photographs; credentials that matter to the buyer; a next step | Reason first, history last; split into team, approach and history pages only when each has substance | CV-style timeline, stock handshake photograph, no next step |
| Contact | Every contact route in one place (phone, WhatsApp, email form, address, hours, map, directions from a known landmark, photograph of the entrance); a short form; a visible confirmation after sending; separate quote form if quotes differ from questions | Phone and messaging links first on mobile; form fields limited to what is needed to reply | Form only, no phone; map embed with no written directions; silent submission |
| FAQ | Only questions genuinely asked often; one- or two-paragraph answers linking deeper; grouping by topic above about 20 items; a route to ask a new question | Disclosure pattern with visible headings, or a topic index; findable by search | A dumping ground that replaces real pages; answers hidden in un-labelled accordions |
| Article, news or insight | Title with the point first, date and author, a lead that states the finding, subheads, related content and a next step | Reading measure 60-75 characters; see `editorial-and-long-form-layout` | Wall of text, or a card grid of undated posts |
| Proof (case study, testimonial page) | Named client, role and organisation (with permission), the problem, what was done, a measured result, a photograph of real people or work | One case per page with a summary strip; proof rules in `trust-credibility-and-social-proof` | Anonymous quotes, invented metrics, logo walls without consent |
| Press or media kit | Current logo files, approved photographs, short and long descriptions, fact sheet, press contact | Download list with file type and size shown | "Contact us for assets" |
| Search results | The query echoed, result count, type filters, a useful zero-results state with suggestions | Results scannable by title and snippet; see `ia-patterns.md` section 8 | "No results found" as a dead end |
| Error (404) | A short apology in brand voice, a note that the address may be mistyped, search, the main routes, a way to report the broken link | Full site header and footer stay present | A joke illustration with no way forward |
| Legal and policy (privacy, terms, cookies) | Plain-language summary first, then the full text; last-updated date; contact for data requests | Long-form measure, anchored table of contents | Tiny grey text reachable only from a cookie banner |
| Coming soon or pre-launch | What is coming, when, and a way to be told (email, WhatsApp channel, social) | Single screen, one action | A logo and a countdown with no capture |
| Checkout or multi-step form step | Step count and current position, a summary of what is being bought, the total including fees, a way back without losing data | See `ecommerce-and-checkout-ux` and `form-ux-design` | Surprise fees on the last step |

**Splash or gateway pages** are excluded by default. Allow one only for a true choice the
visitor must make first (language or country), and prefer a remembered selector on the home page.

## 4. Site-wide layout rules

- **Conventional frame, distinctive content.** Logo top-left (top-right in RTL), primary
  navigation in a stable place, search where the audience expects it. Spend novelty on content,
  imagery and type, not on the frame (`art-direction-routes` unusual-layout test).
- **Compact header.** The page title and the first lines of content should be visible on the first
  mobile screen. A tall hero on inner pages is a common cause of the page's point being pushed off
  screen.
- **Function in the footer.** Key facts, contact routes, secondary navigation and legal links. A
  footer of legal links only wastes the one place every scroller reaches.
- **Link placement signals priority.** From strongest to weakest: primary navigation, persistent
  element on every page, home page, high on the page, in-body text. Place a page's links to match
  its importance to the outcomes list.
- **Descriptive link text.** Destination named, key word first, file type and size stated for
  downloads; never "click here".

## 5. Decision rules

| Condition | Choose | Failure caused by the wrong choice |
|---|---|---|
| Fewer than about 20 pages, one audience | Flat structure, everything reachable from primary navigation | Invented hierarchy hides pages behind needless hubs |
| Several distinct audiences with different jobs | Audience routes on the home page, shared page types underneath | Separate audience sites duplicate content and drift apart |
| A service has distinct buyers or prices | One detail page per service | A shared page answers nobody's question fully |
| Content has no owner or rhythm | Omit the dated-content area | A stale news page tells visitors the business may be closed |
| Visitors mostly arrive on a phone over mobile data | Phone, WhatsApp and directions first on Contact; light pages | Desktop-first contact pages bury the action the visitor came for |

## 6. Quality gate

- Every page maps to an outcome and a job; cut pages are recorded with the reason.
- The top three key facts appear in a persistent element.
- Each page type meets its contract row; the rejected generic output is absent.
- The 404, search zero-results and form confirmation states are designed, not defaulted.
- Tree test and first-click test results are recorded, or marked `NOT_ASSESSED`.

## 7. Original worked example

A Mbarara dental practice asks for "a modern website". Outcomes: booked appointments (measured by
calls and WhatsApp chats from the site) and fewer phone calls about prices. Jobs: booking desk and
price list. Staff rank the key facts: hours including Saturday, price range for a check-up and
cleaning, accepted insurers and mobile money. Inventory at launch: Home, four service detail
pages (check-up, cleaning, fillings, children's dentistry), Prices, About (the two dentists, real
photographs in the surgery), Contact (tap-to-call, WhatsApp, directions from the taxi park, a
photograph of the entrance), 404. Cut: a blog, because nobody owns it. The three key facts sit in
a fact strip under the header on every service page and in the footer.

## Evidence and currentness

Durable planning concepts only; no platform thresholds are asserted here. Page-count and
menu-length figures are working heuristics, not research findings. Access date 2026-09-24.

Sources: Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask Before Building a
Website*, Wiley; McNeil, P. (2013) *The Web Designer's Idea Book, Volume 3*, HOW Books; this
engine's `ia-patterns.md` and `nav-pattern-catalog.md`.
