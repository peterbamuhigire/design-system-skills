---
title: Dark Mode Implementation Guide
description: Complete guide for implementing stunning dark mode support across all sector templates using Tailwind CSS v4
---

# Dark Mode Implementation Guide

Enable beautiful dark mode for all sector websites with seamless light/dark switching, auto-detection, and persistent user preferences.

## Quick Setup

### 1. Update tailwind.config.js

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Enable class-based dark mode
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        // Light mode colors
        light: {
          bg: '#ffffff',
          surface: '#f5f5f4',
          text: '#1c1917',
          border: '#e7e5e4',
        },
        // Dark mode colors
        dark: {
          bg: '#1c1917',
          surface: '#292524',
          text: '#fafaf9',
          border: '#44403c',
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

### 2. Create Dark Mode Toggle Component

```astro
---
// src/components/accessibility/DarkModeToggle.astro
---

<div
  x-data="darkModeToggle()"
  x-init="init()"
  class="fixed bottom-4 right-20 z-40"
>
  <button
    @click="toggle()"
    @keydown.escape="close()"
    :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
    class="p-3 rounded-full bg-neutral-200 dark:bg-neutral-700 text-neutral-800 dark:text-neutral-100 shadow-lg hover:shadow-xl transition transform hover:scale-110"
  >
    <!-- Sun Icon (shown in dark mode) -->
    <svg
      x-show="isDark"
      class="w-5 h-5"
      fill="currentColor"
      viewBox="0 0 24 24"
    >
      <path d="M12 3v1m0 16v1m9-9h-1m-16 0H1m15.364 1.636l.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.343l-.707-.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
    </svg>

    <!-- Moon Icon (shown in light mode) -->
    <svg
      x-show="!isDark"
      class="w-5 h-5"
      fill="currentColor"
      viewBox="0 0 24 24"
    >
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
    </svg>
  </button>
</div>

<script>
  function darkModeToggle() {
    return {
      isDark: false,

      init() {
        // Check user's saved preference
        const saved = localStorage.getItem('theme');

        if (saved) {
          this.isDark = saved === 'dark';
        } else {
          // Check system preference
          this.isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        }

        this.applyTheme();

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
          if (!localStorage.getItem('theme')) {
            this.isDark = e.matches;
            this.applyTheme();
          }
        });
      },

      toggle() {
        this.isDark = !this.isDark;
        this.applyTheme();
        localStorage.setItem('theme', this.isDark ? 'dark' : 'light');
      },

      applyTheme() {
        const html = document.documentElement;
        if (this.isDark) {
          html.classList.add('dark');
        } else {
          html.classList.remove('dark');
        }
      }
    }
  }
</script>
```

### 3. Update Base Layout

```astro
---
// src/layouts/BaseLayout.astro
import '@fontsource/inter/400.css';
import '@fontsource/inter/600.css';
import '@fontsource/inter/700.css';
import DarkModeToggle from '../components/accessibility/DarkModeToggle.astro';
import Navigation from '../components/navigation/MainNav.astro';
import Footer from '../components/shared/Footer.astro';

export interface Props {
  title: string;
  description?: string;
}

const { title, description = 'Modern website' } = Astro.props;
---

<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content={description} />

  <!-- Prevent flash of wrong theme -->
  <script>
    const theme = localStorage.getItem('theme') ||
                  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    }
  </script>
</head>
<body class="bg-white dark:bg-neutral-900 text-neutral-900 dark:text-neutral-50 transition-colors duration-300">
  <DarkModeToggle />
  <Navigation />

  <main>
    <slot />
  </main>

  <Footer />

  <script>
    import Alpine from 'alpinejs';
    window.Alpine = Alpine;
    Alpine.start();
  </script>
</body>
</html>
```

## Dark Mode Best Practices

### 1. Color Mapping Strategy

```css
/* Use dark: prefix for all dark mode colors */
.button {
  @apply bg-primary-600 text-white
         dark:bg-primary-500 dark:text-neutral-100
         hover:bg-primary-700 dark:hover:bg-primary-400
         transition;
}

.card {
  @apply bg-white dark:bg-neutral-800
         border border-neutral-200 dark:border-neutral-700
         shadow-sm dark:shadow-lg;
}

.text-secondary {
  @apply text-neutral-600 dark:text-neutral-300;
}
```

### 2. Image Handling in Dark Mode

```astro
---
// Show different images for light/dark mode
import lightImage from '../images/illustration-light.png';
import darkImage from '../images/illustration-dark.png';
---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset={darkImage.src} />
  <img src={lightImage.src} alt="Illustration" />
</picture>
```

### 3. Form Styling in Dark Mode

```astro
---
// src/components/forms/DarkModeInput.astro
---

<input
  type="text"
  class="px-4 py-2 rounded-lg
         bg-white dark:bg-neutral-800
         border border-neutral-300 dark:border-neutral-600
         text-neutral-900 dark:text-neutral-100
         placeholder-neutral-500 dark:placeholder-neutral-400
         focus:ring-2 focus:ring-primary-500 dark:focus:ring-primary-400
         focus:border-transparent
         transition"
/>
```

## Testing Dark Mode

```bash
# Test with system preference
# macOS: System Preferences → General → Appearance → Dark
# Windows 11: Settings → Personalization → Colors → Dark

# Test in browser DevTools
# Chrome: F12 → Rendering → Emulate CSS media feature prefers-color-scheme
# Firefox: about:config → ui.systemUsesDarkTheme = 1
```

## Accessibility Considerations

✅ **Sufficient contrast** in both modes (WCAG AA 4.5:1)
✅ **Avoid pure black/white** (#000000 / #ffffff) - use neutral tones
✅ **Respect prefers-color-scheme** for users with motion sensitivity
✅ **Test with color blindness simulators** in both modes
✅ **Provide manual toggle** for users who prefer light in dark environment (or vice versa)

## Common Dark Mode Colors by Sector

### Education
- Light: `bg-white`, `text-neutral-900`
- Dark: `bg-neutral-900`, `text-neutral-50`
- Accent remains `primary-600` (both modes)

### Nonprofit/Charity
- Light: `bg-white`, `text-neutral-800`
- Dark: `bg-neutral-800`, `text-neutral-100`
- Impact accent: `impact-500` (both modes, sufficient contrast)

### Healthcare
- Light: `bg-white`, `text-neutral-900`
- Dark: `bg-neutral-900`, `text-neutral-100`
- Trust color: `primary-500` (both modes)

### E-commerce
- Light: `bg-white`, `text-neutral-900`
- Dark: `bg-neutral-900`, `text-neutral-100`
- CTA: `primary-600` (light), `primary-400` (dark - lighter for accessibility)

## Sample Dark Mode Component

```astro
---
// Complete component with dark mode support
---

<div class="space-y-6">
  <!-- Hero -->
  <section class="bg-white dark:bg-neutral-800 py-12 px-6 rounded-xl">
    <h1 class="text-3xl md:text-4xl font-bold text-neutral-900 dark:text-white mb-4">
      Welcome to Our Site
    </h1>
    <p class="text-lg text-neutral-600 dark:text-neutral-300 mb-6">
      This looks great in both light and dark modes.
    </p>
    <button class="bg-primary-600 hover:bg-primary-700 dark:bg-primary-500 dark:hover:bg-primary-400 text-white font-semibold py-2 px-6 rounded-lg transition">
      Get Started
    </button>
  </section>

  <!-- Card Grid -->
  <div class="grid md:grid-cols-3 gap-4">
    {[1, 2, 3].map((i) => (
      <div class="bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-lg p-6 hover:shadow-lg dark:hover:shadow-lg transition">
        <h3 class="text-lg font-semibold text-neutral-900 dark:text-white mb-2">
          Feature {i}
        </h3>
        <p class="text-neutral-600 dark:text-neutral-400">
          Description of feature {i}.
        </p>
      </div>
    ))}
  </div>

  <!-- Call to Action -->
  <div class="bg-gradient-to-r from-primary-600 to-primary-700 dark:from-primary-700 dark:to-primary-600 text-white rounded-xl p-8 text-center">
    <h2 class="text-2xl font-bold mb-4">Ready to join?</h2>
    <button class="bg-white dark:bg-neutral-100 text-primary-600 font-semibold py-2 px-8 rounded-lg hover:bg-neutral-100 dark:hover:bg-white transition">
      Sign Up Now
    </button>
  </div>
</div>
```

## Tailwind v4 Dark Mode Media Query

```javascript
// If using system-preference mode instead of class mode:
export default {
  darkMode: 'media', // Uses prefers-color-scheme media query
  // ... rest of config
}
```

---

**Note**: Apply dark mode support to all sector templates by prefixing color utilities with `dark:` when needed. This ensures a cohesive experience across all websites.
