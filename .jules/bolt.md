## 2024-05-14 - [Optimize convert_mask with NumPy LUT]
**Learning:** Using a NumPy lookup table (LUT) cached as a function attribute is significantly faster than multiple boolean mask assignments when performing pixel-value-to-label mapping in masks (e.g., in `convert_mask`). This yielded a ~12x speedup during benchmarking.
**Action:** When performing pixel-value-to-label mapping, use a NumPy lookup table (LUT) instead of multiple boolean mask assignments.
