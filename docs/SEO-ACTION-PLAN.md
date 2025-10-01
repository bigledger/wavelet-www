# SEO Implementation Action Plan - Wavelet

**Prioritized action items for immediate SEO implementation**

---

## Week 1: Critical Foundation (Days 1-7)

### Day 1-2: E-Invoice Landing Page (HIGHEST PRIORITY)

**Why:** "e-invoice malaysia" is trending HIGH due to July 2025 Phase 3 compliance deadline. This is a critical conversion page.

**Action Items:**
1. Create `/content/en/solutions/e-invoice-malaysia.md`
2. Content requirements:
   - 3,500+ words comprehensive guide
   - Title: "LHDN E-Invoice Malaysia | MDEC PEPPOL Certified | MyInvois Integration - Wavelet"
   - Include: What, Why, When, How sections
   - Timeline with all 5 phases
   - Comprehensive FAQ (10+ questions)
   - Trust signals (MDEC PEPPOL certification)
   - Multiple CTAs

3. Schema markup to include:
   - FAQPage schema (10+ Q&As)
   - SoftwareApplication schema
   - BreadcrumbList schema

**Content outline:**
```markdown
# LHDN E-Invoice Malaysia - MDEC PEPPOL Certified Solution

## What is LHDN E-Invoice Malaysia? (300 words)
- Definition
- Government mandate
- MyInvois system overview

## E-Invoice Implementation Timeline 2025 (500 words)
- Phase 1: August 2024 (RM100M+) - COMPLETED
- Phase 2: January 2025 (RM25-100M) - IN PROGRESS
- Phase 3: July 2025 (RM5-25M) - UPCOMING
- Phase 4: January 2026 (RM1-5M)
- Phase 5: July 2026 (All businesses)

## Why E-Invoice Compliance Matters (400 words)
- Legal requirements
- Tax implications
- Business benefits
- Penalties for non-compliance

## Wavelet E-Invoice Features (700 words)
- MDEC PEPPOL Certified
- Automated LHDN submission
- MyInvois API integration
- Real-time validation
- Multi-format support (XML, JSON)
- Digital certification
- Error handling
- Audit trail

## How Wavelet Simplifies E-Invoice Compliance (600 words)
- Step-by-step process
- Integration with existing workflow
- Automated features
- Support and training

## E-Invoice Requirements for Your Business (400 words)
- Who needs to comply
- When to implement
- What documents are required
- Format requirements

## Getting Started with Wavelet E-Invoice (300 words)
- Implementation timeline
- Setup process
- Training available
- Support options

## Frequently Asked Questions (1,000+ words)
1. What is LHDN E-Invoice Malaysia?
2. When does my business need to comply?
3. What is PEPPOL and why does it matter?
4. Is Wavelet MDEC PEPPOL certified?
5. How does MyInvois integration work?
6. What happens if I don't comply?
7. Can I still issue paper invoices?
8. What invoice formats are supported?
9. How much does E-Invoice implementation cost?
10. What training and support do you provide?
11. How long does implementation take?
12. Can I test before going live?

## Success Stories (300 words)
- Client testimonials
- Implementation examples

## Get E-Invoice Ready Today (200 words)
- Strong CTA
- Contact options
- Free consultation offer

## Related Resources
- Internal links to relevant pages
```

**Deliverable:** Complete, published page ready to rank for high-value compliance keywords.

---

### Day 3: Homepage Optimization

**Action Items:**

1. Update title tag:
```html
<title>Wavelet - Cloud ERP & POS Solution | MDEC PEPPOL Certified Malaysia</title>
```

2. Update meta description:
```html
<meta name="description" content="Complete cloud ERP and POS system for Malaysian businesses. MDEC PEPPOL accredited E-Invoice, multi-industry support, 99.9% uptime. Trusted by 10,000+ businesses across Southeast Asia." />
```

3. Expand homepage content to 2,000 words:
   - Add comprehensive "What is Wavelet" section
   - Add "Industries We Serve" with descriptions
   - Add "Core Modules" with detailed features
   - Add FAQ section (8-10 questions)
   - Add client testimonials/social proof
   - Add E-Invoice compliance banner/section

4. Add schema markup:
   - Organization schema
   - FAQPage schema
   - Aggregate ratings (if available)

**File to edit:** `/content/en/_index.md`

---

### Day 4: Create llms.txt for AI Crawler Optimization

**Action Items:**

1. Create `/static/llms.txt` file with comprehensive information about Wavelet
2. Include:
   - Company overview
   - Primary services
   - Target markets
   - Key differentiators
   - Compliance certifications
   - Industries served
   - Important links
   - Contact information

**File to create:** `/static/llms.txt`

