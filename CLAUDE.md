# F1R3FLY.IO Website — AI Assistant Context

## Project Overview

This is the official F1R3FLY.IO website — a marketing and information site for an AI-native Layer 1 blockchain platform built on Rholang. The site targets three audiences: developers, clients, and partners.

## Live Site

- **URL:** https://f1r3fly.io/f1r3fly-io-website/
- **Deployed from:** GitHub Pages via the `F1R3FLY-io/f1r3fly-io-website` organization repo
- **This local folder** (`website-recreation-2026`) is the working/staging copy. Files are manually uploaded to the org repo for deployment.

## Key Technical Details

- **Framework:** Static HTML with embedded CSS and JS (no build step)
- **Typography:** Brandon Grotesque headings via Adobe Typekit, Source Sans Pro body text
- **Typekit URL:** `https://use.typekit.net/mhz8bvz.css`
- **Design Source:** Figma (files in Dropbox `01 Source Files/`)

## Design System

### Colors
- Background: `#000` (pure black)
- Text primary: `rgba(255, 255, 255, 0.85)`
- Text secondary: `rgba(255, 255, 255, 0.75)`
- Text tertiary: `rgba(255, 255, 255, 0.5)`
- Purple gradient sections: `#1a0033` → `#000`
- Blue gradient sections: `#001a33` → `#000`
- Buttons: Magenta gradient `#a3004d` → `#b8003d`
- Cards: `rgba(255, 255, 255, 0.02)` bg, `rgba(255, 255, 255, 0.08)` border

### Typography
- Headings: `brandon-grotesque`, weight 300–400
- Body: `source-sans-pro`, weight 300, 16px
- Nav links: 21px, weight 330, uppercase, letter-spacing 1.47px

### Key Components
- Fixed nav with blur backdrop and gradient line separator
- Hero section with looping .mov video background
- Scroll-reveal animations on section entry
- FAQ accordion (inspired by Avalanche website)
- Parallax forest/starry sky background layers
- Contact form with role-based dropdown
- Client logo marquee

## File Structure

```
website-recreation-2026/
├── index.html              # Main website (all CSS/JS embedded)
├── images/
│   ├── Arrow.svg
│   ├── F1R3FLY_INDUSTRIES_Logo_Vertical.svg
│   ├── FIREFLY ANIMATION_3.mov
│   ├── FIREFLY ANIMATION_4.mov
│   ├── FIREFLY ANIMATION_5.mov
│   ├── Logo Brand Horizontal Option with Text.svg  (nav)
│   ├── Logo Brand Vertical Option with Text.svg    (hero)
│   ├── Logo Icon.svg                               (favicon)
│   ├── Navigation Line.svg
│   ├── New Background_layer branches..png           (parallax)
│   ├── New Background_layer starry background..png  (parallax)
│   ├── New Background_pines layer.png               (parallax)
│   └── team-photo.jpg
├── docs/
│   └── design-specs.md
├── CLAUDE.md               # This file
├── README.md
├── LICENSE                  # Apache 2.0
├── .gitignore
└── .gitattributes
```

## Current Status

- ✅ Full single-page site with all sections
- ✅ Typography: Brandon Grotesque headings + Source Sans Pro body
- ✅ Navigation with gradient line and blur backdrop
- ✅ Hero with video background and vertical logo
- ✅ Developer / Client / Partner content cards
- ✅ FAQ accordion with scroll-reveal
- ✅ Parallax forest background
- ✅ Contact form
- ✅ Client logo marquee
- ⏳ Team photos (using placeholder)
- ⏳ Partner/client logos (text placeholders)
- ⏳ Demo video embeds
- ⏳ Blog content (placeholder structure)

## Working Conventions

- All CSS and JS are embedded in `index.html` (no separate files)
- Image paths are relative: `images/filename.svg`
- Use "Brandon Grotesque" for headings only, "Source Sans Pro" for body
- Test in Chrome, Safari, Firefox, and mobile
- Workflow: edit here → upload to org repo → live on GitHub Pages

## Folder Location

This working folder lives at:
`Dropbox/01 ACTIVE WORK/F1R3FLY PROJECTS/02 F1R3FLY Website/07 Website Development/`

Sibling folders in the parent contain source files, Figma designs, stock photos, and video options.

## Contact

Website development: Hannah Adams (Creative Director)
Project owner: Greg Meredith (F1R3FLY CEO)
