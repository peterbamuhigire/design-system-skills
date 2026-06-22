# Trust-Signal Catalog (authentic, attributed, honest)

The working catalog for the trust/proof section: every signal class, the credibility hierarchy
(what to lead with), the authenticity rules, the thin-proof substitutes, and where each signal earns
its placement. Use it with `SKILL.md`'s workflow — name the doubt, pick the signal that answers it,
deploy it honestly.

> Why this is doctrine, not preference: `doctrine/design-doctrine.md` §0 — the moat is looking
> *authored and trustworthy by skilled human hands.* Proof works only when believed; fabricated or
> anonymous proof, once suspected, drives trust *below* having none. The authenticity rules below
> trace to the influence and direct-response literature applied *ethically* (Cialdini's principles —
> social proof, authority, liking, commitment — used with truth) and to consumer-protection guidance
> (FTC endorsement rules, EU). Never to an AI tool's recommendation (§2 asymmetry rule).

---

## 1. The signal classes

### A. Social proof — "others (like me) use and trust this"
| Signal | What it is | Honest use |
|---|---|---|
| **Attributed testimonial** | A real quote: name + role + company (+ face) + a concrete result | The strongest signal. Match the person to the visitor (role/sector/size). |
| **Customer logo strip** | Logos of *paying* customers | Only real customers; only logos you are licensed/permitted to show. |
| **Aggregate usage number** | "2,400 teams use this", "1.2M closes processed" | Precise, internally sourced, defensible. Not "millions". |
| **Third-party rating** | G2 / Capterra / Trustpilot score + review count | Show the *real* score and *real* count, linked to the source. |
| **Named case study** | A customer story with real numbers and outcome | The deepest proof for high-consideration buyers; name + metrics. |
| **Press / media mentions** | "As covered in …" | Only real coverage; link it. Don't imply endorsement that wasn't given. |

### B. Security & privacy cues — "my data is safe here"
| Signal | What it is | Honest use |
|---|---|---|
| **Compliance certifications** | SOC 2 Type II, ISO 27001, HIPAA, PCI-DSS | Only if *currently held*; link to the report request / certificate. |
| **Data-protection posture** | GDPR / regional data-residency, DPA available | State the true fact; link the policy / DPA. |
| **Encryption facts** | In transit (TLS) and at rest (AES-256) | Concrete and true; never vague "bank-level security" with nothing behind it. |
| **Data-control facts** | Export, deletion, retention, cancellation path | Reassures on lock-in; state the real path. |
| **Trust seals / security scanners** | Verified-secure / payment-provider marks | Only real, current seals that link to verification. |

### C. Authority & credentials — "the people behind this are competent"
| Signal | What it is | Honest use |
|---|---|---|
| **Founder/team credibility** | Real bios, relevant track record | Real names and verifiable history; strongest for new products. |
| **Professional certifications** | Domain credentials, accreditations | Only ones actually held; relevant to the buyer's risk. |
| **Awards / recognition** | Industry awards, "Leader" placements | Real, recent, and named — link the source. |
| **Endorsements / partnerships** | Named partner, integration, or expert | Real relationship; disclose if paid. |

### D. Risk reversal & transparency — "I can't lose by trying"
| Signal | What it is | Honest use |
|---|---|---|
| **Guarantee** | Money-back, satisfaction, SLA | Only if genuinely honoured; state the terms plainly. |
| **Free tier / trial** | Real free path, "no card required" | Only "no card" if literally true; no forced continuity. |
| **Transparent pricing & terms** | Visible price, renewal, cancellation | Showing them filters for the right buyer and builds trust. |
| **Transparent methodology** | "Here is exactly how it works" | Substitutes for proof when proof is thin (see §4). |

---

## 2. The credibility hierarchy — what to lead with

Order proof by persuasive weight *for this audience*, strongest first. Lead with the highest signal
you can field **honestly**; fall down the list to the strongest real one you have. Never promote a
fabricated signal up the list to fill a gap.

1. **Matched, attributed testimonial with a result** — someone *like the visitor*, named, with a
   concrete outcome and a face. The single strongest signal.
2. **A real, precise aggregate number** — "average close time fell 9.1 → 2.4 days", "2,400 teams".
3. **Genuine customer logos + a real third-party rating** (with the real count linked).
4. **Security/privacy cues** — when data-safety is the doubt, these *lead* (regulated/health/fintech).
5. **Founder/team credibility, named case studies, press, awards, certifications** — supporting,
   unless the audience buys on authority (regulated sectors, high-consideration B2B), where they rise.

