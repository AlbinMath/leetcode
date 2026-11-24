from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m = len(nums2)

        def count(x: int) -> int:
            total = 0
            for a in nums1:
                if a > 0:
                    # b <= floor(x / a)
                    total += bisect_right(nums2, x // a)
                elif a < 0:
                    # b >= ceil(x / a)
                    c = -(-x // a)
                    total += m - bisect_left(nums2, c)
                else:
                    if x >= 0:
                        total += m
            return total

        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
