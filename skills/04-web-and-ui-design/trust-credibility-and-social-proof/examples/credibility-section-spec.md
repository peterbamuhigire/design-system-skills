# Worked example — credibility / proof section spec: "Rafiki Records"

A real, signal-by-signal proof-section spec for a sample product. Not a template — an authored proof
block with a *named doubt*, the credibility hierarchy applied to *this* audience, real attributed
testimonials, honest security/privacy cues placed at the point of fear, a thin-proof fallback noted,
and the WCAG/perf constraints applied. Use this as the *shape* of the spec this skill produces.

---

## Product & brief

- **Product:** **Rafiki Records** — a patient-records (EHR) SaaS for small private clinics
  (1–8 clinicians) in East Africa.
- **Where this section lives:** the social-proof + security band of the marketing page, after the
  value prop and mechanism, before objection handling. (The whole page is owned by
  `landing-page-and-conversion-design`; this spec is *only* the proof section.)
- **Audience:** a clinic owner-clinician evaluating whether to move patient data off paper/Excel.
- **The named doubt (decided first):** the dominant blocker is **"is my patients' data safe and
  legal with you?"** — closely followed by **"will a clinic like mine actually manage this?"** So the
  credibility hierarchy for *this* audience promotes **security/privacy cues** and **matched
  small-clinic testimonials** above generic usage numbers.
- **Real proof inventory (cleared for use):** 3 named clinician testimonials (consented, with faces);
  a logo/name row of 9 real clinic customers; an internal metric (avg chart-retrieval time: paper
  ~4 min → ~8 sec); ISO 27001 certification (held, current); a signed DPA and Uganda/Kenya
  data-residency hosting; AES-256 at rest + TLS 1.3 in transit; a real 4.6/5 across 38 reviews on a
  regional software directory.

### Distinctive decision (stated before markup, per `distinctive-by-design`)
> "The proof band's distinctive idea is a **clinical-record motif**: each testimonial is set like a
> short, dated **chart note** — a thin left rule, a monospaced date/initials stamp, the clinician's
> result pulled large in the brand serif — *not* three identical round-avatar cards. It signals
> 'records, handled with care' to clinicians who live in chart notes. Explicitly NOT the convergent
> 'Loved by teams everywhere' centred grey logo strip."

---

## Credibility hierarchy applied (this audience: data-safety first)

| Rank | Signal | Why here for *this* visitor |
|---|---|---|
| 1 | **Security/privacy cues** (ISO 27001, DPA, data residency, encryption) | The #1 doubt is data safety/legality — this leads, against the usual default. |
| 2 | **Matched testimonial** — a small-clinic owner like the visitor, with a result | Answers "will a clinic *like mine* manage this?" |
| 3 | **Real clinic logo/name row + the 4.6/38 rating** | Breadth of real, similar customers. |
| 4 | **Aggregate metric** (4 min → 8 sec retrieval) | Concrete outcome, defensible. |

---

## Signal 1 — Security & privacy band  *(answers: "is my patients' data safe and legal?")*

- **Placement:** immediately adjacent to the "Start free 30-day trial" CTA and the data-import step —
  *at the point of fear*, not in the footer.
- **Real content (every item true, current, and linked to evidence):**
  - **ISO 27001 certified** — badge links to the certificate (not a static image).
  - **Signed DPA + data residency** — "Your data stays in-region (Nairobi / Kampala data centres)."
    Links to the DPA and the hosting/sub-processor list.
  - **Encryption** — "Encrypted in transit (TLS 1.3) and at rest (AES-256)." Concrete, not "bank-level
    security."
  - **Your data, your control** — "Export or delete all records at any time; cancel in one click."
    (Answers lock-in fear; honest — no roach-motel.)
- **Honesty note:** no certification shown that isn't held; every badge links to evidence. No vague
  seal-as-decoration.
- **Accessibility:** badges meet 3:1 contrast; each evidence link is a real focusable `<a>` with a
  visible focus ring; "encrypted" status is text, not a colour-only lock icon.

## Signal 2 — Matched testimonial (lead quote)  *(answers: "will a clinic like mine manage this?")*

