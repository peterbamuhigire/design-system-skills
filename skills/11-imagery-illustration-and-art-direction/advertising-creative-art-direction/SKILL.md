---
name: advertising-creative-art-direction
description: Use when art-directing advertising or campaign creative - copy and image relationships, poster and cover tests, triplet or cousin campaign systems, big-idea tests across channels, a 7-point effectiveness screen, critique and ad layout specs handed back to the marketing engine. Use art-direction-routes for brand or website directions.
metadata:
  portable: true
  category: 11-imagery-illustration-and-art-direction
  compatible_with:
  - claude-code
  - codex
---

# Advertising Creative Art Direction
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

This skill owns the visual execution of advertising: how a headline and an image work together,
how a campaign stays recognisable across units and channels, and how concepts are screened and
critiqued before anyone produces final artwork. Strategy, audience, offer, copy and media belong
to the marketing engine; this skill receives a brief and returns concepts, layouts and
production specifications.

<!-- dual-compat-start -->
## Use When

- A campaign brief has arrived from the marketing engine and needs visual concepts, key visuals,
  layouts or a campaign art-direction system.
- Designing paid social, display, print, outdoor, point-of-sale, transit or taxi branding,
  radio-plus-visual or influencer-supplied creative that must look like one campaign.
- Headline and image repeat each other, fight each other or fail without the body copy.
- A team must decide between a strict campaign template (triplets) and a family resemblance
  (cousins), or adapt one idea across channels.
- Concepts need screening before a client sees them, or a client's creative feedback needs to be
  turned into actionable direction.

## Do Not Use When

- The work is campaign strategy, audience, offer, media plan, budget or copywriting - that stays
  in the social-media and digital marketing engine (`social-media-skills`: campaign strategy,
  campaign brief, paid social playbook, copy skills).
- The work is choosing a brand or website direction - use `art-direction-routes`.
- The work is a photographic shoot brief, illustration system or AI image generation for an
  agreed concept - use `photography-art-direction`, `illustration-style-and-systems` or
  `ai-image-generation-art-direction`.
- The work is a landing page the ad points to - use `landing-page-and-conversion-design`.
- The work is final release approval of a campaign asset - the marketing engine's creative review
  gate owns release; this skill supplies the design evidence for it.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Creative brief: objective, audience and mindset, current perceptions, single message, proof, offer, mandatory items, timeline | Marketing engine campaign brief | yes | Concepts are judged against the brief, not taste |
| Big idea or campaign platform line, if already agreed | Marketing engine campaign strategy | conditional | Visual system must ladder to one idea |
| Channel and placement list with current specifications | Media plan plus each platform's or publisher's current specification | yes | Sizes and safe zones change; never assume |
| Brand assets: logo, colour, type, imagery style, sound | Brand guide | yes | Distinctive assets are the red thread |
| Approved copy or headline options | Copy owner | yes | Copy-image relationship is designed with real words |
| Claims evidence and legal constraints (regulator, platform policy, disclosure) | Client and marketing engine legal gate | yes | Visuals must not imply claims the evidence cannot support |
| Languages and literacy profile of the audience | Brief | conditional | Decides copy-led versus image-led construction |

## Workflow

1. **Read the brief as a contract.** Restate the objective, audience, single message and proof in
   one line each. Stop and return the brief if the message is not single-minded or the audience
   is "everyone".
2. **Choose the construction** for the core execution: copy-led, image-led or fused (see
   `references/copy-image-constructions.md`). Apply the straight/crooked balance.
3. **Generate at least three substantially different concepts,** not variations of one. Allow
   incubation time between first and second rounds in the plan.
4. **Run the poster and cover tests** on every concept: the headline and visual must carry the
   idea without body copy; covering either one must not leave the other carrying everything or
   nothing; no redundancy between words and picture.
5. **Screen concepts internally** with the 7-point effectiveness scale and the responsible-creative
   visual checks (`references/creative-effectiveness-and-critique.md`). Kill anything scoring 1;
   send 5 back for a sharper hook; advance only 6 and 7.
6. **Test the idea across channels** with the big-idea test pack: three-channel sketches, the
   press-release test and the forward test (`references/campaign-systems-and-channel-adaptation.md`).
7. **Choose the campaign system:** triplets for high-frequency, short-exposure placements;
   cousins for long-running content. Lock the distinctive assets either way.
8. **Build layouts and specifications** per placement from the current platform or publisher
   specification: size, safe zones, text-free zones, file format, weight, captions and alt-text
   brief. Apply the ad layout rules and the thumbnail test.
9. **Present and run the critique protocol.** Frame the assignment first, then show concepts,
   then agree next steps. Translate feedback from "what I dislike" to "which brief goal is not
   yet met". Do not decide in the room when the client needs time.
10. **Hand back** the design deliverables in the contract format
    (`references/handoff-contract-marketing-engine.md`) for the marketing engine's release gate.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Audience spans several languages or lower literacy | Image-led or fused construction; minimal words; test comprehension | Copy-led ad is missed or misread by much of the audience |
