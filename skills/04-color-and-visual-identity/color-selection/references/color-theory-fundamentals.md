# Color Theory Fundamentals

## The Color Wheel

The color wheel is the foundation of color theory, organizing 12 primary colors in a circle:

```
        YELLOW (Warm)
       /          \
    GREEN         ORANGE
   /                  \
CYAN              RED-ORANGE
 |                      |
BLUE-VIOLET         RED
  \                  /
    BLUE          MAGENTA
     \           /
   BLUE-GREEN VIOLET (Cool)
```

**Primary Colors** (cannot be created by mixing):
- Red, Yellow, Blue (traditional)
- Red, Green, Blue (light/digital)

**Secondary Colors** (mix of two primary):
- Orange (Red + Yellow)
- Green (Yellow + Blue)
- Violet (Red + Blue)

**Tertiary Colors** (primary + secondary):
- Red-Orange, Yellow-Orange, Yellow-Green, Blue-Green, Blue-Violet, Red-Violet

## HSL Model (Hue, Saturation, Lightness)

HSL is the most intuitive model for web design:

```
hsl(0-360, 0%-100%, 0%-100%)
```

### Hue (0-360°)
- **0°** = Red
- **60°** = Yellow
- **120°** = Green
- **180°** = Cyan
- **240°** = Blue
- **300°** = Magenta
- **360°** = Red again

### Saturation (0-100%)
- **0%** = Grayscale (no color)
- **50%** = Muted color
- **100%** = Pure, vivid color

**Effect on web design:**
- **100% saturation**: Vibrant, energetic, can be overwhelming
- **50-70% saturation**: Professional, balanced, approachable
- **0-30% saturation**: Muted, sophisticated, calming

### Lightness (0-100%)
- **0%** = Black
- **50%** = Pure color
- **100%** = White

**Effect on web design:**
- **10-30%** = Dark backgrounds (dark mode)
- **40-60%** = Readable text and elements
- **70-90%** = Light backgrounds, subtle elements
- **95%+** = Almost white, off-white backgrounds

### Practical HSL Adjustments

To create a palette from one color, adjust L and S:

```
Base color:       hsl(240, 100%, 50%)    // Pure blue

Lighter variant:  hsl(240, 100%, 70%)    // Lighter blue
Darker variant:   hsl(240, 100%, 30%)    // Darker blue
Muted variant:    hsl(240, 50%, 50%)     // Muted blue
Pale variant:     hsl(240, 30%, 85%)     // Pale blue
```

## Color Temperature

Colors carry psychological warmth:

### Warm Colors (0-60° on wheel)
- **Red, Orange, Yellow**
- Energetic, exciting, stimulating
- Draw forward visually (appear closer)
- Increase sense of urgency
- **Use for**: CTAs, highlights, energy

### Cool Colors (180-360° on wheel)
- **Blue, Green, Violet**
- Calming, trustworthy, refreshing
- Recede visually (appear farther)
- Promote focus and tranquility
- **Use for**: Backgrounds, large surfaces, trust building

### Neutral Colors
- **Grays, Blacks, Whites, Browns**
- Balance warm and cool
- Provide stability and readability
- Essential for accessibility

## Color Harmony Principles

Harmonious colors work together visually. Four main approaches:

### 1. Monochromatic (No angle difference)
Single hue with varied saturation/lightness:
```
hsl(240, 100%, 30%)  // Dark blue
hsl(240, 100%, 50%)  // Base blue
hsl(240, 100%, 70%)  // Light blue
hsl(240, 30%, 85%)   // Pale blue
```
**Properties**: Cohesive, calming, unified but potentially boring
**Best for**: Corporate, healthcare, minimalist sites

### 2. Analogous (0-30° apart)
Adjacent colors on color wheel:
```
hsl(210, 80%, 50%)   // Blue-green
hsl(240, 80%, 50%)   // Blue
hsl(270, 80%, 50%)   // Blue-violet
```
**Properties**: Harmonious, natural, pleasing
**Best for**: Nature, lifestyle, welcoming sites

### 3. Complementary (180° apart)
Opposite colors on wheel:
```
hsl(240, 80%, 50%)   // Blue
hsl(60, 80%, 50%)    // Yellow
```
**Properties**: High contrast, vibrant, energetic
**Best for**: E-commerce, creative, attention-grabbing

