## 2024-05-18 - Optimize convert_mask with NumPy LUT
**Learning:** In pixel-value-to-label mapping for image segmentation masks, multiple boolean mask assignments (e.g., `new_mask[arr==100]=1`) create N intermediate boolean arrays and scale as O(N*C).
**Action:** Use a cached NumPy Lookup Table (LUT) with advanced array indexing (`lut[arr]`). Bound safety must be ensured using `np.where((arr >= 0) & (arr <= MAX_VAL), arr, 0)` before indexing to map out-of-bounds values to 0 (background), preventing `IndexError` while avoiding incorrect mappings from `np.clip`.
