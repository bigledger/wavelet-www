---
bookCollapseSection: true
cascade:
  type: docs
description: Complete reference documentation for all BigLedger APIs.
tags:
- user-guide
title: API Reference
weight: 20
---

# BigLedger API Reference

Complete reference documentation for all BigLedger APIs. Since all applets are built with Angular, every feature in the BigLedger interface has a corresponding API endpoint.

## Base URL

All API requests should be made to:

```
https://api.bigledger.com/v1
```

## Authentication

All API requests require authentication via API key in the Authorization header:

```http
Authorization: Bearer YOUR_API_KEY
```

## Common Headers

Include these headers in all requests:

```http
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
X-Company-Id: your-company-id
```

## Core API Modules

### Accounting APIs
Complete accounting operations including chart of accounts, journal entries, and financial reporting.

- **[Accounts API](./accounting#accounts)** - Manage chart of accounts
- **[Journal Entries API](./accounting#journals)** - Create and manage journal entries  
- **[Financial Reports API](./accounting#reports)** - Generate balance sheets, P&L, trial balance

### E-Invoice APIs
PEPPOL and MyInvois compliance with automated validation and submission.

- **[E-Invoice Creation API](./einvoice#create)** - Create compliant e-invoices
- **[Validation API](./einvoice#validate)** - Validate invoice data before submission
- **[Submission API](./einvoice#submit)** - Submit to government portals
- **[Status Tracking API](./einvoice#status)** - Track submission status

### Inventory APIs
Complete inventory management including stock levels, transfers, and adjustments.

- **[Items API](./inventory#items)** - Manage inventory items
- **[Stock Levels API](./inventory#stock)** - Real-time stock tracking
- **[Transfers API](./inventory#transfers)** - Stock transfers between locations
- **[Adjustments API](./inventory#adjustments)** - Stock adjustments and corrections

### Sales & CRM APIs
Customer management, sales orders, quotes, and invoicing.

- **[Customers API](./sales#customers)** - Customer management
- **[Sales Orders API](./sales#orders)** - Create and manage sales orders
- **[Quotes API](./sales#quotes)** - Generate sales quotes
- **[Invoices API](./sales#invoices)** - Invoice creation and management

### POS APIs
Point-of-sale operations, session management, and retail transactions.

- **[Transactions API](./pos#transactions)** - Process POS transactions
- **[Sessions API](./pos#sessions)** - Manage POS sessions
- **[Reports API](./pos#reports)** - Daily sales reports

## API Design Patterns

### RESTful URLs

BigLedger APIs follow RESTful conventions:

```http
GET    /api/v1/customers           # List customers
POST   /api/v1/customers           # Create customer
GET    /api/v1/customers/{id}      # Get specific customer
PUT    /api/v1/customers/{id}      # Update customer
DELETE /api/v1/customers/{id}      # Delete customer
```

### Standard Response Format

All API responses follow this structure:

```json
{
  "success": true,
  "data": {
    // Response data here
  },
  "meta": {
    "timestamp": "2024-01-15T10:30:00Z",
    "requestId": "req_123456789"
  }
}
```

### Error Response Format

Error responses include detailed information:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid customer data",
    "details": [
      {
        "field": "email",
        "message": "Email format is invalid"
      }
    ]
  },
  "meta": {
    "timestamp": "2024-01-15T10:30:00Z",
    "requestId": "req_123456789"
  }
}
```

### Pagination

For list endpoints, use cursor-based pagination:

```http
GET /api/v1/customers?limit=20&cursor=eyJpZCI6MTIzfQ
```

Response includes pagination metadata:

```json
{
  "success": true,
  "data": [
    // Customer records
  ],
  "pagination": {
    "hasMore": true,
    "nextCursor": "eyJpZCI6MTQzfQ",
    "limit": 20,
    "total": 156
  }
}
```

### Filtering and Sorting

Use query parameters for filtering and sorting:

```http
GET /api/v1/invoices?status=draft&customerName=acme&sort=createdAt:desc
```

## Rate Limiting

API requests are rate limited by API key:

- **Default Limit**: 1000 requests per hour
- **Burst Limit**: 10 requests per second
- **Headers**: Rate limit information is included in response headers

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642248000
```

## Bulk Operations

For high-volume operations, use bulk endpoints:

```http
POST /api/v1/bulk/customers
POST /api/v1/bulk/invoices
POST /api/v1/bulk/inventory-adjustments
```

Bulk requests support up to 100 records per request.

## Webhooks

Subscribe to real-time events:

```http
POST /api/v1/webhooks/subscribe
{
  "url": "https://your-app.com/webhooks",
  "events": ["invoice.created", "payment.received", "stock.updated"]
}
```

## WebSocket API

For real-time data updates:

```javascript
const ws = new WebSocket('wss://api.bigledger.com/v1/stream');
ws.send(JSON.stringify({
  "subscribe": ["invoice.updates", "stock.changes"],
  "auth": "YOUR_API_KEY"
}));
```

## Common HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Invalid or missing API key |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 422 | Unprocessable Entity | Validation errors |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

## Testing Your Integration

### Sandbox Environment

Use the sandbox environment for testing:

```
https://api-sandbox.bigledger.com/v1
```

### Interactive API Explorer

Try our interactive API explorer at:
[https://developers.bigledger.com/api-explorer](https://developers.bigledger.com/api-explorer)

### Postman Collection

Import our Postman collection for quick testing:
[Download BigLedger Postman Collection](../../static/api/bigledger-api.postman.json)

## API Modules

{{< cards >}}
{{< card link="./authentication" title="Authentication" icon="key" subtitle="OAuth 2.0 flows, API key management, and security." >}}
{{< card link="./accounting" title="Accounting APIs" icon="chart-bar" subtitle="Accounts, journals, and financial reporting." >}}
{{< card link="./einvoice" title="E-Invoice APIs" icon="document-text" subtitle="PEPPOL and MyInvois compliance." >}}
{{< card link="./inventory" title="Inventory APIs" icon="cube" subtitle="Stock management and inventory operations." >}}

{{< card link="./sales" title="Sales & CRM APIs" icon="user-group" subtitle="Customers, orders, quotes, and invoices." >}}

{{< card link="./pos" title="POS APIs" icon="shopping-cart" subtitle="Point-of-sale and retail operations." >}}

{{< card link="./webhooks" title="Webhooks API" icon="bell" subtitle="Real-time event notifications." >}}

{{< card link="./errors" title="Error Handling" icon="warning" subtitle="Error codes and troubleshooting." >}}
{{< /cards >}}