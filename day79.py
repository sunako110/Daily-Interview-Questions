# 28 - May - 2020

# Determine If Linked List is Palindrome

# You are given a doubly linked list. Determine if it is a palindrome.

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    # Fill this in.

    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast and not fast.next:
        fast = slow
    else:
        fast = slow.prev

    while fast and slow:
        if fast.val != slow.val:
            return False
        fast = fast.prev
        slow = slow.next

    return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True