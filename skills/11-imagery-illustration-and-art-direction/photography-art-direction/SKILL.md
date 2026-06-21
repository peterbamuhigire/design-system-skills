---
name: photography-art-direction
description: Use when choosing, treating, cropping, or sourcing PHOTOGRAPHY for a brand, website, deck, document, or app — and when directing an AI image generator to produce brand imagery. Routes here for art-direction briefs, photo style/mood boards, image treatment systems (grade/grain/duotone), crop and focal-point rules, anti-stock-photo direction (killing the smiling-handshake/headset-agent/diverse-team-laughing-at-salad look), licensing/sourcing decisions, and the prompt+constraint handoff that keeps generated images off the AI-slop tells. This is the single biggest "looks human-made" lever in the engine.
status: active
metadata:
  portable: true
  category: 11-imagery-illustration-and-art-direction
  compatible_with:
    - claude-code
    - codex
---

# Photography & Art Direction

<!-- dual-compat-start -->

Imagery is the fastest read on a page. A viewer judges "is this real, made by people who
care?" from a hero photo before reading a word. Generic stock and default AI output are the
loudest slop signals there are — louder than a font, because a bad image is *content*, not
chrome. This skill makes imagery a **deliberate, stated, authored choice**, exactly as the
doctrine Mission demands ("the moat is looking human-made", `doctrine/design-doctrine.md` §0).

## Use When
- Selecting or commissioning photography for a brand, site, hero, deck, report cover, or app.
- Defining a **photo treatment system** — colour grade, grain, contrast, duotone, crop ratios,
  focal-point rules — so every image looks like it came from one art director.
- Killing **stock-photo cliché**: smiling handshakes, headset call-centre agents, "diverse team
  laughing at salad," lens-flare cityscapes, isolated-on-white product shots with no story.
- Writing an **art-direction brief / mood board** before a shoot, a stock pull, or a buy.
- **Directing an AI image generator** for brand imagery — the prompt, the negative constraints,
  and the accept/reject gate that keeps the output off the slop tells.
- Auditing existing imagery and deciding *remake / re-grade / re-crop / replace*.

## Do Not Use When
- The asset is a **vector illustration, spot graphic, or hero illustration** → use the
  illustration skill in this group (sibling). 
- The asset is an **icon / icon set** → `iconography-system-design` (this group).
- It is **data visualisation or a chart** → group 12 (`data-visualization`,
  `dashboard-and-data-product-design`).
- You are running the generic **visual slop audit** across a whole product (UI + features) →
  the cross-cutting `visual-product-slop-audit` (group 00/04). This skill owns *imagery
  direction*; that one owns the product-wide reject gate.

## Required Inputs
- The **brand**: voice/positioning, audience, the one feeling the imagery must carry.
- Where the image lives: hero / inline / background / report cover / OG card / avatar — and its
  rendered size and aspect ratios.
- **Budget & sourcing path**: original shoot, commissioned, premium/editorial stock, free stock,
  or AI-generated (and whether AI output is acceptable for this surface at all).
- Technical envelope: max file weight, format (AVIF/WebP), dark/light backgrounds, text-overlay
  zones. (For LCP weight budgets see `doctrine/references/web-performance-budgets-2026.md`.)

## Workflow
1. **State the photographic intent first** (the anti-slop non-negotiable #1,
   `doctrine/design-doctrine.md` §2). One sentence: subject world + light + distance + mood.
   e.g. *"Real clinicians mid-task, available daylight, close and slightly off-centre, calm not
   triumphant."* If you cannot say it, you are not ready to pick an image.
2. **Choose the sourcing tier** against budget and surface, in this order of preference: original
   shoot → commissioned/editorial → premium stock used *non-obviously* (crop/grade it so it
   stops looking like stock) → AI-generated *only where permitted* → free stock (last resort,
   high cliché risk). See `references/anti-stock-direction.md` §Sourcing ladder.
