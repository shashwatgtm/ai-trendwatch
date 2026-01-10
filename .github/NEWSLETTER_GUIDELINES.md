# Offbeat AI Watch - Newsletter Guidelines

## Publication Details

| Property | Value |
|----------|-------|
| **Live Site** | https://gtmhelix.com/ai-trendwatch/ |
| **Frequency** | Fortnightly (every alternate Wednesday) |
| **Target Audience** | B2B leaders, GTM professionals, AI practitioners |
| **Hosting** | GoDaddy Managed WordPress (subfolder) |
| **Deployment** | Automatic via GitHub Actions |

---

## Author Credentials (CRITICAL)

### Official Designation
**Shashwat Ghosh - Cofounder & Fractional CMO**

**DO NOT USE:**
- ~~GTM Alpha Consultant~~
- ~~GTM Alpha Consultant & Fractional CMO~~

### Exit Stories Format
**CORRECT:** "GTM leadership at exits including Happay (sold to CRED, later MakeMyTrip) and Locus (sold to IKEA)"

**WRONG:** ~~"3 successful exits ($180M+)"~~ (too vague, not verifiable)

### Knowledge Graph Signals (Schema)
```json
{
  "jobTitle": "Cofounder & Fractional CMO",
  "worksFor": {
    "@type": "Organization",
    "name": "Helix GTM Consulting",
    "foundingDate": "2016"
  },
  "knowsAbout": [
    "AI Go-To-Market Strategy",
    "Enterprise AI Adoption",
    "B2B Marketing & Positioning",
    "Fractional CMO Services",
    "Sales Enablement"
  ],
  "award": [
    "Most Admired Marketing Leaders 2025",
    "B2B Marketer 2020",
    "LinkedIn Top Voice #10 India"
  ],
  "sameAs": [
    "LinkedIn profile",
    "Substack",
    "GitHub"
  ]
}
```

---

## Editorial Content Guidelines

### Cover Story Selection (ALWAYS 3 OPTIONS)

When selecting a cover story, **ALWAYS present 3 options with rationale**:

```
OPTION 1: [Story Title]
- Rationale: Why this matters for B2B/Enterprise
- EEAT signal: How it aligns with Shashwat's positioning
- Timeliness: Is it fresh and newsworthy?

OPTION 2: [Story Title]
- Rationale: ...
- EEAT signal: ...
- Timeliness: ...

OPTION 3: [Story Title]
- Rationale: ...
- EEAT signal: ...
- Timeliness: ...

RECOMMENDATION: Option X because...
```

### Story Sourcing Guidelines

**DO:**
- Search for diverse, OFFBEAT stories
- Look for stories impacting B2B startups, ITeS, Telecom, Enterprise/MidMarket/SMB
- Find stories that align with Shashwat's positioning
- Use Google Search for genuinely diverse stories from the timeframe
- Look at raw content sources, not just LLM aggregations

**DON'T:**
- Be lazy with model release announcements
- Focus only on LLM/chip/hardware news
- Rely solely on obvious AI headlines
- Skip the research step

### Target Industries/Communities

Stories should impact these communities:
- B2B Startups
- ITeS (IT-enabled Services)
- Telecom
- Enterprise Software
- MidMarket Companies
- SMB Technology Adoption

### EEAT Positioning Alignment

Stories should demonstrate expertise in:
- **AI Go-To-Market strategy** - How companies launch and sell AI products
- **Enterprise AI adoption patterns** - How large orgs evaluate and deploy AI
- **B2B positioning and pricing** - How AI vendors position themselves
- **Sales enablement in the AI era** - How AI changes B2B selling
- **How companies actually buy and deploy AI** - The real procurement process

### Trend Writing

For "Trends to Watch" section:
- Always include **reader insight** (what this means for them)
- Search for recent reports from the chosen timeframe
- Connect trends to actionable business implications

**Example:**
```
TREND: Enterprise AI Budget Shifts
INSIGHT: "If you're pitching AI to enterprises in Q1,
expect longer procurement cycles as budgets reallocate
from experimental to production workloads."
```

---

## SEO Optimization Goals

### Understanding the Three Pillars

**1. LLM Citability**
- Content structure makes it accessible FOR LLMs to cite
- Achieved via proper schema markup, clear headings, structured data
- NOT listed as a skill Shashwat "knows about"

**2. GNN Candidate Generation**
- These expertise topics are what Google should associate WITH Shashwat Ghosh
- The knowsAbout field establishes topic associations
- NOT listed as a skill Shashwat "knows about"

**3. EEAT Signals**
- Schema establishes Shashwat's expertise IN his domain areas
- NOT "expertise in EEAT" itself
- Demonstrated through: credentials, exit stories, awards, verifiable work

### Footer Optimization
Include in footer: "Optimized for SEO, LLM citability, and GNN candidate generation"

