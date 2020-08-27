# 07 - Apr - 2020

# Merge K Sorted Linked Lists

# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    for i in range(1,len(lists)):
        while True:
            a = lists[0]
            b = lists[i]
            if not b:
                break
            if a.val >= b.val:
                lists[i] = b.next
                b.next = a
                lists[0] = b
            else:
                while a.next:
                    if a.next.val >=b.val:
                        lists[i] = b.next
                        b.next = a.next
                        a.next = b
                        break

                    a = a.next

                    if not a.next:
                        lists[i] = b.next
                        b.next = None
                        a.next = b
                        a.next.next = None
                        break
    return lists[0]


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456