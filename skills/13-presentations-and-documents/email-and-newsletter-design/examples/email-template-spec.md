# Worked Example — Responsive HTML Email Template Spec (transactional + newsletter)

A bulletproof, dark-mode-aware responsive email spec. Email's constrained model means the
**fallback IS the design** (many clients strip webfonts) — see `references/email-bulletproof-patterns.md`.

## Brief
"Sente" payments — a receipt + monthly statement newsletter. Must render in Outlook (Windows,
Word engine), Apple Mail, Gmail (web/app), and dark mode; image-off resilient.

## Structure (single-column, table-based, ≤ 600px)
```
[Preheader: hidden, ~90 chars: "Your June statement — UGX 1,240,000 received"]
┌─ Wrapper table (bg, 100%) ───────────────────────────────┐
│  ┌─ Container table (600px, centered) ─────────────────┐ │
│  │  Header: logo (PNG, alt="Sente"), 24px padding      │ │
│  │  Hero: "June statement" H1 + amount (text, not img) │ │
│  │  Body rows: line items (nested tables, not divs)    │ │
│  │  Bulletproof CTA button (see below)                 │ │
│  │  Footer: address, unsubscribe (real), preferences   │ │
│  └─────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────┘
```

## Type & fallback (the design lives in the fallback)
- Chosen face: **Hanken Grotesk** via `@font-face` for clients that honour it (Apple Mail, some
  Gmail) — an approved workhorse, **not** a banned font.
- **Authoritative fallback stack** (what most recipients actually see):
  `font-family: 'Hanken Grotesk', -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;`
  The design is judged on this stack, not the webfont. Amounts use a tabular treatment.
- All type via inline CSS on `<td>` (not `<p>` margins — Outlook ignores them); sizes in px.

## Bulletproof button (works in Outlook Word engine)
```html
<table role="presentation" cellpadding="0" cellspacing="0"><tr>
  <td bgcolor="#0F4C4A" style="border-radius:8px;">
    <a href="{statement_url}" style="display:inline-block;padding:14px 28px;
       font:600 16px/1 'Hanken Grotesk',Arial,sans-serif;color:#ffffff;text-decoration:none;">
      View full statement</a>
  </td></tr></table>
```
(VML fallback added for Outlook rounded corners.)

## Dark mode
- `<meta name="color-scheme" content="light dark">` + `@media (prefers-color-scheme: dark)`.
- Light bg `#FFFFFF`→ dark `#16181D`; ink `#1A1C1E`→ `#ECEEF1`; **don't rely on Outlook honouring
  it** — choose brand colours that survive forced-dark inversion (avoid pure white logos on
  transparent; use a PNG with a safe matte). Re-check contrast in both modes (WCAG 4.5:1).

## Image-off & accessibility
- Every image has real `alt`; the email reads completely with images blocked (the amount + CTA
  are live text, never baked into a hero image). Semantic heading order; `role="presentation"` on
  layout tables; `lang` set; min 14px body; 44px tap target on the CTA.

## Responsive
- Fluid/hybrid: 600px container with `max-width:100%`; `@media (max-width:600px)` stacks padding
  and goes full-width; ghost-table wrapper for Outlook. No horizontal scroll on a 320px phone.

## Pre-send checklist
Litmus/Email-on-Acid across the 4 clients + dark mode + image-off; real unsubscribe; preheader
set; all-text amount; alt on all images; contrast re-checked dark. 

*Illustrative values — copy the patterns, not the numbers.*
