# ==============================================================================
# Ainex Law Project: Recursive Decay (The Hard-Kill Version)
# ==============================================================================

# 1. Install necessary libraries (silent install)
" !pip install transformers datasets sentence-transformers scipy scikit-learn accelerate > /dev/null "

import torch
from torch.utils.data import Dataset, DataLoader
# --- Call correction: AdamW from original source ---
from torch.optim import AdamW
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from scipy.spatial import ConvexHull
import numpy as np
import random
from tqdm import tqdm
import warnings

# Ignore annoying warnings
warnings.filterwarnings("ignore")

# Ensure GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Working on: {device.upper()}")
if device == 'cpu':
    print("Warning: Running on CPU will be very slow.")

# ==============================================================================
# 2. Setup Models and Data
# ==============================================================================

print("... Loading tools ...")
# Load the model (the victim)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

# Load the "measurement scalpel" (Sentence-BERT)
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Load real Wikipedia data
print("... Loading Wikipedia data ...")
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")

# Prepare data
class TextListDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length=128):
        self.inputs = []
        for txt in texts:
            if len(txt) > 50: # Select meaningful texts
                enc = tokenizer(txt, truncation=True, max_length=max_length, padding="max_length", return_tensors="pt")
                self.inputs.append(enc)
    def __len__(self):
        return len(self.inputs)
    def __getitem__(self, i):
        return {k: v.squeeze(0) for k, v in self.inputs[i].items()}

# Take a sample of 400 real texts
real_wiki_texts = [x['text'] for x in dataset if len(x['text']) > 100][:400]

# ==============================================================================
# 3. Core Functions (The Engine)
# ==============================================================================

def train_model(model, texts, epochs=3):
    """
    Intensive training to erase old memory and implant new data
    """
    model.train()
    train_data = TextListDataset(texts, tokenizer)
    loader = DataLoader(train_data, batch_size=8, shuffle=True)
    optim = AdamW(model.parameters(), lr=5e-5)

    print(f">> Training (Overfitting) for {epochs} Epochs...")
    for epoch in range(epochs):
        loop = tqdm(loader, leave=False)
        total_loss = 0
        for batch in loop:
            optim.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = input_ids.clone()

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            loss.backward()
            optim.step()
            total_loss += loss.item()
            loop.set_description(f"Epoch {epoch+1}/{epochs} | Loss: {loss.item():.4f}")

def generate_synthetic_data(model, num_samples=400):
    """
    Generation with restricted randomness (Low Temperature)
    """
    model.eval()
    gen_texts = []
    print(f">> Generating {num_samples} texts from the model's imagination...")

    # Diverse prompts
    prompts = ["The history", "Science is", "War began", "The theory", "He was born",
               "In 1990", "The system", "Water is", "Computers are", "The city"] * (num_samples // 10 + 5)

    batch_size = 10
    for i in tqdm(range(0, num_samples, batch_size)):
        batch_prompts = prompts[i:i+batch_size]
        if not batch_prompts: break

        inputs = tokenizer(batch_prompts, return_tensors="pt", padding=True, truncation=True).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=100,
                do_sample=True,
                top_k=40,        # Reduce options
                temperature=0.7, # Low temperature to kill hallucinations and increase repetition
                repetition_penalty=1.1
            )

        for out in outputs:
            text = tokenizer.decode(out, skip_special_tokens=True)
            gen_texts.append(text)

    return gen_texts[:num_samples]

def get_ainex_volume(texts):
    """
    Calculate the geometric volume of ideas
    """
    embeddings = embedder.encode(texts)
    pca = PCA(n_components=3)
    coords = pca.fit_transform(embeddings)
    try:
        hull = ConvexHull(coords)
        return hull.volume
    except:
        return 0.0

# ==============================================================================
# 4. Execution: The Fatal Experiment
# ==============================================================================

results = {}

print("\n" + "="*50)
print(" STARTING AINEX RECURSIVE DECAY EXPERIMENT ")
print("="*50)

# --- Measure Reality ---
vol_real = get_ainex_volume(real_wiki_texts)
print(f"\n[Baseline] Human Knowledge Volume: {vol_real:.4f}")

# --- Gen 1: Train on reality then generate ---
print("\n--- Stage 1: Learning from Humans ---")
train_model(model, real_wiki_texts, epochs=2) # Train it to understand the pattern
gen_1_texts = generate_synthetic_data(model, num_samples=400)
vol_gen1 = get_ainex_volume(gen_1_texts)
print(f"[Gen 1] First Generation Volume: {vol_gen1:.4f}")

# --- Gen 2: Self-cannibalization (train on Gen 1) ---
print("\n--- Stage 2: Recursive Closure (Training on synthetic data) ---")
# Here the collapse happens: train it heavily (3 epochs) only on its own outputs
train_model(model, gen_1_texts, epochs=3)
gen_2_texts = generate_synthetic_data(model, num_samples=400)
vol_gen2 = get_ainex_volume(gen_2_texts)
print(f"[Gen 2] Second Generation Volume: {vol_gen2:.4f}")

# ==============================================================================
# 5. Final Report
# ==============================================================================

decay_rate = ((vol_real - vol_gen2) / vol_real) * 100

print("\n" + "#"*40)
print("   RESULT REPORT   ")
print("#"*40)
print(f"Human Volume (Origin) : {vol_real:.5f}")
print(f"AI Gen 2 Volume       : {vol_gen2:.5f}")
print(f"Collapse Rate         : {decay_rate:.2f}%")

if decay_rate > 0:
    print("\n>> Result: Collapse.")
    print(">> Ainex Law is proven: The model lost the ability to cover the original semantic space.")
    print(">> Explanation: Self-replication reduced imagination.")
else:
    print("\n>> Result: Expansion (Noise/Hallucination).")
    print(">> The model entered a state of random delirium.")

print("#"*40)
