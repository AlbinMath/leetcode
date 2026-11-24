from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        def can(k: int) -> bool:
            diff = [0] * (n + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r + 1] -= v
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        if not can(q):
            return -1

        lo, hi = 0, q
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
