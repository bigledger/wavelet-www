# SEO Quick Reference Guide - Wavelet

**Quick reference for implementing SEO best practices on Wavelet website**

---

## Page Templates

### Homepage SEO Template

```markdown
---
title: "Wavelet - Cloud ERP & POS Solution | MDEC PEPPOL Certified Malaysia"
description: "Complete cloud ERP and POS system for Malaysian businesses. MDEC PEPPOL accredited E-Invoice, multi-industry support, 99.9% uptime. Trusted by 10,000+ businesses across Southeast Asia."
---

# Complete Cloud ERP & POS Solution for Growing Malaysian Businesses

[Content starts here - 1,500-2,000 words]
```

### Industry Landing Page Template

```markdown
---
title: "[Industry] [Solution Type] Malaysia | [Key Features] | Wavelet"
description: "Complete [solution] for Malaysian [industry] with [feature 1], [feature 2], [feature 3], and E-Invoice compliance."
sitemap:
  priority: 0.9
  changefreq: "weekly"
---

# [Industry]-Specific [Solution] for Malaysian Businesses

[Introduction paragraph with primary keyword in first 100 words]

## Why Choose Wavelet for [Industry]

[Pain points and solutions - 3-5 points]

## Key Features for [Industry]

### Feature 1
[Detailed explanation]

### Feature 2
[Detailed explanation]

### Feature 3
[Detailed explanation]

## Success Stories

[Case study or testimonial]

## How It Works

[Implementation/usage flow]

## Pricing & Plans

[Pricing information with CTA]

## Frequently Asked Questions

### Question 1
Answer 1

### Question 2
Answer 2

[Continue with 5-8 FAQs]

## Get Started Today

[Strong CTA with contact options]

## Related Solutions

- [Link to related solution 1]
- [Link to related solution 2]
- [Link to related solution 3]

[Target: 2,500-3,000 words]
```

---

## Title Tag Formulas

### Homepage
```
[Brand] - [Primary Keyword] | [Trust Signal] [Location]
Example: Wavelet - Cloud ERP & POS Solution | MDEC PEPPOL Certified Malaysia
```

### Industry Pages
```
[Industry] [Solution] Malaysia | [Key Features] | [Brand]
Example: Retail POS System Malaysia | E-Commerce Integration & Inventory | Wavelet
```

### Feature Pages
```
[Feature] - [Benefit] | [Brand] Malaysia
Example: E-Invoice Malaysia - LHDN Compliance | Wavelet
```

### General Rule
- Keep under 60 characters
- Primary keyword at start
- Brand at end
- Include location (Malaysia/Singapore)
- Add trust signal when possible

---

## Meta Description Formulas

### Homepage
```
Complete [product/service] for Malaysian [audience]. [Trust signal], [key features]. Trusted by [social proof].
```

### Industry Pages
```
Complete [solution] for Malaysian [industry] with [feature 1], [feature 2], [feature 3], and [compliance].
```

### General Rules
- 140-160 characters
- Include primary keyword in first sentence
- Add call-to-action
- Mention location (Malaysia)
- Include unique selling point

---

## Heading Structure Template

```html
<h1>One H1 Only - Main Keyword</h1>

<h2>Primary Section 1</h2>
  <h3>Subsection 1.1</h3>
  <h3>Subsection 1.2</h3>

<h2>Primary Section 2</h2>
  <h3>Subsection 2.1</h3>
  <h3>Subsection 2.2</h3>

<h2>FAQ Section</h2>
  <h3>Question 1?</h3>
  <h3>Question 2?</h3>
```

**Rules:**
- Only ONE H1 per page
- H1 must include primary keyword
- Never skip heading levels (H1 → H2 → H3)
- Use H2 for main sections
- Use H3 for subsections
- Keep headings concise (< 70 characters)

---

## Schema Markup Quick Reference

### Organization Schema (All Pages)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Wavelet",
  "alternateName": "BigLedger",
  "url": "https://www.wavelet.net",
  "logo": "https://www.wavelet.net/images/wavelet-logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+60-10-839-9393",
    "contactType": "Sales",
    "areaServed": ["MY", "SG"],
    "availableLanguage": ["en", "ms", "zh"]
  }
}
```

### FAQ Schema (FAQ Sections)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Question text?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Comprehensive answer text here."
    }
  }]
}
```

