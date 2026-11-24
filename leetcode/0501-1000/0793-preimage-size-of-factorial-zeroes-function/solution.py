class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x: int) -> int:
            zeros = 0
            while x:
                x //= 5
                zeros += x
            return zeros

        lo, hi = 0, 5 * (k + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if f(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return 5 if f(lo) == k else 0
