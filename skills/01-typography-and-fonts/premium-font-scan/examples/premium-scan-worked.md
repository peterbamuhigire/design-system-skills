# Worked example: scanning the premium folder before committing a face

A complete, copy-real application of `premium-font-scan` end to end: classify the artifact,
scan the matching `fonts/<category>/` folder, read its `MANIFEST.md`, decide premium-vs-baseline
with the licence basis stated, and record the resolved face for the embedding step. Built on
`doctrine/references/font-groups-and-usage.md`, `licensing-and-embedding.md`, and
`fonts/03-modern-product-grotesque/MANIFEST.md`.

---

## The brief

> **Sasula — SaaS pricing-page section.** Sasula is a subscription-billing product. The new
> pricing page must read as a confident, branded product surface. Output: web (HTML/CSS), so the
> body face is **embedded as `woff2`** and served from the site — never shipped as a downloadable
> file. Audience: startup/product. No client brand guideline mandates fonts.

Classify → **03 Modern Product / Grotesque** (`font-groups-and-usage.md`). The named OFL baseline
anchor for this group is **Bricolage Grotesque**.

---

## Step 1–2 — Locate and list what is actually present

Folder: `fonts/03-modern-product-grotesque/`. Premium binaries are gitignored, so I list what is on *this*
device rather than assuming:

```
$ ls fonts/03-modern-product-grotesque/
MANIFEST.md
Satoshi-Variable.woff2
Satoshi-Variable.ttf
```

Present this device: **Satoshi** (variable). Clash Display, Cabinet Grotesk, and General Sans are
named in the MANIFEST but their files are **absent** here — they are manual Fontshare downloads,
so they are not candidates for this scan.

---

## Step 3 — Read the MANIFEST for the present family

From `fonts/03-modern-product-grotesque/MANIFEST.md`, the row for Satoshi:

| Family | Licence | Embed? | Redistribute file? | Present? |
|---|---|---|---|---|
| Satoshi | **Fontshare** | **Yes** | **NO** | drop-in (present this device) |

So the licence facts for Satoshi are: **embedding into a built artifact is permitted; shipping or
committing the raw `.otf`/`.woff2` file is forbidden** (Fontshare rule, confirmed in
`licensing-and-embedding.md`). Bricolage Grotesque, by contrast, is OFL — embed *and* file both
allowed (kept out of the repo only by the scan-not-commit policy).

---

## Step 4–5 — Decide, with the licence basis stated

The artifact's need: a refined geometric/grotesque **body** face under the display headline, and
the format is web where the face is **embedded**, not file-shipped.

- **Does Satoshi fit better than the baseline?** Yes. For the body/UI layer of a startup product
  surface, Satoshi's even, contemporary geometric grotesque reads more branded and considered than
  defaulting the body to the display anchor. It is exactly the role `font-groups-and-usage.md`
  assigns it ("a refined geometric/grotesque body").
- **Does the MANIFEST grant the permission this format needs?** The format needs **embedding**, and
  the MANIFEST grants embedding = Yes. The forbidden action (file redistribution) is **not** what a
  served, embedded `woff2` does — the page renders the glyphs, it does not offer the file for
  download. So the permission needed is granted.
- **Premium chosen for body → Satoshi.** Baseline **Bricolage Grotesque (OFL)** stays as the
  display/headline anchor — it is the always-available face and the one safe to embed regardless.

Step 5 guard observed: the build pipeline **embeds** Satoshi as `woff2`; it must **not** commit the
Satoshi binary into the site repo or expose it as a downloadable asset. The gitignore on
`fonts/03-modern-product-grotesque/` already enforces this; the deploy step references the embedded face only.

> Counter-case for the record: had this been a **DOCX** deliverable that *bundles* the font file
> inside the document for an external client, that bundling is closer to file redistribution — in
> that case Satoshi would be dropped and the body would fall back to the OFL baseline (Bricolage
> Grotesque, or a 08 Body / UI Workhorse like Hanken Grotesk) and the report would say so. Here the
> web-embed format keeps Satoshi licit.

---

## Resolved faces (recorded for the embedding step)

| Role | Resolved face | Source | Licence basis |
|---|---|---|---|
| Display / headings | Bricolage Grotesque (800) | Baseline (OFL) | OFL — embed + ship both allowed |
| Body / UI | **Satoshi** (variable) | **Premium**, present this device | **Fontshare — embed YES, redistribute file NO**; web-embed only, never ship the file |

**Decision in one line:** Body resolves to **Satoshi (premium, Fontshare)** over the Bricolage
Grotesque baseline because it is present on this device, fits the body role better, and the format
(served web embed) needs only the embedding permission the MANIFEST grants — with the hard
constraint that the `woff2` is embedded, never redistributed as a file.
