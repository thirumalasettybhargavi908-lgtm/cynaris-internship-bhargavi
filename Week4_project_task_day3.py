# Week 4, Day 3 — Regression Analysis
# Project: EDA on Indian Business Dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset (with fallback if CSV is not in current branch)
csv_path = 'cleaned_indian_business_dataset.csv'
if not os.path.exists(csv_path):
    data = {
        'company_name': ['Apex FinTech', 'TechCorp India', 'DataSystems', 'Ganga Logistics', 'MetroRetail', 'Bhaarats Retail'],
        'sector': ['Finance', 'Technology', 'Technology', 'Logistics', 'Retail', 'Retail'],
        'state': ['Karnataka', 'Karnataka', 'Karnataka', 'Delhi', 'Maharashtra', 'Maharashtra'],
        'annual_revenue_in_cr': [220, 150, 130, 90, 60, 45],
        'employees': [180, 450, 320, 300, 500, 1200]
    }
    pd.DataFrame(data).to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)

# Add derived efficiency feature for richer correlation matrix
df['revenue_per_employee_cr'] = (df['annual_revenue_in_cr'] / df['employees']).round(4)

numeric_cols = ['employees', 'annual_revenue_in_cr', 'revenue_per_employee_cr']

# 2. Pearson & Spearman Correlation Coefficients
pearson_corr = df[numeric_cols].corr(method='pearson')
spearman_corr = df[numeric_cols].corr(method='spearman')

print("=== PEARSON CORRELATION MATRIX (LINEAR) ===")
print(pearson_corr.round(4), "\n")

print("=== SPEARMAN CORRELATION MATRIX (MONOTONIC / RANK) ===")
print(spearman_corr.round(4), "\n")

# 3. Simple Linear Regression using scikit-learn
# Predictor (X): Employees | Target (y): Annual Revenue (Cr)
X = df[['employees']]
y = df['annual_revenue_in_cr']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
residuals = y - y_pred

# 4. Model Evaluation Metrics: R², MAE, and RMSE
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("=== SIMPLE LINEAR REGRESSION RESULTS (Revenue ~ Employees) ===")
print(f"Intercept (b0): {model.intercept_:.4f}")
print(f"Slope (b1):     {model.coef_[0]:.4f}")
print(f"R² Score:       {r2:.4f} ({r2*100:.1f}% variance explained)")
print(f"MAE:            {mae:.2f} Cr")
print(f"RMSE:           {rmse:.2f} Cr\n")

# 5. Visualizations: Heatmap, Regression Fit, and Residual Diagnostics
fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))
fig.suptitle('Week 4 Day 3 — Correlation & Simple Linear Regression Analysis', fontsize=13, fontweight='bold')

# Plot 1: Pearson Correlation Heatmap
sns.heatmap(pearson_corr, annot=True, fmt='.2f', cmap='Teal', vmin=-1, vmax=1, ax=axes[0])
axes[0].set_title('Pearson Correlation Heatmap')

# Plot 2: Scatter Plot + Regression Line
axes[1].scatter(df['employees'], y, color='#0F766E', s=70, label='Actual Companies')
axes[1].plot(df['employees'], y_pred, color='#EF4444', linewidth=2, label=f'OLS Fit (R² = {r2:.2f})')
axes[1].set_title('Linear Regression: Employees vs. Revenue')
axes[1].set_xlabel('Employees')
axes[1].set_ylabel('Annual Revenue (Cr)')
axes[1].legend()

# Plot 3: Residual Plot (Checking Homoscedasticity & Linearity)
axes[2].scatter(y_pred, residuals, color='#2563EB', s=70)
axes[2].axhline(0, color='#0F172A', linestyle='--', linewidth=1.2)
axes[2].set_title('Residuals vs. Fitted Values')
axes[2].set_xlabel('Predicted Revenue (Cr)')
axes[2].set_ylabel('Residuals (Actual - Predicted)')

plt.tight_layout()
plt.savefig('regression_diagnostics.png', dpi=150)

# Plot 4: Scatter Matrix (Pairplot)
pair_fig = sns.pairplot(df[numeric_cols], diag_kind='kde', plot_kws={'color': '#0F766E', 's': 60})
pair_fig.fig.suptitle('Scatter Matrix — Indian Business Dataset', y=1.02, fontweight='bold')
pair_fig.savefig('correlation_scatter_matrix.png', dpi=150)

print("Saved regression_diagnostics.png and correlation_scatter_matrix.png successfully.")