**Match beats fame.** A controller at an SMB trusts another SMB controller over a Fortune-500 CFO.
**One strong real signal beats five weak ones** — and beats any number of fabricated ones.

---

## 3. Authenticity rules (the non-negotiables)

1. **Attribution is mandatory.** Name + role + company (+ face with consent). "★★★★★ — A happy
   customer" reads as invented and lowers trust *below* no testimonial.
2. **Never fabricate** a testimonial, rating, logo, review count, or metric. A non-customer's logo is
   dishonest and legally exposed (false endorsement / passing-off).
3. **Real numbers, stated precisely**, internally sourced and defensible. You must be able to produce
   the source. "Reduced tickets 34%" > "dramatically reduced tickets".
4. **Match the proof to the visitor** — same role, sector, size out-converts a famous-but-irrelevant
   name.
5. **Show, don't just claim** — a real screenshot, a named case study with numbers, a linked rating
   beats an adjective.
6. **Disclose relationships** — paid endorsements, affiliate links, sponsored placements (FTC and
   equivalents). Plain disclosure *increases* credibility.
7. **Security cues must be true, current, and link to evidence** — a badge that links nowhere is
   decoration; a badge for an unheld certification is fraud.

**The test for any signal:** *"If a journalist or a skeptical buyer checked this, does it hold?"* If
not, it is out. One challenged claim poisons every other claim on the page.

---

## 4. When proof is genuinely thin

A new product has no testimonials yet. Honest moves only:

- **Founder/team credibility** — real bio, real track record, real faces.
- **Transparent methodology** — "here is exactly how it works", shown not asserted.
- **A strong, real guarantee** or a genuine free tier — honest risk reversal substitutes for proof
  you don't yet have.
- **Real early-stage framing** *if true* — "join the first 100", "early access" — honest and often
  attractive.
- **Pilot / design-partner results**, even small and named, with permission.

**Never** invent a testimonial, borrow a logo, or post a fake review count. The honest thin-proof
section out-converts the padded one that gets caught — and the catch is catastrophic.

---

## 5. Placement — put the signal where the doubt arises

- **Hero credibility anchor:** one strong token above the fold (a rating, a real logo strip, one
  usage number) — enough to earn the scroll, not the whole proof block.
- **Dedicated proof section:** the matched testimonials + case numbers, after value/mechanism, before
  objections (the landing spine, per `landing-page-and-conversion-design`).
- **Security/privacy cues:** *at the point of fear* — beside the signup form, the payment step, the
  data-import CTA — not buried in the footer if data-safety is the conversion blocker.
- **Near the CTA:** a guarantee / "no card required" / a single trust seal where the visitor commits.
- **Objection adjacency:** the case study or guarantee sits next to the objection it answers.

Do not **badge-spray** — a wall of every certification and award answers no specific doubt and reads
as insecure over-justification.

---

## 6. Accessibility & performance (proof is content)

- **Ratings are not colour-only** — pair stars with the numeric value and a text label
  (`doctrine/references/wcag-2.2-criteria.md`, SC 1.4.1; `interaction-anti-patterns.md` D3).
- **Faces have correct `alt`** — descriptive when the image carries the identity, `alt=""` when the
  name is already in adjacent text.
- **Badges meet 3:1** UI-component contrast; **verified-review links** are real focusable controls
  with a visible focus ring.
- **Never hover-lock proof** (`interaction-anti-patterns.md` E3) — a testimonial revealed only on
  hover doesn't exist on touch.
- **Hierarchy:** the *result* in the quote is the focal element, not the avatar
  (`interaction-anti-patterns.md` D1).
- **Performance** (`doctrine/references/web-performance-budgets-2026.md`): logos and headshots are
  sized, compressed AVIF/WebP with width/height set (CLS-reserved); lazy-load below-the-fold proof;
  avoid a heavy third-party review widget that tanks INP.

---

## Sources / authority

Social-proof, authority, liking, and commitment levers trace to Cialdini's influence principles
applied *ethically*, and to conversion-research practice. The authenticity and disclosure rules trace
to consumer-protection guidance (FTC endorsement guides, EU) and the deceptive-design research
community. Human authority and the design/ethics literature only — never an AI tool's recommendation
(`doctrine/design-doctrine.md` §2 asymmetry rule). Posture: persuade with truth, attribute every
claim, refuse fabrication, and prefer the proof section that looks — and is — authored and
trustworthy.
