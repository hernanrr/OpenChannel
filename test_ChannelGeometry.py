import unittest
import ChannelGeometry as cg
import math


class TestRectangularChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.rectangular = cg.Rectangular(width=10)

    def test_create_rectangular_channel(self):
        self.rectangular = cg.Rectangular(width=10)

    def test_create_rectangular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Rectangular(width=0)

        with self.assertRaises(ValueError):
            cg.Rectangular(width=-2.5)

        with self.assertRaises(ValueError):
            cg.Rectangular(width='foo')

    def test_create_rectangular_channel_single_side(self):
        with self.assertRaises(TypeError):
            cg.Rectangular()

        with self.assertRaises(TypeError):
            cg.Rectangular(depth=0)

    def test_create_rectangular_channel_store_values(self):
        r = cg.Rectangular(width=10, depth=2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.depth, 2)

    def test_create_rectangular_channel_valid(self):
        self.assertEqual(self.rectangular.width, 10)
        self.assertEqual(self.rectangular.depth, 2)

    def test_rectangular_area(self):
        self.assertEqual(self.rectangular.area(), 20)

    def test_rectangular_wetted_perimeter(self):
        self.assertEqual(self.rectangular.wetted_perimeter(), 14)

    def test_rectangular_top_width(self):
        self.assertEqual(self.rectangular.top_width(), 10)

    def test_rectangular_hydraulic_radius(self):
        self.assertEqual(self.rectangular.hydraulic_radius(),
                         1.4285714285714286)

    def test_rectangular_hydraulic_depth(self):
        self.assertEqual(self.rectangular.hydraulic_depth(), 2)

    def test_rectangular_shape_function(self):
        self.assertEqual(self.rectangular.shape_function(), 0.7380952380952381)


class TestTriangularChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.triangular = cg.Triangular(depth=2, side_slope=2)

    def test_create_triangular_channel(self):
        self.triangular = cg.Triangular(depth=2, side_slope=2)

    def test_create_triangular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Triangular(depth=0, side_slope=2)

        with self.assertRaises(ValueError):
            cg.Triangular(depth=-2.5, side_slope=2)

        with self.assertRaises(ValueError):
            cg.Triangular(depth='foo', side_slope=2)

        with self.assertRaises(ValueError):
            cg.Triangular(depth=2, side_slope=0)

        with self.assertRaises(ValueError):
            cg.Triangular(depth=2, side_slope=-2.5)

        with self.assertRaises(ValueError):
            cg.Triangular(depth=-2, side_slope='foo')

        with self.assertRaises(ValueError):
            cg.Triangular(depth=-2, side_slope=-2)

    def test_create_triangular_channel_single_argument(self):
        with self.assertRaises(TypeError):
            cg.Triangular(depth=2)

        with self.assertRaises(TypeError):
            cg.Triangular(side_slope=2)

    def test_create_triangular_channel_store_values(self):
        triangle = cg.Triangular(depth=2, side_slope=2)
        self.assertEqual(triangle.depth, 2)
        self.assertEqual(triangle.side_slope, 2)

    def test_create_triangular_channel_valid(self):
        self.assertEqual(self.triangular.depth, 2)
        self.assertEqual(self.triangular.side_slope, 2)

    def test_triangular_area(self):
        self.assertEqual(self.triangular.area(), 8)

    def test_triangular_wetted_perimeter(self):
        self.assertEqual(self.triangular.wetted_perimeter(),
                         8.94427190999916)

    def test_triangular_top_width(self):
        self.assertEqual(self.triangular.top_width(), 8)

    def test_triangular_hydraulic_radius(self):
        self.assertEqual(self.triangular.hydraulic_radius(),
                         0.8944271909999159)

    def test_triangular_hydraulic_depth(self):
        self.assertEqual(self.triangular.hydraulic_depth(), 1)

    def test_triangular_shape_function(self):
        self.assertEqual(self.triangular.shape_function(), 4/3)


class TestTrapezoidalChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.trapezoidal = cg.Trapezoidal(width=2, depth=2, side_slope=2)

    def test_create_trapezoidal_channel(self):
        self.trapezoidal = cg.Trapezoidal(width=2, depth=2, side_slope=2)

    def test_create_trapezoidal_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=0, depth=0, side_slope=0)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, depth=-2.5, side_slope=2)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=-2, depth='foo', side_slope=2)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=-2, depth=2, side_slope=0)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, depth=2, side_slope=-2.5)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, depth=-2, side_slope='foo')

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, depth=-2, side_slope=-2)

    def test_create_trapezoidal_channel_single_argument(self):
        with self.assertRaises(TypeError):
            cg.Trapezoidal(width=2, depth=2)

        with self.assertRaises(TypeError):
            cg.Trapezoidal(width=2, side_slope=2)

    def test_create_trapezoidal_channel_store_values(self):
        trapezoid = cg.Trapezoidal(width=2, depth=2, side_slope=2)
        self.assertEqual(trapezoid.width, 2)
        self.assertEqual(trapezoid.depth, 2)
        self.assertEqual(trapezoid.side_slope, 2)

    def test_create_trapezoidal_channel_valid(self):
        self.assertEqual(self.trapezoidal.width, 2)
        self.assertEqual(self.trapezoidal.depth, 2)
        self.assertEqual(self.trapezoidal.side_slope, 2)

    def test_trapezoidal_area(self):
        self.assertEqual(self.trapezoidal.area(), 12)

    def test_trapezoidal_wetted_perimeter(self):
        self.assertEqual(self.trapezoidal.wetted_perimeter(),
                         10.94427190999916)

    def test_trapezoidal_top_width(self):
        self.assertEqual(self.trapezoidal.top_width(), 10)

    def test_trapezoidal_hydraulic_radius(self):
        self.assertEqual(self.trapezoidal.hydraulic_radius(),
                         1.0964639857893408)

    def test_trapezoidal_hydraulic_depth(self):
        self.assertEqual(self.trapezoidal.hydraulic_depth(), 1.2)

    def test_trapezoidal_shape_function(self):
        self.assertEqual(self.trapezoidal.shape_function(), 1.1164702214327413)


class TestCircularChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.circular = cg.Circular(diameter=2, depth=1)

    def test_create_circular_channel(self):
        self.circular = cg.Circular(diameter=4, depth=2)

    def test_create_circular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Circular(diameter=0, depth=1)

        with self.assertRaises(ValueError):
            cg.Circular(diameter=2, depth=-0.5)

        with self.assertRaises(ValueError):
            cg.Circular(diameter=-2, depth='foo')

        with self.assertRaises(ValueError):
            cg.Circular(diameter=-2, depth=2)

        with self.assertRaises(ValueError):
            cg.Circular(diameter=2, depth=0)

        with self.assertRaises(ValueError):
            cg.Circular(diameter='foo', depth=-2)

        with self.assertRaises(ValueError):
            cg.Circular(diameter=2, depth=0)

    def test_create_circular_channel_invalid_depth(self):
        with self.assertRaises(ValueError):
            cg.Circular(diameter=1, depth=2)

    def test_create_circular_channel_single_argument(self):
        with self.assertRaises(TypeError):
            cg.Circular(diameter=2)

        with self.assertRaises(TypeError):
            cg.Circular(depth=2)

    def test_create_circular_channel_store_values(self):
        circle = cg.Circular(diameter=2, depth=1)
        self.assertEqual(circle.diameter, 2)
        self.assertEqual(circle.depth, 1)

    def test_create_circular_channel_valid(self):
        self.assertEqual(self.circular.diameter, 2)
        self.assertEqual(self.circular.depth, 1)
        self.assertGreaterEqual(self.circular.diameter, self.circular.depth)

    def test_circular_area(self):
        self.assertEqual(self.circular.area(), math.pi/2)

    def test_circular_wetted_perimeter(self):
        self.assertEqual(self.circular.wetted_perimeter(), math.pi)

    def test_circular_top_width(self):
        self.assertEqual(self.circular.top_width(), 2)

    def test_circular_hydraulic_radius(self):
        self.assertEqual(self.circular.hydraulic_radius(), 0.5)

    def test_circular_hydraulic_depth(self):
        self.assertEqual(self.circular.hydraulic_depth(), math.pi/4)

    def test_circular_shape_function(self):
        self.assertEqual(self.circular.shape_function(), 1.6976527263135504)


if __name__ == '__main__':
    unittest.main()
