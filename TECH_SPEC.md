# Technical Specification Document (TSD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.3.0  
**Status:** Approved for Implementation  
**Derived From:** [PRODUCT_SPEC.md](file:///C:/Users/DHINESH/Desktop/github/app-ads.txt/PRODUCT_SPEC.md) (v1.3.0)  
**Last Updated:** 2026-11-02  

---

## 1. Technical Overview & Architectural Principles

The Olai Digital Studios website is architected as an ultra-fast, zero-runtime-overhead Static Site Generation (SSG) web application.

```
┌────────────────────────────────────────────────────────┐
│                   Development / Build                  │
│                                                        │
│  src/content/games/ ──┐                                │
│      (JSON / Zod)     │                                │
│                       ▼                                │
│  src/components/  ──► [ Astro Core (Vite Engine) ]     │
│  src/assets/          │                                │
│                       ▼                                │
│  public/app-ads.txt ──► [ Build Output: dist/ ]        │
└───────────────────────┼────────────────────────────────┘
                        │
                        ▼ (GitHub Actions Push to main)
┌────────────────────────────────────────────────────────┐
│                 Hosting & Delivery                     │
│                                                        │
│                  GitHub Pages (CDN)                    │
│                           │                            │
│           ┌───────────────┴───────────────┐            │
│           ▼                               ▼            │
│  Browsers (0kb JS HTML/CSS)      AdMob Crawler (GET /) │
│  - Instant First Contentful      - 200 OK text/plain   │
│  - Smooth anchor navigation      - pub-489031367453... │
└────────────────────────────────────────────────────────┘
```

### Architectural Principles
- **Static First (0kb JS by default):** All HTML and CSS are pre-rendered at compile time. No client-side framework runtime (no React/Vue runtime overhead) is delivered to the browser.
- **Type-Safe Content Modeling:** Game catalog entries are defined as structured data files validated at build-time with Zod schemas. Any invalid URL, missing banner image, or typo breaks the build immediately with actionable error messages.
- **Root Compliance Preservation:** The critical AdMob `app-ads.txt` is served directly from the root of the domain as an unbundled, untransformed static asset with HTTP 200 and `text/plain` MIME type.
- **Automated CI/CD:** Continuous integration and deployment are fully automated using native GitHub Actions deploying directly to GitHub Pages.

---

## 2. Technology Stack & Tooling

| Layer | Technology | Selection Rationale |
| :--- | :--- | :--- |
| **Framework / SSG** | **Astro (v4.x / v5.x)** | Static-first framework with native Content Collections, Vite-powered developer server, and pure HTML output. |
| **Build Tool / Bundler** | **Vite (Internal to Astro)** | Lightning-fast development HMR, modern ES module bundling, and integrated asset pipeline. |
| **Styling** | **Tailwind CSS (`@astrojs/tailwind`)** | Utility-first CSS compiler that strips all unused styles, simplifies responsive breakpoints, and enforces design tokens. |
| **Type Validation** | **Zod (`astro:content`)** | Built-in compile-time schema validation for game data. |
| **Image Optimization** | **`astro:assets` (Sharp Engine)** | Automatic WebP conversion, layout shift (CLS) prevention, and automatic responsive image sizing. |
| **Runtime Environment** | **Node.js (v20+ LTS)** | Standard Node runtime for build and local development. |
| **Package Manager** | **npm** | Zero-setup package manager standard across GitHub Actions environments. |
| **Hosting & CDN** | **GitHub Pages** | Free, high-availability static hosting integrated directly with the repository. |
| **CI/CD** | **GitHub Actions** | Native repository automation via `actions/deploy-pages`. |

---

## 3. Directory & File Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions CI/CD deployment workflow
├── public/
│   ├── app-ads.txt                 # AdMob publisher verification file (served at /app-ads.txt)
│   ├── favicon.svg                 # Vector browser favicon
│   └── robots.txt                  # Search engine and crawler instructions
├── src/
│   ├── assets/
│   │   ├── images/
│   │   │   ├── logo.svg            # Studio vector brandmark
│   │   │   └── games/              # High-resolution source key art images (.png, .webp, .jpg)
│   │   └── styles/
│   │       └── global.css          # Tailwind base directives, typography & motion tokens
│   ├── components/
│   │   ├── Hero.astro              # Full-viewport screen with Bodoni Moda wordmark, location badge & scroll prompt
│   │   ├── GamesSection.astro      # Section wrapper rendering the game catalog grid
│   │   ├── GameCard.astro          # Unobstructed 16:9 art, single genre, centered title & 4-button launcher dock
│   │   ├── StoreIcon.astro         # Canonical Simple Icons SVG vectors for all gaming platforms
│   │   └── Footer.astro            # Inquiries copy, Text Morph email copy widget & copyright
│   ├── content/
│   │   ├── config.ts               # Content collection definitions & Zod validation schemas
│   │   └── games/                  # Game entries (one JSON file per game)
│   │       ├── orbital-drift.json
│   │       ├── checkless.json
│   │       ├── countagram.json
│   │       ├── flapcrypt.json
│   │       ├── grid-leap.json
│   │       ├── rotatle.json
│   │       └── shadow-grid.json
│   ├── layouts/
│   │   └── BaseLayout.astro        # HTML5 boilerplate, SEO meta tags, OpenGraph, JSON-LD
│   └── pages/
│       └── index.astro             # Single-page entry assembling BaseLayout + Hero + GamesSection + Footer
├── astro.config.mjs                # Astro configuration file (integrations, site URL, base)
├── package.json                    # Dependencies and build scripts
├── tailwind.config.mjs             # Tailwind theme extensions (colors, fonts, screens)
└── tsconfig.json                   # TypeScript configuration for Astro and content collections
```

---

## 4. Data Layer & Content Schema

### 4.1 Content Collection Schema (`src/content/config.ts`)
Astro Content Collections enforce strict compile-time validation using Zod:

```typescript
import { defineCollection, z } from 'astro:content';

const gamesCollection = defineCollection({
  type: 'data',
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1, 'Title is required'),
      tagline: z.string().max(120, 'Tagline must be under 120 characters'),
      genre: z.string(), // Single concise genre (e.g., 'Puzzle', 'Strategy', 'Word Puzzle')
      status: z.enum(['Available Now', 'In Development', 'Early Access']),
      coverImage: image(), // Validates image file existence and enables Sharp optimization
      coverAlt: z.string(),
      featuredOrder: z.number().default(99),
      storeLinks: z
        .array(
          z.object({
            platform: z.enum([
              'google-play',
              'app-store',
              'steam',
              'itch',
              'microsoft-store',
              'web'
            ]),
            label: z.string(),
            url: z.string().optional(),
            primary: z.boolean().default(false)
          })
        )
        .default([])
    })
});

