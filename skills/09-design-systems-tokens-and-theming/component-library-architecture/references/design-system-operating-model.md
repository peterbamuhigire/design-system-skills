# Design-System Operating Model

Parent skill: [`../SKILL.md`](../SKILL.md) (`component-library-architecture`). Also cited by
`design-tokens-and-naming`, `design-handoff-and-dev-spec`, `practical-ui-design`,
`chart-selection-and-encoding`, `ux-research-and-usability-testing` and
`design-qa-and-pre-launch-review`.

**When to read:** when setting up or reviewing a design system, a token source, component
contracts, adoption measures, or the evidence chain for a major design output. Paraphrased and
synthesised from: Mangialardi, M. *Design Systems for Developers*; Hoskins, D. *The Product-Minded
Engineer*; Braganza, A. *Looks Good to Me*; Mall, D. *Design That Scales*; Pickering, H.
*Inclusive Components*; Wathan, A. and Schoger, S. *Refactoring UI*; Krug, S. *Rocket Surgery
Made Easy*; Knaflic, C. N. *Storytelling with Data*; Wiegers, K. *Software Requirements
Essentials*. Book-specific numbers, code and example typography are not adopted.

---

## 1. One authored source of truth for tokens

- Keep design decisions in a versioned, reviewed token source; generate platform outputs from it.
  No competing hand-edited copies in CSS, code, design files and documentation.
- Each token carries a stable name, type, description, semantic purpose and owner where that
  matters for safe change.
- Three layers: **primitives** (raw values), **semantic tokens** (surface, text, border, focus,
  action, danger), **component tokens** (component decisions and states). Aliases express intent,
  never hide arbitrary values.
- Record transformations, supported platforms, generated-file ownership and the deprecation path.
- Interchange format status: the W3C Design Tokens Community Group format is a community report,
  not a W3C Standard. Check its current status before calling any format a standard.

## 2. Component contract

For each reusable component document: user jobs, variants, responsive behaviour, interaction
states, validation and error behaviour, accessibility semantics, content limits and
implementation boundaries. Use a **state matrix** (default, hover, focus-visible, active,
loading, empty, disabled, error, success, overflow, long content, interruption) rather than a
happy-path screenshot.

Inclusive component rules:
- Prefer native semantic controls; expose state to sighted, keyboard and assistive-technology
  users alike.
- Keep navigation semantics separate from application-menu semantics; never put essential
  instructions only in tooltips.
- Treat tabs, collapsibles, sliders, tables and cards as content-and-state systems.
- Preserve source order, keyboard access and meaningful labels across responsive variants.
- Test variable content: long labels, missing images, odd ratios, narrow widths, translation
  expansion, and no-script fallback.
- Verify against current WCAG 2.2, the ARIA Authoring Practices and real assistive technology;
  do not copy historical ARIA advice.

## 3. Build order for screens

Feature first, then hierarchy, then detail: solve structure in greyscale before colour; de-
emphasise secondary content rather than shouting everything; treat spacing as relationships;
tune the type scale for context; use a small colour system with roles and contrast checks; add
personality through coherent choices, not random decoration.

## 4. Grow the system from real product work

- Pilot inside a real product; extract components after patterns prove useful in several places.
- Abstract only where variation evidence supports it.
- Governance answers: what is covered, why, who decides, when changes happen, where decisions are
  recorded, how contribution, review and deprecation work.
- Documentation leads with working examples in product context; an inventory alone is not
  enablement. Aim for unity, not uniformity.

## 5. Measure adoption and outcomes

An adoption scorecard names the owner, sample, baseline, target, review date and corrective
action, and tracks: use of official tokens, components and packages; recorded exceptions; task
success; defects and accessibility failures; migration effort; contribution health; maintenance
cost. Visual fidelity alone is not adoption.

## 6. Handoff behaviour, not only appearance

Handoff links component intent to tokens, semantics, interaction rules, content, responsive limits
and testable acceptance criteria. Anything not demonstrated or verified is marked unassessed.

## 7. Evidence chain for major design outputs

Trace: problem and outcome → audience and task → design decision → token and component → state
and interaction → evidence → release verdict. Every major output carries:
1. a short problem/outcome brief with the audience's action;
2. a state and content matrix including failure and recovery;
3. a semantic, accessibility and responsive plan;
4. a token/component decision record with rationale and uncertainty;
5. a prototype or render evidence bundle;
6. a lightweight usability observation and fix/retest record where risk warrants it
   (`ux-research-and-usability-testing/references/pre-design-research-and-usability-loop.md`);
7. a release verdict that separates schema validity, evidence completeness and human acceptance;
8. an owner, change path and metric plan.

For data exhibits inside that chain: state the audience, the decision and the one big idea
before choosing a chart; declutter; direct-label; give a text alternative; test with a real task
(`chart-selection-and-encoding`).

Scale the weight of this chain to risk; do not impose it on low-risk work.
