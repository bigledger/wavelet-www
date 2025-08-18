# Basic Business Operations: FAQ for Beginners

*Understanding how to manage fundamental business activities in BigLedger*

---

## Customer Management

**Q: How do I create my first customer?**

**A:** Creating customers in BigLedger is like setting up contacts in your phone, but with business details:

**Step-by-Step Process**:
1. **Go to Customers section** → Click "Add New Customer"
2. **Enter basic information**:
   - Customer name (required)
   - Contact person
   - Email and phone
   - Business address
3. **Set business terms**:
   - Payment terms (e.g., "Net 30 days")
   - Credit limit (if any)
   - Preferred communication method
4. **Save and you're done!**

**Pro Tips for Beginners**:
- Start with just name and email - you can add details later
- Use consistent naming (always "Company Name" or "Last, First")
- Add notes about how you met them or their preferences
- Set payment terms from day one to avoid confusion

**Common Beginner Questions**:
- *"What if I don't know their payment terms?"* → Start with your standard terms (like 30 days), you can change it later
- *"Should I add every single person I might sell to?"* → Only add real prospects or existing customers to keep your list clean
- *"What if they're both a customer and a supplier?"* → Create separate customer and vendor records - BigLedger will link them if needed

**Real Example**: Tom runs a landscaping business. His first customer entry looked like:
- Name: "Johnson Residence"
- Contact: "Mary Johnson"
- Email: mary@email.com
- Terms: "Due on completion"
- Notes: "Referred by neighbor, prefers text messages"

**Q: What's the difference between a quote and an invoice?**

**A:** Think of it like the difference between a restaurant menu (quote) and your bill (invoice):

**Quote (Estimate/Proposal)**:
- **Purpose**: "Here's what it would cost IF you buy this"
- **When to use**: Before the customer commits
- **Status**: Proposed, not final
- **Payment**: No money expected yet
- **Example**: "Your website redesign would cost $3,000"

**Invoice (Bill)**:
- **Purpose**: "You bought this, please pay me"
- **When to use**: After work is done or product delivered
- **Status**: Final, legally binding
- **Payment**: Money is due
- **Example**: "Website redesign completed, payment of $3,000 due"

**The Natural Flow**:
1. **Customer inquires** → Create a quote
2. **Customer approves** → Convert quote to sales order
3. **Work completed/shipped** → Convert to invoice
4. **Customer pays** → Record payment

**Beginner-Friendly Process**:
- Start with quotes for anything over $100
- Always get approval before starting work
- Convert approved quotes to invoices (BigLedger does this automatically)
- Track which quotes turn into sales to improve your success rate

**Q: I keep hearing about "sales orders" - what are those and do I need them?**

**A:** Sales orders are like a contract between quote and invoice. Here's when you need them:

**You DON'T need sales orders if**:
- You provide services immediately (like haircuts)
- You sell simple products on the spot
- Payment happens immediately

**You DO need sales orders if**:
- You manufacture or custom-build products
- You order special items for customers
- Work takes weeks or months to complete
- You need to track what's promised vs. what's delivered

**Simple workflow WITH sales orders**:
Quote → Customer Approves → Sales Order → Work/Delivery → Invoice → Payment

**Simple workflow WITHOUT sales orders**:
Quote → Customer Approves → Work/Delivery → Invoice → Payment

**Bottom line**: Start without sales orders. Add them later if you find you need better tracking of work in progress.

---

## Inventory and Products

**Q: How do I track my inventory?**

**A:** Think of inventory tracking like managing your pantry - you need to know what you have, what you've used, and what you need to buy:

**Setting Up Your Products** (one-time setup):
1. **Create each product/service**:
   - Product name and description
   - Cost price (what you pay)
   - Sale price (what you charge)
   - Current quantity on hand

2. **Choose tracking method**:
   - **Simple**: Just track quantities (good for most businesses)
   - **Detailed**: Track by location, lot numbers, serial numbers

**How BigLedger Tracks Automatically**:
- **When you sell something** → Inventory decreases
- **When you buy/receive stock** → Inventory increases
- **Current levels** → Always up-to-date automatically

**For Service Businesses**:
- Track time instead of physical inventory
- Set up services as "products" with hourly rates
- Track materials you use for jobs

**Beginner Tips**:
- Start simple - track main products first
- Don't worry about perfection initially
- Count your actual inventory and enter starting quantities
- Review inventory reports weekly

**Q: What happens when I sell something?**

