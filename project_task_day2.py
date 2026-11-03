import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

companies_data = {
    'company_id': [1, 2, 3, 4],
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka']
}
df_companies = pd.DataFrame(companies_data)

financials_data = {
    'company_id': [1, 2, 3, 5],
    'annual_revenue_in_cr': [120.5, 45.0, 89.2, 55.0],
    'sector': ['Technology', 'Retail', 'Logistics', 'Manufacturing']
}
df_financials = pd.DataFrame(financials_data)

print("--- Base Table 1: Companies ---")
print(df_companies, "\n")
print("--- Base Table 2: Financials ---")
print(df_financials, "\n")

print("--- 2. INNER JOIN ---")
inner_joined = pd.merge(df_companies, df_financials, on='company_id', how='inner')
print(inner_joined, "\n")

print("--- 3. LEFT JOIN ---")
left_joined = pd.merge(df_companies, df_financials, on='company_id', how='left')
print(left_joined, "\n")

# Keeps all rows from the right table (financials) and matching rows from the left
print("--- 4. RIGHT JOIN ---")
right_joined = pd.merge(df_companies, df_financials, on='company_id', how='right')
print(right_joined, "\n")

print("--- 5. FULL OUTER JOIN ---")
outer_joined = pd.merge(df_companies, df_financials, on='company_id', how='outer')
print(outer_joined)