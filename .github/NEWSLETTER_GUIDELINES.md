# Offbeat AI Watch - Newsletter Guidelines

## Publication Schedule
- **Frequency:** Fortnightly (every alternate Wednesday)
- **Target Audience:** B2B leaders, GTM professionals, AI practitioners

---

## Image Specifications

### Cover Image (Lead Story)
| Property | Value |
|----------|-------|
| **Dimensions** | 1280 x 680 pixels |
| **Aspect Ratio** | ~1.88:1 |
| **Format** | JPG (preferred), PNG |
| **Naming Convention** | `{topic}-1280x680.jpg` |
| **Location** | `/images/` |
| **Example** | `aaif-mcp-foundation-1280x680.jpg` |

### Social Sharing Image (OG/Twitter)
| Property | Value |
|----------|-------|
| **Dimensions** | 1200 x 630 pixels |
| **Aspect Ratio** | ~1.91:1 (Facebook/LinkedIn optimal) |
| **Format** | JPG |
| **Naming Convention** | `offbeat-ai-watch-issue{n}-social.jpg` |
| **Location** | `/images/` |
| **Example** | `offbeat-ai-watch-issue5-social.jpg` |

### Image Upload via GitHub
1. Navigate to: `https://github.com/shashwatgtm/ai-trendwatch/tree/{branch}/images`
2. Click "Add file" > "Upload files"
3. Drag image and commit with message: `Add images for Issue #{n}`

---

## SEO Requirements

### Meta Tags (Required)
- [ ] Unique `<title>` tag (50-60 characters)
- [ ] Meta description (under 160 characters)
- [ ] Open Graph tags (og:title, og:description, og:image, og:url)
- [ ] Twitter Card tags (twitter:card, twitter:title, twitter:description, twitter:image)
- [ ] Canonical URL

### Schema.org Structured Data
- [ ] NewsArticle schema with headline, description, dates
- [ ] Author schema with professional details
- [ ] Publisher schema with logo
- [ ] Proper JSON-LD format

### E-E-A-T Guidelines (Google)
- [ ] **Experience:** Author's hands-on B2B GTM work mentioned
- [ ] **Expertise:** "Fractional CMO & AI GTM Expert" credentials
- [ ] **Authoritativeness:** Company affiliation (Helix Consulting), LinkedIn profile
- [ ] **Trustworthiness:** Complete author bio, verifiable credentials

---

## File Updates Per Issue

When publishing a new issue, update these files:

| File | Update Required |
|------|-----------------|
| `issues/YYYY-MM-DD.html` | Create new issue HTML |
| `sitemap.xml` | Add new issue URL with news:news metadata |
| `feed.xml` | Add new item at top of RSS feed |
| `README.md` | Update "Latest Issue" section |
| `archive.html` | Add new issue to archive list |
| `index.html` | Update "Latest Issue" preview section |

---

## Google Search Console Checklist

After publishing each issue:

- [ ] **URL Inspection:** Submit new issue URL for indexing
- [ ] **Sitemap:** Verify sitemap is up to date
- [ ] **Rich Results Test:** Validate structured data at https://search.google.com/test/rich-results
- [ ] **Mobile-Friendly Test:** Verify responsive design

---

## RSS Feed (feed.xml)

- Add new issues at the TOP of the `<channel>` (newest first)
- Update `<lastBuildDate>` to current date
- Include categories relevant to issue content

---

## Newsletter HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags, OG tags, Twitter cards -->
    <!-- Schema.org JSON-LD -->
    <!-- Styles -->
</head>
<body>
    <div class="container">
        <!-- Header with issue number and date -->
        <!-- Lead Story + Editor's Note -->
        <!-- Key Stories Grid -->
        <!-- Trends to Watch -->
        <!-- Author Bio (E-E-A-T) -->
        <!-- Footer with subscribe button -->
    </div>
</body>
</html>
```

---

## Brand Style Guide (Shashwat GTM Expert)

### Background Colors

| Element | Color | Hex |
|---------|-------|-----|
| Primary Dark (Hero) | Dark Gray | `#151617` |
| Secondary Dark | Dark Blue-Gray | `#15151B` |
| Tertiary Dark | Deep Black | `#0B0B10` |
| Light Background 1 | Off White | `#F6F5F8` |
| Light Background 2 | Lavender Tint | `#F6F1FF` |
| White | Pure White | `#FFFFFF` |

### Accent Colors

| Element | Color | Hex |
|---------|-------|-----|
| **Primary Accent** | Coral Pink | `#FAA1A1` |
| Dark Card Background | Dark Purple-Gray | `#1A1A24` |
| Light Card Background | Near White | `#FBFBFD` |
| Borders/Outlines | Light Gray | `#D3D3D3` |

### Text Colors

| Element | Color | Hex |
|---------|-------|-----|
| Primary Text (Dark BG) | White | `#FFFFFF` |
| Stats/Secondary Text | Off White | `#F2F2F2` |
| Primary Text (Light BG) | Dark Gray | `#333333` |

### Typography

- **Display:** Medium size (used for name/headlines)
- **Headings:** H1-H4 default sizes
- **Body:** Default font size
- **Small:** Small size for disclaimers, footer
- **Font Family:** System fonts (-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif)

### Button Styling

| Type | Style | Color |
|------|-------|-------|
| Primary CTA | Solid | `#FAA1A1` (coral pink) |
| Secondary CTA | Solid | Default |
| Tertiary | Outline | Border only |

### Design Principles

- **Dark mode aesthetic:** Heavy use of dark backgrounds (#151617, #0B0B10, #1A1A24)
- **High contrast:** White/light text on dark backgrounds
- **Primary accent:** Coral pink (#FAA1A1) for emphasis, CTAs, and key messaging
- **Cards:** Dark (#1A1A24) or light (#FBFBFD) backgrounds with subtle borders

---

## Contact

**Curator:** Shashwat Ghosh
**Role:** Cofounder & Fractional CMO, Helix Consulting
**LinkedIn:** [linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)
