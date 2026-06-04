## 2024-XX-XX - Pixel Label Mapping Optimization
**Learning:** In the Offroad Segmentation project, the `convert_mask` function used 10 separate boolean mask assignments (e.g., `new_mask[arr==100]=1`) which iterates over the entire image multiple times.
**Action:** Replace multiple boolean mask assignments with a single NumPy Lookup Table (LUT) mapping (cached as a function attribute) and an element-wise mapping array via `np.where`.
