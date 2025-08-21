---
description: Complete guide for setting up your Chart of Accounts in BigLedger.
tags:
- user-guide
title: Chart of Accounts Setup Guide
weight: 10
---

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

*For additional support, contact support@bigledger.com*