## 2024-04-24 - Jupyter Notebook Update Encoding
**Learning:** When using python's `json` module to update `.ipynb` files, `json.dump` by default escapes non-ascii characters (like invisible characters). This causes noisy, non-functional git diffs across the entire file.
**Action:** Always use `json.dump(nb, f, indent=2, ensure_ascii=False)` to write notebooks correctly without modifying the encoding of unrelated cells.

## 2024-04-24 - Compiled Python Files
**Learning:** Ad-hoc python scripts for testing generate `__pycache__` directories.
**Action:** Be absolutely certain to remove ad-hoc testing scripts and their associated `__pycache__` or `.pytest_cache` directories before creating commits or PRs to avoid polluting the git history.
