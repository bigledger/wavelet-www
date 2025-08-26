---
description: Design and implement automated business processes with BigLedger's workflow engine, webhooks, and batch operations.
tags:
- automation
- workflows
- business-processes
- devops
title: Workflow Automation Guide
weight: 80
---

# Workflow Automation Guide

Design and implement sophisticated automated business processes using BigLedger's comprehensive automation tools. Perfect for DevOps engineers, process automation experts, and workflow designers.

{{< callout type="info" >}}
**Event-Driven Automation**: BigLedger's automation framework is built around events, webhooks, and intelligent workflow orchestration that can handle complex business logic and approval processes.
{{< /callout >}}

## Automation Overview

BigLedger provides multiple automation mechanisms:

- **Webhook-Triggered Workflows**: React to business events in real-time
- **Scheduled Operations**: Time-based automation for reports, backups, and maintenance
- **Business Rule Engine**: Automated decision making and approval workflows
- **Batch Processing**: Handle large-scale data operations efficiently
- **Integration Automation**: Sync data between BigLedger and external systems

## Event-Driven Workflows

### Setting Up Webhook-Based Automation

```javascript
// workflow-manager.js
const express = require('express');
const { WorkflowEngine } = require('@bigledger/workflow-sdk');
const { BigLedgerClient } = require('@bigledger/sdk');

class AutomationManager {
  constructor() {
    this.workflowEngine = new WorkflowEngine({
      apiKey: process.env.BIGLEDGER_API_KEY,
      companyId: process.env.BIGLEDGER_COMPANY_ID
    });
    
    this.bigledger = new BigLedgerClient({
      apiKey: process.env.BIGLEDGER_API_KEY,
      companyId: process.env.BIGLEDGER_COMPANY_ID
    });
  }

  async setupWebhookHandlers() {
    // Invoice automation workflows
    this.workflowEngine.on('invoice.created', this.handleInvoiceCreated.bind(this));
    this.workflowEngine.on('invoice.overdue', this.handleOverdueInvoice.bind(this));
    this.workflowEngine.on('payment.received', this.handlePaymentReceived.bind(this));
    
    // Inventory automation workflows
    this.workflowEngine.on('inventory.low_stock', this.handleLowStock.bind(this));
    this.workflowEngine.on('inventory.out_of_stock', this.handleOutOfStock.bind(this));
    
    // Purchase automation workflows
    this.workflowEngine.on('purchase_order.approved', this.handlePurchaseOrderApproved.bind(this));
    this.workflowEngine.on('bill.received', this.handleBillReceived.bind(this));
  }

  async handleInvoiceCreated(event) {
    const invoice = event.data.object;
    
    // Start automated invoice processing workflow
    await this.workflowEngine.startWorkflow('invoice-processing', {
      invoiceId: invoice.id,
      customerId: invoice.customerId,
      amount: invoice.total,
      priority: invoice.total > 10000 ? 'high' : 'normal'
    });
  }

  async handleOverdueInvoice(event) {
    const invoice = event.data.object;
    
    // Start automated dunning process
    await this.workflowEngine.startWorkflow('dunning-process', {
      invoiceId: invoice.id,
      customerId: invoice.customerId,
      overdueAmount: invoice.amountDue,
      overdueDays: invoice.overdueDays
    });
  }
}
```

### Complex Workflow Example: Invoice Processing