### Breadcrumb Schema (All Pages)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{
    "@type": "ListItem",
    "position": 1,
    "name": "Home",
    "item": "https://www.wavelet.net"
  }]
}
```

---

## Primary Keywords to Target

### Critical (Phase 1)
```
✅ e-invoice malaysia
✅ lhdn e-invoice system
✅ peppol malaysia
✅ cloud erp malaysia
✅ pos system malaysia
✅ erp system for sme malaysia
```

### High Priority (Phase 2)
```
⭐ retail pos system malaysia
⭐ restaurant pos system malaysia
⭐ manufacturing erp malaysia
⭐ erp accounting software malaysia
⭐ inventory management system malaysia
⭐ mdec peppol accredited
```

### Long-Tail (Phase 3)
```
💡 best erp for small business malaysia
💡 cloud accounting software malaysia
💡 multi-outlet pos system
💡 e-commerce erp integration
💡 lhdn approved software
```

---

## Internal Linking Rules

### Link Density
- Homepage: 15-20 links
- Main pages: 10-15 links
- Blog posts: 5-10 links
- Ratio: 1 link per 200-300 words

### Anchor Text Distribution
- Exact match: 20%
- Partial match: 40%
- Branded: 20%
- Natural/Descriptive: 20%

### Priority Linking
Always link to these pages from relevant content:
1. E-Invoice landing page
2. Solutions overview
3. Pricing page
4. Industry-specific pages

### Example Links
```markdown
<!-- Exact Match -->
[e-invoice malaysia](/solutions/e-invoice-malaysia)

<!-- Partial Match -->
[complete e-invoice compliance solution](/solutions/e-invoice-malaysia)

