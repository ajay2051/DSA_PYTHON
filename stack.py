# A stack in Python is a linear data structure that follows the Last In First Out (LIFO) principle.
# Stack can be used to maintain history by browser.
# Undo (Ctrl + Z) functionality in any editor uses stack to track down last set of operations.

from collections import deque

stack = deque()


class Stack:
    def __init__(self):
        self.container = stack

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
