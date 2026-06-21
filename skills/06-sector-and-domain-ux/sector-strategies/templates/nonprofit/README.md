---
title: Nonprofit/Charity/NGO Sector - Complete Setup Guide
---

# Nonprofit/Charity/NGO Sector Templates

Complete, production-ready templates for building stunning nonprofit and charity websites using Astro + Tailwind CSS v4 + Alpine.js.

**Features**: Full light mode & dark mode support, accessible design, donation-optimized, impact-focused.

---

## What's Included

### Templates (Copy to Your Project)

1. **sector-brief-template.md** → `docs/sector-brief.md`
   - Mission statement & organization identity
   - Trust & credibility documentation
   - Impact metrics (people served, lives changed, etc.)
   - Donation strategy & tiers
   - Brand colors (hex codes)
   - Stories & testimonials
   - Engagement CTAs

### Design References

2. **design-tokens.md** — Color palettes, typography scale, spacing, animations, accessibility contrast (light + dark mode)

3. **COMPONENT-PATTERNS-INDEX.md** — 10 core components with dark mode support, copy-paste HTML/Tailwind templates

4. **color-psychology.md** — Nonprofit color psychology by hue, competitive differentiation strategies, palette construction formula, sub-sector color guide, semantic token naming

5. **storytelling-design.md** — The dignity principle, hero section patterns, impact numbers, donation conversion design (54% uplift), trust architecture, photography direction, navigation for multiple audiences

6. **sub-sector-patterns.md** — Design patterns for 6 nonprofit sub-sectors: Environment/Agriculture, Healthcare, Education/Youth, Humanitarian, Arts/Culture, Research/Science. Branding personality framework.

### 🎨 Dark Mode Support

All components include:
- ✅ Light mode colors (primary palette)
- ✅ Dark mode colors (adjusted for contrast & readability)
- ✅ WCAG 2.1 AA accessibility in both modes
- ✅ Smooth transitions between modes
- ✅ System preference detection + manual toggle
- ✅ Persistent user choice in localStorage

### 🛠️ How to Implement

#### Step 1: Setup Tailwind for Dark Mode
```javascript
// tailwind.config.js
export default {
  darkMode: 'class', // Enable class-based dark mode
  // ... rest of config
}
```

#### Step 2: Add Dark Mode Toggle
Copy from DARK-MODE-IMPLEMENTATION.md

#### Step 3: Copy Templates to Your Project
```
docs/
├── sector-brief.md              ← Copy sector-brief-template.md & fill in
├── branding-colors.md           ← Define brand colors (hex codes)
└── pages.md                      ← List pages to build
```

#### Step 4: Use Component Patterns
Reference COMPONENT-PATTERNS-INDEX.md for each component you need
All examples include `dark:` prefix utilities

#### Step 5: Run Design System
The design-system skill reads your sector-brief.md and generates:
- tailwind.config.mjs with your brand colors
- design-tokens.md with custom palette
- global CSS with dark mode support

---

## 🎯 Nonprofit-Specific Features

### Donation Optimization
- Multi-step donation form (amount → info → payment)
- Recurring donation options (one-time, monthly, annual)
- Matching gift detection
- Tax receipt option
- Donation tiers ($50 = supplies for 1 student, etc.)

### Impact Storytelling
- Story gallery or featured story stack (manual navigation only if interactive)
- Animated impact metrics (people helped, lives changed)
- Testimonial quotes with attribution
- Before/after transformations
- Real photos + authentic stories

### Engagement CTAs
- Newsletter signup (persistent banner)
- Volunteer opportunities
- Event calendar
- Sponsor a person/project
- Corporate giving
- Planned giving / Legacy donations

### Trust Signals
- 501(c)(3) status badge
- Charity Navigator / GiveWell ratings
- Staff & leadership team
- Financials transparency
- Certifications & awards
- Years of service

### Accessibility (Critical for Nonprofits)
- WCAG 2.1 AA compliance
- Mobile-first (users on slow connections)
- Screen reader support
- High contrast mode
- Keyboard navigation
- Reduced motion support

---

## 🌓 Dark Mode Best Practices

### Color Mapping

