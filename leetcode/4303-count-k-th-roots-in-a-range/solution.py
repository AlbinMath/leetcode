class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if mid ** k <= n:
                    lo = mid
                else:
                    hi = mid - 1
            return lo + 1          # x in [0, lo]

        return count(r) - count(l - 1)
