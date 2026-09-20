# Reference: SSR and Hydration Safety (motion/react)

Source: ECC `motion-foundations` rules 2, 7, 8 — mechanics only, no token values (those stay owned
by `motion-design`).

## The rule

**`initial` must always match what the server renders.** If the server renders `opacity: 1`, the
component's `initial` prop must also declare `opacity: 1` — no exceptions. A mismatch produces a
hydration warning and, worse, a visible flash/jump as React reconciles.

## Wrong

```tsx
// Server renders opacity:1 (no JS). Client's initial says 0.
// Hydration mismatch: React repaints, layout jumps.
<motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} />
```

## Correct — defer the pre-entrance state to the client only

```tsx
"use client"
import { useState, useEffect } from "react"
import { motion } from "motion/react"

export function FadeInCard({ children }: { children: React.ReactNode }) {
  const [mounted, setMounted] = useState(false)
  useEffect(() => setMounted(true), [])

  return (
    <motion.div
      // Server + first client paint both render opacity:1 (mounted=false).
      // Only after mount does 'initial' become the pre-entrance state,
      // and because state is already 1 at that point, animate() has
      // nothing to reconcile against on the server — no mismatch.
      initial={{ opacity: mounted ? 0 : 1 }}
      animate={{ opacity: 1 }}
    >
      {children}
    </motion.div>
  )
}
```

This costs one extra render after mount but is the only way to have both a real entrance animation
and a server-rendered first paint with zero hydration warnings.

## Module-scope guards

Never read `window` or `navigator` at module level — it runs during SSR where neither exists:

```ts
// WRONG — throws during SSR (ReferenceError: navigator is not defined)
const isLowEnd = navigator.hardwareConcurrency <= 4

// CORRECT — guarded, safe to import anywhere
function isLowEnd() {
  return typeof navigator !== "undefined" && navigator.hardwareConcurrency <= 4
}
```

Same for `window.matchMedia` (used for `prefers-reduced-motion` detection outside the
`useReducedMotion()` hook) — always behind `typeof window !== "undefined"`.

## `"use client"` is required

Every file that imports from `motion/react` needs the `"use client"` directive at the top — it is
a client-only library. Omitting it in a Next.js App Router project fails the build or silently
produces a server component that cannot use the import.

## Motion values are SSR-safe on their own

`useMotionValue` and `useSpring` do not read the DOM or browser globals at creation time and do
not cause hydration errors by themselves — the hydration risk is specifically in mismatched
`initial`/`animate` render output, not in motion-value creation.
