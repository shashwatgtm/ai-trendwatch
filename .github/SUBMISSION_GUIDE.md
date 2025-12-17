# Offbeat AI Watch - Issue Submission Guide

## Quick Reference

### Image Sizes
- **Cover Image:** 1280 x 680 pixels
- **Social Image:** 1200 x 630 pixels

### File Naming
- Cover: `{topic}-1280x680.jpg`
- Social: `offbeat-ai-watch-issue{n}-social.jpg`

---

## Pre-Publication Checklist

### Content Ready
- [ ] Editor's Note finalized
- [ ] Lead story with image
- [ ] 5-7 key stories
- [ ] 4-5 trends to watch
- [ ] All source links verified

### Images Ready
- [ ] Cover image (1280x680)
- [ ] Social sharing image (1200x630)
- [ ] Images uploaded to `/images/` folder

---

## Publication Steps

### Step 1: Create Issue HTML
```
/issues/YYYY-MM-DD.html
```
- Copy previous issue as template
- Update all content, meta tags, dates
- Verify Schema.org data

### Step 2: Update Sitemap
```xml
<!-- Add to sitemap.xml -->
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
    <news:title>Issue Title Here</news:title>
  </news:news>
</url>
```

### Step 3: Update RSS Feed
Add new item at TOP of feed.xml:
```xml
<item>
  <title>Issue Title - Offbeat AI Watch</title>
  <link>https://shashwatgtm.github.io/ai-trendwatch/issues/YYYY-MM-DD.html</link>
  <description>Issue description here</description>
  <pubDate>Day, DD Mon YYYY 00:00:00 GMT</pubDate>
  <guid>https://shashwatgtm.github.io/ai-trendwatch/issues/YYYY-MM-DD.html</guid>
  <author>Shashwat Ghosh</author>
  <category>Artificial Intelligence</category>
</item>
```

### Step 4: Update Supporting Files
- [ ] `README.md` - Latest Issue section
- [ ] `archive.html` - Add to archive list
- [ ] `index.html` - Update Latest Issue preview

### Step 5: Commit & Push
```bash
git add .
git commit -m "Publish Issue #N: [Title]"
git push origin main
```

---

## Post-Publication SEO

### Google Search Console
1. Go to [Google Search Console](https://search.google.com/search-console)
2. URL Inspection > Enter new issue URL
3. Request indexing

### Validate Rich Results
1. Go to [Rich Results Test](https://search.google.com/test/rich-results)
2. Enter issue URL
3. Verify NewsArticle schema passes

### Verify Sitemap
1. Search Console > Sitemaps
2. Confirm sitemap.xml shows updated date
3. Check for any crawl errors

---

## Issue Numbering

| Issue # | Date | Theme |
|---------|------|-------|
| 1 | Oct 5, 2025 | Inaugural - Fusion AI |
| 2 | Oct 13, 2025 | Microsoft GB300 |
| 3 | Nov 3, 2025 | OpenAI DevDay |
| 4 | Dec 3, 2025 | AI Cyber Espionage |
| 5 | Dec 17, 2025 | AAIF/MCP Foundation |

---

## Support

For questions about the newsletter process, contact:
- **GitHub:** [@shashwatgtm](https://github.com/shashwatgtm)
- **LinkedIn:** [Shashwat Ghosh](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)
