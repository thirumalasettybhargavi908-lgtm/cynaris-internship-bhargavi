# Week 4, Day 5 — Data Analysis Capstone (Week 4)
# Project: End-to-End Analysis on Indian Business Dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# 1. Load & Clean Dataset (uses Indian Business Dataset; supports external CSV if present)
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

# Data cleaning & feature engineering
df = df.drop_duplicates().copy()
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].median())
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].fillna('Unknown').str.strip()

df['revenue_per_employee_cr'] = (df['annual_revenue_in_cr'] / df['employees']).round(4)
df['high_revenue_flag'] = np.where(df['annual_revenue_in_cr'] >= 100, 'High (>=100 Cr)', 'Moderate (<100 Cr)')

print("=== CAPSTONE DATASET OVERVIEW ===")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print(f"Total Revenue: ₹{df['annual_revenue_in_cr'].sum():.1f} Cr | Total Headcount: {df['employees'].sum():,}\n")

# 2. Descriptive Statistics
rev = df['annual_revenue_in_cr']
emp = df['employees']
print("=== DESCRIPTIVE SUMMARY ===")
print(f"Revenue (Cr) -> Mean: {rev.mean():.2f}, Median: {rev.median():.2f}, SD: {rev.std():.2f}, Skew: {rev.skew():.2f}")
print(f"Employees    -> Mean: {emp.mean():.2f}, Median: {emp.median():.2f}, SD: {emp.std():.2f}, Skew: {emp.skew():.2f}\n")

# 3. Correlation & Simple Linear Regression (Revenue ~ Employees)
pearson_r = emp.corr(rev, method='pearson')
spearman_rho = emp.corr(rev, method='spearman')
slope, intercept = np.polyfit(emp, rev, 1)
y_pred = intercept + slope * emp
ss_res = np.sum((rev - y_pred) ** 2)
ss_tot = np.sum((rev - rev.mean()) ** 2)
r2 = 1 - (ss_res / ss_tot)
mae = np.mean(np.abs(rev - y_pred))
rmse = np.sqrt(np.mean((rev - y_pred) ** 2))

print("=== CORRELATION & SIMPLE LINEAR REGRESSION ===")
print(f"Pearson r: {pearson_r:.4f} | Spearman rho: {spearman_rho:.4f}")
print(f"Model: Revenue = {intercept:.2f} + ({slope:.4f} * Employees) | R² = {r2:.4f}, MAE = {mae:.2f} Cr, RMSE = {rmse:.2f} Cr\n")

# 4. Hypothesis Test (Welch's Two-Sample t-test: Karnataka vs. Non-Karnataka Revenue)
ka_rev = df[df['state'] == 'Karnataka']['annual_revenue_in_cr']
other_rev = df[df['state'] != 'Karnataka']['annual_revenue_in_cr']
t_stat, p_val = stats.ttest_ind(ka_rev, other_rev, equal_var=False)

print("=== HYPOTHESIS TEST (KARNATAKA VS. OTHER STATES REVENUE) ===")
print(f"Karnataka Mean: {ka_rev.mean():.2f} Cr | Other States Mean: {other_rev.mean():.2f} Cr")
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}\n")

# 5. Executive Capstone Visual Dashboard (2x2 Grid)
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle('Week 4 Capstone — Indian Business Dataset Executive Summary', fontsize=14, fontweight='bold')

# Panel A: Revenue by Company
df_sorted = df.sort_values('annual_revenue_in_cr', ascending=True)
axes[0, 0].barh(df_sorted['company_name'], df_sorted['annual_revenue_in_cr'], color='#0F766E')
axes[0, 0].set_title('Annual Revenue by Company (₹ Cr)')
axes[0, 0].set_xlabel('Annual Revenue (₹ Cr)')

# Panel B: Revenue per Employee (Productivity)
prod_sorted = df.sort_values('revenue_per_employee_cr', ascending=True)
axes[0, 1].barh(prod_sorted['company_name'], prod_sorted['revenue_per_employee_cr'], color='#2563EB')
axes[0, 1].set_title('Revenue per Employee (₹ Cr / Headcount)')
axes[0, 1].set_xlabel('₹ Cr per Employee')

# Panel C: Headcount vs. Revenue Regression Fit
axes[1, 0].scatter(emp, rev, color='#0F172A', s=70, label='Actual')
axes[1, 0].plot(emp, y_pred, color='#EF4444', linewidth=2, label=f'Fit (R²={r2:.2f})')
axes[1, 0].set_title('Headcount vs. Annual Revenue')
axes[1, 0].set_xlabel('Employees')
axes[1, 0].set_ylabel('Annual Revenue (₹ Cr)')
axes[1, 0].legend()

# Panel D: Mean Revenue by Region Group
reg_means = df.groupby(np.where(df['state'] == 'Karnataka', 'Karnataka', 'Other States'))['annual_revenue_in_cr'].mean()
axes[1, 1].bar(reg_means.index, reg_means.values, color=['#10B981', '#6366F1'])
axes[1, 1].set_title('Mean Annual Revenue by Region (₹ Cr)')
axes[1, 1].set_ylabel('Mean Revenue (₹ Cr)')

plt.tight_layout()
plt.savefig('capstone_executive_overview.png', dpi=150)
print("Saved capstone_executive_overview.png successfully.")