# Implementation Specification Document (ISD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.3.0  
**Status:** Approved for Implementation  
**Derived From:**  
- [PRODUCT_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/PRODUCT_SPEC.md) (v1.3.0)  
- [TECH_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/TECH_SPEC.md) (v1.3.0)  
- [DESIGN_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/DESIGN_SPEC.md) (v1.3.0)  
**Last Updated:** 2026-11-02  

---

## 1. Implementation Overview & Objectives

This document provides the concrete, file-by-file blueprint and execution roadmap for building the Olai Digital Studios official portfolio website.

### Primary Objectives
- **Zero-Disruption Migration:** Safely reposition the existing AdMob [app-ads.txt](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/app-ads.txt) into `public/app-ads.txt` so that the build output delivers it untouched at `/app-ads.txt`.
- **Reproducible Build Environment:** Define exact dependencies, TypeScript configurations, Tailwind theme bindings, and Astro configuration files.
- **Structured Phased Execution:** Provide a sequential, step-by-step roadmap that can be executed and verified iteratively.

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
  site: 'https://dhineshmoorthy-gamedev.github.io',
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

### 2.3 TypeScript Configuration (`tsconfig.json`)
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

### 2.4 Tailwind Configuration (`tailwind.config.mjs`)
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
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD: Automated build & deploy to GitHub Pages
├── public/
│   ├── app-ads.txt                 # Relocated AdMob record (copied untouched to dist/)
│   ├── favicon.svg                 # Vector browser favicon mark
│   └── robots.txt                  # Public crawler permissions
├── src/
│   ├── assets/
│   │   ├── images/
│   │   │   ├── logo.svg            # Studio vector mark & typography
│   │   │   ├── og-banner.png       # 1200x630 Social sharing card
│   │   │   └── games/              # Source key art images (.png, .webp, .jpg)
│   │   └── styles/
│   │       └── global.css          # Tailwind base, typography & motion tokens
│   ├── components/
│   │   ├── Hero.astro              # Full-viewport screen with Bodoni Moda wordmark, location badge & scroll prompt
│   │   ├── GamesSection.astro      # Section container querying Astro content collection
│   │   ├── GameCard.astro          # Unobstructed 16:9 art, single genre in gold, centered title & 4-button launcher dock
│   │   ├── StoreIcon.astro         # Canonical Simple Icons SVG platform marks
│   │   └── Footer.astro            # Inquiries copy, Text Morph email copy micro-script, copyright
│   ├── content/
│   │   ├── config.ts               # Zod collection schema for game entries
│   │   └── games/                  # Data files (one JSON file per game)
│   │       ├── orbital-drift.json
│   │       ├── checkless.json
│   │       ├── countagram.json
│   │       ├── flapcrypt.json
│   │       ├── grid-leap.json
│   │       ├── rotatle.json
│   │       └── shadow-grid.json
│   ├── layouts/
│   │   └── BaseLayout.astro        # Master HTML shell, SEO, OpenGraph & JSON-LD
│   └── pages/
│       └── index.astro             # Single-page layout composition (Hero + GamesSection + Footer)
├── .gitignore                      # Standard Astro/Node ignore rules
├── astro.config.mjs                # Astro engine configuration
├── package.json                    # Project dependencies and npm scripts
├── tailwind.config.mjs             # Tailwind design token configuration (Direction 4: Heritage & Craft)
├── tsconfig.json                   # TypeScript path aliases & strict rules
├── PRODUCT_SPEC.md                 # Product Specification Document (v1.3.0)
├── TECH_SPEC.md                    # Technical Specification Document (v1.3.0)
├── DESIGN_SPEC.md                  # Design Specification & System Document (v1.3.0)
└── IMPLEMENTATION_SPEC.md          # This implementation blueprint (v1.3.0)
```

---

## 4. Step-by-Step Implementation Roadmap

```
┌────────────────────────────────────────────────────────┐
│ Phase 1: Environment & Tooling Scaffolding             │
│ - package.json, astro.config.mjs, tailwind.config.mjs  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 2: Static Asset Relocation & AdMob Verification  │
│ - Move app-ads.txt to public/, create robots.txt/svg   │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 3: Content Collection & Schema Validation        │
│ - src/content/config.ts with Zod, sample-game.json     │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 4: Design Tokens & Layout Skeleton               │
│ - global.css, Google Fonts import, BaseLayout.astro    │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 5: Component Implementations                     │
│ - Header, Hero, GameCard, GamesSection, Footer         │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 6: Single-Page Composition (index.astro)         │
│ - Wire components, test responsive layout              │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 7: GitHub Actions CI/CD Pipeline                 │
│ - .github/workflows/deploy.yml with dist validation   │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│ Phase 8: Quality Gates & Production Verification       │
│ - Local build test, curl app-ads.txt, Lighthouse test  │
└────────────────────────────────────────────────────────┘
```

---

### Phase 1: Environment & Tooling Scaffolding
1. Create `package.json` with exact versions specified in Section 2.1.
2. Create `astro.config.mjs`, `tailwind.config.mjs`, and `tsconfig.json`.
3. Create `.gitignore` ignoring:
   - `node_modules/`
   - `dist/`
   - `.astro/`
   - `.DS_Store`
4. Run `npm install` to resolve and lock dependencies.

### Phase 2: Static Asset Relocation & AdMob Verification
1. Create directory `public/`.
2. Move root `app-ads.txt` into `public/app-ads.txt`.
3. Verify byte integrity of `public/app-ads.txt` (`pub-4890313674539327`).
4. Add `public/robots.txt`:
   ```txt
   User-agent: *
   Allow: /
   ```
5. Add vector `public/favicon.svg` matching studio aesthetic.

### Phase 3: Content Collection & Schema Validation
1. Create `src/content/config.ts` enforcing the Zod schema defined in [TECH_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/TECH_SPEC.md#L94-L125).
2. Create directory `src/assets/images/games/` for source key art.
3. Create `src/content/games/sample-game.json` with realistic seed data to test the rendering pipeline before real catalog data is inserted.

### Phase 4: Design Tokens & Master Layout
1. Create `src/assets/styles/global.css`:
   - Import fonts (`Space Grotesk` and `Inter` via `@fontsource` or Google Fonts `<link>` in layout).
   - Inject `@tailwind base;`, `@tailwind components;`, `@tailwind utilities;`.
   - Set smooth scrolling on `html`:
     ```css
     html {
       scroll-behavior: smooth;
       background-color: #08090C;
       color: #F3F4F6;
     }
     ```
2. Create `src/layouts/BaseLayout.astro`:
   - Inject SEO `<title>`, `<meta name="description">`.
   - Inject OpenGraph and Twitter card `<meta>` tags.
   - Inject JSON-LD `Organization` schema.
   - Slot default body contents.

### Phase 5: Component Implementations

#### 1. `Hero.astro`
- Full-viewport screen (`min-h-screen`) centered layout on pure dark velvet canvas (`#0C0D0E`).
- Two-tier studio wordmark in high-contrast Didone serif (**`Bodoni Moda`**): **OLAI** primary with **DIGITAL STUDIOS** subtitle, incorporating negative right margin compensation for true geometric center.
- Frosted geographic badge in **`Plus Jakarta Sans`**: `Based in Chennai, Tamil Nadu, India` with pulsating Champagne Gold indicator (`bg-white/5 border border-white/10 px-4 py-1.5 rounded-full backdrop-blur-md`).
- Geometrically centered bouncing scroll prompt (`Scroll to Explore` with downward arrow linking to `#games`) in **`Plus Jakarta Sans`** with optical letter-spacing compensation.
- Zero header, zero logo mark, zero generic taglines, zero primary buttons.

