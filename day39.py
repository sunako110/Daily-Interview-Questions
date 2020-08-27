# 15 - Apr - 2020

# Get all Values at a Certain Height in a Binary Tree

# Given a binary tree, return all values given a certain height h.

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # Fill this in.
    result = []
    for list in recursive(root, height):
        result += list
    return result

def recursive(node, height):
    if not node:
        return
    if height == 1:
        return node.value
    else:
        if node.left and node.right:
            return [recursive(node.left, height - 1)] + [recursive(node.right, height - 1)]
        elif node.right:
            return [] + [recursive(node.right, height - 1)]
        elif node.left:
            return recursive(node.left, height - 1)

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]