```javascript
// workflows/invoice-processing.js
class InvoiceProcessingWorkflow {
  constructor(workflowContext) {
    this.context = workflowContext;
    this.bigledger = workflowContext.bigledger;
  }

  async execute() {
    const { invoiceId, customerId, amount, priority } = this.context.input;
    
    try {
      // Step 1: Validate invoice data
      await this.validateInvoiceData(invoiceId);
      
      // Step 2: Check customer credit limit
      const creditCheck = await this.checkCustomerCredit(customerId, amount);
      
      // Step 3: Apply business rules
      const businessRules = await this.applyBusinessRules(invoiceId, creditCheck);
      
      // Step 4: Generate e-invoice if required
      if (businessRules.requiresEInvoice) {
        await this.generateEInvoice(invoiceId);
      }
      
      // Step 5: Send invoice to customer
      await this.sendInvoiceToCustomer(invoiceId, businessRules.deliveryMethod);
      
      // Step 6: Schedule follow-up actions
      await this.scheduleFollowUpActions(invoiceId, businessRules);
      
      // Step 7: Update CRM and analytics
      await this.updateCRMAndAnalytics(customerId, invoiceId);
      
      return { status: 'completed', invoiceId, actions: businessRules.actions };
      
    } catch (error) {
      // Handle errors and trigger remediation workflows
      await this.handleWorkflowError(error, invoiceId);
      throw error;
    }
  }

  async validateInvoiceData(invoiceId) {
    const invoice = await this.bigledger.invoices.get(invoiceId);
    
    const validations = [
      { field: 'items', check: (inv) => inv.items && inv.items.length > 0 },
      { field: 'customer', check: (inv) => inv.customerId },
      { field: 'total', check: (inv) => inv.total > 0 },
      { field: 'dueDate', check: (inv) => inv.dueDate }
    ];

    const errors = validations
      .filter(v => !v.check(invoice))
      .map(v => `Missing or invalid: ${v.field}`);

    if (errors.length > 0) {
      throw new ValidationError(`Invoice validation failed: ${errors.join(', ')}`);
    }
  }

  async checkCustomerCredit(customerId, amount) {
    const customer = await this.bigledger.customers.get(customerId);
    const outstandingBalance = await this.bigledger.customers.getOutstandingBalance(customerId);
    
    return {
      creditLimit: customer.creditLimit,
      currentBalance: outstandingBalance.total,
      newBalance: outstandingBalance.total + amount,
      withinLimit: (outstandingBalance.total + amount) <= customer.creditLimit,
      riskLevel: this.calculateRiskLevel(customer, outstandingBalance.total + amount)
    };
  }

  async applyBusinessRules(invoiceId, creditCheck) {
    const invoice = await this.bigledger.invoices.get(invoiceId);
    const customer = await this.bigledger.customers.get(invoice.customerId);
    
    const rules = {
      requiresEInvoice: customer.country === 'MY' && invoice.total >= 100,
      requiresApproval: creditCheck.riskLevel === 'high' || invoice.total > 50000,
      deliveryMethod: customer.preferences?.invoiceDelivery || 'email',
      paymentTerms: this.calculatePaymentTerms(customer, creditCheck),
      actions: []
    };

    // Apply conditional logic
    if (!creditCheck.withinLimit) {
      rules.requiresApproval = true;
      rules.actions.push({
        type: 'credit_limit_exceeded_notification',
        recipients: ['credit_manager@company.com'],
        data: { customerId: customer.id, exceedAmount: creditCheck.newBalance - creditCheck.creditLimit }
      });
    }

    if (invoice.total > 25000) {
      rules.actions.push({
        type: 'high_value_invoice_notification',
        recipients: ['finance_director@company.com'],
        data: { invoiceId, amount: invoice.total }
      });
    }

    return rules;
  }

  async generateEInvoice(invoiceId) {
    try {
      const einvoice = await this.bigledger.einvoice.create({
        invoiceId,
        format: 'PEPPOL_UBL',
        autoSubmit: true
      });

      // Monitor e-invoice status
      await this.context.scheduleTask('monitor-einvoice-status', {
        einvoiceId: einvoice.id,
        maxAttempts: 10,
        intervalMinutes: 5
      });

      return einvoice;
    } catch (error) {
      // Handle e-invoice generation errors
      await this.context.createTask('einvoice-manual-review', {
        invoiceId,
        error: error.message,
        assignee: 'compliance_team'
      });
      throw error;
    }
  }

  async sendInvoiceToCustomer(invoiceId, deliveryMethod) {
    const methods = {
      email: () => this.sendInvoiceByEmail(invoiceId),
      portal: () => this.publishToCustomerPortal(invoiceId),
      api: () => this.sendViaCustomerAPI(invoiceId),
      postal: () => this.schedulePostalDelivery(invoiceId)
    };

    if (methods[deliveryMethod]) {
      await methods[deliveryMethod]();
    } else {
      // Default to email
      await this.sendInvoiceByEmail(invoiceId);
    }
  }

  async scheduleFollowUpActions(invoiceId, businessRules) {
    const invoice = await this.bigledger.invoices.get(invoiceId);
    
    // Schedule payment reminder
    const reminderDate = new Date(invoice.dueDate);
    reminderDate.setDate(reminderDate.getDate() - 3); // 3 days before due
    
    await this.context.scheduleWorkflow('payment-reminder', {
      invoiceId,
      customerId: invoice.customerId
    }, reminderDate);

    // Schedule overdue follow-up
    const overdueDate = new Date(invoice.dueDate);
    overdueDate.setDate(overdueDate.getDate() + 1); // 1 day after due
    
    await this.context.scheduleWorkflow('overdue-follow-up', {
      invoiceId,
      customerId: invoice.customerId
    }, overdueDate);
  }
}
```