export const collections = {
  games: gamesCollection
};
```

### 4.2 Game Data Entry Examples

#### Released Title (`src/content/games/countagram.json`)
```json
{
  "title": "Countagram",
  "tagline": "Crack the letter counts. Uncover every anagram.",
  "genre": "Word Puzzle",
  "status": "Available Now",
  "coverImage": "../../assets/images/games/countagram.jpg",
  "coverAlt": "Countagram key art showing letter frequency puzzles and word anagrams",
  "featuredOrder": 4,
  "storeLinks": [
    {
      "platform": "google-play",
      "label": "Get on Google Play",
      "url": "https://play.google.com/store/apps/details?id=com.olaidigitalstudios.countagram",
      "primary": true
    },
    {
      "platform": "microsoft-store",
      "label": "Get it from Microsoft Store",
      "url": "https://apps.microsoft.com/detail/9mvz4fhkbml5",
      "primary": false
    },
    {
      "platform": "itch",
      "label": "Play on itch.io",
      "url": "https://olaidigitalstudios.itch.io/countagram",
      "primary": false
    },
    {
      "platform": "web",
      "label": "Web",
      "url": "https://countagram.netlify.app/",
      "primary": false
    }
  ]
}
```

#### In-Development Title (`src/content/games/rotatle.json`)
```json
{
  "title": "Rotatle",
  "tagline": "Rotate the board, guide falling letters, and solve clever word puzzles.",
  "genre": "Word Puzzle",
  "status": "In Development",
  "coverImage": "../../assets/images/games/rotatle.png",
  "coverAlt": "Rotatle key art showing rotating letter board mechanics and falling gravity puzzles",
  "featuredOrder": 5,
  "storeLinks": [
    {
      "platform": "google-play",
      "label": "Google Play",
      "primary": false
    },
    {
      "platform": "microsoft-store",
      "label": "Microsoft Store",
      "primary": false
    },
    {
      "platform": "itch",
      "label": "itch.io",
      "primary": false
    },
    {
      "platform": "web",
      "label": "Web",
      "primary": false
    }
  ]
}
```

---

## 5. AdMob `app-ads.txt` Integration

### 5.1 Preservation & Deployment Guarantee
- The existing verification file resides in `public/app-ads.txt`.
- When `astro build` executes, Astro copies all files from `public/` directly into the root of `dist/` without modification, transformation, or compression.
- **Verification Rule:** `dist/app-ads.txt` will contain the exact byte sequence:
  ```
  google.com, pub-4890313674539327, DIRECT, f08c47fec0942fa0
  ```

### 5.2 Server Routing & Response Specification
When requested by the Google AdMob crawler via `GET /app-ads.txt`:
- **HTTP Status:** `200 OK`
- **MIME Type:** `text/plain; charset=utf-8`
- **No Redirects:** Direct resolution with zero 301/302 redirects.
- **Cache-Control:** Standard static CDN caching with `stale-while-revalidate`.

---

## 6. Asset Optimization Pipeline

### 6.1 Key Art Presentation & Dual-Layer Ambient Background
Key art source files are stored in `src/assets/images/games/`. To provide an unobstructed, edge-to-edge frame that handles arbitrary image dimensions (16:9 landscape, vertical posters, or square tiles) without letterboxing bars or awkward cropping, `GameCard.astro` implements a dual-layer container:
- **Ambient Blurred Underlayer:** The source key art is rendered full-bleed with `absolute inset-0 object-cover blur-2xl scale-110 opacity-30` to generate a dynamic, color-matched atmospheric glow.
- **Sharp Foreground Key Art:** The primary key art is centered with `relative z-10 w-full h-full object-contain` inside a strict `aspect-video` (16:9) frame.
- **Zero-Overlay Guarantee:** Badges, text overlays, and dark scrims are forbidden over the key art frame, preserving 100% artwork visibility.

```astro
<div class="relative w-full aspect-video rounded-xl overflow-hidden bg-black/40 border border-white/5">
  <!-- Dynamic atmospheric blur background -->
  <Image
    src={game.data.coverImage}
    alt=""
    aria-hidden="true"
    width={400}
    height={225}
    format="webp"
    quality={40}
    class="absolute inset-0 w-full h-full object-cover blur-2xl scale-110 opacity-30 select-none pointer-events-none"
  />
  <!-- Sharp foreground key art -->
  <Image
    src={game.data.coverImage}
    alt={game.data.coverAlt}
    width={640}
    height={360}
    format="webp"
    quality={85}
    loading="lazy"
    decoding="async"
    class="relative z-10 w-full h-full object-contain transition-transform duration-moderate ease-smooth-out group-hover:scale-[1.02]"
  />
