# Week 2, Day 1 — Data Visualisation
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set Seaborn theme for professional styling
sns.set_theme(style="whitegrid")

# 1. Load dataset (Simulated Indian Business Dataset)
data = {
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'DataSystems', 'MetroRetail', 'Vayu Energy', 'IndoPharma'],
    'state': ['Karnataka', 'Maharashtra', 'Delhi', 'Karnataka', 'Karnataka', 'Maharashtra', 'Gujarat', 'Tamil Nadu'],
    'sector': ['Technology', 'Retail', 'Logistics', 'Finance', 'Technology', 'Retail', 'Energy', 'Healthcare'],
    'annual_revenue_in_cr': [150.0, 45.0, 90.0, 220.0, 130.0, 60.0, 180.0, 110.0],
    'employees': [450, 1200, 300, 180, 320, 500, 400, 250],
    'customer_rating': [4.5, 3.8, 4.0, 4.7, 4.2, 3.5, 4.6, 4.1]
}
df = pd.DataFrame(data)

# Create a figure with subplots or plot individually
plt.figure(figsize=(16, 12))

# 1. BAR CHART: Annual Revenue by Sector using Seaborn
plt.subplot(2, 3, 1)
sns.barplot(data=df, x='sector', y='annual_revenue_in_cr', palette='Blues_d', ci=None)
plt.title('Average Revenue by Sector')
plt.xlabel('Sector')
plt.ylabel('Revenue (Cr)')
plt.xticks(rotation=45)

# 2. LINE CHART: Employee Count Trend across Companies (using Matplotlib)
plt.subplot(2, 3, 2)
plt.plot(df['company_name'], df['employees'], marker='o', color='green', linewidth=2, linestyle='-')
plt.title('Employee Count by Company')
plt.xlabel('Company Name')
plt.ylabel('Employees')
plt.xticks(rotation=45, ha='right')

# 3. SCATTER PLOT: Revenue vs Employees using Seaborn
plt.subplot(2, 3, 3)
sns.scatterplot(data=df, x='employees', y='annual_revenue_in_cr', hue='sector', s=100)
plt.title('Revenue vs. Employees')
plt.xlabel('Employees')
plt.ylabel('Annual Revenue (Cr)')

# 4. HISTOGRAM: Distribution of Customer Ratings using Matplotlib
plt.subplot(2, 3, 4)
plt.hist(df['customer_rating'], bins=5, color='purple', edgecolor='black', alpha=0.7)
plt.title('Customer Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')

# 5. BOX PLOT: Revenue Distribution by Sector using Seaborn
plt.subplot(2, 3, 5)
sns.boxplot(data=df, x='sector', y='annual_revenue_in_cr', palette='Set2')
plt.title('Revenue Spread by Sector (Box Plot)')
plt.xlabel('Sector')
plt.ylabel('Revenue (Cr)')
plt.xticks(rotation=45)

# Adjust layout and save figure
plt.tight_layout()
plt.savefig('indian_business_visualisations.png', dpi=300)
print("Charts successfully generated and saved as 'indian_business_visualisations.png'!")
plt.show()