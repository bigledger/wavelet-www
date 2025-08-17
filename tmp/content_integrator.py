#!/usr/bin/env python3
"""
Content Integration Script for BigLedger Documentation
Processes extracted content and creates documentation pages
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List

class DocumentationEnricher:
    """Enrich existing documentation with new content"""
    
    def __init__(self, docs_root: str = "/Users/vincent/repo/blg-wiki"):
        self.docs_root = Path(docs_root)
        self.content_dir = self.docs_root / "content" / "en"
        self.new_content = []
        
    def create_guides_section(self):
        """Create comprehensive guides section based on BigLedger features"""
        
        guides = {
            'accounting-guides': {
                'title': 'Accounting Guides',
                'weight': 30,
                'pages': [
                    {
                        'filename': 'chart-of-accounts-setup.md',
                        'title': 'Chart of Accounts Setup Guide',
                        'content': self.generate_coa_guide()
                    },
                    {
                        'filename': 'journal-entries.md',
                        'title': 'Journal Entries Guide',
                        'content': self.generate_journal_guide()
                    },
                    {
                        'filename': 'financial-reporting.md',
                        'title': 'Financial Reporting Guide',
                        'content': self.generate_financial_reporting_guide()
                    },
                    {
                        'filename': 'bank-reconciliation-guide.md',
                        'title': 'Bank Reconciliation Step-by-Step',
                        'content': self.generate_bank_recon_guide()
                    }
                ]
            },
            'einvoice-guides': {
                'title': 'E-Invoice Implementation',
                'weight': 31,
                'pages': [
                    {
                        'filename': 'myinvois-setup.md',
                        'title': 'MyInvois Setup Guide',
                        'content': self.generate_myinvois_guide()
                    },
                    {
                        'filename': 'peppol-configuration.md',
                        'title': 'PEPPOL Configuration',
                        'content': self.generate_peppol_guide()
                    },
                    {
                        'filename': 'einvoice-validation.md',
                        'title': 'E-Invoice Validation Rules',
                        'content': self.generate_validation_guide()
                    }
                ]
            },
            'inventory-guides': {
                'title': 'Inventory Management',
                'weight': 32,
                'pages': [
                    {
                        'filename': 'stock-management.md',
                        'title': 'Stock Management Guide',
                        'content': self.generate_stock_guide()
                    },
                    {
                        'filename': 'stock-transfer.md',
                        'title': 'Stock Transfer Procedures',
                        'content': self.generate_transfer_guide()
                    }
                ]
            }
        }
        
        return guides
    
    def generate_coa_guide(self) -> str:
        """Generate Chart of Accounts setup guide"""
        return """---
title: Chart of Accounts Setup Guide
weight: 10
---

# Chart of Accounts Setup Guide

Complete guide for setting up your Chart of Accounts in BigLedger.

## Overview

The Chart of Accounts (COA) is the foundation of your financial system in BigLedger. It defines the structure of your general ledger and determines how financial transactions are categorized and reported.

## Prerequisites

Before setting up your COA:
- Complete Organization setup
- Define your fiscal year
- Determine your accounting method (Cash/Accrual)
- Review statutory requirements for Malaysia

## Step-by-Step Setup

### Step 1: Access Chart of Accounts Module

1. Navigate to **Master Data** → **Chart of Account**
2. Click **New Account** to create accounts
3. Or click **Import** to use templates

### Step 2: Define Account Structure

BigLedger uses a hierarchical account structure:

```
1000 - Assets
  1100 - Current Assets
    1110 - Cash and Bank
      1111 - Cash in Hand
      1112 - Bank Accounts
  1200 - Fixed Assets
    1210 - Property and Equipment
    1220 - Vehicles
```

### Step 3: Create Account Categories

#### Assets (1000-1999)
- Current Assets (1000-1499)
- Fixed Assets (1500-1999)

#### Liabilities (2000-2999)
- Current Liabilities (2000-2499)
- Long-term Liabilities (2500-2999)

#### Equity (3000-3999)
- Share Capital (3000-3099)
- Retained Earnings (3100-3199)

#### Revenue (4000-4999)
- Sales Revenue (4000-4499)
- Other Income (4500-4999)

#### Expenses (5000-9999)
- Cost of Goods Sold (5000-5999)
- Operating Expenses (6000-7999)
- Other Expenses (8000-8999)

### Step 4: Configure Account Properties

