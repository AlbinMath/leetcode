import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_val = float('inf')
        for x in nums:
            if x % 2 == 1:
                x *= 2
            heap.append(-x)  # max-heap via negation
            min_val = min(min_val, x)
        heapq.heapify(heap)

        ans = float('inf')
        while True:
            m = -heapq.heappop(heap)
            ans = min(ans, m - min_val)
            if m % 2 == 1:
                break
            half = m // 2
            min_val = min(min_val, half)
            heapq.heappush(heap, -half)
        return ans
