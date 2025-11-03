# Offbeat AI Watch - Newsletter Creation Guidelines

## 📋 Product Selection Standards

### What to Include
- **NEW product launches** from the last 2-3 weeks only
- Enterprise/midmarket/B2B focused products
- Products NOT already covered in "This Edition's Signal" section
- 4 products total in 2x2 grid layout

### What to Avoid
- Consumer-only products
- Products already mentioned in other sections
- Research models/papers (unless they have commercial releases)
- Products older than 3 weeks

---

## 🔗 Link Quality Standards

### ✅ APPROVED Sources (Use These)
- **Official Company Pages**: OpenAI.com, Microsoft.com, Google.com, etc.
- **Product Hunt**: For startup product launches
- **Major News Outlets**: Reuters, CNBC, TechCrunch, The Verge, Bloomberg
- **Official Tech Communities**: Microsoft Tech Community, Google Developers
- **Industry Publications**: InfoQ, VentureBeat

### ❌ AVOID These Sources
- Paywalled sites: WSJ, Financial Times, Barron's
- Low-reputation blogs: aiapps.com, generic AI news aggregators
- Indian news sites (unless specifically requested)
- Social media links (Twitter, LinkedIn posts)
- Sites requiring login/registration

### Link Diversity Rules
- **NEVER repeat the same link** across different sections
- Use different sources for each news item
- If multiple items from same company, use different official pages

---

## 🎨 Layout Requirements

### Product Section
- **Format**: 2x2 grid (4 products)
- **Mobile**: Stacks vertically on small screens
- **Each product needs**:
  - Product name
  - 2-3 sentence description (focus on business value)
  - Link to reputable source

### Editor's Note
- Must be **balanced** with lead story (no excessive blank space below)
- Should mention:
  - Key product launch from the issue
  - Most important trend
- Length: 3-4 sentences minimum

---

## 🔍 SEO Checklist (MUST DO for Every Issue)

### 1. HTML Meta Tags (in issue HTML file)
```html
<title>Clear, descriptive title under 60 chars</title>
<meta name="description" content="Under 160 chars with key products">
```

### 2. Open Graph Tags (for LinkedIn/Facebook)
```html
<meta property="og:title" content="Same as page title">
<meta property="og:description" content="Same as meta description">
<meta property="og:image" content="Social image 1200x630">
```

### 3. Twitter Card Tags
```html
<meta name="twitter:title" content="Same as page title">
<meta name="twitter:description" content="Same as meta description">
<meta name="twitter:image" content="Social image 1200x630">
```

### 4. Schema.org Keywords
Update keywords in JSON-LD to include:
- Main product names
- Technology categories
- Key trends
Example: "Ada AI Data Analyst, Peakflo AI Voice Agents, autonomous data analysis, AI voice automation"

### 5. Update ALL These Files
- [ ] `issues/YYYY-MM-DD.html` - Main issue file
- [ ] `archive.html` - Issue excerpt
- [ ] `feed.xml` - RSS feed description + categories
- [ ] `sitemap.xml` - Already auto-updated with dates
- [ ] `index.html` - Latest issue preview

---

## 📊 RSS Feed Categories

### Standard Categories (Always Include)
- Artificial Intelligence
- Technology
- Enterprise AI

### Add Based on Content
- OpenAI (if OpenAI featured)
- Agentic AI (if agent products)
- Data Analysis (if data tools)
- Voice Automation (if voice AI)
- Healthcare AI (if health products)
- Cloud Computing (if cloud focus)

---

## 🖼️ Image Requirements

### Cover Image (for article)
- **Filename**: `product-name-1280x680.jpg`
- **Dimensions**: 1280 x 680 pixels
- **Format**: JPG
- **Content**: Related to main story/product

### Social Media Image
- **Filename**: `offbeat-ai-watch-issueX-social.jpg`
- **Dimensions**: 1200 x 630 pixels
- **Format**: JPG
- **Location**: `/images/` folder

---

## ✅ Pre-Publication Checklist

Before creating PR, verify:

### Content
- [ ] 4 unique products (not in "This Edition's Signal")
- [ ] All links from reputable, non-paywalled sources
- [ ] No duplicate links across sections
- [ ] Editor's note is balanced with lead story
- [ ] All product descriptions focus on business value

### SEO
- [ ] HTML meta description updated
- [ ] Open Graph description updated
- [ ] Twitter description updated
- [ ] Schema.org keywords include new products
- [ ] archive.html excerpt updated
- [ ] feed.xml description + categories updated
- [ ] index.html latest issue updated

### Images
- [ ] Cover image added (1280x680)
- [ ] Social image added (1200x630)
- [ ] Both images in `/images/` folder

### Links
- [ ] All links tested and working
- [ ] No paywalled sources
- [ ] Link diversity across sections
- [ ] All external links have `rel="noopener" target="_blank"`

---

## 🚀 Deployment Process

1. **Create branch**: `claude/issue-X-[session-id]`
2. **Commit changes** with descriptive message
3. **Push to GitHub**
4. **Create Pull Request**
5. **Merge to main branch**
6. **Wait 3-5 minutes** for GitHub Pages deployment
7. **Verify live site**

---

## 📝 Commit Message Template

```
Create Issue #X: [Main Headline]

Content:
- Add newsletter issue for [date]
- Cover [key topics]
- Feature products: [Product 1], [Product 2], [Product 3], [Product 4]

SEO:
- Update all meta descriptions
- Add Schema.org keywords
- Update feed.xml and archive.html

Images:
- [cover-image-name.jpg] - Main story visual
- [social-image-name.jpg] - Social media sharing
```

---

## 🔧 Troubleshooting Common Issues

### Issue: Blank page with blue background
**Cause**: newsletter-signup.html has conflicting styles
**Fix**: Ensure newsletter-signup.html contains ONLY scripts (no HTML structure)

### Issue: Products section stacked vertically
**Cause**: CSS grid not applied
**Fix**: Check `.product-list` has `display: grid; grid-template-columns: repeat(2, 1fr);`

### Issue: Links not opening
**Cause**: Missing target="_blank"
**Fix**: Add `target="_blank" rel="noopener"` to all external links

### Issue: Images not showing
**Cause**: Wrong file path or filename
**Fix**: Check image is in `/images/` and filename matches HTML exactly

---

## 📞 Support Resources

- **GitHub Issues**: Report bugs at https://github.com/shashwatgtm/ai-trendwatch/issues
- **Newsletter Archive**: https://shashwatgtm.github.io/ai-trendwatch/archive.html
- **Live Site**: https://shashwatgtm.github.io/ai-trendwatch/

---

Last Updated: November 3, 2025