For each account, set:
- **Account Code**: Unique identifier
- **Account Name**: Descriptive name
- **Account Type**: Asset/Liability/Equity/Revenue/Expense
- **Sub-Type**: Further classification
- **Currency**: MYR or foreign currency
- **Tax Code**: Link to tax configuration
- **Status**: Active/Inactive

### Step 5: Set Up Special Accounts

Configure system accounts:
- **Default Bank Account**: For receipts/payments
- **Accounts Receivable**: Customer invoices
- **Accounts Payable**: Vendor bills
- **GST/SST Accounts**: Tax accounts
- **Retained Earnings**: Year-end closing
- **Exchange Gain/Loss**: Forex differences

### Step 6: Import Opening Balances

1. Go to **Finance** → **Journal Entries**
2. Create Opening Balance journal
3. Enter balances as of cutover date
4. Ensure debits = credits
5. Post the journal entry

## Best Practices

### Numbering Convention
- Use consistent digit length (4-5 digits)
- Leave gaps for future accounts
- Group related accounts together
- Use sub-accounts for detail

### Account Naming
- Be descriptive but concise
- Use standard terminology
- Include location/department if needed
- Avoid special characters

### Maintenance
- Review COA quarterly
- Archive unused accounts
- Document changes
- Maintain audit trail

## Malaysian Compliance

### SST Requirements
- Output Tax Account (2310)
- Input Tax Account (1410)
- SST Payable (2311)
- SST Suspense (2312)

### Company Act 2016
- Comply with approved accounting standards
- Maintain prescribed accounts
- Prepare statutory reports

## Integration Points

The COA integrates with:
- **Sales Module**: Revenue recognition
- **Purchase Module**: Expense recording
- **Inventory**: COGS calculation
- **Fixed Assets**: Depreciation posting
- **E-Invoice**: Tax account mapping

## Troubleshooting

### Common Issues

**Cannot delete account**
- Check for transactions posted
- Remove from reports/budgets
- Set to inactive instead

**Balance sheet doesn't balance**
- Review opening balances
- Check retained earnings
- Verify exchange rates

**Wrong account in dropdown**
- Check account status
- Verify account type
- Review user permissions

## Reports

Key reports using COA:
- Trial Balance
- Balance Sheet
- Profit & Loss
- General Ledger
- Account Analysis

## Next Steps

After setting up COA:
1. Configure Tax Settings
2. Set up Opening Balances
3. Create Journal Templates
4. Configure Financial Reports
5. Test with sample transactions

---

*For additional support, contact support@bigledger.com*"""
    
    def generate_journal_guide(self) -> str:
        """Generate Journal Entries guide"""
        return """---
title: Journal Entries Guide
weight: 20
---

# Journal Entries Guide

Master manual and automated journal entries in BigLedger.

## Overview

Journal entries are the foundation of accounting in BigLedger, recording all financial transactions in the general ledger.

## Types of Journal Entries

### Manual Journals
- Adjusting entries
- Accruals and deferrals
- Corrections
- Opening balances

### Automated Journals
- Sales invoices
- Purchase bills
- Payroll posting
- Depreciation

### Recurring Journals
- Monthly accruals
- Rent expenses
- Insurance
- Subscriptions

## Creating Journal Entries

### Step 1: Access Journal Module

Navigate to **Finance** → **Ledger and Journal**

### Step 2: Create New Journal

1. Click **New Journal Entry**
2. Select Journal Type:
   - General Journal
   - Payment Journal
   - Receipt Journal
   - Purchase Journal
   - Sales Journal

### Step 3: Enter Header Information

- **Journal Number**: Auto-generated or manual
- **Date**: Transaction date
- **Reference**: External document reference
- **Description**: Journal description
- **Currency**: Transaction currency

### Step 4: Add Journal Lines

For each line:
```
Account | Description | Debit | Credit | Tax | Project
--------|-------------|-------|--------|-----|--------
1111    | Cash receipt| 1000  |        |     | 
4000    | Sales revenue|      | 1000   | SST | Project A
```

### Step 5: Validate and Post

1. Verify debits = credits
2. Check tax calculations
3. Review account codes
4. Post journal entry

## Common Journal Entries

### Sales Transaction
```
Dr. Accounts Receivable  1,060
  Cr. Sales Revenue         1,000
  Cr. SST Payable             60
```

