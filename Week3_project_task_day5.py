import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 1. Load cleaned dataset (auto-creates from your dataset if not in current branch)
csv_path = 'cleaned_indian_business_dataset.csv'
if not os.path.exists(csv_path):
    data = {
        'company_name': ['Apex FinTech', 'TechCorp India', 'DataSystems', 'Ganga Logistics', 'MetroRetail', 'Bhaarats Retail'],
        'sector': ['Finance', 'Technology', 'Technology', 'Logistics', 'Retail', 'Retail'],
        'state': ['Karnataka', 'Karnataka', 'Karnataka', 'Delhi', 'Maharashtra', 'Maharashtra'],
        'annual_revenue_in_cr': [220, 150, 130, 90, 60, 45],
        'employees': [180, 450, 320, 300, 500, 1200]
    }
    pd.DataFrame(data).to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)

# Week 3, Day 5 — KPI Design
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 1. Load cleaned dataset
df = pd.read_csv('cleaned_indian_business_dataset.csv')

# 2. Compute Business & Efficiency KPIs
df['revenue_per_employee_cr'] = (df['annual_revenue_in_cr'] / df['employees']).round(4)
df['revenue_share_pct'] = ((df['annual_revenue_in_cr'] / df['annual_revenue_in_cr'].sum()) * 100).round(2)

# Target benchmark: >= 0.40 Cr revenue per employee
TARGET_REV_PER_EMP = 0.40
df['kpi_status'] = np.where(df['revenue_per_employee_cr'] >= TARGET_REV_PER_EMP, 'On Target', 'Needs Attention')

print("=== COMPANY-LEVEL KPI SCORECARD ===")
print(df[['company_name', 'sector', 'state', 'annual_revenue_in_cr', 'employees', 'revenue_per_employee_cr', 'revenue_share_pct', 'kpi_status']])

# 3. Sector-Level KPI Summary
sector_kpis = df.groupby('sector').agg(
    total_revenue_cr=('annual_revenue_in_cr', 'sum'),
    total_employees=('employees', 'sum'),
    avg_rev_per_emp=('revenue_per_employee_cr', 'mean'),
    company_count=('company_name', 'count')
).reset_index()

print("\n=== SECTOR KPI SUMMARY ===")
print(sector_kpis)

# 4. Export KPI Summary & Visualize Single-Page KPI Chart
sector_kpis.to_csv('kpi_summary_output.csv', index=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Week 3 Day 5 — Single-Page KPI Summary (Indian Business Dataset)', fontsize=13, fontweight='bold')

# Chart 1: Total Revenue by Sector
axes[0].bar(sector_kpis['sector'], sector_kpis['total_revenue_cr'], color=['#0F766E', '#10B981', '#2563EB', '#6366F1'])
axes[0].set_title('Total Revenue by Sector (Cr)')
axes[0].set_ylabel('Revenue (Cr)')

# Chart 2: Revenue Efficiency (Cr per Employee) by Company
colors = ['#10B981' if s == 'On Target' else '#EF4444' for s in df['kpi_status']]
axes[1].barh(df['company_name'], df['revenue_per_employee_cr'], color=colors)
axes[1].axvline(TARGET_REV_PER_EMP, color='#0F172A', linestyle='--', label=f'Target ({TARGET_REV_PER_EMP} Cr/Emp)')
axes[1].set_title('Revenue per Employee vs. Target')
axes[1].set_xlabel('Cr per Employee')
axes[1].legend()

plt.tight_layout()
plt.savefig('kpi_dashboard_summary.png', dpi=150)
print("\nSaved kpi_summary_output.csv and kpi_dashboard_summary.png successfully.")