| Component | Light Mode | Dark Mode |
|-----------|-----------|-----------|
| Donation CTA | Blue (#0EA5E9) | Cyan (#06B6D4) |
| Impact Stats | Blue text | Cyan text (lighter) |
| Story Cards | White background | Dark surface (#1E293B) |
| Input Fields | Light gray | Dark surface + visible border |
| Body Text | Dark gray | Light gray |
| Accents | Magenta (#D946EF) | Lighter Magenta (#EC4899) |

### Testing Checklist
- [ ] Light mode: All text 7:1 contrast (WCAG AAA)
- [ ] Dark mode: All text 4.5:1 minimum (WCAG AA)
- [ ] Buttons readable in both modes
- [ ] Images visible with dark overlay in dark mode
- [ ] Form inputs have visible borders in dark mode
- [ ] Links underline on hover (both modes)
- [ ] Toggle button works (localStorage persists choice)
- [ ] No flash of wrong theme on page load

---

## 📱 Example Nonprofit Websites to Study

### High-Impact Storytelling
- [Charity: Water](https://www.charitywater.org) - Transparency + visual stories
- [World Wildlife Fund](https://www.worldwildlife.org) - Global scale, powerful imagery

### Trust & Credibility
- [Save the Children](https://www.savethechildren.org) - Professional + clear metrics
- [GiveDirectly](https://www.givedirectly.org) - Transparent, data-driven

### Mobile-First
- [OneGive](https://www.onegivecampaign.com) - Simple, mobile-optimized giving
- [GlobalGiving](https://www.globalgiving.org) - Project browsing, donor dashboard

### Volunteer & Community
- [Idealist.org](https://www.idealist.org) - Opportunity matching
- [VolunteerMatch](https://www.volunteermatch.org) - Searchable volunteer roles

---

## 🚀 Quick Start (3 Steps)

### 1. Copy Templates
```bash
cp sector-brief-template.md ../../docs/sector-brief.md
cp branding-colors-template.md ../../docs/branding-colors.md
```

### 2. Fill in Organization Details
Edit `docs/sector-brief.md`:
- Mission statement
- Impact metrics
- Brand colors (hex codes)
- Stories & testimonials
- Donation tiers

### 3. Run Design System Skill
The design-system skill reads `docs/sector-brief.md` and auto-generates:
- tailwind.config with your colors
- design tokens
- dark mode support

---

## File Structure

```
nonprofit/
├── sector-brief-template.md        (Copy to docs/sector-brief.md)
├── design-tokens.md                (Reference: palettes, typography, spacing)
├── COMPONENT-PATTERNS-INDEX.md     (Reference: 10 components + dark mode)
├── color-psychology.md             (Reference: color meanings, sub-sector palettes)
├── storytelling-design.md          (Reference: dignity principle, trust, donation UX)
├── sub-sector-patterns.md          (Reference: 6 sub-sector design patterns)
└── README.md                       (This file)
```

---

## 🔗 Related Files

- **DARK-MODE-IMPLEMENTATION.md** - Complete dark mode setup guide
- **branding-colors-template.md** - Color documentation template
- **education/IMPLEMENTATION-GUIDE.md** - Component patterns reference
- **photo-manager/SKILL.md** - Auto-logo detection & image optimization

---

## ✨ Key Highlights

✅ **No Code Required** - Fill templates, run skills, get website
✅ **Donation-Optimized** - Multi-step form, recurring options, matching gifts
✅ **Impact-Focused** - Story-led layouts, animated metrics, testimonials
✅ **Dark Mode** - 100% support, accessible, beautiful in both modes
✅ **Accessibility** - WCAG 2.1 AA+, screen reader ready, keyboard nav
✅ **Mobile-First** - Works perfectly on slow connections & small screens
✅ **Performance** - Lighthouse 95+, images optimized, zero external CDN

---

## 🤝 Support

For questions or customizations:
1. Check **design-tokens.md** for color/spacing reference
2. Review **COMPONENT-PATTERNS-INDEX.md** for component examples
3. Consult **DARK-MODE-IMPLEMENTATION.md** for dark mode questions
4. Reference **education/IMPLEMENTATION-GUIDE.md** for accessibility patterns

---

**Ready to build?** Start with sector-brief-template.md → customize → run design-system skill → build with page-builder skill.

**Built with ❤️ for nonprofits making a difference.**
