---
title: "Chart of Accounts Applet"
description: "Define and manage the complete chart of accounts structure for BigLedger"
tags:
- core-module
- financial-accounting
- chart-of-accounts
- master-data
weight: 185
---

## Purpose and Overview

The Chart of Accounts Applet is the financial foundation of BigLedger, providing comprehensive management of your organization's complete chart of accounts structure. This Core Module applet defines account categories, hierarchies, and financial statement mapping that supports all financial transactions across every BigLedger module.

{{< callout type="info" >}}
**Core Module Applet**: This is one of the 13 essential Core Module applets required by all other BigLedger modules, particularly critical for any financial operations.
{{< /callout >}}

### Primary Functions
- **Account Structure Management** - Create and maintain account hierarchies
- **Financial Statement Mapping** - Map accounts to financial reports
- **Multi-Currency Support** - Handle multiple currencies and exchange rates
- **Account Classification** - Categorize accounts by type and purpose
- **Integration Foundation** - Provide account data to all financial modules

## Key Features

### Account Structure
- Hierarchical account organization (up to 10 levels)
- Flexible account numbering systems
- Account categories and sub-categories
- Parent-child account relationships
- Account status management (Active/Inactive)

### Account Types
- **Assets** - Current and non-current assets
- **Liabilities** - Short-term and long-term liabilities
- **Equity** - Owner's equity and retained earnings
- **Income** - Revenue and other income accounts
- **Expenses** - Operating and non-operating expenses

### Financial Statement Integration
- Balance Sheet mapping
- Profit & Loss statement mapping
- Cash Flow statement mapping
- Custom financial report mapping
- Multi-period comparative reporting

### Multi-Currency Capabilities
- Base currency configuration
- Foreign currency account setup
- Real-time exchange rate integration
- Currency translation rules
- Multi-currency reporting

### Account Controls
- Account-level permissions
- Transaction posting controls
- Budget assignment capabilities
- Cost center allocation
- Department-wise account access

## Technical Specifications

### System Requirements
- **Minimum Access Level**: Financial Administrator
- **Database Dependencies**: Core financial tables
- **Integration Points**: All financial modules
- **API Availability**: Full CRUD operations
- **Real-time Updates**: Immediate account balance updates

### Account Configuration Options
- **Account Code Length**: 3-20 characters
- **Hierarchy Levels**: Up to 10 levels deep
- **Account Types**: 50+ predefined types
- **Currency Support**: 150+ global currencies
- **Custom Fields**: Up to 20 custom fields per account

### Performance Parameters
- **Account Capacity**: Up to 100,000 accounts
- **Transaction Volume**: Millions of transactions per account
- **Report Generation**: <5 seconds for standard reports
- **Real-time Updates**: <1 second for balance updates
- **Concurrent Users**: 500+ simultaneous users

## Integration Points

### Core Module Dependencies
- **Organization Applet** - Company and branch structure
- **Tax Configuration Applet** - Tax account mapping
- **Cashbook Applet** - Cash and bank account integration

### Module Integration
| Module | Integration Purpose |
|--------|-------------------|
| **Financial Accounting** | Primary account data source |
| **Sales & CRM** | Revenue and receivable accounts |
| **Purchasing** | Expense and payable accounts |
| **Inventory** | Asset and cost accounts |
| **Payroll** | Salary and benefit accounts |
| **POS** | Sales and cash accounts |
| **E-Commerce** | Online revenue accounts |
| **Manufacturing** | Work-in-progress and cost accounts |

### External Integrations
- **Banking Systems** - Bank account reconciliation
- **Tax Authorities** - Statutory reporting accounts
- **Auditing Software** - Financial statement export
- **Business Intelligence** - Financial analytics
- **Third-party Accounting** - Account synchronization

## Configuration Requirements

### Initial Setup Requirements
1. **Base Currency** - Define primary currency
2. **Account Categories** - Set up major account types
3. **Numbering System** - Define account coding structure
4. **Financial Periods** - Configure accounting periods
5. **Opening Balances** - Enter starting account balances

### Essential Configurations
- **Asset Accounts**: Cash, Bank, Inventory, Fixed Assets
- **Liability Accounts**: Accounts Payable, Loans, Accruals
- **Equity Accounts**: Capital, Retained Earnings
- **Revenue Accounts**: Sales, Service Income, Other Income
- **Expense Accounts**: Cost of Sales, Operating Expenses

### Advanced Configurations
- **Consolidated Accounts** - Multi-entity consolidation
- **Segment Reporting** - Division/department accounts
- **Project Accounting** - Project-specific accounts
- **Multi-Currency** - Foreign currency accounts
- **Budgeting Integration** - Budget account mapping

## Use Cases