### 4. Split-Complementary (150-210° apart)
Primary color + neighbors of complement:
```
hsl(240, 80%, 50%)   // Blue
hsl(30, 80%, 50%)    // Orange
hsl(90, 80%, 50%)    // Yellow-green
```
**Properties**: Less tension than complementary, more dynamic than analogous
**Best for**: Balanced, modern design

### 5. Triadic (120° apart)
Three evenly-spaced colors:
```
hsl(0, 80%, 50%)     // Red
hsl(120, 80%, 50%)   // Green
hsl(240, 80%, 50%)   // Blue
```
**Properties**: Vibrant, balanced, playful
**Best for**: Creative, playful, tech-forward sites

### 6. Tetradic (90° apart)
Four colors in two complementary pairs:
```
hsl(0, 80%, 50%)     // Red
hsl(90, 80%, 50%)    // Yellow-green
hsl(180, 80%, 50%)   // Cyan
hsl(270, 80%, 50%)   // Magenta
```
**Properties**: Rich, complex, requires careful balance
**Best for**: Complex interfaces, rich visual systems

### 7. Achromatic
No hue — only saturation/lightness:
```
hsl(0, 0%, 0%)       // Black
hsl(0, 0%, 30%)      // Dark gray
hsl(0, 0%, 60%)      // Medium gray
hsl(0, 0%, 90%)      // Light gray
hsl(0, 0%, 100%)     // White
```
**Properties**: Timeless, sophisticated, minimal
**Best for**: Minimalist, luxury, typography-focused sites

## Finding Complementary Colors

To find the complement of any color, add 180° to its hue:

```
Base:        hsl(240, 80%, 50%)  // Blue
Complement:  hsl(60, 80%, 50%)   // Yellow (240 + 180 = 420, wraps to 60)

Base:        hsl(30, 80%, 50%)   // Orange
Complement:  hsl(210, 80%, 50%)  // Blue (30 + 180 = 210)
```

## Practical Color Mixing (For Understanding)

Although web design doesn't involve physical mixing, understanding relationships helps:

**Light mixing (additive)**:
- Red + Green + Blue light = White light
- Used in: RGB values, screens, light

**Paint mixing (subtractive)**:
- Red + Yellow + Blue pigment = Brown/dark
- Used in: Print, physical materials

**Web design uses both concepts**:
- RGB/HSL for screen display
- Print-safe CMYK for PDF exports

## Creating Accessible Tints and Shades

### Tints (add white)
Lighten color by increasing lightness:
```
Base:  hsl(240, 100%, 50%)
Tint:  hsl(240, 100%, 70%)  // +20% lightness
```

### Shades (add black)
Darken color by decreasing lightness:
```
Base:   hsl(240, 100%, 50%)
Shade:  hsl(240, 100%, 30%)  // -20% lightness
```

### Design Token Pattern

For each brand color, generate a scale:
```
50:   hsl(240, 100%, 98%)   // Near white
100:  hsl(240, 100%, 95%)   // Very light
200:  hsl(240, 100%, 90%)   // Light
300:  hsl(240, 100%, 75%)   // Medium-light
400:  hsl(240, 100%, 60%)   // Light base
500:  hsl(240, 100%, 50%)   // Base (primary)
600:  hsl(240, 100%, 40%)   // Dark base
700:  hsl(240, 100%, 30%)   // Dark
800:  hsl(240, 100%, 20%)   // Very dark
900:  hsl(240, 100%, 10%)   // Near black
```

This pattern (like Tailwind's 50-900 scale) provides rich options for accessible design.

## Color Blindness Considerations

~8% of males, ~0.4% of females have color vision deficiency:

**Most common: Red-Green blindness**
- Cannot distinguish red from green
- Solution: Never rely solely on red/green to convey meaning
- Use shape, pattern, or text labels in addition to color

**Second most common: Blue-Yellow blindness**
- Rarer but affects blue/yellow combinations
- Solution: Ensure blue text on yellow backgrounds has sufficient contrast

**Practical design rule**: Ensure all information conveyed by color is also conveyed by shape, text, or contrast. Test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/).

---

**Key Takeaway**: Master HSL to manipulate colors predictably. Understand the 12 hues on the color wheel. Know which harmony principle to apply for your design goal.
