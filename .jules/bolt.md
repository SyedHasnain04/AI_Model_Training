## 2025-05-19 - Fast Mask Conversion
**Learning:** In segmentation tasks (like `convert_mask` in this codebase), using a NumPy Lookup Table (LUT) is dramatically faster (about 7.7x speedup) compared to doing multiple boolean mask assignments (`new_mask[arr==val] = cls`) for pixel value mapping.
**Action:** When performing pixel value replacement on large arrays/masks, always look for opportunities to replace boolean indexing chains with a pre-computed lookup table array (LUT).
