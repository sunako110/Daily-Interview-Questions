# 09 - May - 2020

# Min Stack

# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Note: be sure that pop() and top() handle being called on an empty stack.

class minStack(object):
    def __init__(self):
        # Fill this in.
        self.stack = []

    def push(self, x):
        # Fill this in.
        self.stack.append(x)

    def pop(self):
        # Fill this in.
        self.stack.pop()

    def top(self):
        # Fill this in.
        return self.stack[-1]

    def getMin(self):
        # Fill this in.
        return min(self.stack)

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2