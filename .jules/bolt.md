## 2025-02-14 - Lookup Table for Mask Conversion
**Learning:** When converting semantic segmentation masks with multiple sparse pixel values to contiguous class indices, using multiple boolean mask assignments (e.g. `mask[arr==100] = 1`) takes ~0.89s per 100 images, whereas a cached NumPy lookup table (LUT) array takes ~0.10s per 100 images (an 8x speedup). This prevents redundant array traversals for each class.
**Action:** Use cached NumPy lookup tables (e.g., `hasattr` caching) for fast pixel-value-to-label mappings in dataset preprocessing rather than repeated boolean array assignments.
