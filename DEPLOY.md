# AI TrendWatch - Deployment Guide

## 🚀 Get Live in 3 Steps (5 minutes)

Your newsletter is ready to deploy! Follow these simple steps to go live on GitHub Pages.

---

## Step 1: Download & Extract (30 seconds)

1. Download the `ai-trendwatch-deploy.zip` file
2. Extract it to your computer
3. You should see these files:
   ```
   ├── index.html
   ├── feed.xml
   ├── template.html
   ├── DEPLOY.md
   └── issues/
       └── 2025-10-05.html
   ```

---

## Step 2: Upload to GitHub (2 minutes)

1. Go to **https://github.com/shashwatgtm/ai-trendwatch**

2. Click **"Add file"** → **"Upload files"**

3. **IMPORTANT**: Drag ALL items from the extracted folder:
   - `index.html`
   - `feed.xml`
   - `template.html`
   - `DEPLOY.md`
   - `issues` **folder** (containing 2025-10-05.html)

4. Make sure you see `issues/2025-10-05.html` in the upload list (not just `2025-10-05.html`)

5. Scroll down and click **"Commit changes"**

---

## Step 3: Enable GitHub Pages (1 minute)

1. In your repository, click **"Settings"** (top right)

2. Click **"Pages"** in the left sidebar

3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`

4. Click **"Save"**

5. **Wait 2-3 minutes** for deployment

---

## ✅ Verify It's Live

After 2-3 minutes:

1. Go back to **Settings** → **Pages**

2. You should see: **"Your site is live at https://shashwatgtm.github.io/ai-trendwatch/"**

3. Click the URL to view your newsletter!

---

## 📧 Email Subscription Setup

Your landing page includes a Buttondown subscription form. To activate it:

1. Go to **https://buttondown.email**

2. Sign up (FREE for up to 100 subscribers)

3. In your Buttondown settings, note your email name

4. The form is already configured to use `ai-trendwatch` as the email name

5. If you want to change it:
   - Open `index.html`
   - Find line 168: `action="https://buttondown.email/api/emails/embed-subscribe/ai-trendwatch"`
   - Replace `ai-trendwatch` with your chosen email name

**Alternatives:**
- Mailchimp: Replace the form action with your Mailchimp embed URL
- ConvertKit: Use ConvertKit's form code
- Substack: Export subscribers and use Substack's built-in forms

---

## 📝 Publishing Your Next Issue

When you're ready to publish Issue #2:

### A. Create the New Issue

1. **Copy the template:**
   ```
   template.html → issues/2025-10-12.html
   ```

2. **Edit the new file:**
   - Replace all `[PLACEHOLDERS]` with your content
   - Add proper source URLs for each story
   - Make sure all links work

### B. Update the Landing Page

1. **Open `index.html`**

2. **Find line 125** (the "Latest Issues" section)

3. **Add your new issue ABOVE the existing one:**
   ```html
   <div class="issue-card">
       <div class="issue-date">October 12, 2025</div>
       <h3 class="issue-title">Issue #2 - [Your Title]</h3>
       <p class="issue-description">
           [Your description]
       </p>
       <a href="issues/2025-10-12.html" class="read-link">Read Full Issue</a>
   </div>
   ```

### C. Update the RSS Feed

1. **Open `feed.xml`**

2. **Find line 9** (right after `<channel>`)

3. **Add your new issue at the TOP:**
   ```xml
   <item>
     <title>Issue #2 - [Your Title]</title>
     <link>https://shashwatgtm.github.io/ai-trendwatch/issues/2025-10-12.html</link>
     <description>[Your description]</description>
     <pubDate>Sat, 12 Oct 2025 09:00:00 GMT</pubDate>
     <guid>https://shashwatgtm.github.io/ai-trendwatch/issues/2025-10-12.html</guid>
   </item>
   ```

### D. Upload to GitHub

1. Go to your repository

2. Click **"Add file"** → **"Upload files"**

3. Upload:
   - The new `issues/2025-10-12.html`
   - Updated `index.html`
   - Updated `feed.xml`

4. Commit the changes

5. **Your new issue will be live in 1-2 minutes!**

---

## 🔧 Troubleshooting

### "I don't see my site after 3 minutes"

1. Go to **Settings** → **Pages**
2. Check for error messages
3. Make sure **Branch** is set to `main` and **Folder** to `/ (root)`
4. Try clicking the **"Re-run job"** button if available

### "The issues folder didn't upload correctly"

If you see `2025-10-05.html` at the root instead of `issues/2025-10-05.html`:

1. Click on the file in GitHub
2. Click the pencil icon (Edit)
3. Change the filename at the top from `2025-10-05.html` to `issues/2025-10-05.html`
4. Commit the change
5. GitHub will automatically create the folder

### "My links are broken"

Make sure all links in your HTML files use the full path:
- ✅ `https://shashwatgtm.github.io/ai-trendwatch/issues/2025-10-05.html`
- ✅ `issues/2025-10-05.html` (relative path)
- ❌ `2025-10-05.html` (wrong - missing issues/)

