# Week 4, Day 4 — Hypothesis Testing
# Project: EDA on Indian Business Dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
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
alpha = 0.05

def interpret_test(name, t_stat, p_val, mean_diff_or_est, ci_low, ci_high, alpha=0.05):
    decision = "Reject H0 (Statistically Significant)" if p_val < alpha else "Fail to Reject H0 (Not Statistically Significant at α=0.05)"
    print(f"--- {name} ---")
    print(f"Test Statistic: {t_stat:.4f}")
    print(f"p-value:        {p_val:.4f}")
    print(f"Estimate:       {mean_diff_or_est:.2f} | 95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
    print(f"Decision:       {decision}\n")

# ==============================================================================
# SCENARIO 1: One-Sample t-test on Annual Revenue (Cr)
# H0: Mean annual revenue = 100 Cr | H1: Mean annual revenue != 100 Cr
# ==============================================================================
rev = df['annual_revenue_in_cr']
mu_0 = 100.0
t1, p1 = stats.ttest_1samp(rev, popmean=mu_0)
se1 = rev.std(ddof=1) / np.sqrt(len(rev))
ci1_low, ci1_high = stats.t.interval(0.95, df=len(rev)-1, loc=rev.mean(), scale=se1)

print("=== THREE BUSINESS HYPOTHESIS TEST SCENARIOS ===\n")
print("Scenario 1 Hypotheses (Annual Revenue Benchmark):")
print("  H0: μ_revenue = 100 Cr")
print("  H1: μ_revenue ≠ 100 Cr\n")
interpret_test("Scenario 1: One-Sample t-test (Revenue vs. 100 Cr)", t1, p1, rev.mean(), ci1_low, ci1_high, alpha)

# ==============================================================================
# SCENARIO 2: Two-Sample Welch's t-test (Karnataka vs. Non-Karnataka Revenue)
# H0: μ_KA - μ_NonKA = 0 | H1: μ_KA - μ_NonKA != 0
# ==============================================================================
ka_rev = df[df['state'] == 'Karnataka']['annual_revenue_in_cr']
other_rev = df[df['state'] != 'Karnataka']['annual_revenue_in_cr']
t2, p2 = stats.ttest_ind(ka_rev, other_rev, equal_var=False)

diff2 = ka_rev.mean() - other_rev.mean()
se2 = np.sqrt(ka_rev.var(ddof=1)/len(ka_rev) + other_rev.var(ddof=1)/len(other_rev))
df2_welch = (ka_rev.var(ddof=1)/len(ka_rev) + other_rev.var(ddof=1)/len(other_rev))**2 / (
    (ka_rev.var(ddof=1)/len(ka_rev))**2 / (len(ka_rev)-1) +
    (other_rev.var(ddof=1)/len(other_rev))**2 / (len(other_rev)-1)
)
ci2_low, ci2_high = stats.t.interval(0.95, df=df2_welch, loc=diff2, scale=se2)

print("Scenario 2 Hypotheses (Regional Revenue Comparison):")
print("  H0: μ_Karnataka = μ_Other_States")
print("  H1: μ_Karnataka ≠ μ_Other_States\n")
interpret_test("Scenario 2: Two-Sample Welch's t-test (KA vs. Non-KA Revenue)", t2, p2, diff2, ci2_low, ci2_high, alpha)

# ==============================================================================
# SCENARIO 3: Two-Sample Welch's t-test (Tech/Finance vs. Retail/Logistics Headcount)
# H0: μ_TechFin - μ_RetailLog = 0 | H1: μ_TechFin - μ_RetailLog != 0
# ==============================================================================
tech_fin_emp = df[df['sector'].isin(['Technology', 'Finance'])]['employees']
ret_log_emp = df[~df['sector'].isin(['Technology', 'Finance'])]['employees']
t3, p3 = stats.ttest_ind(tech_fin_emp, ret_log_emp, equal_var=False)

diff3 = tech_fin_emp.mean() - ret_log_emp.mean()
se3 = np.sqrt(tech_fin_emp.var(ddof=1)/len(tech_fin_emp) + ret_log_emp.var(ddof=1)/len(ret_log_emp))
df3_welch = (tech_fin_emp.var(ddof=1)/len(tech_fin_emp) + ret_log_emp.var(ddof=1)/len(ret_log_emp))**2 / (
    (tech_fin_emp.var(ddof=1)/len(tech_fin_emp))**2 / (len(tech_fin_emp)-1) +
    (ret_log_emp.var(ddof=1)/len(ret_log_emp))**2 / (len(ret_log_emp)-1)
)
ci3_low, ci3_high = stats.t.interval(0.95, df=df3_welch, loc=diff3, scale=se3)

print("Scenario 3 Hypotheses (Sector Headcount Comparison):")
print("  H0: μ_TechFinance = μ_RetailLogistics")
print("  H1: μ_TechFinance ≠ μ_RetailLogistics\n")
interpret_test("Scenario 3: Two-Sample Welch's t-test (Tech/Fin vs. Retail/Log Employees)", t3, p3, diff3, ci3_low, ci3_high, alpha)

# ==============================================================================
# VISUALIZATION: Group Means & 95% Confidence Intervals
# ==============================================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
fig.suptitle('Week 4 Day 4 — Hypothesis Testing: Group Means & 95% Confidence Intervals', fontsize=13, fontweight='bold')

groups_rev = ['Karnataka Hub', 'Other States']
means_rev = [ka_rev.mean(), other_rev.mean()]
errs_rev = [
    stats.t.ppf(0.975, len(ka_rev)-1) * (ka_rev.std(ddof=1)/np.sqrt(len(ka_rev))),
    stats.t.ppf(0.975, len(other_rev)-1) * (other_rev.std(ddof=1)/np.sqrt(len(other_rev)))
]
axes[0].bar(groups_rev, means_rev, yerr=errs_rev, capsize=6, color=['#0F766E', '#10B981'], alpha=0.88)
axes[0].axhline(mu_0, color='#EF4444', linestyle='--', label=f'Benchmark ({mu_0:.0f} Cr)')
axes[0].set_title('Annual Revenue (Cr) by Region (with 95% CI)')
axes[0].set_ylabel('Mean Revenue (Cr)')
axes[0].legend()

groups_emp = ['Tech & Finance', 'Retail & Logistics']
means_emp = [tech_fin_emp.mean(), ret_log_emp.mean()]
errs_emp = [
    stats.t.ppf(0.975, len(tech_fin_emp)-1) * (tech_fin_emp.std(ddof=1)/np.sqrt(len(tech_fin_emp))),
    stats.t.ppf(0.975, len(ret_log_emp)-1) * (ret_log_emp.std(ddof=1)/np.sqrt(len(ret_log_emp)))
]
axes[1].bar(groups_emp, means_emp, yerr=errs_emp, capsize=6, color=['#0F172A', '#2563EB'], alpha=0.88)
axes[1].set_title('Employee Headcount by Sector Group (with 95% CI)')
axes[1].set_ylabel('Mean Employees')

plt.tight_layout()
plt.savefig('hypothesis_tests_summary.png', dpi=150)
print("Saved hypothesis_tests_summary.png successfully.")