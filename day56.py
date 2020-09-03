# 04 - May - 2020

# Arithmetic Binary Tree

# You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
#
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    # Fill this in.
    if not root.right and not root.left:
        return int(root.val)
    else:
        if root.val == PLUS:
            return evaluate(root.right) + evaluate(root.left)
        elif root.val == MINUS:
            return evaluate(root.right) - evaluate(root.left)
        elif root.val == TIMES:
            return evaluate(root.right) * evaluate(root.left)
        elif root.val == DIVIDE:
            if evaluate(root.left) == 0:
                print("error: cannot divide by 0")
                exit()
            else:
                return evaluate(root.right) / evaluate(root.left)
        else:
            print("error: unknown operator")
            exit()

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45