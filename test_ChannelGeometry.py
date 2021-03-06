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

    def test_create_rectangular_channel_invalid(self):
        with self.assertRaises(TypeError):
            cg.Rectangular()

    def test_create_rectangular_channel_store_values(self):
        r = cg.Rectangular(width=10)
        self.assertEqual(r.width, 10)

    def test_create_rectangular_channel_valid(self):
        self.assertEqual(self.rectangular.width, 10)

    def test_rectangular_area(self):
        self.assertEqual(self.rectangular.area(depth=2), 20)

    def test_rectangular_wetted_perimeter(self):
        self.assertEqual(self.rectangular.wetted_perimeter(depth=2), 14)

    def test_rectangular_top_width(self):
        self.assertEqual(self.rectangular.top_width(depth=2), 10)

    def test_rectangular_hydraulic_radius(self):
        self.assertEqual(self.rectangular.hydraulic_radius(depth=2),
                         1.4285714285714286)

    def test_rectangular_hydraulic_depth(self):
        self.assertEqual(self.rectangular.hydraulic_depth(depth=2), 2)

    def test_rectangular_shape_function(self):
        self.assertEqual(self.rectangular.shape_function(depth=2),
                         0.7380952380952381)

    def test_rectangular_invalid_method_call(self):
        with self.assertRaises(ValueError):
            self.rectangular.area(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.area(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.area(depth='foo')

        with self.assertRaises(ValueError):
            self.rectangular.wetted_perimeter(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.wetted_perimeter(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.wetted_perimeter(depth='foo')

        with self.assertRaises(ValueError):
            self.rectangular.top_width(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.top_width(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.top_width(depth='foo')

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_radius(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_radius(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_radius(depth='foo')

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_depth(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_depth(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.hydraulic_depth(depth='foo')

        with self.assertRaises(ValueError):
            self.rectangular.shape_function(depth=0)

        with self.assertRaises(ValueError):
            self.rectangular.shape_function(depth=-2.5)

        with self.assertRaises(ValueError):
            self.rectangular.shape_function(depth='foo')


class TestTriangularChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.triangular = cg.Triangular(side_slope=2)

    def test_create_triangular_channel(self):
        self.triangular = cg.Triangular(side_slope=2)

    def test_create_triangular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Triangular(side_slope=0)

        with self.assertRaises(ValueError):
            cg.Triangular(side_slope=-2)

        with self.assertRaises(ValueError):
            cg.Triangular(side_slope='foo')

    def test_create_triangular_channel_no_argument(self):
        with self.assertRaises(TypeError):
            cg.Triangular()

    def test_create_triangular_channel_store_values(self):
        triangle = cg.Triangular(side_slope=2)
        self.assertEqual(triangle.side_slope, 2)

    def test_create_triangular_channel_valid(self):
        self.assertEqual(self.triangular.side_slope, 2)

    def test_triangular_area(self):
        self.assertEqual(self.triangular.area(depth=2), 8)

    def test_triangular_wetted_perimeter(self):
        self.assertEqual(self.triangular.wetted_perimeter(depth=2),
                         8.94427190999916)

    def test_triangular_top_width(self):
        self.assertEqual(self.triangular.top_width(depth=2), 8)

    def test_triangular_hydraulic_radius(self):
        self.assertEqual(self.triangular.hydraulic_radius(depth=2),
                         0.8944271909999159)

    def test_triangular_hydraulic_depth(self):
        self.assertEqual(self.triangular.hydraulic_depth(depth=2), 1)

    def test_triangular_shape_function(self):
        self.assertEqual(self.triangular.shape_function(depth=2), 4/3)

    def test_triangular_invalid_method_call(self):
        with self.assertRaises(ValueError):
            self.triangular.area(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.area(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.area(depth='foo')

        with self.assertRaises(ValueError):
            self.triangular.wetted_perimeter(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.wetted_perimeter(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.wetted_perimeter(depth='foo')

        with self.assertRaises(ValueError):
            self.triangular.top_width(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.top_width(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.top_width(depth='foo')

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_radius(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_radius(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_radius(depth='foo')

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_depth(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_depth(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.hydraulic_depth(depth='foo')

        with self.assertRaises(ValueError):
            self.triangular.shape_function(depth=0)

        with self.assertRaises(ValueError):
            self.triangular.shape_function(depth=-2.5)

        with self.assertRaises(ValueError):
            self.triangular.shape_function(depth='foo')


class TestTrapezoidalChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.trapezoidal = cg.Trapezoidal(width=2, side_slope=2)

    def test_create_trapezoidal_channel(self):
        self.trapezoidal = cg.Trapezoidal(width=2, side_slope=2)

    def test_create_trapezoidal_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=0, side_slope=2)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=-2, side_slope=2)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width='foo', side_slope=2)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, side_slope=0)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2, side_slope=-2.5)

        with self.assertRaises(ValueError):
            cg.Trapezoidal(width=2,  side_slope='foo')

    def test_create_trapezoidal_channel_wrong_signature(self):
        with self.assertRaises(TypeError):
            cg.Trapezoidal(width=2)

        with self.assertRaises(TypeError):
            cg.Trapezoidal(side_slope=2)

        with self.assertRaises(TypeError):
            cg.Trapezoidal()

    def test_create_trapezoidal_channel_store_values(self):
        trapezoid = cg.Trapezoidal(width=2, side_slope=2)
        self.assertEqual(trapezoid.width, 2)
        self.assertEqual(trapezoid.side_slope, 2)

    def test_create_trapezoidal_channel_valid(self):
        self.assertEqual(self.trapezoidal.width, 2)
        self.assertEqual(self.trapezoidal.side_slope, 2)

    def test_trapezoidal_area(self):
        self.assertEqual(self.trapezoidal.area(depth=2), 12)

    def test_trapezoidal_wetted_perimeter(self):
        self.assertEqual(self.trapezoidal.wetted_perimeter(depth=2),
                         10.94427190999916)

    def test_trapezoidal_top_width(self):
        self.assertEqual(self.trapezoidal.top_width(depth=2), 10)

    def test_trapezoidal_hydraulic_radius(self):
        self.assertEqual(self.trapezoidal.hydraulic_radius(depth=2),
                         1.0964639857893408)

    def test_trapezoidal_hydraulic_depth(self):
        self.assertEqual(self.trapezoidal.hydraulic_depth(depth=2), 1.2)

    def test_trapezoidal_shape_function(self):
        self.assertEqual(self.trapezoidal.shape_function(depth=2),
                         1.1164702214327413)

    def test_trapezoidal_invalid_method_call(self):
        with self.assertRaises(ValueError):
            self.trapezoidal.area(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.area(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.area(depth='foo')

        with self.assertRaises(ValueError):
            self.trapezoidal.wetted_perimeter(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.wetted_perimeter(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.wetted_perimeter(depth='foo')

        with self.assertRaises(ValueError):
            self.trapezoidal.top_width(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.top_width(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.top_width(depth='foo')

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_radius(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_radius(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_radius(depth='foo')

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_depth(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_depth(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.hydraulic_depth(depth='foo')

        with self.assertRaises(ValueError):
            self.trapezoidal.shape_function(depth=0)

        with self.assertRaises(ValueError):
            self.trapezoidal.shape_function(depth=-2.5)

        with self.assertRaises(ValueError):
            self.trapezoidal.shape_function(depth='foo')


class TestCircularChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.circular = cg.Circular(diameter=2)

    def test_create_circular_channel(self):
        self.circular = cg.Circular(diameter=2)

    def test_create_circular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Circular(diameter=0)

        with self.assertRaises(ValueError):
            cg.Circular(diameter=-2)

        with self.assertRaises(ValueError):
            cg.Circular(diameter='foo')

    # def test_create_circular_channel_invalid_depth(self):
    #     with self.assertRaises(ValueError):
    #         cg.Circular(diameter=1, depth=2)

    def test_create_circular_channel_wrong_signature(self):
        with self.assertRaises(TypeError):
            cg.Circular()

    def test_create_circular_channel_store_values(self):
        circle = cg.Circular(diameter=2)
        self.assertEqual(circle.diameter, 2)

    def test_create_circular_channel_valid(self):
        self.assertEqual(self.circular.diameter, 2)

    def test_circular_area(self):
        self.assertEqual(self.circular.area(depth=1), math.pi/2)

    def test_circular_wetted_perimeter(self):
        self.assertEqual(self.circular.wetted_perimeter(depth=1), math.pi)

    def test_circular_top_width(self):
        self.assertEqual(self.circular.top_width(depth=1), 2)

    def test_circular_hydraulic_radius(self):
        self.assertEqual(self.circular.hydraulic_radius(depth=1), 0.5)

    def test_circular_hydraulic_depth(self):
        self.assertEqual(self.circular.hydraulic_depth(depth=1), math.pi/4)

    def test_circular_shape_function(self):
        self.assertEqual(self.circular.shape_function(depth=1),
                         1.6976527263135504)

    def test_circular_invalid_method_call(self):
        with self.assertRaises(ValueError):
            self.circular.area(depth=0)

        with self.assertRaises(ValueError):
            self.circular.area(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.area(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.area(depth=2.5)

        with self.assertRaises(ValueError):
            self.circular.wetted_perimeter(depth=0)

        with self.assertRaises(ValueError):
            self.circular.wetted_perimeter(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.wetted_perimeter(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.wetted_perimeter(depth=2.5)

        with self.assertRaises(ValueError):
            self.circular.top_width(depth=0)

        with self.assertRaises(ValueError):
            self.circular.top_width(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.top_width(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.top_width(depth=2.5)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_radius(depth=0)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_radius(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_radius(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.hydraulic_radius(depth=2.5)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_depth(depth=0)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_depth(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.hydraulic_depth(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.hydraulic_depth(depth=2.5)

        with self.assertRaises(ValueError):
            self.circular.shape_function(depth=0)

        with self.assertRaises(ValueError):
            self.circular.shape_function(depth=-2.5)

        with self.assertRaises(ValueError):
            self.circular.shape_function(depth='foo')

        with self.assertRaises(ValueError):
            self.circular.shape_function(depth=2.5)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
