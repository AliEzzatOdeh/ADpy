class BinaryTreeNode:
    
    def __init__(self, value = None, left_node = None, right_node = None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

class BinaryTree:

    def __init__(self, root = None):
        self.root = root
        self.node_count = 1 if root else 0

    def __preorder(self, node, visit_method):
        if(node != None):
            visit_method(node)
            self.__preorder(node.left_node, visit_method)
            self.__preorder(node.right_node, visit_method)

    def __inorder(self, node, visit_method):
        if(node != None):
            self.__preorder(node.left_node, visit_method)
            visit_method(node)
            self.__preorder(node.right_node, visit_method)
    
    def __postorder(self, node, visit_method):
        if(node != None):
            self.__preorder(node.left_node, visit_method)
            self.__preorder(node.right_node, visit_method)
            visit_method(node)
            
    def set_root(self, root, nodes_count = 1):
        self.root = root
        self.node_count = nodes_count

    def get_root(self):
        return self.root

    def add_left_node(self, node):
        self.root.left_node = node
        self.node_count += 1
    
    def add_right_node(self, node):
        self.root.right_node = node
        self.node_count += 1
    
    def preorder_traverse(self, visit_method):
        self.__preorder(self.root, visit_method)
    
    def inorder_traverse(self, visit_method):
        self.__inorder(self.root, visit_method)
    
    def postorder_traverse(self, visit_method):
        self.__postorder(self.root, visit_method)