</div>
```

### 6.2 Platform Icon Pipeline (`StoreIcon.astro`)
Platform store marks are rendered as vector SVGs sourced directly from the official **Simple Icons** repository to eliminate hand-drawn approximations and ensure brand fidelity:
- `google-play` / `googleplay`: Official Google Play polygon glyph.
- `microsoft-store` / `microsoftstore`: Official 4-square Microsoft glyph.
- `itch` / `itchdotio`: Official Itch.io gamepad glyph.
- `web`: Crisp globe vector for direct browser playable links.
- `steam`, `app-store`: Ready-to-use canonical SVGs.

---

## 7. Client-Side Interactivity (Text Morph Micro-Script)

To adhere to the 0kb runtime framework principle, client-side functionality is implemented using an isolated, zero-dependency inline script in `Footer.astro` powered by the `transitions-dev` Text Morph interaction pattern:

```html
<script is:inline>
  (function () {
    var btn = document.getElementById('copy-email-btn');
    var label = document.getElementById('copy-label');
    var feedback = document.getElementById('copy-feedback');
    var email = 'olaidigitalstudios@gmail.com';
    var resetTimeout;

    if (!btn || !label) return;

    // Character-diff Text Morph (transitions-dev 33-text-morph)
    function morphText(el, next) {
      var prev = el.dataset.text || el.textContent;
      if (prev === next) return;
      el.dataset.text = next;
      // ... computes longest common prefix/suffix and animates sliding transition ...
    }

    btn.addEventListener('click', async function () {
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(email);
        } else {
          // Fallback textarea copy
          var ta = document.createElement('textarea');
          ta.value = email;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.focus();
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
        }
        morphText(label, '✓ Copied!');
        if (feedback) feedback.textContent = 'Email copied to clipboard';
        btn.classList.add('text-accent-gold');
        clearTimeout(resetTimeout);
        resetTimeout = setTimeout(function () {
          morphText(label, 'Copy');
          btn.classList.remove('text-accent-gold');
        }, 2200);
      } catch (err) {
        console.error('Failed to copy email:', err);
      }
    });
  })();
</script>
```

---

## 8. CI/CD & Deployment Pipeline

### 8.1 GitHub Configuration
- **Repository URL:** `https://github.com/DhineshMoorthy-gamedev/app-ads.txt`
- **Deployment Source:** GitHub Actions (configured in Repository Settings -> Pages -> Build and deployment -> Source: **GitHub Actions**).

### 8.2 GitHub Actions Workflow (`.github/workflows/deploy.yml`)
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: 'pages'
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js (v20)
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build static site with Astro
        run: npm run build

      - name: Verify app-ads.txt in build output
        run: test -f dist/app-ads.txt || (echo "Missing app-ads.txt in dist!" && exit 1)

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './dist'

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 9. Performance & Security Specifications

