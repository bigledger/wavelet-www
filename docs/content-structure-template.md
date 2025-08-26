# BigLedger Documentation Content Structure Template

## Standard Page Structure

Every documentation page should follow this structure:

```markdown
---
title: [Clear, Descriptive Title]
description: [One-line description for SEO]
weight: [Number for ordering]
tags: [relevant, tags]
audience: [developers|business-users|administrators|all]
complexity: [beginner|intermediate|advanced]
readingTime: [X minutes]
lastUpdated: [Date]
---

# [Page Title]

## 🎯 TLDR (Too Long; Didn't Read)
[3-5 bullet points summarizing the key takeaways]
- Key point 1
- Key point 2
- Key point 3

## 📖 Overview
[Brief introduction explaining what this page covers and why it matters]

## 👥 Target Audience
This guide is intended for:
- [Specific role 1]: [Why they need this]
- [Specific role 2]: [Why they need this]

## 📋 Prerequisites
Before reading this guide, you should:
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

## 🔍 What You'll Learn
By the end of this guide, you will understand:
1. [Learning outcome 1]
2. [Learning outcome 2]
3. [Learning outcome 3]

---

## [Main Content Section 1]

### [Subsection 1.1]
[Content with clear explanations]

{{< callout type="info" >}}
**Note**: This is an informational note providing additional context.
{{< /callout >}}

### [Subsection 1.2]
[Content with examples]

{{< callout type="tip" >}}
**💡 Pro Tip**: Best practices and helpful suggestions go here.
{{< /callout >}}

## [Main Content Section 2]

### How It Works
[Technical explanation with diagrams if needed]

{{< callout type="warning" >}}
**⚠️ Warning**: Important cautionary information that users should be aware of.
{{< /callout >}}

### Best Practices
- [Practice 1]
- [Practice 2]

{{< callout type="success" >}}
**✅ Success**: Confirmation or positive outcome information.
{{< /callout >}}

### Common Use Cases
1. **[Use Case 1]**: [Description]
2. **[Use Case 2]**: [Description]

{{< callout type="error" >}}
**❌ Important**: Critical information that could lead to errors if ignored.
{{< /callout >}}

## 💡 Key Takeaways
- **[Concept 1]**: [Brief explanation]
- **[Concept 2]**: [Brief explanation]
- **[Concept 3]**: [Brief explanation]

## 🔗 See Also
- [Related Topic 1](/path/to/page) - [Why it's related]
- [Related Topic 2](/path/to/page) - [Why it's related]
- [Related Topic 3](/path/to/page) - [Why it's related]

## ❓ Frequently Asked Questions

<details>
<summary>Question 1?</summary>
Answer to question 1
</details>

<details>
<summary>Question 2?</summary>
Answer to question 2
</details>

## 📚 Further Reading
- [External Resource 1](https://example.com) - [Description]
- [External Resource 2](https://example.com) - [Description]

## 🤝 Need Help?
- **Community Forum**: [Link to forum]
- **Support**: [Link to support]
- **Training**: [Link to training resources]
```

## Admonition/Callout Types

### Available Callout Types in Hextra Theme

#### 1. **Info Callout** (Default)
```markdown
{{< callout type="info" >}}
**Information**: General information or notes
{{< /callout >}}
```
Use for: General information, additional context, FYI notes

#### 2. **Tip Callout**
```markdown
{{< callout type="tip" >}}
**💡 Tip**: Helpful suggestions and best practices
{{< /callout >}}
```
Use for: Best practices, pro tips, shortcuts, efficiency improvements

#### 3. **Warning Callout**
```markdown
{{< callout type="warning" >}}
**⚠️ Warning**: Important cautionary information
{{< /callout >}}
```
Use for: Potential issues, deprecated features, cautions

#### 4. **Error/Danger Callout**
```markdown
{{< callout type="error" >}}
**❌ Critical**: Critical warnings or error information
{{< /callout >}}
```
Use for: Critical errors, data loss risks, security issues

#### 5. **Success Callout**
```markdown
{{< callout type="success" >}}
**✅ Success**: Positive confirmations or achievements
{{< /callout >}}
```
Use for: Successful outcomes, confirmations, completed steps

### Custom Admonitions Using HTML

For more control, you can also use HTML:

