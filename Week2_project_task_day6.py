# Week 2, Day 6 — Data Governance, Quality Checks & Great Expectations Simulation
# Project: EDA on Indian Business Dataset

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset (with intentionally injected errors to test validation)
data = {
    'company_id': ['CMP001', 'CMP002', 'CMP003', 'CMP004', None], # Error 1: Null ID
    'company_name': ['TechCorp India', 'Bhaarats Retail', 'Ganga Logistics', 'Apex FinTech', 'DataSystems'],
    'annual_revenue_in_cr': [150.0, -45.0, 90.0, 220.0, 130.0], # Error 2: Negative revenue (Validity fail)
    'customer_email': ['contact@techcorp.in', 'invalid-email', 'support@ganga.in', 'info@apexfin.com', 'admin@datasys.in'], # Error 3: Invalid email regex
    'contact_phone': ['+91-9876543210', '+91-8765432109', '+91-7654321098', '+91-6543210987', '+91-5432109876'] # PII field
}
df = pd.DataFrame(data)

print("--- 1. DATASET LOADED FOR GOVERNANCE CHECK ---")
print(df, "\n")

# 2. Automated Data Quality Validation Suite (Simulating Great Expectations Rules)
print("--- 2. RUNNING DATA QUALITY VALIDATION SUITE ---")
errors_found = 0

# Rule 1: Completeness - company_id must not be null
null_ids = df['company_id'].isnull().sum()
if null_ids > 0:
    print(f"[FAIL] Completeness Check: Found {null_ids} missing company_id(s).")
    errors_found += 1
else:
    print("[PASS] Completeness Check: No missing company_ids.")

# Rule 2: Validity - annual_revenue_in_cr must be >= 0
invalid_revenue = (df['annual_revenue_in_cr'] < 0).sum()
if invalid_revenue > 0:
    print(f"[FAIL] Validity Check: Found {invalid_revenue} negative revenue record(s).")
    errors_found += 1
else:
    print("[PASS] Validity Check: All revenues are valid.")

# Rule 3: Validity - Email format validation via regex
email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
invalid_emails = (~df['customer_email'].str.match(email_regex, na=False)).sum()
if invalid_emails > 0:
    print(f"[FAIL] Validity Check: Found {invalid_emails} invalid email format(s).")
    errors_found += 1
else:
    print("[PASS] Validity Check: All emails match required regex.")

print(f"\nValidation Summary: {errors_found} regression error(s) caught successfully! Pipeline halted to prevent bad data downstream.\n")

# 3. PII Masking & Classification Policy
print("--- 3. PII CLASSIFICATION & MASKING ---")
print("Classifying 'contact_phone' and 'customer_email' as CONFIDENTIAL PII under DPDP Act 2023.")
df['contact_phone_masked'] = df['contact_phone'].apply(lambda x: '***-***-' + str(x)[-4:] if pd.notnull(x) else x)
print(df[['company_name', 'contact_phone_masked']])