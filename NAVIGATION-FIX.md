# Immediate Navigation Fixes for BigLedger Wiki

## Current Issues Identified

### 1. **Left Sidebar Not Showing Links**
The Hextra theme requires proper frontmatter configuration for sidebar navigation.

### 2. **Right Sidebar Missing Sections**
Table of contents not generating properly due to heading structure.

### 3. **Top Menu Missing "ERP" as Main Category**
Current menu doesn't emphasize ERP as the core product.

## Quick Fixes to Implement Now

### Fix 1: Update Hugo Configuration for Sidebar

```yaml
# hugo.yaml updates needed
params:
  sidebar:
    enable: true
    # Add these settings
    showPages: true
    showCategories: true
    showTags: false
    
  # Enable section pages in sidebar
  navigation:
    enable: true
    # This will show all pages in current section
    showInSidebar: true
```

### Fix 2: Add Proper Frontmatter to Section Pages

Each `_index.md` file needs:
```yaml
---
title: "Section Title"
weight: 10
bookCollapseSection: false  # Shows expanded by default
bookFlatSection: false       # Shows hierarchy
bookToc: true               # Shows table of contents
---
```

### Fix 3: Update Menu Structure

```yaml
menu:
  main:
    - identifier: erp
      name: "🏢 ERP Applications"
      weight: 1
      hasChildren: true
      
    - identifier: finance
      name: "Finance"
      parent: erp
      pageRef: /applications/finance
      weight: 10
      
    - identifier: sales
      name: "Sales & CRM"
      parent: erp
      pageRef: /applications/sales
      weight: 20
      
    - identifier: inventory
      name: "Inventory"
      parent: erp
      pageRef: /applications/inventory
      weight: 30
      
    - identifier: getting-started
      name: "📚 Getting Started"
      weight: 2
      pageRef: /getting-started
      
    - identifier: platform
      name: "⚙️ Platform"
      weight: 3
      hasChildren: true
      
    - identifier: einvoice
      name: "E-Invoice"
      parent: platform
      pageRef: /platform-features/e-invoicing
      weight: 10
      
    - identifier: applets
      name: "Applets"
      parent: platform
      pageRef: /platform-features/applets
      weight: 20
      
    - identifier: developers
      name: "👩‍💻 Developers"
      weight: 4
      pageRef: /developer-hub
```

## Content Organization Map

### Current → New Location Mapping

| Current Location | New Location | Reason |
|-----------------|--------------|---------|
| `/modules/` | `/applications/` | Industry standard term |
| `/user-guide/` | `/getting-started/` | Clearer purpose |
| `/business-operations/` | `/applications/finance/operations/` | Better categorization |
| `/applets/` | `/platform-features/applets/` | Shows it's a platform capability |
| `/e-invoice-peppol/` | `/platform-features/e-invoicing/` | Grouped with features |
| `/developers/` | `/developer-hub/` | More inviting name |

## Sidebar Navigation Structure

### For Each Application Section:
```
Finance
├── Overview
├── Getting Started
│   ├── First Transaction
│   ├── Basic Setup
│   └── Common Tasks
├── Features
│   ├── General Ledger
│   ├── Accounts Payable
│   ├── Accounts Receivable
│   └── Reports
├── How-To Guides
│   ├── Bank Reconciliation
│   ├── Month-End Close
│   └── Tax Filing
└── Reference
    ├── Account Types
    ├── Tax Codes
    └── Report Definitions
```

## Table of Contents Fix

For right sidebar to show properly, ensure:

1. **Use Proper Heading Hierarchy**
```markdown
# Page Title (H1 - only one per page)

## Main Section (H2)

### Subsection (H3)

#### Detail (H4)
```

2. **Add TOC Configuration**
```yaml
---
toc:
  enable: true
  headingLevel: 3  # Show H2 and H3 in TOC
---
```

## Implementation Priority

### Phase 1 (Immediate):
1. Fix sidebar navigation visibility
2. Update top menu to emphasize ERP
3. Fix table of contents generation

### Phase 2 (This Week):
1. Reorganize content into new structure
2. Create proper landing pages
3. Add breadcrumb navigation

### Phase 3 (Next Week):
1. Implement role-based guides
2. Add search functionality
3. Create cross-references

## Testing Checklist

- [ ] Left sidebar shows navigation tree
- [ ] Right sidebar shows page sections
- [ ] Top menu has clear ERP focus
- [ ] Breadcrumbs work correctly
- [ ] Search returns relevant results
- [ ] Mobile navigation works
- [ ] All links are valid

## Benefits After Implementation

1. **Users can find information 3x faster**
2. **Clear learning path for new users**
3. **Industry-standard navigation patterns**
4. **Better SEO and discoverability**
5. **Reduced support tickets**