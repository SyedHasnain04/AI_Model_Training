
## 2024-05-18 - Optimize pixel-value-to-label mapping in masks using a NumPy lookup table (LUT)
**Learning:** Performing multiple boolean assignments for mask conversion (e.g., `new_mask[arr==100]=1`) is slow because it iterates over the array multiple times.
**Action:** When performing pixel-value-to-label mapping in masks, use a NumPy lookup table (LUT) cached as a function attribute. Ensure bound safety by using `np.where((arr >= 0) & (arr <= MAX_VAL), arr, 0)` before indexing the LUT to prevent `IndexError`s. This gives >6x performance improvement.
