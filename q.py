# A queue in Python is a linear data structure that follows the First In First Out (FIFO) principle.
# This means that the first element added to the queue will be the first element removed.

from collections import deque

wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0, 100)
wmt_stock_price_queue.insert(0, 110)
wmt_stock_price_queue.insert(0, 120)
wmt_stock_price_queue.pop()
print(wmt_stock_price_queue)

q = deque()
q.appendleft(5)
q.appendleft(10)
q.appendleft(15)
print(q)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()
pq.enqueue({
    "company": "Wallmart 1",
    "timestamp": "15 APR, 11.01 AM",
    "price": 120
})
pq.enqueue({
    "company": "Wallmart 2",
    "timestamp": "15 APR, 11.01 AM",
    "price": 120
})
pq.enqueue({
    "company": "Wallmart 3",
    "timestamp": "15 APR, 11.01 AM",
    "price": 120
})
print(pq.size())
print(pq.dequeue())
