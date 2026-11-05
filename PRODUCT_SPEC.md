# Product Specification Document (PSD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.4.0 (Production Live & Monetized)  
**Status:** Live in Production  
**Live Production URL:** `https://olaidigitalstudios.netlify.app/`  
**Last Updated:** 2026-11-05  

---

## 1. Product Overview

Olai Digital Studios is an independent game development studio based in Chennai, Tamil Nadu, India. This website serves as the studio's official public-facing showcase, monetization verification endpoint, and player engagement hub.

The website functions as a clean, high-impact digital storefront and showcase. Its primary role is driving player discovery and conversion to mobile/platform store listings (e.g., Google Play Store, Microsoft Store, itch.io, and Web demos), presenting the studio's game catalog with boutique dark aesthetic polish, handling studio monetization support (UPI / PayPal), hosting legal compliance policies (`/privacy`), and maintaining advertising compliance through Google AdMob (`app-ads.txt`).

---

## 2. Goals and Non-Goals

### 2.1 Goals
- **Showcase Game Catalog:** Feature current and upcoming studio titles with unobstructed promotional key artwork, single concise genre classification, and direct store/web access.
- **Drive Store & Web Conversion:** Enable immediate player handoff directly from game cards to external store listings (Google Play, Microsoft Store, itch.io) and playable browser editions ("Play on Web").
- **Studio Monetization & Support:** Provide a frictionless, zero-server dual-channel tipping mechanism for studio patrons:
  - **Domestic (India):** Hosted Cashfree form supporting instant UPI (GPay, PhonePe, Paytm, BHIM) and Indian cards.
  - **International (Global):** Direct PayPal.me link supporting global cards and PayPal wallets.
- **AdMob Compliance Verification:** Ensure the AdMob `app-ads.txt` file remains permanently accessible at the root of the published domain (`/app-ads.txt`) to support ongoing mobile ad monetization.
- **On-Site Legal & Store Compliance:** Host a dedicated, Google Play Developer policy-compliant Privacy Policy at `/privacy` confirming zero personal data harvesting and COPPA compliance.
- **Search Engine & Analytics Discoverability:** Integrate Google Analytics 4 (`G-QCEE9EZ1X0`), verified Google Search Console property indexing, XML sitemap, and Schema.org `VideoGame` and `Organization` structured data.
- **Establish Studio Credibility:** Convey an authoritative, boutique indie game studio identity through full-screen minimalist typography and geographic provenance (`Based in Chennai, Tamil Nadu, India`).
- **Artisanal Micro-Interactions:** Feature custom dark floating tooltips (`Tooltip.astro`), Text Morph clipboard actions, micro-constellation hero canvas, and card specular highlights.

### 2.2 Non-Goals (YAGNI Boundaries)
- **No Traditional Sticky Header:** Viewport is uncluttered upon initial load; navigation is progressive and natural.
- **No Complex CMS or Backend Server:** No databases, user login accounts, or server-side frameworks. 100% static HTML generation with serverless CDN deployment.
- **No Embedded Heavy WebGL In-Page Demos:** In-page game interactions link out to dedicated Web game deployments (e.g. Netlify web builds) to preserve sub-second site load times.
- **No Modal Popups or In-Place Drawers:** No intermediate modal dialogs or lightboxes.
- **No Dynamic Contact Form:** Uses direct email interaction with a clipboard copy helper rather than complex form-forwarding services.

---

## 3. Target Audience

1. **Gamers and Mobile Players:** Visitors discovering the studio through Google Play or social platforms who want to explore other games created by Olai Digital Studios.
2. **Patrons and Studio Supporters:** Indian and international fans wishing to tip or support indie game development via UPI or PayPal.
3. **Publishers and Industry Partners:** Platform representatives and potential partners looking to verify the studio's active catalog and professional presence.
4. **Automated Crawlers & Search Engines:** Googlebot, Google Search Console, and ad verification crawlers (Google AdMob) inspecting `/app-ads.txt` and `/sitemap.xml`.

---

## 4. Brand Positioning

- **Brand Tone:** Grounded, confident, artisanal, and modern. Subtle cultural resonance with *Olai* (palm-leaf manuscript craft, structure, and permanence) translated into contemporary digital game craft.
- **Aesthetic Direction:** **Heritage & Craft** palette featuring Velvet Charcoal (`#0C0D0E`), Warm Onyx (`#141518`), Champagne Gold (`#E5B869`), and Warm Terracotta (`#E07A5F`) accents with warm ivory and stone typography (`#FAFAF9`, `#A8A29E`).
- **User Perception:** A focused, agile indie game development studio delivering polished, player-first gaming experiences from Chennai, Tamil Nadu, India.

---

## 5. Information Architecture

The website uses a progressive static architecture organized across two primary routes and essential root compliance files:

