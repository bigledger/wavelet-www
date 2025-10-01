# DNS Setup Instructions for bigledger.com

## Current Status

✅ **www.bigledger.com** - Working correctly (points to CloudFront)
❌ **bigledger.com** (apex) - Still pointing to WPEngine (104.154.43.123)

## Problem

GoDaddy doesn't support ALIAS records for apex domains, which is needed for CloudFront. CloudFront uses dynamic IPs that change, so we can't use A records with static IPs.

## Solution: GoDaddy Domain Forwarding

### Option 1: Domain Forwarding (Recommended - Simple)

1. Log into GoDaddy account
2. Go to **My Products** → **Domains**
3. Click on **bigledger.com**
4. Scroll down to **Forwarding** section
5. Click **Add Forwarding**
6. Configure:
   - **Forward to:** `https://www.bigledger.com`
   - **Forward type:** Permanent (301)
   - **Settings:** Forward only (not masked)
7. Click **Save**

**Result:** bigledger.com will redirect to www.bigledger.com with HTTP 301

### Option 2: Use CloudFlare DNS (Advanced - Better for SEO)

CloudFlare provides free DNS with CNAME flattening (ALIAS equivalent):

1. Sign up for CloudFlare (free plan works)
2. Add bigledger.com domain
3. Update nameservers at GoDaddy to CloudFlare's nameservers
4. In CloudFlare DNS:
   - Add CNAME for `@` (apex) → `d3ck4wq4572gna.cloudfront.net`
   - Add CNAME for `www` → `d3ck4wq4572gna.cloudfront.net`
   - Enable "Proxy status" (orange cloud) for both
5. Wait for DNS propagation (24-48 hours max)

**Result:** Both bigledger.com and www.bigledger.com work as primary domains

## Current Infrastructure

```
Domain: bigledger.com
├── www.bigledger.com (CNAME) → d3ck4wq4572gna.cloudfront.net ✅ WORKING
├── bigledger.com (A) → 104.154.43.123 (WPEngine) ❌ OLD
│
CloudFront Distribution: ELHXIGVKWA8XV
├── Domain: d3ck4wq4572gna.cloudfront.net
├── Aliases: bigledger.com, www.bigledger.com
├── SSL Certificate: ACM (validated)
├── Origin: bigledger.com.s3-website.ap-southeast-5.amazonaws.com
│
S3 Bucket: bigledger.com
├── Region: ap-southeast-5
├── Website hosting: Enabled
├── Content: Deployed ✅
```

## Quick Fix (Manual - 5 minutes)

**Until DNS is properly configured, users can:**
- Use `https://www.bigledger.com` (works now)
- Use `https://d3ck4wq4572gna.cloudfront.net` (works now)

## Verification Commands

After making DNS changes:

```bash
# Check DNS propagation
dig bigledger.com
dig www.bigledger.com

# Test HTTP response
curl -I https://bigledger.com
curl -I https://www.bigledger.com

# Check if forwarding works
curl -I http://bigledger.com  # Should return 301 redirect
```

## Expected Results

```
# After Option 1 (Forwarding):
curl -I http://bigledger.com
→ HTTP/1.1 301 Moved Permanently
→ Location: https://www.bigledger.com

# After Option 2 (CloudFlare):
curl -I https://bigledger.com
→ HTTP/2 200
→ (same content as www.bigledger.com)
```

## Support

If you need assistance:
1. Option 1 is simpler and takes 5 minutes
2. Option 2 is better for SEO and performance but takes 1-2 days for full propagation
3. I recommend Option 1 for immediate fix, then migrate to Option 2 later if needed

---

**Status:** Waiting for manual DNS configuration at GoDaddy
**Next Step:** After DNS is configured, website will be accessible at both bigledger.com and www.bigledger.com
