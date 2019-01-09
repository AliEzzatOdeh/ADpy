import unittest
from data_structures.hash_table import HashTable

class TestHashTableMethods(unittest.TestCase):

    def test_add_first_to_empty_table(self):
        my_hash_table = HashTable()
        my_hash_table.add_entry("key1","value1")
        self.assertEqual(my_hash_table.current_items_count, 1)
        self.assertEqual(my_hash_table.get_value_by_key("key1"), "value1")

    def test_add_multiple_elements(self):
        my_hash_table = HashTable()
        my_hash_table.add_entry("key1","value1")
        my_hash_table.add_entry("key2","value2")
        my_hash_table.add_entry("key3","value3")

        self.assertEqual(my_hash_table.current_items_count, 3)
        self.assertEqual(my_hash_table.get_value_by_key("key1"), "value1")
        self.assertEqual(my_hash_table.get_value_by_key("key2"), "value2")
        self.assertEqual(my_hash_table.get_value_by_key("key3"), "value3")
    
    def test_get_key_not_exist(self):
        my_hash_table = HashTable()
        with self.assertRaises(KeyError):
            my_hash_table.get_value_by_key("key1")
        my_hash_table.add_entry("key1","value1")
        with self.assertRaises(KeyError):
            my_hash_table.get_value_by_key("key2")
    
    def test_delete_entry(self):
        my_hash_table = HashTable()
        my_hash_table.add_entry("key1","value1")
        my_hash_table.add_entry("key2","value2")
        my_hash_table.add_entry("key3","value3")
        my_hash_table.delete_entry_by_key("key2")
        self.assertEqual(my_hash_table.current_items_count, 2)
        with self.assertRaises(KeyError):
            my_hash_table.get_value_by_key("key2")
    
    def test_update_existing_element(self):
        my_hash_table = HashTable()
        my_hash_table.add_entry("key1","value1")
        my_hash_table.add_entry("key2","value2")
        
        my_hash_table.add_entry("key2","newValue2")

        self.assertEqual(my_hash_table.current_items_count, 2)
        self.assertEqual(my_hash_table.get_value_by_key("key2"), "newValue2")