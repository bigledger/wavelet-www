#!/bin/bash

# Fix CloudFront to work like a normal static website
# This creates a Lambda@Edge function to handle directory indexes properly

set -e

echo "🔧 Fixing CloudFront to work like a normal website..."

DISTRIBUTION_ID="E3FOFD9ZXC2QVT"
REGION="us-east-1"  # Lambda@Edge must be in us-east-1

# Create the Lambda function code
cat > /tmp/index-redirect.js << 'EOF'
'use strict';

exports.handler = (event, context, callback) => {
    const request = event.Records[0].cf.request;
    const uri = request.uri;
    
    // If URI ends with / or has no extension, append index.html
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    } else if (!uri.includes('.')) {
        // Check if it looks like a directory (no file extension)
        request.uri += '/index.html';
    }
    
    callback(null, request);
};
EOF

# Create deployment package
cd /tmp
zip index-redirect.zip index-redirect.js

echo "Creating Lambda function..."

# Create IAM role for Lambda@Edge
cat > /tmp/trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "lambda.amazonaws.com",
          "edgelambda.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create the role
ROLE_NAME="CloudFrontDirectoryIndexRole"
aws iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document file:///tmp/trust-policy.json \
    --region $REGION 2>/dev/null || echo "Role already exists"

# Attach policy
aws iam attach-role-policy \
    --role-name $ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
    --region $REGION 2>/dev/null || true

# Get role ARN
ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --query 'Role.Arn' --output text --region $REGION)

echo "Role ARN: $ROLE_ARN"

# Wait for role to be available
sleep 10

# Create Lambda function
FUNCTION_NAME="CloudFrontDirectoryIndex"
aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --runtime nodejs18.x \
    --role $ROLE_ARN \
    --handler index-redirect.handler \
    --zip-file fileb:///tmp/index-redirect.zip \
    --timeout 5 \
    --memory-size 128 \
    --region $REGION 2>/dev/null || \
aws lambda update-function-code \
    --function-name $FUNCTION_NAME \
    --zip-file fileb:///tmp/index-redirect.zip \
    --region $REGION > /dev/null

# Get function ARN
FUNCTION_ARN=$(aws lambda get-function --function-name $FUNCTION_NAME --query 'Configuration.FunctionArn' --output text --region $REGION)

echo "Function ARN: $FUNCTION_ARN"

# Publish the function
VERSION=$(aws lambda publish-version --function-name $FUNCTION_NAME --region $REGION --query 'Version' --output text)
VERSIONED_ARN="${FUNCTION_ARN}:${VERSION}"

echo "Published version: $VERSION"
echo "Versioned ARN: $VERSIONED_ARN"

# Update CloudFront distribution
echo "Updating CloudFront distribution..."

aws cloudfront get-distribution-config --id $DISTRIBUTION_ID > /tmp/cf-config.json
ETAG=$(cat /tmp/cf-config.json | jq -r '.ETag')

# Add Lambda@Edge association
cat /tmp/cf-config.json | jq '.DistributionConfig' | jq \
  --arg lambda_arn "$VERSIONED_ARN" \
  '.DefaultCacheBehavior.LambdaFunctionAssociations = {
     "Quantity": 1,
     "Items": [
       {
         "LambdaFunctionARN": $lambda_arn,
         "EventType": "origin-request",
         "IncludeBody": false
       }
     ]
   }' > /tmp/cf-updated-config.json

aws cloudfront update-distribution \
  --id $DISTRIBUTION_ID \
  --distribution-config file:///tmp/cf-updated-config.json \
  --if-match $ETAG

echo "✅ CloudFront distribution updated!"
echo ""
echo "The changes will take 5-15 minutes to deploy globally."
echo "Once deployed, all directory URLs will work normally:"
echo "  ✅ https://wiki.bigledger.com/"
echo "  ✅ https://wiki.bigledger.com/tutorials/"
echo "  ✅ https://wiki.bigledger.com/modules/"
echo ""
echo "No more index.html needed!"

# Clean up
rm -f /tmp/index-redirect.js /tmp/index-redirect.zip /tmp/trust-policy.json /tmp/cf-config.json /tmp/cf-updated-config.json