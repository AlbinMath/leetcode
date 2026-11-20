import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        # Maps index -> current number stored at that index
        self.index_to_num = {}
        # Maps number -> min-heap of candidate indices
        self.num_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_indices:
            return -1
            
        heap = self.num_to_indices[number]
        # Lazily discard stale indices whose current value is no longer `number`
        while heap and self.index_to_num.get(heap[0]) != number:
            heapq.heappop(heap)
            
        return heap[0] if heap else -1
