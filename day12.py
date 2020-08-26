# 15 - Mar - 2020

# Maximum In A Stack

# Implement a class for a stack that supports all the regular functions (push, pop) and
# an additional function of max() which returns the maximum element in the stack (return None if the stack is empty).
# Each method should run in constant time.


class MaxStack:
    def __init__(self):
        # Fill this in.
        self.list = []

    def push(self, val):
        # Fill this in.
        self.list.append(val)

    def pop(self):
        # Fill this in.
        self.list.pop()

    def max(self):
        # Fill this in.
        if len(self.list) == 0:
            return None
        else:
            return max(self.list)


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
