import unittest
from lab3 import BinaryTree, branchSums

class TestBranchSums(unittest.TestCase):
    
    def test_example_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(branchSums(root), 24)

    def test_no_left_leaves(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        self.assertEqual(branchSums(root), 0)

    def test_single_node(self):
        root = BinaryTree(1)
        self.assertEqual(branchSums(root), 0)

    def test_empty_tree(self):
        self.assertEqual(branchSums(None), 0)

if __name__ == '__main__':
    unittest.main()