- **Placement:** the focal element of the proof band; the *result* set large, the attribution small.
- **Real, attributed content (consented):**
  > *"We were terrified of moving 12 years of paper charts. The migration took a weekend, and now I
  > pull a patient's full history in seconds during the consult instead of sending the nurse to the
  > shelf."*
  > — **Dr. Grace Mwangi, Owner & GP, Tumaini Family Clinic, Nairobi (3 clinicians).**  *(real
  > name + role + clinic + size + consented face)*
- **Hierarchy (per `interaction-anti-patterns.md` D1):** the pulled result ("history in seconds…") is
  the largest text; the round headshot is small — the *outcome* is the focal point, not the avatar.
- **Accessibility:** the face has descriptive `alt` ("Dr. Grace Mwangi"); the quote is real text, not
  an image of text; nothing hover-locked.

## Signal 3 — Real clinic row + third-party rating  *(answers: "do others like me trust this?")*

- **Real content:** a row of **9 named real clinic customers** (name + town, not just a grey logo),
  label "Trusted by small clinics across Kenya & Uganda"; and **4.6 / 5 across 38 reviews** on
  [the regional directory](#) — the real score and real count, linked to the source.
- **Honesty note:** every clinic listed is a paying customer; the rating and count are the *actual*
  ones, linked. No "trusted by thousands."
- **Accessibility:** the 4.6 rating shows the **numeric value + a text label** beside the stars (not
  colour/stars only, SC 1.4.1); logos are sized AVIF with `alt` = clinic name.

## Signal 4 — Aggregate metric  *(answers: "what changes, concretely?")*

- **Real content:** **"Average chart retrieval: ~4 minutes on paper → ~8 seconds in Rafiki."**
  Internal, defensible, stated precisely. One number, not a wall of vanity stats.

---

## Thin-proof note (recorded for the team)

If, at launch, the testimonials/rating weren't yet available, the honest fallback (per
`trust-signal-catalog.md` §4) would lead with: the founders' real clinical+security track record, the
ISO 27001 cert and DPA as the trust anchor, a strong "30-day, no-card, export-and-delete-anytime"
guarantee, and honest "design-partner clinics" framing — **never** a borrowed clinic logo or an
invented testimonial to fill the gap.

---

## Performance treatment

- 9 clinic logos + 3 headshots: sized, compressed **AVIF**, width/height set to **reserve space
  (CLS = 0)**; the below-the-fold proof band is **lazy-loaded**.
- The third-party rating is shown as **our own rendered number linking out** — *not* an embedded
  review widget that would tank INP.

---

## Authenticity & trust checklist — applied

| # | Item | Result |
|---|---|---|
| 1 | Doubt named; signals answer it | Pass — data-safety lead, then matched clinic proof |
| 2 | Hierarchy leads with strongest real signal | Pass — security cues lead for this audience; nothing fabricated promoted |
| 3 | Every testimonial attributed (name/role/company/face) | Pass — Dr. Mwangi et al., consented faces |
| 4 | Zero fabrication (quotes/logos/counts/metrics) | Pass — real customers, real 38-review count, real metric |
| 5 | Numbers precise & internally defensible | Pass — 4 min → 8 sec; 4.6/38 sourced |
| 6 | Security cues true, current, evidence-linked, placed at fear | Pass — ISO/ DPA/ residency/ encryption beside the form |
| 7 | Paid/affiliate relationships disclosed | Pass — none here; none implied |
| 8 | No fake scarcity/urgency | Pass — none present (defers to ethics skill) |
| 9 | Accessibility (rating not colour-only, alt, focus, badge 3:1, no hover-lock) | Pass |
| 10 | Performance (sized/CLS-reserved; no INP-tanking widget) | Pass |
| 11 | No convergent default | Pass — chart-note motif, named clinics, result-led quote, no grey 3-card row |

**Verdict:** ships. Authored (chart-note motif), honest (every signal real and attributed, security
cues evidence-linked), accessible and fast — trust earned by truth, per
`doctrine/design-doctrine.md` §0.

> Type named here (a brand serif for pull-quotes, a monospace date stamp) is illustrative of the
> *clinical-record* intent; on a real build, run `01-typography-and-fonts/font-selection-and-pairing`
> and scan `fonts/` for a licensed premium family before committing. No banned default (no Inter, no
> indigo gradient).
