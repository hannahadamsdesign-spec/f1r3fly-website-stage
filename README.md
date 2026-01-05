# F1R3FLY Industries Website

The official website for F1R3FLY Industries — an AI-native Layer 1 platform built on Rholang for verifiable, concurrent, multi-agent applications.

## Overview

This repository contains the source code for the F1R3FLY Industries marketing website. The site introduces F1R3FLY's technology, showcases use cases for developers, clients, and partners, and provides access to documentation and demos.

## Tech Stack

- **HTML5** with embedded CSS
- **Typography:** Brandon Grotesque (via Adobe Typekit)
- **Deployment:** Netlify
- **Design Source:** Figma

## Project Structure

```
website-next/
├── README.md                 # This file
├── CLAUDE.md                 # AI assistant context
├── docs/                     # Documentation
│   └── design-specs.md       # Design specifications
├── src/
│   ├── index.html            # Main website file
│   └── images/               # Logos, animations, assets
├── .gitignore
└── LICENSE
```

## Local Development

1. Clone the repository
2. Open `src/index.html` in a browser
3. For live reload during development, use a local server:
   ```bash
   cd src
   python -m http.server 8000
   ```
   Then visit `http://localhost:8000`

## Deployment

The site is deployed via Netlify. Pushing to `main` triggers automatic deployment.

## Design

- **Color Scheme:** Black background with purple/blue gradients
- **Typography:** Brandon Grotesque (light/regular weights)
- **Visual Style:** Minimal, professional, with parallax effects and subtle animations

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.

## Contact

For questions about the website, reach out to the F1R3FLY team at f1r3fly.ceo@gmail.com
