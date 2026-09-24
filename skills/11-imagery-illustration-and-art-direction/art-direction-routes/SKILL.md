---
name: art-direction-routes
description: Use when proposing visual directions for a brand, website, campaign or product - named art-direction routes, three direction boards (safe fit, stretch, bold) built from real content with cost and maintenance tiers, a timeless or dated style check and a mood-board policy. Use brand-visual-identity to build the chosen route.
metadata:
  portable: true
  category: 11-imagery-illustration-and-art-direction
  compatible_with:
  - claude-code
  - codex
---

# Art-Direction Routes
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

This skill owns the options stage of visual work: turning a brief into a small number of named,
defensible directions that a client can choose between on evidence rather than taste. It gives the
agency a shared route vocabulary, a direction-board protocol and a currency check that keeps dated
surface treatments out of new work.

<!-- dual-compat-start -->
## Use When

- A client needs to see and choose a visual direction before identity, website or campaign
  production begins.
- A premium discovery tier promises "three directions" and the team needs a repeatable method and
  a board format.
- A brief says "modern", "clean" or "like [competitor]" and the team must translate that into
  named routes with reasons.
- A reviewer asks whether a proposed treatment (textures, ribbons, carousels, parallax, device
  mock-ups) is timeless, still relevant or dated.
- The team must decide whether to use a mood board and what it may contain.

## Do Not Use When

- A direction is already chosen and the task is building the identity system - use
  `brand-visual-identity`, then `brand-style-guide`.
- The task is one visual signature for a single UI or artefact - use `distinctive-by-design`.
- The task is advertising or campaign creative (copy-image concepts, campaign systems, ad
  effectiveness) - use `advertising-creative-art-direction`.
- The task is a photographic brief, illustration system or icon family for an agreed route - use
  `photography-art-direction`, `illustration-style-and-systems` or `iconography-system-design`.
- The task is choosing typefaces - describe type character here and choose faces in
  `font-selection-and-pairing`.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Brief: audience, primary job, offer, stakes, success measure | Client and strategist | yes | Routes are filtered by fit, not taste |
| Stigma or expectation to overcome (what buyers wrongly assume) | Discovery interviews | yes | Drives the belief each route must create |
| Real content: headline, one real photograph or product, key facts | Client | yes | Boards are built from reality, never placeholder copy |
| Competitor and category visual audit | Strategist or designer | yes | Differentiation must be proven |
| Budget, build and maintenance capacity (who edits the site or assets later) | Client and producer | yes | Sets cost and maintenance tiers |
| Channel and device reality (for example mid-range Android on mobile data) | Brief and analytics | yes | Routes that fail the main device are excluded |
| Existing brand equity and mandatory standards | Brand owner | conditional | Never break the client's corporate standards |

## Workflow

1. **Pre-filter.** Record audience, job, offer, brand equity, content reality, trust level,
   environment, differentiation need and the stigma to overcome. Draw the mobile job map (what
   phone visitors come to do). Exclude any route that fails a hard gate: accessibility, main
   device, maintenance capacity, brand standards.
2. **Pick three routes** from `references/route-catalogue.md`:
   - **Safe fit** - the most correct route for the audience and category;
   - **Stretch** - a more distinctive route that still fits;
   - **Bold** - the most memorable route, or the safe-fit route at high theme intensity.
   Never present a route you would not stand behind; clients choose the one you disliked.
3. **Set the two dials** for each route: style (how much, how ordered) and theme or material
   (which imagery world), plus theme intensity (subtle, styled, immersive). Lower intensity as
   task urgency rises.
4. **Build one direction board per route** with `references/direction-board-protocol.md`: style
   thesis sentence, type character (faces chosen by `font-selection-and-pairing`), palette logic,
   imagery rule, hero mock with the client's real headline and photograph, one component, a
   mobile view, build and maintenance tiers, risks and the borrow map.
5. **Run the currency check** on every board with `references/style-currency-vocabulary.md`.
   Any dated treatment needs a written brand reason or is removed.
6. **Run the unusual-layout test** for any route that departs from familiar structure: familiar
   anchors kept, purpose served, first-time visitor can find the way, small-screen fallback,
   never experimental in checkout or forms.
7. **Present in plain language.** Lead with the belief each route creates in the buyer, then the
   cost to build and keep, then the look. Agree the decision criteria before showing boards.
8. **Decide against criteria.** Record the chosen route, the rejected routes and the reasons in
   the decision register. Park borrowed ideas from unchosen routes or record them as rejected.
