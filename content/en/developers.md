---
title: Developer Platform
description: Developer Platform for BigLedger - Build integrations, custom applets, and extend the platform with our comprehensive APIs and tools.
---

## Developer Platform

Build powerful accounting and business management solutions with BigLedger's comprehensive developer platform. Whether you're integrating existing systems, building custom applets, or extending the platform, we have the tools and resources for your development needs.

---

## 🚀 Quick Start

Get started with BigLedger's APIs in minutes:

1. **Sign up** for a developer account at [developers.bigledger.com](https://developers.bigledger.com)
2. **Generate** your API credentials from the Developer Console
3. **Explore** our comprehensive API documentation
4. **Build** your integration or custom applet

---

## Developer Resources

### 📚 API Documentation

Complete REST API reference with interactive examples and code samples in multiple languages.

[View API Documentation →](https://developers.bigledger.com/api)

### 🔧 SDKs & Libraries

Official SDKs available for:
- JavaScript/TypeScript
- Python
- PHP
- Java
- .NET
- Go

[Browse SDKs →](https://developers.bigledger.com/sdks)

### 🎓 Tutorials & Guides

Step-by-step tutorials for common integration scenarios:
- E-commerce integration
- Accounting data sync
- E-Invoice automation
- Custom applet development

[View Tutorials →](https://developers.bigledger.com/tutorials)

### 🔗 Webhooks

Real-time event notifications for:
- Order creation and updates
- Invoice generation
- Inventory changes
- Payment processing

[Webhook Documentation →](https://developers.bigledger.com/webhooks)

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

[Access Developer Tools →](https://developers.bigledger.com/console)

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

- **Developer Support**: [developers@bigledger.com](mailto:developers@bigledger.com)
- **Community Forum**: [community.bigledger.com](https://community.bigledger.com)
- **Status Page**: [status.bigledger.com](https://status.bigledger.com)
- **GitHub**: [github.com/bigledger](https://github.com/bigledger)

**Rate Limits**: 1,000 requests/hour per API key with burst support. Enterprise plans include higher limits and dedicated infrastructure.

---

## Ready to Start Building?

Join thousands of developers building on the BigLedger platform.

[Get Started →](https://developers.bigledger.com) | [View Documentation →](https://developers.bigledger.com/docs)
