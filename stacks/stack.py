
class Stack:
    """An implementation of a stack with a resizing array that is push-expensive"""

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 10
        self.items = [None] * self.capacity

    def push(self, item):
        if self.size == self.capacity:
            self.__resize_array(self.capacity * 2)
        if self.size <= self.capacity // 4:
            self.__resize_array(self.capacity // 2)
        self.items[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError
        
        self.size -= 1
        return self.items[self.size]

    def peek(self):
        return self.items[self.size - 1]


    def __resize_array(self, newCapacity):
        self.capacity = newCapacity
        new_item_array = [None] * self.capacity
        
        for i in range(self.size):
            new_item_array[i] = self.items[i]
        
        self.items = new_item_array