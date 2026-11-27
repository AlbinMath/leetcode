import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(zip(quality, wage), key=lambda w: w[1] / w[0])
        heap = []  # max-heap via negated qualities
        q_sum = 0
        ans = float('inf')
        for q, w in workers:
            ratio = w / q
            heapq.heappush(heap, -q)
            q_sum += q
            if len(heap) > k:
                q_sum += heapq.heappop(heap)  # popped value is negative
            if len(heap) == k:
                ans = min(ans, ratio * q_sum)
        return ans
