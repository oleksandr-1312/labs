import unittest
from lab2 import calc_minimum_cost, merge_sort

class TestMergeSort(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [9, 6, 5, 4, 3, 2, 1, 1])

    def test_already_sorted(self):
        self.assertEqual(merge_sort([10, 8, 5, 2]), [10, 8, 5, 2])

    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([42]), [42])

class TestMinimumCost(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(calc_minimum_cost([50, 20, 30, 17, 100], 10), "207.00")

    def test_example_2(self):
        self.assertEqual(calc_minimum_cost([1, 2, 3, 4, 5, 6, 7], 100), "15.00")

    def test_example_3(self):
        self.assertEqual(calc_minimum_cost([1, 1, 1], 33), "2.67")
        
    def test_no_discount_items(self):
        self.assertEqual(calc_minimum_cost([10, 20], 50), "30.00")

if __name__ == '__main__':
    unittest.main()