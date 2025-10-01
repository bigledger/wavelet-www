# Wavelet Website - Development Guidelines

## Language Strategy

### Primary Language: English (en)
- **All new content should be authored in English first**
- English content is located in `content/en/`
- This is the authoritative version of all documentation
- Keep English content up-to-date and comprehensive

### Supported Languages
1. **Chinese (zh)** - `content/zh/`
2. **Malay (ms)** - `content/ms/`  
3. **Arabic (ar)** - `content/ar/` (RTL support enabled)

### Translation Policy
- Translations are updated periodically, not in real-time
- English content takes priority for new features and updates
- Translation folders may not always have complete parity with English
- When creating new content, focus only on the English version

### Content Creation Guidelines for Claude

When creating or updating documentation:

1. **Always work in the English (`content/en/`) directory**
2. **Do not create translations automatically**
3. **Structure all new content in English first**
4. **Use clear, simple English that is easy to translate**
5. **Avoid idioms and culturally-specific references**

## Wavelet Website Architecture

### CRITICAL: Understanding Website Structure

**The Wavelet website is a corporate marketing site, not a documentation wiki:**
- **Home** = Landing page with hero section and key features
- **About** = Company information and team
- **Solutions** = Product offerings and features
- **Pricing** = Pricing tiers and plans
- **Contact** = Contact information and forms
- **Developers** = Developer resources and API documentation

**DO:**
- ✅ Keep marketing copy clear and concise
- ✅ Use hero sections and call-to-action buttons
- ✅ Focus on benefits and features for customers

**DON'T:**
- ❌ Create module/applet documentation (this is not a docs site)
- ❌ Use technical documentation style
- ❌ Create deep navigation hierarchies

### IMPORTANT: Hextra Theme Limitations

⚠️ **The Hextra theme has strict limitations on HTML/CSS usage:**

1. **DO NOT use complex inline HTML with styles** - The theme doesn't properly render complex HTML/CSS
2. **DO NOT use `<div>` tags with inline styles** - They will display as raw HTML
3. **DO NOT use CSS grid or flexbox in markdown** - It won't work correctly

✅ **INSTEAD, use Hextra's built-in components:**

```markdown
# Good - Using Hextra cards component
{{< cards >}}
  {{< card link="/path" title="Title" subtitle="Description" >}}
{{< /cards >}}

# Bad - Using HTML divs
<div style="display: grid;">...</div>
```

✅ **Use these Hextra components:**
- `{{< cards >}}` - For card grids
- `{{< card >}}` - Individual cards with title, subtitle, link
- `{{< hextra/hero-badge >}}` - Hero badges
- `{{< hextra/hero-headline >}}` - Hero headlines
- `{{< hextra/hero-subtitle >}}` - Hero subtitles
- `{{< hextra/hero-button >}}` - Call-to-action buttons
- `{{< tabs >}}` - Tabbed content
- `{{< tab >}}` - Individual tab content

✅ **For styling, use:**
- Standard Markdown formatting
- Hextra's built-in classes only
- Emoji for visual elements (sparingly)
- Simple tables for structured data

❌ **Avoid:**
- Inline `style` attributes
- Complex HTML structures
- Custom CSS classes
- JavaScript in content files

### File Structure Example
```
content/
├── en/           # PRIMARY - Always update this first
│   ├── _index.md
│   ├── user-guide/
│   ├── developer-docs/
│   ├── api-reference/
│   └── tutorials/
├── zh/           # Chinese translations (updated periodically)
├── ms/           # Malay translations (updated periodically)
└── ar/           # Arabic translations (updated periodically, RTL)
```

### Important Commands

Test the site locally:
```bash
./scripts/test-local.sh
# Or manually: hugo server -D
```

Build the site:
```bash
hugo --gc --minify
```

Check for broken links:
```bash
./scripts/check-links.sh
```

### Language URLs
- English: https://www.wavelet.net/ (default)
- Chinese: https://www.wavelet.net/zh/
- Malay: https://www.wavelet.net/ms/
- Arabic: https://www.wavelet.net/ar/

## Deployment Process

### IMPORTANT: Always use GitHub Actions for deployment

**DO NOT deploy directly from local machine to S3!** The site should be deployed through GitHub Actions for consistency and security.

### Deployment Workflow

1. **Complete Deployment Process:**
   ```bash
   ./scripts/deploy.sh
   ```
   This script will:
   - Build the site
   - Optionally test locally
   - Commit changes
   - Push to GitHub
   - Monitor GitHub Actions deployment
   - Verify the deployment