## Business Rule Engine

### Defining Business Rules

```javascript
// business-rules/invoice-rules.js
const { RuleEngine } = require('@bigledger/workflow-sdk');

class InvoiceBusinessRules extends RuleEngine {
  
  constructor() {
    super();
    this.defineRules();
  }

  defineRules() {
    // Rule: High-value invoice approval
    this.addRule('high-value-approval', {
      when: (facts) => facts.invoice.total > 50000,
      then: (facts, actions) => {
        actions.requireApproval({
          approvers: ['finance_director', 'ceo'],
          reason: 'High value invoice requires executive approval'
        });
      }
    });

    // Rule: New customer credit check
    this.addRule('new-customer-credit-check', {
      when: (facts) => facts.customer.isNew && facts.invoice.total > 5000,
      then: (facts, actions) => {
        actions.requireCreditCheck({
          customerId: facts.customer.id,
          requestedAmount: facts.invoice.total
        });
      }
    });

    // Rule: Multi-currency invoice validation
    this.addRule('multi-currency-validation', {
      when: (facts) => facts.invoice.currency !== facts.company.baseCurrency,
      then: (facts, actions) => {
        actions.validateExchangeRate({
          fromCurrency: facts.invoice.currency,
          toCurrency: facts.company.baseCurrency,
          amount: facts.invoice.total,
          date: facts.invoice.invoiceDate
        });
      }
    });

    // Rule: Automatic discount application
    this.addRule('volume-discount', {
      when: (facts) => facts.customer.tier === 'premium' && facts.invoice.total > 10000,
      then: (facts, actions) => {
        actions.applyDiscount({
          type: 'percentage',
          value: 5,
          reason: 'Premium customer volume discount'
        });
      }
    });

    // Rule: Tax validation
    this.addRule('tax-validation', {
      when: (facts) => facts.invoice.items.some(item => !item.taxCode),
      then: (facts, actions) => {
        actions.flagForTaxReview({
          invoiceId: facts.invoice.id,
          reason: 'Missing tax codes on line items'
        });
      }
    });
  }

  async executeRules(invoiceData) {
    const facts = await this.prepareFacts(invoiceData);
    const results = await this.run(facts);
    
    return {
      rules_applied: results.events.map(e => e.type),
      actions_required: results.events.map(e => e.params),
      approval_required: results.events.some(e => e.type === 'requireApproval'),
      warnings: results.events.filter(e => e.type.includes('warning')),
      errors: results.events.filter(e => e.type.includes('error'))
    };
  }

  async prepareFacts(invoiceData) {
    const invoice = await this.bigledger.invoices.get(invoiceData.invoiceId);
    const customer = await this.bigledger.customers.get(invoice.customerId);
    const company = await this.bigledger.company.get();
    
    return {
      invoice: {
        ...invoice,
        isNew: !invoice.invoiceNumber,
        age: Math.floor((Date.now() - new Date(invoice.createdAt)) / (1000 * 60 * 60 * 24))
      },
      customer: {
        ...customer,
        isNew: customer.createdAt > Date.now() - (30 * 24 * 60 * 60 * 1000), // 30 days
        outstandingBalance: await this.getCustomerBalance(customer.id)
      },
      company
    };
  }
}
```

