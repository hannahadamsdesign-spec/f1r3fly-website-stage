# F1R3FLY Website - AI Assistant Context

## Project Overview

This is the official F1R3FLY Industries website — a marketing and information site for an AI-native Layer 1 blockchain platform built on Rholang.

## Key Technical Details

- **Framework:** Static HTML with embedded CSS (no build step required)
- **Typography:** Brandon Grotesque (headings/UI) + Source Sans Pro (body) via Adobe Typekit
- **Deployment Target:** GitHub Pages / Netlify
- **Design Source:** Figma designs translated to production code

## Design System

### Colors
- Background: `#000` (pure black)
- Text: `rgba(255, 255, 255, 0.85)` (primary body), `#fff` (headings)
- Accent: `#03D5FF` (cyan hover states), `#F5D731` (yellow active states)
- Gradient labels: `linear-gradient(90deg, #80D5FF 0%, #C6E0AB 89.42%, #FFE867 100%)`

### Section Gradient Backgrounds
- Teal (Developers): `#001a2a` → `#000`
- Magenta (Clients): `#1a0515` → `#000`
- Green (Partners): `#0a200f` → `#000`
- Neutral (Tech/Blog): `#151B22` → `#000`

### Button Colors (matching section themes)
- Developer: `#0063b0` → `#007a73` (teal)
- Client: `#5c0269` → `#7b0429` (magenta)
- Partner: `#0c8e23` → `#7a9d0e` (green)
- Neutral: `#2a3441` → `#3d4a5c` (slate)

### Typography
- Body: `'source-sans-pro'`, 16px, weight 300, letter-spacing 0.04em
- Headings/UI: `'brandon-grotesque'`
- Nav links: 18px, weight 330, uppercase, letter-spacing 1.47px
- Section headings: 2.75rem, weight 100

### Components
- Cards: Dashed border `rgba(255, 255, 255, 0.2)`, 12px border-radius
- Buttons: 50px border-radius, 32px height, gradient backgrounds
- Navigation: Fixed top, 50% opacity black with blur, gradient line separator
- FAQ: Accordion-style with scroll-reveal animations

## File Structure

```
/
├── index.html              # Main website (all CSS/JS embedded)
├── images/
│   ├── Logo Brand Horizontal Option with Text.svg
│   ├── Logo Brand Vertical Option with Text.svg
│   ├── Logo Icon.svg
│   ├── Navigation Line.svg
│   ├── FIREFLY ANIMATION_3.mov    # Hero video background
│   ├── FIREFLY ANIMATION_5.mov    # Backup video
│   └── team-photo.jpg             # Team parallax section
├── docs/
│   └── design-specs.md
├── README.md
├── CLAUDE.md                      # This file
└── LICENSE                        # Apache 2.0
```

## Current Status (January 2026)

- ✅ Main structure complete with all sections
- ✅ Typography: Source Sans Pro body + Brandon Grotesque headings
- ✅ Navigation with gradient line and active states
- ✅ Hero section with video background
- ✅ Section-specific gradient backgrounds (teal, magenta, green, neutral)
- ✅ Color-coded buttons matching each section
- ✅ FAQ accordion with scroll-reveal animations
- ✅ Team parallax section
- ✅ Mobile responsive with hamburger menu
- ⏳ Individual team photos (using placeholders)
- ⏳ Partner/client logos (using placeholder boxes)
- ⏳ Demo video embeds

## Key Features

### Interactive Elements
- Bouncy smooth scroll with elastic easing
- FAQ accordion (click to expand/collapse)
- Scroll-reveal animations on FAQ panels
- Active nav state highlighting based on scroll position
- Hover effects on buttons and links

### Sections
1. **Intro/Hero** - Video background, vertical logo, taglines
2. **Home** - Three-column cards (Developer/Client/Partner)
3. **Scalable/Storable/Searchable** - Three-column text (neutral gradient)
4. **Team Parallax** - Full-width image break
5. **Toto Quote** - Two-column layout (neutral gradient)
6. **Technology** - Deep dive content + FAQ accordion
7. **Developers** - Three cards + demo section (teal gradient)
8. **Clients** - Logo grid + case studies (magenta gradient)
9. **Partners** - Ecosystem info + partner types (green gradient)
10. **Team** - Four-column grid with bios
11. **Blog** - Three cards (neutral gradient)
12. **Contact** - Two-column form
13. **Footer** - Social icons + copyright

## Working Conventions

- Primary development happens in `07 Development Claude/index2.html`
- This repo (`website-recreation-2026`) is for deployment to GitHub
- Always use "Brandon Grotesque" for headings (not "Brandon Text")
- Image paths are relative: `images/filename.svg`
- Test in Safari, Chrome, Firefox, and on mobile

## Useful Commands

```bash
# Local development server
python -m http.server 8000

# Or with Node
npx serve .
```

## Contact

Website development: Hannah Adams (Creative Director)
Project owner: Greg Meredith (F1R3FLY CEO)
Product: Jeff Turner
