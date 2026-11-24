from bisect import bisect_left
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        items = sorted(zip(costs, capacity))
        cs = [c for c, _ in items]

        pm = []
        cur = 0
        for _, cap in items:
            cur = max(cur, cap)
            pm.append(cur)

        ans = 0
        for i, (c, cap) in enumerate(items):
            if c >= budget:
                break                       # sorted: no later machine is affordable
            ans = max(ans, cap)
            idx = bisect_left(cs, budget - c, 0, i)
            if idx > 0:
                ans = max(ans, cap + pm[idx - 1])
        return ans
