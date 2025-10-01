# 🚨 URGENT: Fix bigledger.com Apex Domain (404 Error)

## Problem
- `www.bigledger.com` works ✅
- `bigledger.com` (apex) shows 404 from WPEngine ❌

## Root Cause
The A record for `bigledger.com` still points to WPEngine IP: `104.154.43.123`

## Immediate Fix Required

### Option 1: GoDaddy Domain Forwarding (5 minutes - RECOMMENDED)

1. **Log into GoDaddy:**
   - Go to https://dcc.godaddy.com/
   - Navigate to Domains → bigledger.com

2. **Set up Forwarding:**
   - Scroll to "Forwarding" section
   - Click "Add Forwarding"
   - Configure:
     ```
     Domain: http://bigledger.com
     Forward to: https://www.bigledger.com
     Forward type: Permanent (301)
     Update my nameservers: No
     ```
   - Save

3. **Result:**
   - `bigledger.com` → redirects to `www.bigledger.com`
   - Both domains will work

### Option 2: Update A Record to CloudFlare Free DNS (Better - 30 minutes)

GoDaddy doesn't support ALIAS records needed for CloudFront. CloudFlare does this for free.

1. **Sign up for CloudFlare (Free)**
   - Go to https://dash.cloudflare.com/sign-up
   - Add domain: `bigledger.com`

2. **CloudFlare will provide nameservers:**
   ```
   Example:
   ns1.cloudflare.com
   ns2.cloudflare.com
   ```

3. **Update nameservers at GoDaddy:**
   - Go to GoDaddy → Domains → bigledger.com
   - Click "Manage DNS"
   - Change Nameservers to "Custom"
   - Enter CloudFlare's nameservers

4. **Configure DNS in CloudFlare:**
   ```
   Type: CNAME
   Name: @
   Target: d3ck4wq4572gna.cloudfront.net
   Proxy status: ON (orange cloud)

   Type: CNAME
   Name: www
   Target: d3ck4wq4572gna.cloudfront.net
   Proxy status: ON (orange cloud)
   ```

5. **Wait for propagation** (2-24 hours)

### Option 3: Manual A Record Update (If you must use GoDaddy DNS)

⚠️ **Not recommended** - CloudFront IPs can change

1. Get CloudFront IP addresses:
   ```bash
   dig d3ck4wq4572gna.cloudfront.net +short
   ```

2. Update A record at GoDaddy:
   - Remove old A record (104.154.43.123)
   - Add new A records with CloudFront IPs

**Problem:** CloudFront IPs change, so this will break again

---

## Quick Test Commands

After DNS changes:

```bash
# Check DNS
dig bigledger.com +short

# Test HTTP (should redirect to HTTPS)
curl -I http://bigledger.com

# Test HTTPS
curl -I https://bigledger.com
```

Expected results after fix:
```
HTTP/1.1 301 Moved Permanently
Location: https://www.bigledger.com
```

---

## Infrastructure Summary

### Current Working Setup
```
www.bigledger.com (CNAME) → d3ck4wq4572gna.cloudfront.net ✅
  ↓
CloudFront Distribution (ELHXIGVKWA8XV)
  ↓
S3 Bucket (bigledger.com) with website content ✅
```

### What Needs Fixing
```
bigledger.com (A) → 104.154.43.123 (WPEngine) ❌
                     Should redirect to www.bigledger.com
```

---

## My Recommendation

**Use Option 1 (GoDaddy Forwarding)** for immediate fix today.

Then **migrate to Option 2 (CloudFlare)** next week for:
- Better performance (CDN)
- Better security (DDoS protection)
- Proper ALIAS support
- Free SSL (though you already have ACM)
- Better analytics

---

## Status

- [x] S3 bucket configured
- [x] CloudFront distribution deployed
- [x] SSL certificate validated
- [x] www.bigledger.com DNS configured ✅
- [ ] bigledger.com apex domain - **NEEDS MANUAL FIX**

---

## Contact

If you need help with any of these steps, the DNS changes must be done through GoDaddy's web interface as their API is having authentication issues.

The site is fully deployed and working at:
- ✅ https://www.bigledger.com
- ✅ https://d3ck4wq4572gna.cloudfront.net

Just need to fix the apex domain DNS!
