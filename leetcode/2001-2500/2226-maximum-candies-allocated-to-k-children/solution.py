from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        lo, hi = 1, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if sum(p // mid for p in candies) >= k:
                lo = mid
            else:
                hi = mid - 1

        return lo
