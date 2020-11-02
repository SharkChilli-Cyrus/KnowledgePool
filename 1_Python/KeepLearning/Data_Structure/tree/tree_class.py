import sys
import os

class BinaryTree:
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp
    
    def get_root_value(self):
        return self.key
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def set_root_value(self, new_object):
        self.key = new_object


if __name__ == "__main__":

    # TEST
    test_tree = BinaryTree("A")
    print("\n---")
    print(test_tree.get_root_value())
    print(test_tree.get_left_child())

    test_tree.insert_left("b")
    print("\n---")
    print(test_tree.get_left_child())
    print(test_tree.get_left_child()\
                   .get_root_value()
    )

    test_tree.insert_right("c")
    print("\n---")
    print(test_tree.get_right_child())
    print(test_tree.get_right_child()\
                   .get_root_value()
    )

    test_tree.get_right_child()\
             .set_root_value("new_node")
    print("\n---")
    print(test_tree.get_right_child()\
                   .get_root_value()
    )