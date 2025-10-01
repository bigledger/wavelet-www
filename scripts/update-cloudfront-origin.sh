#!/bin/bash

# Script to update CloudFront to use S3 website endpoint
# This fixes the directory index.html serving issue

set -e

echo "🔧 Updating CloudFront configuration to use S3 website endpoint..."

DISTRIBUTION_ID="CLOUDFRONT_ID_TBD"
S3_BUCKET="wavelet.net"
REGION="ap-southeast-1"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "Getting current distribution configuration..."
aws cloudfront get-distribution-config --id $DISTRIBUTION_ID > /tmp/cf-config.json

# Extract ETag for update
ETAG=$(cat /tmp/cf-config.json | jq -r '.ETag')
echo "Current ETag: $ETAG"

# Extract just the DistributionConfig
cat /tmp/cf-config.json | jq '.DistributionConfig' > /tmp/cf-distribution-config.json

# Check current origin
CURRENT_ORIGIN=$(cat /tmp/cf-distribution-config.json | jq -r '.Origins.Items[0].DomainName')
echo "Current origin: $CURRENT_ORIGIN"

# Update the origin to use S3 website endpoint
WEBSITE_ENDPOINT="${S3_BUCKET}.s3-website-${REGION}.amazonaws.com"
echo "New origin will be: $WEBSITE_ENDPOINT"

# Update the configuration
cat /tmp/cf-distribution-config.json | jq \
  --arg website_endpoint "$WEBSITE_ENDPOINT" \
  '.Origins.Items[0].DomainName = $website_endpoint |
   .Origins.Items[0].CustomOriginConfig = {
     "HTTPPort": 80,
     "HTTPSPort": 443,
     "OriginProtocolPolicy": "http-only",
     "OriginSslProtocols": {
       "Quantity": 3,
       "Items": ["TLSv1", "TLSv1.1", "TLSv1.2"]
     },
     "OriginReadTimeout": 30,
     "OriginKeepaliveTimeout": 5
   } |
   del(.Origins.Items[0].S3OriginConfig)' > /tmp/cf-updated-config.json

echo ""
echo -e "${YELLOW}⚠️  This will update the CloudFront distribution to use S3 website endpoint.${NC}"
echo "This change will:"
echo "  ✅ Allow directory URLs to work (e.g., /about/ will serve /about/index.html)"
echo "  ✅ Fix the NoSuchKey errors"
echo "  ⏱️  Take 5-15 minutes to fully deploy"
echo ""
echo "Do you want to proceed? (y/n)"
read -r response

if [[ "$response" != "y" ]]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Updating CloudFront distribution..."
aws cloudfront update-distribution \
  --id $DISTRIBUTION_ID \
  --distribution-config file:///tmp/cf-updated-config.json \
  --if-match $ETAG > /tmp/cf-update-result.json

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} CloudFront distribution updated successfully!"
    echo ""
    echo "The distribution is now deploying. Status:"
    aws cloudfront get-distribution --id $DISTRIBUTION_ID --query 'Distribution.Status' --output text
    echo ""
    echo "It will take 5-15 minutes for the changes to propagate globally."
    echo "You can check the status with:"
    echo "  aws cloudfront get-distribution --id $DISTRIBUTION_ID --query 'Distribution.Status'"
    echo ""
    echo "Once status shows 'Deployed', the site should work with directory URLs."
else
    echo -e "${RED}✗${NC} Failed to update CloudFront distribution"
    exit 1
fi

# Clean up temp files
rm -f /tmp/cf-config.json /tmp/cf-distribution-config.json /tmp/cf-updated-config.json /tmp/cf-update-result.json

echo ""
echo -e "${GREEN}✓${NC} Configuration update initiated successfully!"