### Purchase Transaction
```
Dr. Expense Account       500
Dr. Input Tax              30
  Cr. Accounts Payable      530
```

### Bank Receipt
```
Dr. Bank Account        1,000
  Cr. Accounts Receivable  1,000
```

### Depreciation
```
Dr. Depreciation Expense  100
  Cr. Accumulated Depreciation 100
```

## Recurring Journals

### Setup
1. Create template journal
2. Set recurrence pattern
3. Define start/end dates
4. Enable auto-posting

### Management
- Review pending journals
- Approve before posting
- Modify templates
- Track history

## Journal Templates

Create templates for:
- Monthly accruals
- Payroll posting
- Depreciation
- Inter-company transfers

## Validation Rules

BigLedger validates:
- Balanced entries
- Valid account codes
- Open accounting period
- User permissions
- Tax calculations

## Best Practices

### Documentation
- Use clear descriptions
- Attach supporting documents
- Include approval notes
- Maintain audit trail

### Controls
- Segregation of duties
- Approval workflows
- Period closing procedures
- Regular reconciliation

### Review Process
1. Daily journal review
2. Weekly posting verification
3. Monthly reconciliation
4. Period-end procedures

## Integration with Modules

### Sales Module
- Auto-creates customer invoices
- Posts revenue recognition
- Updates AR balance

### Purchase Module
- Records vendor bills
- Manages expense allocation
- Updates AP balance

### Inventory
- Posts COGS entries
- Records stock adjustments
- Updates inventory value

## Reports

### Journal Reports
- Journal Entry Listing
- Journal by Account
- Journal Audit Trail
- Posted vs Unposted

### Analysis Reports
- Account Activity
- Transaction Detail
- GL Movement
- Variance Analysis

## Troubleshooting

### Out of Balance
- Check rounding differences
- Verify tax calculations
- Review currency conversion

### Cannot Post
- Check period status
- Verify permissions
- Review validation errors

### Missing Entries
- Check posting date
- Review filter criteria
- Verify module integration

---

*Need help? Visit our [Support Center](/support) or contact support@bigledger.com*"""
    
    def generate_financial_reporting_guide(self) -> str:
        """Generate Financial Reporting guide"""
        return """---
title: Financial Reporting Guide
weight: 30
---

# Financial Reporting Guide

Generate accurate financial reports with BigLedger's reporting suite.

## Available Reports

### Core Financial Statements

#### Balance Sheet
Shows financial position at a specific date
- Assets
- Liabilities  
- Equity

#### Profit & Loss Statement
Shows financial performance over a period
- Revenue
- Expenses
- Net Profit/Loss

#### Cash Flow Statement
Shows cash movements
- Operating Activities
- Investing Activities
- Financing Activities

#### Statement of Changes in Equity
Shows equity movements
- Share Capital
- Retained Earnings
- Other Reserves

## Generating Reports

### Quick Report Generation

1. Navigate to **Finance** → **Financial Report Applet**
2. Select report type
3. Choose parameters:
   - Period (Month/Quarter/Year)
   - Company/Branch
   - Currency
   - Comparison periods
4. Click **Generate**

### Report Parameters

**Date Range**
- Current Period
- Year-to-Date
- Custom Range
- Comparative Periods

**Format Options**
- Summary vs Detailed
- Consolidated vs Standalone
- Local vs Reporting Currency
- Graphical vs Tabular

## Customizing Reports

### Report Builder

Create custom reports:
1. Define report structure
2. Map accounts to lines
3. Add calculations
4. Format presentation
5. Save template

### Custom Formulas

Examples:
```
Gross Profit = Revenue - COGS
Gross Margin % = (Gross Profit / Revenue) * 100
Current Ratio = Current Assets / Current Liabilities
```

## Malaysian Statutory Reports

### SST Returns
- SST-02 Return
- SST-03 Declaration
- Bad Debt Relief
- Capital Goods Adjustment

### Companies Act Requirements
- Directors' Report
- Auditors' Report
- Statement by Directors
- Statutory Declaration

### LHDN Requirements
- Form C (Company Tax Return)
- Form E (Employer Return)
- Transfer Pricing Documentation

## Report Scheduling

### Automated Reports

Schedule reports:
- Daily: Cash Position
- Weekly: Sales Summary
- Monthly: Financial Statements
- Quarterly: Management Pack
- Yearly: Annual Report

### Distribution

