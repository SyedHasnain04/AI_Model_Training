
## 2024-05-19 - Fast Pixel-to-Label Conversion in Image Segmentation
**Learning:** In segmentation masks, boolean indexing to replace pixel values (e.g. `mask[arr==100]=1`) is very slow due to creating intermediate boolean arrays and iterating over the image multiple times.
**Action:** Use a Lookup Table (LUT) mapping possible pixel values directly to labels and index into it. For safety with out-of-bounds pixels, clip/where the input array to `[0, MAX_LUT_SIZE]` before indexing.

## 2024-05-19 - Efficient mIoU Calculation in PyTorch
**Learning:** Calculating Intersection over Union (IoU) using a loop over classes and boolean operations (e.g. `(pred==cls) & (mask==cls)`) is an O(N_classes * Image_Size) operation and is very slow.
**Action:** Use `torch.bincount` on 1D representations of `mask * num_classes + pred` to compute the entire confusion matrix in one O(Image_Size) vectorized pass.
