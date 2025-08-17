#!/bin/bash

# Script to fix CloudFront directory handling using CloudFront Functions
# This adds a function to append index.html to directory requests

set -e

echo "🔧 Fixing CloudFront directory handling with CloudFront Functions..."

DISTRIBUTION_ID="E3FOFD9ZXC2QVT"

# Create the CloudFront function code
cat > /tmp/cf-function.js << 'EOF'
function handler(event) {
    var request = event.request;
    var uri = request.uri;
    
    // Check whether the URI is missing a file name
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    } 
    // Check whether the URI is missing a file extension
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }
    
    return request;
}
EOF

echo "Creating CloudFront Function..."

# Create the function
FUNCTION_NAME="DirectoryIndexRewriter"
FUNCTION_COMMENT="Appends index.html to directory requests"

# Check if function already exists
EXISTING_FUNCTION=$(aws cloudfront list-functions --query "FunctionList.Items[?Name=='$FUNCTION_NAME'].Name" --output text 2>/dev/null || echo "")

if [ -z "$EXISTING_FUNCTION" ]; then
    echo "Creating new CloudFront Function..."
    aws cloudfront create-function \
        --name "$FUNCTION_NAME" \
        --function-config Comment="$FUNCTION_COMMENT",Runtime="cloudfront-js-2.0" \
        --function-code "$(cat /tmp/cf-function.js)" > /tmp/cf-function-result.json
    
    FUNCTION_ARN=$(cat /tmp/cf-function-result.json | jq -r '.FunctionSummary.FunctionMetadata.FunctionARN')
    ETAG=$(cat /tmp/cf-function-result.json | jq -r '.ETag')
    
    echo "Publishing function..."
    aws cloudfront publish-function --name "$FUNCTION_NAME" --if-match "$ETAG"
else
    echo "Function already exists. Getting ARN..."
    FUNCTION_ARN=$(aws cloudfront describe-function --name "$FUNCTION_NAME" --query 'FunctionSummary.FunctionMetadata.FunctionARN' --output text)
fi

echo "Function ARN: $FUNCTION_ARN"

# Now update the distribution to use this function
echo "Getting current distribution configuration..."
aws cloudfront get-distribution-config --id $DISTRIBUTION_ID > /tmp/cf-config.json
ETAG=$(cat /tmp/cf-config.json | jq -r '.ETag')

# Update to use S3 REST API endpoint and add the function
cat /tmp/cf-config.json | jq '.DistributionConfig' | jq \
  --arg function_arn "$FUNCTION_ARN" \
  '.Origins.Items[0].DomainName = "wiki.bigledger.com.s3.ap-southeast-5.amazonaws.com" |
   .Origins.Items[0].S3OriginConfig = {"OriginAccessIdentity": ""} |
   del(.Origins.Items[0].CustomOriginConfig) |
   .DefaultCacheBehavior.FunctionAssociations = {
     "Quantity": 1,
     "Items": [
       {
         "FunctionARN": $function_arn,
         "EventType": "viewer-request"
       }
     ]
   }' > /tmp/cf-updated-config.json

echo "Updating CloudFront distribution..."
aws cloudfront update-distribution \
  --id $DISTRIBUTION_ID \
  --distribution-config file:///tmp/cf-updated-config.json \
  --if-match $ETAG

if [ $? -eq 0 ]; then
    echo "✅ CloudFront distribution updated successfully!"
    echo ""
    echo "The distribution is now deploying. This will take 5-15 minutes."
    echo "Once deployed, directory URLs will automatically serve index.html files."
else
    echo "❌ Failed to update CloudFront distribution"
    exit 1
fi

# Clean up
rm -f /tmp/cf-function.js /tmp/cf-function-result.json /tmp/cf-config.json /tmp/cf-updated-config.json

echo ""
echo "✅ Configuration complete! CloudFront will now handle directory requests correctly."