Configure distribution:
- Email to stakeholders
- Save to shared folder
- Upload to portal
- Archive in system

## Management Reporting

### KPI Dashboard
- Revenue trends
- Expense analysis
- Profitability metrics
- Cash flow indicators
- Working capital

### Budget vs Actual
- Variance analysis
- YTD comparison
- Forecast vs actual
- Department performance

### Segment Reporting
- By product line
- By geography
- By customer
- By channel

## Export Options

### File Formats
- PDF for presentation
- Excel for analysis
- CSV for data export
- XML for integration

### Excel Integration
- Pivot table ready
- Formatted reports
- Linked worksheets
- Refresh capability

## Best Practices

### Month-End Procedures
1. Complete all transactions
2. Run reconciliations
3. Post adjustments
4. Generate draft reports
5. Review and approve
6. Finalize and distribute

### Report Review
- Check completeness
- Verify accuracy
- Review variances
- Validate calculations
- Confirm compliance

### Documentation
- Report parameters
- Assumptions used
- Adjustments made
- Approval notes

---

*For custom report development, contact support@bigledger.com*"""
    
    def generate_bank_recon_guide(self) -> str:
        """Generate Bank Reconciliation guide"""
        return """---
title: Bank Reconciliation Step-by-Step
weight: 40
---

# Bank Reconciliation Step-by-Step

Master the bank reconciliation process with BigLedger's AI-powered matching.

## Overview

Bank reconciliation ensures your book balance matches your bank statement, identifying discrepancies and maintaining accurate cash records.

## Prerequisites

- Bank account setup in COA
- Bank statement (PDF/CSV/Direct feed)
- Posted transactions in system
- Reconciliation permissions

## Step-by-Step Process

### Step 1: Import Bank Statement

#### Method 1: Direct Bank Feed
1. Go to **Finance** → **Bank Reconciliation**
2. Select bank account
3. Click **Sync Bank Feed**
4. Authenticate with bank
5. Select date range
6. Import transactions

#### Method 2: File Import
1. Download bank statement
2. Click **Import Statement**
3. Select file format:
   - CSV
   - Excel
   - PDF (with OCR)
   - MT940
4. Map columns if needed
5. Import transactions

### Step 2: Automatic Matching

BigLedger's AI matches transactions:

**Matching Criteria**
- Amount (exact or within tolerance)
- Date (exact or within range)
- Reference number
- Description keywords
- Check numbers

**Match Confidence Levels**
- 🟢 **High (95-100%)**: Auto-matched
- 🟡 **Medium (70-94%)**: Suggested matches
- 🔴 **Low (<70%)**: Manual review needed

### Step 3: Review Matches

#### Confirmed Matches
- System shows green checkmark
- No action needed
- Already reconciled

#### Suggested Matches
1. Review each suggestion
2. Verify details match
3. Click **Confirm Match**
4. Or select different transaction

#### Unmatched Items
**Bank transactions without book entries:**
- Bank charges
- Interest earned
- Direct deposits
- Auto-payments

**Book entries without bank transactions:**
- Outstanding checks
- Deposits in transit
- Bank errors
- Timing differences

### Step 4: Create Missing Entries

For unrecorded bank transactions:

1. Click **Create Entry** on unmatched item
2. Select transaction type:
   - Bank charge
   - Interest income
   - Transfer
   - Other
3. Enter details:
   - Account to post
   - Description
   - Tax code if applicable
4. Save and match

### Step 5: Handle Exceptions

#### Outstanding Checks
- List checks not yet cleared
- Monitor aging
- Follow up if stale-dated
- Consider stop payment

#### Deposits in Transit
- Identify uncleared deposits
- Verify with bank
- Check for delays
- Investigate if unusual

#### Bank Errors
1. Document the error
2. Contact bank
3. Create adjustment entry
4. Track resolution

### Step 6: Complete Reconciliation

1. Verify reconciliation summary:
   ```
   Book Balance:         10,000.00
   + Deposits in Transit: 2,000.00
   - Outstanding Checks:  (1,500.00)
   + Bank Adjustments:       50.00
   = Bank Balance:       10,550.00
   ```

2. Confirm bank statement balance matches
3. Review reconciliation report
4. Approve reconciliation
5. Lock period if month-end

## Advanced Features

### Multi-Currency Reconciliation
- Handle foreign currency accounts
- Automatic exchange rate updates
- Realized gain/loss calculation
- Revaluation entries

