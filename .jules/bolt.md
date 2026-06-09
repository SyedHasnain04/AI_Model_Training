## 2024-05-24 - Optimize pixel-value-to-label mapping using a cached NumPy LUT
**Learning:** In image segmentation notebooks, boolean mask assignments for label conversion (`new_mask[arr==X] = Y`) are highly inefficient due to redundant full-array evaluations.
**Action:** Replace multiple boolean mask evaluations with a pre-computed NumPy lookup table (LUT) cached as a function attribute. Ensure safe bounds mapping with `np.where((arr >= 0) & (arr <= max_val), arr, 0)` before indexing the LUT to avoid `IndexError`s.
