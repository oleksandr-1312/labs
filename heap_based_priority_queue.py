class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"Node(value='{self.value}', priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0
    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        max_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return max_node

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        max_index = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        n = len(self.heap)

        if left_child < n and self.heap[left_child].priority > self.heap[max_index].priority:
            max_index = left_child

        if right_child < n and self.heap[right_child].priority > self.heap[max_index].priority:
            max_index = right_child

        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self._sift_down(max_index)