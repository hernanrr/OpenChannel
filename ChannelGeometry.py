#!/usr/bin/env python3

import math
from abc import ABC, abstractmethod
from typing import Union, Callable
import logging


def check_valid_positive_number(**kwargs):
    for key, value in kwargs.items():
        if not isinstance(value, (float, int)) or value <= 0:
            message = f'{key} must be a positive number'
            logging.error(message, stack_info=False)
            raise ValueError(message)
    return None


def check_depth_le_diameter(diameter, depth):
    if depth > diameter:
        logging.error('Depth exceeds diameter', stack_info=False)
        raise ValueError('Depth must be less than or equal to diameter.')
    return None


class ChannelXSection(ABC):
    """A class to represent channel cross-sections."""
    @abstractmethod
    def area(self, depth: Union[int, float]) -> Callable[[float], float]:
        """Returns a function for the area of the channel cross-section."""

    @abstractmethod
    def wetted_perimeter(self, depth: Union[int, float]) -> Callable[[float],
                                                                     float]:
        """Returns a function for wetted perimeter of the channel."""

    @abstractmethod
    def top_width(self, depth: Union[int, float]) -> Callable[[float], float]:
        """Returns  a function forthe water surface width of the channel."""

    @abstractmethod
    def shape_function(self, depth: Union[int, float]) -> Callable[[float],
                                                                   float]:
        r"""Returns a function for the channel shape function of the channel.

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

    def hydraulic_radius(self, depth) -> float:
        """Returns a function for the hydraulic radius of the channel."""
        check_valid_positive_number(Depth=depth)
        return self.area(depth) / self.wetted_perimeter(depth)

    def hydraulic_depth(self, depth) -> float:
        """Returns a function for the hydraulic depth of the channel."""
        check_valid_positive_number(Depth=depth)
        return self.area(depth) / self.top_width(depth)


class Rectangular(ChannelXSection):
    """A class to represent rectangular channel cross-sections.

    Parameters
    ----------
    width : int or float
        Bottom width of the channel [m] or [ft]

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
    >>> rectangle = Rectangular(10)
    >>> rectangle.width
    10.0

    """
    def __init__(self, width: Union[int, float]) -> None:
        """Constructor for rectangular channel cross-section."""
        check_valid_positive_number(Width=width)
        self.width = float(width)

    def area(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return depth * self.width

    def wetted_perimeter(self, depth: Union[int, float]) -> Callable[[float],
                                                                     float]:
        check_valid_positive_number(Depth=depth)
        return self.width + 2 * depth

    def top_width(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return self.width

    def shape_function(self, depth: Union[int, float]) -> Callable[[float],
                                                                   float]:
        check_valid_positive_number(Depth=depth)
        return ((5 * self.width + 6 * depth)
                / (3 * depth * self.wetted_perimeter(depth)))


class Triangular(ChannelXSection):
    """A class to represent symmetrical triangular channel cross-sections.

    Parameters
    ----------
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
    >>> triangle = Triangular(2)
    >>> triangle.side_slope
    2
    """

    def __init__(self, side_slope: Union[int, float]) -> None:
        check_valid_positive_number(**{'Side slope': side_slope})
        self.side_slope = side_slope

    def area(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return self.side_slope * depth ** 2

    def wetted_perimeter(self,
                         depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return 2 * depth * math.sqrt(1 + self.side_slope ** 2)

    def top_width(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return 2 * depth * self.side_slope

    def shape_function(self, depth: Union[int, float]) -> Callable[[float],
                                                                   float]:
        check_valid_positive_number(Depth=depth)
        return 8 / (3 * depth)


class Trapezoidal(ChannelXSection):
    """A class to represent symmetrical trapezoidal channel cross-sections.

    Parameters
    ----------
    width : int or float
        Bottom width of the channel [m] or [ft]
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
    >>> trapezoid.side_slope
    2
    """
    def __init__(self, width: Union[int, float],
                 side_slope: Union[int, float]) -> None:

        check_valid_positive_number(Width=width)
        check_valid_positive_number(**{'Side slope': side_slope})

        self.width = width
        self.side_slope = side_slope

    def area(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return (self.width + self.side_slope * depth) * depth

    def wetted_perimeter(self, depth: Union[int, float]) -> Callable[[float],
                                                                     float]:
        check_valid_positive_number(Depth=depth)
        return (self.width + 2 * depth * math.sqrt(1 + self.side_slope ** 2))

    def top_width(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        return self.width + 2 * depth * self.side_slope

    def shape_function(self, depth: Union[int, float]) -> Callable[[float],
                                                                   float]:
        check_valid_positive_number(Depth=depth)
        A = math.sqrt(1 + self.side_slope ** 2)
        numerator = (self.top_width(depth)
                     * (5 * self.width + 6 * depth * A)
                     + (4 * self.side_slope * depth ** 2 * A))
        denominator = (3 * depth
                       * (self.width + depth * self.side_slope)
                       * (self.width + 2 * depth * A))
        return numerator / denominator


class Circular(ChannelXSection):
    """A class to represent circular channel cross-sections.

    Parameters
    ----------
    diameter : int or float
        Channel diameter or pipe inner diameter [m] or [ft]

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
    """

    def __init__(self, diameter: Union[int, float]) -> None:
        check_valid_positive_number(Diameter=diameter)
        self.diameter = diameter

    def area(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        check_depth_le_diameter(self.diameter, depth)
        theta = 2 * math.acos(1 - (2 * depth) / self.diameter)
        return ((1 / 8)
                * (theta - math.sin(theta))
                * self.diameter ** 2)

    def wetted_perimeter(self, depth: Union[int, float]) -> Callable[[float],
                                                                     float]:
        check_valid_positive_number(Depth=depth)
        check_depth_le_diameter(self.diameter, depth)
        theta = 2 * math.acos(1 - (2 * depth) / self.diameter)
        return 1 / 2 * theta * self.diameter

    def top_width(self, depth: Union[int, float]) -> Callable[[float], float]:
        check_valid_positive_number(Depth=depth)
        check_depth_le_diameter(self.diameter, depth)
        theta = 2 * math.acos(1 - (2 * depth) / self.diameter)
        return math.sin(theta / 2) * self.diameter

    def shape_function(self, depth: Union[int, float]) -> Callable[[float],
                                                                   float]:
        check_valid_positive_number(Depth=depth)
        check_depth_le_diameter(self.diameter, depth)
        theta = 2 * math.acos(1 - (2 * depth) / self.diameter)
        numerator = (4 * (2 * math.sin(theta)
                          + 3 * theta
                          - 5 * theta * math.cos(theta)))
        denominator = (3 * self.diameter * theta
                       * (theta - math.sin(theta))
                       * math.sin(theta / 2))
        return numerator / denominator


def main():
    """ Not implemented yet. """


if __name__ == '__main__':
    main()  # pragma: no cover
