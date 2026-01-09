# AINEX Law: Quick Start Guide

A step-by-step guide to understanding and running the AI model semantic collapse experiment.

---

## 📖 What is the AINEX Law?

The **AINEX Law** states: *Language models lose semantic diversity when recursively trained on their own outputs.*

Think of it like a game of telephone:
1. **Human Message**: Full richness of ideas (semantic space)
2. **First Repetition**: Model learns and regenerates (some loss)
3. **Second Repetition**: Model trained on Step 2 output (further degradation)
4. **Result**: The final message is much simpler and more limited than the original

---

## 🎯 Why Should You Care?

### For AI Safety Researchers
- Shows how self-improving systems can degrade over time
- Demonstrates fundamental limits of synthetic data
- Relevant for continual learning systems

### For ML Engineers
- Important for training pipelines using synthetic data
- Explains why model fine-tuning on generated data fails
- Informs data collection strategies

### For Data Scientists
- Quantifies synthetic data quality degradation
- Provides mathematical framework for semantic diversity
- Shows computational approach to semantic analysis

---

## 🚀 Running the Experiment

### Prerequisites

```bash
# Required: Python 3.8+
python --version

# Check GPU availability
python -c "import torch; print('GPU Available:', torch.cuda.is_available())"
```

### Step 1: Set Up Environment

```bash
# Navigate to project directory
cd Ainex-Limit-Experiment

# All dependencies are installed automatically in the notebook
# (pip install command at the top of main.ipynb)
```

### Step 2: Open Jupyter Notebook

**Option A: Jupyter Lab**
```bash
jupyter lab main.ipynb
```

**Option B: VS Code** (Recommended)
- Open VS Code
- Install "Jupyter" extension if not present
- Click on `main.ipynb` file
- Select "Run All" or execute cells sequentially

**Option C: Google Colab**
```
1. Upload main.ipynb to Google Drive
2. Open with Google Colab
3. Run cells (GPU automatically available)
```

### Step 3: Execute Experiment

The notebook is divided into clear sections:

1. **Installation** - Libraries and setup (automatic)
2. **Model Loading** - GPT-2 and embedders (2-3 minutes)
3. **Data Preparation** - Wikipedia corpus (1-2 minutes)
4. **Baseline Training** - Learn from human text (5-10 minutes)
5. **Generation 1** - Create synthetic texts (3-5 minutes)
6. **Recursive Training** - Train on synthetic data (5-10 minutes)
7. **Generation 2** - Final output analysis (3-5 minutes)
8. **Results** - View semantic collapse metrics (automatic)

### Step 4: Interpret Results

Look for the final metrics section:

```
Baseline (Human Knowledge) Volume : X.XXXX
Generation 1 Volume                : X.XXXX
Generation 2 Volume                : X.XXXX
Semantic Collapse Rate             : XX.XX%
```

**If Collapse Rate > 0%**: ✅ AINEX Law confirmed
**If Collapse Rate < 0%**: ⚠️ Hallucination observed
**If Collapse Rate ≈ 0%**: ❓ Insufficient effect

---

## 🔧 Customization Guide

### Adjust Experiment Size

**Make it faster** (for testing):
```python
# Line ~120: Reduce corpus size
human_knowledge_texts = [...dataset...][:100]  # Change 400 to 100

# Line ~170: Reduce generation size
generate_texts_from_model(model, num_texts=200)  # Change 400 to 200
```

**Make it more rigorous** (for publication):
```python
# Increase all numbers
human_knowledge_texts = [...dataset...][:1000]  # Increase to 1000
generate_texts_from_model(model, num_texts=1000)  # Increase to 1000

# Run multiple times and average results
for run in range(5):
    results[run] = run_experiment()
```

### Adjust Training Intensity

**Weaker collapse** (more human-like):
```python
train_model_on_texts(model, generation_1_texts, epochs=1)  # Reduce from 3
```

**Stronger collapse** (emphasize degradation):
```python
train_model_on_texts(model, generation_1_texts, epochs=5)  # Increase from 3
```

### Adjust Generation Diversity

**More conservative** (less diverse, more repetitive):
```python
generate_texts_from_model(model, temperature=0.5)  # Reduce from 0.7
```

**More diverse** (less coherent, more varied):
```python
generate_texts_from_model(model, temperature=0.9)  # Increase from 0.7
```

---

## ⚡ Performance Tips

### If Running on CPU

Expected time: 2-4 hours (patient required!)

```python
# Speed up slightly by reducing batch size
batch_size = 4  # Reduce memory usage
```

### If Running on GPU

Expected time: 15-30 minutes

```python
# Verify GPU is in use
print(f"Device: {device}")  # Should print "DEVICE: CUDA"

# Monitor GPU usage in separate terminal
watch -n 1 nvidia-smi  # For NVIDIA GPUs
```

### Memory Optimization

If you get "Out of Memory" error:

```python
# Reduce batch size
loader = DataLoader(train_data, batch_size=4, shuffle=True)  # From 8 to 4

# Reduce sequence length
max_length=64  # From 128

# Reduce number of texts
num_texts=200  # From 400
```

---

## 📊 Understanding the Metrics

### Semantic Volume (V)

**What it is**: Geometric size of the convex hull around text embeddings in 3D space

**Why it matters**: 
- Larger volume = more semantic diversity
- Smaller volume = more repetitive/constrained generation

