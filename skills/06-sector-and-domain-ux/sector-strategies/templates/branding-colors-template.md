---
title: Brand Colors & Branding Assets
project: {Your School/Company Name}
sector: education
generated_date: 2026-02-17
---

# Brand Colors & Branding Assets

Copy this file to `docs/branding-colors.md` in your client project and fill in your actual brand colors. Both photo-manager and design-system will reference this file.

## Logo

**Primary Logo Location**: `src/assets/images/logo.png`

- **Dimensions**: Auto-detected by photo-manager from photo-bank/ (all PNG files with "logo" in filename scanned)
- **Selected File**: logo-color.png
- **Width**: 600px
- **Height**: 150px
- **Aspect Ratio**: 4:1 (landscape, suitable for header)
- **Format**: PNG with transparency (RGBA)
- **File Size**: 85 KB
- **Usage**: Homepage header, footer, meta OG image, email templates

**Alternative Logos**:
- **Favicon Version**: logo-square.png (1:1 aspect ratio, min 192x192px)
- **Monochrome Version**: logo-mono.png (for restricted backgrounds)

---

## Primary Color Palette

These colors form the foundation of your brand identity. Define them as hex codes below.

### Primary Brand Color

**Hex Code**: #C97655
**RGB**: rgb(201, 118, 85)
**HSL**: hsl(16, 55%, 56%)
**Name**: Terracotta / Warm Brown
**Usage**:
- Main headers (H1, H2)
- Primary CTA buttons
- Brand identity accent
- Active navigation links

**Tailwind Class**: `text-primary-600` / `bg-primary-600`

### Secondary Color

**Hex Code**: #2D5A4F
**RGB**: rgb(45, 90, 79)
**HSL**: hsl(164, 33%, 27%)
**Name**: Forest Green / Deep Teal
**Usage**:
- Secondary CTAs
- Trust signals (security badges, success states)
- Hover states
- Accent underlines

**Tailwind Class**: `text-secondary-600` / `bg-secondary-600`

### Accent Color

**Hex Code**: #E8B84A
**RGB**: rgb(232, 184, 74)
**HSL**: hsl(42, 77%, 60%)
**Name**: Sunset Gold / Warm Accent
**Usage**:
- Highlights, badges, achievement icons
- Interactive hover states
- Badges and labels
- Call-out boxes

**Tailwind Class**: `text-accent-600` / `bg-accent-600`

---

## Neutral Palette

These colors provide contrast and readability support.

### Background Color

**Hex Code**: #FAF7F1
**RGB**: rgb(250, 247, 241)
**HSL**: hsl(30, 100%, 96%)
**Name**: Cream / Off-white
**Usage**:
- Page backgrounds
- Card backgrounds
- Section alternation
- Form input backgrounds

### Text Color (Primary)

**Hex Code**: #2C2C2C
**RGB**: rgb(44, 44, 44)
**HSL**: hsl(0, 0%, 17%)
**Name**: Charcoal
**Usage**:
- Primary body text
- All headers
- High-contrast text on light backgrounds
- Links

### Text Color (Secondary)

**Hex Code**: #8B8680
**RGB**: rgb(139, 134, 128)
**HSL**: hsl(24, 4%, 52%)
**Name**: Stone Gray
**Usage**:
- Secondary descriptions
- Muted content
- Placeholder text
- Disabled states
- Metadata (dates, authors)

---

## Color Usage Rules

### Accessibility

**Minimum Contrast Ratios** (WCAG AA):
- Primary text on light background: 4.5:1 minimum
- Large text: 3:1 minimum
- Interactive elements: 3:1 minimum

**Test**: Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to verify.

### Buttons & CTAs

- **Primary CTA**: White text on Primary Color (#C97655)
- **Secondary CTA**: Primary Color text on white background with border
- **Hover State**: Darken color by 10% (reduce lightness)
- **Disabled State**: 50% opacity gray
- **Focus State**: Add 2-3px outline in Primary Color

### Forms

- **Input Border**: Secondary text color (#8B8680)
- **Input Background**: Cream (#FAF7F1)
- **Focus Border**: Primary Color (#C97655), 2px solid
- **Focus Ring**: Primary Color with 10% opacity, 4px
- **Error State**: Red (#DC2626)
- **Success State**: Secondary Color (#2D5A4F)

### Links

- **Link Color**: Primary Color (#C97655)
- **Visited**: Darken by 20%
- **Hover**: Underline + 10% darker
- **Focus**: Same as other interactive elements

---

## Tailwind Configuration Integration

Update `tailwind.config.js` with these colors:

```javascript
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0fdf4',   // Lightest
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',  // Main
          600: '#16a34a',  // Used most
          700: '#15803d',
          800: '#166534',
          900: '#14532d',  // Darkest
        },
        secondary: {
          50: '#f8fafc',
          100: '#f1f5f9',
          200: '#e2e8f0',
          300: '#cbd5e1',
          400: '#94a3b8',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          800: '#1e293b',
          900: '#0f172a',
        },
        accent: {
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#d97706',
        }
      }
    }
  }
}
```

---

## Color Variations (Tints & Shades)

Use these when you need lighter or darker versions for hover states, disabled states, etc.

### Primary Tints (Lighter)
- 10% lighter: #DBA876
- 20% lighter: #E6BC98
- 30% lighter: #F1D0B9

### Primary Shades (Darker)
- 10% darker: #B16545
- 20% darker: #975335
- 30% darker: #7D4125

---

## Color Psychology Notes

**Why These Colors for Education**:
- **Terracotta (Primary)**: Warmth, trust, approachability
- **Forest Green (Secondary)**: Growth, learning, stability
- **Sunset Gold (Accent)**: Achievement, celebration, energy
- **Cream Background**: Calm, welcoming, professional

These colors work well on all skin tones and are accessible for color-blind users when used with sufficient contrast.

---

## Brand Color Usage Examples

### Hero Section
```
Background: Primary Color (#C97655)
Text: White
CTA Button: White background, Primary text
```

### Card Headers
```
Background: Accent Color (#E8B84A)
Text: Charcoal (#2C2C2C)
```

### Success Message
```
Border: Secondary Color (#2D5A4F)
Background: Secondary Color at 10% opacity
Text: Secondary Color, semibold
```

### Form Input (Focus)
```
Border: Primary Color (#C97655), 2px
Ring: Primary Color, 4px, 10% opacity
Background: Cream (#FAF7F1)
```

---

## Testing Checklist

- [ ] Colors display correctly on mobile (test on actual phone)
- [ ] Contrast meets WCAG AA standards (test with WebAIM)
- [ ] Colors look good on light & dark monitors
- [ ] Colorblind simulation (use Chrome DevTools)
- [ ] Print-friendly (colors should work in grayscale)
- [ ] Compare against brand guidelines/logo

---

## Next Steps

1. **Copy this file** to `docs/branding-colors.md` in your project
2. **Replace all placeholder colors** with your actual brand colors
3. **Update `tailwind.config.js`** with your color values
4. **Run design-system skill** — it will read this file and generate optimized design tokens
5. **Run photo-manager skill** — it will auto-detect and place your logo

---

**Note**: Both photo-manager and design-system skills automatically read this file during the build process. Keep it updated as your brand evolves.