2. **Manual Steps:**
   ```bash
   # 1. Build and test locally
   ./scripts/test-local.sh
   
   # 2. Check for broken links
   ./scripts/check-links.sh
   
   # 3. Commit changes
   git add -A
   git commit -m "Your commit message"
   
   # 4. Push to GitHub (this triggers deployment)
   git push origin main
   
   # 5. Monitor deployment
   gh run list --workflow=deploy.yml --limit=1
   gh run watch <run-id>
   ```

3. **Setup GitHub Secrets (one-time setup):**
   ```bash
   ./scripts/setup-github-secrets.sh
   ```
   Required secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`

### Deployment Scripts

All deployment scripts are located in the `scripts/` directory:

- **`deploy.sh`** - Complete deployment workflow
- **`test-local.sh`** - Build and test locally
- **`check-links.sh`** - Validate all internal links
- **`setup-github-secrets.sh`** - Configure GitHub Actions secrets

### GitHub Actions

The site is automatically deployed when changes are pushed to the `main` branch. The workflow:

1. Builds the site with Hugo
2. Deploys to S3 bucket: `wavelet.net`
3. Invalidates CloudFront distribution: `CLOUDFRONT_ID_TBD` (to be updated)
4. Verifies deployment

Monitor deployments at: https://github.com/wavelet/wavelet-www/actions

### Troubleshooting Deployment

If deployment fails:

1. **Check GitHub Actions logs:**
   ```bash
   gh run view <run-id>
   ```

2. **Verify secrets are set:**
   ```bash
   gh secret list
   ```

3. **Test build locally:**
   ```bash
   hugo --gc --minify
   ```

4. **Check S3 permissions:**
   - Ensure AWS credentials have S3 write access
   - Verify bucket policy allows uploads

5. **CloudFront issues:**
   - Wait 5-10 minutes for propagation
   - Check CloudFront distribution status in AWS Console

## CRITICAL: Navigation and Title Guidelines

### ⚠️ MANDATORY RULES TO PREVENT NAVIGATION AND TITLE ISSUES

#### 1. Navigation Structure Requirements
**EVERY directory MUST have an _index.md file:**
- Check EVERY directory in `content/en/` for _index.md
- Use this exact template for ALL _index.md files:
```markdown
---
title: "Section Title"
description: "Clear description of this section"
weight: [number for ordering]
bookCollapseSection: false  # For top-level sections
---

[Content here]
```

#### 2. Preventing Duplicate Titles
**NEVER add an H1 heading that duplicates the front matter title:**
```markdown
# BAD Example:
---
title: "Module Overview"
---

# Module Overview  ← DELETE THIS! It duplicates the title above

Content starts here...

# GOOD Example:
---
title: "Module Overview"
---

Content starts here directly without repeating the title...
```

#### 3. Systematic Verification Checklist
Before EVERY commit, run these checks:

```bash
# Check for missing _index.md files
find content/en -type d | while read dir; do
  if [ ! -f "$dir/_index.md" ]; then
    echo "MISSING: $dir/_index.md"
  fi
done

# Check for duplicate titles
find content/en -name "*.md" | while read file; do
  title=$(grep "^title:" "$file" | head -1 | sed 's/title: *//' | tr -d '"')
  h1=$(grep "^# " "$file" | head -1 | sed 's/^# *//')
  if [ "$title" = "$h1" ]; then
    echo "DUPLICATE TITLE: $file"
  fi
done
```

#### 4. When Adding New Content
- **ALWAYS create _index.md FIRST** before adding any content to a directory
- **NEVER use an H1 heading** if it matches the front matter title
- **TEST navigation locally** with `hugo server` before committing
- **Verify left menu appears** on ALL pages

#### 5. Common Mistakes to Avoid
- ❌ Creating content files without parent _index.md
- ❌ Adding H1 headings that duplicate front matter titles
- ❌ Missing bookCollapseSection in section _index.md files
- ❌ Forgetting to test navigation after changes
- ❌ Assuming navigation works without verification

## Remember

1. **When authoring content, focus exclusively on the English version in `content/en/`. Translations will be handled separately.**
2. **Always deploy through GitHub Actions, never directly from local machine to S3.**
3. **Test locally before pushing to ensure the build succeeds.**
4. **Monitor GitHub Actions to confirm successful deployment.**
5. **NEVER add the following lines to commit messages:**
   - `🤖 Generated with [Claude Code](https://claude.ai/code)`
   - `Co-Authored-By: Claude <noreply@anthropic.com>`
   - Keep commit messages clean and professional without attribution tags
6. **ALWAYS verify navigation and titles before committing - use the verification checklist above**