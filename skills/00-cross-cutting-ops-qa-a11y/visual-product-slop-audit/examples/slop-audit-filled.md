# Worked Example: A Filled Slop Audit (before → after)

A real before/after run of the `visual-product-slop-audit` workflow against a sample artifact, using
`../references/visual-tells-checklist.md` and `doctrine/references/ai-slop-taxonomy.md`. This is the
template a designer fills out per audit.

---

## 0. Artifact under audit

- **Asset:** Landing-page hero for **Maduuka** (Chwezi retail/POS product) — a generated hero image
  plus an embedded "Ask Maduuka AI" panel in the top nav.
- **Context / audience:** Public marketing site, prospective SME merchants in East Africa.
- **Public-facing?** Yes → the bar is highest (corporate/advertising slop, taxonomy category 2, is
  the top-backlash failure).

### Before (as received)

- Hero: an AI-generated photo of a smiling shopkeeper at a counter, warm golden-hour light, a
  blurred shop interior behind, a "MADUUKA" sign on the wall, a tablet on the counter showing a
  dashboard.
- Nav: an "Ask Maduuka AI ✨" pill (purple→blue gradient) opening a free-text chatbot that answers
  pricing, plan, and onboarding questions in prose, with no sources and no human-handoff.

---

## 1. Findings (checklist tells → severity)

| # | Tell (checklist ref) | Evidence in artifact | Severity |
|---|---|---|---|
| F1 | **A6 warped/misspelled logo** | Wall sign reads "MADWUKA"; the M and second letter are malformed — not the real wordmark | **Critical** |
| F2 | **A9d garbled UI/fine text** | The tablet dashboard shows pseudo-glyph labels and a chart with no real numbers | **Critical** |
| F3 | **A7 / A9c uncanny face & micro-anatomy** | Shopkeeper's eyes are glassy with too-symmetric catchlights; the hand on the counter has a fused ring-and-little-finger on zoom | **Critical** |
| F4 | **A9a plastic default-render lighting** | Uniform golden-hour glow + creamy bokeh — the convergent AI house style, no authored point of view (A9f) | Major |
| F5 | **B4 decorative "AI ✨" badge + gradient** | The sparkle pill and purple→blue gradient signal "AI" as decoration; no stated user benefit | Major |
| F6 | **B2 ungrounded chatbot invents commitments** | Bot answers "Yes, the Pro plan is $9/mo with free onboarding" — a price/policy it cannot honour; no guardrail, no source, no human handoff | **Critical** |
| F7 | **B1 AI where search was faster** | The questions asked (pricing, plans) are a 2-click pricing page; chat is slower and riskier | Major |

**Tally:** 4 critical, 3 major, 0 minor → **ship blocked.**

---

## 2. Disposition (remake / remediate + human-craft alternative)

| # | Decision | Human-craft alternative (Mission test) |
|---|---|---|
| F1 | **Remake** (do not patch the sign) | Commission a real photo, or composite the *actual* Maduuka wordmark (correct letterforms, brand file) onto a clean shot. A warped logo is never spot-fixed. |
| F2 | **Remake** | Screenshot the *real* Maduuka dashboard with real (anonymised) data; never a hallucinated UI. |
| F3 | **Remake / replace** | Use real photography of a real merchant (with release), art-directed — or a commissioned illustration with an authored style. Impossible anatomy is remade, not retouched. |
| F4 | **Remake / art-direct** | Direct the shoot: specific lens, location, colour grade tied to the brand palette — one committed, authored look, not golden-hour-on-everything. |
| F5 | **Remove** | Drop the sparkle + gradient. If AI assist genuinely helps, label it for what it *does* ("Help me set up"), not what it *is*. |
| F6 | **Remove or ground** | Replace the open chatbot with: (a) a deterministic pricing/plans page, and if assistance is kept, (b) a retrieval-grounded helper that cites the pricing page, refuses out-of-scope commitments, shows confidence, and offers human handoff. |
| F7 | **Remove** | Surface a clear **Pricing** and **Plans** nav item + search. Add AI only where it beats nav, not as a hammer. |

---

## 3. After (remediated artifact)

- Hero: art-directed photograph of a real Maduuka merchant in a real shop, brand-graded, with the
  correct wordmark composited and a genuine dashboard screenshot on the tablet. Authored, specific,
  unmistakably human-made.
- Nav: a **Pricing** + **Plans** link and search. The AI helper, if kept, is a grounded "Help me set
  up" assistant — cites the pricing page, declines to quote unhonourable terms, shows a "may be
  wrong, verify here" cue and a human-handoff. No sparkle, no decorative gradient.

### Result

0 critical / 0 major remaining → **clears the visual-product slop gate.** Every fix names what a
skilled designer ships instead — passing the Mission test ("would a named designer have made this
exact choice?").

---

## Cross-references

- `../references/visual-tells-checklist.md` (tell IDs used above).
- `doctrine/references/ai-slop-taxonomy.md` (categories 2 & 5).
- `doctrine/design-doctrine.md` §0 Mission.
