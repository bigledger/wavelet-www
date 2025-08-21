# BigLedger Documentation - Development Guidelines

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

## BigLedger Architecture - Module-Applet Relationship

### CRITICAL: Understanding Modules and Applets

**Modules and Applets have a many-to-many relationship:**
- **Modules** = Logical business groupings (e.g., Financial Accounting, E-Commerce, POS)
- **Applets** = Reusable functional components that can belong to MULTIPLE modules
- **Location**: All applet documentation stays in `/content/en/applets/` (single source of truth)
- **References**: Modules reference (link to) applets, never duplicate their documentation

**Example**: Tax Configuration Applet is used by:
- Financial Accounting Module
- Sales & CRM Module  
- Purchasing Module
- E-Commerce Module
- POS Module

This applet has ONE documentation file in `/applets/` that all modules link to.

**DO:**
- ✅ Keep applet docs in `/applets/`
- ✅ Have modules list and link to their applets
- ✅ Explain in each module which applets it uses

**DON'T:**
- ❌ Move applets under module folders
- ❌ Duplicate applet documentation
- ❌ Create multiple versions of the same applet doc

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
- English: https://wiki.bigledger.com/ (default)
- Chinese: https://wiki.bigledger.com/zh/
- Malay: https://wiki.bigledger.com/ms/
- Arabic: https://wiki.bigledger.com/ar/

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
2. Deploys to S3 bucket: `wiki.bigledger.com`
3. Invalidates CloudFront distribution: `E3FOFD9ZXC2QVT`
4. Verifies deployment

Monitor deployments at: https://github.com/bigledger/blg-wiki/actions

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

## Remember

1. **When authoring content, focus exclusively on the English version in `content/en/`. Translations will be handled separately.**
2. **Always deploy through GitHub Actions, never directly from local machine to S3.**
3. **Test locally before pushing to ensure the build succeeds.**
4. **Monitor GitHub Actions to confirm successful deployment.**
5. **NEVER add the following lines to commit messages:**
   - `🤖 Generated with [Claude Code](https://claude.ai/code)`
   - `Co-Authored-By: Claude <noreply@anthropic.com>`
   - Keep commit messages clean and professional without attribution tags