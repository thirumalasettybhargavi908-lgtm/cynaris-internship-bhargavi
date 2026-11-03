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
    'employees': [450, 1200, 320, 180, 85]
}
df = pd.DataFrame(data)

print("--- 1. FROM & SELECT * (Dataset Preview) ---")
print(df.head(), "\n")

print("--- 2. SELECT Specific Columns ---")
print(df[['company_name', 'sector', 'annual_revenue_in_cr']].head(), "\n")

print("--- 3. WHERE: Single Condition (State = Karnataka) ---")
print(df[df['state'] == 'Karnataka'], "\n")

print("--- 4. WHERE: Multiple Conditions (Karnataka AND Revenue > 100 Cr) ---")
print(df[(df['state'] == 'Karnataka') & (df['annual_revenue_in_cr'] > 100)], "\n")

print("--- 5. WHERE: IN Operator (Sectors: Technology or Finance) ---")
print(df[df['sector'].isin(['Technology', 'Finance'])])