```
https://olaidigitalstudios.netlify.app/
│
├── / (Home / Portfolio Showcase)
│     ├── [Minimalist Hero Section] (Full Viewport / 100vh)
│     │     ├── Ambient Breathing Studio Glow
│     │     ├── Micro-Constellation Interactive Canvas
│     │     ├── Monolithic Studio Typography ("OLAI DIGITAL STUDIOS" in Bodoni Moda)
│     │     ├── Studio Provenance Badge ("Based in Chennai, Tamil Nadu, India")
│     │     └── Ambient Scroll Cue ("Scroll to Explore" ↓ with custom tooltip)
│     │
│     ├── [Games Showcase Section (#games)]
│     │     ├── Section Header ("Our Games" with expanding gold hairline)
│     │     └── Responsive Showcase Grid (7 Game Titles)
│     │           └── Game Card Components:
│     │                 ├── 100% Clean Key Art (Unobstructed, Ambient Blurred Fill)
│     │                 ├── Single Concise Genre Tag in Champagne Gold
│     │                 ├── Release Status Pill (Available Now / In Development)
│     │                 ├── Centered Game Title
│     │                 └── Centered Store Icon Launcher Dock:
│     │                       ├── Available Games: Tactile launcher buttons (Google Play, Microsoft Store, itch.io, Web)
│     │                       └── In-Development Games: Disabled dock labeled "Planned on"
│     │
│     ├── [Footer / Inquiries & Monetization (#contact)]
│     │     ├── Studio Provenance & Brand Signature
│     │     ├── Interactive Email Copy Widget (with Text Morph "Copy" → "Copied!")
│     │     ├── Dual-Channel "Support Our Craft" Hub:
│     │     │     ├── Domestic: Cashfree UPI / Indian Cards (₹)
│     │     │     └── International: PayPal Global ($)
│     │     └── Sub-Footer Bar (Copyright + Link to Privacy Policy)
│     │
│     └── [Singleton Global Floating Tooltip (#app-tooltip)]
│
├── /privacy (Privacy Policy)
│     ├── Dedicated Compliant Legal Policy for Google Play Developer Requirements
│     ├── Explicit Zero-Data Collection & COPPA Protections
│     └── Direct Support Contact (`olaidigitalstudios@gmail.com`)
│
├── /app-ads.txt (AdMob Publisher Authorization Record)
├── /sitemap.xml (Search Engine XML Sitemap)
├── /robots.txt (Crawler Directive File)
└── /og-banner.png (OpenGraph Social Share Card 1200×630)
```

---

## 6. Page and Section Requirements

### 6.1 Landing Screen (Full Viewport)
- **Uncluttered Canvas:** Operates without a sticky top header bar, presenting an edge-to-edge cinematic introduction on a pure velvet charcoal canvas (`#0C0D0E`).
- **Interactive Constellation Canvas:** Ambient, non-intrusive floating nodes with hairline proximity connections and mouse repulsion, automatically pausing via `IntersectionObserver` when scrolled out of view.
- **Studio Identity:** Displays the studio wordmark in high-contrast Didone serif (**`Bodoni Moda`**): **OLAI** primary with **DIGITAL STUDIOS** subtitle, incorporating negative right margin compensation for true geometric center.
- **Studio Provenance:** A frosted pill badge in `Plus Jakarta Sans` with a pulsating Champagne Gold indicator reading **Based in Chennai, Tamil Nadu, India**.
- **Scroll Cue:** A geometrically centered prompt (**`Scroll to Explore`** ↓) with optical letter-spacing compensation, bouncing chevron, and custom tooltip (`data-tooltip="View our game catalog"`).

### 6.2 Games Showcase Section (`#games`)
- **Section Heading:** Clean categorization identifying the studio's game catalog with scroll-driven expanding Champagne Gold accent line.
- **Card Architecture:**
  - **Clean Key Art Frame:** 100% unobstructed key art with zero overlays or text badges. Non-16:9 images feature an ambient blurred background clone so art is never clipped.
  - **Metadata Row:** Single concise genre in `Plus Jakarta Sans` in Champagne Gold positioned opposite a release status pill (`● Available Now` in emerald, `● In Development` in amber).
  - **Centered Title:** High-contrast, bold display title in `Manrope` centered within the card body.
  - **Centered Store Icon Launcher Dock:**
    - Live games feature tactile 44×44px icon tiles linking directly to external stores using official **Simple Icons** vectors (`google-play`, `microsoft-store`, `itch`, `web`).
    - Tooltip Copy: Active web builds display **`Play on Web`**, store links display **`Get on [Platform]`**.
    - In-development games are explicitly labeled with `"Planned on"` and feature matching disabled icon tiles (`cursor-not-allowed`, `select-none`, muted opacity) with tooltips reading **`[Platform] — Planned`** (including **`Web — Planned`**).
    - All card tooltips anchor to `data-tooltip-placement="bottom"` to eliminate any overlap with game titles.

### 6.3 Footer and Monetization Section (`#contact`)
- **Studio Signature Split Layout:** Two-column responsive architecture (`md:grid-cols-2`).
  - **Left Column:** Displays the `Bodoni Moda` brand signature and studio provenance statement.
  - **Right Column:** Section label `GET IN TOUCH`, subtitle copy, interactive email copy widget, and studio monetization hub.
