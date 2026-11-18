import pandas as pd
import numpy as np
import sqlite3
import warnings
warnings.filterwarnings('ignore')

# 1. Automatically create a sample Indian Business Dataset DataFrame
data = {
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'customer_name': ['Aarav Sharma', 'Ananya Patel', 'Rohan Gupta', 'Priya Singh', 'Vikram Kumar', 
                      'Neha Verma', 'Amit Rao', 'Sneha Iyer', 'Rahul Nair', 'Pooja Deshmukh'],
    'city': ['Bengaluru', 'Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 
             'Hyderabad', 'Pune', 'Mumbai', 'Bengaluru', 'Delhi'],
    'category': ['Technology', 'Furniture', 'Technology', 'Office Supplies', 'Technology', 
                 'Furniture', 'Office Supplies', 'Technology', 'Office Supplies', 'Furniture'],
    'sales_amount': [12500, 4500, 18000, 3200, 22000, 6700, 1500, 11000, 4800, 9500],
    'order_status': ['Completed', 'Completed', 'Shipped', 'Cancelled', 'Completed', 
                     'Completed', 'Shipped', 'Completed', 'Cancelled', 'Completed'],
    'discount': [0.1, 0.0, 0.2, 0.0, 0.15, 0.05, 0.0, 0.1, None, 0.05]
}

df = pd.DataFrame(data)

# 2. Load DataFrame into an in-memory SQLite database
conn = sqlite3.connect(':memory:')
df.to_sql('sales_data', conn, index=False, if_exists='replace')

print("Dataset loaded successfully into SQLite database!\n")

# 3. Run a sample SQL query (SELECT, FROM, WHERE, AND, IN)
query = """
SELECT order_id, customer_name, city, sales_amount 
FROM sales_data 
WHERE sales_amount > 5000 
  AND city IN ('Bengaluru', 'Mumbai', 'Delhi');
"""

result_df = pd.read_sql_query(query, conn)
print("Query Results:")
print(result_df)

# 4. Export result set to CSV (fulfills your practical task requirement)
result_df.to_csv('filtered_sales_export.csv', index=False)
print("\nExported result set to filtered_sales_export.csv successfully!")

conn.close()