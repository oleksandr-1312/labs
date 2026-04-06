import unittest
from lab5 import shortest_path_maze

class TestMazeShortestPath(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

    def test_example_path(self):
        start = (0, 0)
        end = (7, 5)
        self.assertEqual(shortest_path_maze(self.matrix, start, end), 12)

    def test_no_path(self):
        start = (0, 0)
        end = (0, 9)
        self.assertEqual(shortest_path_maze(self.matrix, start, end), -1)

    def test_start_is_end(self):
        start = (0, 0)
        end = (0, 0)
        self.assertEqual(shortest_path_maze(self.matrix, start, end), 0)

    def test_start_is_wall(self):
        start = (1, 0)
        end = (7, 5)
        self.assertEqual(shortest_path_maze(self.matrix, start, end), -1)

if __name__ == "__main__":
    unittest.main()