- **Direct Email & Clipboard Action:** Displays `olaidigitalstudios@gmail.com` with a one-click Text Morph interaction (`"Copy"` $\rightarrow$ `"Copied!"`) with temporary confirmation feedback and screen-reader polite announcement.
- **Dual-Gateway "Support Our Craft" Hub:**
  - **UPI / India (₹):** Connects to Cashfree hosted form (`https://payments.cashfree.com/forms/support-olai`) with green active node indicator. Tooltip: *"Instant support via UPI, GPay, PhonePe or Cards"*.
  - **PayPal / Global ($):** Connects to PayPal (`https://paypal.me/olaidigitalstudios`) with gold PayPal monogram icon. Tooltip: *"International support via PayPal, Cards or Balance"*.
- **Sub-Footer Bar:** Studio copyright statement and direct link to `/privacy`.

### 6.4 Privacy Policy Page (`/privacy`)
- Fully compliant on-site Privacy Policy meeting Google Play Console and COPPA standards.
- Discloses: zero collection of personally identifiable information (PII), optional Google Play Game Services and AdMob advertising ID policies, child privacy safeguards, and direct support contact.
- Quiet standalone footer returning to studio home.

### 6.5 Root Verification & SEO Files
- **`/app-ads.txt`:** Preserves the exact AdMob verification record: `google.com, pub-4890313674539327, DIRECT, f08c47fec0942fa0`.
- **`/sitemap.xml`:** XML sitemap referencing `https://olaidigitalstudios.netlify.app/` and `/privacy`.
- **`/robots.txt`:** Crawler directives pointing to the live sitemap URL.

---

## 7. Content Catalog (7 Configured Titles)

| Title | Single Genre | Status | Available / Target Platforms | Key Art File |
| :--- | :--- | :--- | :--- | :--- |
| **Grid Leap** | `Puzzle` | Available Now | Google Play, Microsoft Store, itch.io, Web (`https://gridleap.netlify.app/`) | `grid-leap.png` (1920×1080) |
| **Countagram** | `Word Puzzle` | Available Now | Google Play, Microsoft Store, itch.io, Web (`https://countagram.netlify.app/`) | `countagram.jpg` (1024×500) |
| **Zen Fourier** | `Puzzle` | Available Now | Google Play, Microsoft Store, itch.io | `zen-fourier.jpg` (1024×500) |
| **Node Attack** | `Strategy` | Available Now | Google Play, itch.io | `node-attack.png` (512×512) |
| **Checkless** | `Puzzle` | In Development | Planned: Google Play, Microsoft Store, itch.io, Web (`https://checkless.netlify.app/`) | `checkless.png` (1024×500) |
| **Rotatle** | `Word Puzzle` | In Development | Planned: Google Play, Microsoft Store, itch.io, Web | `rotatle.png` (1024×500) |
| **Flapcrypt** | `Word Puzzle` | In Development | Planned: Google Play, Microsoft Store, itch.io, Web | `flapcrypt.png` (1024×500) |

---

## 8. Functional Requirements

- **FR-01: Unobstructed Art Display:** Game cards must display key artwork completely clean without floating overlays.
- **FR-02: Single Genre Classification:** Every game must display a single concise genre in uppercase monospace.
- **FR-03: Equal-Weight Launcher Dock:** All platform options in the launcher dock must have equal visual height and official brand vectors without browser default SVG tooltips.
- **FR-04: Non-Disruptive Outbound Links:** Active store and payment links must open in a separate tab (`target="_blank" rel="noopener noreferrer"`).
- **FR-05: Clipboard Copy Feedback:** Visitors must be able to copy the contact email with a single click and observe an accessible Text Morph transition.
- **FR-06: Unaltered Root File Delivery:** The root `app-ads.txt` file must be served directly at the domain root for AdMob crawlers.
- **FR-07: Dual-Channel Monetization:** The footer must provide direct paths for domestic UPI contributions (Cashfree) and international contributions (PayPal).
- **FR-08: Artisanal Tooltip System:** A singleton floating tooltip must anchor to `[data-tooltip]` elements, honoring placement (defaulting to bottom on game cards to prevent title overlap), with gliding transitions across adjacent buttons.
- **FR-09: On-Site Privacy Policy:** An accessible legal privacy page must be available at `/privacy`.

---

## 9. Non-Functional Requirements

- **NFR-01: Zero Runtime Framework JavaScript:** Compiled as 100% static HTML/CSS with isolated vanilla micro-scripts for tooltips, text morphing, and canvas ambient effects.
- **NFR-02: Accessibility & Reduced Motion:** All animations respect `@media (prefers-reduced-motion: reduce)`.
- **NFR-03: High-Performance Image Optimization:** Game key art is automatically optimized to responsive WebP formats at build time via Astro Sharp.
- **NFR-04: Analytics & SEO Compliance:** Includes Google Analytics 4 (`G-QCEE9EZ1X0`), verified Search Console sitemap, and rich Schema.org `VideoGame` and `Organization` JSON-LD data.