**A:** When you make a sale, BigLedger automatically handles multiple things behind the scenes:

**What You Do** (the simple part):
1. Create an invoice for the customer
2. Add the products/services sold
3. Save the invoice

**What BigLedger Does Automatically**:
- **Inventory**: Reduces stock levels for products sold
- **Accounting**: Records the sale in your books
- **Customer Account**: Updates what this customer owes you
- **Reports**: Updates all sales and inventory reports
- **Taxes**: Calculates and tracks tax obligations

**The Complete Picture**:
```
Sale of Widget ($100) →
├── Inventory: Widget count goes from 10 to 9
├── Accounting: $100 added to Sales Revenue
├── Customer: $100 added to what they owe
└── Taxes: Sales tax calculated and tracked
```

**Beginner Reassurance**:
- You don't need to understand the accounting - BigLedger handles it
- You just focus on recording what you actually sold
- Everything stays in sync automatically
- You can see the impact in easy-to-read reports

**Q: How do I know if my business is profitable?**

**A:** This is the most important question! BigLedger makes this easy to understand:

**Simple Profitability Check**:
1. **Go to Reports** → **Profit & Loss** (Income Statement)
2. **Look at three key numbers**:
   - **Total Revenue**: All money coming in
   - **Total Expenses**: All money going out
   - **Net Profit**: Revenue minus Expenses

**What Good Looks Like**:
- **Positive Net Profit**: You're making money! 
- **Growing Revenue**: Sales are increasing over time
- **Controlled Expenses**: Costs aren't growing faster than sales

**Warning Signs to Watch**:
- **Negative Net Profit**: You're losing money
- **Declining Revenue**: Sales are going down
- **Expenses growing faster than revenue**: Costs are out of control

**Beginner-Friendly Profitability Metrics**:
- **Gross Profit Margin**: (Revenue - Cost of Goods) ÷ Revenue
  - Good: 40%+ for most businesses
- **Net Profit Margin**: Net Profit ÷ Revenue
  - Good: 10%+ for most small businesses

**Real Example**: 
Sarah's Bakery monthly report:
- Revenue: $8,000
- Cost of ingredients: $2,400 (30% - Good!)
- Other expenses: $4,000
- Net Profit: $1,600 (20% - Excellent!)

**Use BigLedger's Dashboard**: Shows your profitability at a glance with traffic light colors (Green = Good, Yellow = Warning, Red = Problem).

---

## Managing Suppliers and Purchases

**Q: How do I pay my suppliers?**

**A:** Managing supplier payments is like paying your household bills, but with better tracking:

**The Complete Process**:

**Step 1: Record What You Owe**
- Enter supplier invoices as "Bills" in BigLedger
- This tracks what you owe without paying yet
- System reminds you when payments are due

**Step 2: Schedule Payments**
- Review bills due this week
- Group payments by supplier or due date
- Choose payment method (check, bank transfer, etc.)

**Step 3: Make Payments**
- Pay suppliers through your preferred method
- Record the payment in BigLedger
- System automatically matches payment to bill

**Step 4: Track Results**
- See what's paid and what's still owed
- Track payment history with each supplier
- Monitor cash flow impact

**Beginner-Friendly Tips**:
- Set a weekly "pay bills" routine
- Take advantage of early payment discounts
- Always record the payment in BigLedger (even if paid outside the system)
- Use payment tracking to improve cash flow planning

**Q: What are "purchase orders" and do I need them?**

**A:** Purchase orders (POs) are like a formal shopping list that becomes a contract:

**You DON'T need POs if**:
- You buy simple supplies (office supplies, gas, etc.)
- Purchases are small and routine
- You have simple supplier relationships

**You DO need POs if**:
- Making large purchases (over $1,000)
- Buying custom or special-order items
- Need approval for purchases
- Want to track what was ordered vs. what was received

**Benefits of Using POs**:
- **Control spending**: Approve before money is spent
- **Track orders**: Know what's coming and when
- **Avoid disputes**: Clear record of what was ordered
- **Better accounting**: Match PO → Receipt → Invoice

**Simple Process**:
1. **Create PO**: List what you want to buy
2. **Get approval**: (if required by your business)
3. **Send to supplier**: They know exactly what you want
4. **Receive goods**: Check against PO
5. **Pay invoice**: Verify invoice matches PO and receipt

**Start Simple**: Begin using POs for purchases over $500, then expand as you get comfortable.

---

## Understanding Money Flow

**Q: What are "chart of accounts" and why do I need them?**

