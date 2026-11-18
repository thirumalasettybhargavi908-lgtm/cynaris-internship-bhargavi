# Week 3, Day 1 — Power BI Data Preparation Script
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Generate clean dataset optimized for Power BI reporting
data = {
    'company_id': ['CMP001', 'CMP002', 'CMP003', 'CMP004', 'CMP005', 'CMP006', 'CMP007', 'CMP008'],
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'DataSystems', 'MetroRetail', 'Vayu Energy', 'IndoPharma'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka', 'Karnataka', 'Maharashtra', 'Gujarat', 'Tamil Nadu'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Technology', 'Retail', 'Energy', 'Healthcare'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 220.0, 130.0, 60.0, 180.0, 110.0],
    'employees': [450, 1200, 300, 180, 320, 500, 400, 250],
    'customer_rating': [4.5, 3.8, 4.0, 4.7, 4.2, 3.5, 4.6, 4.1],
    'report_date': ['2026-01-15', '2026-01-15', '2026-01-15', '2026-01-15', '2026-02-15', '2026-02-15', '2026-02-15', '2026-02-15']
}
df = pd.DataFrame(data)

# Export to CSV for Power BI Desktop ingestion
df.to_csv('powerbi_indian_business_dataset.csv', index=False)
print("Dataset successfully prepared and exported to 'powerbi_indian_business_dataset.csv' for Power BI Desktop!")