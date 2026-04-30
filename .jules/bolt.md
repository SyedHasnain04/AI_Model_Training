## 2026-04-30 - Optimize convert_mask
**Learning:** Using a cached NumPy LUT for pixel mappings in masks avoids multiple boolean mask assignments and provides O(1) performance.
**Action:** Use cached NumPy LUTs instead of multiple boolean assignments when mapping pixel values in segmentation masks.