**A:** Chart of accounts is like organizing your filing cabinet - it's a way to categorize all your business money:

**Think of it as organized folders**:
- **Assets**: Things you own (cash, equipment, inventory)
- **Liabilities**: Things you owe (loans, credit cards, bills)
- **Equity**: Your ownership in the business
- **Revenue**: Money coming in from sales
- **Expenses**: Money going out for costs

**Why It Matters**:
- **Organized reporting**: Know exactly where money goes
- **Tax preparation**: Easy to find deductible expenses
- **Business insights**: See which expenses are growing
- **Professional appearance**: Clean books for banks/investors

**BigLedger Makes This Easy**:
- Pre-built chart of accounts for your industry
- Automatic categorization of common transactions
- Simple names instead of accounting jargon
- Easy to modify as your business grows

**Beginner Approach**:
1. **Start with BigLedger's template** (90% of accounts you'll need)
2. **Add specific accounts** for your business (like "Website Hosting")
3. **Don't overthink it** - you can adjust as you learn
4. **Ask your accountant** to review once per year

**Example for a Consulting Business**:
```
INCOME:
├── Consulting Revenue
├── Training Revenue
└── Other Income

EXPENSES:
├── Office Rent
├── Internet & Phone
├── Professional Development
├── Marketing
└── Travel
```

**Q: How do I reconcile my bank account?**

**A:** Bank reconciliation is like balancing your checkbook, but BigLedger makes it much easier:

**What Bank Reconciliation Means**:
Making sure your BigLedger records match your actual bank statement.

**Why It's Important**:
- **Catch errors**: Find mistakes before they become big problems
- **Prevent fraud**: Notice unauthorized transactions quickly
- **Accurate reporting**: Ensure financial reports are correct
- **Peace of mind**: Know your cash position is accurate

**BigLedger's Smart Process**:
1. **Connect your bank**: Link bank account for automatic transaction import
2. **Review transactions**: BigLedger shows bank transactions vs. your records
3. **Match automatically**: System automatically matches most transactions
4. **Handle exceptions**: Review and categorize any unmatched items
5. **Confirm balance**: Verify your books match your bank

**What to Do with Common Unmatched Items**:
- **Bank fees**: Categorize as "Bank Charges" expense
- **Interest earned**: Categorize as "Interest Income"
- **Automatic payments**: Make sure they're recorded in your system
- **Deposits**: Verify all sales were recorded properly

**Beginner Schedule**:
- **Weekly**: For active businesses with many transactions
- **Monthly**: For smaller businesses with fewer transactions
- **Never less than monthly**: Things get too hard to track

**Red Flags to Watch For**:
- Transactions you don't recognize
- Amounts that don't match your records
- Missing deposits or payments
- Unusual bank fees

---

## Generating Reports

**Q: How do I generate reports for my accountant?**

**A:** BigLedger makes it easy to give your accountant exactly what they need:

**Essential Reports for Accountants**:

**1. Trial Balance**
- Shows all account balances
- Used to verify books are balanced
- Usually needed monthly or quarterly

**2. Profit & Loss (Income Statement)**
- Shows revenue and expenses for a period
- Needed monthly, quarterly, and annually

**3. Balance Sheet**
- Shows assets, liabilities, and equity at a specific date
- Snapshot of financial position

**4. Cash Flow Statement**
- Shows where cash came from and went to
- Important for understanding cash management

**5. General Ledger Detail**
- Shows all transactions by account
- Used for detailed review and audits

**How to Generate** (Super Easy):
1. **Go to Reports section**
2. **Select report type**
3. **Choose date range**
4. **Click "Generate"**
5. **Export to PDF or Excel**
6. **Email directly to accountant**

**Accountant Communication Tips**:
- **Set regular schedule**: Monthly or quarterly report delivery
- **Use consistent format**: Same reports, same date ranges
- **Include notes**: Explain any unusual transactions
- **Give access**: Consider giving accountant read-only access to BigLedger

**Q: What reports should I look at regularly to understand my business?**

**A:** As a business owner, focus on these key reports that tell the story of your business:

**Daily/Weekly Reports**:

**1. Cash Position Dashboard**
- How much cash you have right now
- What's coming in this week
- What bills are due

**2. Sales Summary**
- This week vs last week
- This month vs last month
- Top-selling products/services

**Monthly Reports**:

**3. Profit & Loss Statement**
- Are you making money?
- Which expenses are growing?
- Revenue trends