| Audience is professional and reading on LinkedIn or in print | Copy-led construction is available; headline must beat the picture | Weak image distracts from a strong argument |
| Image is odd, funny or shocking | Keep the headline straight | Two clever elements compete and neither lands |
| Image and headline are both plain | Make one of them unexpected | The ad is ignored |
| High-frequency, short-exposure placements (outdoor, prospecting social, transit, point of sale) | Triplet system: one master template, only image and headline change | Recognition does not build across impressions |
| Long-running organic content or brand campaign | Cousin system: shared assets, varied composition | Audience fatigue after repeated identical units |
| Platform specification not verified for this placement | Build to the current published specification and date it; if unavailable, mark `NOT_ASSESSED` and block release | Text cropped by interface overlays or rejected files |
| Concept scores 1 on the effectiveness scale | Kill regardless of craft | Harmful or brand-damaging work reaches the client |
| Visual implies a result, price or endorsement the evidence does not support | Change the visual or obtain evidence | Misleading advertising and regulatory exposure |

## Capability Contract

- Read access to the brief, brand assets, copy and specifications is required. Layout and
  rendering tools are required to claim any layout is production-ready.
- Presenting concepts, recording client decisions and releasing assets need the account owner's
  authority. Buying media, imagery or talent is out of scope.
- Network access is used only to read current platform or publisher specifications; record the
  source and date.

## Degraded Mode

- Without a single-minded brief, deliver brief questions only and block concept work.
- Without verified placement specifications, deliver master layouts with specifications marked
  `NOT_ASSESSED` and block release until they are checked.
- Without rendering, deliver concept descriptions and layout specifications, labelled unverified.
- Without claims evidence, remove claim-bearing visuals or mark them conditional.

## Anti-Patterns

- Showing a horse and writing "horse" - correct by letting words and picture each add meaning.
- Three colourways of one layout presented as three concepts - correct with substantially
  different ideas.
- Resizing one desktop banner into every placement - correct with channel-native executions of
  one idea and per-placement safe zones.
- Borrowed-interest visuals that need a strained headline to connect - correct with product,
  user or proof as the hero.
- Feedback such as "make the logo bigger" passed straight to the designer - correct by stating
  the brief problem (for example weak brand linkage in the first seconds) and letting the
  designer solve it.
- Relying on remembered platform sizes - correct by checking the platform's current specification
  and dating it.
- Stereotyped or "poverty" imagery in development or NGO advertising - correct with the swap test,
  dignity rules and people shown as agents, not recipients.
- Testing to decide the concept - correct by testing to validate or de-risk; research favours the
  familiar.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Concept boards (three or more distinct concepts) | Marketing lead, client | Each passes the poster and cover tests and carries an effectiveness score with a one-line reason |
| Campaign art-direction system (triplet or cousin rules, locked assets) | Designers, producers, influencers | Master template or family rules documented with do and do-not examples |
| Placement layouts and production specifications | Producers, media buyer, marketing engine | Each placement lists size, safe zones, format, weight, captions and alt-text brief, with the specification source and date |
| Critique and decision record | Account lead | Feedback translated to brief goals; decision, rejected concepts and reasons recorded |
| Design evidence packet for release | Marketing engine creative review gate | Rendered assets in context, accessibility evidence, rights and claim notes |

## Examples

- `examples/campaign-art-direction-worked.md` - a mobile-money savings campaign for a fictional
  Ugandan fintech: brief restatement, three concepts with scores, the chosen triplet system,
  placement specifications and the hand-back packet.

## References

- `references/copy-image-constructions.md` - constructions, straight/crooked rule, poster and
  cover tests, ad layout rules, captions and thumbnail tests.
- `references/campaign-systems-and-channel-adaptation.md` - triplets and cousins, distinctive
  assets, the big-idea test pack, channel tailoring and the placement specification check.
- `references/creative-effectiveness-and-critique.md` - the 7-point scale, concept screen,
  responsible-creative visual checks, critique protocol and feedback translations.
- `references/handoff-contract-marketing-engine.md` - what the marketing engine sends, what this
  engine returns, and who owns each decision.
- Siblings: `art-direction-routes`, `photography-art-direction`, `illustration-style-and-systems`,
  `ai-image-generation-art-direction`, `landing-page-and-conversion-design`,
  `print-production-and-finishing`, `accessible-color-and-contrast`.
- Sources (human authority): Landa, R. (2022) *Strategic Creativity: A Business Field Guide to
  Advertising, Branding, and Design*, Routledge; Serling, B. (ed.) (2002) *How to Write Million
  Dollar Ads, Sales Letters and Web Marketing Pieces*, The Internet Marketing Center
  (practitioners' essays on headline, visual and layout); Kelley, L. D. and Sheehan, K. B.
  (c. 2021) *Advertising Management in a Digital Environment: Text and Cases*, Routledge
  (creative brief and creative assessment); Adams, S. et al. (2012, revised edition) *Graphic
  Design Rules*, Frances Lincoln.
<!-- dual-compat-end -->
