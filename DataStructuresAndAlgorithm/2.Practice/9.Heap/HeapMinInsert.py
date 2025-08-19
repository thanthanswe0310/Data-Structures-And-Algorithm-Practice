class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self,index):
        return 2 * index +1

    def _right_child(self,index):
        return 2 * index +2

    def _parent(self,index):
        return (index-1)//2

    def _swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2],self.heap[index1]


    # WRITE THE INSERT METHOD HERE #
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


myheap = MinHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)


myheap.insert(100)

print(myheap.heap)


myheap.insert(75)

print(myheap.heap)

