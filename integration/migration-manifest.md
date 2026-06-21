# Migration Manifest (APPROVED 2026-06-21)

Consolidates design/presentation skills from the domain engines into design-system-skills.
**Model:** reference (not mirror). **Decisions locked:** website = move portable / keep
build-coupled; blended engineering skills = leave + reference (only tailwind & avalonia split);
execution = phased, safe-first. Source deletions happen only after the additive copy is verified.

Safety rules (from integration-plan.md): `git pull --ff-only` each source before touching it;
no per-skill stubs (the engine's trigger block is the single pointer); update counts after each
phase.

---

## PHASE 1 — clean, non-duplicated, standalone MOVES (low risk)

### From engineering-catalog (`C:\wamp64\www\skills-web-dev`, relocated 2026-06-21) — 11 skills

| Source skill folder | → Destination group |
|---|---|
| `skills\frontend-ux\design-audit` | 03-web-and-ui-design |
| `skills\frontend-ux\healthcare-ui-design` | 03-web-and-ui-design |
| `skills\frontend-ux\motion-design` | 03-web-and-ui-design |
| `skills\frontend-ux\practical-ui-design` | 03-web-and-ui-design |
| `skills\frontend-ux\webapp-gui-design` | 03-web-and-ui-design |
| `skills\frontend-ux\interaction-design-patterns` | 03-web-and-ui-design |
| `skills\frontend-ux\enterprise-ux-process` | 03-web-and-ui-design |
| `skills\ai\ai-agent-ux` | 03-web-and-ui-design |
| `skills\ai\ai-output-design` | 03-web-and-ui-design |
| `skills\android\android-ui-ux-design` | 06-mobile-ui-ux |
| `skills\ios\ios-ui-ux-design` | 06-mobile-ui-ux |

### From social-media-skills (`C:\wamp64\www\social-media-skills`) — 8 skills

| Source skill folder | → Destination group |
|---|---|
| `skills\decks\deck-ai-strategy-presentation` | 02-document-formatting |
| `skills\decks\deck-annual-review` | 02-document-formatting |
| `skills\decks\deck-campaign-proposal` | 02-document-formatting |
| `skills\decks\deck-credentials` | 02-document-formatting |
| `skills\decks\deck-initial-pitch` | 02-document-formatting |
| `skills\decks\deck-monthly-report` | 02-document-formatting |
| `skills\decks\deck-quarterly-review` | 02-document-formatting |
| `skills\decks\deck-strategy-presentation` | 02-document-formatting |

> Note: the 8 decks share a deck-design doctrine but carry social-media-specific content. They
> move as-is in Phase 1; a later pass can extract shared deck-visual doctrine if wanted.

**Phase 1 relief:** engineering-catalog 153 → 142; social-media 184 → 176.

---

## PHASE 2 — dedup consolidations + visual identity + website portable (medium)

- **Dedup to one canonical copy here, both old homes reference it:**
  - `data-visualization` (engineering-catalog `frontend-ux` + digital-research) → 05-layout-grid-and-data-viz
  - `professional-word-output` (engineering-catalog `product-business` + digital-research) → 02-document-formatting
  - `premium-ui-ux-design` (engineering-catalog `frontend-ux` + website `orchestration`) → 03-web-and-ui-design
  - `form-ux-design` (engineering-catalog `frontend-ux` + website `ux-conversion`) → 03-web-and-ui-design
- **Visual identity (social + website):** `platform-instagram-visual-system`,
  `playbook-social-media-brand-style-guide`, website `brand\brand-style-guide`,
  `build\color-selection`, `brand\brand-alignment` → 04-color-and-visual-identity
- **AI imagery:** social `image-prompt-engineer`, `prompt-library-image-audio-video` → 05.
- **Website portable design knowledge (keep build-coupled in place):** `ux-conversion\ux-psychology`,
  `build\sector-strategies`, `sectors\legal`, `quality-gates\design-quality-score` (rubric) →
  03-web-and-ui-design. **KEEP in website-skills:** `design-system`, `page-builder`, `visual-qa`,
  `website-builder` (build pipeline) — add reference only.
- **business-plan decks:** `meta-pitch\pitch-deck`, `meta-pitch\meta-presentation-design` → 02.
- **digital-research clean moves:** `markdown-lint-cleanup` → 02; `data-visualization` (see dedup).

---

## PHASE 3 — SPLITs + reference wiring (careful)

- **Split (clean seam only):** `tailwind-css` (tokens → design; mechanics stay),
  `avalonia-desktop-development` (XAML theming → design; MVVM stays).
- **Leave + reference (do NOT split):** `react-development`, `nextjs-app-router`,
  `frontend-performance`, `kmp-development`, `pwa-offline-first`, `image-compression`,
  ecommerce/cro/cro-audit, srs `05-ux-specification` design-system half, slop-audit visual gates.
- **Add the trigger block** (integration-plan.md §1) to every engine's CLAUDE.md + AGENTS.md,
  and a row to the user's global `~/.claude/CLAUDE.md` engine table.

---

## Status log

- 2026-06-21: manifest approved; Phase 1 beginning (additive copy first, then source deletion).
- 2026-06-21: **Phase 1 COMPLETE.** 19 skills migrated (copied to design engine, then deleted
  from source): 11 from skills-web-dev (frontend-ux design cluster + ai-agent-ux + ai-output-
  design + android/ios UI → groups 03 & 06), 8 deck skills from social-media → group 02.
  skills-web-dev 153→142; social-media 184→176. All 9 engines wired with the portable trigger
  block. (Embedded finance doctrine mirror in skills-web-dev untracked + gitignored.)
- Pending: Phase 2 (dedup consolidations + visual identity + website portable) and Phase 3
  (tailwind/avalonia splits + reference wiring + doctrine-alignment of migrated skills).
