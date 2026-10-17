from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def pieces(S):
            cnt, cur = 1, 0
            for v in nums:
                if cur + v > S:
                    cnt += 1
                    cur = v
                else:
                    cur += v
            return cnt

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if pieces(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
