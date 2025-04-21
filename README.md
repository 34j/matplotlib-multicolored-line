# Matplotlib Multicolored Line

<p align="center">
  <a href="https://github.com/34j/matplotlib-multicolored-line/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/matplotlib-multicolored-line/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://matplotlib-multicolored-line.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/matplotlib-multicolored-line.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/34j/matplotlib-multicolored-line">
    <img src="https://img.shields.io/codecov/c/github/34j/matplotlib-multicolored-line.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
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
lc = colored_line(x, y, t, ax, linewidth=5)
fig.colorbar(lc)
```

![Result](https://raw.githubusercontent.com/34j/matplotlib-multicolored-line/main/example.jpg)

![Result 2](https://raw.githubusercontent.com/34j/matplotlib-multicolored-line/main/example_small.jpg)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/34j"><img src="https://avatars.githubusercontent.com/u/55338215?v=4?s=80" width="80px;" alt="34j"/><br /><sub><b>34j</b></sub></a><br /><a href="https://github.com/34j/matplotlib-multicolored-line/commits?author=34j" title="Code">💻</a> <a href="#ideas-34j" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/34j/matplotlib-multicolored-line/commits?author=34j" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

This package was created with
[Copier](https://copier.readthedocs.io/) and the
[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
project template.
