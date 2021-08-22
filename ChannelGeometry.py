#!/usr/bin/env python3

import math
import numpy as np
from abc import ABC, abstractmethod
from typing import Union


class ChannelXSection(ABC):
    """A class to represent channel cross-sections."""
    @abstractmethod
    def area(self) -> float:
        """Returns the wetted area of the channel cross-section."""
        pass

    @abstractmethod
    def wetted_perimeter(self) -> float:
        """Returns the wetted perimeter of the channel cross-section."""
        pass

    @abstractmethod
    def top_width(self) -> float:
        """Returns the water surface width of the channel cross-section."""
        pass

    @abstractmethod
    def shape_function(self) -> float:
        r"""Returns the channel shape function of the cross-section.

        Notes
        -----
        The channel shape function results from the solution to Manning's
        equation for normal depth using the Newton-Raphson method. It is
        defined as:

        .. math::
        \left(\frac{2}{3R}\frac{dR}{dy} + \frac{1}{A}\frac{dA}{dy} \right)

        where R and y are the hydraulic radius and the water depth
        respectively.
        """
        pass

    def hydraulic_radius(self) -> float:
        """Returns the hydraulic radius of the channel cross-section."""
        return self.area() / self.wetted_perimeter()

    def hydraulic_depth(self) -> float:
        """Returns the hydraulic depth of the channel cross-section."""
        return self.area() / self.top_width()


class Rectangular(ChannelXSection):
    """A class to represent rectangular channel cross-sections.

    Parameters
    ----------
    width : int or float
        Bottom width of the channel [m] or [ft]
    depth : int or float
        Water surface elevation from the bottom of the channel [m] or [ft]

    Raises
    ------
    ValueError
    Only accepts positive, real numbers (int or float).

    Notes
    -----
    Unit consistency, correctness and compatibility is the user's
    responsibility.

    Examples
    --------
    >>> foo = Rectangular(10, 2)
    >>> foo.width
    10
    >>> foo.depth
    2

    """
    def __init__(self, width: Union[int, float],
                 depth: Union[int, float]) -> None:
        """Constructor for rectangular channel cross-section."""

        if not isinstance(width, (float, int)) or width <= 0:
            raise ValueError('Width must be a positive number')
        if not isinstance(depth, (float, int)) or depth <= 0:
            raise ValueError('Depth must be a positive number')

        self.width = float(width)
        self.depth = float(depth)

    def area(self) -> float:
        return self.width * self.depth

    def wetted_perimeter(self) -> float:
        return self.width + 2 * self.depth

    def top_width(self) -> float:
        return self.width

    def shape_function(self) -> float:
        numerator = 5 * self.width + 6 * self.depth
        denominator = 3 * self.depth * self.wetted_perimeter()
        return numerator / denominator


class Triangular(ChannelXSection):
    """A class to represent symmetrical triangular channel cross-sections.

    Parameters
    ----------
    depth : int or float
        Water surface elevation from the bottom of the channel [m] or [ft]
    side_slope : int or float
        Horizontal distance per unit vertical rise of the side

    Raises
    ------
    ValueError
    Only accepts positive, real numbers (int or float).

    Notes
    -----
    Unit consistency, correctness and compatibility is the user's
    responsibility.

    Examples
    --------
    >>> triangle = Triangular(2, 2)
    >>> triangle.depth
    2
    >>> triangle.side_slope
    2
    """

    def __init__(self, depth: Union[int, float],
                 side_slope: Union[int, float]) -> None:

        if not isinstance(depth, (float, int)) or depth <= 0:
            raise ValueError('Depth must be a positive number')
        if not isinstance(side_slope, (float, int)) or side_slope <= 0:
            raise ValueError('Side slope must be a positive number')

        self.depth = depth
        self.side_slope = side_slope

    def area(self) -> float:
        return self.side_slope * self.depth ** 2

    def wetted_perimeter(self) -> float:
        return 2 * self.depth * math.sqrt(1 + self.side_slope ** 2)

    def top_width(self) -> float:
        return 2 * self.depth * self.side_slope

    def shape_function(self) -> float:
        return 8 / (3 * self.depth)