## Scheduled Automation

### Automated Report Generation

```javascript
// schedulers/report-scheduler.js
const cron = require('node-cron');
const { ReportGenerator } = require('@bigledger/reporting-sdk');

class AutomatedReportScheduler {
  
  constructor() {
    this.reportGenerator = new ReportGenerator({
      apiKey: process.env.BIGLEDGER_API_KEY,
      companyId: process.env.BIGLEDGER_COMPANY_ID
    });
  }

  start() {
    // Daily reports
    cron.schedule('0 9 * * 1-5', () => {
      this.generateDailyReports();
    }, { timezone: 'Asia/Kuala_Lumpur' });

    // Weekly reports  
    cron.schedule('0 10 * * 1', () => {
      this.generateWeeklyReports();
    });

    // Monthly reports
    cron.schedule('0 9 1 * *', () => {
      this.generateMonthlyReports();
    });

    // End-of-quarter reports
    cron.schedule('0 8 1 1,4,7,10 *', () => {
      this.generateQuarterlyReports();
    });
  }

  async generateDailyReports() {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    
    const reports = [
      {
        name: 'Daily Sales Summary',
        type: 'sales_summary',
        dateRange: { from: yesterday, to: yesterday },
        recipients: ['sales@company.com', 'management@company.com']
      },
      {
        name: 'Cash Flow Report',
        type: 'cash_flow',
        dateRange: { from: yesterday, to: yesterday },
        recipients: ['finance@company.com']
      },
      {
        name: 'Outstanding Invoices',
        type: 'aged_receivables',
        asOfDate: yesterday,
        recipients: ['accounts@company.com']
      }
    ];

    for (const reportConfig of reports) {
      try {
        await this.generateAndDistributeReport(reportConfig);
      } catch (error) {
        console.error(`Failed to generate ${reportConfig.name}:`, error);
        await this.notifyReportFailure(reportConfig, error);
      }
    }
  }

  async generateWeeklyReports() {
    const lastWeek = this.getLastWeekRange();
    
    const reports = [
      {
        name: 'Weekly Financial Summary',
        type: 'financial_summary',
        dateRange: lastWeek,
        recipients: ['ceo@company.com', 'cfo@company.com'],
        format: 'pdf'
      },
      {
        name: 'Inventory Movement Report',
        type: 'inventory_movement',
        dateRange: lastWeek,
        recipients: ['warehouse@company.com', 'purchasing@company.com']
      },
      {
        name: 'Customer Payment Analysis',
        type: 'payment_analysis',
        dateRange: lastWeek,
        recipients: ['credit_control@company.com']
      }
    ];

    await this.processReportsInBatch(reports);
  }

  async generateAndDistributeReport(config) {
    // Generate the report
    const report = await this.reportGenerator.generate({
      type: config.type,
      parameters: {
        dateRange: config.dateRange,
        asOfDate: config.asOfDate,
        format: config.format || 'pdf',
        includeCharts: true,
        includeComparisons: true
      }
    });

    // Add executive summary for management reports
    if (config.recipients.some(email => email.includes('ceo') || email.includes('management'))) {
      report.executiveSummary = await this.generateExecutiveSummary(report);
    }

    // Distribute via email
    await this.distributeReport(report, config.recipients, config.name);

    // Store in document management system
    await this.archiveReport(report, config);

    // Log the generation
    console.log(`✅ Generated and distributed: ${config.name}`);
  }
}
```

### Automated Maintenance Tasks

