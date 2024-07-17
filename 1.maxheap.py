class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            raise IndexError("Oops! The heap is empty. Nothing to delete.")

        max_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)

        return max_value

    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("Oops! The heap is empty. No maximum element available.")

        return self.heap[0]

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index != index:
                self.heap[largest_index], self.heap[index] = self.heap[index], self.heap[largest_index]
                index = largest_index
            else:
                break
            
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(10)
max_heap.insert(3)
max_heap.insert(8)

print("Maximum element in the heap:", max_heap.get_max())  

max_heap.delete()
print("After deleting the maximum element, new maximum element:", max_heap.get_max())

