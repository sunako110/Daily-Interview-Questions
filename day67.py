# 15 - May - 2020

# Symmetric k-ary Tree

# A k-ary tree is a tree with k-children, and a tree is symmetrical
# if the data of the left side of the tree is the same as the right side of the tree.
#
# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
    # Fill this in.
    if not root:
        return
    if not root.children:
        return True
    return is_mirror(root.children,root.children)

def is_mirror(children1,children2):
    if len(children1) != len(children2):
        return False
    for i in range(len(children1)):
        if children1[i].value != children2[-(i+1)].value:
            return False
        else:
            return is_mirror(children1[i].children, children2[-(i+1)].children)
    return True


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True