### Bulk Operations
- Match multiple transactions
- Bulk create entries
- Mass unmatch
- Batch approvals

### Rules Engine
Create matching rules:
- Recurring transactions
- Vendor payments
- Customer receipts
- Standard amounts

## Reports

### Reconciliation Reports
- Reconciliation Summary
- Outstanding Items List
- Reconciliation History
- Audit Trail Report

### Analysis Reports
- Cleared vs Outstanding
- Aging Analysis
- Reconciliation Timeline
- Exception Report

## Best Practices

### Daily Reconciliation
- Import transactions daily
- Review and match immediately
- Investigate discrepancies quickly
- Maintain clean records

### Month-End Procedures
1. Complete all entries
2. Final statement import
3. Clear all matches
4. Document exceptions
5. Generate reports
6. Obtain approval
7. Lock the period

### Controls
- Segregate duties
- Independent review
- Timely completion
- Document exceptions
- Maintain support

## Troubleshooting

### Cannot Match Transactions
- Check date ranges
- Verify amounts
- Review references
- Check for duplicates

### Out of Balance
- Verify opening balance
- Check for unposted entries
- Review adjustments
- Confirm exchange rates

### Missing Transactions
- Refresh bank feed
- Check import mapping
- Verify date range
- Review filters

## Tips for 95% Auto-Match Rate

1. **Consistent References**: Use invoice numbers in payment references
2. **Timely Recording**: Enter transactions promptly
3. **Clean Data**: Maintain accurate vendor/customer names
4. **Rules Setup**: Configure recurring transaction rules
5. **Regular Reconciliation**: Don't let transactions accumulate

---

*Need assistance? Our support team can help achieve 95% automation. Contact support@bigledger.com*"""
    
    def generate_myinvois_guide(self) -> str:
        """Generate MyInvois setup guide"""
        return """---
title: MyInvois Setup Guide
weight: 10
---

# MyInvois Setup Guide

Complete guide for MyInvois implementation with BigLedger.

## Overview

MyInvois is Malaysia's national e-invoicing initiative by LHDN. BigLedger provides seamless integration as an MDEC-accredited PEPPOL service provider.

## Implementation Timeline

- **Phase 1** (Aug 2024): Turnover > RM 100 million
- **Phase 2** (Jan 2025): Turnover > RM 25 million  
- **Phase 3** (Jul 2025): All businesses

## Setup Process

### Step 1: LHDN Registration

1. Access MyInvois Portal
2. Register with LHDN
3. Obtain credentials:
   - Client ID
   - Client Secret
   - TIN Number
4. Generate certificates

### Step 2: BigLedger Configuration

1. Navigate to **E-Invoice** → **My E-Invoice Admin**
2. Enter LHDN credentials
3. Configure company details:
   - Legal name
   - Registration number
   - Tax identification
   - Address details
4. Test connection

### Step 3: Document Setup

Configure invoice formats:
- Standard Invoice
- Credit Note
- Debit Note
- Refund Note
- Self-billed Invoice

### Step 4: Validation Rules

Set up validation:
- Mandatory fields
- Tax calculations
- Format requirements
- Business rules

### Step 5: Testing

1. Create test invoices
2. Validate format
3. Submit to sandbox
4. Verify acceptance
5. Check status updates

## Integration Points

### With Sales Module
- Auto-generate e-invoices
- Real-time submission
- Status tracking

### With Accounting
- GL posting
- Tax reporting
- Reconciliation

## Go-Live Checklist

- [ ] LHDN registration complete
- [ ] Credentials configured
- [ ] Test submission successful
- [ ] Staff training done
- [ ] Backup process ready

---

*For MyInvois support, contact einvoice@bigledger.com*"""
    
    def generate_peppol_guide(self) -> str:
        """Generate PEPPOL configuration guide"""
        return """---
title: PEPPOL Configuration Guide
weight: 20
---

# PEPPOL Configuration Guide

Configure PEPPOL for international e-invoicing.

## What is PEPPOL?

Pan-European Public Procurement On-Line (PEPPOL) enables cross-border electronic document exchange.

## PEPPOL ID Setup

### Step 1: Obtain PEPPOL ID

Your PEPPOL ID format:
```
0195:MYREGISTRATIONNUMBER
```
- 0195 = Malaysia country code
- Followed by your business registration

### Step 2: Configure in BigLedger

