# 05 - Apr - 2020

# Queue Using Two Stacks

# Implement a queue class using two stacks.
# A queue is a data structure that supports the FIFO protocol (First in = first out).
# Your class should support the enqueue and dequeue methods like a standard queue.

class Queue:
    def __init__(self):
    # Fill this in.
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
    # Fill this in.
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(val)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
    # Fill this in.
        if len(self.s1) == 0:
            return None
        x = self.s1[-1]
        self.s1.pop()
        return x

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
