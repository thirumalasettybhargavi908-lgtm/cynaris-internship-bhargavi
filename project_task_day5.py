# Week 1, Day 5 — Python for Data — Pandas Basics
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset (Simulated Indian Business Dataset)
data = {
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'DataSystems', 'MetroRetail'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka', 'Karnataka', 'Maharashtra'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Technology', 'Retail'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 220.0, 130.0, 60.0],
    'employees': [450, 1200, 300, 180, 320, 500]
}
df = pd.DataFrame(data)

# 2. Inspect with .head(), .info(), .describe(), .value_counts()
print("--- .head() ---")
print(df.head(), "\n")

print("--- .info() ---")
df.info()
print("\n")

print("--- .describe() ---")
print(df.describe(), "\n")

print("--- .value_counts() (Sectors) ---")
print(df['sector'].value_counts(), "\n")

# 3. Filter rows & select columns
print("--- Filtered Rows (Revenue > 100 Cr) & Selected Columns ---")
filtered_df = df[df['annual_revenue_in_cr'] > 100][['company_name', 'sector', 'annual_revenue_in_cr']]
print(filtered_df, "\n")

# 4. Group by a column and aggregate
print("--- Group By Sector: Total Revenue ---")
grouped_df = df.groupby('sector')['annual_revenue_in_cr'].sum().reset_index()
print(grouped_df, "\n")

# 5. Export cleaned data to CSV
df.to_csv('cleaned_indian_business_dataset.csv', index=False)
print("Dataset successfully exported to cleaned_indian_business_dataset.csv")