# Offbeat AI Watch - Newsletter Creation Guidelines

## Overview
This guide covers the complete process for creating new newsletter editions, including content selection, SEO optimization, and quality standards.

---

## Content Selection Standards

### Lead Story Selection
- Choose stories that are **genuinely "offbeat"** - not mainstream headlines
- Prefer **first-of-its-kind events** with real implications
- Avoid stories already covered in previous editions
- Must have **verifiable sources** from official company blogs or trusted publishers

### Signal Stories Selection (6-7 stories)
- **Concrete, verifiable news** that has actually happened
- Avoid speculative stories ("considering", "nearing", "planning")
- Must be recent (within 2-3 weeks)
- Each story needs a direct link to reputable source

### Trends to Watch (4-5 trends)
- **Must correlate back to chosen stories** - create a mapping table
- At least one trend should align with author's EEAT expertise (GTM, positioning, B2B marketing)
- Avoid trends outside author's domain expertise (e.g., biotech/pharma details)
- Use pattern: Story X + Story Y = Trend insight

---

## Link Quality Standards

### Approved Sources (Use These)
- **Official Company Blogs**: Microsoft Research, Google Research, DeepMind, Anthropic, OpenAI
- **Major News Outlets**: Reuters, Fortune, TechCrunch, The Verge, Bloomberg, Axios
- **Press Releases**: Business Wire, PR Newswire
- **Academic Sources**: MIT News, arXiv, Nature
- **Product Platforms**: Product Hunt (for startup launches)

### Avoid These Sources
- Paywalled sites: WSJ, Financial Times, Barron's
- Low-reputation aggregators
- Social media links (Twitter, LinkedIn posts) - except for author's own take
- Sites requiring login/registration
- Speculative or rumor-based articles

### Link Verification Rules
- **Test all links** before committing
- Use the **exact URL** provided by the source
- All external links must have `rel="noopener" target="_blank"`
- Never repeat the same link across different sections

---

## Layout Requirements

### Lead Story Section (65% width)
- Cover image: 1280 x 680 pixels
- Image caption with source attribution
- 2-3 paragraphs of content
- "Bottom line" summary statement
- Multiple source links (official + news coverage + author's take if available)

### Editor's Note (35% width, aligned to bottom)
- CSS: `display: flex; flex-direction: column; justify-content: flex-end;`
- Explain any publication gaps (async breaks)
- Connect to lead story's significance
- Sign off with name, title, company

### Signal Stories Grid
- 2-column grid layout
- 6-7 stories total
- Last story can span full width (`story-item-full` class)
- Each story: headline, description, source link

### Trends to Watch Grid
- 2-column grid layout
- 4-5 trends total
- Last trend can span full width (`trend-item-full` class)
- Each trend: emoji icon, title, description

---

## SEO Checklist (Required for Every Issue)

### 1. HTML Meta Tags
```html
<title>[Headline] - Offbeat AI Watch</title>
<meta name="description" content="[Under 160 chars with key topics]">
<meta name="keywords" content="[Comma-separated keywords]">
```

### 2. Open Graph Tags (LinkedIn/Facebook)
```html
<meta property="og:title" content="[Same as page title]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="[Full URL to social image]">
<meta property="og:url" content="[Canonical URL]">
```

### 3. Twitter Card Tags
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Same as page title]">
<meta name="twitter:description" content="[Same as meta description]">
<meta name="twitter:image" content="[Full URL to social image]">
```

### 4. Schema.org JSON-LD
- NewsArticle schema with headline, description, dates
- Author Person schema with credentials
- Publisher Organization schema
- "about" entities linking to Wikipedia

### 5. Files to Update
- [ ] `issues/YYYY-MM-DD.html` - Main issue file
- [ ] `archive.html` - Add issue entry at top
- [ ] `feed.xml` - Add RSS item at top, update lastBuildDate
- [ ] `sitemap.xml` - Add URL entry, update lastmod dates
- [ ] `index.html` - Update "Latest Issue" section

---

## Image Requirements

### Cover Image (Lead Story)
- **Filename**: `[topic]-1280x680.jpg`
- **Dimensions**: 1280 x 680 pixels
- **Format**: JPG
- **Source**: Official company imagery or reputable news outlet
- **Alt text**: Descriptive, includes key terms

### Social Media Image (Optional)
- **Filename**: `offbeat-ai-watch-issue[X]-social.jpg`
- **Dimensions**: 1200 x 630 pixels
- **Location**: `/images/` folder

---

## EEAT Compliance

### Experience
- Reference author's hands-on B2B GTM work
- Include specific examples from consulting practice

### Expertise
- "Fractional CMO & AI GTM Expert" positioning
- Focus areas clearly listed in bio

### Authoritativeness
- Helix Consulting affiliation
- LinkedIn profile links
- GitHub profile links

### Trustworthiness
- Complete author bio section
- Verifiable credentials
- Schema.org Person markup

---

## Mobile Responsive Requirements
- Breakpoint: `@media (max-width: 600px)`
- Stack flex layouts to block
- Reduce font sizes appropriately
- Adjust padding for mobile

---

## Pre-Publication Checklist

### Content
- [ ] Lead story is verifiable and "offbeat"
- [ ] No duplicate stories from previous editions
- [ ] All links tested and working
- [ ] No speculative/rumor-based news
- [ ] Trends map back to stories
- [ ] At least one trend aligns with author EEAT

### SEO
- [ ] All meta tags updated
- [ ] Schema.org keywords updated
- [ ] sitemap.xml updated with new issue
- [ ] feed.xml updated with new item
- [ ] archive.html updated
- [ ] index.html latest issue updated

### Layout
- [ ] Cover image displays correctly
- [ ] Editor note aligns to bottom
- [ ] Mobile responsive verified
- [ ] All external links open in new tab

---

## Commit Message Template

```
Create Issue #X: [Main Headline]

Content:
- Add newsletter issue for [date]
- Lead story: [brief description]
- Signal stories: [list key stories]
- X Trends to watch

SEO:
- Update all meta descriptions
- Add Schema.org keywords
- Update feed.xml, sitemap.xml, archive.html, index.html

Layout:
- [Any layout changes made]
```

---

## Troubleshooting

### Issue: Editor note has gap below
**Fix**: Add `display: flex; flex-direction: column; justify-content: flex-end;` to `.editor-note-box`

### Issue: Links not working
**Fix**: Verify exact URL, ensure `target="_blank" rel="noopener"` present

### Issue: Images not showing
**Fix**: Check path is `../images/filename.jpg` for issue pages

### Issue: Mobile layout broken
**Fix**: Verify `@media` query converts grid/flex to block

---

Last Updated: December 3, 2025 (Issue #4)
