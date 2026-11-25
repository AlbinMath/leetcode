from typing import List

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def ok(k: int) -> bool:
            return sum((x + k - 1) // k for x in nums) <= k * k

        lo, hi = 1, max(max(nums), 317)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
