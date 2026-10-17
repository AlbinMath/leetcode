import sys
from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        sys.setrecursionlimit(10000)

        @lru_cache(maxsize=None)
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[l + 1] == boxes[l]:
                l += 1
                k += 1
            best = (k + 1) ** 2 + dp(l + 1, r, 0)
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    best = max(best, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))
            return best

        return dp(0, len(boxes) - 1, 0)
