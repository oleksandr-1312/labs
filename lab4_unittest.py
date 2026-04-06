import unittest
from heap_based_priority_queue import PriorityQueue, Node

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("A", 1)
        self.assertEqual(self.pq.peek().value, "A")
        
        self.pq.insert("B", 5)
        self.assertEqual(self.pq.peek().value, "B")
        
        self.pq.insert("C", 3)
        self.assertEqual(self.pq.peek().value, "B")

    def test_extract_max(self):
        self.pq.insert("Low", 1)
        self.pq.insert("High", 10)
        self.pq.insert("Medium", 5)

        self.assertEqual(self.pq.extract_max().value, "High")
        self.assertEqual(self.pq.extract_max().value, "Medium")
        self.assertEqual(self.pq.extract_max().value, "Low")

    def test_equal_priorities(self):
        self.pq.insert("Task 1", 5)
        self.pq.insert("Task 2", 5)
        
        first = self.pq.extract_max()
        second = self.pq.extract_max()
        
        self.assertEqual(first.priority, 5)
        self.assertEqual(second.priority, 5)

    def test_empty_queue(self):
        self.assertTrue(self.pq.is_empty())
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.extract_max())

if __name__ == '__main__':
    unittest.main()