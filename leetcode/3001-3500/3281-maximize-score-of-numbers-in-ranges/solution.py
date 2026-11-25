from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)

        def ok(g: int) -> bool:
            cur = start[0]
            for i in range(1, n):
                cur = max(start[i], cur + g)
                if cur > start[i] + d:
                    return False
            return True

        lo, hi = 0, (start[-1] + d - start[0]) // (n - 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
