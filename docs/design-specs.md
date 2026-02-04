# F1R3FLY.IO Website — Design Specifications

Last updated: February 2026

## Typography

### Font Families
- **Headings:** Brandon Grotesque (Adobe Typekit)
- **Body:** Source Sans Pro (Adobe Typekit)
- **Fallbacks:** -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif

### Font Weights
- Light: 300 (body text, most headings)
- Regular: 400 (emphasis, buttons)
- Medium: 330 (navigation)

### Sizes
- Body: 16px
- Navigation: 21px
- Hero tagline: 24px
- Section headings (h2): 2.2rem
- Card headings (h3): 1.2–1.3rem
- Small text / labels: 0.85–0.95rem

### Letter Spacing
- Navigation: 1.47px
- Hero tagline: 1.68px
- Labels / eyebrows: 1.5px

---

## Color Palette

### Backgrounds
- Primary: `#000000`
- Purple gradient: `linear-gradient(180deg, #1a0033 0%, #000 100%)`
- Blue gradient: `linear-gradient(180deg, #001a33 0%, #000 100%)`
- Cards: `rgba(255, 255, 255, 0.02)`
- Form inputs: `rgba(255, 255, 255, 0.05)`

### Text
- Primary: `rgba(255, 255, 255, 0.85)`
- Secondary: `rgba(255, 255, 255, 0.75)`
- Tertiary: `rgba(255, 255, 255, 0.5)`
- Links: `#FFF`

### Borders
- Cards: `rgba(255, 255, 255, 0.08)`
- Footer: `rgba(255, 255, 255, 0.05)`
- Form inputs: `rgba(255, 255, 255, 0.1)`

### Buttons
- Gradient: `linear-gradient(90deg, #a3004d, #b8003d)`
- Hover shadow: `rgba(255, 0, 110, 0.3)`

---

## Layout

### Max Widths
- Content container: 1400px
- Form: 600px
- Text blocks: 900px

### Spacing
- Section padding: 80px vertical, 40px horizontal
- Card padding: 30px
- Navigation: 20px top padding
- Grid gaps: 25–40px

### Navigation
- Fixed position, z-index 1000
- Logo height: 70px
- Link gap: 35px
- Blur backdrop: 10px
- Gradient line separator below

---

## Components

### Cards
- Border radius: 12px
- Background: `rgba(255, 255, 255, 0.02)`
- Border: 1px solid `rgba(255, 255, 255, 0.08)`

### Buttons
- Border radius: 50px (pill shape)
- Padding: 14px 40px
- Text: uppercase, 0.85rem, weight 400
- Hover: translateY(-2px) with box-shadow

### FAQ Accordion
- Expand/collapse with + / − toggle
- Inspired by Avalanche website pattern
- Scroll-reveal animation on entry

### Forms
- Input background: `rgba(255, 255, 255, 0.05)`
- Input border: 1px solid `rgba(255, 255, 255, 0.1)`
- Border radius: 8px
- Padding: 12px

### Parallax Background
- Three PNG layers: starry sky, pine trees, branches
- CSS parallax scrolling effect
- Located in the technology/deep-dive section

### Client Logo Marquee
- Horizontal scrolling animation
- Duplicated set for seamless loop

---

## Responsive Breakpoints

### Mobile (max-width: 768px)
- Navigation logo: 32px height
- Navigation links: 0.7rem
- Headings: 1.8rem
- Grid: single column
- Section padding: 60px 20px

---

## Assets

### Logos
- Navigation: `Logo Brand Horizontal Option with Text.svg`
- Hero: `Logo Brand Vertical Option with Text.svg`
- Favicon: `Logo Icon.svg`
- Industries vertical: `F1R3FLY_INDUSTRIES_Logo_Vertical.svg`

### Video
- Hero background: `FIREFLY ANIMATION_3.mov` (default)
- Alternates: `FIREFLY ANIMATION_4.mov`, `FIREFLY ANIMATION_5.mov`
- Behavior: autoplay, muted, loop, playsinline

### Parallax Layers
- `New Background_layer starry background..png`
- `New Background_pines layer.png`
- `New Background_layer branches..png`

### UI Elements
- `Arrow.svg` — scroll-down indicator
- `Navigation Line.svg` — nav gradient separator
- `team-photo.jpg` — team section photo