**4. Accounts Receivable Aging**
- Who owes you money?
- How old are the debts?
- Collection priorities

**5. Inventory Status** (if applicable)
- What's running low?
- What's not selling?
- Reorder priorities

**Quarterly Reports**:

**6. Business Performance Summary**
- Growth trends
- Profitability analysis
- Key performance indicators

**How to Read Reports** (Beginner Tips):
- **Look for trends**: Is it getting better or worse?
- **Compare periods**: This month vs last month
- **Watch percentages**: Often more important than raw numbers
- **Focus on what you can control**: Expenses, pricing, collections

**Warning Signs in Reports**:
- Profit margins getting smaller
- Cash balance declining
- Old unpaid invoices growing
- Inventory not turning over

---

## Error Prevention and Recovery

**Q: What if I make a mistake?**

**A:** Mistakes happen to everyone! BigLedger is designed to help you fix them easily:

**Common Mistakes and How to Fix Them**:

**1. Wrong Amount on Invoice**
- **Easy fix**: Edit the invoice if not paid yet
- **If already paid**: Create a credit note for difference

**2. Forgot to Record a Sale**
- **Easy fix**: Create invoice for the backdated sale
- **Best practice**: Try to enter sales daily to avoid this

**3. Paid Wrong Amount to Supplier**
- **Overpaid**: Supplier owes you credit for next purchase
- **Underpaid**: Pay the difference on next payment

**4. Categorized Expense Wrong**
- **Easy fix**: Move expense to correct category
- **System keeps history**: You can see what changed

**BigLedger's Mistake-Prevention Features**:
- **Warnings**: System alerts you to unusual amounts
- **Duplicates**: Prevents entering same transaction twice
- **Required fields**: Won't let you skip important information
- **Approval workflows**: Someone else reviews big transactions

**When to Get Help**:
- **Complex accounting errors**: Contact support or your accountant
- **Tax-related mistakes**: Definitely involve a professional
- **System issues**: Contact BigLedger support immediately

**Best Practices to Avoid Mistakes**:
- **Enter transactions daily**: Don't let them pile up
- **Double-check big amounts**: Anything over $1,000
- **Review reports weekly**: Catch errors early
- **Set up approval rules**: Someone else checks important transactions

**Remember**: Making mistakes while learning is normal and expected. The key is catching and fixing them quickly.

---

## Next Steps for Business Operations

**Q: I understand the basics - what should I focus on first?**

**A:** Smart question! Here's a beginner-friendly priority order:

**Week 1-2: Foundation**
1. Set up customers and suppliers
2. Create basic product/service list
3. Start entering sales (invoices)
4. Record basic expenses

**Week 3-4: Cash Management**
1. Connect bank account
2. Learn bank reconciliation
3. Set up supplier payment process
4. Start tracking what customers owe you

**Month 2: Reporting & Analysis**
1. Generate first Profit & Loss report
2. Set up regular report schedule
3. Learn to read cash flow
4. Start tracking business trends

**Month 3: Optimization**
1. Set up approval workflows (if needed)
2. Automate recurring transactions
3. Improve inventory tracking
4. Plan for growth features

**Key Success Factors**:
- **Start simple**: Don't try to use every feature immediately
- **Be consistent**: Enter data regularly
- **Learn gradually**: Add one new feature per week
- **Get help**: Use training resources and support

**Q: How do I know I'm doing this right?**

**A:** Great question! Here are signs you're on the right track:

**Good Signs You're Succeeding**:
- ✅ You can answer "How much cash do I have?" instantly
- ✅ You know which customers owe you money
- ✅ Your inventory counts match what's in the system
- ✅ Your accountant is happy with your records
- ✅ You're making business decisions based on reports
- ✅ Tax time is easier than before

**Warning Signs You Need Help**:
- ❌ Reports don't match what you expect
- ❌ Can't explain where your cash went
- ❌ Inventory is always wrong
- ❌ Spending too much time on data entry
- ❌ Making decisions based on gut feeling instead of data

**Monthly Check-Up Questions**:
1. Do my bank balances match BigLedger?
2. Are customer payments being recorded properly?
3. Are all expenses categorized correctly?
4. Can I explain my profit/loss to someone else?

**Remember**: You don't need to be perfect immediately. Focus on consistent improvement and don't hesitate to ask for help when needed.

---

*This FAQ covers the fundamental business operations that every business owner needs to understand. For more advanced topics or specific industry questions, please refer to the other FAQ sections or contact our support team.*