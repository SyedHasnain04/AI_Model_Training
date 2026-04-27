## 2025-05-19 - Use Numpy LUT for mask mapping
**Learning:** In the `randoms_(1).ipynb` notebook, the `convert_mask` function takes raw mask tensors and converts them into classification indices by doing repeated boolean indexing like `new_mask[arr==100]=1`. For large images, these repeated boolean array creations and assignments form a bottleneck.
**Action:** When performing pixel-value-to-label mapping in masks, use a NumPy lookup table (LUT) cached as a function attribute instead of multiple boolean mask assignments for better performance.
