class CircularArray:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = 0


    def insert(self, item):
        if self.size == self.capacity:
            self.__resize()
        assert self.array[self.head] == None

        self.array[self.head] = item
        self.size += 1
        
        self.__move_head()

    def append(self, item):
        if self.size == self.capacity:
            self.__resize()
        assert self.array[self.tail] == None

        self.array[self.tail] = item
        self.size += 1

        self.__move_tail()

    def peek_head(self):
        return self.array[self.head + 1] if self.head < self.capacity - 1 else self.array[0]

    def peek_tail(self):
        return self.array[self.tail - 1] if self.tail > 0 else self.array[self.capacity - 1]

    def list_items(self):
        """Returns an array with items in the order from head to tail"""

        tmp_head = self.head + 1
        if tmp_head >= self.capacity:
            tmp_head = 0

        res_arr = []
        while tmp_head != self.head:
            if self.array[tmp_head] != None:
                res_arr.append(self.array[tmp_head])

            tmp_head += 1
            if tmp_head >= self.capacity:
                tmp_head = 0


        if self.array[tmp_head] != None:
            res_arr.append(self.array[tmp_head])

        return res_arr


    def __move_head(self):
        self.head -= 1
        if self.head + 1 == self.tail:
            self.__move_tail()
        
        if self.head == -1:
            self.head = self.capacity - 1

    def __move_tail(self):
        self.tail += 1
        if self.tail - 1 == self.head:
            self.__move_head()

        if self.tail == self.capacity:
            self.tail = 0

    def __resize(self):
        new_array = [None] * (self.capacity * 2)
        existing_items = self.list_items()

        for i in range(len(existing_items)):
            new_array[i] = existing_items[i]

        self.array = new_array
        self.capacity *= 2
        self.head = self.capacity - 1
        self.tail = len(existing_items) + 1


