# Week 2, Day 4 — Data Cleaning (Missing Values, Duplicates, Outliers & String Standardization)
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset with intentional dirty data (missing values, typos, duplicates, outliers)
data = {
    'company_name': ['TechCorp India', '  bhaarats retail ', 'Ganga Logistics', 'TechCorp India', 'Apex FinTech', 'MetroRetail', 'Vayu Energy'],
    'state': ['Karnataka', 'maharashtra', 'Delhi', 'Karnataka', np.nan, 'Maharashtra', 'Gujarat'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Technology', 'Finance', 'retail', 'Energy'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 150.0, np.nan, 60.0, 5000.0], # 5000 is an outlier
    'employees': [450, 1200, 300, 450, 180, np.nan, 400]
}
df = pd.DataFrame(data)

print("--- BEFORE CLEANING ---")
print(df, "\n")
print("Missing Values Before:\n", df.isnull().sum(), "\n")

# 2. Handle Duplicates
df = df.drop_duplicates().reset_index(drop=True)

# 3. Standardize String Values (strip whitespace, title case)
df['company_name'] = df['company_name'].str.strip().str.title()
df['state'] = df['state'].str.strip().str.title()
df['sector'] = df['sector'].str.strip().str.title()

# 4. Handle Missing Values (Imputation)
df['state'] = df['state'].fillna('Unknown')
df['annual_revenue_in_cr'] = df['annual_revenue_in_cr'].fillna(df['annual_revenue_in_cr'].median())
df['employees'] = df['employees'].fillna(df['employees'].mean())

# 5. Handle Outliers using IQR method on 'annual_revenue_in_cr'
Q1 = df['annual_revenue_in_cr'].quantile(0.25)
Q3 = df['annual_revenue_in_cr'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Cap outliers
df['annual_revenue_in_cr'] = np.where(df['annual_revenue_in_cr'] > upper_bound, upper_bound, 
                                     np.where(df['annual_revenue_in_cr'] < lower_bound, lower_bound, df['annual_revenue_in_cr']))

print("--- AFTER CLEANING ---")
print(df, "\n")
print("Missing Values After:\n", df.isnull().sum())

# Export cleaned dataset and generate data quality log
df.to_csv('cleaned_dataset.csv', index=False)