### Small Business Setup
**Scenario**: Local retail shop
- Simple 4-digit account structure (1000-9999)
- Basic account categories (Assets, Liabilities, Income, Expenses)
- Single currency operation
- Standard financial reports

**Benefits**: Simple, easy-to-understand financial structure

### Multi-Branch Enterprise
**Scenario**: Chain of retail stores
- Complex hierarchical structure with branch codes
- Department-wise account allocation
- Inter-branch transaction accounts
- Consolidated and branch-wise reporting

**Benefits**: Comprehensive multi-location financial management

### Manufacturing Company
**Scenario**: Production and assembly operations
- Work-in-progress accounts
- Raw material and finished goods accounts
- Manufacturing overhead allocation
- Cost center-based reporting

**Benefits**: Detailed manufacturing cost tracking

### International Business
**Scenario**: Multi-country operations
- Multi-currency account setup
- Foreign exchange accounts
- Country-specific chart of accounts
- Consolidated multi-currency reporting

**Benefits**: Global financial management with local compliance

## Related Applets

### Core Module Applets
- **[Tax Configuration Applet](/applets/tax-configuration-applet/)** - Tax account mapping
- **[Cashbook Applet](/applets/cashbook-applet/)** - Cash and bank accounts
- **[Organization Applet](/applets/organization-applet/)** - Company structure

### Financial Applets
- **[General Ledger Applet](/applets/general-ledger-applet/)** - Transaction posting
- **[Financial Reports Applet](/applets/financial-reports-applet/)** - Report generation
- **[Budget Management Applet](/applets/budget-management-applet/)** - Budget allocation

### Master Data Applets
- **[Customer Maintenance Applet](/applets/customer-maintenance-applet/)** - Customer accounts
- **[Supplier Maintenance Applet](/applets/supplier-maintenance-applet/)** - Vendor accounts

## Setup Guide

### Quick Start
1. **Access Chart of Accounts** - Navigate to the applet
2. **Define Account Structure** - Set up account numbering
3. **Create Main Categories** - Add major account types
4. **Set up Sub-Accounts** - Create detailed account hierarchy
5. **Configure Opening Balances** - Enter starting balances

### Advanced Setup
1. **Multi-Currency Configuration** - Set up foreign currencies
2. **Financial Statement Mapping** - Map accounts to reports
3. **Budget Integration** - Link accounts to budget system
4. **Cost Center Setup** - Configure departmental accounts
5. **Approval Workflows** - Set up account change approvals

## Standard Chart of Accounts Templates

### Retail Business Template
```
1000-1999: ASSETS
  1000-1099: Current Assets
    1001: Cash on Hand
    1002: Cash at Bank
    1010: Accounts Receivable
    1020: Inventory
  1100-1999: Non-Current Assets
    1101: Equipment
    1102: Accumulated Depreciation

2000-2999: LIABILITIES
  2000-2099: Current Liabilities
    2001: Accounts Payable
    2010: Accrued Expenses
  2100-2999: Non-Current Liabilities
    2101: Long-term Loans

3000-3999: EQUITY
  3001: Owner's Capital
  3002: Retained Earnings

4000-4999: INCOME
  4001: Sales Revenue
  4002: Service Income

5000-5999: EXPENSES
  5001: Cost of Sales
  5002: Salaries & Wages
  5003: Rent Expense
```

## Best Practices

### Account Structure Best Practices
- **Consistent Numbering** - Use logical, consistent account codes
- **Future Growth** - Leave gaps for future accounts
- **Clear Naming** - Use descriptive account names
- **Regular Review** - Periodic chart of accounts cleanup
- **Documentation** - Maintain account usage guidelines

### Security Best Practices
- **Access Control** - Limit chart of accounts modification rights
- **Change Approval** - Implement approval workflows for changes
- **Audit Trail** - Monitor all account changes
- **Backup** - Regular backup of chart of accounts structure
- **Testing** - Test changes in development environment

## Troubleshooting

### Common Issues
**Cannot create transactions**
- Verify account is active
- Check account posting permissions
- Ensure account type allows transactions
- Verify account balance controls

**Incorrect financial reports**
- Review account mapping to financial statements
- Check account classifications
- Verify account hierarchies
- Confirm period-end procedures

**Multi-currency issues**
- Check exchange rate configuration
- Verify currency account setup
- Review currency translation rules
- Confirm base currency settings

### Support Resources
- Chart of accounts setup guide
- Financial reporting configuration
- Multi-currency setup documentation
- Integration troubleshooting guide

{{< callout type="warning" >}}
**Important**: Changes to the Chart of Accounts can significantly impact financial reporting and system integrations. Always test changes thoroughly before implementing in production.
{{< /callout >}}