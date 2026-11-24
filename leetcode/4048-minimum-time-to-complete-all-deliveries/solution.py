from math import gcd
from typing import List

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        l = r1 * r2 // gcd(r1, r2)

        def ok(T: int) -> bool:
            return (T - T // r1 >= d1
                    and T - T // r2 >= d2
                    and T - T // l >= d1 + d2)

        lo, hi = 1, 4 * (d1 + d2)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
