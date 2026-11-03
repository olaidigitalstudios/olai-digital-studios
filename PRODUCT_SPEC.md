# Product Specification Document (PSD)
**Project Name:** Olai Digital Studios - Official Portfolio Website  
**Document Version:** 1.3.0 (Heritage & Craft Architecture)  
**Status:** Approved for Implementation  
**Last Updated:** 2026-11-02  

---

## 1. Product Overview

Olai Digital Studios is an independent game development studio based in Chennai, Tamil Nadu, India. This website serves as the studio's official public-facing showcase and digital hub.

The website functions as a clean, high-impact digital storefront and showcase. Its primary role is driving player discovery and conversion to mobile/platform store listings (e.g., Google Play Store, Microsoft Store, itch.io, and Web demos), presenting the studio's game catalog with professional polish, and maintaining advertising compliance through Google AdMob (`app-ads.txt`).

---

## 2. Goals and Non-Goals

### 2.1 Goals
- **Showcase Game Catalog:** Feature current and upcoming studio titles with unobstructed promotional key artwork, single concise genre classification, and direct store access.
- **Drive Store Conversion:** Enable immediate, friction-free player handoff directly from game cards to external store listings via official brand launcher docks.
- **AdMob Compliance Verification:** Ensure the existing AdMob `app-ads.txt` file remains permanently accessible at the root of the published domain to support ongoing ad monetization.
- **Establish Studio Credibility:** Convey a focused, confident, boutique indie game development studio identity through full-screen minimalist typography and geographic provenance (`Based in Chennai, Tamil Nadu, India`).
- **Streamlined Studio Inquiries:** Provide direct, low-friction communication channels via email with a tactile Text Morph clipboard copy interaction.
- **Maintainability:** Enable straightforward catalog updates (adding or editing games) through static JSON records.

### 2.2 Non-Goals (YAGNI Boundaries)
- **No Traditional Sticky Header:** Viewport is uncluttered upon initial load; navigation is progressive and natural.
- **No Complex CMS or Backend Services:** No databases, user login accounts, administrative dashboards, or dynamic server-side applications.
- **No Embedded Heavy WebGL In-Page Demos:** Game interactions link directly to official store pages and dedicated Netlify web game deployments.
- **No Modal Popups or In-Place Drawers:** No intermediate modal dialogs or lightboxes.
- **No Newsroom or Blog Section:** No dynamic articles, press releases, or changelog feeds.
- **No On-Site Privacy Policy or Terms Pages:** The website is strictly a portfolio showcase; legal documents are hosted on external platforms/store portals.
- **No Dynamic Contact Form:** No multi-field web forms or automated email forwarding services.

---

## 3. Target Audience

1. **Gamers and Mobile Players:** Visitors discovering the studio through games or social platforms who want to explore other games created by Olai Digital Studios.
2. **Publishers and Industry Partners:** Platform representatives and potential partners looking to verify the studio's active catalog and professional presence.
3. **Automated Ad Network Crawlers:** Verification crawlers (such as Google AdMob) that inspect the domain root for developer authorization.

---

## 4. Brand Positioning

- **Brand Tone:** Grounded, confident, artisanal, and modern. Subtle cultural resonance with *Olai* (palm-leaf manuscript craft, structure, and permanence) translated into contemporary digital game craft.
- **Aesthetic Direction:** **Heritage & Craft** palette featuring Velvet Charcoal (`#0C0D0E`), Warm Onyx (`#141518`), Champagne Gold (`#E5B869`), and Warm Terracotta (`#E07A5F`) accents with warm ivory and stone typography (`#FAFAF9`, `#A8A29E`).
- **User Perception:** A focused, agile indie game development studio delivering polished, player-first gaming experiences from Chennai, Tamil Nadu, India.

---

## 5. Information Architecture

The website uses a single-page progressive structure organized into focused functional areas:

```
/ (Domain Root)
│
├── [Minimalist Hero Section] (Full Viewport / 100vh)
│     ├── Monolithic Studio Typography ("OLAI DIGITAL STUDIOS" in Manrope)
│     ├── Studio Provenance Badge ("Based in Chennai, Tamil Nadu, India")
│     └── Ambient Scroll Cue ("Scroll to Explore" ↓)
│
├── [Games Showcase Section (#games)]
│     ├── Section Header ("Our Games")
│     └── Responsive Showcase Grid
│           └── Game Card Components:
│                 ├── 100% Clean Key Art (Unobstructed, Ambient Backdrop Fill)
│                 ├── Single Concise Genre Tag in Champagne Gold (e.g. Puzzle, Strategy, Word Puzzle)
│                 ├── Release Status Pill (Live / In Dev)
│                 ├── Centered Game Title
│                 └── 4-Button Launcher Dock:
│                       ├── Active Live Games: Clickable tactile icon tiles (Google Play, Microsoft Store, itch.io, Web)
│                       └── In-Development Games: Disabled dock labeled "Planned on"
│
├── [Footer / Contact Section (#contact)]
│     ├── Studio Contact Invitation ("For inquiries, partnerships, or feedback, drop us a line.")
│     ├── Interactive Email Copy Widget (with Text Morph interaction)
│     └── Copyright Notice
│
└── /app-ads.txt (Root Verification File)
```

