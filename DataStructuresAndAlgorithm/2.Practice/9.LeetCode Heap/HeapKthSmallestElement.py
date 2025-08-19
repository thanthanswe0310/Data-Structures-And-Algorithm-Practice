# Heap: Kth Smallest Element in an Array
# You are given a list of numbers called nums and a number k.
# Your task is to write a function find_kth_smallest(nums, k) to find the kth smallest number in the list.
# The list can contain duplicate numbers and k is guaranteed to be within the range of the length of the list.
# This function will take the following parameters:
# nums: A list of integers.#
# k: An integer.
# This function should return the kth smallest number in nums.
# Example 1:
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(find_kth_smallest(nums, k))
# In the example above, the function should return 2. If we sort the list, it becomes [1, 2, 3, 4, 5, 6]. The 2nd smallest number is 2, so the function returns 2.
#
# There are two common approaches:
#
# Min-Heap: Push all elements into a min-heap, then pop k times → O(n + k log n).
#
# Max-Heap (size k): Keep a max-heap of size k. Traverse the array, and if the heap grows beyond k, remove the largest. Finally, the root of the heap is the kth smallest → O(n log k).
#
# Here’s the Python solution using Max-Heap (size k) (efficient when k is small compared to n):
# Time Complexity: O(n log k)
# Space Complexity: O(k)



class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


#### WRITE FIND_KTH_SMALLEST FUNCTION HERE ####
def find_kth_smallest(nums, k):
    heap = MaxHeap()

    for num in nums:
        heap.insert(num)
        if len(heap.heap) > k:  # keep only k elements
            heap.remove()

    return heap.heap[0]  # kth smallest


# Test cases
nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i + 1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')
