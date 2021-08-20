#!/usr/bin/env python3

import math
import numpy as np


class ChannelXSection:
    def hydraulic_radius(self):
        return self.area() / self.perimeter()

    def hydraulic_depth(self):
        return self.area() / self.top_width()


class Rectangular(ChannelXSection):
    def __init__(self, width, depth):
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

    def perimeter(self):
        return self.width + 2 * self.depth

    def top_width(self):
        return self.width

    def shape_function(self):
        numerator = 5 * self.width + 6 * self.depth
        denominator = 3 * self.depth * self.perimeter()
        return numerator / denominator


class Triangular(ChannelXSection):
    def __init__(self, depth, slope):
        self.depth = depth
        self.slope = slope

    def area(self):
        return self.slope * self.depth ** 2

    def perimeter(self):
        return 2 * self.depth * math.sqrt(1 + self.slope ** 2)

    def top_width(self):
        return 2 * self.depth * self.slope

    def shape_function(self):
        return 8 / (3 * self.depth)


def main():
    pass


if __name__ == '__main__':
    main()
