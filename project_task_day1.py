import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
data = {
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'Mumbai Exports'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka', 'Maharashtra'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Manufacturing'],
    'annual_revenue_in_cr': [120.5, 45.0, 89.2, 210.0, 15.4],
    'employees': [450, 1200, 320, 180, 85],
    'is_active': [True, True, False, True, True]
}

df = pd.DataFrame(data)
print("--- 1. FROM: Full Dataset Preview ---")
print(df.head(), "\n")

# 2. SELECT: Choose specific columns (like SELECT company_name, sector FROM df)
print("--- 2. SELECT: Selecting Specific Columns ---")
selected_columns = df[['company_name', 'sector', 'annual_revenue_in_cr']]
print(selected_columns.head(), "\n")

# 3. WHERE: Filter rows based on conditions (like WHERE state = 'Karnataka')
print("--- 3. WHERE: Single Condition Filtering (State = Karnataka) ---")
karnataka_companies = df[df['state'] == 'Karnataka']
print(karnataka_companies, "\n")

# 4. WHERE with multiple conditions (AND / OR)
# Example: Companies in Karnataka AND Revenue > 100 Crore
print("--- 4. WHERE: Multiple Conditions (State = Karnataka AND Revenue > 100 Cr) ---")
filtered_companies = df[(df['state'] == 'Karnataka') & (df['annual_revenue_in_cr'] > 100)]
print(filtered_companies, "\n")

# 5. WHERE with .isin() (Equivalent to SQL IN operator)
print("--- 5. WHERE: IN Operator (Sectors in Technology or Finance) ---")
tech_finance = df[df['sector'].isin(['Technology', 'Finance'])]
print(tech_finance)