import unittest
from data_structures.binary_tree import BinaryTreeNode, BinaryTree

class TestLinkedListMethods(unittest.TestCase):

    def test_add_root(self):
        root = BinaryTreeNode('root node')
        binary_tree = BinaryTree(root)
        self.assertEqual(binary_tree.get_root().value, 'root node')

if __name__ == '__main__':
    unittest.main()