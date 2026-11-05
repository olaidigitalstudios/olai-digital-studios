# Implementation Specification Document (ISD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.4.0 (Production Live & Monetized Implementation)  
**Status:** Live in Production  
**Live Production URL:** `https://olaidigitalstudios.netlify.app/`  
**Derived From:**  
- [PRODUCT_SPEC.md](file:///E:/olai-digital-studios/PRODUCT_SPEC.md) (v1.4.0)  
- [TECH_SPEC.md](file:///E:/olai-digital-studios/TECH_SPEC.md) (v1.4.0)  
- [DESIGN_SPEC.md](file:///E:/olai-digital-studios/DESIGN_SPEC.md) (v1.4.0)  
**Last Updated:** 2026-11-05  

---

## 1. Implementation Overview & Objectives

This document provides the definitive, file-by-file implementation blueprint, architecture patterns, and verification records for the Olai Digital Studios official portfolio website.

### Primary Objectives
- **Zero-Disruption AdMob Compliance:** Safely preserve the AdMob crawler file at `public/app-ads.txt` so that the SSG build output delivers `dist/app-ads.txt` with exact byte matching (`google.com, pub-4890313674539327, DIRECT, f08c47fec0942fa0`) and correct `text/plain; charset=utf-8` MIME type.
- **Reproducible Production Environment:** Define exact dependencies, TypeScript configurations, Tailwind theme bindings, Netlify build configurations, and Astro engine parameters.
- **Artisanal Floating UI Tooltip Architecture:** Implement a high-performance, collision-aware dark floating tooltip system (`Tooltip.astro`) with decoupled geometry to eliminate layout drift and zoom-scaling glitches.
- **Dual-Channel Studio Monetization:** Implement zero-server player support actions in `Footer.astro` combining Cashfree hosted UPI for Indian patrons and PayPal.me for global patrons.
- **Store & SEO Compliance:** Provide dedicated Google Play developer policy compliance (`/privacy`), Google Analytics 4 tracking (`G-QCEE9EZ1X0`), Google Search Console verification, and automated sitemap crawling.

---

## 2. Dependencies & Project Configuration

### 2.1 Package Manifest (`package.json`)
```json
{
  "name": "olai-digital-studios",
  "type": "module",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "astro": "astro",
    "check": "astro check"
  },
  "dependencies": {
    "@astrojs/check": "^0.9.4",
    "@astrojs/tailwind": "^5.1.5",
    "astro": "^4.16.18",
    "sharp": "^0.33.5",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.7.3"
  }
}
```

### 2.2 Astro Configuration (`astro.config.mjs`)
```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://olaidigitalstudios.netlify.app',
  base: '/',
  trailingSlash: 'never',
  integrations: [
    tailwind({
      applyBaseStyles: false
    })
  ],
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  }
});
```

### 2.3 Netlify Configuration (`netlify.toml`)
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/app-ads.txt"
  [headers.values]
    Content-Type = "text/plain; charset=utf-8"
```

### 2.4 TypeScript Configuration (`tsconfig.json`)
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "strictNullChecks": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@layouts/*": ["src/layouts/*"],
      "@assets/*": ["src/assets/*"]
    }
  }
}
```

### 2.5 Tailwind Configuration (`tailwind.config.mjs`)
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
        serif: ['"Bodoni Moda"', 'serif'],
        display: ['"Manrope"', 'system-ui', 'sans-serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif']
      },
      boxShadow: {
        'glow-gold': '0 0 24px -4px rgba(229, 184, 105, 0.35)',
        'card-hover': '0 12px 30px -10px rgba(0, 0, 0, 0.8), 0 0 20px -5px rgba(229, 184, 105, 0.15)'
      },
      aspectRatio: {
        'card-art': '16 / 9'
      }
    }
  },
  plugins: []
};
```

---

## 3. Complete File Manifest & Roles

```
.
├── netlify.toml                    # Netlify production build & app-ads.txt MIME header config
├── public/
│   ├── app-ads.txt                 # Canonical AdMob developer record (verified pub-4890313674539327)
│   ├── apple-touch-icon.png        # 180x180 iOS home-screen touch icon
│   ├── favicon.ico                 # Legacy browser fallback icon
│   ├── favicon.svg                 # Vector browser favicon mark
│   ├── og-banner.png               # 1200x630 Social sharing card
│   ├── robots.txt                  # Public crawler permissions & sitemap reference
│   └── sitemap.xml                 # Canonical XML sitemap for Netlify domain
├── src/
│   ├── assets/
│   │   ├── images/
│   │   │   └── games/              # Source key art images (.png, .webp, .jpg)
│   │   └── styles/
│   │       └── global.css          # Tailwind base, typography, motion tokens & tooltip styling
│   ├── components/
│   │   ├── Hero.astro              # Full-viewport screen with Bodoni Moda wordmark, location badge & scroll prompt
│   │   ├── GamesSection.astro      # Section container querying Astro content collection
│   │   ├── GameCard.astro          # Unobstructed 16:9 art, single genre in gold, centered title & 4-button launcher dock
│   │   ├── StoreIcon.astro         # Clean Simple Icons SVG platform marks (stripped of <title> tags)
│   │   ├── Tooltip.astro           # Artisanal unscaled floating tooltip engine with is-gliding transitions
│   │   └── Footer.astro            # Monetization dock (Cashfree & PayPal), Text Morph email copy, copyright
│   ├── content/
│   │   ├── config.ts               # Zod collection schema for game entries
│   │   └── games/                  # Data files (one JSON file per studio title)
│   │       ├── checkless.json
│   │       ├── countagram.json
│   │       ├── flapcrypt.json
│   │       ├── grid-leap.json
│   │       ├── node-attack.json
│   │       ├── rotatle.json
│   │       └── zen-fourier.json
│   ├── layouts/
│   │   └── BaseLayout.astro        # Master HTML shell, GA4, SEO, OpenGraph, JSON-LD & Tooltip mount
│   └── pages/
│       ├── index.astro             # Single-page layout composition (Hero + GamesSection + Footer)
│       └── privacy.astro           # Google Play Developer Policy compliant privacy policy
├── .gitignore                      # Standard Astro/Node ignore rules
├── astro.config.mjs                # Astro engine configuration (Netlify site URL)
├── package.json                    # Project dependencies and npm scripts
├── tailwind.config.mjs             # Tailwind design token configuration
├── tsconfig.json                   # TypeScript path aliases & strict rules
├── PRODUCT_SPEC.md                 # Product Specification Document (v1.4.0)
├── TECH_SPEC.md                    # Technical Specification Document (v1.4.0)
├── DESIGN_SPEC.md                  # Design Specification & System Document (v1.4.0)
└── IMPLEMENTATION_SPEC.md          # This implementation blueprint (v1.4.0)
```

---

## 4. Implementation Blueprint by Subsystem

### 4.1 Master Shell & Global Setup (`src/layouts/BaseLayout.astro`)
- **Google Analytics 4 Integration:** Embedded in `<head>` via `is:inline` directive:
  ```html
  <script is:inline async src="https://www.googletagmanager.com/gtag/js?id=G-QCEE9EZ1X0"></script>
  <script is:inline>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-QCEE9EZ1X0');
  </script>
  ```
- **SEO & Canonical Tags:** Injects `<link rel="canonical" href="https://olaidigitalstudios.netlify.app/">`, OpenGraph cards, Twitter preview metadata, and JSON-LD structured data (`Organization` and `VideoGameCollection`).
- **Global Tooltip Mount:** Mounts `<Tooltip />` once right before `</body>` to serve all hoverable elements across the application without DOM duplication.

### 4.2 Artisanal Floating Tooltip Engine (`src/components/Tooltip.astro`)
- **Decoupled Architecture:**
  - Outer `#app-tooltip`: Strictly manages coordinate positioning (`left`, `top`). Does not apply CSS `transform: scale()`, eliminating geometry recalculation errors and cross-screen fly-in glitches from `(0, 0)`.
  - Inner `.tooltip-bubble`: Handles visual rendering, background blur (`backdrop-blur-md`), typography (`Plus Jakarta Sans`), and scale animation (`scale(0.96)` to `scale(1)`).
