## 2024-04-25 - [Jupyter Notebook LUT Performance Optimization]
**Learning:** Found an $O(K \cdot N)$ bottleneck when mapping mask labels inside `convert_mask()` functions in notebooks, replacing multiple boolean masking operations.
**Action:** Replace multiple mask indexing assignments with an O(N) cached lookup table (LUT). Make sure to safely type cast the input array (`arr = np.array(mask).astype(np.int32)`) and consider bounds (`np.clip(arr, 0, 10000)`) to ensure indexing works and no out-of-bounds indices are fetched from the LUT.
