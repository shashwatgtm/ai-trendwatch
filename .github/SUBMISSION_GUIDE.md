# Offbeat AI Watch - SEO & Discoverability Guide

## Overview
This guide covers all SEO, discoverability, and submission requirements to ensure each newsletter issue reaches maximum visibility across search engines, LLMs, and news aggregators.

---

## SEO & Discoverability Checklist

### Google Search Console & Analytics

#### sitemap.xml
- [ ] Add new issue URL with Google News schema
- [ ] Update homepage lastmod date
- [ ] Update archive page lastmod date
- [ ] Format: `YYYY-MM-DD` for dates

```xml
<!-- Newsletter Issue #X -->
<url>
  <loc>https://shashwatgtm.github.io/ai-trendwatch/issues/YYYY-MM-DD.html</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.9</priority>
  <news:news>
    <news:publication>
      <news:name>Offbeat AI Watch</news:name>
      <news:language>en</news:language>
    </news:publication>
    <news:publication_date>YYYY-MM-DD</news:publication_date>
    <news:title>[Issue Headline]</news:title>
  </news:news>
</url>
```

#### robots.txt (Pre-configured)
Already allows all crawlers:
- GPTBot, ChatGPT-User (OpenAI)
- Google-Extended (Google Gemini)
- CCBot (Common Crawl)
- anthropic-ai, Claude-Web (Anthropic)
- Googlebot, Bingbot

---

### Schema.org Markup (Full NewsArticle Schema)

Required in every issue HTML:

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "[Main headline]",
  "alternativeHeadline": "[Expanded headline]",
  "description": "[Meta description]",
  "image": "[Cover image URL]",
  "datePublished": "YYYY-MM-DDT00:00:00Z",
  "dateModified": "YYYY-MM-DDT00:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Shashwat Ghosh",
    "jobTitle": "Fractional CMO & AI GTM Expert",
    "url": "[LinkedIn URL]",
    "sameAs": ["[LinkedIn]", "[Twitter]", "[GitHub]"],
    "affiliation": {
      "@type": "Organization",
      "name": "Helix Consulting"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Offbeat AI Watch",
    "url": "https://shashwatgtm.github.io/ai-trendwatch/"
  },
  "keywords": "[Comma-separated keywords]",
  "about": [
    {
      "@type": "Thing",
      "name": "[Topic]",
      "sameAs": "[Wikipedia URL]"
    }
  ]
}
```

---

### Google EEAT Guidelines Compliance

| Criterion | Implementation |
|-----------|---------------|
| **Experience** | Author's hands-on B2B GTM work with specific examples |
| **Expertise** | "Fractional CMO & AI GTM Expert" with focus areas listed |
| **Authoritativeness** | Helix Consulting affiliation, LinkedIn profile links |
| **Trustworthiness** | Complete author bio section with verifiable credentials |

#### Author Bio Section (Required)
```html
<section class="author-bio" itemscope itemtype="https://schema.org/Person">
  <h3>About the Author</h3>
  <p><strong itemprop="name">Shashwat Ghosh</strong> is a
     <span itemprop="jobTitle">Fractional CMO and AI GTM operator</span>...</p>
  <p><strong>Focus areas:</strong> AI GTM strategy, product positioning...</p>
  <ul>
    <li>LinkedIn: <a href="[URL]" itemprop="sameAs">...</a></li>
    <li>Newsletter: <a href="[URL]" itemprop="url">...</a></li>
    <li>GitHub: <a href="[URL]" itemprop="sameAs">...</a></li>
  </ul>
