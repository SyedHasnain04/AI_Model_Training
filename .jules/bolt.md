## 2024-05-15 - [NumPy LUT for pixel mapping]
**Learning:** When performing pixel-value-to-label mapping in masks (e.g., in `convert_mask`), multiple boolean mask assignments (e.g., `new_mask[arr==100]=1`) are highly inefficient for large arrays because they require scanning the array multiple times.
**Action:** Use a NumPy lookup table (LUT) cached as a function attribute. Ensure bound safety by using `np.where((arr >= 0) & (arr <= MAX_VAL), arr, 0)` before indexing the LUT to safely map out-of-bounds values to 0 (background) and prevent `IndexError`s.
