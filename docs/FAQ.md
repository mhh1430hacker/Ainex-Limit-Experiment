# Frequently Asked Questions

Answers to common questions about the AINEX Law experiment.

---

## General Questions

### Q: What is the AINEX Law?

**A**: The AINEX Law states that language models lose semantic diversity when trained recursively on their own outputs. It's demonstrated through this experiment by comparing semantic "volume" across generations.

### Q: Is this peer-reviewed research?

**A**: This is a computational demonstration of a phenomenon related to model collapse. While the experiment is rigorous, it's designed for educational purposes and proof-of-concept validation.

### Q: How is this different from mode collapse in GANs?

**A**: Mode collapse in GANs typically refers to generator diversity. The AINEX Law specifically addresses semantic space contraction in language models through iterative self-training. The metrics and domain are different.

### Q: Can I use this for my research?

**A**: Yes! The project is provided for educational and research use. Please cite appropriately and contribute back if you make improvements.

---

## Technical Questions

### Q: Do I need a GPU?

**A**: No, but it's strongly recommended. The experiment takes ~30 minutes on GPU and 2-4 hours on CPU.

### Q: What's the minimum GPU memory needed?

**A**: 6GB VRAM is sufficient. The model and operations are relatively lightweight. You can reduce batch size if needed.

### Q: Can I use a different language model?

**A**: Yes! Replace `GPT2LMHeadModel` with any Hugging Face model that supports generation. Tested alternatives include GPT-Neo, DistilGPT-2, and BLOOM.

### Q: Can I use a different embedding model?

**A**: Yes! Replace `SentenceTransformer('all-MiniLM-L6-v2')` with alternatives like:
- `paraphrase-MiniLM-L6-v2` (different training)
- `all-mpnet-base-v2` (larger, more accurate)
- `sentence-t5-base` (different architecture)

### Q: How do I change the dataset?

**A**: Replace the Wikipedia loading with any text corpus:
```python
# Instead of Wikipedia:
texts = load_your_custom_dataset()
# Or manually:
texts = ["your text 1", "your text 2", ...]
```

### Q: What if my volumes are all zero?

**A**: This suggests:
1. Not enough texts (need >4 in 3D space)
2. Texts too similar (embedding variance is low)
3. Embedding model not working

**Solution**: Increase text diversity or verify embeddings work separately.

### Q: Can I parallelize this experiment?

**A**: The current design is sequential. You could parallelize by:
- Running multiple experiments with different seeds
- Using `multiprocessing` or `torch.distributed`
- Running separate generations in parallel (if memory allows)

---

## Results Questions

### Q: What collapse rate should I expect?

**A**: Typically 10-30% for this setup. Results vary due to:
- Random initialization in training
- Temperature in generation
- Specific texts sampled
- Embedding model randomness

Run 5 times and average for stability.

### Q: Is my collapse rate significant?

**A**: 
- **>15%**: Strong effect
- **5-15%**: Moderate effect
- **0-5%**: Weak/marginal effect
- **<0%**: Hallucination instead of collapse

Consider statistical testing for publication.

### Q: Why are my results different each time?

**A**: Multiple stochastic elements:
- Random initialization of model weights
- Random training data shuffling
- Random generation sampling (temperature)
- Random data split for embedding analysis

Set random seeds for reproducibility:
```python
import random, numpy as np, torch
random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
```

### Q: What does negative collapse rate mean?

**A**: The model generated more diverse outputs than the baseline. This suggests:
- Hallucination (incoherent but novel patterns)
- Insufficient training collapse
- Random noise dominating

Check generated text quality to diagnose.

---

## Interpretation Questions

### Q: Does collapse prove the AINEX Law?

**A**: This experiment provides evidence supporting the hypothesis, but:
- It's one specific setup (GPT-2, Wikipedia, etc.)
- Replication with other models would strengthen claims
- Statistical testing (multiple runs) is recommended
- Publication would require peer review

### Q: What about other model sizes?

**A**: The AINEX Law likely scales with model size:
- **Smaller models** (125M): Stronger collapse expected
- **Larger models** (7B+): Might resist collapse longer
- **Huge models** (175B+): Unknown (requires resources)

Research with multiple sizes would be valuable.

### Q: Does this affect real model training?

**A**: Yes, indirectly:
- Fine-tuning on synthetic data degrades performance
- Continual learning needs fresh data
- Recursive generation creates feedback loops
- Implications for AI safety and self-improvement

### Q: How is this related to data poisoning?

**A**: Similar mechanism but different intent:
- **AINEX Law**: Natural degradation from iteration
- **Data poisoning**: Intentional attack
- Both show risks of synthetic data feedback loops

---

## Methodological Questions

### Q: Why use convex hull volume as a metric?

**A**: Advantages:
- Computationally efficient
- Geometric interpretation (semantic "spread")
- Scale-invariant in 3D
- Easy to visualize

Limitations:
- Approximation of true semantic space (384D→3D)
- Sensitive to outliers
- May miss internal diversity changes

### Q: Why only 3 dimensions for PCA?

**A**: Trade-off:
- **3D**: Computable (convex hull), visualizable
- **Higher**: More complete but no convex hull in >3D
- **Alternative**: Use entropy or other metrics

### Q: Why these specific prompts for generation?

**A**: Current prompts cover diverse semantic domains:
- History, science, war, theory, biography
- Dates, systems, physics, technology, geography

