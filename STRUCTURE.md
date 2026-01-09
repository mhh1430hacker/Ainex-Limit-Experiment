# Project Structure

```
Ainex-Limit-Experiment/
│
├── 📄 README.md                 # Main project documentation (start here)
│
├── 📄 QUICKSTART.md             # Quick start guide for running the experiment
│
├── 📄 METHODOLOGY.md            # Detailed research methodology and theory
│
├── 📄 INSTALLATION.md           # Installation and environment setup
│
├── 📓 main.ipynb                # Main experiment notebook (fully executable)
│   ├── Section 1: Library Installation
│   ├── Section 2: Model and Data Loading
│   ├── Section 3: Data Processing Classes
│   ├── Section 4: Core Functions
│   ├── Section 5: AINEX Experiment Execution
│   └── Section 6: Results Analysis
│
└── 📁 docs/ (optional)          # Additional documentation
    ├── CONTRIBUTING.md          # How to contribute
    ├── FAQ.md                   # Frequently asked questions
    └── REFERENCES.md            # Academic references
```

## File Descriptions

### Core Files

| File | Purpose | Audience |
|------|---------|----------|
| **README.md** | Comprehensive project overview, results interpretation, and technical details | Everyone (start here) |
| **main.ipynb** | Complete, executable experiment in Jupyter notebook format | Researchers, practitioners |
| **QUICKSTART.md** | Step-by-step guide to run the experiment and interpret results | First-time users |
| **METHODOLOGY.md** | Detailed scientific methodology, hypotheses, and mathematical framework | Academic researchers |
| **INSTALLATION.md** | Environment setup, dependency installation, and troubleshooting | Technical users |

### Organization Principles

- **Single notebook design**: All code in `main.ipynb` for easy execution and modification
- **Multiple documentation layers**: 
  - Quick access (README summary)
  - User guide (QUICKSTART)
  - Deep dive (METHODOLOGY)
- **Self-contained**: No external scripts needed; all functionality in one notebook
- **Reproducibility**: Clear organization enables exact replication

---

## How to Use This Repository

### For Quick Understanding
1. Read [README.md](README.md) - Section "Overview"
2. See expected results in README - Section "Expected Results"

### To Run the Experiment
1. Follow [INSTALLATION.md](INSTALLATION.md)
2. Open and execute [main.ipynb](main.ipynb)
3. Check results in the final notebook cells

### To Understand the Science
1. Read [README.md](README.md) - Sections "Scientific Foundation"
2. Deep dive into [METHODOLOGY.md](METHODOLOGY.md)
3. Examine code comments in [main.ipynb](main.ipynb)

### To Modify the Experiment
1. Read [QUICKSTART.md](QUICKSTART.md) - Section "Customization Guide"
2. Edit parameters in [main.ipynb](main.ipynb)
3. Run modified cells to observe differences

---

## Document Navigation

### Quick Links by Question

**"What is this project about?"**
→ [README.md - Overview](README.md#-overview)

**"How do I run this?"**
→ [QUICKSTART.md - Running the Experiment](QUICKSTART.md#-running-the-experiment)

**"What should I install?"**
→ [INSTALLATION.md](INSTALLATION.md)

**"What are the results?"**
→ [README.md - Expected Results](README.md#-expected-results)

**"How do I interpret the metrics?"**
→ [QUICKSTART.md - Understanding the Metrics](QUICKSTART.md#-understanding-the-metrics)

**"What's the scientific basis?"**
→ [METHODOLOGY.md - Mathematical Framework](METHODOLOGY.md#mathematical-framework)

**"Something's broken, help!"**
→ [QUICKSTART.md - Troubleshooting](QUICKSTART.md#-troubleshooting)

**"How can I customize it?"**
→ [QUICKSTART.md - Customization Guide](QUICKSTART.md#-customization-guide)

---

## Notebook Structure

The `main.ipynb` notebook is organized into clear sections:

### Section 1: Installation & Imports (≈1 min)
- Installs required packages
- Imports all necessary libraries
- Verifies GPU availability

### Section 2: Model Loading (≈2 min)
- Loads GPT-2 model and tokenizer
- Loads Sentence-BERT embedder
- Downloads Wikipedia dataset

### Section 3: Data Processing (≈1 min)
- Defines `TextDataset` class
- Prepares 400 Wikipedia texts
- Displays sample texts

### Section 4: Core Functions (≈0 min)
- `train_model_on_texts()`: Fine-tune model on texts
- `generate_texts_from_model()`: Generate synthetic texts
- `calculate_semantic_volume()`: Compute semantic coverage metric

### Section 5: Experiment (≈20 min)
- **Baseline**: Measure human knowledge volume
- **Generation 1**: Train on human data, generate synthetic
- **Generation 2**: Train on synthetic data, generate final texts

### Section 6: Results (≈1 min)
- Display metrics
- Calculate collapse rate
- Provide interpretation

**Total Runtime**: 
- GPU: 15-30 minutes
- CPU: 2-4 hours

---

## Code Quality Features

✅ **Well-commented**: Every function has docstrings  
✅ **Type hints**: (Python 3.9+) Enhanced readability  
✅ **Error handling**: Graceful failures with informative messages  
✅ **Progress bars**: Visual feedback during long operations  
✅ **Modularity**: Reusable functions for custom modifications  
✅ **Reproducibility**: Deterministic components where possible  

---

## Git Repository Structure

```bash
# Clone the repository
git clone <repository-url>
cd Ainex-Limit-Experiment

# Main branch contains production-ready code
# Experiment freely in your own branches
git checkout -b my-experiments
```

---

## Extending the Project

### Adding New Experiments

1. Create a new notebook: `experiment_variant.ipynb`
2. Import classes from `main.ipynb` or copy and modify
3. Run new experiment and compare results
4. Document findings in a new `.md` file

### Parallel Runs

```python
# Run multiple experiments in parallel (if you have multiple GPUs)
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def run_single_experiment(seed):
    # Run experiment with different random seed
    set_seed(seed)
    return run_ainex_experiment()

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(run_single_experiment, range(5)))
```

### Integration with Other Tools

- **MLflow**: Add experiment tracking
- **Weights & Biases**: Log metrics and artifacts
- **DVC**: Version control large data files
- **Docker**: Containerize for reproducibility

---

## Citation

If you use this project in your research, please cite:

```bibtex
@software{ainex2024,
  title={AINEX Law: AI Model Collapse via Semantic Contraction},
  author={Your Name},
  year={2024},
  url={https://github.com/yourusername/Ainex-Limit-Experiment}
}
```

---

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on:
- Reporting bugs
- Suggesting features
- Contributing code improvements
- Adding experiments

---

## License

This project is released under [specify license - MIT, Apache 2.0, etc.]

---

**Last Updated**: January 2026  
**Status**: Active Development  
**Maintained by**: [Your Name/Organization]