```html
<div class="admonition note">
<p class="admonition-title">📝 Note</p>
<p>Custom note content here</p>
</div>

<div class="admonition tip">
<p class="admonition-title">💡 Tip</p>
<p>Custom tip content here</p>
</div>

<div class="admonition warning">
<p class="admonition-title">⚠️ Warning</p>
<p>Custom warning content here</p>
</div>

<div class="admonition danger">
<p class="admonition-title">🚨 Danger</p>
<p>Custom danger content here</p>
</div>

<div class="admonition important">
<p class="admonition-title">❗ Important</p>
<p>Custom important content here</p>
</div>
```

### Malaysian Business Context Callouts

For BigLedger documentation, consider these specific callout patterns:

```markdown
{{< callout type="info" >}}
**🇲🇾 Malaysian Compliance**: This feature complies with SST requirements and LHDN e-Invoice standards.
{{< /callout >}}

{{< callout type="warning" >}}
**⚠️ MDEC Requirement**: Ensure this configuration aligns with MDEC Digital Investment Office guidelines.
{{< /callout >}}

{{< callout type="tip" >}}
**💰 Cost Saving Tip**: Malaysian SMEs can save up to 30% by utilizing this feature effectively.
{{< /callout >}}

{{< callout type="success" >}}
**✅ PEPPOL Ready**: This module is fully compliant with PEPPOL standards for cross-border invoicing.
{{< /callout >}}
```

## Content Categories

### 1. Module Documentation
- Overview pages
- Feature descriptions
- Configuration guides
- User guides
- API references

### 2. Tutorial/How-To Content
- Step-by-step guides
- Video tutorials
- Quick starts
- Best practices

### 3. Reference Documentation
- API documentation
- Configuration references
- Glossaries
- Technical specifications

### 4. Conceptual Documentation
- Architecture overviews
- Design patterns
- Integration strategies
- Business processes

## Writing Guidelines

### Tone and Voice
- **Professional but approachable**
- **Clear and concise**
- **Action-oriented**
- **Malaysian business context aware**

### Structure Rules
1. Start with the end in mind (TLDR first)
2. Progressive disclosure (simple to complex)
3. Use visual hierarchy (headers, bullets, bold)
4. Include practical examples
5. Provide context for Malaysian businesses
6. Use admonitions strategically (don't overuse)

### When to Use Each Admonition Type

| Type | Use Case | Frequency | Example |
|------|----------|-----------|---------|
| **Info** | Additional context, FYI | Common | "The system processes transactions in MYR by default" |
| **Tip** | Best practices, shortcuts | Moderate | "Enable auto-reconciliation to save 2 hours daily" |
| **Warning** | Potential issues, cautions | Selective | "Changing this setting affects all branches" |
| **Error** | Critical risks, data loss | Rare | "Do not delete this without backup" |
| **Success** | Confirmations, achievements | Moderate | "Setup completed successfully" |

### Visual Elements
- Screenshots with annotations
- Flowcharts for processes
- Tables for comparisons
- Icons for visual breaks
- Code examples with syntax highlighting
- Strategic use of callouts/admonitions

## Cross-Reference Strategy

### Internal Links
- Link to prerequisites
- Link to related features
- Link to next steps
- Link to troubleshooting

### Categories for "See Also"
1. **Related Features**: Same module, different features
2. **Integration Points**: How this connects with other modules
3. **Business Processes**: Related business workflows
4. **Technical Deep Dives**: Advanced topics
5. **Troubleshooting**: Common issues and solutions

## Example: Fully Structured Page

```markdown
---
title: Setting Up GST/SST in BigLedger
description: Complete guide to configure Malaysian GST/SST tax settings
weight: 10
tags: [tax, compliance, malaysia, sst]
audience: [administrators, accountants]
complexity: intermediate
readingTime: 15 minutes
lastUpdated: 2024-08-18
---

# Setting Up GST/SST in BigLedger

## 🎯 TLDR
- Configure SST rates for Malaysian tax compliance
- Set up tax codes for different product categories
- Enable automatic tax calculations
- Generate SST-03 returns with one click

## 📖 Overview
This guide walks you through configuring Sales and Service Tax (SST) in BigLedger, ensuring compliance with Malaysian tax regulations while automating your tax calculations and reporting.

{{< callout type="info" >}}
**🇲🇾 Malaysian Tax Update**: As of 2024, SST rates are 10% for sales tax and 6% for service tax. Digital services are subject to 8% service tax.
{{< /callout >}}

## 👥 Target Audience
This guide is intended for:
- **Finance Managers**: Need to ensure tax compliance
- **System Administrators**: Responsible for system configuration
- **Accountants**: Handle day-to-day tax operations

[Rest of content follows structure...]
```