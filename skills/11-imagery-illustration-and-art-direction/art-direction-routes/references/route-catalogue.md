# Route Catalogue

Parent skill: [`../SKILL.md`](../SKILL.md) (`art-direction-routes`).

**When to read:** when picking the three routes for direction boards. Each route is a durable
direction, abstracted from recurring styles catalogued by McNeil (*The Web Designer's Idea Book*,
Volumes 2 and 3, HOW Books, 2010 and 2013) and re-classified for current practice. Borrow
principles, never compositions. Type character is described here; actual faces come from
`font-selection-and-pairing` and must pass the banned list.

Cost tiers: **build** (studio effort to make) / **maintain** (effort for the client to keep it
right after launch). Currency class: see `style-currency-vocabulary.md`.

| # | Route | Promise to the buyer | Best-fit clients (East African examples) | Signature moves (principles) | Risks | Build / maintain | Currency |
|---|---|---|---|---|---|---|---|
| R1 | Superclean Authority | "Clear; we have it handled" | Law chambers, consultancies, fintech, government services, hospitals | Generous space, strict alignment, restrained palette, hierarchy by type scale and weight, one accent for action | Sterile without one signature detail | Low / Low | Timeless |
| R2 | Honest Minimal | "The work speaks" | Architects, photographers, results-led agencies, premium lodges | Work shown large and first, almost no chrome, image layout follows the work's real proportions | Thin content exposed | Low / Low | Timeless |
| R3 | Type-Led Voice | "We have something to say" | Publishers, strategy firms, idea events, NGOs with a manifesto | Typography as the hero; weights of one family; editorial scale contrast; live text | Display type overused; licence cost | Low-Med / Low | Timeless |
| R4 | Illustrated World | "Human, memorable, ours alone" | Fintech for first-time users, edtech, children's brands, health promotion | Commissioned illustration system used as hero or woven into components | Commissioning cost; inconsistent illustrators; infantilising serious topics | Med-High / Med | Timeless |
| R5 | Hand-Made Accent | "Personal, not corporate" | Craft makers, cafés, community health, social enterprises | Hand-drawn notes and marks over a clean structure; editable text stays live | Looks amateur if half-done; hand-lettered headings the client cannot edit | Med / Med | Still-relevant (niche) |
| R6 | Tactile Craft and Material | "Warm, crafted, real" | Coffee exporters, furniture makers, breweries, lodges, artisanal food | Material shown through real close-up photography (grain, weave, clay, bark cloth) and a natural palette; subtle grain | Sliding into literal textured UI; heavy images | Med / Med | Principle still-relevant; literal texture UI dated |
| R7 | Heritage Editorial | "Established, principled, enduring" | Family firms, heritage hotels, cultural institutions, law chambers | Period-appropriate serif or slab character, line-art illustration, monochrome with one strong accent, symmetrical composition | Pastiche; fussiness; low contrast | Med / Med | Still-relevant (niche) |
| R8 | Immersive Photographic | "Be there" | Tourism, safari lodges, real estate, venues | Full-bleed original photography; simple foreground | Page weight on mobile data; stock kills it; text contrast over images | Med-High / Med | Still-relevant |
| R9 | Colour-Coded System | "Many programmes, easy to navigate" | Multi-programme NGOs, universities, conglomerates, marketplaces | Muted base with one semantic accent per section; consistent tokens | Clown palette if unsystematic; colour-only meaning | Low / Low | Timeless |
| R10 | Themed Narrative | "A memorable story with a double meaning" | Launches, campaigns, events, agencies showing craft | One theme tied to the brand name or mission at a chosen intensity | Gimmick; usability loss at high intensity | Med-High / Med-High | Still-relevant when subtle |
| R11 | Character or Mascot | "Friendly; lowers anxiety" | IT services, consumer apps, youth brands, events | A brand character used strategically (symbol, stressful step, event host) | Childish for B2B or government; hard to extend | Med / Med | Still-relevant |
| R12 | Product Stage | "Look at this" | Single products, apps, FMCG launches, books | Product as hero with real depth; one-page sales structure; one call to action repeated per section | Weak product photography; fake 3D | Med / Low | Timeless |
| R13 | Content Grid and Discovery | "Lots to explore, easy to browse" | Media, galleries, marketplaces, large portfolios | Equal tiles, filters, reflow, strong block titles, list-view fallback | Undifferentiated card soup; heavy galleries | Med / Low | Timeless |
| R14 | Editorial Art-Directed | "Every story is crafted" | Flagship thought leadership, annual reports, campaign long reads | Stable frame (header, type system) with bespoke layout per long piece | Time cost; brand drift | High / High per piece | Still-relevant for flagship content only |

## Stigma-to-route prompts

Use the stigma or expectation the buyer holds to shortlist routes. Examples:

| Client | Assumption to overcome | Routes to consider |
|---|---|---|
| Microfinance or SACCO | "Financial institutions are cold and take advantage" | R4 with real-member photography, or R1 with warm imagery |
| Government agency | "Bureaucratic and opaque" | R1 with plain language and task-first structure |
| Local furniture maker | "Imported is better" | R6 close-up joinery photography; R2 |
| Private clinic | "Expensive and intimidating" | R1 calm layout with friendly human photography and visible prices |
| IT support firm | "Jargon and condescension" | R11 used lightly, or R1 with real staff photography in client offices |

## Route combinations

Routes combine as style plus theme, for example "R1 Superclean with an R6 material imagery rule"
or "R3 Type-Led with R9 colour coding". Keep one route dominant; a board that mixes three routes
equally has no thesis.

## East African route checks

- At least one route in every set must prove itself on a mid-range Android phone over mobile
  data (see `performance-as-ux-and-core-web-vitals`).
- Use locally shot photography in every option wherever the route depends on photographs.
- Show the WhatsApp and mobile-money moments in the mock where the client sells or books.
- For bilingual clients, show a second-language headline to test type and line-length
  resilience.
- Keep government, health and finance routes at low theme intensity.
