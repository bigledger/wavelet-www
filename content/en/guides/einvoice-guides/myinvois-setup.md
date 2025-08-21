---
description: Complete guide for MyInvois implementation with BigLedger.
tags:
- user-guide
title: MyInvois Setup Guide
weight: 10
---

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

*For MyInvois support, contact einvoice@bigledger.com*