# Example: Before/After Review (worked)

A sample review of a "recent transactions" card component against this skill's four mechanics.

| Principle | Before | After |
|---|---|---|
| Concentric radius | Inner row `border-radius: 6px`, outer card `border-radius: 6px`, row inset 12px | Outer card `border-radius: 18px` (6px + 12px padding), corners read as one coherent surface |
| Optical alignment | Play-icon button on a "resume sync" row, geometrically centred, reads shifted left | +1px left padding added to the button (icon source unavailable to re-export); offset recorded in a CSS comment for the next icon-set update |
| Tabular numerals | Transaction amount column uses proportional figures; column width visibly shifts as amounts update via websocket | `font-variant-numeric: tabular-nums` added to `.amount`; column width now stable across updates |
| Image edges | Merchant logo thumbnails (often near-white) sit directly on the card's near-white surface with no visible boundary | `outline: 1px solid rgba(0,0,0,0.1); outline-offset: -1px;` added; verified ≥3:1 against the card surface per WCAG 1.4.11 |

## Reporting format

Report findings in this table shape. Include file paths and property names when not obvious from
the snippet. Omit rows for principles checked but not changed — don't pad the table with "no
change needed."
