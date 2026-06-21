# Phase 0.1 — Taxonomy Migration (37 skills → 13 + 1 groups)

Source of truth: `docs/initial-analysis/02-coverage-and-taxonomy.md`. **No skill is deleted** —
every one moves (git mv) to exactly one new group, and its `metadata.category` is updated.

## Target group folders
```
skills/
├── 01-typography-and-fonts/
├── 02-color-brand-and-visual-identity/
├── 03-layout-grid-and-composition/
├── 04-web-and-ui-design/
├── 05-ux-process-research-and-psychology/
├── 06-sector-and-domain-ux/
├── 07-mobile-ios-android-cross-platform/
├── 08-motion-and-interaction/
├── 09-design-systems-tokens-and-theming/   (new)
├── 10-content-design-and-ux-writing/        (new)
├── 11-imagery-illustration-and-art-direction/ (new)
├── 12-data-viz-and-dashboards/
├── 13-presentations-and-documents/
└── 00-cross-cutting-ops-qa-a11y/            (new — co-activates with every group)
```
> `00-` prefix on the cross-cutting group signals "always-on" (co-activates like the finance
> engine), while staying glob-discoverable. Document the co-activation in its group README.

## The complete old → new mapping (all 37)

| Current path | New path | category value |
|---|---|---|
| 01-typography-and-fonts/font-selection-and-pairing | 01-typography-and-fonts/ | 01-typography-and-fonts |
| 01-typography-and-fonts/ai-slop-typography-audit | 01-typography-and-fonts/ *(cross-links to 00)* | 01-typography-and-fonts |
| 01-typography-and-fonts/premium-font-scan | 01-typography-and-fonts/ | 01-typography-and-fonts |
| 01-typography-and-fonts/font-embedding-and-licensing | 01-typography-and-fonts/ | 01-typography-and-fonts |
| 02-document-formatting/deck-* (×8) | 13-presentations-and-documents/ *(see de-dup §4)* | 13-presentations-and-documents |
| 03-web-and-ui-design/practical-ui-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/distinctive-by-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/webapp-gui-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/premium-ui-ux-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/interaction-design-patterns | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/form-ux-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/ai-agent-ux | 04-web-and-ui-design/ *(AI-native UI craft)* | 04-web-and-ui-design |
| 03-web-and-ui-design/ai-output-design | 04-web-and-ui-design/ | 04-web-and-ui-design |
| 03-web-and-ui-design/enterprise-ux-process | 05-ux-process-research-and-psychology/ | 05-ux-process-research-and-psychology |
| 03-web-and-ui-design/ux-psychology | 05-ux-process-research-and-psychology/ | 05-ux-process-research-and-psychology |
| 03-web-and-ui-design/healthcare-ui-design | 06-sector-and-domain-ux/ | 06-sector-and-domain-ux |
| 03-web-and-ui-design/legal-sector-ui-ux | 06-sector-and-domain-ux/ | 06-sector-and-domain-ux |
| 03-web-and-ui-design/sector-strategies | 06-sector-and-domain-ux/ | 06-sector-and-domain-ux |
| 03-web-and-ui-design/motion-design | 08-motion-and-interaction/ | 08-motion-and-interaction |
| 03-web-and-ui-design/design-audit | 00-cross-cutting-ops-qa-a11y/ | 00-cross-cutting-ops-qa-a11y |
| 03-web-and-ui-design/visual-product-slop-audit | 00-cross-cutting-ops-qa-a11y/ | 00-cross-cutting-ops-qa-a11y |
| 04-color-and-visual-identity/* (×5) | 02-color-brand-and-visual-identity/ | 02-color-brand-and-visual-identity |
| 05-layout-grid-and-data-viz/layout-grid-and-spacing | 03-layout-grid-and-composition/ | 03-layout-grid-and-composition |
| 05-layout-grid-and-data-viz/data-visualization | 12-data-viz-and-dashboards/ | 12-data-viz-and-dashboards |
| 06-mobile-ui-ux/android-ui-ux-design | 07-mobile-ios-android-cross-platform/ | 07-mobile-ios-android-cross-platform |
| 06-mobile-ui-ux/ios-ui-ux-design | 07-mobile-ios-android-cross-platform/ | 07-mobile-ios-android-cross-platform |

## Execution steps (per skill, scripted by source-group)
1. `git mv skills/<old>/<skill> skills/<new-group>/<skill>` (preserves history).
2. Update the moved skill's frontmatter `metadata.category` to the new value.
3. Repoint any internal cross-refs that named the old group path.
4. After each source-group is moved, delete the now-empty old group folder.

## Routing updates (one commit at the end)
- Rewrite the README router table + Layout block to the 14 groups.
- Update `CLAUDE.md` / `AGENTS.md` group references.
- Update `doctrine/design-doctrine.md` §3 "How the engine is organised" table.
- Update `integration/migration-manifest.md` to log the restructure.

## Acceptance
- `find skills -name SKILL.md` count unchanged (37 + any de-dup delta); old group folders gone;
  every `metadata.category` matches its folder; routers list 14 groups; no dangling links.
**Effort: L.**
