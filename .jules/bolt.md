## 2025-05-24 - Safe NumPy LUT Mask Conversion
**Learning:** When optimizing pixel-value-to-label mapping in masks with a NumPy lookup table (LUT) to avoid multiple boolean mask assignments, `np.clip` can incorrectly map out-of-bounds values to the maximum valid label, leading to silent misclassifications.
**Action:** Always ensure bound safety by using `np.where((arr >= 0) & (arr <= MAX_VAL), arr, 0)` before indexing the LUT to safely map out-of-bounds values to 0 (background) and prevent `IndexError`s.
