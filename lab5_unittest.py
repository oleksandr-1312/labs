import unittest
from lab5 import flood_fill

class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            ['Y', 'Y', 'G'],
            ['Y', 'X', 'X'],
            ['G', 'G', 'X']
        ]

    def test_basic_fill(self):
        expected = [
            ['Y', 'Y', 'G'],
            ['Y', 'C', 'C'],
            ['G', 'G', 'C']
        ]
        result = flood_fill(self.matrix, 1, 1, 'C')
        self.assertEqual(result, expected)

    def test_same_color(self):
        expected = [row[:] for row in self.matrix]
        result = flood_fill(self.matrix, 0, 0, 'Y')
        self.assertEqual(result, expected)

    def test_out_of_bounds(self):
        expected = [row[:] for row in self.matrix]
        result = flood_fill(self.matrix, 10, 10, 'C')
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()