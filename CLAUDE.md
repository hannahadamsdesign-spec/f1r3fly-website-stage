# F1R3FLY Website - AI Assistant Context

## Project Overview

This is the official F1R3FLY Industries website — a marketing and information site for an AI-native Layer 1 blockchain platform built on Rholang.

## Key Technical Details

- **Framework:** Static HTML with embedded CSS (no build step required)
- **Typography:** Brandon Grotesque via Adobe Typekit (`https://use.typekit.net/mhz8bvz.css`)
- **Deployment Target:** Netlify
- **Design Source:** Figma designs translated to production code

## Design System

### Colors
- Background: `#000` (pure black)
- Text: `#f5f5f5` (off-white), `rgba(255, 255, 255, 0.75)` (secondary)
- Gradient sections: Purple (`#1a0033` → `#000`), Blue (`#001a33` → `#000`)
- Buttons: Magenta gradient (`#a3004d` → `#b8003d`)

### Typography
- Font family: `'brandon-grotesque'`
- Body: 16px, weight 300
- Nav links: 21px, weight 330, uppercase, letter-spacing 1.47px
- Headings: weight 300-400

### Components
- Cards: `rgba(255, 255, 255, 0.02)` background, `rgba(255, 255, 255, 0.08)` border
- Buttons: 50px border-radius, uppercase, gradient background
- Navigation: Fixed top, blur backdrop, gradient line separator

## File Structure

```
src/
├── index.html          # Main website (all CSS embedded)
└── images/
    ├── Logo Brand Horizontal Option with Text.svg  # Nav logo
    ├── Logo Brand Vertical Option with Text.svg    # Hero logo
    ├── Logo Icon.svg
    ├── Navigation Line.svg
    └── FIREFLY ANIMATION_*.mov                     # Background videos
```

## Current Status

- ✅ Main structure complete
- ✅ Typography implemented
- ✅ Navigation with gradient line
- ✅ Hero section with video background
- ✅ All content sections
- ⏳ Team photos (placeholders)
- ⏳ Partner/client logos (placeholders)
- ⏳ Demo video embed

## Working Conventions

- Primary development file: `src/index.html`
- Always use "Brandon Grotesque" (not "Brandon Text")
- Image paths are relative to the HTML file: `images/filename.svg`
- Test in Chrome, Safari, Firefox, and on mobile

## Useful Commands

```bash
# Local development server
cd src && python -m http.server 8000

# Check file structure
ls -la src/images/
```

## Contact

Website development coordinated by Hannah Adams
Project owner: Greg Meredith (F1R3FLY CEO)
