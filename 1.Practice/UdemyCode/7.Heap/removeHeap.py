def remove(self):
    if len(self.heap) ==0:
        return None
    if len(self.heap) ==1:
        return self.heap.pop()
    max_value = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)
    return max_value

def _sink_down(self,index):
    max_index = index
    while True:
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        if self.heap[left_index] > self.heap[max_index]:
            max_index = left_index

        if self.heap[right_index] > self.heap[max_index]:
            max_index =right_index

        if max_index != index:
            self._swap(index, max_index)
            index = max_index
        else:
            return


