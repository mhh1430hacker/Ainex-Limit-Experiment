# Security Policy

## ⚠️ Critical Warning

This repository contains research code designed to induce **Model Collapse** and **Semantic Decay**. 
Executing this loop on production models without proper isolation may result in irreversible weight degradation.

**Use with caution.**

## Supported Versions

| Version | Supported          | Notes |
| ------- | ------------------ | ----- |
| 1.x     | :white_check_mark: | Active Research |
| < 1.0   | :x:                | Deprecated |

## Reporting a Vulnerability

### What is NOT a vulnerability?
Since the goal of **The Ainex Limit** is to prove semantic instability:
* **Hallucinations:** If the model starts outputting nonsense (e.g., "crocodiles are physics"), this is **intended behavior**, not a bug.
* **High Perplexity:** Sudden spikes in perplexity are expected outcomes of the singularity point.

### What IS a vulnerability?
Please report:
1.  Remote Code Execution (RCE) flaws in the python scripts.
2.  Errors in the geometric calculation formulas (PCA/Convex Hull) that skew the scientific data.

### How to Report
Please report sensitive security issues via email to: **mahdi1430hacker@gmail.com**
For standard bugs, please open a GitHub Issue with the label `bug`.
