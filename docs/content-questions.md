# Content Questions for BigLedger Documentation

## Priority 1: Core Module Questions

### Financial Accounting Module
1. **Unique Features**: What makes BigLedger's accounting module different from competitors like SAP or Oracle?
2. **Malaysian Compliance**: Which specific Malaysian accounting standards (MFRS/MPERS) are built-in?
3. **Integration**: How does it integrate with Malaysian banks for auto-reconciliation?
4. **Reporting**: What standard Malaysian financial reports are available (e.g., Form 9, Form 24, Form 49)?
5. **Multi-currency**: How does it handle MYR and foreign currency transactions?
6. **Tax Integration**: How does it connect with LHDN's e-Invoice system?

### Inventory Module
1. **Warehouse Management**: Does it support multi-location warehouses?
2. **Barcode/RFID**: What scanning technologies are supported?
3. **Stock Valuation**: Which methods are available (FIFO, LIFO, Weighted Average)?
4. **Reorder Points**: How does automatic reordering work?
5. **Batch/Serial Tracking**: How detailed is the tracking capability?
6. **Integration**: How does it sync with e-commerce platforms?

### CRM Module
1. **Lead Management**: What's the lead scoring mechanism?
2. **Customer Segmentation**: What criteria can be used for segmentation?
3. **Communication**: Which channels are integrated (email, SMS, WhatsApp)?
4. **Pipeline Management**: How customizable is the sales pipeline?
5. **Analytics**: What CRM metrics and KPIs are tracked?
6. **Mobile Access**: Is there a mobile app for sales teams?

### POS Module
1. **Hardware Support**: Which POS hardware is compatible?
2. **Offline Mode**: Can it work without internet connection?
3. **Payment Methods**: Which Malaysian payment gateways are integrated?
4. **Loyalty Programs**: How do customer loyalty features work?
5. **Multi-outlet**: How does it handle chain stores?
6. **Integration**: How does it sync with inventory and accounting?

## Priority 2: Platform Features

### Applet Ecosystem
1. **Development**: Can third parties develop applets?
2. **Marketplace**: How does the applet approval process work?
3. **Pricing**: What's the revenue sharing model for applet developers?
4. **Security**: How are applets sandboxed for security?
5. **Updates**: How are applet updates managed?
6. **Popular Applets**: What are the top 10 most-used applets?

### E-Invoice & PEPPOL
1. **LHDN Integration**: What's the exact integration method with MyInvois?
2. **Validation**: What validation rules are enforced?
3. **Bulk Processing**: How many invoices can be processed per batch?
4. **Error Handling**: How are rejected invoices handled?
5. **PEPPOL Network**: Which countries can we invoice directly?
6. **Compliance Timeline**: What's the roadmap for full compliance?

### AI Intelligence
1. **OCR Capabilities**: What document types can be auto-processed?
2. **Accuracy Rates**: What's the accuracy for invoice data extraction?
3. **Language Support**: Which languages are supported for NLP?
4. **Predictive Analytics**: What predictions are available (sales, inventory, cash flow)?
5. **Custom Models**: Can businesses train custom AI models?
6. **Data Privacy**: How is sensitive data handled in AI processing?

## Priority 3: Industry Solutions

### Automotive Workshop
1. **Job Cards**: How detailed is the job card system?
2. **Parts Catalog**: Is there integration with parts suppliers?
3. **Service History**: How is vehicle service history tracked?
4. **Warranty Management**: How are warranties handled?
5. **Insurance Claims**: Is there insurance company integration?
6. **Appointment System**: How does appointment scheduling work?

### F&B Industry
1. **Recipe Management**: Can it handle recipe costing?
2. **Table Management**: How does table/reservation management work?
3. **Kitchen Display**: Is there a kitchen display system?
4. **Food Delivery**: Which delivery platforms are integrated?
5. **Wastage Tracking**: How is food wastage monitored?
6. **Franchise Support**: Can it handle franchise operations?

### Manufacturing
1. **BOM Management**: How complex can Bill of Materials be?
2. **Production Planning**: What planning methods are available?
3. **Quality Control**: How is QC integrated into production?
4. **Machine Integration**: Can it connect to IoT/machines?
5. **Costing**: How is production costing calculated?
6. **MRP**: Is there Material Requirements Planning?

## Priority 4: Technical Details

### API & Integration
1. **API Rate Limits**: What are the API call limits?
2. **Webhooks**: Which events trigger webhooks?
3. **Data Format**: What data formats are supported (JSON, XML, CSV)?
4. **Authentication**: What authentication methods are available?
5. **SDKs**: Which programming languages have SDKs?
6. **Postman Collection**: Is there a Postman collection available?

### Security & Compliance
1. **Data Encryption**: What encryption standards are used?
2. **Audit Trail**: How detailed is the audit logging?
3. **PDPA Compliance**: How does it ensure PDPA compliance?
4. **Backup & Recovery**: What's the backup frequency and RTO/RPO?
5. **Access Control**: How granular is role-based access?
6. **ISO Certifications**: Which ISO standards are certified?

### Performance & Scalability
1. **User Limits**: How many concurrent users are supported?
2. **Transaction Volume**: What's the maximum transactions/day?
3. **Response Time**: What are the SLA response times?
4. **Database Size**: What's the maximum database size supported?
5. **Cloud Infrastructure**: Which cloud providers are used?
6. **CDN**: Is there CDN for global access?

## Priority 5: Business Information

### Pricing & Licensing
1. **Pricing Models**: What pricing tiers are available?
2. **User-based vs Module-based**: How is pricing structured?
3. **Implementation Costs**: What are typical implementation costs?
4. **Training Costs**: What training packages are available?
5. **Support Plans**: What support levels are offered?
6. **Upgrade Path**: How do customers upgrade plans?

### Success Stories
1. **Case Studies**: Can you provide 5 detailed case studies?
2. **ROI Metrics**: What ROI do customers typically see?
3. **Implementation Time**: What's the average implementation time?
4. **Customer Testimonials**: Can you provide customer quotes?
5. **Industry Adoption**: What's the market share in Malaysia?
6. **Awards/Recognition**: What awards has BigLedger won?

### Competitive Advantages
1. **vs SAP**: What are key advantages over SAP?
2. **vs SQL Accounting**: How does it compare to SQL Accounting?
3. **vs Autocount**: What differentiates from Autocount?
4. **vs QuickBooks**: How does it compare to QuickBooks?
5. **Unique Features**: What features are unique to BigLedger?
6. **Malaysian Market Fit**: Why is it better for Malaysian businesses?

## Information Needed Format

For each question, please provide:
1. **Short Answer**: 1-2 sentences
2. **Detailed Explanation**: 1-2 paragraphs
3. **Example/Screenshot**: If applicable
4. **Related Features**: Links to related functionality
5. **Business Impact**: How this helps businesses

## How to Answer

Please create separate files in the `todos/answers/` folder:
- `financial-accounting-answers.md`
- `inventory-answers.md`
- `crm-answers.md`
- `pos-answers.md`
- `platform-features-answers.md`
- `industry-solutions-answers.md`
- `technical-details-answers.md`
- `business-information-answers.md`

Each answer should follow this format:
```markdown
## Q1: [Question]
**Short Answer**: [1-2 sentences]

**Detailed Explanation**: 
[1-2 paragraphs]

**Example**: 
[Screenshot or code example if applicable]

**Related Features**: 
- [Feature 1]
- [Feature 2]

**Business Impact**: 
[How this helps businesses]
```