### 9.1 Performance Budgets
| Metric | Target | Technical Mechanism |
| :--- | :--- | :--- |
| **First Contentful Paint (FCP)** | < 0.8s | Zero external render-blocking scripts; critical CSS inlined by Tailwind. |
| **Largest Contentful Paint (LCP)** | < 1.5s | Hero section key art preloaded; WebP asset compression via Sharp. |
| **Cumulative Layout Shift (CLS)** | 0.00 | Strict image dimensions (`width`/`height`) set on every visual element. |
| **Total JavaScript Delivered** | < 2 KB | Only the ~30-line inline clipboard handler; no framework runtime. |

### 9.2 Security Rules
- **Outbound Link Hardening:** Every external anchor tag targeting stores or developer profiles must strictly include:
  ```html
  target="_blank" rel="noopener noreferrer"
  ```
- **Zero Attack Surface:** No backend servers, API endpoints, or database connections.
- **Content Security:** No external script CDN tags (no third-party tracking libraries, tag managers, or ad scripts on the portfolio site).

### 9.3 SEO, Social Metadata & Schema.org
`BaseLayout.astro` generates standard head tags:
- Canonical URL: `https://dhineshmoorthy-gamedev.github.io`
- OpenGraph Tags: `og:title`, `og:description`, `og:type="website"`, `og:image` (1200x630 social card banner)
- Twitter Card: `twitter:card="summary_large_image"`
- Structured Data (JSON-LD):
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Olai Digital Studios",
    "url": "https://dhineshmoorthy-gamedev.github.io",
    "logo": "https://dhineshmoorthy-gamedev.github.io/assets/logo.svg",
    "contactPoint": {
      "@type": "ContactPoint",
      "email": "olaidigitalstudios@gmail.com",
      "contactType": "customer support"
    }
  }
  ```

---

## 10. Traceability Matrix

| Product Spec Requirement | Tech Spec Implementation Mechanism |
| :--- | :--- |
| **FR-01: Section Anchor Navigation** | Native HTML smooth scrolling (`scroll-behavior: smooth`) with semantic IDs (`#games`, `#contact`). |
| **FR-02: Structured Catalog Presentation** | Astro Content Collections (`src/content/games/*.json`) rendered via `Astro.getCollection('games')`. |
| **FR-03: Responsive Grid Layout** | Tailwind CSS grid classes (`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8`). |
| **FR-04: Non-Disruptive Outbound Links** | Native HTML `target="_blank" rel="noopener noreferrer"` attributes on store buttons. |
| **FR-05: Clipboard Copy Capability** | Scoped vanilla inline script utilizing `navigator.clipboard` with visual feedback toggle. |
| **FR-06: Unaltered Root File Delivery** | `public/app-ads.txt` mapped 1:1 to `dist/app-ads.txt` verified by CI workflow step. |
| **NFR-01: Mobile-First Usability** | Tailwind responsive breakpoint utilities (`sm:`, `md:`, `lg:`) with minimum 44px touch targets. |
| **NFR-02: Rapid Loading Experience** | Astro SSG zero-JS output + `astro:assets` Sharp WebP image compression. |
| **NFR-03: Visual Accessibility** | Semantic HTML tags (`<nav>`, `<main>`, `<article>`), high-contrast dark theme tokens, explicit `alt` text. |
| **NFR-04: Social Sharing Previews** | OpenGraph & Twitter Card `<meta>` tags dynamically populated in `BaseLayout.astro`. |
| **NFR-05: High Reliability** | Static hosting on GitHub Pages CDN with zero server runtime dependencies. |

---

## 11. Testing & Verification Checklist

1. **Build Validation:** Run `npm run check && npm run build` locally; ensure zero errors and valid generation of `dist/index.html` and `dist/app-ads.txt` (Verified: 12 files scanned, 0 errors, 0 warnings).
2. **Type Safety Test:** Schema constraints in `src/content/config.ts` validate `genre`, `status`, `coverImage`, and `storeLinks` across all 7 catalog games.
3. **MIME & Root Verification:** Run `curl -I https://dhineshmoorthy-gamedev.github.io/app-ads.txt` post-deploy to confirm `HTTP/2 200` and `Content-Type: text/plain`.
4. **Lighthouse Audit:** Performance, Accessibility, Best Practices, and SEO scores target 95+ on mobile and desktop due to static zero-framework delivery.
5. **Interactive Check:** Verify that clicking the copy button in `Footer.astro` triggers the `transitions-dev` character-diff morph into `✓ Copied!`, copies `olaidigitalstudios@gmail.com` to clipboard, and announces via ARIA live region.