- **Coordinate Precision:** Calculates target boundaries relative to `window.pageXOffset` / `window.pageYOffset` and uncouples any CSS scale transformations applied to hovered cards.
- **Gliding Interpolation (`is-gliding`):**
  - First hover: Activates after a 120ms intention delay with silent positioning snap (no travel animation).
  - Hovering between adjacent sibling buttons: Enters `.is-gliding` state with a 150ms `cubic-bezier(0.16, 1, 0.3, 1)` transition on `left` and `top`, smoothly gliding between controls without flicker.
  - Hover exit: Fades out in 80ms (`opacity: 0`).
- **Collision Detection & Viewport Clamping:** Automatically evaluates viewport bounds. If a tooltip placed at `top` overflows the viewport ceiling, it flips to `bottom`. Supports explicit overrides via `data-tooltip-placement="bottom"`.
- **Keyboard & Accessibility Support:** Binds to `pointerenter`/`pointerleave` as well as `focusin`/`focusout`. Closes instantly on `Escape`.

### 4.3 Clean Vector Store Launcher Dock (`src/components/StoreIcon.astro` & `GameCard.astro`)
- **OS Tooltip Suppression:** All SVG `<title>` elements removed from `StoreIcon.astro`. SVGs marked with `aria-hidden="true"`.
- **Accessible Tooltip Binding:** Anchors and buttons declare both accessible `aria-label` and visual `data-tooltip` attributes.
- **Contextual Copy Generation:**
  - Live Web build: `"Play on Web"`
  - Planned Web build: `"Web — Planned"`
  - Active platform store link: `"Get on [Platform]"`
  - In-development store target: `"[Platform] — Planned"`
- **Placement Override:** Game card store links enforce `data-tooltip-placement="bottom"` to prevent the tooltip from obscuring the game title located above the launcher dock.

