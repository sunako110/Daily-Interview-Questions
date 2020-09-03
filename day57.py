# 05 - May - 2020

# Tree Serialization

# You are given the root of a binary tree. You need to implement 2 functions:
#
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
#
# For this problem, often you will be asked to design your own serialization format.
# However, for simplicity, let's use the pre-order traversal of the tree.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

def serialize(root):
  # Fill this in.
  result = str(root.val) + " "
  if root.left:
      result += serialize(root.left)
  else:
      result += "# "
  if root.right:
      result += serialize(root.right)
  else:
      result += "# "
  return result


def deserialize(data):
    # Fill this in.
    pos = -1
    nodes = data.split()
    if nodes[0] == "#":
        return
    root, count = pre_order_deserialize(nodes, pos)
    return root

def pre_order_deserialize(nodes, pos):
    pos +=1
    if pos >= len(nodes) or nodes[pos] == "#":
        return None, pos

    root = Node(nodes[pos])
    root.left, pos = pre_order_deserialize(nodes,pos)
    root.right, pos = pre_order_deserialize(nodes,pos)
    return root, pos


#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547