---

## 6. Page and Section Requirements

### 6.1 Landing Screen (Full Viewport)
- **Uncluttered Canvas:** Operates without a sticky top header bar, presenting an edge-to-edge cinematic introduction on a pure velvet charcoal canvas (`#0C0D0E`).
- **Studio Identity:** Displays the studio wordmark in high-contrast Didone serif (**`Bodoni Moda`**): **OLAI** primary with **DIGITAL STUDIOS** subtitle, incorporating negative right margin compensation for true geometric center.
- **Studio Provenance:** A frosted pill badge in `Plus Jakarta Sans` with a pulsating Champagne Gold indicator reading **Based in Chennai, Tamil Nadu, India**.
- **Scroll Cue:** A geometrically centered prompt (**`Scroll to Explore`** ↓) in `Plus Jakarta Sans` with optical letter-spacing compensation and bouncing chevron, inviting visitors to scroll down into `#games`.

### 6.2 Games Showcase Section (`#games`)
- **Section Heading:** Clean categorization identifying the studio's game catalog.
- **Card Architecture:**
  - **Clean Key Art Frame:** 100% unobstructed key art with zero overlays or text badges. Non-16:9 images feature an ambient blurred background clone so art is never clipped.
  - **Metadata Row:** Single concise genre in `Plus Jakarta Sans` (`font-sans font-semibold`) in Champagne Gold positioned opposite a release status pill (`● Available Now` in emerald, `● In Development` in amber).
  - **Centered Title:** High-contrast, bold display title in `Manrope` centered within the card body.
  - **No Tagline Paragraph:** Body text is omitted to maintain a tight, uniform vertical card height across the grid.
  - **Uniform 4-Button Launcher Dock:**
    - Live games feature tactile 44×44px icon tiles linking directly to external stores using official **Simple Icons** vectors (`google-play`, `microsoft-store`, `itch`, `web`).
    - In-development games are explicitly labeled with `"Planned on"` in `Plus Jakarta Sans` and feature matching disabled icon tiles (`cursor-not-allowed`, `select-none`, muted opacity).

### 6.3 Footer and Contact Section (`#contact`)
- **Studio Signature Split Layout:** Two-column responsive architecture (`md:grid-cols-2`).
  - **Left Column:** Displays the `Bodoni Moda` brand signature and studio provenance statement (*"Independent game development studio based in Chennai, Tamil Nadu, India."*).
  - **Right Column:** Section label `GET IN TOUCH`, subtitle copy (*"For inquiries, partnerships, or feedback, drop us a line."*), and interactive email copy widget.
- **Direct Email & Clipboard Action:** Displays `olaidigitalstudios@gmail.com` with a one-click Text Morph interaction (`"Copy"` $\rightarrow$ `"Copied!"`) with temporary confirmation feedback and screen-reader polite announcement.
- **Sub-Footer Bar:** Centered studio copyright statement: `© 2026 Olai Digital Studios. All rights reserved.`

### 6.4 Root Verification File (`/app-ads.txt`)
- Accessible directly at the root path of the published website (`https://dhineshmoorthy-gamedev.github.io/app-ads.txt`).
- Preserves the existing AdMob verification record without modification: `google.com, pub-4890313674539327, DIRECT, f08c47fec0942fa0`.

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
- **FR-03: Equal-Weight Launcher Dock:** All platform options in the launcher dock must have equal visual height and official brand vectors.
- **FR-04: Non-Disruptive Outbound Links:** Active store links must open in a separate tab (`target="_blank" rel="noopener noreferrer"`).
- **FR-05: Clipboard Copy Feedback:** Visitors must be able to copy the contact email with a single click and observe an accessible Text Morph transition.
- **FR-06: Unaltered Root File Delivery:** The root `app-ads.txt` file must be served directly at the domain root.

---

## 9. Non-Functional Requirements

- **NFR-01: Zero Runtime Framework JavaScript:** Compiled as 100% static HTML/CSS with isolated vanilla micro-scripts (<35 lines) for the clipboard copy.
- **NFR-02: Accessibility & Reduced Motion:** All animations respect `@media (prefers-reduced-motion: reduce)`.
- **NFR-03: High-Performance Image Optimization:** Game key art is automatically optimized to responsive WebP formats at build time.
