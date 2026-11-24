from math import isqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo, hi = 1, min(ranks) * cars * cars

        while lo < hi:
            mid = (lo + hi) // 2
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                hi = mid
            else:
                lo = mid + 1

        return lo
