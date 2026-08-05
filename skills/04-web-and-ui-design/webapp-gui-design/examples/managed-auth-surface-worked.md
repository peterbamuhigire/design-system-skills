# Worked Example: Managed Authentication Surface

Parent skill: [`webapp-gui-design`](../SKILL.md). Canonical contract:
[`auth-and-tenant-visual-standard`](../references/auth-and-tenant-visual-standard.md).

## Brief

Build sign-in, forgot-password, reset-password, and pre-auth tenant selection for an accounting
SaaS. Super Admins also need to manage the imagery without deploying code.

The visual choice is Bricolage Grotesque for display and Hanken Grotesk for body/UI: the display
face makes the small brand moment authored, while the body face remains quiet around forms. The
palette uses a charcoal photographic veil, a warm ivory glass card, and one saturated brand
accent for focus and the primary action.

## Shared composition

`AuthSurface` selects one server-authorized active image at journey start and stores its opaque
asset identifier in journey/session state. It renders four sibling layers: image, enlarged blur,
veil, then content. `AuthCard` owns the glass treatment and an opaque fallback. Every auth route
uses those two primitives; no route owns a background URL or blur value.

Sign-in puts the light-surface logo inside the ivory card. Forgot-password places its logo above
the card, directly against the dark veil, so it always requests the dark-surface logo. A system
dark-mode preference does not change either choice because the immediate surfaces do not change.

## Admin manager

The page presents three fixed slots first: light-surface logo on a light preview, dark-surface
logo on a dark preview, and favicon at 16/32/64 px. The background library follows as ordered
preview tiles with status, dimensions, compressed size, activate/deactivate, move, replace, and
delete actions. When 20 images exist, upload is disabled with a direct explanation.

Dropping a JPEG starts optional client compression and exposes progress. The server remains the
authority. A successful response swaps in the canonical preview and reports `1920 x 1280,
184 KB WebP`. A rejected file remains absent and the current active pool is unchanged.

## State and evidence matrix

| State | Expected result |
|---|---|
| No custom assets | Bundled backgrounds and all three bundled brand fallbacks render |
| Validation failure | Form error appears; selected background and focus context remain stable |
| Blur unsupported | Opaque card keeps text/control contrast and hierarchy |
| 20 backgrounds | Upload disabled; reorder, activate, preview, and delete remain available |
| Keyboard reorder | Move controls update order and announce the new position |
| Narrow/short viewport | Card uses fluid width and page scrolls without clipping |
| Failed replacement | Existing active asset remains live and the failure is auditable |

Release evidence includes representative renders at 360, 768, 1280, and 1920 px; 200% zoom;
keyboard-only administration; reduced motion; and the opaque fallback. Missing assistive-
technology or browser-matrix evidence produces a `CONDITIONAL`, not `PASS`, verdict.
