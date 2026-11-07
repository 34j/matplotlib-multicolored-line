# Matplotlib Multicolored Line

<p align="center">
  <a href="https://github.com/34j/matplotlib-multicolored-line/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/matplotlib-multicolored-line/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://matplotlib-multicolored-line.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/matplotlib-multicolored-line.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
</p>
<p align="center">
  <a href="https://codecov.io/gh/34j/matplotlib-multicolored-line">
    <img src="https://img.shields.io/codecov/c/github/34j/matplotlib-multicolored-line.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/j178/prek">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json" alt="prek">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/matplotlib-multicolored-line/">
    <img src="https://img.shields.io/pypi/v/matplotlib-multicolored-line.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/matplotlib-multicolored-line.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/matplotlib-multicolored-line.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://matplotlib-multicolored-line.readthedocs.io" target="_blank">https://matplotlib-multicolored-line.readthedocs.io </a>

**Source Code**: <a href="https://github.com/34j/matplotlib-multicolored-line" target="_blank">https://github.com/34j/matplotlib-multicolored-line </a>

---

Plot multicolored lines in Matplotlib. Port of [Multicolored lines — Matplotlib 3.10.1 documentation](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html) with slight improvements.

## Installation

Install this via pip (or your favourite package manager):

```shell
pip install matplotlib-multicolored-line
```

## Usage

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib_multicolored_line import colored_line


t = np.linspace(-7.4, -0.5, 200)
x = 0.9 * np.sin(t)
y = 0.9 * np.cos(1.6 * t)

fig, ax = plt.subplots()
lc = colored_line(x, y, c=t, ax=ax, linewidth=10)
fig.colorbar(lc)
```

![Result](https://raw.githubusercontent.com/34j/matplotlib-multicolored-line/main/example.jpg)

```python
y = np.random.normal(size=(5, 2))
c = np.random.normal(size=(5, 2))

fig, ax = plt.subplots()
lc = colored_line(y, c=c, ax=ax, linewidth=10)
fig.colorbar(lc)
```

![Result 2](https://raw.githubusercontent.com/34j/matplotlib-multicolored-line/main/example_multiple.jpg)
