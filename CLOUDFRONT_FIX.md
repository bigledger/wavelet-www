# CloudFront Configuration Fix Required

## Problem
The CloudFront distribution is currently using the S3 REST API endpoint as its origin, which causes it to return XML directory listings instead of serving the website.

## Solution Required
You need to update the CloudFront distribution settings in the AWS Console:

### Option 1: Change Origin to S3 Website Endpoint (Recommended)
1. Go to AWS CloudFront Console
2. Find the distribution for wiki.bigledger.com
3. Go to "Origins" tab
4. Edit the origin
5. Change the **Origin Domain Name** from:
   - Current: `wiki.bigledger.com.s3.amazonaws.com` (S3 REST endpoint)
   - To: `wiki.bigledger.com.s3-website-ap-southeast-5.amazonaws.com` (S3 website endpoint)
6. Save changes
7. Wait for distribution to deploy (5-10 minutes)

### Option 2: Configure CloudFront Default Root Object
1. Go to AWS CloudFront Console
2. Find the distribution for wiki.bigledger.com
3. Go to "General" tab → "Settings" → Edit
4. Set **Default Root Object** to: `index.html`
5. Go to "Behaviors" tab
6. Edit the default behavior
7. Ensure "Viewer Protocol Policy" is set to "Redirect HTTP to HTTPS"
8. Save changes

### Option 3: Use Origin Access Identity (OAI) with Custom Error Pages
1. Keep the S3 REST endpoint as origin
2. Configure CloudFront Error Pages:
   - 403 Error → Response Page: `/index.html` → HTTP Response Code: 200
   - 404 Error → Response Page: `/404.html` → HTTP Response Code: 404

## Testing
After CloudFront deploys the changes:
1. Clear browser cache
2. Visit https://wiki.bigledger.com
3. You should see the Hugo website instead of XML

## Alternative: Direct S3 Website Access
While CloudFront is being fixed, the site is accessible at:
http://wiki.bigledger.com.s3-website-ap-southeast-5.amazonaws.com

## Notes
- The Hugo site files are correctly deployed to S3
- S3 static website hosting is properly configured
- The issue is only with CloudFront origin configuration