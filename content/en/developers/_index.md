---
bookCollapseSection: true
cascade:
  type: docs
description: Welcome to the BigLedger Developer Platform.
tags:
- user-guide
title: Developer Platform
weight: 25
---

# BigLedger Developer Platform

Welcome to the BigLedger Developer Platform. Build powerful accounting and business management integrations with our comprehensive RESTful APIs.

{{< callout type="info" >}}
**All applets in BigLedger are built with Angular and can be automated via RESTful API calls.** Everything you see in the BigLedger interface can be programmatically controlled through our APIs.
{{< /callout >}}

## Quick Start

Get up and running with BigLedger APIs in minutes:

{{< steps >}}

### Get API Credentials
Create a developer account and generate your API keys from the BigLedger Developer Console.

### Make Your First API Call
```bash
curl -X GET "https://api.bigledger.com/v1/accounts" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Explore the API Reference
Browse our comprehensive API documentation with interactive examples.

### Build Your Integration
Use our SDKs and code examples to build production-ready integrations.

{{< /steps >}}

## Core API Modules

BigLedger's RESTful APIs are organized into logical modules that mirror our Angular applets:

{{< cards >}}
{{< card link="./api-reference/accounting" title="Accounting APIs" icon="chart-bar" subtitle="Complete accounting operations including accounts, journals, and financial reporting." >}}

{{< card link="./api-reference/einvoice" title="E-Invoice APIs" icon="document-text" subtitle="PEPPOL and MyInvois compliance with automated invoice submission and validation." >}}

{{< card link="./api-reference/inventory" title="Inventory APIs" icon="cube" subtitle="Stock management, transfers, adjustments, and real-time inventory tracking." >}}

{{< card link="./api-reference/sales" title="Sales & CRM APIs" icon="user-group" subtitle="Customer management, sales orders, quotes, and CRM operations." >}}

{{< card link="./api-reference/pos" title="POS APIs" icon="shopping-cart" subtitle="Point-of-sale transactions, session management, and retail operations." >}}

{{< card link="./api-reference/reports" title="Reporting APIs" icon="chart-bar" subtitle="Generate financial reports, analytics, and business intelligence data." >}}
{{< /cards >}}

## Developer Resources

{{< cards >}}
{{< card link="./getting-started" title="Getting Started" icon="play" subtitle="Complete guide to integrating with BigLedger APIs including authentication and first API calls." >}}

{{< card link="./authentication" title="Authentication" icon="key" subtitle="OAuth 2.0 flows, API key management, and security best practices." >}}

{{< card link="./sdks" title="SDKs & Libraries" icon="code" subtitle="Official SDKs for JavaScript, Python, PHP, Java, .NET, and more." >}}

{{< card link="./webhooks" title="Webhooks" icon="bell" subtitle="Real-time notifications for events like invoice creation, payment receipt, and stock changes." >}}

{{< card link="./examples" title="Code Examples" icon="document-duplicate" subtitle="Production-ready code examples and integration patterns." >}}

{{< card link="./migration" title="Migration Guides" icon="arrow-right" subtitle="Migrate from QuickBooks, Xero, Sage, and other accounting platforms." >}}
{{< /cards >}}

## What Makes BigLedger Different

### Angular-First Architecture
Since all BigLedger applets are built with Angular, you get:
- **Complete API Coverage**: Every feature in the UI has a corresponding API endpoint
- **Consistent Data Models**: Angular TypeScript interfaces ensure data consistency
- **Real-time Updates**: WebSocket connections for live data synchronization
- **Component-Based Integration**: Embed BigLedger Angular components directly in your app

### Industry-Leading Compliance
- **E-Invoice Ready**: Built-in PEPPOL and MyInvois compliance
- **Multi-Currency**: Full support for global accounting standards
- **Audit Trail**: Complete transaction history and compliance reporting
- **Security**: Enterprise-grade security with SOC 2 Type II compliance

### Accounting-Specific Features
- **Double-Entry Accounting**: Automatic journal entries and account balancing
- **Multi-Company**: Manage multiple entities from a single integration
- **Financial Reporting**: Pre-built reports for Balance Sheet, P&L, Trial Balance
- **Chart of Accounts**: Flexible account hierarchies and classification

## API Design Principles

Our APIs follow RESTful design principles with:

- **Predictable URLs**: `/api/v1/resource` and `/api/v1/resource/{id}`
- **HTTP Methods**: GET (read), POST (create), PUT (update), DELETE (remove)
- **JSON Format**: All requests and responses use JSON
- **Error Codes**: Standard HTTP status codes with detailed error messages
- **Pagination**: Cursor-based pagination for large datasets
- **Filtering**: Query parameters for searching and filtering
- **Rate Limiting**: Fair usage with 1000 requests per hour per API key

## Sample Integration

Here's a complete example of creating a sales invoice:

```typescript
// TypeScript/Angular Integration
import { BigLedgerClient } from '@bigledger/sdk';

const client = new BigLedgerClient({
  apiKey: 'your-api-key',
  baseUrl: 'https://api.bigledger.com/v1'
});

// Create a customer
const customer = await client.customers.create({
  name: 'Acme Corporation',
  email: 'billing@acme.com',
  address: {
    street: '123 Main St',
    city: 'Kuala Lumpur',
    country: 'MY'
  }
});

// Create an invoice
const invoice = await client.invoices.create({
  customerId: customer.id,
  invoiceDate: new Date(),
  dueDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000), // 30 days
  items: [
    {
      description: 'Professional Services',
      quantity: 10,
      unitPrice: 100.00,
      taxCode: 'SST'
    }
  ],
  notes: 'Thank you for your business!'
});

// Submit for e-invoice compliance
const einvoice = await client.einvoice.submit({
  invoiceId: invoice.id,
  format: 'PEPPOL_UBL'
});

console.log(`Invoice ${invoice.number} created and submitted as e-invoice`);
```

## Rate Limits & Quotas

{{< callout type="warning" >}}
**Default Rate Limits**
- 1000 requests per hour per API key
- 10 requests per second burst limit
- Bulk operations have separate limits

Enterprise plans include higher limits and dedicated infrastructure.
{{< /callout >}}

## Support & Community

- **Developer Support**: [developers@bigledger.com](mailto:developers@bigledger.com)
- **Community Forum**: [community.bigledger.com](https://community.bigledger.com)
- **Status Page**: [status.bigledger.com](https://status.bigledger.com)
- **GitHub**: [github.com/bigledger](https://github.com/bigledger)

## Ready to Get Started?

{{< cards >}}
{{< card link="./getting-started" title="Start Building" icon="play" subtitle="Follow our quickstart guide to make your first API call in under 5 minutes." >}}

{{< card link="./api-reference" title="API Reference" icon="book-open" subtitle="Explore the complete API documentation with interactive examples." >}}

{{< card link="https://developers.bigledger.com/console" title="Developer Console" icon="cog" subtitle="Manage your API keys, view usage analytics, and test API endpoints." >}}
{{< /cards >}}