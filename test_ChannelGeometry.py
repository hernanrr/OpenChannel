import unittest
import ChannelGeometry as cg

class TestChannelGeometry(unittest.TestCase):

    def setUp(self):
        self.rectangular = cg.Rectangular(width=10, depth=2)

    def test_create_rectangular_channel(self):
        self.rectangular = cg.Rectangular(width=10, depth=2)

    def test_create_rectangular_channel_invalid_size(self):
        with self.assertRaises(ValueError):
            cg.Rectangular(width=0, depth=2)

        with self.assertRaises(ValueError):
            cg.Rectangular(width=-2.5, depth=2)

        with self.assertRaises(ValueError):
            cg.Rectangular(width='foo', depth=2)

        with self.assertRaises(ValueError):
            cg.Rectangular(width=10, depth=0)

        with self.assertRaises(ValueError):
            cg.Rectangular(width=10, depth=-2.5)

        with self.assertRaises(ValueError):
            cg.Rectangular(width=-2.5, depth='foo')

        with self.assertRaises(ValueError):
            cg.Rectangular(width=-2.5, depth=-2)

    def test_create_rectangular_channel_single_side(self):
        with self.assertRaises(TypeError):
            cg.Rectangular(width=0)

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
        self.assertAlmostEqual(self.rectangular.hydraulic_radius(), 1.42857142)

    def test_rectangular_hydraulic_depth(self):
        self.assertEqual(self.rectangular.hydraulic_depth(), 2)


if __name__ == '__main__':
    unittest.main()
