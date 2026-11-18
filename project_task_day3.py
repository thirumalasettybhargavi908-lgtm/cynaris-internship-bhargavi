# Week 1, Day 3 — SQL Aggregations — GROUP BY & HAVING
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 1. Sample Dataset creation
data = {
    'company_name': ['TechCorp', 'RetailHub', 'LogiMove', 'FinServe', 'DataSystems', 'MetroRetail'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka', 'Karnataka', 'Maharashtra'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Technology', 'Retail'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 220.0, 130.0, 60.0]
}
df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df, "\n")

# 2. GROUP BY & Aggregation (Equivalent to: SELECT state, SUM(annual_revenue_in_cr) FROM df GROUP BY state)
print("--- 2. GROUP BY: Total Revenue by State ---")
revenue_by_state = df.groupby('state')['annual_revenue_in_cr'].sum().reset_index()
print(revenue_by_state, "\n")

# 3. GROUP BY with Multiple Aggregations (COUNT, AVG, SUM)
print("--- 3. GROUP BY: Multiple Aggregations by Sector ---")
sector_stats = df.groupby('sector').agg(
    company_count=('company_name', 'count'),
    avg_revenue=('annual_revenue_in_cr', 'mean'),
    total_revenue=('annual_revenue_in_cr', 'sum')
).reset_index()
print(sector_stats, "\n")

# 4. HAVING Clause Equivalent (Filtering after GROUP BY)
# SQL Equivalent: SELECT state, SUM(annual_revenue_in_cr) FROM df GROUP BY state HAVING SUM(annual_revenue_in_cr) > 200
print("--- 4. HAVING Clause: States with Total Revenue > 200 Cr ---")
grouped_df = df.groupby('state')['annual_revenue_in_cr'].sum().reset_index()
filtered_having = grouped_df[grouped_df['annual_revenue_in_cr'] > 200]
print(filtered_having)
