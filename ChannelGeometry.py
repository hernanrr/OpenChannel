#!/usr/bin/env python3

import numpy as np


class Rectangular:
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

    def hydraulic_radius(self):
        return self.area() / self.perimeter()

    def top_width(self):
        return self.width

    def hydraulic_depth(self):
        return self.depth

    def shape_function(self):
        numerator = 5 * self.width + 6 * self.depth
        denominator = 3 * self.depth * self.perimeter()
        return numerator / denominator


def main():
    pass


if __name__ == '__main__':
    main()
