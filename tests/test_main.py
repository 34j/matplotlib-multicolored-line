from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pytest

from matplotlib_multicolored_line import colored_line

CACHE_PATH = Path(__file__).parent / ".cache"


@pytest.fixture(autouse=True)
def setup_cache() -> None:
    CACHE_PATH.mkdir(parents=True, exist_ok=True)


def test_main() -> None:
    t = np.linspace(-7.4, -0.5, 200)
    x = 0.9 * np.sin(t)
    y = 0.9 * np.cos(1.6 * t)

    fig, ax = plt.subplots()
    lc = colored_line(x, y, t, ax, linewidth=10)
    fig.colorbar(lc)
    fig.savefig(CACHE_PATH / "example.jpg")


def test_main_small() -> None:
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 2, 1, 1]
    c = [1, 2, 3, 4, 5]

    fig, ax = plt.subplots()
    lc = colored_line(x, y, c, ax, linewidth=10)
    fig.colorbar(lc)
    fig.savefig(CACHE_PATH / "example_small.jpg")
