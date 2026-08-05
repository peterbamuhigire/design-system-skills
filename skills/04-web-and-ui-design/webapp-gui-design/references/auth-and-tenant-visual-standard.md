# Authentication and Tenant-Entry Visual Standard

Parent skill: [`webapp-gui-design`](../SKILL.md).

Use this contract for sign-in, registration, forgot/reset password, 2FA, expired-session
recovery, invitation acceptance, and pre-auth tenant selection in Chwezi SaaS products. It
defines the visual behaviour; the engineering engine owns storage, authorization, and upload
implementation.

## Default art direction

- **Typeface pair:** Bricolage Grotesque for display and Hanken Grotesk for body/UI. The pair is
  OFL-compatible, distinctive at headline scale, and calm at form-control scale. Verify the
  actual font licence and delivery method before embedding.
- **Palette intent:** a dark neutral photographic veil creates focus and reliable contrast;
  a warm, near-opaque light card keeps form controls crisp. Brand colour is reserved for the
  primary action, focus, and small identity accents.
- **Character:** quiet confidence, not a decorative glass demo. Blur supports hierarchy; it is
  not the subject of the page.

Existing products may retain an established licensed type system during a scoped security or
maintenance change. New products and deliberate auth redesigns use the pair above unless a
documented brand system supplies a stronger approved pair.

## Layer contract

Implement one shared auth-surface primitive or stylesheet, consumed by every page in the
journey. Its layers, back to front, are:

1. A server-authorized image from the active background pool.
2. An enlarged copy or pseudo-layer with cover sizing, about 8-14 px blur, and slight scale so
   the viewport never reveals bright blur edges.
3. A dark neutral veil strong enough to make the darkest and lightest approved photographs safe.
4. The content region and a restrained glass card: translucent light fill, subtle border,
   modest shadow, and blur only where supported.

Provide an opaque card fallback with `@supports` or the platform equivalent. Keep controls and
body copy opaque. Do not apply opacity to a parent containing text.

Choose the background once at the beginning of an auth journey and keep it stable through
validation errors, password reset steps, and tenant selection. A refresh or new journey may
select another active image. Never let a client path select an unapproved file.

## Surface-aware brand assets

Name brand assets by the surface they are designed to sit on, not by operating-system theme:

| Immediate surface | Asset | Wrong-choice failure |
|---|---|---|
| Dark blurred image or dark veil | Dark-surface logo | A light-card logo can disappear or lose its intended colour balance |
| Light or warm-white card | Light-surface logo | A dark-surface reversal can lose contrast or look visually heavy |
| Browser tab, bookmark, or install prompt | Favicon/app mark | Reusing a wide logo becomes illegible at small sizes |

The dark-surface logo is the default for a mark placed outside the card. The light-surface logo
is permitted only when the mark is inside a verified light card. The operating-system theme
must not override this local-surface rule. Supply safe bundled fallbacks for all three slots.

## Responsive and accessibility contract

- Support 320 CSS px and wider, 200% zoom, safe-area insets, keyboard display, and vertical
  scrolling without clipped content.
- Keep the primary card within the viewport using a fluid inline width and a sensible maximum;
  avoid fixed widths and fixed vertical centring that clips short screens.
- Preserve visible labels, server-authoritative errors, focus order, focus return, and a
  44-by-44 CSS px minimum interactive target.
- Body text and controls meet WCAG contrast against the card; logo variants and any text outside
  the card meet contrast against every approved background after the veil.
- Decorative backgrounds have no announced alternative text. Meaningful brand marks have an
  accessible name where the surrounding link or heading does not already provide one.
- Respect reduced motion. Cross-fades are optional and must not be needed to understand state.

## Super Admin visual-asset manager

Every SaaS platform provides one clear, permission-protected management surface containing:

- a background library with preview, active/inactive state, order, replacement, and deletion;
- an exact platform limit of 20 stored backgrounds per scope, including inactive items;
- exactly one light-surface logo, one dark-surface logo, and one favicon slot;
- drag-and-drop plus a keyboard-accessible file picker, visible requirements, upload progress,
  success/failure status, and a cancel or retry path;
- side-by-side previews on representative dark and light surfaces;
- a safe default restoration path and clear confirmation for destructive deletion;
- post-compression dimensions and file size so an administrator can verify the result.

Reordering must have keyboard controls as well as drag interaction. The UI must explain that
client-side checks and compression improve speed but the server makes the final security and
acceptance decision. Changes are auditable and previewed before activation.

## Image preparation targets

- Backgrounds: do not upscale; fit inside a 1920 px long-edge envelope; prefer WebP at about
  quality 75; enforce 512 KB maximum after canonical server processing. Treat approximately
  200 KB as the performance target for a likely LCP image, not as a reason to damage imagery.
- Logos: preserve transparency, fit inside a 1200-by-400 px envelope, and use PNG or WebP as
  appropriate.
- Favicon: preserve transparency and small-scale legibility; use a square canonical output and
  provide the formats required by the target platform.
- Client Canvas/Squoosh compression is an optimization only. The engineering contract must still
  validate decoded content, constrain pixels, strip metadata, and re-encode on the server.

## Review evidence

Record representative renders for sign-in, forgot-password, reset, 2FA, tenant selection, and
the admin manager at 320/360, 768, 1280, and 1920 px. Include keyboard paths, 200% zoom, reduced
motion, opaque fallback, empty pool, 20-item limit, failed upload, replacement, and deletion.
A design verdict is `CONDITIONAL` when this matrix or assistive-technology checks remain
unexecuted; a desktop happy-path render alone is not a production-ready result.

## Anti-patterns

- Page-specific background CSS. Correction: consume the shared auth-surface primitive.
- Random image on every failed submit. Correction: persist the journey selection.
- Theme-swapping a logo that sits on a fixed dark veil. Correction: select by immediate surface.
- Blur or opacity on the form-content parent. Correction: separate background/card layers.
- Drag-only reordering. Correction: expose move-before/move-after or equivalent keyboard actions.
