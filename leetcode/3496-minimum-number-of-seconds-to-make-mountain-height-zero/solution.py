from math import isqrt
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        H = mountainHeight

        def can(t: int) -> bool:
            total = 0
            for w in workerTimes:
                q = t // w
                total += (isqrt(8 * q + 1) - 1) // 2
                if total >= H:
                    return True
            return False

        lo, hi = 1, min(workerTimes) * H * (H + 1) // 2
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
