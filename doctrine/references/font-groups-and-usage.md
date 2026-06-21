# Reference: Font Groups, Where They Apply, and the Approved Baseline

Four groups. Each maps to a folder in `fonts/<group>/` (mirroring the user's `Downloads\Fonts`
taxonomy) and to a context. The faces listed are **OFL/Google-Fonts baselines** — always
available, safe to embed — unless noted. Before committing, scan the matching `fonts/<group>/`
folder for a purchased premium family and prefer it when it improves the result
(see `premium-font-scan`).

> Pairing always crosses a display/header face with a refined body face. A group tells you the
> *mood*; the pairing rules in `pairing-principles.md` tell you how to combine.

---

## Group 1 — Editorial / Authoritative

**Use for:** reports, proposals, business plans, BRD/SRS documents, whitepapers, any artifact
that must read as considered, credible, and institutional. The default group for the
document-generating engines (business-plan, srs, proposal, digital-research).

**Baseline faces (serif):** Fraunces · Crimson Pro · Newsreader · Source Serif 4 · Spectral

**Premium folder:** `fonts/1-Editorial-Authoritative/`
**Typical role:** distinctive serif for headings + a refined serif or quiet sans for body.

---

## Group 2 — Developer / Technical

**Use for:** dashboards, code-adjacent UI, API docs, technical documentation, admin panels,
anything where a precise, engineered feel is correct.

**Baseline faces:** IBM Plex family (Sans / Serif / Mono — pairs *within* one superfamily) ·
JetBrains Mono (display or code accents) · Fira Code (code blocks) · Space Mono (sparingly,
short labels only).

**Premium folder:** `fonts/2-Developer-Technical/`
**Typical role:** IBM Plex Sans for UI body, IBM Plex Mono / JetBrains Mono for code and data,
a Plex Serif accent for long-form. Never mix monospace with proportional in the same role.

---

## Group 3 — Startup / Product

**Use for:** landing pages, SaaS marketing, product launch sites, pitch decks — anywhere a
confident, contemporary, branded feel wins.

**Baseline faces:** Bricolage Grotesque (distinctive display, OFL) is the always-available
anchor. **Clash Display, Satoshi, Cabinet Grotesk, General Sans** are premium (Fontshare) —
free to *use/embed* but **not redistributable as files**, so they live in the premium folder,
not the repo.

**Premium folder:** `fonts/3-Startup-Product/`
**Typical role:** a strong display face (Clash Display / Bricolage Grotesque) for headlines +
a refined geometric/grotesque body (Satoshi / General Sans).

---

## Group 4 — Body Workhorses (NOT slop)

**Use for:** the body-text layer of any artifact, paired beneath a distinctive display face
from groups 1–3. These are quiet, legible, and deliberately chosen — never the headline.

**Baseline faces:** Public Sans · Hanken Grotesk · Source Sans 3 *(body only, paired — never
alone, never as the display face)* · Geist *(if licence permits)*.

**Premium folder:** `fonts/4-Body-Workhorses/`
**Typical role:** body, captions, UI labels — the calm layer under the expressive one.

---

## Quick chooser by artifact

| Artifact | Default group | Header → Body example |
|---|---|---|
| Business plan / proposal / SRS / report (DOCX/PDF) | 1 Editorial | Fraunces → Source Serif 4 (or → Public Sans) |
| Dashboard / admin UI / API docs | 2 Developer | IBM Plex Sans → IBM Plex Sans + Mono accents |
| SaaS landing / product marketing / pitch deck | 3 Startup | Clash Display (premium) or Bricolage → Satoshi / Hanken Grotesk |
| App / web UI body layer | 4 Workhorse under a display face | Bricolage Grotesque → Hanken Grotesk |
| Mobile app UI | 3 or 4 + platform constraints | see `skills/06-mobile-ui-ux/` |

Whatever you pick, **state it and say why** before producing the artifact.