**Reference:** See full llms.txt content in SEO-STRATEGY-2025.md Section 5

---

### Day 5: Implement Core Schema Markup

**Action Items:**

1. Create Hugo partial for Organization schema:
   - File: `/layouts/partials/schema/organization.html`
   - Include on all pages

2. Create Hugo partial for BreadcrumbList schema:
   - File: `/layouts/partials/schema/breadcrumb.html`
   - Include on all pages

3. Update `/themes/hextra/layouts/_partials/head.html` to include schema partials

4. Test all schema with Google Rich Results Test

**Deliverable:** All pages have proper Organization and BreadcrumbList schema.

---

### Day 6-7: Technical SEO Audit & Quick Fixes

**Action Items:**

1. Run PageSpeed Insights on all major pages
   - Document current scores
   - Identify quick wins

2. Check mobile usability
   - Test all pages on mobile devices
   - Ensure touch targets are adequate (44px minimum)
   - Check form usability

3. Update robots.txt:
   - Allow AI crawlers (GPTBot, ClaudeBot)
   - Ensure sitemap is listed
   - Block admin/test pages

4. Verify sitemap.xml:
   - All pages included
   - Proper priority settings
   - Submit to Google Search Console

5. Fix any broken links:
   - Run link checker
   - Fix or remove broken links

**Deliverables:**
- Technical audit report
- Updated robots.txt
- Verified sitemap
- No broken links

---

## Week 2: Industry Landing Pages (Days 8-14)

### Priority 1: Retail POS Landing Page (Days 8-10)

**File:** `/content/en/solutions/retail-pos-system-malaysia.md`

**Title:** "Retail POS System Malaysia | E-Commerce Integration & Inventory | Wavelet"

**Target Keywords:**
- retail pos system malaysia
- pos system for retail
- retail inventory management
- multi-outlet pos system

**Content:** 2,500+ words
**Schema:** Service + FAQPage

**Key sections:**
- Why retail businesses need Wavelet
- Complete feature list (POS, inventory, e-commerce, loyalty)
- Multi-outlet management
- E-commerce integration (Shopify, Lazada, Shopee)
- Success story/testimonial
- Pricing/demo CTA
- FAQ section

---

### Priority 2: Restaurant POS Landing Page (Days 11-12)

**File:** `/content/en/solutions/restaurant-pos-system-malaysia.md`

**Title:** "Restaurant POS System Malaysia | F&B Management & Kitchen Display | Wavelet"

**Target Keywords:**
- restaurant pos system malaysia
- f&b pos system
- kitchen display system
- restaurant management software

**Content:** 2,500+ words
**Schema:** Service + FAQPage

**Key sections:**
- Why F&B businesses need Wavelet
- Table management and reservations
- Kitchen Display System (KDS)
- Online ordering integration
- Split bill and custom orders
- Recipe and ingredient management
- Success story from F&B client
- FAQ section

---

### Priority 3: Manufacturing ERP Landing Page (Days 13-14)

**File:** `/content/en/solutions/manufacturing-erp-malaysia.md`

**Title:** "Manufacturing ERP Malaysia | Production Planning & MRP | Wavelet"

**Target Keywords:**
- manufacturing erp malaysia
- production management system
- mrp software malaysia
- bom management

**Content:** 2,500+ words
**Schema:** Service + FAQPage

**Key sections:**
- Why manufacturers need ERP
- Bill of Materials (BOM) management
- Production planning and scheduling
- Shop floor control
- Quality control and inspection
- Material Requirements Planning (MRP)
- Success story from manufacturing client
- FAQ section

---

## Week 3: Schema Markup & Technical Optimization (Days 15-21)

### Day 15-16: Comprehensive Schema Implementation

**Action Items:**

1. Create SoftwareApplication schema partial
   - File: `/layouts/partials/schema/software.html`
   - Include on product/solution pages

2. Create Service schema partial
   - File: `/layouts/partials/schema/service.html`
   - Include on solution pages

3. Create FAQPage schema partial
   - File: `/layouts/partials/schema/faq.html`
   - Include on pages with FAQ sections

4. Test all schema implementations
   - Use Google Rich Results Test
   - Fix any errors
   - Document which pages have which schema

---

### Day 17-18: Internal Linking Implementation

**Action Items:**

1. Create internal linking strategy spreadsheet:
   - List all pages
   - Identify priority pages (E-Invoice, Solutions, Pricing)
   - Plan linking structure (hub-and-spoke)

2. Add contextual links to homepage:
   - Link to E-Invoice page (3-5 times with different anchors)
   - Link to industry solutions
   - Link to pricing

3. Add internal links to Solutions page:
   - Link to each industry landing page
   - Link to E-Invoice page
   - Link to pricing

