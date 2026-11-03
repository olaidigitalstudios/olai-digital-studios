# Design Specification & Design System
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.3.0 (Heritage & Craft Design System)  
**Status:** Approved for Implementation  
**Derived From:** [PRODUCT_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/PRODUCT_SPEC.md) & [TECH_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/TECH_SPEC.md)  
**Last Updated:** 2026-11-02  

---

## 1. Design Philosophy & Aesthetic Direction

The design system for Olai Digital Studios embodies **Heritage & Craft**: a grounded, artisanal, and modern indie game studio aesthetic.

In Tamil culture, *Olai* (ஓலை) refers to the palm leaves historically used to inscribe manuscripts—symbolizing craftsmanship, deliberate structure, permanence, and timelessness. This direction bridges that cultural provenance with high-polish contemporary digital game design.

### Core Tenets
- **Warm Cinematic Contrast:** Replaces generic cold cyan-purple dark modes with deep Velvet Charcoal (`#0C0D0E`) and Warm Onyx (`#141518`) surfaces, establishing a tactile, filmic canvas that grounds key artwork.
- **Champagne Gold Accents:** Rich, warm Champagne Gold (`#E5B869`) and Warm Terracotta (`#E07A5F`) replace synthetic neon cyan, conveying prestige, craft, and human care.
- **Unobstructed Media Focus:** Game artwork is presented 100% clean—free of intrusive badges, text overlays, or artificial gradient scrims.
- **Distinctive Humanist Typography:** Confident, geometric display typography (**`Manrope`**) paired with high-clarity **`Plus Jakarta Sans`** interface copy provides an approachable yet authoritative studio presence.
- **Tactile Responsiveness (`transitions-dev`):** Every interactive element responds to user input via standardized motion tokens and reduced-motion guards.

---

## 2. Design Tokens

### 2.1 Color Palette

```
  Backgrounds (Warm Dark / Depth Scale)
  ┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
  │ Void #0C0D0E    │ Surface #141518 │ Elevated #1C1E22│ Highlight #26293 │
  └─────────────────┴─────────────────┴─────────────────┴─────────────────┘

  Foregrounds / Typography (Warm Stone Scale)
  ┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
  │ Ivory #FAFAF9   │ Stone-400 #A8A2 │ Stone-500 #7871 │ Border #292A2E  │
  └─────────────────┴─────────────────┴─────────────────┴─────────────────┘

  Accents & Status (Heritage Warmth)
  ┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
  │ Gold #E5B869    │ Terracotta #E07 │ Emerald #10B981 │ Amber #F59E0B   │
  └─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

#### Color Token Definitions

| Token Name | Hex Value | Usage / Semantic Role | Contrast vs Void (`#0C0D0E`) |
| :--- | :--- | :--- | :--- |
| `color-bg-void` | `#0C0D0E` | Deepest root viewport background (Velvet Charcoal) | — |
| `color-bg-surface` | `#141518` | Card surfaces, footer panel (Warm Onyx) | 1.15:1 |
| `color-bg-surface-elevated` | `#1C1E22` | Interactive hover states, elevated containers (Deep Basalt) | 1.35:1 |
| `color-bg-surface-highlight` | `#262930` | Selected states, active borders (Warm Slate) | 1.8:1 |
| `color-border-subtle` | `rgba(255, 255, 255, 0.08)` | Standard card and section divider borders | > 3:1 (structural) |
| `color-border-accent` | `rgba(229, 184, 105, 0.40)` | Interactive focus rings and card hover edges (Gold tint) | > 4.5:1 |
| `color-text-primary` | `#FAFAF9` (Stone 50) | Primary headlines, game titles, high-contrast text (Warm Ivory) | 17.5:1 (AAA) |
| `color-text-secondary` | `#A8A29E` (Stone 400) | Descriptions, subheadings, metadata (Warm Stone) | 8.8:1 (AAA) |
| `color-text-muted` | `#78716C` (Stone 500) | Copyright text, inactive labels, target platform tags | 5.2:1 (AA) |
| `color-accent-gold` | `#E5B869` | Primary action highlights, CTA glows, link hovers (Champagne Gold) | 11.4:1 (AAA) |
| `color-accent-terracotta`| `#E07A5F` | Gradient pairings, ambient radial glow aura (Warm Terracotta) | 6.8:1 (AAA) |
| `color-status-live` | `#10B981` (Emerald) | "Available Now" game badge indicator | 8.2:1 |
| `color-status-dev` | `#F59E0B` (Amber) | "In Development" game badge indicator | 9.9:1 |

---

### 2.2 Typography System

- **Studio Brand Mark (Hero):** **`Bodoni Moda`** (weights: `400`, `600`, `700`; optical sizing `6..96`; fallback `Georgia, serif`)
- **Display & Headings:** **`Manrope`** (fallback `system-ui, sans-serif`)
- **Body & Interface:** **`Plus Jakarta Sans`** (fallback `system-ui, sans-serif`)
- **Metadata & Badges:** **`Plus Jakarta Sans`** (refined geometric sans for genre tags, status pills, and location badges)

