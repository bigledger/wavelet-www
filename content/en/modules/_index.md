---
title: "Modules"
description: "BigLedger's comprehensive business modules - collections of applets working together"
weight: 30
---

# BigLedger Modules

BigLedger is organized into functional modules, each containing a collection of applets that work together to deliver specific business capabilities. Understanding the module-applet relationship is key to maximizing BigLedger's potential.

## Module-Applet Architecture

{{< callout type="info" >}}
**Important Concept**: Modules are logical groupings of applets. A single applet can belong to multiple modules (many-to-many relationship). For example, the Tax Configuration Applet is used by Financial Accounting, Sales, Purchasing, and E-Commerce modules.
{{< /callout >}}

### How It Works

```
┌─────────────────────────────────────────────────────┐
│                    APPLETS                          │
│  (Reusable components - single source of truth)     │
└─────────────────────────────────────────────────────┘
                         ↓ ↑
     ┌──────────────┬────────────┬──────────────┐
     │              │            │              │
┌────▼─────┐  ┌────▼─────┐ ┌───▼──────┐ ┌────▼─────┐
│   Core   │  │Financial │ │   Sales  │ │E-Commerce│
│  Module  │  │Accounting│ │   & CRM  │ │  Module  │
└──────────┘  └──────────┘ └──────────┘ └──────────┘
```

- **Applets** are the actual functional components
- **Modules** are business-focused collections of applets
- Each module documentation references the applets it uses
- Applet documentation lives in `/applets/` (no duplication)

## Module Categories

### 1. Core Module
**Foundation for all operations**
- Essential master data applets
- System configuration applets
- Required by all other modules
- [Explore Core Module →](/modules/core/)

### 2. Financial Modules

#### Financial Accounting
**Complete accounting and financial management**
- General ledger and journals
- Accounts receivable/payable
- Financial reporting
- [Learn about Financial Accounting →](/modules/financial-accounting/)

### 3. Operations Modules

#### Inventory & Warehouse
**Stock and warehouse management**
- Multi-location inventory
- Stock movements
- Warehouse operations
- [Manage Inventory →](/modules/inventory/)

#### Sales & CRM
**Customer relationship and sales management**
- Customer management
- Quotations and orders
- Sales analytics
- [Explore Sales & CRM →](/modules/crm/)

#### Purchasing
**Procurement and vendor management**
- Purchase orders
- Vendor management
- Purchase analytics
- [View Purchasing →](/modules/procurement/)

### 4. Retail & Commerce

#### Point of Sale (POS)
**Retail store operations**
- Cashier operations
- Multi-outlet management
- Offline/online sync
- [Discover POS Features →](/modules/pos/)

#### E-Commerce
**Online sales and marketplace integration**
- Multi-channel selling
- Marketplace integration
- Website management
- [Explore E-Commerce →](/modules/ecommerce/)

### 5. Human Resources

#### HR & Payroll
**Employee and payroll management**
- Employee records
- Payroll processing
- Leave and claims
- [HR Management →](/modules/hr/)

### 6. Production

#### Manufacturing
**Production and assembly operations**
- Bill of materials
- Production planning
- Quality control
- [Manufacturing Guide →](/modules/manufacturing/)

#### Projects
**Project and task management**
- Project tracking
- Resource allocation
- Time tracking
- [Project Management →](/modules/projects/)

## Understanding Module Composition

Each module consists of:

### Core Applets
Applets that are essential for the module's primary function

### Shared Applets
Applets from the Core Module or other modules that provide supporting functions

### Optional Applets
Additional applets that enhance functionality but aren't required

## Example: Financial Accounting Module

```yaml
Core Applets:
  - General Ledger Applet
  - Journal Entry Applet
  - Financial Reports Applet

Shared Applets (from Core Module):
  - Chart of Accounts Applet
  - Tax Configuration Applet
  - Cashbook Applet
  - Organization Applet

Optional Applets:
  - Budget Management Applet
  - Fixed Assets Applet
  - Cost Center Applet
```

## Module Implementation Path

### Phase 1: Foundation
1. **Core Module** - Set up master data and configurations
2. **Financial Accounting** - Establish financial foundation

### Phase 2: Operations
3. **Sales & CRM** or **Purchasing** - Based on business priority
4. **Inventory & Warehouse** - If handling physical goods

### Phase 3: Expansion
5. **POS** - For retail operations
6. **E-Commerce** - For online sales
7. **Manufacturing** - For production
8. **HR & Payroll** - For employee management

## Module Selection Guide

### For Retail Businesses
- Core Module
- Financial Accounting
- POS Module
- Inventory & Warehouse
- E-Commerce (optional)

### For Wholesale/Distribution
- Core Module
- Financial Accounting
- Sales & CRM
- Purchasing
- Inventory & Warehouse

### For Service Businesses
- Core Module
- Financial Accounting
- Sales & CRM
- Projects
- HR & Payroll

### For Manufacturing
- Core Module
- Financial Accounting
- Manufacturing
- Inventory & Warehouse
- Purchasing

### For E-Commerce
- Core Module
- Financial Accounting
- E-Commerce
- Inventory & Warehouse
- Sales & CRM

## Integration Between Modules

Modules are designed to work seamlessly together:

### Data Flow
- Master data flows from Core Module to all others
- Transactions flow between operational modules
- Financial data consolidates in Financial Accounting

### Process Integration
- Sales orders (Sales) → Delivery (Warehouse) → Invoice (Financial)
- Purchase (Purchasing) → Receipt (Warehouse) → Payment (Financial)
- Online orders (E-Commerce) → Fulfillment (Warehouse) → Accounting (Financial)

## Getting Started

1. **Understand your needs** - Which modules match your business?
2. **Start with Core** - Essential foundation for all modules
3. **Add modules gradually** - Implement in phases
4. **Configure applets** - Set up the applets within each module
5. **Train users** - Module-specific training for teams

## Module vs Applet Documentation

### When to Read Module Documentation
- Understanding business processes
- Learning module capabilities
- Planning implementation
- Training by department

### When to Read Applet Documentation
- Detailed configuration steps
- Technical specifications
- Troubleshooting specific features
- Understanding cross-module usage

## Related Resources

### Applet Library
- [Browse All Applets](/applets/) - Complete applet documentation
- [Applet Directory](/applets/applet-directory/) - Searchable applet list
- [Applet Store](/applets/applet-store/) - Add-on applets

### Implementation Guides
- [Getting Started Guide](/user-guide/introduction/)
- [Implementation Best Practices](/guides/advanced/integration-best-practices/)
- [Role-Based Training](/guides/roles/)

{{< callout type="tip" >}}
**Remember**: Modules are business-focused groupings. The same applet can serve multiple modules. Always refer to the applet documentation in `/applets/` for detailed configuration and features.
{{< /callout >}}