9. **Hand off** the chosen route to `brand-visual-identity`, `photography-art-direction`,
   `illustration-style-and-systems` and the token skills.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Task-critical site (health, government, finance, checkout) | Low theme intensity; familiar structure; distinctiveness through type, colour and imagery quality | Immersive treatment blocks the task and erodes trust |
| Client cannot edit hand-made or art-directed elements without a designer | Prefer code-rendered type and colour; price the maintenance tier explicitly | Site freezes after launch because every change needs the studio |
| Route relies on photography but no budget exists for an original or local shoot | Drop the route or change its imagery rule | Imported stock breaks the promise and looks borrowed |
| Two routes differ only in colour | Replace one with a substantially different route | Client picks a colour, not a direction; time is wasted |
| Client asks for "like [competitor]" | Name the quality they respond to (warmth, confidence, calm) and express it in a different route | Imitation invites legal risk and erases difference |
| Mood board requested before any concept | Use it only to agree the brand's taste level internally or with the client; never bill it as the concept | Mood board replaces thinking and anchors everyone on other people's work |
| A treatment is classed as dated | Remove it unless the brand has a stated, specific reason | Work looks a decade old on launch day |

## Capability Contract

- Read access to the brief, content, audit and brand standards is required. Rendering or mock-up
  tools are required to produce boards; without them, boards are written specifications only.
- Presenting to the client, recording decisions and committing budget need the account owner's
  authority. This skill does not purchase imagery or fonts.

## Degraded Mode

- Without real content, stop board production and request it; deliver route descriptions only,
  marked provisional.
- Without rendering, deliver written direction specifications and label the visual fit
  `NOT_ASSESSED`.
- Without a competitor audit, mark differentiation unverified and do not present a route as
  "unique".

## Anti-Patterns

- Three variations of one idea presented as three directions - correct with three substantially
  different routes.
- Boards filled with placeholder text and stock photographs - correct with the client's real
  headline and real imagery.
- Leading the presentation with aesthetics ("clean, modern, sleek") - correct by leading with the
  belief created in the buyer and the cost to keep.
- Reviving dated treatments by default (stitched fabric, wood-grain panels, ribbons, glossy glows,
  auto-rotating carousels) - correct with the currency check and a written reason.
- Copying one admired site - correct with an element-level borrow map drawn from several sources
  and a replica check.
- Immersive themes on task-critical pages - correct by lowering intensity or confining the theme
  to story pages.
- Mood boards used as a billable deliverable in place of concepts - correct with the mood-board
  policy.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Three direction boards | Client decision-maker | Each board has thesis, real-content mock, mobile view, cost and maintenance tiers, risks and borrow map |
| Route decision record | Account lead, designers | Chosen and rejected routes with reasons and criteria used |
| Currency check log | Design lead | Every dated treatment removed or justified in writing |
| Hand-off brief for the chosen route | Identity, imagery and token skills | Style thesis, dials, type character and imagery rule stated |

## Examples

- `examples/three-direction-boards-worked.md` - three boards for a fictional Kampala private
  clinic group: safe fit, stretch and bold routes with theses, dials, cost tiers, currency checks
  and the recorded decision.

## References

- `references/route-catalogue.md` - fourteen named routes with promise, fit, signature moves,
  risks, cost tiers and currency class.
- `references/direction-board-protocol.md` - the board format, the two dials and intensity,
  the unusual-layout test, the borrow map, the mood-board policy and presentation lines.
- `references/style-currency-vocabulary.md` - timeless, still-relevant and dated classes, the
  trend-adoption checklist, the dated-treatment list for design QA, and the era-dating table
  (web 2.0 gloss to the current AI-generated SaaS default) used to date references and write the
  brief's avoid line.
- `doctrine/design-doctrine.md` (purpose-fit premium, human authority);
  `doctrine/references/creative-selection-and-taste.md`; `doctrine/references/ai-slop-taxonomy.md`.
- Siblings: `distinctive-by-design`, `brand-visual-identity`, `photography-art-direction`,
  `illustration-style-and-systems`, `advertising-creative-art-direction`,
  `performance-as-ux-and-core-web-vitals` (weight budget per route).
- Sources (human design authority): McNeil, P. (2010) *The Web Designer's Idea Book, Volume 2*,
  HOW Books; McNeil, P. (2013) *The Web Designer's Idea Book, Volume 3*, HOW Books; Landa, R.
  (2022) *Strategic Creativity*, Routledge; Adams, S. et al. (2012, revised edition) *Graphic
  Design Rules*, Frances Lincoln.
<!-- dual-compat-end -->