1. Go to **E-Invoice** → **PEPPOL Settings**
2. Enter PEPPOL ID
3. Select document types:
   - Invoice
   - Credit Note
   - Order
   - Order Response
4. Configure endpoints

### Step 3: Trading Partner Setup

Add trading partners:
- Partner PEPPOL ID
- Document types
- Validation rules
- Routing preferences

## Document Standards

### UBL 2.1 Format
- XML-based standard
- Structured data
- Machine-readable
- Validated format

### Compliance Requirements
- Digital signatures
- Timestamps
- Audit trails
- Archival (7 years)

## Testing Process

1. Connect to PEPPOL test network
2. Exchange test documents
3. Validate receipts
4. Verify delivery
5. Check compliance

---

*PEPPOL support: peppol@bigledger.com*"""
    
    def generate_validation_guide(self) -> str:
        """Generate e-invoice validation guide"""
        return """---
title: E-Invoice Validation Rules
weight: 30
---

# E-Invoice Validation Rules

Comprehensive validation rules for MyInvois compliance.

## Mandatory Fields

### Invoice Header
- Invoice number (unique)
- Invoice date
- Supplier details
- Buyer details
- Currency code

### Line Items
- Description
- Quantity
- Unit price
- Tax code
- Line total

### Tax Information
- Tax type (SST/GST)
- Tax rate
- Tax amount
- Tax inclusive/exclusive

## Validation Checks

### Format Validation
- Date format: YYYY-MM-DD
- Amount format: 2 decimals
- Tax number format
- Phone number format

### Business Rules
- Invoice date <= current date
- Tax calculations accuracy
- Total amount validation
- Currency code validity

### LHDN Specific
- TIN validation
- Business registration
- SST registration
- Industry codes

## Common Errors

### Error Codes
- E001: Invalid format
- E002: Missing mandatory field
- E003: Invalid tax calculation
- E004: Duplicate invoice
- E005: Invalid supplier

### Resolution Steps
1. Identify error code
2. Check field mapping
3. Verify data source
4. Correct and resubmit
5. Monitor status

---

*Validation support: einvoice@bigledger.com*"""
    
    def generate_stock_guide(self) -> str:
        """Generate stock management guide"""
        return """---
title: Stock Management Guide
weight: 10
---

# Stock Management Guide

Complete inventory management with BigLedger.

## Stock Setup

### Item Master
1. Create item codes
2. Set descriptions
3. Define units of measure
4. Assign categories
5. Set reorder points

### Warehouse Configuration
- Location setup
- Bin management
- Zone definition
- Capacity planning

## Stock Transactions

### Goods Receipt
1. From purchase orders
2. Direct receipts
3. Customer returns
4. Production output

### Stock Issue
1. Sales orders
2. Internal consumption
3. Production input
4. Write-offs

### Stock Transfer
- Inter-warehouse
- Inter-location
- Consignment
- In-transit tracking

## Stock Valuation

### Methods Available
- FIFO
- Weighted Average
- Standard Cost
- Specific Identification

### Periodic Tasks
- Cycle counting
- Physical inventory
- Revaluation
- Obsolescence review

---

*Inventory support: support@bigledger.com*"""
    
    def generate_transfer_guide(self) -> str:
        """Generate stock transfer guide"""
        return """---
title: Stock Transfer Procedures
weight: 20
---

# Stock Transfer Procedures

Manage inventory movements between locations.

## Transfer Types

### Inter-Warehouse Transfer
Moving stock between warehouses:
1. Create transfer order
2. Pick items
3. Ship to destination
4. Receive at target
5. Update inventory

### Inter-Branch Transfer
Between company branches:
- Transfer pricing
- Tax implications
- Documentation
- Approval workflow

## Transfer Process

### Initiation
1. Create transfer request
2. Check availability
3. Get approvals
4. Generate transfer order

### Execution
1. Pick items
2. Pack and label
3. Create shipping docs
4. Update in-transit
5. Track shipment

### Completion
1. Receive goods
2. Verify quantities
3. Handle discrepancies
4. Update inventory
5. Close transfer

## Controls

### Approval Matrix
- Request approval
- Shipping approval
- Receiving approval
- Variance approval

### Documentation
- Transfer order
- Packing list
- Delivery note
- Receipt confirmation

---

