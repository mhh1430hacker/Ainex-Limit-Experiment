# Project Information

**Project Name**: AINEX Law: AI Model Collapse via Semantic Contraction  
**Current Version**: 1.0.0  
**Last Updated**: January 2026  
**Status**: Active Development  

---

## 📋 Quick Summary

This project provides a computational demonstration that language models lose semantic diversity when trained recursively on their own outputs—a phenomenon formalized as the AINEX Law.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Main Notebook** | 1 (main.ipynb) |
| **Documentation Files** | 7 |
| **Core Functions** | 3 |
| **Dependencies** | 8 |
| **Expected Runtime** | 15-30 min (GPU) / 2-4h (CPU) |
| **Model Parameters** | 124M (GPT-2) |
| **Text Samples** | 400 per generation |
| **Embedding Dimension** | 384 (reduced to 3D for analysis) |

---

## 🎯 Core Concept

### The Hypothesis

> Language models trained on synthetic data generated from previous iterations will demonstrate:
> 1. Loss of semantic diversity
> 2. Convergence to lower-dimensional attractors
> 3. Increased repetition and degeneration

### The Metric

**Semantic Volume** (V): Computed as the convex hull volume of text embeddings in PCA-reduced space

**Collapse Rate**: Percentage decrease from baseline to second generation

$$\text{Collapse Rate} = \frac{V_{\text{baseline}} - V_{\text{generation 2}}}{V_{\text{baseline}}} \times 100\%$$

---

## 📂 Repository Contents

### Documentation Hierarchy

```
Level 1: START HERE
├─ README.md (comprehensive overview)
└─ QUICKSTART.md (practical guide)

Level 2: TECHNICAL DETAILS
├─ METHODOLOGY.md (scientific framework)
├─ INSTALLATION.md (setup instructions)
└─ STRUCTURE.md (file organization)

Level 3: ENGAGEMENT
├─ docs/CONTRIBUTING.md (how to contribute)
└─ docs/FAQ.md (common questions)

Level 4: EXECUTION
└─ main.ipynb (the actual experiment)
```

### File Directory Tree

```
Ainex-Limit-Experiment/
├── README.md                    # Main documentation (2,500+ words)
├── QUICKSTART.md                # Beginner's guide (2,000+ words)
├── METHODOLOGY.md               # Research methodology (2,000+ words)
├── INSTALLATION.md              # Setup guide (1,500+ words)
├── STRUCTURE.md                 # File organization guide (500 words)
├── .gitignore                   # Git ignore rules
├── main.ipynb                   # Experiment notebook (fully executable)
└── docs/
    ├── CONTRIBUTING.md          # Contribution guidelines (1,500+ words)
    ├── FAQ.md                   # FAQs (1,500+ words)
    └── PROJECT_INFO.md          # This file
```

---

## 🔧 Technology Stack

### Core Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **PyTorch** | ≥2.0.0 | Deep learning framework |
| **Transformers** | ≥4.30.0 | Language models (GPT-2) |
| **Sentence-Transformers** | ≥2.2.0 | Semantic embeddings |
| **Scikit-learn** | ≥1.3.0 | PCA dimensionality reduction |
| **SciPy** | ≥1.10.0 | Convex hull computation |
| **NumPy** | ≥1.24.0 | Numerical computations |
| **Datasets** | ≥2.10.0 | Wikipedia corpus loading |
| **Jupyter** | ≥1.0.0 | Interactive notebook environment |

### Development Tools

- **Black**: Code formatting
- **Flake8**: Code linting  
- **pytest**: Testing framework
- **Git**: Version control
- **GitHub**: Repository hosting

---

## 🚀 Quick Start Paths

### Path 1: Just Run It (5 minutes)
1. Install: `pip install -r requirements.txt`
2. Open: `jupyter lab main.ipynb`
3. Execute: Run all cells
4. View: Check final results section

