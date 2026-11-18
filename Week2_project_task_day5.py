# Week 2, Day 5 — NumPy for Data (Efficient Numerical Computation & Array Operations)
# Project: EDA on Indian Business Dataset

import numpy as np
import time
import warnings
warnings.filterwarnings('ignore')

# 1. Create and Manipulate 1D, 2D, and 3D NumPy Arrays
print("--- 1. ARRAY CREATION & MANIPULATION ---")
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[150, 45, 90], [220, 130, 60]]) # e.g., Indian business annual revenues by sector/region
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array Shape:", arr_1d.shape)
print("2D Array Shape:", arr_2d.shape, "\n")

# 2. Vectorised Operations & Aggregations Across Axes
print("--- 2. VECTORISED OPERATIONS & AXIS AGGREGATIONS ---")
print("Original 2D Array:\n", arr_2d)
print("Sum across columns (axis=0):", np.sum(arr_2d, axis=0))
print("Mean across rows (axis=1):", np.mean(arr_2d, axis=1), "\n")

# 3. Boolean Masking and Fancy Indexing
print("--- 3. BOOLEAN MASKING & FANCY INDEXING ---")
mask = arr_2d > 100
print("Mask (Elements > 100):\n", mask)
print("Filtered values using mask:", arr_2d[mask], "\n")

# 4. Statistical Measures
print("--- 4. STATISTICAL MEASURES ---")
revenues = np.array([150.0, 45.0, 90.0, 220.0, 130.0, 60.0, 180.0, 110.0])
print("Mean Revenue:", np.mean(revenues))
print("Standard Deviation:", np.std(revenues))
print("75th Percentile:", np.percentile(revenues, 75))
print("Correlation Matrix:\n", np.corrcoef(arr_2d))
print()

# 5. Performance Benchmark: NumPy vs Python Loops (1M-row dataset)
print("--- 5. PERFORMANCE BENCHMARK (1 Million Elements) ---")
size = 1_000_000
py_list = list(range(size))
np_arr = np.arange(size)

# Python Loop Benchmark
start_time = time.time()
py_result = [x * 2 for x in py_list]
py_duration = time.time() - start_time
print(f"Python List comprehension time: {py_duration:.4f} seconds")

# NumPy Vectorised Benchmark
start_time = time.time()
np_result = np_arr * 2
np_duration = time.time() - start_time
print(f"NumPy vectorised operation time: {np_duration:.4f} seconds")
print(f"NumPy is approximately {py_duration / np_duration:.1f}x faster!")