from circular_array import circular_array

class Queue:

    def __init__(self):
        self.capacity = 10
        self.items = [None] * self.capacity
        self.size = 0

    def enqueue(self, item):
        self.items[0] = item
        self.size += 1

    def dequeue(self, item):
        self.size - 