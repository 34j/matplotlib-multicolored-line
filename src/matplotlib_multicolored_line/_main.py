from __future__ import annotations

import warnings
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from numpy.typing import ArrayLike


def colored_line(
    *args: ArrayLike,
    c: ArrayLike,
    start: ArrayLike = 0.5,
    end: ArrayLike = 0,
    ax: Axes | None = None,
    **kwargs: Any,
) -> LineCollection:
    """
    Plot a line with a color specified along the line by a third value.

    It does this by creating a collection of line segments. Each line segment is
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    *args : array-like
        The horizontal and vertical coordinates of the data points
        of shape (N,) or (N, m).
    c : array-like or array-like of color, optional
        The line values. Possible values:
        - array-like of numbers of shape (N,) or (N, m) to be mapped
            to colors using cmap and norm.
        - array-like of numbers of shape (N, m, 3) or (N, m, 4),
            where the last dimension is RGB or RGBA.
        - array-like of colors of shape (N,) or (N, m).
    ax : matplotlib.axes.Axes, optional
        The axes to plot on. If not provided, the current axes will be used.
    start : array-like, optional
        The ratio of the point where the color starts.
        Should be between 0 and 1.
    end : array-like, optional
        The ratio of the point where the color changes.
        Should be between 0 and 1.
    **kwargs : Any
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.

    """
    for key in ["array", "colors"]:
        if key in kwargs:
            warnings.warn(
                f'The provided "{key}" keyword argument will be overridden',
                UserWarning,
                stacklevel=2,
            )

    # parse args
    if len(args) == 1:
        y = args[0]
        x = np.arange(len(y))
    elif len(args) == 2:
        x, y = args
    else:
        raise ValueError("Invalid number of arguments. Provide either x and y or just y.")

    # ensure x, y, c are 1D or 2D arrays
    x, y, c = map(np.asarray, (x, y, c))
    if x.ndim == 1:
        x = x[:, None]
    elif x.ndim == 2:
        pass
    else:
        raise ValueError(f"{x.ndim=} should be 1 or 2")
    if y.ndim == 1:
        y = y[:, None]
    elif y.ndim == 2:
        pass
    else:
        raise ValueError(f"{y.ndim=} should be 1 or 2")
    x, y = np.broadcast_arrays(x, y)

    if c.ndim == 1:
        c = c[:, None]
    if c.ndim == 2:
        c = np.broadcast_to(c, x.shape).reshape((-1,))
        if np.issubdtype(c.dtype, np.number):
            kwargs["array"] = c
        else:
            kwargs["colors"] = c
    elif c.ndim == 3:
        c = np.broadcast_to(c, (*x.shape, c.shape[-1])).reshape((-1, c.shape[-1]))
        c = [tuple(c[i]) for i in range(c.shape[0])]
        kwargs["colors"] = c
    else:
        raise ValueError(f"{c.ndim=} should be 2 or 3")

    # (N, m, 2)
    xy = np.stack((x, y), axis=-1)
    # (N, m, 2)
    xy_start = np.concat(
        (xy[0, :, :][None, :, :], xy[:-1, :, :] * (1 - start) + xy[1:, :, :] * start), axis=0
    )
    xy_end = np.concat(
        (xy[:-1, :, :] * end + xy[1:, :, :] * (1 - end), xy[-1, :][None, :, :]), axis=0
    )
    segments = np.stack((xy_start, xy, xy_end), axis=-2)
    segments = np.reshape(segments, (-1, segments.shape[-2], segments.shape[-1]))

    lc = LineCollection(segments, **kwargs)

    # Plot the line collection to the axes
    ax = ax or plt.gca()
    ax.add_collection(lc)
    ax.autoscale_view()

    # Return the LineCollection object
    return lc
