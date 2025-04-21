from __future__ import annotations

import warnings
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from numpy.typing import ArrayLike


def colored_line(
    x: ArrayLike,
    y: ArrayLike,
    c: ArrayLike,
    ax: Axes | None = None,
    scalex: bool = True,
    scaley: bool = True,
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
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should be the same size as x and y.
    ax : matplotlib.axes.Axes, optional
        The axes to plot on. If not provided, the current axes will be used.
    scalex, scaley : bool
        These parameters determine if the view limits are adapted to the data limits.
        The values are passed on to autoscale_view.
    **kwargs : Any
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.

    """
    if "array" in kwargs:
        warnings.warn(
            'The provided "array" keyword argument will be overridden',
            UserWarning,
            stacklevel=2,
        )

    xy = np.stack((x, y), axis=-1)
    xy_mid = np.concat(
        (xy[0, :][None, :], (xy[:-1, :] + xy[1:, :]) / 2, xy[-1, :][None, :]), axis=0
    )
    segments = np.stack((xy_mid[:-1, :], xy, xy_mid[1:, :]), axis=-2)
    # Note that segments is [
    #   [[x[0], y[0]], [x[0], y[0]], [mean(x[0], x[1]), mean(y[0], y[1])]],
    #   [[mean(x[0], x[1]), mean(y[0], y[1])], [x[1], y[1]], [mean(x[1], x[2]), mean(y[1], y[2])]],
    #   ...
    #   [[mean(x[-2], x[-1]), mean(y[-2], y[-1])], [x[-1], y[-1]], [x[-1], y[-1]]]
    # ]

    kwargs["array"] = c
    lc = LineCollection(segments, **kwargs)

    # Plot the line collection to the axes
    ax = ax or plt.gca()
    ax.add_collection(lc)
    ax.autoscale_view(scalex=scalex, scaley=scaley)

    # Return the LineCollection object
    return lc