#### 2. `GameCard.astro`
- Unobstructed 16:9 art frame (`aspect-video rounded-xl overflow-hidden`) with zero badges, text overlays, or dark scrims over the art.
- Dynamic atmospheric background blur (`object-cover blur-2xl scale-110 opacity-30`) paired with sharp foreground key art (`object-contain`).
- Clean metadata row below image in **`Plus Jakarta Sans`**: single concise genre pill in Champagne Gold (`Puzzle`, `Strategy`, `Word Puzzle`) and live status dot (`Available Now` vs `In Development`).
- Centered bold title (**`Manrope`** 700 text transitioning to Champagne Gold on card hover). Tagline removed.
- Centered 4-button launcher dock:
  - Active games: interactive buttons styled with `bg-surface-elevated/80 border border-white/10 hover:border-accent-gold hover:bg-white/10` with tooltip labels.
  - In-development games: labeled `Planned on` in **`Plus Jakarta Sans`**, buttons rendered with `opacity-60 cursor-not-allowed select-none`.

#### 3. `StoreIcon.astro`
- Renders canonical vector SVGs sourced directly from official **Simple Icons**:
  - `google-play` / `googleplay`
  - `microsoft-store` / `microsoftstore`
  - `itch` / `itchdotio`
  - `web` (crisp globe vector)
  - `steam`
  - `app-store`

