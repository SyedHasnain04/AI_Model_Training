
## 2024-06-08 - Fast semantic segmentation mask mapping
**Learning:** In segmentation tasks, applying multiple boolean masks to map pixel values to class indices (e.g., `new_mask[arr==100]=1`) is O(N*C) where N is number of pixels and C is number of classes. It causes significant CPU overhead during data loading in PyTorch datasets because it creates a new boolean array and indexes the mask for every single class.
**Action:** When performing pixel-value-to-label mapping in masks, use a NumPy lookup table (LUT) cached as a function attribute instead of multiple boolean mask assignments for better performance. Ensure bound safety by using `np.where((arr >= 0) & (arr <= MAX_VAL), arr, 0)` before indexing the LUT to safely map out-of-bounds values to 0 (background).