---

## Content Syndication Platforms

### Platform-Specific Formatting

| Platform | Format Style | Notes |
|----------|-------------|-------|
| **Medium** | Narrative-driven, opinionated, clear takeaways | Use Medium toolbar for headings |
| **Dev.to** | Clean, no nested code blocks | Technical audience |
| **Quora** | Article format | Good for reach |
| **DZone** | Technical focus | Developer audience |
| **Vocal Media** | Storytelling format | General audience |
| **Newsbreak** | News-style | Broader distribution |

### Platforms to Avoid (For Now)
- ~~LinkedIn Articles~~ (not prioritized currently)
- ~~Reddit~~ (problematic for this content type)
- ~~India Hackers~~ (didn't work previously)

---

## Deployment Workflow

### Automatic Deployment (Recommended)
1. Edit files in Claude Code or locally
2. Commit and push to `main` branch
3. GitHub Actions automatically deploys to GoDaddy via SFTP

```bash
git add .
git commit -m "Publish Issue #N: [Title]"
git push origin main
```

### Check Deployment Status
https://github.com/shashwatgtm/ai-trendwatch/actions

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

### Social Sharing Image (OG/Twitter)
| Property | Value |
|----------|-------|
| **Dimensions** | 1200 x 630 pixels |
| **Aspect Ratio** | ~1.91:1 |
| **Format** | JPG |
| **Naming Convention** | `offbeat-ai-watch-issue{n}-social.jpg` |
| **Location** | `/images/` |

---

## Schema.org Requirements

### NewsArticle Schema
- [ ] Headline, description, dates
- [ ] Author with proper jobTitle: "Cofounder & Fractional CMO"
- [ ] Publisher with logo
- [ ] Proper knowsAbout fields (NOT optimization techniques)

### Author Schema Updates (All Issues)
When updating old issues, ensure:
- [ ] jobTitle: "Cofounder & Fractional CMO"
- [ ] Exit stories use specific company names
- [ ] knowsAbout includes GTM/B2B expertise areas
- [ ] Awards listed properly
- [ ] sameAs includes all profile links

---

## File Updates Per Issue

| File | Update Required |
|------|-----------------|
| `issues/YYYY-MM-DD.html` | Create new issue HTML |
| `sitemap.xml` | Add new issue URL with news:news metadata |
| `sitemap-news.xml` | Add new issue to news sitemap |
| `feed.xml` | Add new item at top of RSS feed |
| `archive.html` | Add new issue to archive list |
| `index.html` | Update "Latest Issue" preview section |

---

## Google Search Console

### Property Details
- **URL:** https://gtmhelix.com/ai-trendwatch/
- **Sitemaps Submitted:**
  - sitemap-index.xml
  - sitemap.xml
  - sitemap-news.xml

### After Publishing Each Issue
1. URL Inspection → Submit new issue URL
2. Request Indexing
3. Rich Results Test → Validate schema
4. Mobile-Friendly Test

---

## Internal Linking

Each issue should include a "Previous Issues" section before the footer:

```html
<section class="related-issues">
    <h3>Previous Issues</h3>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
        <a href="2025-12-17.html">
            <span>ISSUE #5</span>
            <div>Tech Giants Unite: Agentic AI Foundation</div>
        </a>
        <!-- More issues... -->
    </div>
</section>
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

## URL Structure

### Current Domain (Use These)
```
https://gtmhelix.com/ai-trendwatch/
https://gtmhelix.com/ai-trendwatch/archive.html
https://gtmhelix.com/ai-trendwatch/issues/YYYY-MM-DD.html
```

### Old Domain (Redirects Automatically)
```
shashwatgtm.github.io/ai-trendwatch/ → gtmhelix.com/ai-trendwatch/
```

---

## Quick Reference Checklist

### Before Writing
- [ ] 3 cover story options with rationale prepared
- [ ] Stories searched for diversity (not just LLM news)
- [ ] Stories align with Shashwat's positioning
- [ ] Target industries considered (B2B, ITeS, Telecom, Enterprise)

### During Writing
- [ ] Trends include reader insight
- [ ] Author designation: "Cofounder & Fractional CMO"
- [ ] Exit stories use specific company names
- [ ] EEAT signals in content (not just schema)

### Schema Check
- [ ] knowsAbout = GTM/B2B expertise (NOT optimization techniques)
- [ ] jobTitle = "Cofounder & Fractional CMO"
- [ ] Exit stories = specific companies, not dollar amounts
- [ ] Footer includes optimization note

---

## Contact

**Curator:** Shashwat Ghosh
**Role:** Cofounder & Fractional CMO, Helix GTM Consulting
**LinkedIn:** [linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo](https://www.linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo/)

---

*Last updated: January 10, 2026*
