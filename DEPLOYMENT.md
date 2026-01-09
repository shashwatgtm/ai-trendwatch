# Deployment Guide - Offbeat AI Watch

## Current Hosting Setup

**Live Site:** https://gtmhelix.com/ai-trendwatch/

| Component | Details |
|-----------|---------|
| **Hosting** | GoDaddy Managed WordPress |
| **Domain** | gtmhelix.com (aged domain for SEO) |
| **Subfolder** | /ai-trendwatch/ |
| **Deployment** | Automatic via GitHub Actions |
| **Old URL** | shashwatgtm.github.io/ai-trendwatch (redirects to new domain) |

---

## Quick Start: Publishing New Content

### The Simple Workflow

1. **Edit files** in Claude Code or locally
2. **Commit and push** to `main` branch
3. **Done!** Files automatically deploy to GoDaddy via SFTP

```bash
git add .
git commit -m "Publish Issue #N: [Title]"
git push origin main
```

GitHub Actions will automatically:
- Connect to GoDaddy via SFTP
- Upload all changed files to `/ai-trendwatch/` folder
- Exclude unnecessary files (.git, .github, README.md, etc.)

---

## Architecture Overview

### Domain Structure
```
gtmhelix.com/                    ← WordPress site (Helix Consulting)
├── wp-admin/
├── wp-content/
├── wp-includes/
├── ai-trendwatch/               ← Newsletter (static HTML)
│   ├── index.html
│   ├── archive.html
│   ├── issues/
│   │   ├── 2025-10-05.html
│   │   ├── 2025-10-13.html
│   │   └── ...
│   ├── images/
│   ├── sitemap.xml
│   ├── sitemap-news.xml
│   ├── sitemap-index.xml
│   ├── robots.txt
│   └── feed.xml
└── .htaccess                    ← Controls redirects & routing
```

### GitHub Repository Structure
```
ai-trendwatch/
├── .github/
│   ├── workflows/
│   │   └── deploy.yml           ← Auto-deployment workflow
│   ├── NEWSLETTER_GUIDELINES.md
│   └── SUBMISSION_GUIDE.md
├── issues/                      ← Newsletter HTML files
├── images/                      ← Newsletter images
├── index.html                   ← Landing page
├── archive.html                 ← All issues archive
├── sitemap.xml                  ← Main sitemap
├── sitemap-news.xml             ← Google News sitemap
├── sitemap-index.xml            ← Sitemap index
├── robots.txt
├── feed.xml                     ← RSS feed
└── DEPLOYMENT.md                ← This file
```

---

## GitHub Actions Deployment

### How It Works

The workflow file `.github/workflows/deploy.yml` handles automatic deployment:

```yaml
name: Deploy to GoDaddy

on:
  push:
    branches:
      - main
  workflow_dispatch:  # Manual trigger option

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install lftp
        run: sudo apt-get update && sudo apt-get install -y lftp

      - name: Deploy via SFTP
        run: |
          lftp -u "${{ secrets.FTP_USERNAME }},${{ secrets.FTP_PASSWORD }}" \
            -e "set sftp:auto-confirm yes; \
            mkdir -p ai-trendwatch; \
            mirror -R --verbose --exclude .git/ --exclude .github/ ... \
            ./ ai-trendwatch/; quit" \
            sftp://${{ secrets.FTP_SERVER }}
```

### Required GitHub Secrets

These secrets must be configured in: `Settings → Secrets and variables → Actions`

| Secret Name | Value |
|-------------|-------|
| `FTP_SERVER` | `r55.c1c.myftpupload.com` |
| `FTP_USERNAME` | (SFTP username from GoDaddy) |
| `FTP_PASSWORD` | (SFTP password from GoDaddy) |

### Getting SFTP Credentials from GoDaddy

1. Go to GoDaddy → My Products → Managed WordPress
2. Click **Manage** on your site
3. Go to **Settings** → Look for **SSH/SFTP**
4. Click **Create New Login**
5. Save the username and password immediately (shown only once)

---

## .htaccess Configuration

The `.htaccess` file in GoDaddy's root directory contains:

```apache
# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Force non-www
RewriteCond %{HTTP_HOST} ^www\.gtmhelix\.com [NC]
RewriteRule ^(.*)$ https://gtmhelix.com/$1 [L,R=301]

# Serve index.html for ai-trendwatch directory
RewriteRule ^ai-trendwatch/?$ /ai-trendwatch/index.html [L]

# WordPress rules below...
```

**Important:** This file is on GoDaddy, NOT in the GitHub repo. Edit via GoDaddy File Manager if changes are needed.

---

## Google Search Console

### Property Setup
- **Property URL:** `https://gtmhelix.com/ai-trendwatch/`
- **Verification:** HTML file (`google87795e2cfa947d33.html`)

### Submitted Sitemaps
| Sitemap | Purpose | URLs |
|---------|---------|------|
| `sitemap-index.xml` | Index of all sitemaps | - |
| `sitemap.xml` | All pages | ~10 |
| `sitemap-news.xml` | News articles only | 6 (issues) |

### After Publishing New Issue
1. Go to Google Search Console
2. URL Inspection → Enter new issue URL
3. Click **Request Indexing**

---

## 301 Redirects

### Old GitHub Pages → New Domain

The old GitHub Pages site (`shashwatgtm.github.io/ai-trendwatch`) automatically redirects to the new domain. All HTML files in the GitHub repo contain redirect code:

```html
<meta http-equiv="refresh" content="0; url=https://gtmhelix.com/ai-trendwatch/">
<script>window.location.replace("https://gtmhelix.com/ai-trendwatch/");</script>
```

This preserves SEO link equity from any old backlinks.

---

## Troubleshooting

### Deployment Failed?
1. Check GitHub Actions tab for error logs
2. Verify SFTP credentials in GitHub Secrets
3. Check if GoDaddy SFTP is enabled

### Site Not Updating?
1. Clear browser cache (Ctrl+Shift+R)
2. Check GitHub Actions completed successfully
3. Wait 1-2 minutes for CDN propagation

### 404 Error on gtmhelix.com/ai-trendwatch/?
1. Verify `.htaccess` rules on GoDaddy
2. Check that `ai-trendwatch` folder exists
3. Ensure `index.html` is in the folder

### SFTP Connection Issues?
1. Regenerate SFTP credentials in GoDaddy
2. Update GitHub Secrets with new credentials
3. Re-run the failed workflow

---

## Manual Deployment (Fallback)

If GitHub Actions fails, you can manually deploy:

1. Download ZIP from GitHub
2. Go to GoDaddy File Manager
3. Navigate to `ai-trendwatch` folder
4. Upload/replace files

---

## Contact

**Curator:** Shashwat Ghosh
**Role:** Cofounder & Fractional CMO, Helix Consulting
**GitHub:** [@shashwatgtm](https://github.com/shashwatgtm)

---

*Last updated: January 10, 2026*
