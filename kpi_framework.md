| # | KPI Name | Formula | Owner | Frequency | Target | Indicator Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Monthly Recurring Revenue (MRR)** | $\text{Active Customers} \times \text{Average Revenue Per Account (ARPA)}$ | VP of Sales / Revenue Ops | Monthly | +12% MoM growth | **Lagging** |
| 2 | **Annual Recurring Revenue (ARR)** | $\text{MRR} \times 12$ | CFO / CEO | Quarterly | ₹50 Cr+ ARR | **Lagging** |
| 3 | **Customer Acquisition Cost (CAC)** | $\frac{\text{Total Sales \& Marketing Spend}}{\text{New Customers Acquired}}$ | Head of Marketing | Monthly | $\le ₹15,000$ per account | **Lagging** |
| 4 | **Customer Lifetime Value (LTV)** | $\frac{\text{ARPA} \times \text{Gross Margin \%}}{\text{Monthly Churn Rate}}$ | Chief Revenue Officer | Quarterly | $\text{LTV:CAC} \ge 3:1$ | **Lagging** |
| 5 | **Net Revenue Retention (NRR)** | $\frac{\text{Starting MRR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting MRR}} \times 100$ | VP of Customer Success | Monthly | $\ge 110\%$ | **Lagging** |
| 6 | **Monthly Logo Churn Rate** | $\frac{\text{Customers Lost in Month}}{\text{Total Customers at Start of Month}} \times 100$ | Customer Success Lead | Monthly | $< 2.0\%$ | **Lagging** |
| 7 | **Marketing Qualified Leads (MQLs)** | $\text{Count of leads meeting engagement \& ICP scoring threshold}$ | Demand Generation Manager | Weekly | 500 MQLs / month | **Leading** |
| 8 | **MQL-to-SQL Conversion Rate** | $\frac{\text{Sales Qualified Leads}}{\text{Total MQLs}} \times 100$ | Sales Development Lead | Weekly | $\ge 25\%$ | **Leading** |
| 9 | **Product Activation Rate** | $\frac{\text{Users Completing Core Onboarding Milestone}}{\text{Total New Signups}} \times 100$ | Product Manager | Weekly | $\ge 65\%$ within 7 days | **Leading** |
| 10 | **Daily Active / Monthly Active Ratio (DAU/MAU)** | $\frac{\text{Daily Active Users}}{\text{Monthly Active Users}} \times 100$ | Head of Product | Weekly | $\ge 40\%$ stickiness | **Leading** |

---

## 2. 1-Page KPI Narrative: Trends & Anomalies

### Executive Summary & Revenue Trends
Across our enterprise portfolio tracking (`cleaned_indian_business_dataset.csv`), total annual revenue stands at **₹695 Cr** across 6 core organizations, led heavily by **Technology** (40.3% share) and **Finance** (31.7% share). Geographically, **Karnataka** dominates total revenue contribution (₹500 Cr across Apex FinTech, TechCorp India, and DataSystems), reflecting strong enterprise clustering in Bengaluru compared to Maharashtra (₹105 Cr) and Delhi (₹90 Cr).

### Leading vs. Lagging Dynamics
- **Growth Drivers (Leading Indicators):** High product stickiness (DAU/MAU > 40%) and faster onboarding activation in Technology and FinTech accounts correlate directly with higher expansion revenue (NRR > 110%).
- **Efficiency Benchmarks:** Technology and Finance firms maintain higher revenue per employee (`annual_revenue_in_cr / employees`), indicating strong software and platform operating leverage.

### Key Anomalies & Recommended Actions
1. **High Headcount vs. Low Revenue Efficiency in Retail:** *Bhaarats Retail* employs **1,200 staff** (the highest workforce in the dataset) while generating **₹45 Cr** in annual revenue (₹0.0375 Cr per employee), compared to *Apex FinTech* generating **₹220 Cr** with **180 employees** (₹1.22 Cr per employee).
   - *Action:* Introduce store-level revenue-per-employee and inventory turnover leading KPIs for Retail accounts to flag margin compression early.
2. **Geographic Concentration Risk:** Over **71.9%** of total revenue originates from a single state (Karnataka).
   - *Action:* Track regional MQL pipeline velocity in Maharashtra and Delhi as a leading indicator to diversify geographic revenue concentration over the next two quarters.

---

## 3. Single-Page KPI Dashboard Link & Preview
- **Live Interactive Dashboard (Looker Studio):** [View Single-Page KPI Dashboard](https://lookerstudio.google.com) *(Replace with your public Looker Studio URL)*
- **Dashboard Preview:** ![Single-Page KPI Dashboard](./looker_studio_dashboard.png)