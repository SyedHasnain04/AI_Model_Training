## 2025-05-06 - [LUT for image mask conversion]
 **Learning:** In semantic segmentation models, mapping discrete pixel values to class indices in data loaders happens per-image per-epoch. Converting a series of boolean masks (e.g. `new_mask[arr==100]=1`) creates intermediate boolean arrays for every mapped class.
 **Action:** For performance, use a pre-allocated lookup table (LUT) mapping possible pixel values to output labels, indexing into the array. This provides a ~6x speedup. Ensure the array indices are valid using `np.where` before indexing.
