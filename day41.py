#  17 - Apr - 2020

# Count Number of Unival Subtrees

# A unival tree is a tree where all the nodes have the same value.
# Given a binary tree, return the number of unival subtrees in the tree.
#
# For example, the following tree should return 5:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
  # Fill this in.
    count = 0
    if not root:
        return 0
    if is_unival_subtrees(root):
        count += 1
    count += count_unival_subtrees(root.right)
    count += count_unival_subtrees(root.left)
    return count

def is_unival_subtrees(root):
    if not root.right and not root.left:
        return True
    elif root.right and not root.left:
        return True if root.val == root.right.val else False
    elif root.left and not root.right:
        return True if root.val == root.left.val else False
    else:
        if root.val != root.right.val or root.val != root.left.val:
            return False
        else:
            return is_unival_subtrees(root.right) and is_unival_subtrees(root.left)





a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5