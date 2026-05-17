
## 2024-05-24 - Optimize convert_mask with NumPy Lookup Table
**Learning:** In Jupyter notebook pixel-wise operations on arrays, using multiple sequential boolean mask assignments (e.g., `new_mask[arr==100]=1`) is a major performance bottleneck due to repeatedly iterating over the array and allocating temporary boolean masks.
**Action:** Replace multiple boolean assignments with a high-performance, single-pass lookup table (LUT). Cache the LUT as a function attribute using `hasattr` to avoid reallocation. Prepend an explicit bounds safety check like `np.where((arr >= 0) & (arr <= 10000), arr, 0)` before indexing to prevent out-of-bounds `IndexError`s.

Note: Local environment dependency constraints (`numpy`, `torch` not available) prevented empirical empirical measurement, but performance gains are logically sound due to shifting from O(N*C) boolean passes to an O(N) array-based index lookup.
