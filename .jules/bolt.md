## 2024-04-29 - Lookup Table for Pixel Mask Conversion
**Learning:** Multiple O(N) boolean mask operations inside `convert_mask` during data loading are a significant performance bottleneck.
**Action:** When performing pixel-value-to-label mapping in masks, use a NumPy lookup table (LUT) cached as a function attribute instead of multiple boolean mask assignments for better performance.
