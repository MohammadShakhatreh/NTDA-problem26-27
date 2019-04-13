class MinHeap:

    def __init__(self):
        self.size = 0
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.up_heap()

    def peek(self):
        '''get min element'''
        if self.size == 0:
            raise Exception('Heap is empty!')
        return self.heap[0]

    def poll(self):
        '''get min element and remove it'''
        if self.size == 0:
            raise Exception('Heap is empty!')

        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]

        self.heap.pop()
        self.size -= 1
        self.down_heap()
        return root

    def up_heap(self):
        '''move last element up to it's normal pos'''
        index = self.size - 1
        while self.has_parent(index) and self.heap[index] < self.parent(index):
            self.heap[index], self.heap[self.parent_index(index)] = \
                self.heap[self.parent_index(index)], self.heap[index]
            index = self.parent_index(index)

    def down_heap(self):
        '''move the root element down to it's normal pos'''
        index = 0
        while self.has_left(index):
            min_index = self.left_index(index)
            if self.has_right(index) and self.right(index) < self.left(index):
                min_index = self.right_index(index)

            if self.heap[index] < self.heap[min_index]:
                break
            else:
                self.heap[index], self.heap[min_index] = \
                    self.heap[min_index], self.heap[index]

            index = min_index

    def empty(self):
        return self.size == 0

    #helper methods
    def parent(self, index):
        return self.heap[self.parent_index(index)]

    def parent_index(self, index):
        return (index - 1) >> 1

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def left(self, index):
        return self.heap[self.left_index(index)]

    def right(self, index):
        return self.heap[self.right_index(index)]

    def has_left(self, index):
        return self.left_index(index) < self.size

    def has_right(self, index):
        return self.right_index(index) < self.size

    def left_index(self, index):
        return (index << 1) + 1

    def right_index(self, index):
        return (index << 1) + 2
