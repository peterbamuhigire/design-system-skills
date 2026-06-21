# Audit Rubric — scored gates (slop + a11y + perf)

This rubric turns the 10 audit dimensions (see `SKILL.md` §2) into a **scored, repeatable**
instrument. It composes three hard gates — **AI Slop**, **Accessibility (WCAG 2.2)**, and
**Performance (Core Web Vitals)** — then weights all ten dimensions into a 0–100 score.

Use it whenever an audit needs a defensible number, not just prose findings. Score each
dimension 0–4, multiply by its weight, sum, and apply the gate overrides.

Provenance: composes `doctrine/references/ai-slop-taxonomy.md`,
`doctrine/references/wcag-2.2-criteria.md`, and
`doctrine/references/web-performance-budgets-2026.md`. AA is the accessibility floor for all
Chwezi work; CWV "good" (field p75) is the performance floor.

---

## 1. The three hard gates (pass/fail — they cap the score)

A dimension score alone can flatter a broken product. These gates **override** the weighted
total: failing one caps the maximum achievable score regardless of how the other dimensions
look.

| Gate | Source ref | Fail condition (any one) | Cap on overall score if FAILED |
|---|---|---|---|
| **AI Slop** | `ai-slop-taxonomy.md` | Immediately reads as machine-generated (banned default font + generic palette + uniform cards); OR any "feature cramming" tell (AI inserted where nav/search was faster; ungrounded chatbot inventing commitments); OR slop imagery tell (warped logo, gibberish signage, uncanny faces, impossible physics) | **≤ 59** ("major redesign") |
| **Accessibility (WCAG 2.2 AA)** | `wcag-2.2-criteria.md` | Body text < 4.5:1 or UI/graphics < 3:1 (1.4.3 / 1.4.11); OR not keyboard-operable / no visible focus order (2.1.1 / 2.4.7); OR target < 24×24 CSS px without spacing (2.5.8); OR focus obscured by sticky chrome (2.4.11); OR a drag with no single-pointer alternative (2.5.7); OR control missing name/role/value (4.1.2) | **≤ 59** (a11y is a legal floor) |
| **Performance (CWV)** | `web-performance-budgets-2026.md` | Field p75 **LCP > 2.5 s**, OR **INP > 200 ms**, OR **CLS > 0.1**; OR page over its archetype asset budget (e.g. marketing total > 1 MB gz) | **≤ 74** ("significant issues") |

> Two gates failed → cap at the lower of the two caps. The slop and a11y gates are the
> non-negotiables; never report ≥ 60 while either is failing.

---

## 2. Dimension scoring (0–4 per dimension)

Score each of the ten dimensions on this scale, then weight. Anchors:

| Score | Anchor |
|---|---|
| **4** | Exemplary — authored, deliberate, exceeds the standard. |
| **3** | Solid — meets the standard, minor polish only. |
| **2** | Partial — meets some checks, noticeable gaps. |
| **1** | Weak — fails most checks in the dimension. |
| **0** | Absent / actively harmful — triggers a gate where applicable. |

### Weights (same as `SKILL.md` §4; sum = 100%)

| # | Dimension | Weight | Gate it feeds |
|---|---|---|---|
| 3 | Accessibility | 20% | **A11y gate** |
| 2 | Visual Hierarchy | 15% | — |
| 7 | Interaction States | 12% | — |
| 9 | Content & Microcopy | 12% | — |
| 4 | Typography | 10% | (slop: banned fonts) |
| 5 | Colour | 8% | (slop: generic palette; a11y: contrast) |
| 6 | Layout & Spacing | 8% | — |
| 10 | Performance | 6% | **Perf gate** |
| 8 | Motion | 5% | (a11y: reduced motion) |
| 1 | AI Slop | 4% | **Slop gate** |

**Weighted score** = Σ (dimension_score ÷ 4 × weight) → 0–100. Then apply §1 caps.

### Per-dimension gate triggers (the 0/fail rows)

- **Accessibility → 0/fail** if any A11y-gate condition in §1 is true. New WCAG 2.2 criteria to
  spot-check while scoring: 2.4.11 Focus Not Obscured, 2.5.8 Target Size (24px), 2.5.7 Dragging
  Movements, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication, 3.2.6 Consistent Help.
- **Performance → 0/fail** if any CWV threshold or asset budget in §1 is breached. Verify CWV
  from **field p75** (CrUX/RUM) where available; lab (Lighthouse) is a proxy only.
- **AI Slop → 0/fail** if any slop tell in §1 fires. This is a binary distinctiveness check, so
  its 4% weight is small — the gate (not the weight) does the work.

---

## 3. Banding (after caps applied)

| Score | Band | Meaning |
|---|---|---|
| 90–100 | Production-ready | Minor polish only. |
| 75–89 | Good foundation | Fix high-priority issues before shipping. |
| 60–74 | Significant issues | Focused remediation sprint. |
| 40–59 | Major redesign | Multiple dimensions failing. |
| < 40 | Fundamental | Start with structure and hierarchy. |

---

## 4. Worksheet (copy into the report)

```
Gates:  AI Slop [PASS/FAIL]  ·  A11y WCAG 2.2 AA [PASS/FAIL]  ·  CWV [PASS/FAIL]
Caps applied: [none | ≤59 | ≤74]

| # | Dimension          | Weight | Score (0–4) | Weighted |
|---|--------------------|--------|-------------|----------|
| 3 | Accessibility      | 20%    |             |          |
| 2 | Visual Hierarchy   | 15%    |             |          |
| 7 | Interaction States | 12%    |             |          |
| 9 | Content & Microcopy| 12%    |             |          |
| 4 | Typography         | 10%    |             |          |
| 5 | Colour             | 8%     |             |          |
| 6 | Layout & Spacing   | 8%     |             |          |
| 10| Performance        | 6%     |             |          |
| 8 | Motion             | 5%     |             |          |
| 1 | AI Slop            | 4%     |             |          |
|   | RAW TOTAL          | 100%   |             | /100     |
|   | AFTER CAPS         |        |             | /100     |
```

Weighted column = (Score ÷ 4) × Weight. Raw total is the sum; "after caps" applies §1.

---

*Composes the three cross-cutting references named above. Certify accessibility against the
WCAG 2.x ratios; design with APCA. Set the CWV thresholds as Lighthouse-CI build gates so the
perf gate is enforced, not just observed.*
