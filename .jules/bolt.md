## 2024-06-02 - Vectorized mIoU Calculation
**Learning:** In PyTorch, iteratively calculating Intersection over Union (IoU) class-by-class using boolean masks in Python `for` loops is highly inefficient because it prevents parallelization on GPUs and incurs high Python-C++ boundary overhead.
**Action:** Replace Python loops with a vectorized confusion matrix calculation using `torch.bincount` to leverage low-level C++/CUDA operations, making metric computation significantly faster, particularly during evaluation and training loops on large segmentation masks.
