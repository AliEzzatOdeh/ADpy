class LinkedListNode:
    def __init__(self, value = None, next = None):
        self.node_value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_first(self,value):
        nodeToAdd = LinkedListNode(value)
        if self.length == 0:            
            self.head = nodeToAdd
        else:
            nodeToAdd.next = self.head
            self.head = nodeToAdd  
            

    def __str__(self):
        str_to_return = ''
        counter = 1
        node_to_iterate = self.head
        while node_to_iterate != None:
            str_to_return.join("{count}:{node_value}\n".format(count=counter, node_value = node_to_iterate.node_value))
            node_to_iterate = node_to_iterate.next
        return str_to_return
            

    
