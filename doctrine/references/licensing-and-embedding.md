# Reference: Licence Check - Mandatory Before Embedding

Embedding redistributes the font file. Many commercial fonts forbid this. Chwezi client
deliverables are distributed externally under the Chwezi Core Systems name, so this is not
optional.

## The rule

1. Before embedding any font, confirm the licence permits the intended use and embedding.
2. OFL (SIL Open Font License) and other open licences are generally safe to use and embed, but
   this must still be recorded in the matching `fonts/<category>/MANIFEST.md`.
3. Fontshare fonts (Clash Display, Satoshi, Cabinet Grotesk, General Sans) are free to use and
   embed in documents/apps/web, but the raw font files may not be redistributed. They live in
   the gitignored `fonts/03-modern-product-grotesque/` folder and must never be committed.
4. Unknown or restrictive licence means do not embed. Choose an OFL alternative from
   `font-groups-and-usage.md` instead.

## How to record the decision

Each `fonts/<category>/MANIFEST.md` states, per family: role, voice, best use, avoid use,
pairing guidance, licence, whether embedding is permitted, and whether file redistribution is
permitted. The `premium-font-scan` skill reads the manifest before using a premium family. If the
manifest does not grant the permission the artifact needs, the skill falls back to the named OFL
baseline and says so.

## Quick table

| Category | Typical licence | Embed in artifact? | Commit file to repo? |
|---|---|---|---|
| 01 Formal / Institutional | OFL or verified commercial | Yes if manifest permits | No by policy |
| 02 Editorial / Literary | OFL or verified commercial | Yes if manifest permits | No by policy |
| 03 Product / Grotesque - Bricolage | OFL | Yes | No by policy |
| 03 Product / Grotesque - Fontshare families | Fontshare | Yes | No, redistribution forbidden |
| 04 Technical / Data / Code | OFL or verified commercial | Yes if manifest permits | No by policy |
| 05 Friendly / Humanist | OFL or verified commercial | Yes if manifest permits | No by policy |
| 06 Expressive Display / Artistic | OFL or verified commercial | Yes if manifest permits | No by policy |
| 07 Script / Cursive / Handwritten | OFL or verified commercial | Yes if manifest permits | No by policy |
| 08 Body / UI Workhorses | OFL or verified commercial | Yes if manifest permits | No by policy |

Policy: regardless of OFL permission, font binaries are gitignored across the board and tracked
only via MANIFEST. This keeps the repo light and keeps the Fontshare rule uniform.
