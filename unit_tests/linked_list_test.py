import unittest
from data_structures.linked_list import LinkedListNode, LinkedList

class TestStringMethods(unittest.TestCase):

    def test_add_first(self):
        node1 = LinkedListNode("node 1")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)        
        print(my_linked_list)
        self.assertEqual(my_linked_list.head.node_value, 'node 1')

if __name__ == '__main__':
    unittest.main()

