# 27 - Mar - 2020

# Remove k-th Last Element From Linked List

# You are given a singly linked list and an integer k.
# Return the linked list, removing the k-th last element from the list.
#
# Try to do it in a single pass and using constant space.

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
  # Fill this in
    node = Node(0)
    node.next = head
    length = 0
    while head:
        length += 1
        head = head.next
    if not (0 < k <= length):
        return node.next
    length -= k
    head = node
    while length > 0:
        length -= 1
        head = head.next
    head.next = head.next.next
    return node.next



head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]