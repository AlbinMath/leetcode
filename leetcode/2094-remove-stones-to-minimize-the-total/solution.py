import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]  # max-heap via negation
        heapq.heapify(heap)
        for _ in range(k):
            p = -heap[0]
            heapq.heapreplace(heap, -(p - p // 2))
        return -sum(heap)
