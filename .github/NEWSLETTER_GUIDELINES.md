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

## Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Primary (Headers) | Blue | `#0066cc` |
| Secondary | Cyan | `#00b8d4` |
| Accent | Purple | `#7b1fa2` |
| Text | Dark Gray | `#333333` |
| Background | White | `#ffffff` |
| Light Background | Light Gray | `#f5f5f5` |

---

## Contact

**Curator:** Shashwat Ghosh
**Role:** Cofounder & Fractional CMO, Helix Consulting
**LinkedIn:** [linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)
