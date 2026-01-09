# images/

This folder holds images used by the repository documentation. To include images in the root-level pages (e.g. `CONTRIBUTING.md`, `FAQ.md`) or in `main.ipynb`, add image files here.

Recommended filenames:
- `hero.png` — main header graphic
- `architecture.png` — model/process diagram
- `screenshot-1.png` — UI screenshot

How to add images locally:

```bash
# From repo root
mkdir -p images
# copy or add files into images/
# e.g., cp ~/Downloads/screenshot.png images/screenshot-1.png
```

Usage example in markdown:

```markdown
![Project screenshot](images/screenshot-1.png)
```
