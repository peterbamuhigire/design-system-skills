---
name: visual-product-slop-audit
description: Use when auditing imagery, generated visuals, brand/marketing assets, UI screens, or AI-powered product features for AI slop — beyond typography. Detects the visual tells (waxy skin, melted backgrounds, gibberish text, extra fingers, warped logos, uncanny faces) and product/interface tells (AI-hammer feature cramming, ungrounded chatbots, decorative "AI" gradients). Produces findings + a remake/remediation. Pairs with ai-slop-typography-audit (type) and the digital-research engine's anti-ai-slop (writing).
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
    - claude-code
    - codex
---

# Visual & Product Slop Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Reviewing AI-generated or AI-assisted imagery, key art, thumbnails, or brand/marketing assets.
- Auditing a UI screen or a product feature that embeds generative AI.
- Gate-checking any visual deliverable before it ships under the Chwezi name.

## Do Not Use When

- The concern is the typeface/type system — use `ai-slop-typography-audit`.
- The concern is written copy (preambles, buzzword salad, vague attribution) — that is a writing
  concern owned by the `digital-research-engine` (`anti-ai-slop`); route there.

## Required Inputs

- The asset(s) or screens (images, mockups, the live UI, or a description of the feature).
- The context and audience, and whether it is public-facing (raises the bar — corporate slop is
  the highest-backlash failure, per `doctrine/references/ai-slop-taxonomy.md`).

## Workflow

1. **Run the visual tells checklist** (`ai-slop-taxonomy.md` → Visual & video tells): waxy skin,
   melted backgrounds, gibberish text, floating objects, extra fingers/impossible anatomy,
   warped/misspelled logos, uncanny faces, mismatched lighting.
2. **Run the product/interface tells checklist**: AI feature where nav/search was faster;
   ungrounded chatbot that can invent commitments; generative output with no verifiability/undo;
   decorative "AI" badges/gradients with no user benefit.
3. **Classify each finding** — *critical* (public-facing visual anomaly, warped logo, halluc\
   inating bot) vs *major/minor*.
4. **Decide remake vs remediate.** Anomalous AI imagery is **remade or replaced** (art-directed,
   or real photography/illustration), not patched. Product slop is **removed or grounded**.
5. **State the human-craft alternative** — what a skilled designer would ship instead (per the
   Mission: distinct, authored, not templated).
6. **Report** findings → fixes with before/after.

## Anti-Patterns

- "Touching up" a six-fingered hero image instead of remaking it.
- Keeping an AI feature because it's impressive when a search bar served users better.
- Treating an AI gradient/badge as design.

## Outputs

- A findings list (tagged critical/major/minor with the tell it breaks) and a stated,
  human-craft remediation ready to apply.

## References

- `doctrine/references/ai-slop-taxonomy.md`, `doctrine/design-doctrine.md` (Mission).
- Sibling audits: `ai-slop-typography-audit` (type); digital-research `anti-ai-slop` (writing).
<!-- dual-compat-end -->
