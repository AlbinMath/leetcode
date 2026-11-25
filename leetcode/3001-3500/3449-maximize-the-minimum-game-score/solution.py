from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def check(x: int) -> bool:
            rem = m
            pre = 0
            for i in range(n):
                k = -(-x // points[i]) - pre      # ceil(x / p) - pre
                if i == n - 1 and k <= 0:
                    break
                if k < 1:
                    k = 1
                rem -= 2 * k - 1
                if rem < 0:
                    return False
                pre = k - 1
            return True

        lo, hi = 0, 10**15
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