<!-- Branded -->
[Wavelet's E-Invoice features](/solutions/e-invoice-malaysia)

<!-- Natural -->
[learn more about LHDN compliance](/solutions/e-invoice-malaysia)
```

---

## Content Length Guidelines

| Page Type | Minimum | Optimal |
|-----------|---------|---------|
| Homepage | 1,500 | 2,000 |
| Solutions Overview | 2,000 | 2,500 |
| Industry Landing Pages | 2,500 | 3,000 |
| E-Invoice Page | 3,000+ | 4,000+ |
| Blog Posts | 1,500 | 2,500+ |
| Product Pages | 1,500 | 2,000 |

**Key Principle:** Write as much as needed to comprehensively answer the user's question.

---

## Keyword Placement Checklist

### Every Page Must Have:
- [ ] Primary keyword in title tag (start)
- [ ] Primary keyword in meta description (first sentence)
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword 3-5 times per 1,000 words (0.3-0.5% density)
- [ ] Semantic variations throughout content
- [ ] Primary keyword in at least one H2
- [ ] Primary keyword in URL slug
- [ ] Primary keyword in image alt text (at least 1)

### Avoid:
- [ ] Keyword stuffing
- [ ] Unnatural keyword usage
- [ ] Exact match repetition
- [ ] Keyword in every paragraph

---

## Technical SEO Checklist

### Must-Have on Every Page:
- [ ] Unique title tag (< 60 characters)
- [ ] Unique meta description (140-160 characters)
- [ ] One H1 heading only
- [ ] Proper heading hierarchy (H1 > H2 > H3)
- [ ] Canonical URL
- [ ] Mobile-friendly design
- [ ] Fast loading speed (< 3 seconds)
- [ ] HTTPS enabled
- [ ] Schema markup (at minimum: Organization)
- [ ] Internal links (5-15 per page)
- [ ] Images optimized (WebP, alt tags, lazy loading)

### Core Web Vitals Targets:
- [ ] LCP < 2.5 seconds
- [ ] INP < 200 milliseconds
- [ ] CLS < 0.1

---

## AI/LLM Optimization Checklist

### Content Structure:
- [ ] Use clear, semantic HTML (article, section, header, footer)
- [ ] Write in conversational, Q&A format where appropriate
- [ ] Include specific facts, numbers, dates
- [ ] Cite authoritative sources (LHDN, MDEC)
- [ ] Use structured lists and tables
- [ ] Add comprehensive FAQ sections

### Technical:
- [ ] Server-side rendering (Hugo does this)
- [ ] llms.txt file created
- [ ] Schema markup implemented
- [ ] Clean URL structure
- [ ] No JavaScript-rendered critical content

### Content Style:
- [ ] Answer questions directly and comprehensively
- [ ] Use "What/Why/How" headings
- [ ] Include step-by-step instructions
- [ ] Provide complete, self-contained answers
- [ ] Use entity-based writing (people, places, products, organizations)

---

## Malaysian Market Localization

### Language:
- Use British English spelling (organisation, colour, centre)
- Include Malay terms: "Lembaga Hasil Dalam Negeri (LHDN)"
- Use MYR for pricing
- Date format: DD/MM/YYYY

### Compliance Keywords:
- LHDN (Lembaga Hasil Dalam Negeri)
- MDEC PEPPOL
- MyInvois
- SST (Sales and Service Tax)
- EPF (Employees Provident Fund)
- SOCSO (Social Security Organisation)

### Cultural References:
- Mention multi-language support (English, Malay, Chinese)
- Reference local business practices
- Include Malaysian business hours
- Mention local data centers
- Reference local holidays (where relevant)

---

## Priority Pages to Create

### Immediate (Week 1):
1. [ ] /solutions/e-invoice-malaysia (3,500+ words)
2. [ ] Update homepage with comprehensive content
3. [ ] Create /static/llms.txt

### Short-term (Weeks 2-4):
1. [ ] /solutions/retail-pos-system-malaysia
2. [ ] /solutions/restaurant-pos-system-malaysia
3. [ ] /solutions/manufacturing-erp-malaysia
4. [ ] /solutions/wholesale-distribution-erp-malaysia

### Medium-term (Weeks 5-8):
1. [ ] Blog: "Complete Guide to LHDN E-Invoice Compliance 2025"
2. [ ] Blog: "How to Choose ERP System for Malaysian Business"
3. [ ] Case study: Retail client success
4. [ ] Case study: F&B client success

---

## Common Mistakes to Avoid

### Content:
- ❌ Thin content (< 500 words on important pages)
- ❌ Duplicate title tags across pages
- ❌ Missing meta descriptions
- ❌ Multiple H1 tags
- ❌ Keyword stuffing

### Technical:
- ❌ Slow page load (> 5 seconds)
- ❌ Not mobile-friendly
- ❌ Missing canonical tags
- ❌ Broken internal links
- ❌ No HTTPS

### Schema:
- ❌ Invalid schema markup
- ❌ Schema for hidden content
- ❌ Wrong schema type

---

## Tools & Resources

### Free Tools:
- Google Search Console
- Google Analytics 4
- Google PageSpeed Insights
- Google Rich Results Test
- Google Mobile-Friendly Test

### Testing URLs:
- PageSpeed: https://pagespeed.web.dev/
- Rich Results: https://search.google.com/test/rich-results
- Mobile-Friendly: https://search.google.com/test/mobile-friendly
- Schema Validator: https://validator.schema.org/

### Malaysian Resources:
- LHDN E-Invoice: https://www.hasil.gov.my/en/e-invoice/
- MDEC: https://mdec.my/

---

## Monthly SEO Tasks

### Week 1:
- Review Search Console performance
- Check for technical errors
- Analyze top-performing pages
- Identify new keyword opportunities

### Week 2:
- Publish 1 new blog post
- Update 1-2 existing pages
- Fix any broken links
- Add new internal links

### Week 3:
- Review Core Web Vitals
- Optimize images on slow pages
- Check mobile usability
- Test schema markup validity

### Week 4:
- Competitor analysis
- Backlink profile review
- Update statistics and facts
- Plan next month's content

---

## Success Metrics

### Track Weekly:
- Keyword rankings (top 20)
- Organic traffic
- Core Web Vitals scores

### Track Monthly:
- Total organic sessions
- Conversion rate
- Top landing pages
- New keywords ranking
- Competitors' rankings

### Targets (6 months):
- 200% increase in organic traffic
- Top 3 for primary keywords
- 50+ qualified leads per month
- All Core Web Vitals in green

---

**Document Version:** 1.0
**Last Updated:** October 1, 2025

For comprehensive details, see: SEO-STRATEGY-2025.md
