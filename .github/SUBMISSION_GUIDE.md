# Offbeat AI Watch - Issue Submission Guide

## Quick Reference

### Live Site
**URL:** https://gtmhelix.com/ai-trendwatch/

### Image Sizes
- **Cover Image:** 1280 x 680 pixels
- **Social Image:** 1200 x 630 pixels

### File Naming
- Cover: `{topic}-1280x680.jpg`
- Social: `offbeat-ai-watch-issue{n}-social.jpg`

---

## Publishing Workflow (Automatic Deployment)

### Step 1: Create Issue HTML
```
issues/YYYY-MM-DD.html
```
- Copy previous issue as template
- Update all content, meta tags, dates
- Verify Schema.org data
- Update all URLs to use `gtmhelix.com/ai-trendwatch/`

### Step 2: Add Images
Upload to `/images/` folder:
- Cover image: `{topic}-1280x680.jpg`
- Social image: `offbeat-ai-watch-issue{n}-social.jpg`

### Step 3: Update Sitemap
Add to `sitemap.xml`:
```xml
<url>
  <loc>https://gtmhelix.com/ai-trendwatch/issues/YYYY-MM-DD.html</loc>
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

Also add to `sitemap-news.xml`.

### Step 4: Update RSS Feed
Add new item at TOP of `feed.xml`:
```xml
<item>
  <title>Issue Title - Offbeat AI Watch</title>
  <link>https://gtmhelix.com/ai-trendwatch/issues/YYYY-MM-DD.html</link>
  <description>Issue description here</description>
  <pubDate>Day, DD Mon YYYY 00:00:00 GMT</pubDate>
  <guid>https://gtmhelix.com/ai-trendwatch/issues/YYYY-MM-DD.html</guid>
  <author>Shashwat Ghosh</author>
  <category>Artificial Intelligence</category>
</item>
```

### Step 5: Update Supporting Files
- [ ] `archive.html` - Add new issue to archive list
- [ ] `index.html` - Update "Latest Issue" preview section

### Step 6: Commit & Push (Auto-Deploys!)
```bash
git add .
git commit -m "Publish Issue #N: [Title]"
git push origin main
```

**That's it!** GitHub Actions automatically deploys to GoDaddy.

Check deployment status: https://github.com/shashwatgtm/ai-trendwatch/actions

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
- [ ] Images in `/images/` folder

### SEO Ready
- [ ] Unique `<title>` tag (50-60 chars)
- [ ] Meta description (under 160 chars)
- [ ] Open Graph tags updated
- [ ] Twitter Card tags updated
- [ ] Canonical URL set to `gtmhelix.com/ai-trendwatch/issues/...`
- [ ] Schema.org NewsArticle data updated

### Files Updated
- [ ] `issues/YYYY-MM-DD.html` created
- [ ] `sitemap.xml` updated
- [ ] `sitemap-news.xml` updated
- [ ] `feed.xml` updated
- [ ] `archive.html` updated
- [ ] `index.html` updated

---

## Post-Publication SEO

### Google Search Console
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select property: `https://gtmhelix.com/ai-trendwatch/`
3. URL Inspection → Enter new issue URL
4. Click **Request Indexing**

### Validate Rich Results
1. Go to [Rich Results Test](https://search.google.com/test/rich-results)
2. Enter issue URL
3. Verify NewsArticle schema passes

### Verify Sitemap
1. Search Console → Sitemaps
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
| 6 | Jan 7, 2026 | Google December 2025 Core Update |

---

## URL Reference

### Old URLs (Redirect to New)
```
shashwatgtm.github.io/ai-trendwatch/  →  gtmhelix.com/ai-trendwatch/
```

### Current URLs (Use These)
```
https://gtmhelix.com/ai-trendwatch/
https://gtmhelix.com/ai-trendwatch/archive.html
https://gtmhelix.com/ai-trendwatch/issues/YYYY-MM-DD.html
https://gtmhelix.com/ai-trendwatch/sitemap.xml
https://gtmhelix.com/ai-trendwatch/feed.xml
```

---

## Troubleshooting

### Deployment Not Working?
1. Check GitHub Actions: https://github.com/shashwatgtm/ai-trendwatch/actions
2. Look for red X on latest workflow run
3. Click to see error details
4. Common fixes:
   - Regenerate SFTP credentials in GoDaddy
   - Update GitHub Secrets

### Page Shows 404?
1. Verify file was committed to GitHub
2. Check GitHub Actions completed successfully
3. Clear browser cache (Ctrl+Shift+R)
4. Check `.htaccess` on GoDaddy if directory URL fails

### Images Not Loading?
1. Verify image path in HTML matches actual file location
2. Check image was uploaded to `/images/` folder
3. Ensure filename matches exactly (case-sensitive)

---

## Support

For questions about the newsletter process:
- **GitHub:** [@shashwatgtm](https://github.com/shashwatgtm)
- **LinkedIn:** [Shashwat Ghosh](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)

---

*Last updated: January 10, 2026*