```javascript
// maintenance/automated-maintenance.js
class AutomatedMaintenanceTasks {
  
  constructor() {
    this.bigledger = new BigLedgerClient({
      apiKey: process.env.BIGLEDGER_API_KEY,
      companyId: process.env.BIGLEDGER_COMPANY_ID
    });
  }

  startMaintenanceTasks() {
    // Daily cleanup tasks
    cron.schedule('0 2 * * *', () => {
      this.runDailyMaintenance();
    });

    // Weekly optimization tasks
    cron.schedule('0 3 * * 0', () => {
      this.runWeeklyMaintenance();
    });

    // Monthly archival tasks  
    cron.schedule('0 4 1 * *', () => {
      this.runMonthlyMaintenance();
    });
  }

  async runDailyMaintenance() {
    const tasks = [
      { name: 'Clean temporary files', fn: () => this.cleanTemporaryFiles() },
      { name: 'Update exchange rates', fn: () => this.updateExchangeRates() },
      { name: 'Process pending e-invoices', fn: () => this.processPendingEInvoices() },
      { name: 'Check system health', fn: () => this.performHealthCheck() },
      { name: 'Backup critical data', fn: () => this.backupCriticalData() }
    ];

    await this.executeMaintenance('Daily', tasks);
  }

  async runWeeklyMaintenance() {
    const tasks = [
      { name: 'Optimize database indexes', fn: () => this.optimizeDatabase() },
      { name: 'Archive old audit logs', fn: () => this.archiveAuditLogs() },
      { name: 'Update currency rates history', fn: () => this.updateCurrencyHistory() },
      { name: 'Clean up expired sessions', fn: () => this.cleanExpiredSessions() },
      { name: 'Generate performance reports', fn: () => this.generatePerformanceReports() }
    ];

    await this.executeMaintenance('Weekly', tasks);
  }

  async runMonthlyMaintenance() {
    const tasks = [
      { name: 'Archive completed transactions', fn: () => this.archiveTransactions() },
      { name: 'Update customer risk scores', fn: () => this.updateRiskScores() },
      { name: 'Cleanup old document versions', fn: () => this.cleanupDocumentVersions() },
      { name: 'Generate monthly compliance report', fn: () => this.generateComplianceReport() }
    ];

    await this.executeMaintenance('Monthly', tasks);
  }

  async executeMaintenance(type, tasks) {
    const startTime = Date.now();
    const results = [];

    console.log(`🔧 Starting ${type.toLowerCase()} maintenance tasks...`);

    for (const task of tasks) {
      const taskStart = Date.now();
      try {
        await task.fn();
        const duration = Date.now() - taskStart;
        results.push({ name: task.name, status: 'success', duration });
        console.log(`✅ ${task.name} completed in ${duration}ms`);
      } catch (error) {
        const duration = Date.now() - taskStart;
        results.push({ name: task.name, status: 'failed', duration, error: error.message });
        console.error(`❌ ${task.name} failed:`, error.message);
      }
    }

    const totalDuration = Date.now() - startTime;
    const summary = {
      type,
      totalDuration,
      tasksCompleted: results.filter(r => r.status === 'success').length,
      tasksFailed: results.filter(r => r.status === 'failed').length,
      results
    };

    // Send maintenance report
    await this.sendMaintenanceReport(summary);
    
    console.log(`🏁 ${type} maintenance completed in ${totalDuration}ms`);
  }
}
```

## Integration Automation

### Third-Party System Synchronization

