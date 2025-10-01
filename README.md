# Wavelet Website

This repository contains the source for Wavelet's corporate website, built with Hugo and hosted at https://www.wavelet.net

## ⚠️ CRITICAL: GitHub File Paths

### **ALL content files are located under `content/en/` NOT just `en/`**

❌ **WRONG**: `https://github.com/wavelet/wavelet-www/blob/main/en/about/_index.md`
✅ **CORRECT**: `https://github.com/wavelet/wavelet-www/blob/main/content/en/about/_index.md`

**The `content/` prefix is REQUIRED for all GitHub paths!**

## Overview

The website is organized into sections under `content/en/`:
- **Home** (`content/en/_index.md`) - Homepage
- **About** (`content/en/about/`) - Company information
- **Solutions** (`content/en/solutions/`) - Product solutions
- **Pricing** (`content/en/pricing/`) - Pricing information
- **Contact** (`content/en/contact/`) - Contact page
- **Developers** (`content/en/developers/`) - Developer resources

## Local Development

### Prerequisites
- Hugo (extended version) - `brew install hugo`
- Git

### Running Locally

1. Clone the repository with submodules:
```bash
git clone --recurse-submodules https://github.com/wavelet/wavelet-www.git
cd wavelet-www
```

2. Start the Hugo development server:
```bash
hugo server -D
```

3. Open http://localhost:1313 in your browser

## Deployment

The site automatically deploys to AWS S3 when changes are pushed to the `main` branch via GitHub Actions.

### Manual Deployment

If you need to deploy manually (requires AWS credentials):

```bash
hugo deploy --target=production
```

## Content Structure

```
content/
├── _index.md                 # Homepage
├── about/                    # About page
│   └── _index.md
├── solutions/                # Solutions
│   └── _index.md
├── pricing/                  # Pricing
│   └── _index.md
├── contact/                  # Contact
│   └── _index.md
└── developers/               # Developer resources
    └── _index.md
```

## Adding Content

Create new content using Hugo's `new` command:

```bash
# About page
hugo new about/team.md

# Solutions page
hugo new solutions/enterprise.md

# Developer documentation
hugo new developers/api-guide.md
```

## Configuration

Site configuration is in `hugo.yaml`:
- Base URL: https://www.wavelet.net
- Theme: Hextra
- AWS Region: ap-southeast-1
- S3 Bucket: wavelet.net
- CloudFront Distribution: CLOUDFRONT_ID_TBD (to be updated)

## GitHub Actions

The `.github/workflows/deploy.yml` workflow handles automatic deployment:
1. Builds the Hugo site
2. Deploys to S3 bucket
3. Verifies deployment

Required secrets (already configured):
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

## Contributing

1. Create a feature branch
2. Make your changes
3. Test locally with `hugo server`
4. Submit a pull request

## License

Copyright Wavelet. All rights reserved.