# Design Specification & Design System
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.4.0 (Heritage & Craft Design System)  
**Status:** Live in Production  
**Live Production URL:** `https://olaidigitalstudios.netlify.app/`  
**Derived From:** [PRODUCT_SPEC.md](file:///E:/olai-digital-studios/PRODUCT_SPEC.md) & [TECH_SPEC.md](file:///E:/olai-digital-studios/TECH_SPEC.md)  
**Last Updated:** 2026-11-05  

---

## 1. Design Philosophy & Aesthetic Direction

The design system for Olai Digital Studios embodies **Heritage & Craft**: a grounded, artisanal, and modern indie game studio aesthetic.

In Tamil culture, *Olai* (ஓலை) refers to the palm leaves historically used to inscribe manuscripts—symbolizing craftsmanship, deliberate structure, permanence, and timelessness. This direction bridges that cultural provenance with high-polish contemporary digital game design.

### Core Tenets
- **Warm Cinematic Contrast:** Replaces generic cold cyan-purple dark modes with deep Velvet Charcoal (`#0C0D0E`) and Warm Onyx (`#141518`) surfaces, establishing a tactile, filmic canvas that grounds key artwork.
- **Champagne Gold Accents:** Rich, warm Champagne Gold (`#E5B869`) and Warm Terracotta (`#E07A5F`) replace synthetic neon cyan, conveying prestige, craft, and human care.
- **Unobstructed Media Focus:** Game artwork is presented 100% clean—free of intrusive badges, text overlays, or artificial gradient scrims.
- **Distinctive Humanist Typography:** Confident, geometric display typography (**`Manrope`**) paired with high-clarity **`Plus Jakarta Sans`** interface copy and prestigious Didone display headlines (**`Bodoni Moda`**).
- **Tactile Responsiveness (`transitions-dev`):** Every interactive element responds to user input via standardized motion tokens, collision-aware tooltips, and reduced-motion guards.

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

| Token Name | Hex / RGBA Value | Usage / Semantic Role | Contrast vs Void (`#0C0D0E`) |
| :--- | :--- | :--- | :--- |
| `color-bg-void` | `#0C0D0E` | Deepest root viewport background (Velvet Charcoal) | — |
| `color-bg-surface` | `#141518` | Card surfaces, footer panel (Warm Onyx) | 1.15:1 |
| `color-bg-surface-elevated`| `#1C1E22` | Interactive hover states, elevated containers, widgets (Deep Basalt) | 1.35:1 |
| `color-bg-surface-highlight`| `#262930` | Active borders, scrollbar thumbs (Warm Slate) | 1.8:1 |
| `color-border-subtle` | `rgba(255, 255, 255, 0.08)` | Standard card and section divider borders | > 3:1 (structural) |
| `color-border-accent` | `rgba(229, 184, 105, 0.25)` | Specular highlights, tooltip borders, card hover edges (Gold tint) | > 4.5:1 |
| `color-text-primary` | `#FAFAF9` (Stone 50) | Primary headlines, game titles, high-contrast text (Warm Ivory) | 17.5:1 (AAA) |
| `color-text-secondary` | `#A8A29E` (Stone 400) | Descriptions, subheadings, metadata (Warm Stone) | 8.8:1 (AAA) |
| `color-text-muted` | `#78716C` (Stone 500) | Copyright text, inactive labels, target platform tags | 5.2:1 (AA) |
| `color-accent-gold` | `#E5B869` | Primary action highlights, CTA glows, link hovers (Champagne Gold) | 11.4:1 (AAA) |
| `color-accent-terracotta`| `#E07A5F` | Gradient pairings, ambient radial glow aura (Warm Terracotta) | 6.8:1 (AAA) |
| `color-status-live` | `#10B981` (Emerald) | "Available Now" game badge indicator, active UPI payment node | 8.2:1 |
| `color-status-dev` | `#F59E0B` (Amber) | "In Development" game badge indicator | 9.9:1 |

---

### 2.2 Typography System

- **Studio Brand Mark (Hero & Footer):** **`Bodoni Moda`** (weights: `300..700`; optical sizing `6..96`; fallback `Georgia, serif`)
- **Display & Headings:** **`Manrope`** (weights: `600`, `700`, `800`; fallback `system-ui, sans-serif`)
- **Body & Interface:** **`Plus Jakarta Sans`** (weights: `400`, `500`, `600`; fallback `system-ui, sans-serif`)
- **Metadata, Badges & Tooltips:** **`Plus Jakarta Sans`** (refined geometric sans for genre tags, status pills, and tooltips)

#### Type Hierarchy Scale

| Role | Size | Line Height | Weight | Letter Spacing | Element / Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Studio Wordmark** | 64px–128px / 4.0rem–8.0rem | 0.95 | 400 (Regular) | +0.12em (`mr-[-0.12em]`) | `h1.font-brand.uppercase` |
| **Studio Subtitle** | 18px–36px / 1.125rem–2.25rem | 1.00 | 400 (Regular) | +0.10em (`mr-[-0.10em]`) | `p.font-brand.uppercase` |
| **Section Title** | 28px–32px / 1.75rem–2.0rem | 1.20 | 700 (Bold) | -0.01em | `h2.font-display` |
| **Game Title** | 20px–24px / 1.25rem–1.5rem | 1.30 | 700 (Bold) | -0.01em | `h3.font-display.text-center` |
| **Genre / Status Pill** | 11px / 0.6875rem | 1.00 | 600 / 500 (Medium) | +0.05em (Caps) | `span.font-sans` |
| **Tooltip Text** | 11px–12px / 0.6875rem–0.75rem| 1.20 | 500 (Medium) | +0.02em | `span#app-tooltip-text` |
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

## 3. Component Design Specifications

### 3.1 Hero Landing Screen (`Hero.astro`)
- **Structure:** Full-viewport (`min-h-screen flex flex-col justify-between`) edge-to-edge canvas with no sticky header.
- **Ambient Constellation Canvas:** Background `<canvas>` with sacred geometry, floating golden micro-nodes, and proximity hairline connections reacting gently to mouse movement. Managed via `IntersectionObserver` to pause render loop off-screen.
- **Breathing Studio Aura:** Subtle radial gradient glow centered behind the brandmark cycling softly on an 11s loop.
- **Studio Typography:** `Bodoni Moda` Didone lettering with optical right-margin compensation:
  - Primary: **`OLAI`** (text-6xl to text-9xl)
  - Subtitle: **`DIGITAL STUDIOS`** (text-lg to text-4xl)
- **Location Badge:** Frosted pill badge in `Plus Jakarta Sans` with pulsating Champagne Gold indicator: **`Based in Chennai, Tamil Nadu, India`**.
- **Scroll Cue:** Bottom-anchored prompt (**`Scroll to Explore`** ↓) with subtle bounce animation and custom tooltip.

---

### 3.2 Game Showcase Card (`GameCard.astro`)
- **Structure:** Obsidian vertical card (`h-full flex flex-col rounded-2xl bg-gradient-to-b from-surface-elevated/40 via-surface to-surface border-t border-t-white/20 border-x border-x-white/10 border-b border-b-white/10 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.14),0_8px_24px_-8px_rgba(0,0,0,0.6)] overflow-hidden`).
- **Card Anatomy:**
  1. **Clean Key Art Frame (Top):** 16:9 aspect ratio (`aspect-video bg-black/60`). 100% clean art with zero overlays. Non-16:9 images feature an ambient blurred background clone so art is never clipped.
  2. **Metadata Row:** Single concise genre in Champagne Gold uppercase tracking positioned opposite a release status pill (`● Available Now` in emerald, `● In Development` in amber).
  3. **Centered Game Title:** High-contrast, bold display title in `Manrope` centered within the card body.
  4. **Centered Store Launcher Dock (Bottom):**
     - Centered row of 44×44px tactile icon tiles (`w-11 h-11 rounded-xl`).
     - **Live Games:** Active clickable tiles with hover lift (`-translate-y-0.5`), gold illumination (`text-accent-gold`, `border-accent-gold/40`, `bg-accent-gold/10`).
     - **Tooltips:** Enforced `data-tooltip-placement="bottom"`. Displays **`Play on Web`** for browser editions, **`Get on [Platform]`** for store editions.
     - **In-Development Games:** Explicitly labeled `"Planned on"` with matching disabled icon tiles (`cursor-not-allowed`, `select-none`, `opacity-60`). Tooltips read **`[Platform] — Planned`** (including **`Web — Planned`**).

---

### 3.3 Custom Tooltip System (`Tooltip.astro`)
- **Structure:** Global singleton `#app-tooltip` mounted at root coordinates.
- **Aesthetic Styling:**
  - Surface: `bg-[#141518]/95` with `backdrop-filter: blur(12px)`.
  - Border: Hairline `1px solid rgba(229, 184, 105, 0.25)` (Warm Champagne Gold).
  - Specular Highlight: 1px top line `linear-gradient(90deg, transparent, rgba(229, 184, 105, 0.40), transparent)`.
  - Shadow: `0 8px 24px -4px rgba(0,0,0,0.8), 0 0 12px rgba(229,184,105,0.12)`.
  - Typography: `font-sans text-[11px] sm:text-xs font-medium text-stone-200 tracking-wide`.
  - Caret / Arrow: 8×8px diamond rotated 45deg with matching fill and subtle gold border.
- **Motion & Collision Engine:**
  - Geometry is completely decoupled from visual entrance to prevent scale distortion.
  - Silent coordinate snap on first hover eliminates any "flying from (0, 0)" effect.
  - Smooth coordinate gliding (`is-gliding`, 150ms) is active only when scrubbing between adjacent buttons.
  - Defaults to `data-placement="bottom"` on game cards so titles are never covered. Automatically flips to `top` if near the bottom viewport edge.
  - Suppressed on touch screens (`@media (hover: none)`); fully accessible via keyboard `Tab` and `Escape`.

---

### 3.4 Studio Footer & Monetization Hub (`Footer.astro`)
- **Multi-Column Studio Signature Split (`md:grid-cols-2`):**
  1. **Left Column:** `Bodoni Moda` wordmark with studio provenance statement.
  2. **Right Column:** Section label `GET IN TOUCH`, subtitle copy, interactive email copy widget, and dual-channel support hub.
- **Interactive Email Copy Widget:** Email address with Text Morph button (`"Copy"` $\rightarrow$ `"Copied!"` $\rightarrow$ `"Copy"` after 2.5s) using `transitions-dev` character-diff morphing and gold active highlight.
- **Dual-Channel Monetization Hub ("Support Our Craft"):**
  - **Domestic UPI Button:** Capsule badge (`px-3.5 py-2 rounded-xl bg-surface-elevated border border-white/10`) featuring an emerald active pulse dot, reading **`UPI / India (₹)`**, linking to Cashfree hosted checkout. Tooltip: *"Instant support via UPI, GPay, PhonePe or Cards"*.
  - **International PayPal Button:** Matching capsule badge featuring gold PayPal monogram, reading **`PayPal / Global ($)`**, linking to `paypal.me/olaidigitalstudios`. Tooltip: *"International support via PayPal, Cards or Balance"*.
  - Both tooltips anchor cleanly to `data-tooltip-placement="bottom"`.
- **Sub-Footer Bar:** Studio copyright text and direct link to `/privacy`.

---

### 3.5 Privacy Policy Page (`privacy.astro`)
- Dedicated standalone legal policy styled with the same dark luxury aesthetics (`bg-void #0C0D0E`, `bg-surface #141518`, warm stone typography).
- Quiet legal sub-footer with clean return link to studio home (`← Return to Studio Home`).

---

## 4. Responsive Breakpoints & Adaptive Layout

| Viewport Breakpoint | Target Devices | Grid Layout & Structure |
| :--- | :--- | :--- |
| **Mobile (`< 640px`)** | iPhone, Android phones | Single column (`grid-cols-1`). Full-width cards. 44px min touch targets. Hover effects disabled on touch (`hoverOnlyWhenSupported`). |
| **Tablet (`640px - 1023px`)** | iPads, small laptops | Two-column grid (`sm:grid-cols-2 gap-6`). Row stretching with `h-full`. |
| **Desktop (`≥ 1024px`)** | Laptops, desktop monitors | Three-column grid (`lg:grid-cols-3 gap-8`). Full max-width container (`max-w-7xl`). |

---

## 5. Tailwind CSS Token Configuration (`tailwind.config.mjs`)

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  future: {
    hoverOnlyWhenSupported: true
  },
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
