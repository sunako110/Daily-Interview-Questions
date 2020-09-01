# 22 - Apr - 2020

# Largest BST in a Binary Tree

# You are given the root of a binary tree.
# Find and return the largest subtree of that tree, which is a valid binary search tree.

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def largest_bst_subtree(root):
    # Fill this in.
    if bst_subtree_size(root) > 0:
        return root
    else:
        if bst_subtree_size(root.right) > bst_subtree_size(root.left):
            return root.right
        elif bst_subtree_size(root.right) < bst_subtree_size(root.left):
            return root.left
        else:
            if bst_subtree_size(largest_bst_subtree(root.right)) > bst_subtree_size(largest_bst_subtree(root.left)):
                return largest_bst_subtree(root.left)
            else:
                return largest_bst_subtree(root.left)


def bst_subtree_size (root):
    if not root.left and not root.right:
        return 1
    if root.left and not root.right:
        if root.left.key > root.key:
            return 0
        else:
            return 1 + bst_subtree_size(root.left)
    elif root.right and not root.left:
        if root.right.key < root.key:
            return 0
        else:
            return 1 + bst_subtree_size(root.right)
    else:
        if root.left.key > root.key or root.right.key < root.key:
            return 0
        else:
            return 1 + bst_subtree_size(root.left) + bst_subtree_size(root.right)


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
#749