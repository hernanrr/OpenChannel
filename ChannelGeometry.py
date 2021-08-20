#!/usr/bin/env python3

import math
import numpy as np
from abc import ABC, abstractmethod


class ChannelXSection(ABC):
    """A class to represent channel cross-sections."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def wetted_perimeter(self):
        pass

    @abstractmethod
    def top_width(self):
        pass

    @abstractmethod
    def shape_function(self):
        pass

    def hydraulic_radius(self):
        return self.area() / self.wetted_perimeter()

    def hydraulic_depth(self):
        return self.area() / self.top_width()


class Rectangular(ChannelXSection):
    """
    A class to represent rectangular channel cross-sections.

    Parameters
    ----------
    width : int or float
    Bottom width of the channel
    depth : int or float
        Water surface elevation measured from the bottom of the channel.

    Raises
    ------
    ValueError
    Only accepts positive, real numbers (int or float).



    Examples
    --------
    >>> foo = Rectangular(10, 2)
    >>> foo.width
    array(10)
    >>> foo.depth
    array(2)

    """
    def __init__(self, width, depth):
        """Constructor for rectangular channel cross-section."""
        width = np.array(width)
        depth = np.array(depth)

        if width.dtype.type is np.str_ or np.all(width <= 0):
            raise ValueError('Width must be a positive number')
        if depth.dtype.type is np.str_ or np.all(depth <= 0):
            raise ValueError('Depth must be a positive number')

        self.width = width
        self.depth = depth

    def area(self):
        return self.width * self.depth

    def wetted_perimeter(self):
        return self.width + 2 * self.depth

    def top_width(self):
        return self.width

    def shape_function(self):
        numerator = 5 * self.width + 6 * self.depth
        denominator = 3 * self.depth * self.wetted_perimeter()
        return numerator / denominator


class Triangular(ChannelXSection):
    def __init__(self, depth, slope):
        self.depth = depth
        self.slope = slope

    def area(self):
        return self.slope * self.depth ** 2

    def wetted_perimeter(self):
        return 2 * self.depth * math.sqrt(1 + self.slope ** 2)

    def top_width(self):
        return 2 * self.depth * self.slope

    def shape_function(self):
        return 8 / (3 * self.depth)


class Trapezoidal(ChannelXSection):
    def __init__(self, width, depth, slope):
        self.width = width
        self.depth = depth
        self.slope = slope

    def area(self):
        return (self.width + self.slope * self.depth) * self.depth

    def wetted_perimeter(self):
        return (self.width
                + 2 * self.depth * math.sqrt(1 + self.slope ** 2))

    def top_width(self):
        return self.width + 2 * self.depth * self.slope

    def shape_function(self):
        A = math.sqrt(1 + self.slope ** 2)
        numerator = (self.top_width
                     * (5 * self.width + 6 * self.depth * A)
                     * (4 * self.slope * self.depth ** 2 * A))
        denominator = (3 * self.depth
                       * (self.width + self.depth * self.slope)
                       * (self.width + 2 * self.depth * A))
        return numerator / denominator


class Circular(ChannelXSection):
    def __init__(self, diameter, depth):
        self.diameter = diameter
        self.depth = depth
        self.theta = 2 * math.acos(1 - (2 * depth)/diameter)

    def area(self):
        return ((1 / 8)
                * (self.theta - math.sin(self.theta))
                * self.diameter ** 2)

    def wetted_perimeter(self):
        return 1/2 * self.theta * self.diameter

    def top_width(self):
        return math.sin(self.theta/2) * self.diameter

    def shape_function(self):
        numerator = (4 * (2 * math.sin(self.theta)
                          + 3 * self.theta
                          - 5 * self.theta * math.cos(self.theta)))
        denominator = (3 * self.diameter * self.theta
                       * (self.theta - math.sin(self.theta))
                       * math.sin(self.theta/2))
        return numerator / denominator


def main():
    pass


if __name__ == '__main__':
    main()
