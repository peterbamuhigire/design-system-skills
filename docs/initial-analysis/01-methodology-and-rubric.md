# Methodology & Scoring Rubric

## How this audit was run

Six independent agents ran in parallel, each owning distinct report files, to avoid single-
viewpoint bias and to let strict scores emerge independently before synthesis:

1. **2026 standards benchmark** (`06`) — cited research under the **digital-research engine's**
   no-hallucination rule (every version fact primary-source-verified, inline URLs).
2. **Reading list** (`08`) — cited research, real ISBNs, honouring the doctrine's sourcing-
   authority asymmetry (human design authority only; HIG/Material as implementation constraints).
3. **Existing-skills audit** (`03`) — deep read of all 37 SKILL.md + references; per-skill scores.
4. **Taxonomy & gap analysis** (`02`, `04`) — structure sufficiency + missing-skill enumeration.
5. **Per-output-type readiness** (`05`) — scored 10 deliverable types against the bar.
6. **Hardening plan** (`07`) — concrete `references/*` + `examples/*` build plan per skill.

The connective files (`00`, `01`, `09`, `10`) are the synthesis, reconciling the six.

## The scoring rubric (deliberately ruthless)

The reference standard is the **top 0.1% globally** — Pentagram, IDEO, Instrument, MetaLab, Clay,
Work & Co, Koto; Apple/Stripe/Linear/Vercel/Figma product design; Awwwards SOTD, Apple Design
Awards, D&AD, CSSDA, FWA, Webby winners.

| Band | Meaning |
|---|---|
| **90–100** | Rivals the named studios/award winners. Essentially nothing missing. |
| **75–89** | Excellent professional. Minor gaps only. |
| **60–74** | Solid but **visibly short** of world-class. Notable gaps. |
| **40–59** | Competent / amateur-to-pro. Major gaps. |
| **< 40** | Skeletal / inadequate. |

**Strictness directive (enforced):** default to **45–65**. A 70+ requires extraordinary, specific
justification. *If you are tempted to score 70+, you have not been strict enough — find what is
missing.* Every score is justified with concrete deficiencies (named missing techniques, absent
reference files, missing worked examples, stale standards), never vibes.

## What "world-class" was measured against
- **Craft**: typographic rigor, grid discipline, deliberate colour, motion quality, distinctive
  (non-templated) point of view.
- **Standards (2026)**: WCAG 2.2 (+ 3.0 draft / APCA), Core Web Vitals, modern CSS Baseline,
  Apple HIG (Liquid Glass), Material 3 Expressive.
- **Completeness**: can the engine actually drive each deliverable type end-to-end?
- **Applied proof**: worked examples, reference depth, production/handoff readiness.