class Trapezoidal(ChannelXSection):
    """A class to represent symmetrical trapezoidal channel cross-sections.

    Parameters
    ----------
    width : int or float
        Bottom width of the channel [m] or [ft]
    depth : int or float
        Water surface elevation from the bottom of the channel [m] or [ft]
    side_slope : int or float
        Horizontal distance per unit vertical rise of the side

    Raises
    ------
    ValueError
    Only accepts positive, real numbers (int or float).

    Notes
    -----
    Unit consistency, correctness and compatibility is the user's
    responsibility.

    Examples
    --------
    >>> trapezoid = Trapezoidal(10, 2, 2)
    >>> trapezoid.width
    10
    >>> trapezoid.depth
    2
    >>> trapezoid.side_slope
    2
    """
    def __init__(self, width: Union[int, float], depth: Union[int, float],
                 side_slope: Union[int, float]) -> None:

        if not isinstance(width, (float, int)) or width <= 0:
            raise ValueError('Width must be a positive number')
        if not isinstance(depth, (float, int)) or depth <= 0:
            raise ValueError('Depth must be a positive number')
        if not isinstance(side_slope, (float, int)) or side_slope <= 0:
            raise ValueError('Side slope must be a positive number')

        self.width = width
        self.depth = depth
        self.side_slope = side_slope

    def area(self) -> float:
        return (self.width + self.side_slope * self.depth) * self.depth

    def wetted_perimeter(self) -> float:
        return (self.width
                + 2 * self.depth * math.sqrt(1 + self.side_slope ** 2))

    def top_width(self) -> float:
        return self.width + 2 * self.depth * self.side_slope

    def shape_function(self) -> float:
        A = math.sqrt(1 + self.side_slope ** 2)
        numerator = (self.top_width()
                     * (5 * self.width + 6 * self.depth * A)
                     + (4 * self.side_slope * self.depth ** 2 * A))
        denominator = (3 * self.depth
                       * (self.width + self.depth * self.side_slope)
                       * (self.width + 2 * self.depth * A))
        return numerator / denominator


class Circular(ChannelXSection):
    """A class to represent circular channel cross-sections.

    Parameters
    ----------
    diameter : int or float
        Channel diameter or pipe inner diameter [m] or [ft]
    depth : int or float
        Water surface elevation from lowest point of the channel [m] or [ft]

    Raises
    ------
    ValueError
    Only accepts positive, real numbers (int or float).

    Notes
    -----
    Unit consistency, correctness and compatibility is the user's
    responsibility.

    Examples
    --------
    >>> circle = Circular(0.2, 0.1)
    >>> circle.diameter
    0.2
    >>> circle.depth
    0.1
    """

    def __init__(self, diameter: Union[int, float],
                 depth: Union[int, float]) -> None:

        if not isinstance(diameter, (float, int)) or diameter <= 0:
            raise ValueError('Diameter must be a positive number')
        if not isinstance(depth, (float, int)) or depth <= 0:
            raise ValueError('Depth must be a positive number')
        if depth > diameter:
            raise ValueError('Depth must be smaller or equal than diameter')

        self.diameter = diameter
        self.depth = depth
        self.theta = 2 * math.acos(1 - (2 * depth) / diameter)

    def area(self) -> float:
        return ((1 / 8)
                * (self.theta - math.sin(self.theta))
                * self.diameter ** 2)

    def wetted_perimeter(self):
        return 1 / 2 * self.theta * self.diameter

    def top_width(self) -> float:
        return math.sin(self.theta / 2) * self.diameter

    def shape_function(self) -> float:
        numerator = (4 * (2 * math.sin(self.theta)
                          + 3 * self.theta
                          - 5 * self.theta * math.cos(self.theta)))
        denominator = (3 * self.diameter * self.theta
                       * (self.theta - math.sin(self.theta))
                       * math.sin(self.theta / 2))
        return numerator / denominator


def main():
    pass


if __name__ == '__main__':
    main()
