from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0

        gap = max(1, (hi - lo) // (n - 1))
        size = (hi - lo) // gap + 1
        bmin = [None] * size
        bmax = [None] * size

        for v in nums:
            b = (v - lo) // gap
            if bmin[b] is None or v < bmin[b]:
                bmin[b] = v
            if bmax[b] is None or v > bmax[b]:
                bmax[b] = v

        ans = 0
        prev_max = lo
        for b in range(size):
            if bmin[b] is None:
                continue
            ans = max(ans, bmin[b] - prev_max)
            prev_max = bmax[b]
        return ans
