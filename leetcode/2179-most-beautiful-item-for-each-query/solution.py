from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = [p for p, _ in items]

        best = []
        cur = 0
        for _, b in items:
            cur = max(cur, b)
            best.append(cur)

        ans = []
        for q in queries:
            idx = bisect_right(prices, q) - 1
            ans.append(best[idx] if idx >= 0 else 0)
        return ans
