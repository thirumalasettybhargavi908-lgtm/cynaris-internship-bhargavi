# Week 2, Day 2 — Pandas Advanced (Merge, Pivot, Melt, and Method Chaining)
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Create sample multi-tables to demonstrate advanced operations
companies_data = {
    'company_id': [1, 2, 3, 4],
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech'],
    'region': ['South', 'West', 'North', 'South']
}
df_companies = pd.DataFrame(companies_data)

sales_data = {
    'company_id': [1, 2, 3, 5],
    'Q1_sales': [120.5, 45.0, 89.2, 55.0],
    'Q2_sales': [135.0, 50.0, 95.0, 60.0]
}
df_sales = pd.DataFrame(sales_data)

print("--- 1. MERGE: Combining Multiple Tables (Full Outer Join) ---")
df_merged = pd.merge(df_companies, df_sales, on='company_id', how='outer')
print(df_merged, "\n")

# 2. PIVOT TABLE: Summarising sales by region
print("--- 2. PIVOT TABLE: Total Sales by Region ---")
# First let's clean missing values for clear pivot demonstration
df_clean = df_merged.fillna({'company_name': 'Unknown', 'region': 'Unknown', 'Q1_sales': 0, 'Q2_sales': 0})
pivot_table = pd.pivot_table(df_clean, values=['Q1_sales', 'Q2_sales'], index=['region'], aggfunc='sum')
print(pivot_table, "\n")

# 3. MELT: Reshaping wide data to long format
print("--- 3. MELT: Reshaping from Wide to Long Format ---")
df_melted = pd.melt(df_clean, id_vars=['company_id', 'company_name', 'region'], 
                    value_vars=['Q1_sales', 'Q2_sales'], 
                    var_name='Quarter', value_name='Sales')
print(df_melted.head(), "\n")

# 4. METHOD CHAINING: Cleaner, fluent Pandas workflows
print("--- 4. METHOD CHAINING Example ---")
summary_chained = (
    df_clean
    .assign(total_annual_sales=lambda x: x['Q1_sales'] + x['Q2_sales'])
    .query("total_annual_sales > 100")
    .sort_values(by='total_annual_sales', ascending=False)
    [['company_name', 'region', 'total_annual_sales']]
)
print(summary_chained)

# Export deliverable
summary_chained.to_csv('advanced_pandas_output.csv', index=False)
print("\nAdvanced analysis successfully executed and exported!")