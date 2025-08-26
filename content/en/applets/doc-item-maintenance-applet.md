---
title: "Document Item Maintenance Applet"
description: "Manage document-based items, services, and non-inventory items in BigLedger"
tags:
- core-module
- item-management
- services
- master-data
- document-items
weight: 3
---

## Purpose and Overview

The Document Item Maintenance Applet is a crucial Core Module component that manages all non-physical items in BigLedger. This includes services, consulting fees, digital products, licenses, subscriptions, and any other document-based or non-inventory items that your business sells or purchases.

{{< callout type="info" >}}
**Core Module Applet**: This is one of the 13 essential Core Module applets, particularly important for service-based businesses and companies that sell both products and services.
{{< /callout >}}

### Primary Functions
- **Service Item Management** - Professional services, consulting, labor
- **Digital Product Management** - Software, licenses, subscriptions
- **Document Templates** - Standardized service descriptions
- **Billing Item Configuration** - Non-inventory billing items
- **Service Pricing** - Flexible pricing models for services

## Key Features

### Document Item Types
- **Professional Services** - Consulting, legal, accounting services
- **Labor Services** - Installation, maintenance, repair services
- **Digital Products** - Software licenses, digital downloads
- **Subscriptions** - Recurring service agreements
- **Fees and Charges** - Processing fees, service charges
- **Miscellaneous Items** - Other non-inventory items

### Item Configuration
- Detailed item descriptions and specifications
- Service category classification
- Units of measure (hours, days, licenses, etc.)
- Tax category assignment
- Account mapping for revenue/expense
- Pricing structure configuration

### Service Specifications
- Service delivery parameters
- Skill requirements and qualifications
- Duration and time estimates
- Resource requirements
- Quality standards and SLAs
- Deliverable definitions

### Pricing Models
- **Fixed Price** - Flat rate for service
- **Time-based** - Hourly, daily, weekly rates
- **Tiered Pricing** - Volume-based pricing
- **Subscription** - Recurring billing models
- **Custom Pricing** - Project-specific pricing

### Document Integration
- Service contract templates
- Statement of work (SOW) generation
- Service level agreement (SLA) templates
- Invoice line item descriptions
- Proposal and quote templates

## Technical Specifications

### System Requirements
- **Minimum Access Level**: Item Administrator
- **Database Dependencies**: Item master tables
- **Integration Points**: Sales, purchasing, financial modules
- **API Availability**: Full CRUD operations
- **Template Engine**: Document generation capabilities

### Item Configuration Options
- **Item Code Length**: 3-50 characters
- **Description Length**: Up to 2,000 characters
- **Category Levels**: Up to 5 hierarchy levels
- **Custom Fields**: Up to 15 custom fields
- **Attachment Support**: Multiple file types

### Performance Parameters
- **Item Capacity**: Up to 50,000 document items
- **Search Performance**: <2 seconds for complex queries
- **Template Generation**: <5 seconds for standard templates
- **Concurrent Users**: 200+ simultaneous users
- **Bulk Operations**: Process 1,000+ items per batch

## Integration Points

### Core Module Dependencies
- **Tax Configuration Applet** - Service tax mapping
- **Chart of Account Applet** - Revenue/expense accounts
- **Customer Maintenance Applet** - Service delivery setup
- **Supplier Maintenance Applet** - Service procurement

### Module Integration
| Module | Integration Purpose |
|--------|-------------------|
| **Sales & CRM** | Service quotations and sales orders |
| **Project Management** | Project-based service delivery |
| **Financial Accounting** | Service revenue and expense tracking |
| **HR & Payroll** | Resource allocation and costing |
| **Time Tracking** | Service time recording |
| **Purchasing** | Service procurement and subcontracting |

### External Integrations
- **Professional Services Platforms** - Service marketplaces
- **Time Tracking Systems** - External time capture
- **Document Management** - Template repositories
- **CRM Systems** - Customer service history
- **Accounting Software** - Service revenue integration

## Configuration Requirements

### Initial Setup Requirements
1. **Service Categories** - Define service classifications
2. **Units of Measure** - Set up service units (hours, days, etc.)
3. **Account Mapping** - Link to chart of accounts
4. **Tax Configuration** - Assign appropriate tax codes
5. **Pricing Structure** - Define pricing methodologies

### Essential Configurations
- **Standard Services**: Common services offered
- **Service Packages**: Bundled service offerings
- **Resource Requirements**: Skills and equipment needed
- **Delivery Methods**: How services are delivered
- **Quality Standards**: Service level expectations

### Advanced Configurations
- **Contract Templates** - Standardized service agreements
- **SLA Definitions** - Service level agreements
- **Milestone Tracking** - Project milestone management
- **Resource Planning** - Capacity and scheduling
- **Performance Metrics** - Service KPI tracking

## Use Cases

