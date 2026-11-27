import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        heap = [-x for x in nums]  # max-heap via negation
        heapq.heapify(heap)
        reduced = 0.0
        ops = 0
        target = total / 2
        while reduced < target:
            x = -heapq.heappop(heap)
            half = x / 2
            reduced += half
            heapq.heappush(heap, -half)
            ops += 1
        return ops