3. **Define the treatment system** — the look that unifies every image: colour grade, black
   point/contrast curve, grain, optional duotone/monotone, and the crop/focal-point/aspect rules.
   Specify it concretely (values, ratios), per `references/photo-treatment-system.md`. This is
   what makes a stock or AI image read as *yours*.
4. **Direct the crop & focal point** — most "stock look" dies in the crop. Push the subject off
   the thirds, crop into the action, leave intentional negative space for text. Define safe text
   zones and the art-directed ratios (`references/photo-treatment-system.md` §Cropping).
5. **If sourcing AI:** write the prompt + the **negative-constraint list** + the **accept/reject
   gate** keyed to the slop tells (`doctrine/references/ai-slop-taxonomy.md` §Visual tells) —
   waxy skin, melted backgrounds, gibberish signage, extra fingers, warped logos, mismatched
   lighting. AI imagery is admissible only when it can pass that gate AND a human re-grades/crops
   it into the treatment system. Per doctrine §2 sourcing-authority rule, an AI tool's *own*
   aesthetic defaults are never the authority for the look — they are what we art-direct *away*
   from. See `references/anti-stock-direction.md` §AI-image direction.
6. **Run the reject gate** on every candidate (stock or AI): cliché test, slop-tell test,
   treatment-fit test, performance-weight test. Anything that fails is re-graded, re-cropped, or
   replaced — never shipped "because it's close."
7. **Accessibility & weight:** every content image needs meaningful `alt` text (decorative →
   empty alt), sufficient contrast for any overlaid text (`doctrine/references/wcag-2.2-criteria.md`),
   and a weight inside the LCP budget (`doctrine/references/web-performance-budgets-2026.md`).

## Anti-Patterns
- **The slop cliché set:** smiling handshake, headset agent, team-laughing-at-salad,
  isolated-on-white with no story, generic-gradient-city, fake-candid-with-perfect-teeth.
- **Stock used raw** — straight off the library, uncropped, ungraded, recognisable. The image is
  fine; shipping it *unauthored* is the failure.
- **No treatment system** — ten images from ten sources, ten different grades, reads as a
  scrapbook, not a brand.
- **AI image shipped un-vetted** — waxy skin / 6 fingers / melted background / warped logo (the
  `ai-slop-taxonomy.md` tells). This is the highest public-backlash risk (taxonomy §2,
  "shovelware assets").
- **Centre-punched crop with the subject staring down the lens** — the default everything-looks-
  the-same composition.
- **Decorative AI sparkle/gradient as "imagery"** with no subject and no benefit — slop by §
  product-tells.

## Outputs
- A one-page **art-direction brief / board**: intent sentence, sourcing tier, treatment spec
  (grade/grain/crop/ratios), reference frames, do/don't, and (if AI) the prompt + negative list
  + accept/reject gate.
- A reusable **treatment recipe** (concrete values) that any later image can be run through.
- A **reject log** for audited candidates.

## Examples
- `examples/art-direction-board.md` — a complete, real art-direction brief for a sample brand
  (a community health-tech product, "BrightSoma Clinics"): intent, sourcing ladder decision,
  full treatment recipe, crop rules, and an AI-image direction block with negative constraints
  and the accept/reject gate. Reusable as a template — not lorem.

## References
- `references/photo-treatment-system.md` — the concrete treatment + cropping/focal-point system
  (grade, grain, duotone, ratios, safe text zones, weight).
- `references/anti-stock-direction.md` — the cliché kill-list, the sourcing ladder, how to make
  stock un-stock, and the AI-image direction handoff (prompt + negatives + gate).
- `doctrine/design-doctrine.md` — Mission §0 ("looks human-made") and Anti-Slop Charter §2
  (state-the-choice; sourcing-authority asymmetry rule).
- `doctrine/references/ai-slop-taxonomy.md` — the visual tells (the reject-gate checklist) and
  the "shovelware assets" public-backlash risk.
- `doctrine/references/wcag-2.2-criteria.md` — alt text & text-over-image contrast.
- `doctrine/references/web-performance-budgets-2026.md` — image weight inside the LCP budget.
<!-- dual-compat-end -->