</section>
```

---

### LLM Accessibility

#### Semantic HTML5 Structure
- `<article>` for main content
- `<section>` for distinct sections
- `<header>` and `<footer>` for page structure
- `<nav>` for navigation
- Proper heading hierarchy (H1 > H2 > H3 > H4)

#### Machine-Readable Data
- Schema.org JSON-LD in `<head>`
- Descriptive alt text on all images
- Clear, semantic class names
- Structured content blocks

---

### Social Media Discoverability

#### Open Graph (LinkedIn & Facebook)
```html
<meta property="og:url" content="[Canonical URL]">
<meta property="og:type" content="article">
<meta property="og:title" content="[Headline] - Offbeat AI Watch">
<meta property="og:description" content="[Under 160 chars]">
<meta property="og:image" content="[1200x630 social image URL]">
<meta property="og:site_name" content="Offbeat AI Watch">
```

#### Twitter/X Cards
```html
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:domain" content="shashwatgtm.github.io">
<meta property="twitter:url" content="[Canonical URL]">
<meta name="twitter:title" content="[Headline] - Offbeat AI Watch">
<meta name="twitter:description" content="[Under 160 chars]">
<meta name="twitter:image" content="[1200x630 social image URL]">
```

---

### RSS Feed (feed.xml)

#### Update Process
1. Update `<lastBuildDate>` to current date
2. Add new `<item>` at top (below channel info)
3. Include all required fields:

```xml
<item>
  <title>[Headline] - Offbeat AI Watch</title>
  <link>[Issue URL]</link>
  <description>[Meta description]</description>
  <pubDate>[Day, DD Mon YYYY 00:00:00 GMT]</pubDate>
  <guid>[Issue URL]</guid>
  <author>Shashwat Ghosh</author>
  <category>Artificial Intelligence</category>
  <category>Technology</category>
  <category>Enterprise AI</category>
  <!-- Add topic-specific categories -->
</item>
```

#### Standard Categories (Always Include)
- Artificial Intelligence
- Technology
- Enterprise AI

#### Topic-Specific Categories (Add as Relevant)
- Cybersecurity / AI Security
- Edge Computing
- Continual Learning
- Agentic AI
- Data Analysis
- Voice Automation
- Healthcare AI
- Cloud Computing
- Infrastructure

---

### SEO Best Practices Checklist

| Item | Requirement |
|------|-------------|
| Title tags | Unique, under 60 characters |
| Meta descriptions | Under 160 characters, includes key topics |
| Canonical URLs | Set on every page |
| Alt text | Descriptive, on all images |
| Heading hierarchy | H1 > H2 > H3 > H4, no skipping |
| Internal linking | Archive link, back to home |
| External links | `rel="noopener" target="_blank"` |
| Mobile responsive | Tested at 600px breakpoint |

---

### Mobile Responsive Design

#### Required CSS
```css
@media only screen and (max-width: 600px) {
    .container { padding: 20px; }
    .header-title { font-size: 36px; }
    .lead-story-wrapper { display: block; }
    .lead-story, .editor-note-box {
        flex: none;
        width: 100%;
        margin-bottom: 30px;
    }
    .story-grid, .trends-grid { display: block; }
    .story-item, .trend-item { margin-bottom: 20px; }
    .story-title { font-size: 28px; }
    .header-meta { margin-top: 20px; text-align: left; }
}
```

---

### Email Signup Form (Formspree)

Already configured in index.html:
- Form action: `https://formspree.io/f/mnngzoee`
- JavaScript validation and success handling
- No backend required

---

### Files to Update Per Issue

| File | Updates Required |
|------|-----------------|
| `issues/YYYY-MM-DD.html` | New issue HTML |
| `archive.html` | Add issue entry at top of list |
| `feed.xml` | Add RSS item, update lastBuildDate |
| `sitemap.xml` | Add URL, update lastmod dates |
| `index.html` | Update "Latest Issue" section |
| `/images/` | Add cover image (1280x680) |

---

### Verification Tools

#### Before Publishing
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)

#### After Publishing
- Google Search Console: Check indexing status
- RSS feed validators: Verify feed.xml
- Mobile-friendly test: Verify responsive design

---

### News Aggregator Compatibility

RSS feed (feed.xml) is compatible with:
- Feedly
- Inoreader
- NewsBlur
- Google News (via sitemap)
- Apple News (RSS compatible)

---

### Troubleshooting

#### Issue: Not appearing in Google News
**Fix**: Verify sitemap.xml has `news:news` schema, check Google Search Console

#### Issue: Social preview not showing image
**Fix**: Verify og:image URL is absolute path, test with platform debuggers

#### Issue: RSS feed not updating
**Fix**: Check lastBuildDate format, verify XML is valid

#### Issue: Schema validation errors
**Fix**: Use Google Rich Results Test, check JSON-LD syntax

---

Last Updated: December 3, 2025 (Issue #4)