### Path 2: Understand First (30 minutes)
1. Read: [README.md](README.md) Overview
2. Review: [QUICKSTART.md](QUICKSTART.md) Section 2
3. Run: [main.ipynb](main.ipynb)
4. Interpret: [QUICKSTART.md](QUICKSTART.md) Section 5

### Path 3: Deep Dive (2 hours)
1. Read: All documentation files in order
2. Study: [METHODOLOGY.md](METHODOLOGY.md) thoroughly
3. Run: [main.ipynb](main.ipynb) cell by cell
4. Experiment: Modify parameters and observe changes

### Path 4: Contribute (varies)
1. Fork: GitHub fork button
2. Read: [CONTRIBUTING.md](docs/CONTRIBUTING.md)
3. Create: Feature branch
4. Submit: Pull request with your improvements

---

## 📊 Experiment Stages

### Stage 1: Baseline Measurement
- **Input**: Wikipedia texts (400 samples)
- **Process**: Embed and compute semantic volume
- **Output**: V₀ (baseline volume)
- **Duration**: ~2 minutes

### Stage 2: First Generation
- **Input**: Baseline texts (400)
- **Process**: Train model for 2 epochs, generate 400 texts
- **Output**: V₁ (generation 1 volume)
- **Duration**: ~10 minutes

### Stage 3: Recursive Training
- **Input**: Generation 1 texts (400)
- **Process**: Train model for 3 epochs on own outputs, generate texts
- **Output**: V₂ (generation 2 volume)
- **Duration**: ~10 minutes

### Stage 4: Analysis
- **Input**: V₀, V₁, V₂
- **Process**: Calculate collapse rate and metrics
- **Output**: Interpretation of AINEX Law
- **Duration**: ~1 minute

---

## 💡 Key Innovation

### What Makes This Special

1. **Quantifiable**: Turns linguistic phenomenon into geometric measurement
2. **Reproducible**: Clear methodology, fully documented
3. **Extensible**: Easy to modify and experiment with
4. **Interpretable**: Results have clear semantic meaning
5. **Educational**: Suitable for learning and research

### Novelty Aspects

- Applies convex hull geometry to semantic collapse
- Demonstrates model degradation through measurable metric
- Connects to broader model collapse literature
- Provides testbed for mitigation strategies

---

## 📈 Expected Outcomes

### Success Scenario (Most Likely)

```
Results:
  Baseline: 2.34
  Gen 1:    2.15 (-8% vs baseline)
  Gen 2:    1.87 (-20% vs baseline)
  
Interpretation: ✅ AINEX Law Confirmed
```

### Alternative Scenarios

**Hallucination** (-5% to -20%): Model generates novel but incoherent text  
**No Effect** (±5%): Model maintains semantic stability  
**Expansion** (<-20%): Possible outlier or extreme overtraining  

---

## 🔍 Reproducibility

### Deterministic Components

- Model architecture (GPT-2)
- Dataset source (Wikipedia)
- Embedding model (Sentence-BERT)
- Mathematical procedures (PCA, convex hull)

### Stochastic Components

- Random weight initialization
- Data shuffling in training
- Temperature-based generation
- Embedding model internal randomness

### Controlling Randomness

```python
import random, numpy as np, torch
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
```

---

## 🎓 Learning Outcomes

After completing this project, you will understand:

✅ How language models are fine-tuned  
✅ Semantic embeddings and their computation  
✅ Dimensionality reduction techniques  
✅ Computational geometry (convex hull)  
✅ Model degradation through iteration  
✅ Implications for AI safety and data quality  

---

## 🔗 Related Concepts

### Academic References

- **Model Collapse**: Shumailov et al. (2023)
- **Mode Collapse**: Goodfellow et al. (2014) [GANs]
- **Semantic Space**: Distributional semantics
- **Convex Geometry**: Computational geometry

### Practical Applications

- Synthetic data quality assessment
- Continual learning system design
- Model safety evaluation
- Data augmentation strategy validation

---

## 🚀 Future Extensions

### Potential Research Directions

