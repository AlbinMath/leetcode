from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calc(v: int) -> int:
            return sum(x if x < v else v for x in arr)

        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if calc(mid) >= target:
                hi = mid
            else:
                lo = mid + 1

        # lo is the smallest value with calc(lo) >= target (or max(arr))
        if lo > 0 and abs(calc(lo - 1) - target) <= abs(calc(lo) - target):
            return lo - 1
        return lo
