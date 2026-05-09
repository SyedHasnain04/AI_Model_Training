
## 2024-05-18 - Optimize pixel mapping for semantic segmentation masks
**Learning:** In PyTorch/NumPy computer vision pipelines (like offroad semantic segmentation), sequential boolean assignment operations to map dense pixel values to discrete class labels (`new_mask[arr==100]=1`) create an O(N*C) bottleneck.
**Action:** Replace sequential boolean assignments with a cached O(1) NumPy lookup table (LUT) function attribute. Bound the array safely with `np.where` before indexing to prevent `IndexError` when values are outside the LUT dimensions.