**Mathematical basis**: 
- Convert texts to embeddings (Sentence-BERT, 384D)
- Reduce to 3D (PCA)
- Compute convex hull volume

### Collapse Rate (%)

**Formula**: 
$$\text{Rate} = \frac{\text{Baseline} - \text{Gen2}}{\text{Baseline}} \times 100\%$$

**Interpretation**:
- **+30%**: Strong collapse (model became much more limited)
- **+10%**: Moderate collapse (model lost some diversity)
- **+2%**: Weak/marginal collapse (nearly stable)
- **-5%**: Hallucination (model went "wild")

---

## 🔍 Interpreting Different Outcomes

### Outcome 1: Clear Collapse (Most Common)

```
Baseline : 2.5000
Gen 1    : 2.3000
Gen 2    : 1.8000
Rate     : 28%
```

**What happened**: 
- Model learned from humans (small drop to Gen 1)
- Then degraded significantly when trained recursively (large drop to Gen 2)
- The AINEX Law is confirmed

**Why**:
- Model overfit to generation patterns
- Lost diversity through recursive training
- Semantic space contracted to core attractors

---

### Outcome 2: Hallucination Pattern

```
Baseline : 2.5000
Gen 1    : 2.4000
Gen 2    : 2.8000
Rate     : -12%
```

**What happened**:
- Gen 2 is actually LARGER than baseline
- Model entered a state of random generation
- Not true collapse, but noise amplification

**Why**:
- Over-aggressive training caused instability
- Model generating incoherent but novel patterns
- May need to reduce training epochs

---

### Outcome 3: No Effect

```
Baseline : 2.5000
Gen 1    : 2.5100
Gen 2    : 2.4900
Rate     : -0.4%
```

**What happened**:
- No significant semantic change across generations
- Model maintained stability

**Why**:
- Model capacity is large relative to corpus size
- Might need more training or recursive iterations
- Noise in volume calculation masks small effects

---

## 🐛 Troubleshooting

### Problem: "ImportError: No module named 'transformers'"

**Solution**: The notebook's pip install cell didn't run
```python
!pip install transformers datasets sentence-transformers scipy scikit-learn accelerate
```

### Problem: "RuntimeError: CUDA out of memory"

**Solution**: Reduce memory usage
```python
# Smaller batch size
loader = DataLoader(train_data, batch_size=4)

# Fewer texts
num_texts = 200

# Shorter sequences
max_length = 64
```

### Problem: "ConvexHull error: QH6154"

**Solution**: Not enough points for convex hull
- This happens when you have < 4 points in 3D space
- Increase number of texts or reduce PCA components

### Problem: Volumes are all zero

**Solution**: Texts might be too similar or embeddings failed
```python
# Check if texts are meaningful
print(human_knowledge_texts[0])  # Should be substantial text

# Verify embeddings work
test_embedding = embedder.encode("Test text")
print(test_embedding.shape)  # Should be (384,)
```

### Problem: Experiment runs but results seem wrong

**Solution**: Check intermediate outputs
```python
# After training, generate and inspect texts
print(gen_1_texts[0])  # Should be reasonable English

# Check volumes
print(f"Volumes: {baseline_volume:.4f}, {gen_1_volume:.4f}, {gen_2_volume:.4f}")
# Should be positive and decreasing (or stable)
```

---

## 📚 Learning Resources

### To Understand Semantic Embeddings
- [Sentence-BERT Paper](https://arxiv.org/abs/1908.10084)
- [OpenAI Embeddings Blog](https://openai.com/blog/new-embedding-models-and-api-updates/)

### To Understand Language Model Training
- [Hugging Face Course](https://huggingface.co/course)
- [Fine-tuning Guide](https://huggingface.co/docs/transformers/training)

### To Understand Dimensionality Reduction
- [PCA Explained](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [Understanding Convex Hulls](https://en.wikipedia.org/wiki/Convex_hull)

### Related Papers
- Shumailov et al. (2023): "The Curse of Recursion"
- Carlini et al. (2023): "Extracting Training Data from Diffusion Models"

---

## ❓ FAQs

**Q: Can I use a different language model?**  
A: Yes! Replace `GPT2LMHeadModel` with any Hugging Face model compatible with language generation (T5, BLOOM, LLaMA).

**Q: Why Wikipedia data?**  
A: It's diverse, freely available, and has clear semantic structure. You can substitute with any corpus.

**Q: How long should I wait?**  
A: GPU: 15-30 min | CPU: 2-4 hours | Google Colab: 10-20 min (GPU included)

**Q: Can results be reproduced exactly?**  
A: Nearly. Set random seeds, but GPU operations have slight non-determinism.

**Q: What if I get different results each time?**  
A: Normal! Due to randomness in training and generation. Run multiple times and average.

**Q: Is this scientifically rigorous?**  
A: For a quick demonstration, yes. For publication, run 5-10 repetitions and do statistical testing.

---

## 🎓 Next Steps

After understanding the AINEX Law:

1. **Replicate** the experiment with different models
2. **Extend** with multiple iterations (Generation 3+)
3. **Measure** other metrics (entropy, KL divergence)
4. **Theorize** why this happens (mode collapse, attractor states)
5. **Solve** how to prevent it (data augmentation, diversity constraints)

---

**Good luck with your experiment!** 🚀
