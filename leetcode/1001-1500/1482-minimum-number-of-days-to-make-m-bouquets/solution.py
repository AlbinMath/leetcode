from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make(d: int) -> bool:
            bouquets = run = 0
            for b in bloomDay:
                if b <= d:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
