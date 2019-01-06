import unittest
from data_structures.linked_list import LinkedListNode, LinkedList

class TestLinkedListMethods(unittest.TestCase):

    def test_add_first_to_empty_list(self):
        node1 = LinkedListNode("node 1")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)        
        print(my_linked_list)
        self.assertEqual(my_linked_list.head.node_value, 'node 1')
        self.assertEqual(my_linked_list.head.next, None)
        self.assertEqual(my_linked_list.tail.node_value, 'node 1')
        self.assertEqual(my_linked_list.tail.next, None)
        self.assertEqual(my_linked_list.length, 1)

    def test_add_first_to_non_Empty_list(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1) 
        my_linked_list.add_first(node2)
        print(my_linked_list)
        self.assertEqual(my_linked_list.head.node_value, 'node 2')
        self.assertEqual(my_linked_list.head.next.node_value, 'node 1')
        self.assertEqual(my_linked_list.head.next.next, None)
        self.assertEqual(my_linked_list.tail.node_value, 'node 1')
        self.assertEqual(my_linked_list.tail.next, None)
        self.assertEqual(my_linked_list.length, 2)
    
    def test_get_node_by_index(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1) 
        my_linked_list.add_last(node2)
        print(my_linked_list)
        with self.assertRaises(IndexError):
            my_linked_list.get_node_by_index(2)
        self.assertEqual(my_linked_list.get_node_by_index(0).node_value, 'node 1')
        self.assertEqual(my_linked_list.get_node_by_index(1).node_value, 'node 2')

    def test_add_node_before(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        node3 = LinkedListNode("node 3")
        node4 = LinkedListNode("node 4")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node3)
        my_linked_list.add_node_before(node3, node1)
        self.assertEqual(my_linked_list.head.node_value, 'node 1')
        self.assertEqual(my_linked_list.get_node_by_index(1).node_value, 'node 3')
        self.assertEqual(my_linked_list.length, 2)
        with self.assertRaises(ValueError):
            my_linked_list.add_node_before(node2, node4)
        my_linked_list.add_node_before(node3, node2)
        self.assertEqual(my_linked_list.get_node_by_index(1).node_value, 'node 2')
        self.assertEqual(my_linked_list.get_node_by_index(2).node_value, 'node 3')
        self.assertEqual(my_linked_list.tail.node_value, 'node 3')
        self.assertEqual(my_linked_list.length, 3)
        print(my_linked_list)

    def test_add_node_after(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        node3 = LinkedListNode("node 3")
        node4 = LinkedListNode("node 4")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)
        my_linked_list.add_node_after(node1, node2)
        self.assertEqual(my_linked_list.head.node_value, 'node 1')
        self.assertEqual(my_linked_list.get_node_by_index(1).node_value, 'node 2')
        self.assertEqual(my_linked_list.length, 2)
        with self.assertRaises(ValueError):
            my_linked_list.add_node_after(node3, node4)
        my_linked_list.add_node_after(node2, node3)
        self.assertEqual(my_linked_list.get_node_by_index(1).node_value, 'node 2')
        self.assertEqual(my_linked_list.get_node_by_index(2).node_value, 'node 3')
        self.assertEqual(my_linked_list.tail.node_value, 'node 3')
        self.assertEqual(my_linked_list.length, 3)
        print(my_linked_list)

    def test_find_node_by_value(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        node3 = LinkedListNode("node 3")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)
        my_linked_list.add_node_after(node1, node2)
        my_linked_list.add_last(node3)
        
        node_to_find = my_linked_list.find_node_by_value("node 1")
        self.assertEqual(node_to_find, node1)
        node_to_find = my_linked_list.find_node_by_value("node 2")
        self.assertEqual(node_to_find, node2)
        node_to_find = my_linked_list.find_node_by_value("node 3")
        self.assertEqual(node_to_find, node3)
    
    def test_delete_nodes(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        node3 = LinkedListNode("node 3")
        node4 = LinkedListNode("node 4")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)
        my_linked_list.add_last(node2)
        my_linked_list.add_last(node3)
        my_linked_list.add_last(node4)

        my_linked_list.delete_node(node1)
        self.assertEqual(my_linked_list.length, 3)
        self.assertEqual(my_linked_list.head, node2)
        my_linked_list.delete_node(node3)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.get_node_by_index(1), node4)
        my_linked_list.delete_node(node4)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head, node2)
        self.assertEqual(my_linked_list.tail, node2)
        with self.assertRaises(ValueError):
            my_linked_list.delete_node(node4)
        my_linked_list.delete_node(node2)
        self.assertEqual(my_linked_list.length, 0)
        self.assertEqual(my_linked_list.head, None)
        self.assertEqual(my_linked_list.tail, None)

    def test_iteration_of_nodes(self):
        node1 = LinkedListNode("node 1")
        node2 = LinkedListNode("node 2")
        node3 = LinkedListNode("node 3")
        my_linked_list = LinkedList()
        my_linked_list.add_first(node1)
        my_linked_list.add_last(node2)
        my_linked_list.add_last(node3)
        counter = 0
        for node in my_linked_list:
            self.assertEqual(node, my_linked_list.get_node_by_index(counter))
            counter += 1

if __name__ == '__main__':
    unittest.main()