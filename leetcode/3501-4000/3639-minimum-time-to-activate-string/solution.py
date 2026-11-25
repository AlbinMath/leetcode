from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if total < k:
            return -1

        def ok(t: int) -> bool:
            star = [False] * n
            for i in range(t + 1):
                star[order[i]] = True
            bad = 0
            run = 0
            for i in range(n):
                if star[i]:
                    bad += run * (run + 1) // 2
                    run = 0
                else:
                    run += 1
            bad += run * (run + 1) // 2
            return total - bad >= k

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
