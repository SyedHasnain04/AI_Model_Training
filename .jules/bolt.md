## 2025-02-28 - Optimize mask conversion with NumPy LUT
**Learning:** Using a NumPy lookup table (LUT) cached as a function attribute is significantly faster (~4.8x speedup) than sequential boolean masking (`new_mask[arr==val]=mapped_val`) for mapping pixel values to labels in segmentation masks.
**Action:** Always prefer LUT over multiple boolean masks for discrete value mapping in NumPy when the range of input values is reasonably small (e.g., up to 10000). Ensure bound safety by clamping/filtering out-of-bounds inputs to avoid `IndexError`.
