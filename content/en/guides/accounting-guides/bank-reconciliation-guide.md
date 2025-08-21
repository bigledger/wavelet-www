---
description: Master the bank reconciliation process with BigLedger's AI-powered matching.
tags:
- user-guide
title: Bank Reconciliation Step-by-Step
weight: 40
---

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

*Need assistance? Our support team can help achieve 95% automation. Contact support@bigledger.com*