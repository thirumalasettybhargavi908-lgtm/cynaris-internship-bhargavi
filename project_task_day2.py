# Week 1, Day 2 - SQL Joins — Combining Tables
# Project: EDA on Indian Business Dataset

import pandas as pd
import sqlite3

# 1. Create sample DataFrames
df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'customer_name': ['Aarav', 'Ananya', 'Rohan'],
    'city': ['Bengaluru', 'Mumbai', 'Delhi']
})

df_orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer_id': [1, 2, 1],
    'sales_amount': [12500, 4500, 18000]
})

# 2. Load into SQLite database
conn = sqlite3.connect(':memory:')
df_customers.to_sql('customers', conn, index=False, if_exists='replace')
df_orders.to_sql('orders', conn, index=False, if_exists='replace')

# 3. Run INNER JOIN via Python
query = """
SELECT o.order_id, c.customer_name, c.city, o.sales_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;
"""

result_df = pd.read_sql_query(query, conn)
print(result_df)
conn.close()