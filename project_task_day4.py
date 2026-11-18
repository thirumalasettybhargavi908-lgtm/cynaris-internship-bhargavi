# Week 1, Day 4 — Advanced Data Cleaning & Missing Value Imputation
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 1. Create a sample dataset with missing (NaN) values to practice data cleaning
data = {
    'company_name': ['TechCorp', 'RetailHub', 'LogiMove', 'FinServe', 'DataSystems', 'MetroRetail'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', np.nan, 'Karnataka', 'Maharashtra'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', np.nan, 'Retail'],
    'annual_revenue_in_cr': [150.0, np.nan, 90.0, 220.0, 130.0, 60.0],
    'employees': [450, 1200, np.nan, 180, 320, np.nan]
}
df = pd.DataFrame(data)

print("--- 1. Original Dataset with Missing Values (NaN) ---")
print(df, "\n")

# 2. Identify missing values count per column
print("--- 2. Missing Values Count per Column ---")
print(df.isnull().sum(), "\n")

# 3. Imputation: Fill missing categorical values (State & Sector) with 'Unknown' or Mode
df['state'] = df['state'].fillna('Unknown')
df['sector'] = df['sector'].fillna(df['sector'].mode()[0])

# 4. Imputation: Fill missing numerical values (Revenue & Employees) with Mean or Median
df['annual_revenue_in_cr'] = df['annual_revenue_in_cr'].fillna(df['annual_revenue_in_cr'].mean())
df['employees'] = df['employees'].fillna(df['employees'].median())

print("--- 3. Cleaned Dataset After Imputation ---")
print(df)