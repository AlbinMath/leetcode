from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, max(quantities)

        while lo < hi:
            mid = (lo + hi) // 2
            stores = sum((q + mid - 1) // mid for q in quantities)

            if stores <= n:
                hi = mid
            else:
                lo = mid + 1

        return lo