*Transfer support: inventory@bigledger.com*"""
    
    def save_guides(self, guides: Dict):
        """Save generated guides to documentation"""
        
        # Create guides directory
        guides_dir = self.content_dir / "guides"
        guides_dir.mkdir(exist_ok=True)
        
        saved_files = []
        
        for category_key, category_data in guides.items():
            # Create category directory
            category_dir = guides_dir / category_key
            category_dir.mkdir(exist_ok=True)
            
            # Create index file for category
            index_content = f"""---
title: {category_data['title']}
weight: {category_data['weight']}
---

# {category_data['title']}

Comprehensive guides for {category_data['title'].lower()}.

## Available Guides
"""
            
            # Save individual guide pages
            for page in category_data['pages']:
                # Save guide file
                page_path = category_dir / page['filename']
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(page['content'])
                saved_files.append(page_path)
                
                # Add to index
                title = page['title']
                filename = page['filename'].replace('.md', '')
                index_content += f"\n- [{title}](/guides/{category_key}/{filename}/)"
            
            # Save category index
            index_path = category_dir / "_index.md"
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            saved_files.append(index_path)
        
        return saved_files
    
    def create_tutorials_section(self):
        """Create step-by-step tutorials"""
        
        tutorials = [
            {
                'filename': 'first-invoice.md',
                'content': """---
title: Creating Your First Invoice
weight: 10
---

# Creating Your First Invoice

Step-by-step guide to create and submit your first e-invoice.

## Prerequisites
- Customer created in system
- Products/services configured
- Tax settings complete
- E-invoice module activated

## Steps

### 1. Create Sales Order
Navigate to **Sales** → **Internal Sales Order**

### 2. Add Customer
Select or create customer

### 3. Add Items
Add products/services with quantities

### 4. Review Pricing
Check prices, discounts, taxes

### 5. Generate Invoice
Click **Create Invoice**

### 6. Submit to LHDN
Invoice automatically submitted

### 7. Track Status
Monitor submission status

## Video Tutorial
[Watch video walkthrough](#)

---
*Need help? Contact support@bigledger.com*"""
            },
            {
                'filename': 'month-end-closing.md',
                'content': """---
title: Month-End Closing Process
weight: 20
---

# Month-End Closing Process

Complete month-end procedures in BigLedger.

## Checklist

### Week 4 - Preparation
- [ ] Process pending transactions
- [ ] Follow up on approvals
- [ ] Collect supporting documents

### Day 1-3 - Transaction Processing
- [ ] Complete all sales invoices
- [ ] Process purchase bills
- [ ] Record cash transactions
- [ ] Post payroll journals

### Day 4-5 - Reconciliation
- [ ] Bank reconciliation
- [ ] Customer reconciliation
- [ ] Vendor reconciliation
- [ ] Inventory count

### Day 6-7 - Adjustments
- [ ] Accruals and deferrals
- [ ] Depreciation
- [ ] Provisions
- [ ] Tax calculations

### Day 8-10 - Reporting
- [ ] Generate trial balance
- [ ] Prepare financial statements
- [ ] Review variances
- [ ] Management reporting

## Best Practices
- Start early
- Follow checklist
- Document exceptions
- Get approvals

---
*Download month-end checklist template*"""
            }
        ]
        
        # Create tutorials directory
        tutorials_dir = self.content_dir / "tutorials"
        tutorials_dir.mkdir(exist_ok=True)
        
        saved_files = []
        for tutorial in tutorials:
            path = tutorials_dir / tutorial['filename']
            with open(path, 'w', encoding='utf-8') as f:
                f.write(tutorial['content'])
            saved_files.append(path)
        
        return saved_files


def main():
    """Main execution"""
    
    # Create enricher
    enricher = DocumentationEnricher()
    
    print("Creating comprehensive guides...")
    guides = enricher.create_guides_section()
    
    print("Saving guides to documentation...")
    saved_guides = enricher.save_guides(guides)
    print(f"Saved {len(saved_guides)} guide files")
    
    print("\nCreating tutorials...")
    saved_tutorials = enricher.create_tutorials_section()
    print(f"Saved {len(saved_tutorials)} tutorial files")
    
    print("\nDocumentation enrichment complete!")
    print("\nNew sections created:")
    print("- /guides/accounting-guides/")
    print("- /guides/einvoice-guides/")
    print("- /guides/inventory-guides/")
    print("- /tutorials/")
    
    return saved_guides + saved_tutorials


if __name__ == "__main__":
    main()