import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]  # max-heap via negation
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            x = -heap[0]
            score += x
            heapq.heapreplace(heap, -((x + 2) // 3))
        return score
