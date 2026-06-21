---
name: premium-font-scan
description: Use before committing to a typeface to scan the engine's fonts/<group>/ folders for premium font files the user has purchased and dropped in, read each group's MANIFEST for licence/embedding permission, and decide whether a premium family should override the named OFL baseline for this artifact. Implements the standard-first, premium-when-present rule.
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

- No font group has been chosen yet — classify the artifact first.

## Required Inputs

- The chosen font group (1–4) and the artifact's output format and intended use (so the licence
  check is meaningful — embedding vs reference vs file-ship).

## Workflow

1. **Locate the folder:** `fonts/<matching-group>/` in this engine. The four groups mirror the
   user's `Downloads\Fonts`: `1-Editorial-Authoritative`, `2-Developer-Technical`,
   `3-Startup-Product`, `4-Body-Workhorses`.
2. **List present families.** Premium binaries are gitignored, so they may or may not be on this
   device. List whatever `.ttf`/`.otf`/`.woff2` families are actually present.
3. **Read `MANIFEST.md`** in that folder. For each present family confirm: licence, embedding
   permitted?, file-redistribution permitted?
4. **Decide:** if a present family fits the artifact's mood better than the baseline **and** its
   MANIFEST grants the permission the format needs → use it. Otherwise use the named OFL
   baseline from `font-groups-and-usage.md`.
5. **Never ship a file you may not redistribute.** Embedding a Fontshare face into a built
   artifact is fine; committing or shipping the raw file is not.
6. **Report** which family was chosen and why (premium vs baseline), and the licence basis.

## Anti-Patterns

- Using a premium family whose MANIFEST does not grant the needed permission.
- Assuming a premium file is present because it is on another device — always list first.
- Committing premium binaries into any repo.

## Outputs

- The resolved typeface (premium or baseline) with its licence basis recorded for the embedding
  step.

## References

- `doctrine/references/font-groups-and-usage.md`, `licensing-and-embedding.md`;
  the per-group `fonts/<group>/MANIFEST.md`.
<!-- dual-compat-end -->
