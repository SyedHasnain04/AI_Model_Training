
## 2024-10-25 - Lookup Table in Jupyter Notebooks
**Learning:** In Jupyter Notebooks, optimizing heavily called functions like `convert_mask` via function attributes (e.g., `convert_mask.lut = lut`) effectively creates an extremely fast O(1) Look-Up Table cache that persists across repeated calls. This avoids repetitive costly Boolean mask instantiations.
**Action:** When a function repeatedly maps specific integers to other integers, implement an array LUT cached as a function attribute and boundary-check (`np.where`) input arrays to guarantee fast execution without `IndexError`.
