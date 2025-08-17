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