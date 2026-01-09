# Contributing Guide

Thank you for your interest in contributing to the AINEX Law project! This guide will help you make meaningful contributions.

---

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Code of Conduct](#code-of-conduct)
3. [Getting Started](#getting-started)
4. [Development Workflow](#development-workflow)
5. [Coding Standards](#coding-standards)
6. [Testing](#testing)
7. [Commit Messages](#commit-messages)
8. [Pull Requests](#pull-requests)

---

## Ways to Contribute

### 📝 Documentation
- Improve README clarity
- Add FAQ entries
- Fix typos or grammar
- Translate documentation
- Create tutorials or examples

### 🐛 Bug Reports
- Report issues with execution
- Document error messages
- Provide reproduction steps
- Suggest fixes

### 💡 Feature Requests
- Suggest new experiments
- Propose different models
- Recommend new metrics
- Improve visualization

### 🔬 Research
- Replicate experiment with different settings
- Test on alternative datasets
- Validate with other models
- Publish findings

### 💻 Code Improvements
- Optimize performance
- Refactor code for clarity
- Add error handling
- Implement new features

---

## Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

✅ Be respectful and professional  
✅ Welcome diverse perspectives  
✅ Give credit to others' work  
✅ Provide constructive feedback  
✅ Focus on code, not individuals  

### Unacceptable Behavior

❌ Harassment or discrimination  
❌ Sharing private information  
❌ Plagiarism or unattributed work  
❌ Abusive or derogatory language  
❌ Trolling or bad-faith arguments  

---

## Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" button on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Ainex-Limit-Experiment.git
cd Ainex-Limit-Experiment
```

### 2. Add Upstream Remote

```bash
# To stay in sync with original
git remote add upstream https://github.com/ORIGINAL_OWNER/Ainex-Limit-Experiment.git
```

### 3. Create Development Environment

```bash
# Create virtual environment
python -m venv dev_env
source dev_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install black flake8 pytest jupyter
```

### 4. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

---

## Development Workflow

### Making Changes

1. **Create descriptive branch name**:
   - Feature: `feature/semantic-diversity-metric`
   - Bug fix: `fix/gpu-memory-error`
   - Documentation: `docs/quickstart-guide`
   - Research: `research/multi-model-comparison`

2. **Make your changes**:
   - Edit files in your feature branch
   - Test frequently
   - Commit regularly with clear messages

3. **Keep branch updated**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**:
   - Go to GitHub
   - Click "Compare & pull request"
   - Fill in description following template

---

## Coding Standards

### Python Style

Follow PEP 8 with these additions:

```python
# Good: Clear variable names
semantic_volume = calculate_convex_hull_volume(embeddings)

# Avoid: Cryptic abbreviations
sem_vol = calc_cvx_hull_vol(embs)
```

### Docstrings

Use Google-style docstrings:

```python
def calculate_semantic_volume(texts):
    """
    Calculate the geometric volume of text embeddings using convex hull.
    
    This metric quantifies semantic diversity and coverage of the text corpus.
    
    Args:
        texts: List of text strings to analyze
    
    Returns:
        float: Volume of convex hull in 3D PCA space (0.0 if fails)
    
    Raises:
        ValueError: If texts list is empty
        RuntimeError: If convex hull computation fails
    
    Examples:
        >>> texts = ["Hello world", "Good morning"]
        >>> volume = calculate_semantic_volume(texts)
        >>> print(volume)
        1.234
    """
    # Implementation
    pass
```

### Comments

```python
# Good: Explain WHY not WHAT
# Reduce to 3D for computational efficiency and visualization
pca = PCA(n_components=3)

# Avoid: Obvious comments
# Create PCA object
pca = PCA(n_components=3)
```

### Type Hints

```python
# Use type hints for clarity
from typing import List, Dict, Tuple, Optional

def generate_texts_from_model(
    model: GPT2LMHeadModel,
    num_texts: int = 400,
    temperature: float = 0.7
) -> List[str]:
    """Generate text sequences from model."""
    pass
```

### Format Code

```bash
# Auto-format with Black
black main.ipynb --target-version py310

# Check style
flake8 *.py --max-line-length=100
```

---

## Testing

### Add Test Cases

For new functions, create simple test cells:

```python
def test_semantic_volume_calculation():
    """Test volume calculation doesn't crash."""
    texts = ["Test one", "Test two", "Test three"]
    volume = calculate_semantic_volume(texts)
    assert isinstance(volume, float)
    assert volume >= 0

test_semantic_volume_calculation()
print("✓ Test passed")
```

### Test Different Scenarios

```python
# Test with minimal input
test_with_minimal_corpus()

# Test with edge cases
test_with_identical_texts()

# Test error handling
test_with_invalid_input()
```

### Document Expected Results

```python
# When collapse is strong: volume should decrease significantly
# Expected: baseline ~2.5, gen2 ~1.8, rate ~28%

# When hallucination occurs: volume might increase
# Expected: baseline ~2.5, gen2 ~2.7, rate ~-8%
```

---

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature or experiment
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code restructuring
- `perf`: Performance improvements
- `test`: Adding/improving tests
- `ci`: CI/CD changes

### Examples

```
Good commits:
- feat(training): add support for custom learning rates
- fix(gpu): resolve CUDA out of memory on large batches
- docs(readme): clarify interpretation of collapse metrics
- refactor(embeddings): simplify semantic volume calculation

Avoid:
- fix bugs
- update stuff
- various changes
- wip (work in progress)
```

### Body Guidelines

- Explain WHAT and WHY (not HOW)
- Reference related issues: "Fixes #123"
- Keep lines under 72 characters
- Use imperative mood: "Add" not "Added"

### Example Full Commit

```
feat(experiment): add generation 3 recursive training stage

The AINEX Law would be stronger if we traced the collapse
across more generations. This adds an optional third generation
where Gen 2 outputs are used for training.

- Add train_generation_3() function
- Extend results reporting to show Gen 3 metrics
- Update documentation with multi-generation interpretation

Relates to #45
```

---

## Pull Requests

### Before Submitting

- [ ] Tested your changes
- [ ] Followed coding standards
- [ ] Updated documentation
- [ ] Added comments for complex logic
- [ ] No unrelated changes included

### PR Template

```markdown
## Description
Brief explanation of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Related Issues
Fixes #(issue number)

## Testing
Describe testing performed

## Changes Made
- Item 1
- Item 2
- Item 3

## Screenshots (if applicable)
[Add results, graphs, or examples]

## Checklist
- [ ] My code follows style guidelines
- [ ] I've updated documentation
- [ ] Tests pass successfully
- [ ] No new warnings generated
```

### PR Guidelines

1. **Keep it focused**: One feature or fix per PR
2. **Clear description**: Explain what and why
3. **Link issues**: Reference related GitHub issues
4. **Be responsive**: Respond to review comments promptly
5. **Rebase if needed**: Keep history clean

### Review Process

- Maintainers will review within 1 week
- May request changes for clarity
- Be open to feedback
- Discuss disagreements respectfully
- Celebrate approved PRs! 🎉

---

## Documentation Contributions

### Adding to README

1. Check the section exists
2. Keep language clear and concise
3. Include examples where helpful
4. Update table of contents
5. Test all links work

### Creating New Guides

Use this template:

```markdown
# Guide Title

Brief introduction explaining the purpose.

## Table of Contents

## Section 1

Content here.

### Subsection

Details here.

## Section 2

More content.

## Related Resources

Link to related docs.
```

### Documentation Standards

- Use clear, professional language
- Include examples for technical concepts
- Provide links to related sections
- Keep headers hierarchical (H1 → H2 → H3)
- Test all code examples work

---

## Research Contributions

### Publishing Results

1. **Document your experiment**:
   - Modify notebook to add your variant
   - Save results to `results/your_experiment/`
   - Create summary in `docs/experiments.md`

2. **Share findings**:
   - Create discussion in GitHub Issues
   - Or submit research report (see template)

3. **Citation**:
   ```bibtex
   @software{ainex2024_yourname,
     title={AINEX Law: [Your Research Title]},
     author={Your Name},
     year={2024},
     url={https://github.com/.../your-contribution}
   }
   ```

### Research Report Template

```markdown
# Experiment: [Title]

## Hypothesis
What did you expect to find?

## Methodology
How did you test it?

## Results
What did you find?

## Interpretation
What does it mean?

## Limitations
What are the caveats?

## Conclusion
Summary and next steps.
```

---

## Getting Help

### Resources

- **Issues**: Search/create GitHub Issues for bugs
- **Discussions**: Use GitHub Discussions for ideas
- **Documentation**: Check README, QUICKSTART, METHODOLOGY
- **Code Comments**: Read inline documentation in notebook

### Asking Questions

When asking for help:
1. Search existing issues first
2. Provide minimal reproducible example
3. Include error messages
4. Describe what you've tried
5. Be specific about your environment

### Good Question Example

```
Title: GPU out of memory when running on reduced batch size

Description:
When I reduce batch_size to 4 (from 8) and run on A100 GPU,
I still get "CUDA out of memory" error.

Steps:
1. Changed batch_size = 4 in cell 5
2. Run cells 1-6
3. Error occurs in training loop

Error:
RuntimeError: CUDA out of memory. Tried to allocate X.XX GiB

Environment:
- GPU: NVIDIA A100 (80GB)
- CUDA: 12.0
- PyTorch: 2.0.0

What I've tried:
- Reduced max_length to 64
- Reduced num_texts to 200
```

---

## Acknowledgments

Thank you for contributing! Your efforts help make this project better for everyone. All contributors will be recognized in:
- Project README
- Release notes
- Contributor list

---

## Final Checklist

Before submitting your contribution:

- [ ] You've read this guide
- [ ] Your code follows the style guide
- [ ] You've tested your changes
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] PR description is complete
- [ ] You've linked related issues
- [ ] No unrelated files are included

---

**Ready to contribute?** Start with a small improvement, fork the repo, and submit a PR. We're excited to work with you! 🚀

Questions? Open a GitHub Discussion or Issue!