### 4.4 Studio Monetization Dock (`src/components/Footer.astro`)
- **"Support Our Craft" Interface:** Built as a dedicated community support tier directly above the legal copyright bar.
- **Cashfree Hosted Payment Form:**
  - URL: `https://payments.cashfree.com/forms/support-olai`
  - Targets domestic Indian supporters with zero server-side maintenance.
  - Supports instant UPI (Google Pay, PhonePe, Paytm, BHIM), RuPay cards, and domestic net banking.
  - Decorated with UPI vector mark and tooltip: `"Contribute via UPI, GPay, PhonePe or Cards (India)"` (`data-tooltip-placement="bottom"`).
- **PayPal.me International Link:**
  - URL: `https://paypal.me/olaidigitalstudios`
  - Targets global/cross-border patrons.
  - Handled via PayPal India with Purpose Code `P0802` daily auto-sweeps to Indian bank accounts.
  - Decorated with PayPal mark and tooltip: `"Support internationally via PayPal or Card"` (`data-tooltip-placement="bottom"`).
- **Text Morph Copy Micro-Interaction:** Contact email button morphs from `"Copy"` to `"✓ Copied!"` using `transitions-dev 33-text-morph` with Champagne Gold feedback and ARIA live regions.

### 4.5 Store Compliance Privacy Endpoint (`src/pages/privacy.astro`)
- Dedicated Google Play Developer policy-compliant page.
- Establishes zero personal identifiable information (PII) harvesting.
- Outlines third-party ad network policies (Google AdMob), child privacy compliance (COPPA), and contact mechanisms (`olaidigitalstudios@gmail.com`).

---

## 5. Step-by-Step Implementation & Verification Roadmap

```
┌────────────────────────────────────────────────────────┐
│ Phase 1: Environment & Tooling Scaffolding             │ [COMPLETED]
│ - package.json, astro.config.mjs, tailwind.config.mjs  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 2: Static Asset Relocation & AdMob Verification  │ [COMPLETED]
│ - public/app-ads.txt, sitemap.xml, robots.txt, icons   │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 3: Content Collection & Schema Validation        │ [COMPLETED]
│ - src/content/config.ts with Zod, 7 game data files    │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 4: Master Layout, Design Tokens & Analytics      │ [COMPLETED]
│ - global.css, BaseLayout.astro, GA4 G-QCEE9EZ1X0       │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 5: Component Implementations & Interactions      │ [COMPLETED]
│ - Hero, GameCard, StoreIcon, Tooltip, Footer           │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 6: Privacy Policy & Compliance Route             │ [COMPLETED]
│ - src/pages/privacy.astro with Google Play compliance  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 7: Netlify Build & Production Deployment         │ [COMPLETED]
│ - netlify.toml, edge CDN, zero-error static compilation│
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 8: Quality Gates & Verification Testing          │ [COMPLETED]
│ - TypeScript check, AdMob validation, tooltip audit    │
└────────────────────────────────────────────────────────┘
```

---

## 6. Security, Compliance & Risk Mitigations

| Risk | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **`app-ads.txt` missing or corrupted** | Critical (AdMob crawler fails verification, ad revenue ceases) | Placed directly in `public/app-ads.txt`. Verified byte-by-byte (`pub-4890313674539327`). Netlify headers config forces `text/plain; charset=utf-8`. |
| **Payment security / PCI liability** | High (Regulatory penalties or data compromise) | Zero customer financial data touches the studio server. Cashfree handles domestic UPI/cards on their PCI-DSS Level 1 certified hosted form; PayPal handles international payments on their secure checkout. |
| **Foreign Exchange compliance (India)** | Moderate (Account freeze or RBI compliance inquiry) | PayPal account configured under export purpose code `P0802` (Software & Gaming Services), allowing RBI auto-repatriation to the registered Indian bank account. |
| **Browser native tooltip collisions** | Low (Clunky double tooltips on hover) | Removed all `<title>` elements from SVGs in `StoreIcon.astro`. Kept accessible `aria-label` on buttons and hooked into the custom `#app-tooltip`. |
| **Tooltip positioning drift during card hover** | Low (Visual jank / flying tooltips) | Decoupled the outer positioning container (`#app-tooltip`) from scale transitions and calculated unscaled target dimensions. |

---

## 7. Execution Readiness & Sign-Off Checklist

- [x] **Product Specification** finalized and approved ([PRODUCT_SPEC.md](file:///E:/olai-digital-studios/PRODUCT_SPEC.md) v1.4.0).
- [x] **Technical Specification** finalized and approved ([TECH_SPEC.md](file:///E:/olai-digital-studios/TECH_SPEC.md) v1.4.0).
- [x] **Design Specification & Tokens** finalized and approved ([DESIGN_SPEC.md](file:///E:/olai-digital-studios/DESIGN_SPEC.md) v1.4.0).
- [x] **Implementation Blueprint** fully synchronized and verified ([IMPLEMENTATION_SPEC.md](file:///E:/olai-digital-studios/IMPLEMENTATION_SPEC.md) v1.4.0).
- [x] **Production Verification:** Zero Astro/TypeScript check errors, zero build errors, all 7 catalog games rendering cleanly, AdMob crawler file live at `/app-ads.txt`, monetization forms operational.
