# Week 4, Day 2 — Probability
# Project: EDA on Indian Business Dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# 2. Contingency Table & Basic Probabilities: P(A), P(A ∩ B), P(A | B)
# Define Event A: High Revenue (>= 100 Cr) | Event B: Located in Karnataka
df['high_revenue_A'] = df['annual_revenue_in_cr'] >= 100
df['karnataka_B'] = df['state'] == 'Karnataka'

ct = pd.crosstab(df['karnataka_B'], df['high_revenue_A'], margins=True)
print("=== CONTINGENCY TABLE (ROWS: Karnataka_B, COLS: High_Revenue_A) ===")
print(ct, "\n")

n_total = len(df)
p_a = df['high_revenue_A'].mean()
p_b = df['karnataka_B'].mean()
p_a_and_b = (df['high_revenue_A'] & df['karnataka_B']).mean()
p_a_given_b = p_a_and_b / p_b if p_b > 0 else 0.0

print("=== PROBABILITY CALCULATIONS ===")
print(f"P(A) [Revenue >= 100 Cr]:           {p_a:.4f} ({p_a*100:.1f}%)")
print(f"P(B) [State == Karnataka]:          {p_b:.4f} ({p_b*100:.1f}%)")
print(f"P(A ∩ B) [Both High Rev & KA]:      {p_a_and_b:.4f} ({p_a_and_b*100:.1f}%)")
print(f"P(A | B) [High Rev given KA]:       {p_a_given_b:.4f} ({p_a_given_b*100:.1f}%)\n")

# 3. Binomial Distribution Simulation (NumPy)
# Example: Simulating 10,000 trials of 20 enterprise leads where conversion probability p = 0.25
rng = np.random.default_rng(42)
n_trials = 20
p_conv = 0.25
binom_samples = rng.binomial(n=n_trials, p=p_conv, size=10000)

print("=== BINOMIAL SIMULATION SUMMARY (n=20, p=0.25, 10,000 draws) ===")
print(f"Simulated Mean: {binom_samples.mean():.2f} (Theoretical: {n_trials * p_conv:.2f})")
print(f"Simulated Std:  {binom_samples.std():.2f} (Theoretical: {np.sqrt(n_trials * p_conv * (1 - p_conv)):.2f})\n")

# 4. Central Limit Theorem (CLT) Sampling Simulation
# Sample repeatedly from the right-skewed annual_revenue_in_cr distribution
pop_revenue = df['annual_revenue_in_cr'].to_numpy()
sample_size = 3
n_simulations = 2000
sample_means = [rng.choice(pop_revenue, size=sample_size, replace=True).mean() for _ in range(n_simulations)]
sample_means = np.array(sample_means)

print("=== CENTRAL LIMIT THEOREM (CLT) SIMULATION ===")
print(f"Population Mean:        {pop_revenue.mean():.2f}, Population Std: {pop_revenue.std():.2f}")
print(f"Sample Means Mean:      {sample_means.mean():.2f}")
print(f"Sample Means Std (SE):  {sample_means.std():.2f}\n")

# 5. Visualizations: Normal Distribution (68-95-99.7 Rule), Binomial, and CLT
fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))
fig.suptitle('Week 4 Day 2 — Probability Distributions & CLT Simulation', fontsize=13, fontweight='bold')

# Plot 1: Normal Distribution & 68-95-99.7 Rule
mu, sigma = 100, 15
x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)
y_norm = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_norm - mu) / sigma) ** 2)

axes[0].plot(x_norm, y_norm, color='#0F766E', linewidth=2)
axes[0].fill_between(x_norm, y_norm, where=(np.abs(x_norm - mu) <= sigma), color='#10B981', alpha=0.45, label='68% (±1σ)')
axes[0].fill_between(x_norm, y_norm, where=((np.abs(x_norm - mu) > sigma) & (np.abs(x_norm - mu) <= 2*sigma)), color='#2563EB', alpha=0.25, label='95% (±2σ)')
axes[0].fill_between(x_norm, y_norm, where=((np.abs(x_norm - mu) > 2*sigma) & (np.abs(x_norm - mu) <= 3*sigma)), color='#6366F1', alpha=0.18, label='99.7% (±3σ)')
axes[0].set_title('Normal Distribution (68-95-99.7 Rule)')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=8)

# Plot 2: Binomial Distribution
vals, counts = np.unique(binom_samples, return_counts=True)
axes[1].bar(vals, counts / len(binom_samples), color='#2563EB', alpha=0.85)
axes[1].set_title('Binomial Simulation (n=20, p=0.25)')
axes[1].set_xlabel('Number of Successes')
axes[1].set_ylabel('Probability')

# Plot 3: CLT Sample Means Distribution
axes[2].hist(sample_means, bins=25, density=True, color='#0F766E', alpha=0.75, edgecolor='white')
axes[2].axvline(sample_means.mean(), color='#EF4444', linestyle='--', label=f"Mean of Means ({sample_means.mean():.1f})")
axes[2].set_title('CLT: Distribution of Sample Means')
axes[2].set_xlabel('Sample Mean Revenue (Cr)')
axes[2].set_ylabel('Density')
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig('probability_distributions_clt.png', dpi=150)
print("Saved probability_distributions_clt.png successfully.")