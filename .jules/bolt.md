
## 2024-06-16 - NumPy LUT vs Multiple Boolean Masks
**Learning:** In PyTorch/NumPy dataset preprocessing, doing sequential boolean mask mapping (`new_mask[arr==100] = 1`, etc.) scales linearly with the number of classes (O(K*N)) and allocates an intermediate boolean array for each class. Using a pre-allocated Lookup Table (`lut[arr]`) is O(N) over pixels and ~5.5x faster.
**Action:** When mapping discrete label values in image masks (especially in `__getitem__` tight loops), always use a 1D NumPy LUT bounded by `np.where` for out-of-bounds safety.
