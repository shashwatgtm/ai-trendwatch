# Deployment Guide - Offbeat AI Watch

## Quick Start: Deploying to GitHub Pages

### Step 1: Update Your Repository Name (Optional)
If you want to change from `ai-trendwatch` to `offbeat-ai-watch`:

1. Go to your repository on GitHub
2. Click **Settings**
3. Under "Repository name", change `ai-trendwatch` to `offbeat-ai-watch`
4. Click **Rename**

### Step 2: Upload Files to GitHub

#### Option A: Via GitHub Web Interface (Easiest)
1. Go to your repository: `https://github.com/shashwatgtm/ai-trendwatch`
2. Click **Add file** → **Upload files**
3. Drag and drop ALL files from this package
4. Write a commit message: "Update to Offbeat AI Watch with inaugural issue"
5. Click **Commit changes**

#### Option B: Via Git Command Line
```bash
# Navigate to your repository folder
cd /path/to/your/repo

# Add all files
git add .

# Commit changes
git commit -m "Update to Offbeat AI Watch with inaugural issue"

# Push to GitHub
git push origin main
```

### Step 3: Enable GitHub Pages

1. Go to repository **Settings**
2. Scroll to **Pages** section (left sidebar)
3. Under "Source", select **main** branch
4. Select **/ (root)** folder
5. Click **Save**

### Step 4: Wait for Deployment
- GitHub Pages will take 1-3 minutes to build
- Your site will be live at: `https://gtmhelix.com/ai-trendwatch/`
  (or `https://gtmhelix.com/offbeat-ai-watch/` if you renamed)

### Step 5: Update Subscribe Form

**Important**: Replace the Formspree placeholder in `index.html`:

1. Go to [Formspree.io](https://formspree.io) and create a free account
2. Create a new form
3. Copy your form endpoint ID
4. In `index.html`, replace:
   ```html
   action="https://formspree.io/f/YOUR_FORM_ID"
   ```
   with your actual form ID:
   ```html
   action="https://formspree.io/f/xyzabc123"
   ```

## File Structure

```
offbeat-ai-watch/
├── index.html              # Landing page with subscribe form
├── archive.html            # Archive of all issues
├── issues/
│   └── 2025-10-05.html    # Inaugural issue
├── README.md              # Repository documentation
├── DEPLOYMENT.md          # This file
└── .gitignore            # Git ignore rules
```

## Adding Future Issues

1. Create new HTML file: `issues/YYYY-MM-DD.html`
2. Copy format from `2025-10-05.html`
3. Update content
4. Add entry to `archive.html`
5. Update "Latest Issue" section in `index.html`

## Custom Domain (Optional)

To use a custom domain like `offbeatai.watch`:

1. Purchase domain from registrar
2. Add CNAME file to repository root with domain name
3. Configure DNS settings at your registrar
4. Update GitHub Pages settings to use custom domain

## Troubleshooting

**Site not updating?**
- Check GitHub Actions tab for build status
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 5 minutes and try again

**404 Error?**
- Ensure GitHub Pages is enabled
- Check that files are in root directory
- Verify repository is public

## Support

For issues, contact: [your-email@example.com]

---

Last updated: October 6, 2025
