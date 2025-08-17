#!/bin/bash

# Script to help set up GitHub Actions secrets for deployment
# Run this to configure the required secrets for automated deployment

set -e

echo "🔐 GitHub Actions Secrets Setup"
echo "================================"
echo ""
echo "This script will help you set up the required GitHub secrets for automated deployment."
echo "You need to have the GitHub CLI (gh) installed and authenticated."
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Please install it first: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ You are not authenticated with GitHub CLI."
    echo "Please run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI is installed and authenticated"
echo ""

# Function to set a secret
set_secret() {
    local secret_name=$1
    local prompt_text=$2
    local is_sensitive=${3:-true}
    
    echo "$prompt_text"
    if [ "$is_sensitive" = true ]; then
        read -s secret_value
        echo ""
    else
        read secret_value
    fi
    
    if [ -n "$secret_value" ]; then
        echo "$secret_value" | gh secret set "$secret_name"
        echo "✅ $secret_name has been set"
    else
        echo "⚠️  Skipped $secret_name"
    fi
    echo ""
}

echo "Setting up AWS credentials for S3 deployment..."
echo "================================================"
echo ""

# AWS Access Key ID
set_secret "AWS_ACCESS_KEY_ID" "Enter your AWS Access Key ID:" true

# AWS Secret Access Key
set_secret "AWS_SECRET_ACCESS_KEY" "Enter your AWS Secret Access Key:" true

# AWS Region
echo "Enter your AWS Region (e.g., ap-southeast-5):"
read aws_region
if [ -n "$aws_region" ]; then
    echo "$aws_region" | gh secret set "AWS_REGION"
    echo "✅ AWS_REGION has been set to: $aws_region"
else
    echo "⚠️  Using default region from hugo.yaml"
fi

echo ""
echo "Verifying secrets..."
echo "===================="

# List secrets (names only, not values)
echo "The following secrets are now configured:"
gh secret list

echo ""
echo "✅ Setup complete!"
echo ""
echo "Your GitHub Actions workflow should now be able to deploy to S3."
echo "Push a commit to the main branch to trigger automatic deployment."
echo ""
echo "You can monitor deployments at:"
echo "https://github.com/bigledger/blg-wiki/actions"