You can modify for different domains.

### Q: How long should each epoch be?

**A**: Current: 2 epochs baseline, 3 epochs recursive
- **Fewer epochs**: Weaker effect, faster
- **More epochs**: Stronger collapse, slower

Experiment to find the threshold.

---

## Computational Questions

### Q: How much disk space is needed?

**A**: ~10GB total:
- 500MB for libraries
- 1GB for models (GPT-2, SBERT)
- 2GB for datasets
- 5GB temporary/cache

### Q: Can I reduce runtime?

**A**: 
- Reduce number of texts (400→200)
- Reduce epochs (2→1, 3→2)
- Reduce sequence length (128→64)
- Use DistilGPT-2 instead of GPT-2

Trade-off: Results may be less robust.

### Q: Why is generation slow?

**A**: Model.generate() is sequential, not parallelized in this implementation. Optimization options:
- Use batch generation (already implemented)
- Enable Flash Attention (if using newer PyTorch)
- Use `torch.compile()` (PyTorch 2.0+)

### Q: Can I stop and resume?

**A**: Partially:
- Save model after training: `torch.save(model.state_dict(), 'checkpoint.pt')`
- Load model before generation: `model.load_state_dict(torch.load('checkpoint.pt'))`
- You'll need to regenerate texts each time

Full checkpoint/resume would require restructuring.

---

## Dataset Questions

### Q: Can I use a different language?

**A**: Yes, but:
- Must use appropriate Sentence-BERT model for language
- Different languages may show different collapse rates
- Semantic diversity metrics may vary

Challenge: Multilingual experiments are less studied.

### Q: Can I use proprietary data?

**A**: Yes, if:
- You have legal right to it
- It's formatted as list of text strings
- You replace Wikipedia loading

Example:
```python
with open('my_data.txt') as f:
    texts = [line.strip() for line in f if len(line) > 100]
```

### Q: Should I use the full Wikipedia?

**A**: Depends on your goal:
- **Smaller (400)**: Quick demos, high noise
- **Larger (1000+)**: More stable, slower
- **Full dataset**: Very slow, but most comprehensive

Start small, scale up for final results.

### Q: What if my dataset is very small?

**A**: 
- Minimum ~50 texts (for convex hull in 3D)
- More texts = more stable results
- Very small datasets (100-200) may show high variance

---

## Extension Questions

### Q: How do I add a Generation 3?

**A**: 
```python
# After Generation 2
print("\n[GENERATION 3] Further recursive training...")
train_model_on_texts(model, generation_2_texts, epochs=3)
generation_3_texts = generate_texts_from_model(model, num_texts=400)
volume_gen3 = calculate_semantic_volume(generation_3_texts)
```

Expected: Further collapse (lower volume).

### Q: Can I analyze semantic direction instead of volume?

**A**: Yes! Use PCA components:
```python
# Semantic drift analysis
baseline_pca = pca.fit_transform(baseline_embeddings)
gen2_pca = pca.fit_transform(gen2_embeddings)
drift = np.mean(np.sqrt(np.sum((baseline_pca - gen2_pca)**2, axis=1)))
```

### Q: How do I measure text quality directly?

**A**: Options:
- **BLEU/ROUGE**: Compare to original
- **Perplexity**: Internal model metric
- **BLEURT**: Learned quality metric
- **Human evaluation**: Gold standard

### Q: Can I track intermediate states?

**A**: Yes, sample texts after each epoch:
```python
for epoch in range(epochs):
    # ... training ...
    if epoch % 2 == 0:
        sample_texts = generate_texts_from_model(model, num_texts=50)
        volumes[epoch] = calculate_semantic_volume(sample_texts)
```

---

## Troubleshooting Questions

### Q: My notebook keeps crashing

**A**: Check:
1. GPU memory sufficient?
2. All imports successful?
3. Model loading completed?
4. Try reducing batch size

### Q: Why is the generation very repetitive?

**A**: Might be working as designed (collapse!), but check:
- Temperature too low? (increase to 0.9)
- Model overtrained? (reduce epochs)
- Model broken? (test on fresh model)

### Q: Why are results inconsistent?

**A**: 
- Set random seeds (see earlier FAQ)
- Run multiple times
- Average results

---

## Contribution Questions

### Q: Can I contribute my modifications?

**A**: Yes! See [CONTRIBUTING.md](../CONTRIBUTING.md) for details. Welcome contributions:
- Bug fixes
- Performance improvements
- New experiment variants
- Documentation improvements
- Research findings

### Q: Can I publish this work?

**A**: Yes, with proper attribution:
- Cite this project
- Credit original authors
- Share improvements back
- Follow publication ethics

---

## Citation Questions

### Q: How do I cite this project?

**A**: 
```bibtex
@software{ainex2024,
  title={AINEX Law: AI Model Collapse via Semantic Contraction},
  author={Your Name},
  year={2024},
  url={https://github.com/yourusername/Ainex-Limit-Experiment}
}
```

### Q: Is there a paper?

**A**: Not yet! This is a demonstration project. If you publish research using this, please let us know.

---

## Still Have Questions?

- **Check**: README.md, QUICKSTART.md, METHODOLOGY.md
- **Open**: GitHub Issue (bugs/features)
- **Discuss**: GitHub Discussions (questions)
- **Read**: Code comments in main.ipynb

We're here to help! 🚀
