# Color Selection Tools & Resources

A comprehensive guide to tools and resources for selecting, testing, and implementing color palettes.

## Color Picker & Generator Tools

### Adobe Color (Recommended)
**Website**: [color.adobe.com](https://color.adobe.com)

**Features**:
- Interactive color wheel with harmony rules built-in
- Save palettes to Creative Cloud
- Extract colors from images
- Harmonize automatic suggestions
- WCAG accessibility check
- Trending palettes library

**Best for**: Quick palette generation, exploring different harmonies, professional color design

**Workflow**:
1. Click wheel to select base color
2. Switch harmony rule (monochromatic, analogous, complementary, etc.)
3. Adjust saturation/lightness with sliders
4. Save palette to account
5. Export as JSON, XML, CSS, or ASE

---

### Coolors.co (Most Popular)
**Website**: [coolors.co](https://coolors.co)

**Features**:
- Super fast palette generator (spacebar to generate)
- Lock colors and regenerate others
- Color picker from images
- Explore trending palettes
- Accessibility contrast check
- Export to multiple formats

**Best for**: Quick inspiration, rapid iteration, collaborative palette building

**Workflow**:
1. Go to site
2. Press spacebar to generate random palette
3. Lock colors you like, unlock others
4. Repeat until satisfied
5. Export or share link with team

---

### Paletton (formerly Colorjive)
**Website**: [paletton.com](https://paletton.com)

**Features**:
- Advanced color wheel with all 7 harmonies
- Real-time preview on sample website
- Manual RGB/HSL value entry
- Tint/shade generation
- Colorblind vision simulator built-in
- Export CSS, HTML, XML

**Best for**: Advanced color theory exploration, seeing colors in context, colorblind checking

**Workflow**:
1. Select harmony rule from dropdown
2. Adjust base color position on wheel
3. Preview colors on sample site layout
4. Check all 3 colorblind modes (Vision tab)
5. Export CSS code

---

### Chir.ag Tools
**Website**: [chir.ag/projects/ntc/](https://chir.ag/projects/ntc/)

**Features**:
- Color name generator (name any hex)
- Color temperature visualization
- HSL picker with values
- Name color you see in nature

**Best for**: Understanding color relationships, finding color names

---

### Colorhexa.com
**Website**: [colorhexa.com](https://colorhexa.com)

**Features**:
- Hex value lookup (e.g., colorhexa.com/3B82F6)
- Full color information (RGB, HSL, HSV, CMYK)
- Complementary colors calculated
- Tints and shades generated
- Variations and harmonies

**Best for**: Quick color information lookup, understanding color value conversions

---

## Accessibility & Contrast Testing

### WebAIM Contrast Checker (Essential)
**Website**: [webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)

**Features**:
- Enter foreground and background colors
- Get contrast ratio instantly
- See if ratio meets AA/AAA standards
- Suggestions for improving contrast
- Swap colors to try different combinations
- Visual preview of actual contrast

**Must-use**: Test every color pair before implementation

**Workflow**:
1. Enter text color (hex or RGB)
2. Enter background color
3. Check ratio meets 4.5:1 (normal text) or 3:1 (large text/UI)
4. Adjust if needed
5. Note final colors for implementation

---

### TPGI Color Contrast Analyzer
**Website**: [tpgi.com/color-contrast-checker/](https://www.tpgi.com/color-contrast-checker/)

**Features**:
- More detailed than WebAIM
- Level AA and AAA indicators
- Alternative combinations suggestions
- Export results
- Browser extension available

**Best for**: Detailed accessibility audits, professional compliance documentation

---

### Coblis Color Blindness Simulator (Essential)
**Website**: [color-blindness.com/coblis/](https://www.color-blindness.com/coblis-color-blindness-simulator/)

**Features**:
- Upload screenshot
- See how colorblind users perceive colors
- Simulate all 3 types (Protanopia, Deuteranopia, Tritanopia)
- Interactive color picker to test individual colors
- Download simulation images

**Must-use**: Test colors through colorblind lens before launch

**Workflow**:
1. Upload screenshot of color palette
2. View all 3 colorblind simulations
3. Check if colors still distinguishable
4. Add text labels if needed
5. Iterate until colorblind-accessible

---

### Vischeck Color Blindness Simulator
**Website**: [vischeck.com](https://www.vischeck.com/)

**Features**:
- Another colorblind simulator
- Detailed information about types
- Educational resources
- Image upload
- FAQ about color blindness

---

### Chrome DevTools Accessibility Checker
**Built-in**: Browser developer tools

**Features**:
- Automatic contrast checking
- Accessibility audit in DevTools
- Real-time feedback on live sites
- Check actual rendered colors

**How to use**:
1. Open DevTools (F12)
2. Go to Lighthouse tab
3. Run Accessibility audit
4. Check contrast issues section
5. See specific elements failing

---

## Color Extraction Tools

### Color Picker Tools

**Chrome Extension - Eye Dropper**
- Pick any color on any website
- Copy hex value
- View RGB/HSL
- [Install here](https://chrome.google.com/webstore/detail/eye-dropper/cppjkneekbjaeellbfkmgnhbagmmfol)

**Firefox Extension - Color Picker**
- Similar to Chrome version
- Built into Firefox DevTools
- Shortcut: Shift + O in DevTools

**Online Tool - Image Color Picker**
- [imagecolorpicker.com](https://imagecolorpicker.com/)
- Upload or paste image URL
- Click to extract colors
- Get hex/RGB values

---

## Color Theory & Psychology References

### Books
- **"Thinking with Type"** by Ellen Lupton — Color in typography
- **"The Art of Color"** by Johannes Itten — Classic color theory
- **"Seizing the Light"** by Roger Cicala — Color in photography
- **"Web Design Secrets"** includes extensive color chapters

### Online Resources
- **Color Theory 101** - [interaction-design.org](https://www.interaction-design.org/literature/topics/color-theory)
- **WCAG Guidelines** - [w3.org/WAI/WCAG21/quickref](https://www.w3.org/WAI/WCAG21/quickref/)
- **Color Psychology Guide** - [empower.com](https://www.empower.com/resources/color-psychology)

---

## Design Tool Integration

### Figma Color Library
**Built-in feature**:
```
1. Create color styles in Figma
2. Right-click component → Create component
3. Add color as design token
4. Share library with team
5. Export to code with plugins
```

**Recommended plugins**:
- **Figma Tokens** (Design Tokens) — Sync design system
- **Color Var** — CSS variable generator
- **Stark** — Colorblind simulator in Figma

---

### Tailwind CSS Color Config
**Use Tailwind's built-in colors or customize**:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    colors: {
      primary: '#3B82F6',
      secondary: '#F3F4F6',
      accent: '#DC2626',
      success: '#10B981',
      warning: '#F59E0B',
      error: '#EF4444',
      text: '#1F2937',
      background: '#FFFFFF'
    }
  }
}
```

**Generate scale with plugins**:
- **Tailwind Color Shades Generator** — Generate 50-900 scale
- **Palette generator** — Create monochromatic scales

---

### CSS Custom Properties Generator
**Create from palette**:

```css
:root {
  --color-primary: #3B82F6;
  --color-primary-dark: #1E40AF;
  --color-primary-light: #DBEAFE;

  --color-secondary: #F3F4F6;

  --color-accent: #DC2626;

  /* ... etc */
}
```

**Tools that generate**:
- [CSS Variable Generator](https://chir.ag/)
- [Tailwind Config Generator](https://tailwindcss.com/docs/configuration)

---

## Trend & Inspiration Resources

### Design Inspiration
- **Dribbble** - dribbble.com — Professional design showcase
- **Behance** - behance.net — Adobe portfolio community
- **Pinterest** - pinterest.com — Search "color palette" for trends
- **Brand Style Guides** - brandonguidelines.com — Real brand color systems

### 2026 Color Trends
- **Pantone Color of the Year** - pantone.com/color-intelligence
- **Adobe Color Trends** - adobe.com/creativecloud/design/discover
- **Design Trend Reports** - designmodo.com/trends

---

## Command-Line Tools

### ColorSpace CLI
Generate color palettes from command line:

```bash
npm install -g colorspace
colorspace generate blue complementary
```

### Chroma.js
Node.js library for color manipulation:

```javascript
const chroma = require('chroma-js');

// Generate palette
const palette = chroma.scale(['blue', 'red']).mode('lab').colors(5);
console.log(palette);  // Array of 5 colors

// Convert
const hex = chroma('#3B82F6').hex();
const rgb = chroma('#3B82F6').rgb();
const hsl = chroma('#3B82F6').css('hsl');
```

---

## Best Practices Workflow

### Complete Color Selection Process

1. **Research** (15 min)
   - Define brand personality
   - Research industry color expectations
   - Look at competitor colors
   - Browse inspiration (Dribbble, Behance)

2. **Generate** (20 min)
   - Use Adobe Color or Coolors
   - Create 3-4 different palettes
   - Screenshot for comparison

3. **Validate** (15 min)
   - Test contrast with WebAIM
   - Simulate colorblindness with Coblis
   - Check against industry best practices
   - Get feedback from team

4. **Refine** (15 min)
   - Adjust colors that failed accessibility
   - Balance saturation/lightness
   - Ensure 60-30-10 distribution works

5. **Implement** (20 min)
   - Create CSS variables
   - Add to Tailwind config
   - Document in design system
   - Test on real components

**Total time**: ~1.5 hours for complete palette

---

## Quick Reference: Tool Selection

**Question**: What tool should I use?

| Need | Recommended Tool | Alternative |
|------|------------------|-------------|
| Generate palette | Coolors.co | Adobe Color |
| Understand theory | Paletton | Chir.ag |
| Check contrast | WebAIM | Lighthouse DevTools |
| Colorblind simulation | Coblis | Vischeck |
| Pick color from image | Eye Dropper extension | Online picker |
| Export to code | Adobe Color | Figma |
| Get hex values | Colorhexa | Chrome DevTools |
| Browse trends | Pantone/Adobe | Pinterest |

---

**Key Takeaway**: Use the right tool for each phase of color selection. Start with generators, validate with accessibility checkers, inspect with pickers, and document with design systems.
