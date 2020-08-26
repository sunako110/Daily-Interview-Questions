# 14 - Mar - 2020

# Invert a Binary Tree

# You are given the root of a binary tree. Invert the binary tree in place.
# That is, all left children should become right children, and all right children should become left children.

# Example:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
#
# The inverted version of this tree is as follows:
#
#   a
#  / \
#  c  b
#  \  / \
#   f e  d

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print self.value,
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
    # Fill this in.
    if node.left and node.right:
        node.left, node.right = node.right, node.left
        invert(node.left)
        invert(node.right)
    if node.left and node.right is None:
        node.right = node.left
        node.left = None
        invert(node.right)
    if node.left is None and node.right:
        node.left = node.right
        node.right = None
        invert(node.left)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print "\n"
invert(root)
root.preorder()
# a c f b e d