---
name: premium-font-scan
description: Use before committing to a typeface to scan the engine's fonts/<category>/ folders for premium font files the user has purchased and dropped in, read each category's MANIFEST for role, voice, licence, and embedding permission, and decide whether a premium family should override the named OFL baseline for this artifact. Implements the standard-first, premium-when-present rule.
status: active
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
    - claude-code
    - codex
---

# Premium Font Scan
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- About to commit to a typeface and you want to check whether a purchased premium family is
  available and would look better than the OFL baseline.
- Called as step 2 of `font-selection-and-pairing`.

## Do Not Use When

- No font category has been chosen yet - classify the artifact first.

## Required Inputs

- The chosen font category and the artifact's output format and intended use, so the licence
  check is meaningful: embedding, reference, or raw file shipment.

## Workflow

1. **Locate the folder:** `fonts/<matching-category>/` in this engine. Categories are:
   `01-formal-institutional`, `02-editorial-literary`, `03-modern-product-grotesque`,
   `04-technical-data-code`, `05-friendly-humanist`, `06-expressive-display-artistic`,
   `07-script-cursive-handwritten`, and `08-body-ui-workhorses`.
2. **List present families.** Premium binaries are gitignored, so they may or may not be on this
   device. List whatever `.ttf`/`.otf`/`.woff2` families are actually present.
3. **Read `MANIFEST.md`** in that folder. For each present family confirm: role, voice, best
   use, avoid-for notes, pairing guidance, licence, embedding permitted?, and file
   redistribution permitted?
4. **Decide:** if a present family fits the artifact's voice and role better than the baseline
   and its MANIFEST grants the permission the format needs, use it. Otherwise use the named OFL
   baseline from `font-groups-and-usage.md`.
5. **Never ship a file you may not redistribute.** Embedding a Fontshare face into a built
   artifact is fine; committing or shipping the raw file is not.
6. **Report** which family was chosen and why: premium vs baseline, category, role, pairing,
   and licence basis.

## Anti-Patterns

- Using a premium family whose MANIFEST does not grant the needed permission.
- Assuming a premium file is present because it is on another device - always list first.
- Committing premium binaries into any repo.
- Scanning a body workhorse category when the artifact needs an expressive display face.
- Using a script/cursive face for body text or dense UI.

## Outputs

- The resolved typeface, premium or baseline, with role, voice, pairing, and licence basis
  recorded for the embedding step.

## Examples

- `examples/premium-scan-worked.md` - a full worked scan for a startup-product artifact: scan
  `fonts/03-modern-product-grotesque/`, read its MANIFEST, find Satoshi present, apply its
  Fontshare embed-yes/redistribute-no rule, decide premium-vs-baseline with the licence basis
  stated, and record the resolved face.

## References

- `doctrine/references/font-groups-and-usage.md`, `licensing-and-embedding.md`;
  the per-category `fonts/<category>/MANIFEST.md`.
<!-- dual-compat-end -->
