# Reference: Licence Check — Mandatory Before Embedding

Embedding **redistributes** the font file. Many commercial fonts forbid this. Chwezi client
deliverables are distributed externally under the Chwezi Core Systems name, so this is not
optional.

---

## The rule

1. **Before embedding any font, confirm the licence permits embedding/redistribution** in the
   intended artifact.
2. **OFL (SIL Open Font License)** — most Google Fonts — is safe to embed and ship. All Group
   1, 2, and 4 baselines, plus Bricolage Grotesque in Group 3, are OFL.
3. **Fontshare fonts (Clash Display, Satoshi, Cabinet Grotesk, General Sans)** — free to *use
   and embed* in documents/apps/web, but **the font files may not be redistributed** as files.
   This is why they live in the gitignored `fonts/3-Startup-Product/` folder, never committed
   to the repo: shipping a built artifact that *embeds* them is fine; committing the `.ttf`/
   `.otf` to a repo is redistribution and is not.
4. **Unknown or restrictive licence → do not embed.** Choose an OFL alternative from
   `font-groups-and-usage.md` instead.

---

## How to record the decision

Each `fonts/<group>/MANIFEST.md` states, per family: the licence, whether **embedding** is
permitted, and whether **file redistribution** is permitted. The premium-font-scan skill reads
the MANIFEST before using a premium family — if the MANIFEST does not grant the permission the
artifact needs, the skill falls back to the named OFL baseline and says so.

---

## Quick table

| Family group | Typical licence | Embed in artifact? | Commit file to repo? |
|---|---|---|---|
| 1 Editorial (Fraunces, Crimson Pro, Newsreader, Source Serif 4, Spectral) | OFL | Yes | Yes (but kept out by policy — scan-not-commit) |
| 2 Developer (IBM Plex *, JetBrains Mono, Fira Code, Space Mono) | OFL / Apache | Yes | Yes |
| 3 Startup — Bricolage Grotesque | OFL | Yes | Yes |
| 3 Startup — Clash Display, Satoshi, Cabinet Grotesk, General Sans | Fontshare | **Yes** | **No — redistribution forbidden** |
| 4 Workhorse (Public Sans, Hanken Grotesk, Source Sans 3) | OFL | Yes | Yes |

> Policy: regardless of OFL permission, premium binaries are **gitignored** across the board and
> tracked only via MANIFEST — this keeps the repo light and the Fontshare rule uniform.
