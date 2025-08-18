---
description: Master manual and automated journal entries in BigLedger.
tags:
- user-guide
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

*Need help? Visit our [Support Center](/user-guide/) or contact support@bigledger.com*