```javascript
// integrations/sync-manager.js
class IntegrationSyncManager {
  
  constructor() {
    this.bigledger = new BigLedgerClient({
      apiKey: process.env.BIGLEDGER_API_KEY,
      companyId: process.env.BIGLEDGER_COMPANY_ID
    });
    
    this.integrations = {
      shopify: new ShopifyIntegration(),
      stripe: new StripeIntegration(),
      quickbooks: new QuickBooksIntegration(),
      warehouse: new WarehouseIntegration()
    };
  }

  startSyncProcesses() {
    // Real-time sync via webhooks
    this.setupWebhookSync();
    
    // Scheduled batch sync
    this.setupBatchSync();
    
    // Error recovery sync
    this.setupErrorRecovery();
  }

  setupWebhookSync() {
    // Shopify order sync
    this.bigledger.webhooks.on('sales_order.created', async (event) => {
      await this.syncOrderToShopify(event.data.object);
    });

    // Inventory sync
    this.bigledger.webhooks.on('inventory.adjustment', async (event) => {
      await this.syncInventoryToAllPlatforms(event.data.object);
    });

    // Payment sync
    this.bigledger.webhooks.on('payment.received', async (event) => {
      await this.syncPaymentToAccounting(event.data.object);
    });
  }

  setupBatchSync() {
    // Hourly customer sync
    cron.schedule('0 * * * *', () => {
      this.syncCustomersFromAllPlatforms();
    });

    // Daily product sync
    cron.schedule('0 6 * * *', () => {
      this.syncProductsToAllPlatforms();
    });

    // Daily financial sync
    cron.schedule('0 23 * * *', () => {
      this.syncFinancialDataToAccounting();
    });
  }

  async syncOrderToShopify(order) {
    try {
      const shopifyOrder = await this.transformOrderForShopify(order);
      
      // Create or update order in Shopify
      const result = await this.integrations.shopify.orders.upsert(shopifyOrder);
      
      // Update BigLedger with Shopify order ID
      await this.bigledger.salesOrders.update(order.id, {
        externalReferences: {
          shopify: result.id
        }
      });

      // Sync inventory levels
      await this.syncInventoryToShopify(order.items);
      
      console.log(`✅ Order ${order.orderNumber} synced to Shopify`);
      
    } catch (error) {
      console.error(`❌ Failed to sync order ${order.id} to Shopify:`, error);
      await this.queueRetrySync('shopify', 'order', order.id, error);
    }
  }

  async syncInventoryToAllPlatforms(inventoryItem) {
    const syncTasks = Object.entries(this.integrations).map(async ([platform, integration]) => {
      try {
        if (integration.inventory && integration.inventory.updateStock) {
          await integration.inventory.updateStock({
            sku: inventoryItem.sku,
            quantity: inventoryItem.currentStock,
            location: inventoryItem.location
          });
          
          console.log(`✅ Inventory synced to ${platform}: ${inventoryItem.sku}`);
        }
      } catch (error) {
        console.error(`❌ Failed to sync inventory to ${platform}:`, error);
        await this.queueRetrySync(platform, 'inventory', inventoryItem.id, error);
      }
    });

    await Promise.allSettled(syncTasks);
  }

  async setupErrorRecovery() {
    // Process failed sync queue every 15 minutes
    cron.schedule('*/15 * * * *', () => {
      this.processFailedSyncQueue();
    });
  }

  async processFailedSyncQueue() {
    const failedSyncs = await this.getFailedSyncs();
    
    for (const sync of failedSyncs) {
      if (sync.retryCount < 5) {
        try {
          await this.retrySyncOperation(sync);
          await this.markSyncAsSuccessful(sync.id);
          console.log(`✅ Retry successful for ${sync.platform} ${sync.type}`);
        } catch (error) {
          await this.incrementRetryCount(sync.id);
          console.error(`❌ Retry failed for ${sync.platform} ${sync.type}:`, error);
        }
      } else {
        // Mark as permanently failed and notify administrators
        await this.markSyncAsFailedPermanently(sync.id);
        await this.notifyAdministrators(sync);
      }
    }
  }
}
```

## Approval Workflows

### Multi-Stage Approval Process

