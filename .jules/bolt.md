## 2024-05-24 - NumPy Array Advanced Indexing for Mask Mapping
**Learning:** When performing pixel-value-to-label mapping in masks, using multiple boolean mask assignments (e.g., `new_mask[arr==100]=1`) is very slow due to repeated array iterations and mask creation O(N * C).
**Action:** Use a NumPy lookup table (LUT) cached as a function attribute and advanced indexing (`lut[arr]`). Ensure bound safety using `np.where` before indexing to map out-of-bounds to a default value and prevent `IndexError`. This results in a ~5.8x speedup.
