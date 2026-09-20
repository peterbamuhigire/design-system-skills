# Example: Drag-to-Dismiss Sheet (worked)

An end-to-end component combining this skill's API surface: `useMotionValue` +
`useTransform` for the drag-linked backdrop fade, offset+velocity gesture threshold,
`AnimatePresence` for mount/unmount, a mount-guarded SSR-safe entrance, and a shimmer
loading state that pauses off-screen. Durations/springs are imported, not inlined,
per `motion-design`'s token contract — substitute your project's actual token module.

```tsx
"use client"
import { useState, useEffect } from "react"
import { motion, AnimatePresence, useMotionValue, useTransform, useReducedMotion } from "motion/react"
// Import from the project's motion-design-derived token module — do not inline values.
import { motionTokens, springs } from "@/lib/motion-tokens"

export function DismissibleSheet({
  isOpen,
  onClose,
  loading,
  children,
}: {
  isOpen: boolean
  onClose: () => void
  loading: boolean
  children: React.ReactNode
}) {
  // --- SSR-safe entrance guard (references/ssr-and-hydration.md) ---
  const [mounted, setMounted] = useState(false)
  useEffect(() => setMounted(true), [])

  // --- reduced-motion contract owned by motion-design, wired here ---
  const reduce = useReducedMotion()
  const enterY = reduce ? 0 : motionTokens.distance.xl

  // --- drag-linked backdrop fade via motion values (no re-render per frame) ---
  const y = useMotionValue(0)
  const opacity = useTransform(y, [0, 200], [1, 0])

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            key="backdrop"
            className="fixed inset-0 bg-black/40"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
          />
          <motion.div
            key="sheet"
            className="fixed bottom-0 inset-x-0 rounded-t-2xl bg-white p-6"
            drag="y"
            dragConstraints={{ top: 0 }}
            style={{ y, opacity }}
            onDragEnd={(_, info) => {
              // Rule: check offset AND velocity, never velocity alone.
              if (info.offset.y > 120 || info.velocity.y > 500) onClose()
            }}
            initial={{ opacity: mounted ? 0 : 1, y: mounted ? enterY : 0 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: enterY }}
            transition={springs.gentle}
          >
            {loading ? <ShimmerSkeleton /> : children}
          </motion.div>
        </>
      )}
    </AnimatePresence>
  )
}
```

## What this demonstrates

- `initial`/`animate`/`exit` never diverge from the server-rendered state before mount — see the
  `mounted ?` ternaries (`references/ssr-and-hydration.md`).
- `onDragEnd` checks both `info.offset.y` and `info.velocity.y` (`references/api-decision-tree.md`,
  gesture threshold rule) — neither is trusted alone.
- `useReducedMotion()` collapses the entrance distance to `0` rather than removing the transition
  outright, matching `motion-design`'s reduced-motion contract (replace vestibular triggers with
  non-spatial equivalents, don't strip all feedback).
- Duration/spring values (`motionTokens`, `springs`) are imported from the project's token module,
  never inlined — this skill implements `motion-design`'s decisions, it does not invent new ones.