```javascript
// workflows/approval-workflow.js
class ApprovalWorkflow {
  
  constructor(workflowContext) {
    this.context = workflowContext;
    this.bigledger = workflowContext.bigledger;
  }

  async execute() {
    const { entityType, entityId, approvalType, requestedBy } = this.context.input;
    
    try {
      // Get approval configuration
      const approvalConfig = await this.getApprovalConfig(entityType, approvalType);
      
      // Create approval request
      const approvalRequest = await this.createApprovalRequest({
        entityType,
        entityId,
        approvalType,
        requestedBy,
        approvers: approvalConfig.approvers,
        rules: approvalConfig.rules
      });

      // Start approval process
      return await this.processApproval(approvalRequest, approvalConfig);
      
    } catch (error) {
      await this.handleApprovalError(error);
      throw error;
    }
  }

  async getApprovalConfig(entityType, approvalType) {
    const configs = {
      'purchase_order': {
        'standard': {
          approvers: [
            { role: 'department_manager', required: true, order: 1 },
            { role: 'finance_manager', required: true, order: 2 }
          ],
          rules: {
            maxAmount: 10000,
            timeoutHours: 48
          }
        },
        'high_value': {
          approvers: [
            { role: 'department_manager', required: true, order: 1 },
            { role: 'finance_manager', required: true, order: 2 },
            { role: 'cfo', required: true, order: 3 },
            { role: 'ceo', required: false, order: 4 }
          ],
          rules: {
            minAmount: 10000,
            timeoutHours: 72
          }
        }
      },
      'expense_report': {
        'standard': {
          approvers: [
            { role: 'line_manager', required: true, order: 1 }
          ],
          rules: {
            maxAmount: 1000,
            timeoutHours: 24
          }
        },
        'high_value': {
          approvers: [
            { role: 'line_manager', required: true, order: 1 },
            { role: 'finance_manager', required: true, order: 2 }
          ],
          rules: {
            minAmount: 1000,
            timeoutHours: 48
          }
        }
      }
    };

    return configs[entityType]?.[approvalType] || configs[entityType]?.['standard'];
  }

  async processApproval(approvalRequest, config) {
    const approvers = config.approvers.sort((a, b) => a.order - b.order);
    
    for (const approver of approvers) {
      if (approver.required) {
        // Send approval notification
        await this.sendApprovalNotification(approvalRequest, approver);
        
        // Wait for approval with timeout
        const approval = await this.waitForApproval(
          approvalRequest.id, 
          approver.role, 
          config.rules.timeoutHours
        );

        if (approval.status === 'approved') {
          await this.recordApproval(approvalRequest.id, approver.role, approval);
        } else if (approval.status === 'rejected') {
          await this.recordRejection(approvalRequest.id, approver.role, approval);
          return { status: 'rejected', rejectedBy: approver.role, reason: approval.reason };
        } else {
          // Timeout occurred
          return { status: 'timeout', approver: approver.role };
        }
      }
    }

    // All required approvals received
    await this.finalizeApproval(approvalRequest.id);
    return { status: 'approved' };
  }

  async sendApprovalNotification(approvalRequest, approver) {
    const users = await this.getUsersByRole(approver.role);
    
    for (const user of users) {
      // Send email notification
      await this.sendEmail({
        to: user.email,
        subject: `Approval Required: ${approvalRequest.entityType} ${approvalRequest.entityId}`,
        template: 'approval-request',
        data: {
          approvalRequest,
          approver: user,
          approvalLink: `${process.env.APPROVAL_PORTAL_URL}/approve/${approvalRequest.id}`,
          timeoutHours: approver.timeoutHours
        }
      });

      // Send in-app notification
      await this.bigledger.notifications.create({
        userId: user.id,
        type: 'approval_request',
        title: 'Approval Required',
        message: `${approvalRequest.entityType} requires your approval`,
        data: { approvalRequestId: approvalRequest.id }
      });
    }
  }

  async waitForApproval(approvalRequestId, approverRole, timeoutHours) {
    return new Promise((resolve) => {
      const timeout = setTimeout(() => {
        resolve({ status: 'timeout' });
      }, timeoutHours * 60 * 60 * 1000);

      // Listen for approval webhook
      this.context.onWebhook(`approval.${approvalRequestId}.${approverRole}`, (event) => {
        clearTimeout(timeout);
        resolve(event.data);
      });

      // Also check periodically in case webhook fails
      const checkInterval = setInterval(async () => {
        const approval = await this.checkApprovalStatus(approvalRequestId, approverRole);
        if (approval) {
          clearTimeout(timeout);
          clearInterval(checkInterval);
          resolve(approval);
        }
      }, 5 * 60 * 1000); // Check every 5 minutes
    });
  }
}
```

## Monitoring and Analytics

### Workflow Performance Monitoring

