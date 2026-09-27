# Offbeat AI Watch

![Offbeat AI Watch](https://img.shields.io/badge/Status-Active-success)
![Issue](https://img.shields.io/badge/Latest-Issue%20%236-blue)

**Unconventional AI insights delivered fortnightly.**

Offbeat AI Watch is a curated fortnightly intelligence brief that distills the signal from the noise in artificial intelligence. Beyond the headlines, we surface the stories that matter.

## 🎯 What We Cover

- **Infrastructure & Compute**: AI hardware deployments, custom silicon strategies, and datacenter buildouts
- **Strategic Partnerships**: Cross-industry alliances reshaping the AI landscape
- **Product Launches**: New AI capabilities hitting the market
- **Regulatory Developments**: Policy shifts across jurisdictions
- **Emerging Trends**: Pattern recognition across AI developments

## 📬 Subscribe

Visit [gtmhelix.com/ai-trendwatch](https://gtmhelix.com/ai-trendwatch/) to subscribe and receive fortnightly updates on alternate Wednesdays.

## 📰 Latest Issue

**Issue #6 - January 7, 2026**

- 🔍 **Lead Story**: Google's AI Content Reckoning: December 2025 Core Update Changes Everything
- 🤖 **Meta-Manus $2B**: Meta acquires AI agent startup with $100M ARR
- 💰 **Nvidia-Groq $20B**: Largest AI infrastructure deal, signals inference market shift
- 🔒 **ServiceNow-Armis $7.75B**: Enterprise security consolidation accelerates
- 🇨🇳 **China 700+ Models**: Unprecedented government-cleared AI deployment scale
- 🇮🇳 **India SOAR Initiative**: President Murmu launches #SkilltheNation AI challenge

[Read Issue #6 →](issues/2026-01-07.html)

## 📚 Archive

- [January 7, 2026](issues/2026-01-07.html) - Issue #6: Google's AI Content Reckoning: December 2025 Core Update
- [December 17, 2025](issues/2025-12-17.html) - Issue #5: Tech Giants Unite: Agentic AI Foundation Launches
- [December 3, 2025](issues/2025-12-03.html) - Issue #4: First AI-Orchestrated Cyber Espionage Campaign Disclosed
- [November 3, 2025](issues/2025-11-03.html) - Issue #3: OpenAI DevDay Spotlights Enterprise-Ready Agents
- [October 13, 2025](issues/2025-10-13.html) - Issue #2: Microsoft's GB300 AI Factory
- [October 5, 2025](issues/2025-10-05.html) - Inaugural Issue: Fusion Energy Gets AI Shield

## 👤 About

Curated by **Shashwat Ghosh**
Co-Founder and Fractional CMO, Helix GTM Consulting
AI Go-To-Market Strategist

**Connect:**
- LinkedIn: [linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)
- Newsletter: [Offbeat AI Watch](https://gtmhelix.com/ai-trendwatch/)
- GitHub: [@shashwatgtm](https://github.com/shashwatgtm)

---

## 🛠 Technical Details

This newsletter is built with:
- Pure HTML/CSS (no frameworks)
- Hosted on GoDaddy Managed WordPress (subfolder: `/ai-trendwatch/`)
- Mobile-responsive design
- Dark theme (#151617 background, #FAA1A1 accent)
- SEO and Schema.org structured data

## 🚀 Deployment Guide

### Automatic Deployment
Push to `main` branch triggers GitHub Actions workflow that deploys to GoDaddy via SFTP.

### Critical Path Configuration
```
SFTP uploads to: html/ai-trendwatch/
Web serves from: gtmhelix.com/ai-trendwatch/
```

### Image Naming Convention
All images must use exact filenames as listed in `images/` folder:
- `google-core-update-eeat-1280x680.jpg` (NOT google-dec-2025...)
- `anthropic-ai-cyber-espionage-1280x680.jpg` (NOT ai-cyber-espionage...)
- `openai-devday-agentkit-1280x680.jpg` (NOT openai-devday-2025...)
- `aaif-mcp-foundation-1280x680.jpg`
- `msft-azure-gb300-1280x680-1.jpg`

### Post-Deployment Checklist
1. ✅ Check GitHub Actions → "Deploy to GoDaddy" succeeded
2. ✅ Go to GoDaddy → Settings → Flush Cache
3. ✅ Wait 5-15 minutes for CDN propagation
4. ✅ Test in Incognito + Hard Refresh (Ctrl+Shift+R)

### Troubleshooting
- **Files not updating**: Verify `deploy.yml` uses `cd html/ai-trendwatch` (NOT just `ai-trendwatch`)
- **Images broken**: Check exact filename match in `images/` folder
- **Caching issues**: Add `?v=timestamp` to URL for testing

## 📝 Lessons Learned (RCA)

| Issue | Root Cause | Prevention |
|-------|-----------|------------|
| Deploy succeeds but files not updating | Wrong SFTP path (`ai-trendwatch/` vs `html/ai-trendwatch/`) | Always verify path in deploy.yml |
| Broken images | Filename mismatch in HTML vs actual files | Use exact filenames from images/ folder |
| Old design showing after deploy | CDN caching | Always flush GoDaddy cache after deploy |
| Redirect loops on issue pages | Migration created redirect stubs | Never use redirect stubs, always full content |
| Light mode CSS incomplete | `@media (prefers-color-scheme: light)` missing some CSS classes | Add ALL CSS classes to light mode override, especially `.tech-*`, `.mini-*`, `.category-header` |
| Email form goes to wrong newsletter | Homepage form action pointed to `gtmexpert.substack.com` instead of Formspree | Always use Formspree endpoint: `https://formspree.io/f/mnngzoee` |

### Email Subscription Configuration
The homepage uses Formspree for email collection:
```html
<form action="https://formspree.io/f/mnngzoee" method="POST">
```
Issue pages use Google Reader Revenue Manager (separate from homepage form).

## 📄 License

© 2026 Offbeat AI Watch. All rights reserved.

---

**Fortnightly Intelligence Brief** • Delivered alternate Wednesdays
