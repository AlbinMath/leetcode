from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        H = round(hour * 100)

        if H <= 100 * (n - 1):
            return -1

        def ok(v: int) -> bool:
            t = 0
            for d in dist[:-1]:
                t += (d + v - 1) // v          # whole hours
            t *= 100
            t += (100 * dist[-1] + v - 1) // v  # last ride, in hundredths, rounded up
            return t <= H

        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