### Professional Services Firm
**Scenario**: Legal or consulting firm
- Legal consultation services
- Document review and preparation
- Court representation fees
- Retainer and hourly billing
- Specialized legal research services

**Benefits**: Comprehensive professional service management

### IT Services Company
**Scenario**: Technology services provider
- Software implementation services
- System maintenance contracts
- Training and consultation
- Software licenses and subscriptions
- Technical support services

**Benefits**: Complete IT service portfolio management

### Healthcare Practice
**Scenario**: Medical clinic or dental practice
- Consultation and examination services
- Specialized procedures and treatments
- Diagnostic services
- Wellness programs
- Medical report preparation

**Benefits**: Comprehensive healthcare service tracking

### Educational Institution
**Scenario**: Training center or university
- Course and program offerings
- Certification services
- Online learning subscriptions
- Educational consulting
- Assessment and testing services

**Benefits**: Complete educational service management

## Related Applets

### Core Module Applets
- **[Inventory Item Maintenance Applet](/applets/inv-item-maintenance-applet/)** - Physical inventory items
- **[Tax Configuration Applet](/applets/tax-configuration-applet/)** - Service tax setup
- **[Customer Maintenance Applet](/applets/customer-maintenance-applet/)** - Service customers

### Service-Related Applets
- **[Time Tracking Applet](/applets/time-tracking-applet/)** - Service time recording
- **[Project Management Applet](/applets/project-management-applet/)** - Project-based services
- **[Resource Planning Applet](/applets/resource-planning-applet/)** - Service resource management

### Financial Applets
- **[Pricing Management Applet](/applets/pricing-management-applet/)** - Service pricing
- **[Invoice Generation Applet](/applets/invoice-generation-applet/)** - Service billing
- **[Revenue Recognition Applet](/applets/revenue-recognition-applet/)** - Service revenue

## Setup Guide

### Quick Start
1. **Access Document Item Maintenance** - Navigate to the applet
2. **Define Service Categories** - Set up service classifications
3. **Create Standard Services** - Add common services
4. **Configure Pricing** - Set up pricing models
5. **Test Service Creation** - Create sample service items

### Advanced Setup
1. **Template Configuration** - Set up service templates
2. **Integration Setup** - Connect with other modules
3. **Workflow Configuration** - Set up approval processes
4. **Reporting Setup** - Configure service reports
5. **Performance Optimization** - Optimize for high volume

## Service Item Templates

### Consulting Services Template
```yaml
Item Code: CONS-001
Description: Management Consulting Services
Category: Professional Services
Unit of Measure: Hours
Default Rate: $150/hour
Tax Category: Professional Services Tax
Account: 4100 - Professional Service Revenue
Skills Required: 
  - Business Analysis
  - Project Management
Deliverables:
  - Analysis Report
  - Recommendations Document
```

### Software Services Template
```yaml
Item Code: SOFT-001
Description: Software Implementation Service
Category: IT Services
Unit of Measure: Project
Default Rate: $5,000/project
Tax Category: IT Services Tax
Account: 4200 - IT Service Revenue
Duration: 30 days
Resources Required:
  - Software Developer
  - Project Manager
Deliverables:
  - Implemented System
  - User Training
  - Documentation
```

## Best Practices

### Item Management Best Practices
- **Standardization** - Use consistent naming conventions
- **Classification** - Proper service categorization
- **Documentation** - Detailed service descriptions
- **Regular Updates** - Keep service information current
- **Version Control** - Track service definition changes

### Pricing Best Practices
- **Market Research** - Competitive pricing analysis
- **Cost Analysis** - Understand service delivery costs
- **Value Pricing** - Price based on customer value
- **Regular Review** - Periodic pricing adjustments
- **Profitability Analysis** - Monitor service profitability

### Service Delivery Best Practices
- **Clear Specifications** - Well-defined service scope
- **Quality Standards** - Consistent service quality
- **Resource Planning** - Adequate resource allocation
- **Performance Monitoring** - Track service metrics
- **Customer Feedback** - Regular quality assessment

## Troubleshooting

### Common Issues
**Cannot create service items**
- Check user permissions for item creation
- Verify required fields are completed
- Ensure service categories are defined
- Check account mapping configuration

**Pricing issues in quotes/invoices**
- Verify pricing model configuration
- Check customer-specific pricing rules
- Ensure tax calculations are correct
- Review discount and markup settings

**Service delivery problems**
- Check resource availability
- Verify skill requirements
- Review delivery timeline settings
- Confirm quality standards

### Support Resources
- Service item setup guide
- Pricing configuration documentation
- Integration troubleshooting guide
- Best practices documentation

{{< callout type="tip" >}}
**Pro Tip**: Document items should be as detailed as inventory items. Clear descriptions and specifications prevent billing disputes and ensure consistent service delivery.
{{< /callout >}}