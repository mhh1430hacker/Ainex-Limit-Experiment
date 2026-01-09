# Installation Guide

Complete setup instructions for the AINEX Law experiment.

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Methods](#installation-methods)
3. [Dependency Setup](#dependency-setup)
4. [GPU Configuration](#gpu-configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements

| Component | Requirement | Notes |
|-----------|-------------|-------|
| **OS** | Linux, macOS, or Windows | Linux recommended |
| **Python** | 3.8+ | 3.10+ recommended |
| **RAM** | 8GB | 16GB+ recommended |
| **Disk** | 10GB free | ~5GB for models, ~5GB temp space |
| **GPU** | Optional but recommended | 6GB+ VRAM (NVIDIA/AMD) |

### Recommended Setup

- **Python**: 3.10 or 3.11
- **RAM**: 16GB+
- **GPU**: NVIDIA with CUDA 11.8+
- **OS**: Ubuntu 20.04+ or macOS 12+

---

## Installation Methods

### Method 1: Local Installation (Recommended)

#### Step 1: Clone Repository

```bash
git clone <repository-url>
cd Ainex-Limit-Experiment
```

#### Step 2: Create Virtual Environment

**Using venv (Python 3.8+)**
```bash
python3 -m venv ainex_env
source ainex_env/bin/activate  # Linux/macOS
# or
ainex_env\Scripts\activate      # Windows
```

**Using conda (if installed)**
```bash
conda create -n ainex python=3.10
conda activate ainex
```

#### Step 3: Install Dependencies

```bash
# The notebook will auto-install dependencies, but you can pre-install:
pip install --upgrade pip
pip install torch transformers datasets sentence-transformers scipy scikit-learn accelerate jupyter
```

#### Step 4: Open Notebook

**Jupyter Lab**
```bash
jupyter lab main.ipynb
```

**Jupyter Notebook**
```bash
jupyter notebook main.ipynb
```

**VS Code** (if installed with Jupyter extension)
1. Install [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
2. Open `main.ipynb` in VS Code
3. Click "Run All" button

---

### Method 2: Docker Installation

#### Create Dockerfile

```dockerfile
FROM pytorch/pytorch:2.0-cuda11.8-runtime-ubuntu22.04

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    transformers \
    datasets \
    sentence-transformers \
    scipy \
    scikit-learn \
    accelerate \
    jupyter \
    ipykernel

# Copy project
COPY . /workspace/

# Set up Jupyter
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
```

#### Build and Run

```bash
# Build image
docker build -t ainex-experiment .

# Run container
docker run --gpus all -it -p 8888:8888 -v $(pwd):/workspace ainex-experiment

# Access at http://localhost:8888
```

---

### Method 3: Google Colab (Free GPU)

#### Step 1: Upload Notebook

1. Go to [Google Colab](https://colab.research.google.com)
2. Click "Upload" tab
3. Select `main.ipynb` from your computer

#### Step 2: Enable GPU

1. Menu → Runtime → Change runtime type
2. Hardware accelerator: Select **GPU**
3. Click Save

#### Step 3: Run

```python
# In first cell, mount Google Drive (optional)
from google.colab import drive
drive.mount('/content/drive')

# Then run all cells
```

**Advantages**:
- Free GPU access (12 hours/session)
- No local setup needed
- Easy sharing with others

**Limitations**:
- 12-hour session limit
- Variable GPU performance
- Data doesn't persist between sessions

---

### Method 4: Remote Server (SSH)

#### Setup on Server

```bash
# SSH into server
ssh user@your_server.com

# Create conda environment
conda create -n ainex python=3.10
conda activate ainex

# Install dependencies
pip install -r requirements.txt
```

#### Access from Local Machine

```bash
# Forward Jupyter port
ssh -L 8888:localhost:8888 user@your_server.com

# Start Jupyter on server
jupyter lab --ip=localhost --port=8888

# Access at http://localhost:8888 on your local machine
```

---

## Dependency Setup

### Requirements File

Create `requirements.txt` for reproducible installations:

```txt
torch>=2.0.0,<3.0.0
transformers>=4.30.0
datasets>=2.10.0
sentence-transformers>=2.2.0
scipy>=1.10.0
scikit-learn>=1.3.0
accelerate>=0.20.0
jupyter>=1.0.0
ipykernel>=6.0.0
numpy>=1.24.0
tqdm>=4.65.0
```

Install from requirements:
```bash
pip install -r requirements.txt
```

### Key Dependencies Explained

| Package | Version | Purpose |
|---------|---------|---------|
| **torch** | ≥2.0 | Deep learning framework |
| **transformers** | ≥4.30 | GPT-2 and tokenizers |
| **datasets** | ≥2.10 | Load Wikipedia corpus |
| **sentence-transformers** | ≥2.2 | Semantic embeddings |
| **scipy** | ≥1.10 | Convex hull computation |
| **scikit-learn** | ≥1.3 | PCA dimensionality reduction |
| **accelerate** | ≥0.20 | Distributed training utils |
| **jupyter** | ≥1.0 | Interactive notebooks |

---

## GPU Configuration

### NVIDIA GPUs

#### Install CUDA Toolkit

```bash
# Ubuntu 22.04
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-repository-ubuntu2204_12.0.0_amd64.deb
sudo dpkg -i cuda-repository-ubuntu2204_12.0.0_amd64.deb
sudo apt-get update
sudo apt-get -y install cuda
```

#### Install cuDNN (Optional, for faster operations)

```bash
# Download from NVIDIA website, then:
tar -xzvf cudnn-linux-*.tgz
sudo cp cudnn-linux-*/include/cudnn.h /usr/local/cuda/include/
sudo cp cudnn-linux-*/lib/libcudnn* /usr/local/cuda/lib64/
```

#### Verify Installation

```bash
# Check CUDA
nvcc --version

# Check PyTorch can access GPU
python -c "import torch; print('GPU Available:', torch.cuda.is_available())"
```

### AMD GPUs

#### Install ROCm

```bash
# Ubuntu 22.04
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
sudo apt update
sudo apt install rocm-hip-runtime rocm-dev
```

#### Install PyTorch with ROCm

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7
```

### Apple Silicon (M1/M2/M3)

#### Install PyTorch for Metal

```bash
# Metal accelerated version
pip install torch torchvision torchaudio
```

**Note**: GPU support is automatic on Apple Silicon.

#### Verify

```python
import torch
print(torch.backends.mps.is_available())  # Should be True
```

---

## Verification

### Check Installation

```bash
python << 'EOF'
import torch
import transformers
import sentence_transformers
import sklearn
import scipy

print("✓ PyTorch version:", torch.__version__)
print("✓ CUDA available:", torch.cuda.is_available())
print("✓ CUDA device:", torch.cuda.get_device_name() if torch.cuda.is_available() else "None")
print("✓ Transformers version:", transformers.__version__)
print("✓ Sentence-Transformers version:", sentence_transformers.__version__)
print("✓ Scikit-learn version:", sklearn.__version__)
print("✓ SciPy version:", scipy.__version__)
print("\n✅ All dependencies installed correctly!")
EOF
```

### Test GPU Access

```bash
python << 'EOF'
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

# Test generation
input_ids = tokenizer.encode("Hello", return_tensors="pt").to(device)
output = model.generate(input_ids, max_length=20)
print("✅ Model loaded and working!")
EOF
```

### Pre-download Models

To avoid downloads during execution:

```bash
python << 'EOF'
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from sentence_transformers import SentenceTransformer
from datasets import load_dataset

print("Downloading GPT-2...")
GPT2Tokenizer.from_pretrained("gpt2")
GPT2LMHeadModel.from_pretrained("gpt2")

print("Downloading Sentence-BERT...")
SentenceTransformer('all-MiniLM-L6-v2')

print("Downloading Wikipedia data...")
load_dataset("wikitext", "wikitext-2-raw-v1", split="train")

print("✅ All models cached locally!")
EOF
```

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'torch'"

**Solution**:
```bash
pip install --upgrade torch
# Or for GPU:
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Problem: "CUDA out of memory"

**Solution**:
```bash
# Option 1: Use CPU (slower but works)
device = "cpu"

# Option 2: Reduce batch size in notebook
batch_size = 4  # From 8

# Option 3: Reduce sequence length
max_length = 64  # From 128

# Option 4: Use smaller model
# Replace GPT2 with DistilGPT2
```

### Problem: "No module named 'sentence_transformers'"

**Solution**:
```bash
pip install sentence-transformers
```

### Problem: "RuntimeError: Expected all tensors to be on the same device"

**Solution**: Ensure all tensors are on same device
```python
# Check device
print("Model device:", next(model.parameters()).device)
print("Input device:", input_ids.device)

# Move to same device
device = "cuda" if torch.cuda.is_available() else "cpu"
input_ids = input_ids.to(device)
model = model.to(device)
```

### Problem: "ConnectionError: Unable to download model"

**Solution**: Network or Hugging Face server issue
```bash
# Retry with longer timeout
export HF_HUB_DOWNLOAD_TIMEOUT=300

# Or manually download
# Then load locally
model = GPT2LMHeadModel.from_pretrained("/path/to/local/model")
```

### Problem: "ValueError: ConvexHull requires at least 4 points"

**Solution**: Not enough text samples
```python
# Increase number of texts
human_knowledge_texts = [...dataset...][:800]  # Increase from 400
```

### Problem: Slow execution even with GPU

**Verify GPU is being used**:
```python
import torch

# In notebook cell:
print(f"Device: {device}")  # Should say "cuda"
print(f"GPU Name: {torch.cuda.get_device_name()}")

# Monitor during execution
# In separate terminal:
watch -n 1 nvidia-smi
```

**If still slow**:
- Check GPU driver: `nvidia-smi`
- Check CUDA version matches PyTorch
- Try CPU for testing

---

## Environment Variables

### For Faster Downloads

```bash
export HF_HOME="/path/to/cache"  # Cache Hugging Face models
export TORCH_HOME="/path/to/torch"  # Cache PyTorch models
```

### For Performance

```bash
export CUDA_LAUNCH_BLOCKING=1  # Synchronize CUDA (helps debugging)
export OMP_NUM_THREADS=8  # For CPU parallelization
```

### For Jupyter

```bash
export JUPYTER_ENABLE_LAB=1  # Use Lab instead of Notebook
```

---

## Updating Dependencies

### Check for Updates

```bash
pip list --outdated
```

### Update All Packages

```bash
pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

### Pin Specific Versions

If you find a working combination, freeze it:

```bash
pip freeze > requirements-lock.txt
# Later: pip install -r requirements-lock.txt
```

---

## Next Steps

After successful installation:

1. Verify setup: See [Verification](#verification) section
2. Quick start: Read [QUICKSTART.md](QUICKSTART.md)
3. Run experiment: Execute [main.ipynb](main.ipynb)
4. Interpret results: Check [README.md](README.md)

---

**Installation complete!** 🎉

If you encounter issues not covered here, please check:
- [QUICKSTART.md](QUICKSTART.md) - Troubleshooting section
- [README.md](README.md) - Known limitations
- GitHub Issues (if applicable)

Good luck with your AINEX experiment! 🚀