4. Add "Related Solutions" section to all landing pages:
   - Include 3-5 related internal links
   - Use descriptive anchor text

**Target:** 10-15 contextual internal links per page

---

### Day 19-20: Image Optimization

**Action Items:**

1. Audit all images:
   - List all images used on site
   - Check file sizes
   - Check formats

2. Optimize images:
   - Convert to WebP format
   - Compress to appropriate size
   - Add descriptive alt text (include keywords where natural)
   - Implement lazy loading

3. Add images to new landing pages:
   - Screenshots of relevant features
   - Client logos (if available)
   - Industry-specific imagery

**Tools:**
- ImageOptim or similar
- Hugo's built-in image processing

---

### Day 21: Core Web Vitals Optimization

**Action Items:**

1. Run PageSpeed Insights on all major pages
2. Fix LCP issues:
   - Optimize largest image
   - Ensure server responds quickly
   - Use CDN (already using CloudFront)

3. Fix INP issues:
   - Minimize JavaScript
   - Optimize event handlers
   - Remove unused JavaScript

4. Fix CLS issues:
   - Set explicit dimensions for images
   - Reserve space for dynamic content
   - Avoid inserting content above existing content

**Target:** All Core Web Vitals in green zone

---

## Week 4: Content Expansion & Local SEO (Days 22-28)

### Day 22-24: Create First Blog Posts

**Blog Post 1:** "Complete Guide to LHDN E-Invoice Compliance 2025"
- 2,500+ words
- Comprehensive compliance guide
- Step-by-step implementation
- Timeline with all phases
- FAQ section
- Internal links to E-Invoice landing page

**Blog Post 2:** "How to Choose the Right ERP System for Your Malaysian Business"
- 2,000+ words
- Decision framework
- Feature comparison
- Industry considerations
- Budget planning
- Internal links to Solutions and Pricing

---

### Day 25-26: Optimize Solutions Page

**File:** `/content/en/solutions.md`

**Action Items:**

1. Expand content to 2,500+ words:
   - Detailed description of each industry solution
   - Benefits for each industry
   - Feature highlights

2. Add schema markup:
   - ItemList schema for solutions
   - Service schema

3. Add internal links:
   - Link to each industry landing page
   - Link to E-Invoice page
   - Link to pricing

4. Add FAQ section specific to solutions/industries

---

### Day 27: Optimize Pricing Page

**File:** `/content/en/pricing.md`

**Action Items:**

1. Expand FAQ section to 15+ questions:
   - Pricing-related questions
   - Trial and demo information
   - Contract terms
   - Support levels
   - Migration assistance

2. Add comparison table (if applicable):
   - Different plan features
   - What's included in each

3. Implement Offer schema markup

4. Add trust signals:
   - Security certifications
   - Compliance badges
   - Client testimonials

---

### Day 28: Google Business Profile & Local SEO

**Action Items:**

1. Create/optimize Google Business Profile:
   - Complete all information
   - Add business hours
   - Add photos (office, team, products)
   - Add services
   - Add service areas

2. Ensure NAP (Name, Address, Phone) consistency:
   - Check website footer
   - Check contact page
   - Check About page
   - Match exactly with Google Business Profile

3. Add LocalBusiness schema to website:
   - Include in Organization schema
   - Add address, phone, hours

4. Create location page (if applicable):
   - Office locations
   - Service areas
   - Local contact information

---

## Immediate Quick Wins (Can be done in parallel)

### Quick Win 1: Update All Title Tags (2 hours)
Go through each page and ensure:
- Unique title tag
- Under 60 characters
- Primary keyword at start
- Brand at end

### Quick Win 2: Update All Meta Descriptions (2 hours)
Go through each page and ensure:
- Unique meta description
- 140-160 characters
- Primary keyword in first sentence
- Call-to-action included

