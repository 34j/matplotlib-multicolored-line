from collections.abc import Sequence
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pytest
from numpy.typing import ArrayLike

from matplotlib_multicolored_line import colored_line

CACHE_PATH = Path(__file__).parent / ".cache"


@pytest.fixture(autouse=True)
def setup_cache() -> None:
    CACHE_PATH.mkdir(parents=True, exist_ok=True)


t = np.linspace(-7.4, -0.5, 200)


@pytest.mark.parametrize(
    "name, args, c",
    [
        ("notebook1", (0.9 * np.sin(t), 0.5 * np.sin(t)), t),
        ("notebook2", ([0, 1, 2, 3, 4], [0, 1, 2, 1, 1]), [1, 2, 3, 4, 5]),
        ("singley", (np.random.normal(size=(5,)),), np.random.normal(size=(5,))),
        ("singley.rgb", (np.random.normal(size=(5,)),), np.random.normal(size=(5, 1, 3))),
        ("singley.rgba", (np.random.normal(size=(5,)),), np.random.normal(size=(5, 1, 4))),
        (
            "singley.colors",
            (np.random.normal(size=(5,)),),
            np.random.choice(["black", "red"], size=(5,)),
        ),
        (
            "singlexy",
            (
                np.random.normal(size=(5,)),
                np.random.normal(size=(5,)),
            ),
            np.random.normal(size=(5,)),
        ),
        (
            "singlexy.rgb",
            (
                np.random.normal(size=(5,)),
                np.random.normal(size=(5,)),
            ),
            np.random.normal(size=(5, 1, 3)),
        ),
        (
            "singlexy.rgba",
            (
                np.random.normal(size=(5,)),
                np.random.normal(size=(5,)),
            ),
            np.random.normal(size=(5, 1, 4)),
        ),
        (
            "singlexy.colors",
            (
                np.random.normal(size=(5,)),
                np.random.normal(size=(5,)),
            ),
            np.random.choice(["black", "red"], size=(5,)),
        ),
        ("multiy", (np.random.normal(size=(5, 2)),), np.random.normal(size=(5, 2))),
        ("multiy.rgb", (np.random.normal(size=(5, 2)),), np.random.uniform(size=(5, 2, 3))),
        ("multiy.rgba", (np.random.normal(size=(5, 2)),), np.random.uniform(size=(5, 2, 4))),
        (
            "multiy.colors",
            (np.random.normal(size=(5, 2)),),
            np.random.choice(["black", "red"], size=(5, 2)),
        ),
        (
            "multixy",
            (
                np.random.normal(size=(5, 2)),
                np.random.normal(size=(5, 2)),
            ),
            np.random.normal(size=(5, 2)),
        ),
        (
            "multixy.rgb",
            (
                np.random.normal(size=(5, 2)),
                np.random.normal(size=(5, 2)),
            ),
            np.random.uniform(size=(5, 2, 3)),
        ),
        (
            "multixy.rgba",
            (
                np.random.normal(size=(5, 2)),
                np.random.normal(size=(5, 2)),
            ),
            np.random.uniform(size=(5, 2, 4)),
        ),
        (
            "multixy.colors",
            (
                np.random.normal(size=(5, 2)),
                np.random.normal(size=(5, 2)),
            ),
            np.random.choice(["black", "red"], size=(5, 2)),
        ),
    ],
)
def test_multicolor(name: str, args: Sequence[ArrayLike], c: ArrayLike) -> None:
    fig, ax = plt.subplots()
    lc = colored_line(*args, c=c, ax=ax, linewidth=10)
    if "rgb" not in name:
        fig.colorbar(lc)
    fig.savefig(CACHE_PATH / f"example.{name}.jpg")
