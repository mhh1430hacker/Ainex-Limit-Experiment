# AINEX Law Experiment: Detailed Methodology

## Table of Contents

1. [Research Question](#research-question)
2. [Hypothesis](#hypothesis)
3. [Experimental Design](#experimental-design)
4. [Mathematical Framework](#mathematical-framework)
5. [Implementation Details](#implementation-details)
6. [Data Pipeline](#data-pipeline)
7. [Statistical Analysis](#statistical-analysis)

---

## Research Question

**Primary Question**: Do language models lose semantic diversity when trained recursively on their own generated outputs?

**Specific Inquiry**: Can we quantify this loss using geometric measures of semantic space?

---

## Hypothesis

### Main Hypothesis (H₁)

When a language model is fine-tuned on texts it generated (rather than human-authored texts), the resulting model generates outputs that cover a smaller region of semantic space.

**Null Hypothesis (H₀)**: There is no difference in semantic space coverage between models trained on human vs. synthetic data.

### Secondary Hypotheses

1. **Convergence Hypothesis**: Repeated iterations amplify the semantic contraction effect
2. **Information Loss Hypothesis**: The model systematically loses information about the original semantic distribution
3. **Attractor Hypothesis**: The model converges to lower-dimensional attractors in semantic space

---

## Experimental Design

### Three-Stage Comparison

```
┌─────────────────────┐
│  STAGE 1: BASELINE  │
│ Human Wikipedia     │
│ Text Volume: V₀     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ STAGE 2: GEN 1      │
│ Train on V₀         │
│ Generate G₁ texts   │
│ Volume: V₁          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ STAGE 3: GEN 2      │
│ Train on G₁ only    │
│ Generate G₂ texts   │
│ Volume: V₂          │
└─────────────────────┘
```

### Metrics Computed

For each stage, we calculate:
- Semantic embeddings (via Sentence-BERT)
- Dimensionality reduction (PCA to 3D)
- Convex hull volume in reduced space
- Collapse rate: $\text{CR} = \frac{V_0 - V_2}{V_0} \times 100\%$

---

## Mathematical Framework

### Semantic Space Representation

Each text $t$ is embedded as:
$$\vec{e}_t = \text{SentenceTransformer}(t) \in \mathbb{R}^{384}$$

For a corpus $T = \{t_1, t_2, ..., t_n\}$:
$$E = [\vec{e}_{t_1}, \vec{e}_{t_2}, ..., \vec{e}_{t_n}]^T \in \mathbb{R}^{n \times 384}$$

### Dimensionality Reduction

PCA projects to 3D for computational tractability:
$$P = E \cdot U_3$$

where $U_3$ contains the first 3 principal components.

### Volume Calculation

The convex hull of projected points defines the semantic volume:
$$V = \text{ConvexHull}(P).volume$$

This metric represents the "spread" of semantically distinct ideas.

### Collapse Rate Formula

$$\text{Collapse Rate (\%)} = \frac{V_{\text{baseline}} - V_{\text{gen2}}}{V_{\text{baseline}}} \times 100$$

**Interpretation**:
- Positive CR: Semantic contraction (AINEX Law confirmed)
- Negative CR: Semantic expansion (hallucination/noise)
- CR ≈ 0: No systematic change

---

## Implementation Details

### Model Selection

**Base Model**: GPT-2 (124M parameters)
- **Rationale**: Sufficient capacity to exhibit collapse, manageable size for quick iteration
- **Alternative**: Could use GPT-Neo, BLOOM for validation

**Embedder**: Sentence-BERT (all-MiniLM-L6-v2)
- **Rationale**: Optimized for sentence-level semantic similarity
- **Alternative**: Could use OpenAI embeddings or other SentenceTransformers

### Training Configuration

| Parameter | Value | Justification |
|-----------|-------|---------------|
| **Initial Epochs** | 2 | Learn patterns without extreme overfitting |
| **Recursive Epochs** | 3 | Trigger collapse via heavy retraining |
| **Batch Size** | 8 | Stability vs. memory tradeoff |
| **Learning Rate** | 5e-5 | Standard for LLM fine-tuning |
| **Max Sequence Length** | 128 | Computational efficiency |
| **Optimization** | AdamW | Industry standard |

### Generation Configuration

| Parameter | Value | Justification |
|-----------|-------|---------------|
| **Temperature** | 0.7 | Moderate diversity (not too repetitive/random) |
| **Top-k Sampling** | 40 | Filter to top 40 tokens |
| **Repetition Penalty** | 1.1 | Discourage repetition |
| **Max Length** | 100 tokens | Long enough for semantic analysis |

---

## Data Pipeline

### Stage 1: Baseline Data Preparation

```python
# Load Wikipedia corpus
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")

# Filter criteria:
# - Minimum length: 100 characters (meaningful content)
# - Selection: First 400 texts
baseline_texts = [x['text'] for x in dataset if len(x['text']) > 100][:400]
```

**Rationale for 400 texts**:
- Sufficient for convex hull computation (>4 points in 3D)
- Manageable size for quick iteration
- Reasonable sample size for empirical testing

### Stage 2: Model Training (Generation 1)

```python
# Train on baseline texts for 2 epochs
train_model_on_texts(model, baseline_texts, epochs=2)

# Generate 400 synthetic texts
gen1_texts = generate_texts_from_model(model, num_texts=400)
```

### Stage 3: Model Training (Generation 2)

```python
# Critical: Train ONLY on generation 1 texts
# This forces recursive self-training
train_model_on_texts(model, gen1_texts, epochs=3)

# Generate 400 texts from recursively trained model
gen2_texts = generate_texts_from_model(model, num_texts=400)
```

---

## Statistical Analysis

### Variance and Uncertainty

Volume calculations have inherent variability due to:
1. Stochastic training (random initialization, shuffling)
2. Random generation (temperature sampling)
3. Embedding model approximation error

**Error Estimation** (not implemented but recommended):
- Run experiment 5+ times
- Report mean ± standard deviation
- Perform paired t-tests for statistical significance

### Confidence Intervals

For publication-quality results:

$$CI = \bar{V} \pm 1.96 \times \frac{s}{\sqrt{n}}$$

where:
- $\bar{V}$ = mean volume across runs
- $s$ = sample standard deviation
- $n$ = number of experimental runs

---

## Expected Outcomes

### Scenario 1: AINEX Law Confirmed (Most Likely)

- V₁ < V₀ (initial slight decrease)
- V₂ << V₁ (dramatic decrease after recursion)
- Collapse Rate: 10-40%
- **Interpretation**: Semantic contraction through recursive training confirmed

### Scenario 2: Hallucination Pattern

- V₀ ≈ V₁ (similar to baseline)
- V₂ > V₁ (expansion)
- Collapse Rate: Negative (-5% to -20%)
- **Interpretation**: Model generates random/incoherent outputs rather than contracting

### Scenario 3: No Effect

- V₀ ≈ V₁ ≈ V₂
- Collapse Rate: Near 0%
- **Interpretation**: Model maintains semantic stability (possible causes: large capacity, short training, noise in metric)

---

## Limitations and Caveats

### Known Limitations

1. **Corpus Size**: 400 texts is relatively small; results may not generalize to larger corpora
2. **Single Model**: Only GPT-2; other architectures may behave differently
3. **Language**: English only; multilingual effects unknown
4. **Metric Approximation**: Convex hull volume has computational/sampling errors
5. **Discrete Sampling**: PCA to 3D loses ~20% of variance information

### Potential Confounds

- Tokenizer effects (BPE-based tokenization may affect generation)
- Embedding model biases (Sentence-BERT has its own semantic assumptions)
- Random seed effects (results may vary between runs)
- Fine-tuning hyperparameter sensitivity

### Recommendations for Future Work

1. Replicate with multiple model sizes (125M, 1B, 7B parameters)
2. Test with other architectures (T5, BERT, modern LLMs)
3. Increase corpus size to 1000+ texts
4. Implement statistical significance testing (multiple runs)
5. Analyze semantic direction changes (not just volume)
6. Measure information-theoretic metrics (entropy, divergence)

---

## Validation Checklist

Before accepting results:

- [ ] Both training stages complete without errors
- [ ] Generation produces coherent (not all gibberish) text
- [ ] All three volumes are computed (non-zero)
- [ ] Generation 2 volume is reasonable (same order of magnitude as baseline)
- [ ] Collapse rate is within expected range (-100% to +100%)
- [ ] Results are logged and reproducible

---

## Reproducibility

### Random Seeds

For full reproducibility, set:

```python
import random
import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
```

### System Information to Report

- Python version
- PyTorch version
- CUDA version (if applicable)
- GPU model (if used)
- Execution date and time
- Total runtime

---

## References

### Theoretical Background

- Information Theory: Shannon entropy in semantic space
- Dimensionality Reduction: PCA variance explanation
- Computational Geometry: Convex hull algorithms

### Related Empirical Studies

- Model collapse in diffusion models (Shumailov et al., 2023)
- Synthetic data degradation in iterative learning
- Language model mode coverage and mode collapse
