## 2024-05-14 - Optimize Semantic Segmentation Mask Mapping

**Learning:** When performing pixel-value-to-label mapping in masks (e.g., in `convert_mask`), using a NumPy lookup table (LUT) cached as a function attribute is significantly faster than using multiple boolean mask assignments.
**Action:** Use a NumPy LUT and cache it as a function attribute to avoid recomputing it. Use `np.where` to safely map out-of-bounds values to 0 (background) and prevent `IndexError`s.
