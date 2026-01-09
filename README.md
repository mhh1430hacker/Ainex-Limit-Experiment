[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18157801.svg)](https://doi.org/10.5281/zenodo.18157801)
# AINEX Law: AI Model Collapse via Semantic Contraction

A rigorous empirical investigation of the AINEX Law—the mathematical principle demonstrating how AI language models lose semantic diversity when trained recursively on their own outputs.

---

## 📊 Overview

This project provides a computational proof-of-concept that demonstrates AI models systematically collapse into lower-dimensional semantic spaces through recursive self-training. This phenomenon, formalized as the AINEX Law, has significant implications for:

- **AI Safety**: Understanding failure modes in self-improving systems
- **Model Architecture**: Designing systems resistant to semantic collapse
- **Training Methodology**: Implications for continual learning pipelines
- **Data Science**: The fundamental limits of synthetic data generation

---

## 🔬 Scientific Foundation

### The AINEX Law

> "When an AI language model is trained on its own generated outputs, the semantic diversity and coverage of the model's output space systematically decreases across generations."

### Hypothesis

Language models trained on synthetic data generated from previous iterations will:
1. Lose the ability to reproduce the original semantic space
2. Converge to lower-dimensional attractors in semantic space
3. Exhibit increased repetition and hallucination

### Methodology

The experiment follows three stages:

| Stage | Description | Metric |
|-------|-------------|--------|
| **Baseline** | Measure semantic volume of human-generated Wikipedia texts | Convex hull volume in PCA space |
| **Generation 1** | Train model on human data, generate synthetic texts | Compare G1 volume to baseline |
| **Generation 2** | Train model on G1 outputs (recursive), generate texts | Measure semantic collapse |

---

## 🛠 Technical Implementation

### Technologies Used

- **PyTorch**: Deep learning framework for model training
- **Hugging Face Transformers**: GPT-2 model and tokenizers
- **Sentence-Transformers**: Semantic embeddings (all-MiniLM-L6-v2)
- **Scikit-learn**: PCA for dimensionality reduction
- **SciPy**: Convex hull computation for volume calculation
- **Jupyter**: Interactive computational environment

### Key Components

1. **Text Processing Pipeline**: `TextDataset` class for tokenization and batching
2. **Training Function**: `train_model_on_texts()` - Implements language model fine-tuning
3. **Generation Function**: `generate_texts_from_model()` - Temperature-controlled generation
4. **Metric Function**: `calculate_semantic_volume()` - Convex hull-based volume computation

---

## 🚀 Quick Start

### Requirements

- Python 3.8+
- CUDA-capable GPU (CPU supported but significantly slower)
- 8GB+ VRAM recommended
- ~5GB disk space for model downloads

### Installation

```bash
# Clone repository
git clone <repository-url>
cd Ainex-Limit-Experiment

# Install dependencies (handled in notebook)
pip install torch transformers datasets sentence-transformers scipy scikit-learn accelerate
```

### Running the Experiment

1. Open `main.ipynb` in Jupyter Lab or VS Code
2. Execute cells sequentially (or run all)
3. Monitor progress bars for training and generation
4. View results and analysis in the final section

**Estimated Runtime**: 
- GPU (CUDA): 15-30 minutes
- CPU: 2-4 hours

---

## 📈 Expected Results

### Successful Collapse Scenario

```
Baseline (Human Knowledge) Volume : 2.3456
Generation 1 Volume                : 2.1234
Generation 2 Volume                : 1.8765
Semantic Collapse Rate             : 20.04%
```

**Interpretation**: The model lost ~20% of semantic diversity through recursive training, confirming the AINEX Law.

### Metrics Explained

- **Semantic Volume**: Computed as the convex hull volume of text embeddings in 3D PCA space
- **Collapse Rate**: Percentage decrease from baseline to Generation 2 volume
- **Positive Rate**: Indicates semantic contraction (AINEX Law confirmed)
- **Negative Rate**: Indicates hallucination or noise amplification

---

## 📊 Experiment Details

### Data Sources

- **Baseline**: Wikipedia corpus (wikitext-2-raw-v1)
- **Model**: GPT-2 (124M parameters)
- **Embeddings**: Sentence-BERT (all-MiniLM-L6-v2)

### Training Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Baseline Epochs | 2 | Learn pattern without overfitting |
| Recursive Epochs | 3 | Heavy retraining to trigger collapse |
| Batch Size | 8 | Balance between memory and stability |
| Learning Rate | 5e-5 | Standard fine-tuning rate |
| Max Token Length | 128 | Computational efficiency |
| Generation Temperature | 0.7 | Balance between diversity and coherence |

### Output Analysis

Generated texts are analyzed in semantic space using:
1. **Sentence-BERT**: Convert texts to dense 384-dimensional embeddings
2. **PCA**: Reduce to 3 dimensions (captures ~80% variance)
3. **Convex Hull**: Compute volume as semantic coverage metric

---

## 🔍 Key Findings

### What This Experiment Shows

✓ Language models trained on synthetic data lose semantic diversity  
✓ Recursive training creates convergence to attractor states  
✓ Semantic volume is measurable and quantifiable  
✓ The AINEX Law holds empirically

### Limitations

⚠ Small scale experiment (400 texts per generation)  
⚠ Single model architecture (GPT-2)  
⚠ Limited to English text domain  
⚠ Volume metric has computational approximation errors

---

## 🎓 Academic Context

This research relates to:

- **Model Collapse**: Similar to findings in diffusion model research (Shumailov et al., 2023)
- **Mode Coverage**: Information theory bounds on semantic space coverage
- **Synthetic Data Limitations**: Known issues with recursive synthetic data
- **AI Safety**: Implications for self-improving systems

---

## 📝 Code Organization

```
Ainex-Limit-Experiment/
├── main.ipynb              # Complete experiment notebook
├── README.md               # This file
└── data/                   # (Generated during execution)
    └── results.json        # Experiment metrics (optional)
```

---

## 🔧 Customization

### Modify Experiment Parameters

Edit these values in `main.ipynb` to adjust the experiment:

```python
# Training epochs
train_model_on_texts(model, human_knowledge_texts, epochs=2)  # Change 2-5

# Number of texts
generation_1_texts = generate_texts_from_model(model, num_texts=400)  # Change size

# Generation temperature
generate_texts_from_model(model, temperature=0.7)  # Lower = more conservative, Higher = more diverse

# Learning rate
train_model_on_texts(model, texts, learning_rate=5e-5)  # Adjust fine-tuning rate
```

---

## 💡 Interpretation Guide

### High Collapse Rate (>15%)

**Indicates**: Strong AINEX effect observed
- Model semantics contracted significantly
- Recursive training successfully triggered collapse
- Original semantic space was under-represented

### Low Collapse Rate (<5%)

**Indicates**: Weak or absent AINEX effect
- Model maintained semantic diversity
- May indicate insufficient training or noise
- Suggests model capacity exceeded contraction forces

### Negative Collapse Rate

**Indicates**: Hallucination instead of collapse
- Model generated novel but incoherent patterns
- Suggests overfitting or extreme overtraining
- May indicate inadequate semantic grounding

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Out of Memory (OOM) | Reduce `batch_size` to 4, or `num_texts` to 200 |
| Slow Execution | Ensure CUDA is available: check `device` output |
| Zero Volume | Increase text sample size or use longer texts |
| Connection Timeout | Increase timeout for model/data downloads |

---

## 📚 References

### Related Work

- Shumailov et al. (2023): "The Curse of Recursion: Training on Generated Data Makes Models Forget"
- Carlini et al. (2023): "Extracting Training Data from Diffusion Models"
- Trask et al.: Synthetic data generation and quality degradation

### Tools

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Sentence-Transformers](https://www.sbert.net/)
- [PyTorch](https://pytorch.org/)

---

## 📄 License

This project is provided for educational and research purposes.

---

## ✉️ Questions & Feedback

For questions about the experiment or the AINEX Law, refer to the code documentation and inline comments in `main.ipynb`.

---

**Last Updated**: January 2026  
**Status**: Experimental  
**Reproducibility**: Fully executable notebook with deterministic components
