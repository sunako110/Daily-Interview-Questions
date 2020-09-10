# 24 - May - 2020

# Maximum Path Sum in Binary Tree

# You are given the root of a binary tree.
# Find the path between 2 nodes that maximizes the sum of all the nodes in the path, and return the sum.
# The path does not necessarily need to go through the root.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def maxPathSum(root):
    # Fill this in.
    res = 0
    partial_sum, res = maxPathSumUtil(root,res)
    return res

def maxPathSumUtil(root, res):
    if not root:
        return 0, 0

    partial_left, res = maxPathSumUtil(root.left, res)
    partial_right, res = maxPathSumUtil(root.right, res)

    partial_sum = max(root.val, root.val + partial_left, root.val + partial_right)
    sum = root.val + partial_left + partial_right

    res = max(sum, partial_sum)
    return partial_sum, res

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42
