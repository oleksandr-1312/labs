import unittest

from lab1 import is_subarray

class TestSubarrayFunction(unittest.TestCase):

    def test_normal_case(self):
        result = is_subarray([2, 3], [1, 2, 3, 4])
        print("Тест 1 (Звичайний випадок):", result)
        self.assertEqual(result, True)

    def test_at_beginning(self):
        result = is_subarray([1, 2], [1, 2, 3, 4])
        print("Тест 2 (Підмасив на початку):", result)
        self.assertEqual(result, True)

    def test_not_consecutive(self):
        result = is_subarray([1, 3], [1, 2, 3, 4])
        print("Тест 3 (Не підряд):", result)
        self.assertEqual(result, False)

    def test_missing_elements(self):
        result = is_subarray([5, 6], [1, 2, 3, 4])
        print("Тест 4 (Елементів немає):", result)
        self.assertEqual(result, False)

    def test_full_match(self):
        result = is_subarray([1, 2, 3], [1, 2, 3])
        print("Тест 5 (Повний збіг):", result)
        self.assertEqual(result, True)

if is_subarray == 'main':
    unittest.main()

