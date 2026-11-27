import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []  # min-heap of speeds
        s_sum = 0
        best = 0
        for e, s in engineers:
            heapq.heappush(heap, s)
            s_sum += s
            if len(heap) > k:
                s_sum -= heapq.heappop(heap)
            best = max(best, s_sum * e)
        return best % MOD
