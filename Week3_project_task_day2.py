# Week 3, Day 2 — DAX Basics Data Preparation Script
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset with revenue and cost columns for DAX calculations
data = {
    'company_id': ['CMP001', 'CMP002', 'CMP003', 'CMP004', 'CMP005'],
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'DataSystems'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Technology'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 220.0, 130.0],
    'total_cost_in_cr': [100.0, 35.0, 70.0, 150.0, 90.0],
    'transaction_date': ['2026-01-10', '2026-01-15', '2026-02-01', '2026-02-20', '2026-03-05']
}
df = pd.DataFrame(data)
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Export to CSV
df.to_csv('dax_dataset.csv', index=False)
print("Dataset prepared and exported to 'dax_dataset.csv' for Power BI DAX modeling!")