### Quick Win 3: Add Alt Text to All Images (1 hour)
- Audit all images
- Add descriptive alt text
- Include keywords where natural (don't stuff)

### Quick Win 4: Fix Heading Structure (1 hour)
Check each page:
- Only ONE H1
- Proper hierarchy (H1 > H2 > H3)
- Keywords in headings
- No skipped levels

### Quick Win 5: Create Compelling CTAs (1 hour)
Every page should have:
- Primary CTA above the fold
- Secondary CTA in middle of page
- Final CTA at bottom
- Clear, action-oriented copy

---

## Measurement & Tracking Setup

### Week 1: Setup Tools

**Action Items:**

1. Google Search Console:
   - [ ] Verify property
   - [ ] Submit sitemap
   - [ ] Check for errors

2. Google Analytics 4:
   - [ ] Install tracking code
   - [ ] Set up goals/conversions
   - [ ] Configure events

3. PageSpeed Insights:
   - [ ] Baseline all major pages
   - [ ] Document current scores

4. Rank Tracking (if using tool):
   - [ ] Set up project
   - [ ] Add primary keywords
   - [ ] Set up competitor tracking

---

## Priority Keyword Targets (First 3 Months)

### Must Rank For (Top Priority):
1. e-invoice malaysia
2. lhdn e-invoice system
3. peppol malaysia
4. mdec peppol accredited

### Should Rank For (High Priority):
5. cloud erp malaysia
6. pos system malaysia
7. erp system for sme malaysia
8. retail pos system malaysia
9. restaurant pos system malaysia
10. manufacturing erp malaysia

### Nice to Rank For (Medium Priority):
11. erp accounting software malaysia
12. inventory management system malaysia
13. multi-outlet pos system
14. e-commerce erp integration
15. lhdn approved software

---

## Success Metrics - 90 Day Targets

### Traffic:
- [ ] 100% increase in organic sessions
- [ ] 500+ monthly organic sessions
- [ ] 200+ monthly new users from organic

### Rankings:
- [ ] Top 10 for "e-invoice malaysia"
- [ ] Top 20 for "cloud erp malaysia"
- [ ] Top 20 for "pos system malaysia"
- [ ] 50+ keywords ranking in top 100

### Technical:
- [ ] All Core Web Vitals in green
- [ ] Mobile usability score 90+
- [ ] PageSpeed score 80+ (mobile and desktop)
- [ ] 0 crawl errors in Search Console

### Conversions:
- [ ] 20+ qualified leads per month
- [ ] 5+ demo requests per month
- [ ] 10+ contact form submissions per month

---

## Monthly Recurring Tasks

### Week 1 of Each Month:
- [ ] Review Search Console performance
- [ ] Analyze top-performing pages
- [ ] Check for technical errors
- [ ] Review competitor rankings

### Week 2 of Each Month:
- [ ] Publish 1-2 new blog posts
- [ ] Update 1-2 existing pages with fresh content
- [ ] Add new internal links
- [ ] Check for broken links

### Week 3 of Each Month:
- [ ] Review Core Web Vitals
- [ ] Optimize slow pages
- [ ] Test mobile usability
- [ ] Validate schema markup

### Week 4 of Each Month:
- [ ] Create monthly SEO report
- [ ] Plan next month's content
- [ ] Research new keywords
- [ ] Analyze backlink profile

---

## Red Flags to Watch For

### Weekly Checks:
- [ ] No sudden traffic drops
- [ ] No new crawl errors
- [ ] No broken internal links
- [ ] No Core Web Vitals degradation

### Monthly Checks:
- [ ] No ranking drops for priority keywords
- [ ] No manual actions in Search Console
- [ ] No duplicate content issues
- [ ] No site speed degradation

---

## Resources Needed

### Content Creation:
- Content writer (familiar with ERP/POS systems)
- Malaysian market knowledge
- LHDN/E-Invoice expertise
- Industry-specific knowledge (Retail, F&B, Manufacturing)

### Technical:
- Hugo knowledge (site modifications)
- Schema markup implementation
- Image optimization tools
- PageSpeed optimization expertise

### Tools (Free):
- Google Search Console
- Google Analytics 4
- Google PageSpeed Insights
- Google Rich Results Test
- Google Mobile-Friendly Test

### Tools (Paid - Recommended):
- SEMrush or Ahrefs (keyword research, tracking)
- Screaming Frog (technical audits)

---

## Contact for Questions

**SEO Strategy Questions:**
- Refer to: SEO-STRATEGY-2025.md (comprehensive strategy)
- Refer to: SEO-QUICK-REFERENCE.md (templates and guidelines)

**Implementation Questions:**
- Review this document for step-by-step actions
- Check Hugo documentation for technical implementation
- Test changes locally before deploying

---

## Next Steps

1. **Review this action plan** with team
2. **Assign responsibilities** for each phase
3. **Set realistic timelines** based on resources
4. **Start with Week 1 priorities** (E-Invoice page is CRITICAL)
5. **Track progress** using checklist format
6. **Measure results** after 30, 60, 90 days

---

**Remember:** SEO is a marathon, not a sprint. Focus on:
- Quality over quantity
- User value over search engines
- Consistent execution over perfection
- Measuring and optimizing over guessing

**Start with the highest-impact pages first:**
1. E-Invoice landing page (highest urgency)
2. Homepage optimization (highest traffic)
3. Industry landing pages (highest conversion potential)

---

**Document Version:** 1.0
**Last Updated:** October 1, 2025
**Status:** READY FOR IMPLEMENTATION