#### Type Hierarchy Scale

| Role | Size | Line Height | Weight | Letter Spacing | Element / Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Studio Wordmark** | 64px–120px / 4.0rem–7.5rem | 0.95 | 400 (Regular) | +0.12em (`mr-[-0.12em]`) | `h1.font-brand.uppercase` |
| **Studio Subtitle** | 20px–36px / 1.25rem–2.25rem | 1.00 | 400 (Regular) | +0.10em (`mr-[-0.10em]`) | `p.font-brand.uppercase` |
| **Section Title** | 30px / 1.875rem | 1.20 | 700 (Bold) | -0.01em | `h2.font-display` |
| **Game Title** | 22px / 1.375rem | 1.30 | 700 (Bold) | -0.01em | `h3.font-display.text-center` |
| **Genre / Status Pill** | 11px / 0.6875rem | 1.00 | 600 / 500 (Medium) | +0.05em (Caps) | `span.font-sans` |
| **Location Badge** | 12px–14px / 0.75rem–0.875rem | 1.20 | 500 (Medium) | 0.00em | `span.font-sans` |
| **Caption / Legal** | 12px / 0.75rem | 1.40 | 400 (Regular) | 0.00em | `p.text-xs` |

---

### 2.3 Motion & Timing Tokens (`transitions-dev` / `transitions-polish`)

Standardized CSS custom properties in `:root` and registered directly in Tailwind:

```css
:root {
  /* Durations */
  --duration-stagger: 40ms;
  --duration-micro: 80ms;
  --duration-quick: 150ms;
  --duration-fast: 250ms;
  --duration-medium: 350ms;
  --duration-slow: 400ms;
  --duration-very-slow: 500ms;

  /* Easings */
  --ease-smooth-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-spring-soft: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: ease-in-out;
  --ease-out: ease-out;

  /* Text Morph (33-text-morph.md) */
  --text-morph-dur: 180ms;
  --text-morph-resize-dur: 240ms;
  --text-morph-blur: 2px;
  --text-morph-ease: cubic-bezier(0.22, 1, 0.36, 1);
}
```

#### Reduced Motion Guard
```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto !important; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 3. Component Specifications

### 3.1 Hero Landing Screen (`Hero.astro`)
- **Structure:** Full-viewport (`min-h-screen flex flex-col justify-between`) canvas with no sticky header.
- **Atmospheric Background:** Pure velvet dark canvas (`bg-void #0C0D0E`), distraction-free.
- **Core Elements:**
  1. **Studio Wordmark:** Two-tier high-contrast Didone typography in **`Bodoni Moda`**:
     - Primary: **`OLAI`** (64px–120px) with `0.12em` tracking and `mr-[-0.12em]` optical center compensation.
     - Subtitle: **`DIGITAL STUDIOS`** (20px–36px) with `0.10em` tracking and `mr-[-0.10em]`.
  2. **Location Badge:** Frosted pill badge in `Plus Jakarta Sans` (`font-sans font-medium text-xs sm:text-sm`) with pulsating Champagne Gold indicator: **Based in Chennai, Tamil Nadu, India**.
  3. **Scroll Cue:** Bottom-anchored geometrically centered prompt in `font-sans font-medium uppercase tracking-[0.2em]` with `-0.2em` right margin compensation and bouncing chevron indicator: **Scroll to Explore ↓**.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                            OLAI                             │