1. **Multi-Model Study**: Test with GPT-Neo, BLOOM, LLaMA
2. **Scaling Laws**: How does collapse scale with model size?
3. **Mitigation Strategies**: Data augmentation, regularization
4. **Theoretical Analysis**: Mathematical bounds on semantic volume
5. **Multilingual**: Does AINEX Law hold across languages?
6. **Domain-Specific**: Compare technical vs. creative text

### Possible Enhancements

- [ ] Statistical significance testing (5+ runs)
- [ ] Visualization of semantic space
- [ ] Interactive parameter exploration
- [ ] Automated report generation
- [ ] MLflow integration for tracking
- [ ] Distributed training support

---

## 📞 Support and Contact

### Documentation Lookup

| Question | Document |
|----------|----------|
| "How do I run this?" | [QUICKSTART.md](QUICKSTART.md) |
| "What are the results?" | [README.md](README.md) |
| "How does it work?" | [METHODOLOGY.md](METHODOLOGY.md) |
| "I need to install it" | [INSTALLATION.md](INSTALLATION.md) |
| "Something's broken" | [QUICKSTART.md - Troubleshooting](QUICKSTART.md#-troubleshooting) |
| "I want to contribute" | [CONTRIBUTING.md](docs/CONTRIBUTING.md) |
| "I have a question" | [FAQ.md](docs/FAQ.md) |

### Getting Help

1. **Documentation**: Check relevant .md file
2. **Search**: Look in FAQ.md for your question
3. **Issues**: GitHub Issues for bugs/features
4. **Discussions**: GitHub Discussions for questions
5. **Code**: Read inline comments in main.ipynb

---

## 📄 License

This project is provided for educational and research purposes.

---

## 🙏 Acknowledgments

This project builds on:
- Hugging Face Transformers library
- Sentence-Transformers research
- PyTorch deep learning framework
- SciPy scientific computing

---

## 🎉 Getting Started

### For Impatient Users (5 minutes)

```bash
# 1. Setup
pip install -r requirements.txt

# 2. Run
jupyter lab main.ipynb
# Execute all cells

# 3. Observe
# Check final section for results
```

### For Thorough Users (1 hour)

```bash
# 1. Study
# Read README.md and QUICKSTART.md

# 2. Setup
# Follow INSTALLATION.md carefully

# 3. Run
# Execute main.ipynb step by step
# Study code and comments

# 4. Experiment
# Modify parameters and observe effects

# 5. Reflect
# Read METHODOLOGY.md to understand theory
```

---

## 📊 Project Metrics

| Metric | Value |
|--------|-------|
| **Total Documentation** | 10,000+ words |
| **Code Comments** | 100+ lines |
| **Examples** | 20+ code snippets |
| **Diagrams** | 5+ technical diagrams |
| **Estimated Learning Time** | 2-3 hours |
| **Estimated Runtime** | 15-30 min (GPU) |

---

## 🔄 Versioning

### Current Version: 1.0.0

- **Status**: Stable
- **Last Updated**: January 2026
- **Tested On**: Python 3.10+, CUDA 12.0+, PyTorch 2.0+

### Version History

| Version | Date | Status |
|---------|------|--------|
| 1.0.0 | Jan 2026 | 🟢 Stable |
| 0.9.0 | Dec 2025 | 🟡 Beta |
| 0.1.0 | Nov 2025 | 🔴 Alpha |

---

## ✨ Project Highlights

✅ **Fully Executable**: One-click run in Jupyter  
✅ **Well Documented**: 10,000+ words of guides  
✅ **Production Ready**: Clean, tested code  
✅ **Extensible**: Easy to modify and experiment  
✅ **Educational**: Great for learning NLP concepts  
✅ **Research Quality**: Suitable for academic work  

---

**Welcome to the AINEX Law experiment!** 🚀

Start with [README.md](README.md) or jump straight to [QUICKSTART.md](QUICKSTART.md).

Questions? Check [FAQ.md](docs/FAQ.md) or open a GitHub Issue.

Ready to contribute? See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

Happy experimenting! 🎓
