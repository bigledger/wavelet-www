---
description: Comprehensive validation rules for MyInvois compliance.
tags:
- user-guide
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

*Validation support: einvoice@bigledger.com*