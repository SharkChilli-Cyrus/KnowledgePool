import sys
import os
import operator

# (3*(4+5))

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, root_value=""):
        self.key = root_value
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
            temp.left_child = self.left_child
            self.left_child = temp
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def set_root_value(self, new_value):
        self.key = new_value
    
    def get_root_value(self):
        return self.key

# ============================================================

def build_parse_tree(expression):
    if " " in expression:
        token_list = expression.split(" ")
    else:
        token_list = list(expression)

    tree_stack = Stack()
    tree = BinaryTree()

    tree_stack.push(tree)
    current_tree = tree # change current_tree will also change tree

    for token in token_list:
        if token == "(":
            current_tree.insert_left("")
            tree_stack.push(current_tree) # parent node
            current_tree = current_tree.get_left_child() # left child

        elif token not in ["+", "-", "*", "/", ")"]:
            current_tree.set_root_value(int(token))
            parent = tree_stack.pop() # parent.child has been set as int(token)
            current_tree = parent

        elif token in ["+", "-", "*", "/"]:
            current_tree.set_root_value(token)
            current_tree.insert_right("")
            tree_stack.push(current_tree) # parent node
            current_tree = current_tree.get_right_child() # right child

        elif token == ")":
            current_tree = tree_stack.pop()

        else:
            raise ValueError
    
    return tree


def evaluate_tree(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        function = operators[parse_tree.get_root_value()]
        return function(evaluate_tree(left_child), evaluate_tree(right_child))
    else:
        return parse_tree.get_root_value()


if __name__ == "__main__":