│                       DIGITAL STUDIOS                       │
│                                                             │
│          [ ● Based in Chennai, Tamil Nadu, India ]          │
│                                                             │
│                                                             │
│                     ⌄ Scroll to Explore                     │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.2 Game Showcase Card (`GameCard.astro`)
- **Structure:** Unified vertical card (`h-full flex flex-col rounded-2xl bg-surface border border-white/10 overflow-hidden`).
- **Card Anatomy:**
  1. **100% Clean Key Art Frame (Top):**
     - 16:9 aspect ratio container (`aspect-video bg-black/60`).
     - Zero floating badges or text overlays over the artwork.
     - Ambient blurred background clone (`object-cover blur-xl scale-125 opacity-30`) fills the frame for non-16:9 assets.
     - Subtle zoom on card hover (`group-hover:scale-105 transition-transform duration-slow ease-smooth-out`).
  2. **Metadata Row (Body Top):**
     - Left: Single concise genre tag in `Plus Jakarta Sans` (`font-sans font-semibold uppercase tracking-wider text-[11px]`) in Champagne Gold.
     - Right: Release status pill in `font-sans font-medium text-[11px]` (`● Available Now` in emerald, `● In Development` in amber).
  3. **Centered Game Title (Body Center):**
     - Manrope bold text (`text-xl sm:text-2xl text-center text-white`) transitioning to Champagne Gold (`text-accent-gold`) on card hover.
     - Body tagline omitted to keep vertical heights tight and perfectly aligned.
  4. **4-Button Launcher Dock (Body Bottom, `mt-auto`):**
     - Centered row of 44×44px tactile icon tiles (`w-11 h-11 rounded-xl`).
     - **Live Games:** Active clickable tiles with hover lift (`-translate-y-0.5`), gold icon illumination (`text-accent-gold`, `border-accent-gold/40`, `bg-accent-gold/10`), tooltips, and accessibility labels.
     - **In-Development Games:** Explicitly labeled `"Planned on"` in `font-sans font-medium text-[11px]` with matching disabled icon tiles (`cursor-not-allowed`, `opacity-60`).

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                   100% CLEAN KEY ART                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  PUZZLE                                   ● AVAILABLE NOW   │
│                                                             │
│                        Zen Fourier                          │
│                                                             │
│             [ ▶ ]     [ ⊞ ]     [ 👾 ]     [ 🌐 ]           │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.3 Store Brand Vectors (`StoreIcon.astro`)
All brand icons are sourced directly from canonical **Simple Icons** (`simpleicons.org`):
- `google-play` $\rightarrow$ `googleplay`
- `microsoft-store` $\rightarrow$ `microsoftstore`
- `itch` $\rightarrow$ `itchdotio`
- `steam` $\rightarrow$ `steam`
- `app-store` $\rightarrow$ `appstore`
- `github` $\rightarrow$ `github`
- `web` $\rightarrow$ Clean SVG web globe

---

### 3.4 Footer & Contact Section (`Footer.astro`)
- **Structure:** Multi-column studio signature split seamlessly integrated with canvas (`border-t border-white/5 pt-16 pb-12 px-4 sm:px-6 lg:px-8`).
- **Main Split Row (`grid grid-cols-1 md:grid-cols-2 gap-10`):**
  1. **Left Column (Studio Identity):**
     - Brand signature in `Bodoni Moda`: **OLAI DIGITAL STUDIOS**.
     - Studio provenance statement: *Independent game development studio based in Chennai, Tamil Nadu, India.*
  2. **Right Column (Direct Inquiries & Interactive Email):**
     - Section label: `GET IN TOUCH` in Champagne Gold uppercase tracking.
     - Subtitle: `"For inquiries, partnerships, or feedback, drop us a line."`
     - Interactive Email Widget with **Text Morph Copy Button (`33-text-morph.md`)**: Smooth cross-blur transition from `"Copy"` to `"Copied!"` with container expansion and gold active state.
- **Bottom Sub-Footer Bar (`border-t border-white/5 pt-8 text-center`):**
  - Centered legal text: `© 2026 Olai Digital Studios. All rights reserved.`

---

## 4. Responsive Breakpoints & Adaptive Layout

| Viewport Breakpoint | Target Devices | Grid Layout & Structure |
| :--- | :--- | :--- |
| **Mobile (`< 640px`)** | iPhone, Android phones | Single column (`grid-cols-1`). Full-width cards. 44px min touch targets. |
| **Tablet (`640px - 1023px`)** | iPads, small laptops | Two-column grid (`sm:grid-cols-2 gap-6`). Row stretching with `h-full`. |
| **Desktop (`≥ 1024px`)** | Laptops, desktop monitors | Three-column grid (`lg:grid-cols-3 gap-8`). Full max-width container (`max-w-7xl`). |

---

## 5. Tailwind CSS Token Configuration (`tailwind.config.mjs`)

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        void: '#0C0D0E',
        surface: {
          DEFAULT: '#141518',
          elevated: '#1C1E22',
          highlight: '#262930'
        },
        accent: {
          gold: '#E5B869',
          terracotta: '#E07A5F',
          amber: '#F59E0B'
        }
      },
      fontFamily: {
        display: ['"Manrope"', 'system-ui', 'sans-serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        brand: ['"Bodoni Moda"', 'Georgia', 'serif']
      },
      boxShadow: {
        'glow-gold': '0 0 24px -4px rgba(229, 184, 105, 0.35)',
        'card-hover': '0 12px 30px -10px rgba(0, 0, 0, 0.8), 0 0 20px -5px rgba(229, 184, 105, 0.15)'
      },
      aspectRatio: {
        'card-art': '16 / 9'
      },
      transitionDuration: {
        stagger: 'var(--duration-stagger)',
        micro: 'var(--duration-micro)',
        quick: 'var(--duration-quick)',
        fast: 'var(--duration-fast)',
        medium: 'var(--duration-medium)',
        slow: 'var(--duration-slow)',
        'very-slow': 'var(--duration-very-slow)'
      },
      transitionTimingFunction: {
        'smooth-out': 'var(--ease-smooth-out)',
        'spring-soft': 'var(--ease-spring-soft)'
      }
    }
  },
  plugins: []
};
```
