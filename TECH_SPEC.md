# Technical Specification Document (TSD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.4.0 (Production Live & Monetized Architecture)  
**Status:** Live in Production  
**Live Production URL:** `https://olaidigitalstudios.netlify.app/`  
**Derived From:** [PRODUCT_SPEC.md](file:///E:/olai-digital-studios/PRODUCT_SPEC.md) (v1.4.0)  
**Last Updated:** 2026-11-05  

---

## 1. Technical Overview & Architectural Principles

The Olai Digital Studios website is architected as an ultra-fast, zero-runtime-overhead Static Site Generation (SSG) web application deployed natively on Netlify.

```
┌────────────────────────────────────────────────────────┐
│                   Development / Build                  │
│                                                        │
│  src/content/games/ ──┐                                │
│      (JSON / Zod)     │                                │
│                       ▼                                │
│  src/components/  ──► [ Astro Core (Vite Engine) ]     │
│  src/layouts/         │                                │
│  src/assets/          ▼                                │
│  public/          ──► [ Build Output: dist/ ]          │
│                       ├── index.html                   │
│                       ├── privacy/index.html           │
│                       ├── app-ads.txt                  │
│                       └── sitemap.xml                  │
└───────────────────────┼────────────────────────────────┘
                        │
                        ▼ (Git Push to master / Netlify Webhook)
┌────────────────────────────────────────────────────────┐
│                 Hosting & Edge Delivery                │
│                                                        │
│                 Netlify Edge Network (CDN)             │
│                           │                            │
│           ┌───────────────┼───────────────┐            │
│           ▼               ▼               ▼            │
│  Browsers             AdMob Crawler   Search Engines   │
│  (Pure Static HTML)   (GET /app-ads)  (GET /sitemap)   │
│  - GA4 Telemetry      - 200 OK text   - 200 OK xml     │
│  - Floating Tooltip   - pub-4890...   - Canonical URLs │
└────────────────────────────────────────────────────────┘
```

### Architectural Principles
- **Static First (0kb JS Framework by Default):** All HTML and CSS are pre-rendered at compile time. No client-side framework runtime (no React, Vue, or Angular bundle overhead) is delivered to the browser.
- **Type-Safe Content Modeling:** Game catalog entries are defined as structured data files validated at build-time with Zod schemas (`astro:content`). Any invalid URL, missing banner image, or typo breaks the build immediately with actionable error messages.
- **Root Compliance Preservation:** The AdMob `app-ads.txt` is served directly from the root of the domain as an unbundled, untransformed static asset with HTTP 200 and `text/plain` MIME type.
- **Dual-Channel Zero-Server Monetization:** Studio support links (Cashfree UPI & PayPal) operate via secure, pre-validated hosted checkout URLs, requiring zero custom backend code and creating zero PCI-DSS compliance liability.
- **Client-Side Micro-Orchestration:** Client scripts are isolated to lightweight vanilla JS singletons (< 80 lines each) for the custom floating tooltip engine, Text Morph clipboard feedback, and ambient canvas constellation.

---

## 2. Technology Stack & Tooling

| Layer | Technology | Selection Rationale |
| :--- | :--- | :--- |
| **Framework / SSG** | **Astro (v4.16.x)** | Static-first framework with native Content Collections, Vite-powered developer server, and pure HTML output. |
| **Build Tool / Bundler** | **Vite (Internal to Astro)** | High-speed development HMR, modern ES module bundling, and integrated asset pipeline. |
| **Styling** | **Tailwind CSS (`@astrojs/tailwind`)** | Utility-first CSS compiler that strips unused styles, simplifies responsive breakpoints, and enforces design tokens. |
| **Type Validation** | **Zod (`astro:content`)** | Built-in compile-time schema validation for game data. |
| **Image Optimization** | **`astro:assets` (Sharp Engine)** | Automatic WebP conversion, layout shift (CLS) prevention, and responsive image sizing. |
| **Runtime Environment** | **Node.js (v20+ LTS)** | Standard Node runtime for build and local development. |
| **Package Manager** | **npm** | Package manager and build script runner. |
| **Hosting & Edge Delivery** | **Netlify** | Native Astro static deployment, global edge CDN, and automated HTTPS. |
| **Analytics & Telemetry** | **Google Analytics 4 (GA4)** | Client-side tracking via `gtag.js` (`G-QCEE9EZ1X0`) for real-time player and visitor telemetry. |
| **Search Engine Console** | **Google Search Console** | Verified property with XML sitemap submission (`https://olaidigitalstudios.netlify.app/sitemap.xml`). |

---

## 3. Directory & File Structure

```
.
├── netlify.toml                    # Netlify build configuration & publish settings
├── package.json                    # Project dependencies & build scripts
├── astro.config.mjs                # Astro configuration (site URL, Tailwind integration)
├── tailwind.config.mjs             # Tailwind design tokens, colors & transitions
├── tsconfig.json                   # TypeScript strict compiler configuration
│
├── public/
│   ├── app-ads.txt                 # AdMob publisher authorization record
│   ├── robots.txt                  # Web crawler directives referencing sitemap
│   ├── sitemap.xml                 # XML sitemap for Google Search Console
│   ├── favicon.svg                 # Vector browser favicon
│   ├── favicon.ico                 # Fallback browser icon
│   ├── apple-touch-icon.png        # Mobile touch icon
│   └── og-banner.png               # High-res OpenGraph social share card (1200×630)
│
└── src/
    ├── assets/
    │   ├── images/games/           # High-resolution key art (.png, .webp, .jpg)
    │   └── styles/
    │       └── global.css          # Tailwind base, typography & motion tokens
    ├── components/
    │   ├── Hero.astro              # Full-viewport landing with Bodoni Moda & constellation canvas
    │   ├── GamesSection.astro      # Section wrapper rendering the game catalog grid
    │   ├── GameCard.astro          # Unobstructed art, status, title & 4-button launcher dock
    │   ├── StoreIcon.astro         # Clean Simple Icons SVG vectors (no default title elements)
    │   ├── Tooltip.astro           # Singleton floating tooltip portal with collision detection
    │   └── Footer.astro            # Inquiries, Text Morph email copy & dual-channel support buttons
    ├── content/
    │   ├── config.ts               # Content collection definitions & Zod validation schemas
    │   └── games/                  # Game entries (one JSON file per game)
    │       ├── zen-fourier.json
    │       ├── countagram.json
    │       ├── grid-leap.json
    │       ├── node-attack.json
    │       ├── checkless.json
    │       ├── rotatle.json
    │       └── flapcrypt.json
    ├── layouts/
    │   └── BaseLayout.astro        # HTML5 boilerplate, GA4 tag, SEO, OpenGraph, JSON-LD Schema
    └── pages/
        ├── index.astro             # Studio homepage aggregating Hero, Games, and Footer
        └── privacy.astro           # Google Play compliant on-site Privacy Policy
```

---

## 4. Component Architecture & Implementation Details

### 4.1 BaseLayout (`src/layouts/BaseLayout.astro`)
- **Google Analytics 4 Tag (`gtag.js`):** Embedded in `<head>` using Astro's `is:inline` directive:
  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-QCEE9EZ1X0"></script>
  <script is:inline>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-QCEE9EZ1X0');
  </script>
  ```
- **SEO & Canonical URLs:** Dynamic `<link rel="canonical">` and OpenGraph metadata generated against `https://olaidigitalstudios.netlify.app`.
- **Structured Data (Schema.org):** Comprehensive `@graph` containing:
  - `Organization` metadata (studio identity, Chennai location, support email).
  - `VideoGame` schema for all 7 catalog games (title, genre, platform, operating system, and offer availability).
- **Global Portal Mount:** Instantiates `<Tooltip />` immediately before `</body>` to prevent clipping by overflow-hidden containers.

### 4.2 Custom Tooltip Engine (`src/components/Tooltip.astro`)
- **Singleton Architecture:** Single `#app-tooltip` element anchored at root coordinates, eliminating DOM bloat.
- **Decoupled Geometry & Visuals:** Outer `#app-tooltip` strictly handles `top` and `left` in fixed coordinates, while inner `.tooltip-bubble` handles `scale` and `opacity` transitions.
- **Silent Snap on First Hover:** Coordinates are positioned silently *before* triggering the appear animation, completely preventing "fly-in" motion from `(0, 0)`.
- **Adjacent Button Gliding:** When scrubbing between adjacent store buttons while the tooltip is already visible, the `.is-gliding` class activates smooth coordinate interpolation (`150ms`).
- **Collision & Viewport Detection:** Defaults to `data-placement="bottom"` on game cards to prevent overlapping card titles; flips to `top` if colliding with viewport bottom.
- **Touch & Accessibility Guards:** Suppressed on touch devices (`@media (hover: none)`), supports `Tab` keyboard focus, and dismisses on `Escape` or scroll.

### 4.3 Clean Vector Icons (`src/components/StoreIcon.astro`)
- Brand icons (Google Play, Microsoft Store, itch.io, Steam, App Store, Web, GitHub) rendered from canonical Simple Icons vectors.
- **Zero Browser Default Tooltips:** All SVG `<title>` elements are completely omitted. Parent links and badges carry explicit `aria-label` attributes for screen readers, preventing browsers from rendering the native OS tooltip.

### 4.4 Game Cards (`src/components/GameCard.astro`)
- **Unobstructed 16:9 Frame:** Key artwork rendered with Sharp-optimized WebP images with an ambient blurred clone backdrop for non-standard aspect ratios.
- **Launcher Dock Behavior:**
  - Live games: Clickable 44×44px tiles linking to external stores. Web builds feature custom tooltip copy **`Play on Web`**; store links display **`Get on [Platform]`**.
  - In-development games: Muted tiles (`opacity-60 cursor-not-allowed select-none`) with tooltips reading **`[Platform] — Planned`** (including **`Web — Planned`**).
  - All card tooltips enforce `data-tooltip-placement="bottom"`.

### 4.5 Studio Footer & Monetization Hub (`src/components/Footer.astro`)
- **Text Morph Clipboard Copy:** Powered by `transitions-dev` character-diff morphing (`"Copy"` $\rightarrow$ `"Copied!"` $\rightarrow$ `"Copy"` after 2.5s) using `navigator.clipboard` with an invisible `textarea` fallback for legacy browsers.
- **Dual-Channel Monetization Hub ("Support Our Craft"):**
  - **Domestic Button (Cashfree):** Direct link to `https://payments.cashfree.com/forms/support-olai` with emerald active indicator. Accepts UPI (GPay, PhonePe, Paytm, BHIM) and Indian cards.
  - **International Button (PayPal):** Direct link to `https://paypal.me/olaidigitalstudios` with gold PayPal monogram. Accepts global PayPal wallets and international cards.
  - Both buttons enforce `target="_blank" rel="noopener noreferrer"` and carry bottom tooltips.

### 4.6 Privacy Policy (`src/pages/privacy.astro`)
- On-site legal page meeting Google Play Developer Policy and COPPA requirements.
- Details: No account creation, no personal data collection, Google Play Game Services and AdMob advertising ID policies, child privacy safeguards, and contact email.

---

## 5. Content Collection Schema (`src/content/config.ts`)

```typescript
import { defineCollection, z } from 'astro:content';

const gamesCollection = defineCollection({
  type: 'data',
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1, 'Title is required'),
      genre: z.string().min(1, 'Genre is required'),
      tagline: z.string().min(1, 'Tagline is required'),
      status: z.enum(['Available Now', 'In Development']),
      coverImage: image(),
      coverAlt: z.string().min(1, 'Cover alt text is required'),
      releaseDate: z.string().optional(),
      storeLinks: z
        .array(
          z.object({
            platform: z.enum(['google-play', 'app-store', 'steam', 'itch', 'microsoft-store', 'web']),
            url: z.string().url().or(z.literal('')).optional(),
            label: z.string()
          })
        )
        .optional()
    })
});

export const collections = {
  games: gamesCollection
};
```

---

## 6. Hosting & CI/CD Deployment

### 6.1 Netlify Configuration (`netlify.toml`)
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/app-ads.txt"
  [headers.values]
    Content-Type = "text/plain; charset=utf-8"
    Cache-Control = "public, max-age=3600"
```

### 6.2 Deployment Pipeline
1. Changes pushed to GitHub repository `olaidigitalstudios/olai-digital-studios` on branch `master`.
2. Netlify automated webhook detects commit, executes `npm run build` (`astro check && astro build`).
3. Astro generates static output into `dist/`.
4. Netlify edge nodes deploy new static bundle across global CDN within ~20 seconds with zero downtime.

---

## 7. Performance & Security Specifications

### 7.1 Performance Targets
| Metric | Target | Actual / Technical Mechanism |
| :--- | :--- | :--- |
| **First Contentful Paint (FCP)** | < 0.8s | Zero render-blocking JS; inlined atomic CSS via Tailwind. |
| **Largest Contentful Paint (LCP)** | < 1.2s | WebP image optimization via Sharp with priority lazy loading. |
| **Cumulative Layout Shift (CLS)** | 0.00 | Explicit aspect ratios (`aspect-video`) and image dimensions. |
| **Total JavaScript Delivered** | < 4 KB | Vanilla singleton scripts for tooltip, text morph, and canvas. |

### 7.2 Security Hardening
- **Reverse Tab-Nabbing Guard:** All external outbound links (stores, Cashfree, PayPal) enforce `target="_blank" rel="noopener noreferrer"`.
- **Zero API Key Exposure:** No private tokens or gateway client secrets are embedded in client code.
- **Zero Backend Attack Surface:** No dynamic database queries, server endpoints, or user input execution.
- **PCI-DSS Compliance:** All payments are processed on PCI-compliant hosted pages (Cashfree / PayPal); the website never touches card or UPI data.

---

## 8. Verification & Test Checklist

1. **Build Validation:** Run `npm run build` &mdash; confirms 0 TypeScript errors and clean compilation of 2 pages (`/index.html` and `/privacy/index.html`).
2. **AdMob Verification:** `curl -I https://olaidigitalstudios.netlify.app/app-ads.txt` returns `HTTP 200` with `text/plain`.
3. **Analytics Verification:** Verify active sessions appear in Google Analytics Realtime view (`G-QCEE9EZ1X0`).
4. **Search Console Verification:** Sitemaps section confirms green "Success" status for `sitemap.xml`.
5. **Tooltip Interaction:** Hovering store icons glides cleanly with zero fly-in, displays bottom-positioned tooltips without obscuring titles, and suppresses on mobile touch.
6. **Payment Links:** Cashfree link opens UPI/Card checkout; PayPal link opens `paypal.me/olaidigitalstudios`.
