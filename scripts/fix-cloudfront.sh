#!/bin/bash

# Script to fix CloudFront configuration for proper directory index handling
# This configures CloudFront to use S3 website endpoint instead of REST API

echo "🔧 Fixing CloudFront configuration for proper directory handling..."

DISTRIBUTION_ID="CLOUDFRONT_ID_TBD"
S3_BUCKET="wavelet.net"
REGION="ap-southeast-1"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "Current issue: CloudFront is using S3 REST API endpoint which doesn't handle directory indexes."
echo "Solution: Switch to S3 website endpoint which automatically serves index.html for directories."
echo ""
echo -e "${YELLOW}⚠️  This requires updating CloudFront distribution configuration.${NC}"
echo ""

echo "The S3 website endpoint should be:"
echo -e "${GREEN}${S3_BUCKET}.s3-website-${REGION}.amazonaws.com${NC}"
echo ""

echo "To fix this issue:"
echo "1. Go to AWS Console > CloudFront > Distribution ${DISTRIBUTION_ID}"
echo "2. Click 'Origins' tab"
echo "3. Edit the origin"
echo "4. Change Origin Domain Name from:"
echo "   ${S3_BUCKET}.s3.${REGION}.amazonaws.com"
echo "   to:"
echo "   ${S3_BUCKET}.s3-website-${REGION}.amazonaws.com"
echo "5. Change Origin Protocol Policy to 'HTTP Only'"
echo "6. Save changes"
echo "7. Wait for distribution to deploy (5-10 minutes)"
echo ""

echo "Alternative: Use Lambda@Edge to rewrite requests"
echo "This would append /index.html to directory requests automatically."
echo ""

echo "For now, users need to access pages with explicit /index.html:"
echo "  ❌ https://www.wavelet.net/about/"
echo "  ✅ https://www.wavelet.net/about/index.html"