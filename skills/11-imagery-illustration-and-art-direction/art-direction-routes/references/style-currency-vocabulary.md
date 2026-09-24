# Style Currency Vocabulary

Parent skill: [`../SKILL.md`](../SKILL.md) (`art-direction-routes`).

**When to read:** when judging whether a style, element or structure belongs in new work, and when
running design QA on inherited sites. Classes are the engine's current judgement, built from
McNeil's catalogues of 2009-2012 web styles (*The Web Designer's Idea Book*, Volumes 2 and 3) and
re-checked against current practice. Re-assess at each Kaizen cycle; currency drifts.

## Classes

- **Timeless** - the principle and its common forms remain sound; use freely when it fits.
- **Still-relevant** - sound in a bounded or niche form; state the condition.
- **Dated** - the surface form reads as a specific past era. Keep the underlying principle if it
  is useful, express it in a current idiom, and revive the literal form only with a written
  brand reason (for example a real letterpress studio using letterpress texture).

## Classification table

| Style, element or structure | Class | Keep (principle) | Drop (surface) |
|---|---|---|---|
| Superclean / ultra-clean | Timeless | Clarity, polish, air | - |
| Minimal | Timeless | Work shown first; fast; maintainable | Pure white as a rule |
| Type-led | Timeless | Type as the main visual; live text | - |
| Illustrated | Timeless | Humanises and differentiates | Over-theming every element |
| Solid colour | Timeless | Crisp, code-rendered, fast | - |
| Muted base with semantic accents | Timeless | Colour-coded navigation of many sections | Unsystematic rainbow |
| Equal-tile grids | Timeless | Scannable, responsive | Card soup without hierarchy |
| Homepage elevator pitch | Timeless | Purpose in three to ten words | - |
| Helpful homepage, functional footer, useful 404 | Timeless | Routes to what visitors want; next step at the end of a page | Footer of legal links only |
| Hand-drawn / sketch accents | Still-relevant (niche) | Personal, organic | Hand-lettered headings the client cannot edit |
| Collage | Still-relevant (niche) | Layered storytelling | Used as a crutch |
| Full-bleed photographic backgrounds | Still-relevant | Immersion with a simple foreground | Photographs behind body text |
| One-page sites | Still-relevant | Poster-like overview for lean content | Cramming a large site into one page |
| Unusual layouts | Still-relevant (bounded) | Surprise with familiar anchors | Novelty that hurts use |
| Heritage / period type | Still-relevant (niche) | Period-appropriate character | Inset "letterpress" text shadows |
| Mascots and characters | Still-relevant | Lower anxiety at a stressful step | Childish tone for serious B2B or government |
| Parallax and scroll effects | Still-relevant (story pages only) | Depth on a brand story page, compositor-only, with a static reduced-motion version | Scroll-jacking, auto-scroll, JavaScript scroll-listener parallax |
| Device mock-ups | Still-relevant (product-in-context only) | Showing a real app screen in use | Decorative device photographs |
| Atypical navigation | Mostly dated / high risk | Only where it is the experience (exploratory portfolio) | Any commerce or service site |
| Horizontal whole-site scrolling | Dated | Photo strips that reveal the next item | Sideways scrolling of whole desktop sites |
| Auto-rotating hero carousels | Dated | User-driven, ordered story sequences only | Auto-rotation |
| Glossy glows, bevels, radial light bursts | Dated | Subtle depth to direct attention | Glossy "web 2.0" effects |
| Literal fabric stitching, wood-grain panels, zigzag edges, corner ribbons, "hands holding content" | Dated | Tactile warmth through real photography and material colour | Skeuomorphic surface decoration |
| Pure flat with no signifiers | Dated | Reduced ornament, colour carries meaning | Buttons that look like labels, links without a cue |
| Icon fonts from a third-party service | Dated | Consistent icon family | Font-based icons; use inline SVG or a sprite |

## Era dating for references and inherited sites

Use era labels to date a reference image or an inherited site, and to write the brief's "avoid"
line precisely. Eras are approximate peak periods, the engine's judgement from the catalogues
cited above and observed practice; they are not measured data.

| Era (approximate peak) | Recognisable surface vocabulary | What it signals today |
|---|---|---|
| Web 2.0 gloss, about 2005-2010 | Glossy buttons, reflections, radial light bursts, starburst badges | A site not redesigned for over a decade |
| Skeuomorphic and textured, about 2009-2013 | Stitching, wood, paper, leather, ribbons, zigzag edges, letterpress insets, faux-3D shelves | Template-marketplace theme; low care |
| Flat, about 2013-2016 | Solid fields, long shadows, circular icons, no depth cues | Affordance risk; see the pure-flat row |
| Material and card systems, about 2014-2019 | Consistent elevation, card grids, floating action buttons on the web | Acceptable when systematic; generic when copied wholesale |
| Neumorphism, about 2020-2021 | Soft extruded and inset surfaces in one low-contrast hue | Fails contrast and state visibility; reject for UI controls |
| Glassmorphism, about 2020-2023 | Frosted translucent cards over colourful blurs | Convergent slop tell (`doctrine/references/ai-slop-taxonomy.md`); translucency only for genuine platform chrome |
| Neo-brutalism, about 2021-2024 | Hard black outlines, offset solid shadows, clashing flat colour | Still-relevant (niche) for youth and indie brands; a costume elsewhere |
| Bento grids, about 2023-2025 | Rounded tiles of mixed sizes summarising features | Generic when every tile is a feature blurb; keep only when tiles hold real content of different weight |
| AI-generated SaaS default, about 2023-present | Dark hero, purple-to-blue gradient glow, centred slogan, three icon cards, glass panels, banned-list sans | The engine's primary slop signature; reject on sight |

**Anti-slop rule for trend vocabulary.** A trend name may appear in a brief only as a *reference
to avoid* or with a written brand reason and the principle kept (see the Keep column). A direction
described only by trend names ("bento, glass, gradient") has no thesis; send it back to the route
catalogue.

## Trend-adoption checklist

Before adopting any fashionable element, answer and record:
1. What does the element mean, and does that meaning connect with this brand's message?
2. Is it decoration only? If so, is decoration the right investment here?
3. Would the design fail without it? If not, is it adding focus or noise?
4. How many competitors already use it? Will it look dated within two or three years?
5. Can it be done subtly, in a supporting role?
6. What does it cost to build and to maintain?
7. Decision: adopt, adapt or reject, with the reason.

## Design QA use

Add the dated rows above to the design QA pass (`design-qa-and-pre-launch-review`) and to the
inherited-site audit: any dated surface without a written brand reason is a finding. Flat
directions must also pass the signifier and contrast checks in
`accessible-color-and-contrast` and `component-states-and-interaction-fidelity`.
