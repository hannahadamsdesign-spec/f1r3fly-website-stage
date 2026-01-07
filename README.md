# F1R3FLY Industries Website

The official website for F1R3FLY Industries — an AI-native Layer 1 platform built on Rholang for verifiable, concurrent, multi-agent applications.

## Overview

This repository contains the source code for the F1R3FLY Industries marketing website. The site introduces F1R3FLY's technology, showcases use cases for developers, clients, and partners, and provides access to documentation and demos.

## Tech Stack

- **HTML5** with embedded CSS and JavaScript
- **Typography:** Brandon Grotesque (headings) + Source Sans Pro (body) via Adobe Typekit
- **Deployment:** GitHub Pages / Netlify
- **Design Source:** Figma

## Project Structure

```
/
├── index.html                # Main website file (all CSS/JS embedded)
├── images/                   # Logos, videos, assets
│   ├── Logo Brand Horizontal Option with Text.svg
│   ├── Logo Brand Vertical Option with Text.svg
│   ├── Logo Icon.svg
│   ├── Navigation Line.svg
│   ├── FIREFLY ANIMATION_3.mov
│   ├── FIREFLY ANIMATION_5.mov
│   └── team-photo.jpg
├── docs/
│   └── design-specs.md       # Design specifications
├── CLAUDE.md                 # AI assistant context
├── README.md                 # This file
├── LICENSE                   # Apache 2.0
└── .gitignore
```

## Local Development

1. Clone the repository
2. Open `index.html` in a browser, or use a local server:
   ```bash
   python -m http.server 8000
   # or
   npx serve .
   ```
3. Visit `http://localhost:8000`

## Features

- **Video hero** with looping firefly animation
- **Section-specific gradient backgrounds** (teal, magenta, green, neutral)
- **FAQ accordion** with scroll-reveal animations
- **Team parallax** section
- **Mobile responsive** with hamburger menu
- **Bouncy smooth scroll** with elastic easing
- **Active nav highlighting** based on scroll position

## Design

- **Color Scheme:** Black background with section-specific gradients
- **Typography:** Brandon Grotesque for headings, Source Sans Pro for body
- **Accent Colors:** Cyan (#03D5FF) for hover, Yellow (#F5D731) for active states
- **Visual Style:** Minimal, professional, with subtle animations

## Deployment

Push to `main` to trigger deployment via GitHub Pages or Netlify.

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.

## Contact

For questions about the website, reach out to the F1R3FLY team at f1r3fly.ceo@gmail.com
