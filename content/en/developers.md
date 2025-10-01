---
title: Developer Platform
description: Developer Platform for BigLedger - Build integrations, custom applets, and extend the platform with our comprehensive APIs and tools.
---

## Developer Platform

Build powerful accounting and business management solutions with BigLedger's comprehensive developer platform. Whether you're integrating existing systems, building custom applets, or extending the platform, we have the tools and resources for your development needs.

---

## 🚀 Quick Start

Get started with BigLedger's APIs in minutes:

1. **Contact us** to request API access at [vincent@aimatrix.com](mailto:vincent@aimatrix.com)
2. **Receive** your API credentials and documentation
3. **Explore** the comprehensive API reference
4. **Build** your integration or custom applet

---

## Developer Resources

### 📚 API Documentation

Complete REST API reference with interactive examples and code samples in multiple languages.

Contact us for access: [vincent@aimatrix.com](mailto:vincent@aimatrix.com)

### 🔧 SDKs & Libraries

Official SDKs available for:
- JavaScript/TypeScript
- Python
- PHP
- Java
- .NET
- Go

### 🎓 Tutorials & Guides

Step-by-step tutorials for common integration scenarios:
- E-commerce integration
- Accounting data sync
- E-Invoice automation
- Custom applet development

### 🔗 Webhooks

Real-time event notifications for:
- Order creation and updates
- Invoice generation
- Inventory changes
- Payment processing

---

## What You Can Build

### Integration Projects

- **E-commerce Integrations**: Connect Shopify, WooCommerce, or custom stores
- **Payment Gateway Connections**: Integrate with Stripe, PayPal, local banks
- **Marketplace Integrations**: Sync with Amazon, Lazada, Shopee
- **ERP Synchronization**: Connect with existing business systems

### Custom Applets

- **Industry-Specific Modules**: Healthcare, construction, professional services
- **Custom Workflows**: Approval processes, specialized reporting
- **Extended Functionality**: Custom fields, calculations, business rules
- **White-Label Solutions**: Branded applets for your clients

### Automation Solutions

- **Event-Driven Workflows**: Automate business processes with webhooks
- **Bulk Data Processing**: Handle large-scale data imports and exports
- **Scheduled Operations**: Automated reports, backups, and maintenance
- **Business Rule Automation**: Complex approval workflows and notifications

---

## Developer Tools

- **Developer Console**: Manage API keys, monitor usage, view analytics
- **API Explorer**: Interactive API testing with live requests
- **Postman Collection**: Ready-to-use collection with all endpoints
- **OpenAPI Spec**: Complete OpenAPI/Swagger specification

Contact us for access: [vincent@aimatrix.com](mailto:vincent@aimatrix.com)

---

## Quick Example

Here's how easy it is to create an invoice using our TypeScript SDK:

```typescript
import { BigLedgerClient } from '@bigledger/sdk';

const client = new BigLedgerClient({
  apiKey: process.env.BIGLEDGER_API_KEY,
  companyId: process.env.BIGLEDGER_COMPANY_ID
});

// Create customer and invoice
const customer = await client.customers.create({
  name: 'Acme Corporation',
  email: 'billing@acme.com'
});

const invoice = await client.invoices.create({
  customerId: customer.id,
  items: [{
    description: 'Professional Services',
    quantity: 10,
    unitPrice: 100.00,
    taxCode: 'SST'
  }]
});

console.log(`Invoice ${invoice.invoiceNumber} created!`);
```

---

## Support & Community

- **Developer Support**: [vincent@aimatrix.com](mailto:vincent@aimatrix.com)
- **Sales Inquiries**: [fatimah@bigledger.com](mailto:fatimah@bigledger.com)
- **GitHub**: [github.com/bigledger](https://github.com/bigledger)

**Rate Limits**: 1,000 requests/hour per API key with burst support. Enterprise plans include higher limits and dedicated infrastructure.

---

## Ready to Start Building?

Contact us to get started with the BigLedger developer platform.

[Contact Developer Team](/contact)
