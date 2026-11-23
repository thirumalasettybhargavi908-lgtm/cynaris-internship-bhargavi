# Week 4, Day 1 — Statistics for Data Analysis
# Project: EDA on Indian Business Dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset (with fallback if CSV is not in current branch)
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

# 2. Central Tendency & Dispersion (Mean, Median, Mode, Variance, Std Dev)
def descriptive_summary(series, name):
    mean_val = series.mean()
    median_val = series.median()
    mode_val = series.mode().tolist()
    var_val = series.var()
    std_val = series.std()
    skew_val = series.skew()
    
    print(f"=== {name.upper()} DESCRIPTIVE STATISTICS ===")
    print(f"Mean:               {mean_val:.2f}")
    print(f"Median:             {median_val:.2f}")
    print(f"Mode:               {mode_val}")
    print(f"Variance:           {var_val:.2f}")
    print(f"Standard Deviation: {std_val:.2f}")
    print(f"Skewness:           {skew_val:.2f} ({'Right-Skewed' if skew_val > 0.5 else 'Left-Skewed' if skew_val < -0.5 else 'Approx. Symmetric'})\n")

descriptive_summary(df['annual_revenue_in_cr'], 'Annual Revenue (Cr)')
descriptive_summary(df['employees'], 'Employees')

# 3. Percentiles, Quartiles, and IQR
print("=== PERCENTILES & QUARTILES (ANNUAL REVENUE IN CR) ===")
percentiles = np.percentile(df['annual_revenue_in_cr'], [10, 25, 50, 75, 90])
q1, q2, q3 = percentiles[1], percentiles[2], percentiles[3]
iqr = q3 - q1

print(f"10th Percentile: {percentiles[0]:.2f}")
print(f"Q1 (25th):       {q1:.2f}")
print(f"Q2 / Median:     {q2:.2f}")
print(f"Q3 (75th):       {q3:.2f}")
print(f"90th Percentile: {percentiles[4]:.2f}")
print(f"IQR (Q3 - Q1):   {iqr:.2f}\n")

# 4. Visualizations: Frequency Distribution & Side-by-Side Box Plots
df['region_group'] = np.where(df['state'] == 'Karnataka', 'Karnataka Hub', 'Other States')

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Week 4 Day 1 — Descriptive Statistics & Distribution Analysis', fontsize=13, fontweight='bold')

# Plot 1: Frequency Distribution (Histogram + KDE)
sns.histplot(df['annual_revenue_in_cr'], bins=4, kde=True, color='#0F766E', ax=axes[0])
axes[0].axvline(df['annual_revenue_in_cr'].mean(), color='#EF4444', linestyle='--', label=f"Mean ({df['annual_revenue_in_cr'].mean():.1f})")
axes[0].axvline(df['annual_revenue_in_cr'].median(), color='#2563EB', linestyle='-', label=f"Median ({df['annual_revenue_in_cr'].median():.1f})")
axes[0].set_title('Frequency Distribution: Annual Revenue (Right-Skewed)')
axes[0].set_xlabel('Annual Revenue (Cr)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# Plot 2: Side-by-Side Box Plots Comparing Two Groups
sns.boxplot(x='region_group', y='annual_revenue_in_cr', data=df, palette=['#10B981', '#6366F1'], ax=axes[1])
axes[1].set_title('Revenue Distribution: Karnataka Hub vs. Other States')
axes[1].set_xlabel('Region Group')
axes[1].set_ylabel('Annual Revenue (Cr)')

plt.tight_layout()
plt.savefig('descriptive_stats_plots.png', dpi=150)
print("Saved descriptive_stats_plots.png successfully.")