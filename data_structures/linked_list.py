class LinkedListNode:
    def __init__(self, value = None, next = None):
        self.node_value = value
        self.next = next

    def __eq__(self, other_node):
        if isinstance(other_node, LinkedListNode):
            return self.node_value == other_node.node_value
        return NotImplemented
    
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.iteration_counter = 0

    def __str__(self):
        str_list = []
        str_to_return = ''
        counter = 1
        node_to_iterate = self.head
        while node_to_iterate != None:
            str_list.append('{count}:"{node_value}"\n'.format(count=counter, node_value = node_to_iterate.node_value))
            node_to_iterate = node_to_iterate.next
            counter += 1
        return str_to_return.join(str_list)

    def __iter__(self):
        return self
    
    #O(n^2) as a performance optimization we can make the data as array which will access index by O(1) and iteration will become O(n) instead
    def __next__(self):
        if self.iteration_counter >= self.length:
            self.iteration_counter = 0
            raise StopIteration
        else:
            node_to_return = self.get_node_by_index(self.iteration_counter)
            self.iteration_counter += 1
            return node_to_return
    #O(1)
    def add_first(self, node_to_add):
        if self.length == 0:            
            self.head = node_to_add
            self.tail = node_to_add
        else:
            node_to_add.next = self.head
            self.head = node_to_add  
        self.length += 1

    #O(1)
    def add_last(self, node_to_add):
        if self.length == 0:            
            self.head = node_to_add
            self.tail = node_to_add
        else:
            self.tail.next = node_to_add
            self.tail = node_to_add
        self.length += 1

    #O(n)
    def get_node_by_index(self, index):
        node_to_return = self.head
        
        if index >= self.length:
            raise IndexError("Index was out of range for the current linked list")
        
        counter = 0
        while counter != index:
            node_to_return = node_to_return.next
            counter += 1
        
        return node_to_return

    #O(n)
    def add_node_before(self, existing_node, node_to_add):
        current_node = self.head
        while current_node != None:
            if existing_node == self.head:
                self.add_first(node_to_add) #to change head reference
                break
            elif current_node.next == existing_node:
                node_to_add.next = current_node.next
                current_node.next = node_to_add
                self.length += 1
                break     
            current_node = current_node.next

        if current_node == None:
            raise ValueError("No valid existing node matches the node passed, can't insert new node before non existant one")

    #O(n)
    def add_node_after(self, existing_node, node_to_add):
        current_node = self.head
        while current_node != None:
            if current_node == existing_node:
                if current_node == self.tail:
                    self.add_last(node_to_add)#to also change the tail reference
                else:
                    node_to_add.next = existing_node.next
                    existing_node.next = node_to_add
                    self.length += 1
                break
            current_node = current_node.next
        if current_node == None:
            raise ValueError("No valid existing node matches the node passed, can't insert new node after non existant one")

    #O(n)
    def find_node_by_value(self, node_value):
        current_node = self.head
        while current_node != None:
            if current_node.node_value == node_value:
                break
            current_node = current_node.next
        return current_node

    #O(n)   
    def delete_node(self, node_to_delete):
        current_node = self.head

        if self.length == 1 and node_to_delete == current_node:
            self.head = None
            self.tail = None
            self.length = 0
        elif node_to_delete == self.head:
            self.head = self.head.next
            current_node.next = None
            self.length -= 1
        else:
            while current_node != None:
                if current_node.next == node_to_delete:
                    if current_node.next == self.tail:
                        current_node.next = None
                        self.tail = current_node
                    else:                        
                        current_node.next = current_node.next.next
                        node_to_delete.next = None
                    self.length -= 1
                    break
                else:
                    current_node = current_node.next

            if current_node == None:
                raise ValueError("No valid node matches the one passed, can't delete non existant node")   
