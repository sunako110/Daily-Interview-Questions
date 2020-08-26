# 03 - Mar - 2020

# Add two numbers as a linked list

# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        head = None
        prev = None
        temp = None
        while l1 or l2:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            digit = val1 + val2 + c
            c = digit // 10 if digit >= 10 else 0
            digit = digit if digit < 10 else digit % 10
            temp = ListNode(digit)
            if head is None:
                head = temp
            else:
                prev.next = temp
            prev = temp
            l1 = l1.next
            l2 = l2.next
        if c > 0:
            temp.next = ListNode(c)
        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# l1 = ListNode(5)
# l1.next = ListNode(7)
# l1.next.next = ListNode(8)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print result.val
    result = result.next
# 7 0 8