from data_structures.linked_list import LinkedListNode, LinkedList

class HashTableEntry:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value

class HashTable:
    #To Do: iterating can be implemented

    def __init__(self):
        self.increased_capacity_value = 100
        self.data_max_size = 100
        self.data_array = [None] * self.data_max_size
        self.current_items_count = 0

    def _compute_hash_code(self, stringKey):
        return stringKey.__hash__()

    def _compute_index_from_hash(self, hash_value):
        return hash_value % self.data_max_size

    def _assure_max_size_Not_exceeded(self):
        if(self.current_items_count >=  self.data_max_size):
            extended_array = [None] * self.increased_capacity_value
            self.data_max_size += self.increased_capacity_value
            self.data_array.extend(extended_array)

    #O(1) best and should be for most cases, and worst if collision happened O(n) where n is the # of elements at same index
    def get_value_by_key(self, key):
        value_to_return = None
        hash_for_item_to_add = self._compute_hash_code(key)
        index_for_item_to_add = self._compute_index_from_hash(hash_for_item_to_add)

        if self.data_array[index_for_item_to_add] == None:
            raise KeyError("Key not found")
        else:
            linked_list = self.data_array[index_for_item_to_add]
            if linked_list.length == 1 and linked_list.head.node_value.key == key:
                return linked_list.head.node_value.value
            else:#collision occurred
                node = linked_list.head
                while node != None:
                    if(node.node_value.key == key):
                        value_to_return = node.node_value.value
                        break
                    node = node.next
                if node == None:
                    raise KeyError("Key not found")

        return value_to_return

    #O(1) best and should be for most cases, and worst if collision happened O(n) where n is the # of elements at same index
    #if same key is added its value will be updated
    def add_entry(self, key, value):
        hash_for_item_to_add = self._compute_hash_code(key)
        index_for_item_to_add = self._compute_index_from_hash(hash_for_item_to_add)
        hash_table_entry = HashTableEntry(key, value)
        node_to_add = LinkedListNode(hash_table_entry)

        if self.data_array[index_for_item_to_add] == None:     
            linked_list = LinkedList()
            linked_list.add_first(node_to_add)
            self.data_array[index_for_item_to_add] = linked_list
            self.current_items_count += 1
        else:#check if same key exist and update it
            linked_list = self.data_array[index_for_item_to_add]
            node = linked_list.head
            while node != None:
                if(node.node_value.key == key):
                    node.node_value.value = value
                    break
                node = node.next
            if node == None:#if key not exist then it is a new element just add it to linked list at that index
                linked_list.add_last(node_to_add)
                self.current_items_count += 1
        

        self._assure_max_size_Not_exceeded()

    #O(1) best and should be for most cases, and worst if collision happened O(n) where n is the # of elements at same index
    def delete_entry_by_key(self, key):
        hash_for_item_to_add = self._compute_hash_code(key)
        index_for_item_to_add = self._compute_index_from_hash(hash_for_item_to_add)
        
        if self.data_array[index_for_item_to_add] == None:
            raise KeyError("Key not found")
        else:
            linked_list = self.data_array[index_for_item_to_add]
            if linked_list.length == 1 and linked_list.head.node_value.key == key:
                linked_list.delete_node(linked_list.head)
                self.current_items_count -= 1
            else:#collision had occurred
                node = linked_list.head
                while node != None:
                    if(node.node_value.key == key):
                        linked_list.delete_node(node)
                        self.current_items_count -= 1
                        break
                    node = node.next
                if node == None:
                    raise KeyError("Key not found")