```javascript
// monitoring/workflow-monitor.js
class WorkflowMonitor {
  
  constructor() {
    this.metrics = {
      workflowsStarted: new Counter('workflows_started_total', ['workflow_type', 'status']),
      workflowDuration: new Histogram('workflow_duration_seconds', ['workflow_type']),
      workflowErrors: new Counter('workflow_errors_total', ['workflow_type', 'error_type']),
      activeWorkflows: new Gauge('active_workflows', ['workflow_type'])
    };
  }

  startMonitoring() {
    // Monitor workflow health
    setInterval(() => {
      this.checkWorkflowHealth();
    }, 60000); // Every minute

    // Generate workflow analytics
    cron.schedule('0 * * * *', () => {
      this.generateWorkflowAnalytics();
    });

    // Alert on workflow failures
    this.setupFailureAlerts();
  }

  async trackWorkflowStart(workflowType, workflowId) {
    this.metrics.workflowsStarted.inc({ workflow_type: workflowType, status: 'started' });
    this.metrics.activeWorkflows.inc({ workflow_type: workflowType });
    
    await this.recordWorkflowEvent({
      workflowId,
      workflowType,
      event: 'started',
      timestamp: new Date(),
      metadata: {}
    });
  }

  async trackWorkflowCompletion(workflowType, workflowId, duration, status) {
    this.metrics.workflowsStarted.inc({ workflow_type: workflowType, status });
    this.metrics.workflowDuration.observe({ workflow_type: workflowType }, duration);
    this.metrics.activeWorkflows.dec({ workflow_type: workflowType });
    
    await this.recordWorkflowEvent({
      workflowId,
      workflowType,
      event: 'completed',
      status,
      duration,
      timestamp: new Date()
    });
  }

  async trackWorkflowError(workflowType, workflowId, error) {
    this.metrics.workflowErrors.inc({ 
      workflow_type: workflowType, 
      error_type: error.constructor.name 
    });
    
    await this.recordWorkflowEvent({
      workflowId,
      workflowType,
      event: 'error',
      error: {
        name: error.name,
        message: error.message,
        stack: error.stack
      },
      timestamp: new Date()
    });

    // Send alert for critical errors
    if (this.isCriticalError(error)) {
      await this.sendCriticalErrorAlert(workflowType, workflowId, error);
    }
  }

  async generateWorkflowAnalytics() {
    const analytics = {
      hourly: await this.getHourlyWorkflowStats(),
      daily: await this.getDailyWorkflowStats(),
      weekly: await this.getWeeklyWorkflowStats(),
      performance: await this.getPerformanceMetrics(),
      errors: await this.getErrorAnalytics()
    };

    // Store analytics
    await this.storeAnalytics(analytics);
    
    // Generate insights
    const insights = await this.generateInsights(analytics);
    
    // Send analytics report
    await this.sendAnalyticsReport(analytics, insights);
  }

  async generateInsights(analytics) {
    const insights = [];

    // Performance insights
    if (analytics.performance.averageDuration > analytics.performance.baseline * 1.5) {
      insights.push({
        type: 'performance_degradation',
        severity: 'warning',
        message: 'Workflow performance has degraded by 50% compared to baseline',
        recommendation: 'Investigate resource constraints and optimize bottlenecks'
      });
    }

    // Error rate insights
    if (analytics.errors.errorRate > 5) {
      insights.push({
        type: 'high_error_rate',
        severity: 'critical',
        message: `Error rate is ${analytics.errors.errorRate}%, above 5% threshold`,
        recommendation: 'Investigate common error patterns and implement fixes'
      });
    }

    // Volume insights
    const volumeChange = analytics.daily.today.volume / analytics.daily.yesterday.volume;
    if (volumeChange > 2) {
      insights.push({
        type: 'volume_spike',
        severity: 'info',
        message: `Workflow volume increased ${Math.round(volumeChange * 100)}% from yesterday`,
        recommendation: 'Monitor system resources and scaling requirements'
      });
    }

    return insights;
  }
}
```

This comprehensive automation framework enables sophisticated business process automation, from simple webhook-triggered actions to complex multi-stage approval workflows. The monitoring and analytics capabilities ensure your automations run reliably and efficiently at scale.