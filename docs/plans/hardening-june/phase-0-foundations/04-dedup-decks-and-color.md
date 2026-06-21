# Phase 0.4 — De-dup: Decks & Colour/Brand

## A. The 8 deck skills → one `_deck-system/`
**Problem:** `deck-ai-strategy-presentation, deck-annual-review, deck-campaign-proposal,
deck-credentials, deck-initial-pitch, deck-monthly-report, deck-quarterly-review,
deck-strategy-presentation` are ~8 copies of one template differing mainly by slide count and
purpose (audit: "8× one deck template").

**Target:** in group `13-presentations-and-documents/`, create one canonical
`deck-system/SKILL.md` that owns the shared deck-design doctrine (narrative arc, slide economy,
grid, type, builds, presenter craft) and carries the 8 purposes as **variant references**:
```
13-presentations-and-documents/deck-system/
├── SKILL.md                      # the deck-design discipline + how to pick a variant
├── references/
│   ├── deck-narrative-and-structure.md
│   └── presenter-and-delivery.md
└── examples/
    ├── variant-initial-pitch.md       # the old deck-initial-pitch content as a worked outline
    ├── variant-strategy.md
    ├── variant-ai-strategy.md
    ├── variant-campaign-proposal.md
    ├── variant-credentials.md
    ├── variant-monthly-report.md
    ├── variant-quarterly-review.md
    └── variant-annual-review.md
```
**Steps:** create `deck-system`; fold each old deck's *unique* content (slide list, purpose,
tone) into a `examples/variant-*.md`; write the shared SKILL.md; `git rm` the 8 old folders;
update routing. **Net skill count: 8 → 1** (variants are examples, not skills). Note the drop in
the migration manifest. *(Keep this as P0 narrative craft — see Phase 1 #53 `pitch-deck-narrative-and-craft`, which can BE this skill or pair with it; decide at build time — recommend deck-system = the craft skill, #53 folds in.)*
**Effort: M.**

## B. Colour/brand overlap (5 skills) in new group `02-color-brand-and-visual-identity/`
Current 5: `color-selection`, `color-system-and-palette`, `brand-alignment`, `brand-style-guide`,
`brand-visual-identity`. Audit flagged "5 overlapping colour/brand skills"; `brand-alignment`
scored the engine's lowest (44).

**Resolution (keep boundaries, don't over-merge):**
- **Colour (2, keep both, cross-linked):** `color-system-and-palette` (the SYSTEM — roles, ramps,
  OKLCH, dark-mode, contrast) is canonical; `color-selection` (palette GENERATION — mood, harmony)
  stays as its sibling. Already framed this way; just confirm the cross-refs.
- **Brand (3 → 2):** `brand-visual-identity` is canonical for *building* identity;
  `brand-style-guide` stays as the *deliverable* (the documented guide). **Merge `brand-alignment`
  (weakest, 44) INTO `brand-visual-identity` as a `references/brand-consistency-gate.md`** — it's a
  consistency quality-gate, not a standalone discipline. `git rm` brand-alignment after folding.
**Net: 5 → 4.**
**Effort: M.**

## Acceptance
Decks consolidated (8→1, variants preserved as examples); brand-alignment folded; counts + manifest
updated; no lost content; routing updated.
