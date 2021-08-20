import unittest
import ChannelGeometry as cg

class TestChannelGeometry(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