### "Subscribe button doesn't work"

1. The button on the landing page scrolls to the subscription form - this is correct
2. Make sure you've set up your Buttondown account
3. Test the subscription form by entering an email
4. Check your Buttondown dashboard to see if the subscription came through

### "How do I edit my content after publishing?"

1. Go to your repository
2. Click on the file you want to edit
3. Click the pencil icon (✏️) in the top right
4. Make your changes
5. Scroll down and click "Commit changes"
6. Changes go live in 1-2 minutes

### "Can I use a custom domain?"

Yes! To use a custom domain like `aitrendwatch.com`:

1. Buy a domain from a registrar (Namecheap, GoDaddy, etc.)
2. In your registrar's DNS settings, add:
   - Type: `CNAME`
   - Name: `www`
   - Value: `shashwatgtm.github.io`
3. In GitHub:
   - Go to **Settings** → **Pages**
   - Enter your domain in "Custom domain"
   - Click Save
   - Wait 24-48 hours for DNS to propagate

---

## 📊 Analytics (Optional)

To track visitors, add Google Analytics:

1. Get your Google Analytics tracking code

2. Add it before the closing `</head>` tag in:
   - `index.html`
   - `template.html` (so future issues include it)

3. Example:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

---

## 🎨 Customization Ideas

### Change Colors

The main brand color is `#667eea` (purple). To change it:

1. Edit the CSS in `<style>` tags
2. Find and replace `#667eea` with your color
3. Update in:
   - `index.html`
   - `template.html`
   - Any existing issues

### Add Social Sharing

Add social sharing buttons to your newsletter issues:

```html
<!-- Add before the subscribe box -->
<div style="text-align: center; margin: 40px 0;">
    <a href="https://twitter.com/intent/tweet?url=YOUR_ISSUE_URL&text=Check out this week's AI TrendWatch" 
       target="_blank" 
       style="margin: 0 10px; color: #1DA1F2; text-decoration: none;">
        Tweet 🐦
    </a>
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=YOUR_ISSUE_URL" 
       target="_blank" 
       style="margin: 0 10px; color: #0077B5; text-decoration: none;">
        Share on LinkedIn 💼
    </a>
</div>
```

### Add Comments

Integrate Disqus or other commenting systems:

1. Sign up for Disqus
2. Get your embed code
3. Add it before the footer in your newsletter issues

---

## 🆘 Need Help?

If you get stuck:

1. **Check GitHub Pages status**: https://www.githubstatus.com/
2. **GitHub Pages docs**: https://docs.github.com/en/pages
3. **Buttondown support**: https://buttondown.email/help

---

## 🎉 What You've Built

✅ Professional newsletter website
✅ RSS feed for readers
✅ Email subscription form
✅ Mobile-responsive design
✅ Fast, free hosting
✅ Easy content management
✅ Proper source citations
✅ Template for future issues

**Your newsletter is ready for the world!** 🚀

Share your URL: `https://shashwatgtm.github.io/ai-trendwatch/`

---

## 📅 Recommended Publishing Schedule

- **Monday mornings**: Best for B2B newsletters
- **Consistency is key**: Pick a day and stick to it
- **Typical workflow time**: 
  - Research & writing: 2-3 hours
  - Formatting in template: 30 minutes
  - Publishing: 5 minutes

Good luck with AI TrendWatch! 🎯
