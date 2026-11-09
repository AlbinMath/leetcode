from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        for p in range(n):
            total = heights[p]
            cur = heights[p]
            for i in range(p - 1, -1, -1):
                cur = min(cur, heights[i])
                total += cur
            cur = heights[p]
            for i in range(p + 1, n):
                cur = min(cur, heights[i])
                total += cur
            best = max(best, total)
        return best
