# 24 - Mar - 2020

# Intersection of Linked Lists

# You are given two singly linked lists. The lists intersect at some node.
# Find, and return the node. Note: the lists are non-cyclical.

# Example:
#
# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4
#
# This should return 3 (you may assume that any nodes with the same value are the same node).

def intersection(a, b):
  # fill this in.
  #   b_next = b
  #   while a:
  #       while b_next:
  #           if a.val == b_next.val:
  #               return Node(a.val)
  #           b_next = b_next.next
  #       b_next = b
  #       a = a.next
  #   return None
    if a == None or b == None:
        return None

    pa = a
    pb = b

    while pa != pb:
        pa = b if pa == None else pa.next
        pb = a if pb == None else pb.next

    return pa


class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print c.val,
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4