#### 4. `GamesSection.astro`
- Section wrapper with `id="games"`.
- Fetches all games via `await getCollection('games')` and sorts by `featuredOrder`.
- Renders responsive grid: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8` with stretch column cards (`h-full flex flex-col`).

#### 5. `Footer.astro`
- Section container with `id="contact"`.
- Studio contact email display with updated copy: *"For inquiries, partnerships, or feedback, drop us a line."*
- Character-diff Text Morph clipboard interaction (`transitions-dev 33-text-morph`) morphing `Copy` into `✓ Copied!` with Champagne Gold visual feedback and accessible ARIA live feedback.
- Outbound developer links and copyright notice: `© 2026 Olai Digital Studios. All rights reserved.`.

### Phase 6: Single-Page Composition
1. Create `src/pages/index.astro`:
   ```astro
   ---
   import BaseLayout from '@layouts/BaseLayout.astro';
   import Hero from '@components/Hero.astro';
   import GamesSection from '@components/GamesSection.astro';
   import Footer from '@components/Footer.astro';
   ---
   <BaseLayout title="Olai Digital Studios | Independent Game Studio">
     <main>
       <Hero />
       <GamesSection />
     </main>
     <Footer />
   </BaseLayout>
   ```
2. Verify responsive layout across mobile (375px), tablet (768px), and desktop (1440px).

### Phase 7: GitHub Actions CI/CD Pipeline
1. Create directory `.github/workflows/`.
2. Create `.github/workflows/deploy.yml` with the exact workflow defined in [TECH_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/TECH_SPEC.md#L187-L232).
3. Include the pre-deployment verification step:
   ```yaml
   - name: Verify app-ads.txt in build output
     run: test -f dist/app-ads.txt || (echo "Missing app-ads.txt in dist!" && exit 1)
   ```

### Phase 8: Quality Gates & Verification Testing
1. Run `npm run check` to verify TypeScript and Astro schema integrity (0 errors, 0 warnings).
2. Run `npm run build` to verify clean build generation in `dist/` (0 errors, static HTML + Sharp WebP assets generated).
3. Inspect `dist/app-ads.txt` to verify exact matching content with the original file (`google.com, pub-4890313674539327, DIRECT, f08c47fec0942fa0`).
4. Outbound link verification: all live platform links tested including Netlify web demos.

---

## 5. Risk Assessment & Mitigations

| Risk | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **`app-ads.txt` accidentally excluded from build** | Critical (AdMob crawler fails verification, ad revenue halts) | Placed directly in `public/app-ads.txt`. CI/CD workflow contains an explicit assertion step (`test -f dist/app-ads.txt`) that aborts the deployment if missing. |
| **Missing image or broken URL in game data** | Moderate (Broken UI) | Zod schema validation in `src/content/config.ts` fails the build at compile time if an image doesn't exist or a URL is malformed. |
| **Clipboard API blocked in non-HTTPS / restricted contexts** | Low (Copy button fails silently) | Micro-script includes a `try/catch` block with fallback to `document.execCommand('copy')`. |
| **Cumulative Layout Shift from unoptimized key art** | Low (SEO/Performance penalty) | Astro's `<Image />` component automatically sets intrinsic `width` and `height` dimensions and compiles images to WebP. |

---

## 6. Execution Readiness Checklist

- [x] **Product Specification** finalized and approved ([PRODUCT_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/PRODUCT_SPEC.md)).
- [x] **Technical Specification** finalized and approved ([TECH_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/TECH_SPEC.md)).
- [x] **Design Specification & Tokens** finalized and approved ([DESIGN_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/DESIGN_SPEC.md)).
- [x] **Implementation Roadmap** documented with exact dependencies and file manifest ([IMPLEMENTATION_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/IMPLEMENTATION_SPEC.md)).
- [x] **Implementation Execution:** All phases (1 through 8) fully implemented and verified with zero errors. Build output and AdMob compliance confirmed.
