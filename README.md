# BigLedger Documentation Wiki

This repository contains the source for BigLedger's documentation website, built with Hugo and hosted at https://wiki.bigledger.com

## ⚠️ CRITICAL: GitHub File Paths

### **ALL documentation files are located under `content/en/` NOT just `en/`**

❌ **WRONG**: `https://github.com/bigledger/blg-wiki/blob/main/en/user-guide/_index.md`  
✅ **CORRECT**: `https://github.com/bigledger/blg-wiki/blob/main/content/en/user-guide/_index.md`

**The `content/` prefix is REQUIRED for all GitHub paths!**

## Overview

The documentation is organized into sections under `content/en/`:
- **User Guide** (`content/en/user-guide/`) - Comprehensive guides for end users
- **Developer Documentation** (`content/en/developers/`) - Technical documentation for developers
- **API Reference** (`content/en/developers/api-reference/`) - Complete API documentation
- **Modules** (`content/en/modules/`) - Core module documentation
- **Applets** (`content/en/applets/`) - Applet documentation
- **Business Operations** (`content/en/business-operations/`) - Operational workflows
- **E-Commerce** (`content/en/ecommerce/`) - E-commerce features
- **Industry Solutions** (`content/en/industry-solutions/`) - Industry-specific guides

## Local Development

### Prerequisites
- Hugo (extended version) - `brew install hugo`
- Git

### Running Locally

1. Clone the repository with submodules:
```bash
git clone --recurse-submodules https://github.com/[your-org]/blg-wiki.git
cd blg-wiki
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
├── user-guide/               # End user documentation
│   ├── _index.md
│   └── getting-started.md
├── developer-docs/           # Developer documentation
│   ├── _index.md
│   └── installation.md
├── api-reference/           # API documentation
│   └── _index.md
└── tutorials/               # Tutorials
    └── _index.md
```

## Adding Content

Create new content using Hugo's `new` command:

```bash
# User guide page
hugo new user-guide/new-feature.md

# Developer documentation
hugo new developer-docs/integration-guide.md

# Tutorial
hugo new tutorials/how-to-integrate.md
```

## Configuration

Site configuration is in `hugo.yaml`:
- Base URL: https://wiki.bigledger.com
- Theme: Geekdoc
- AWS Region: ap-southeast-5

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

Copyright BigLedger. All rights reserved.