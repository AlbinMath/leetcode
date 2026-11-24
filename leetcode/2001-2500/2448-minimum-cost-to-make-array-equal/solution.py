class Solution:
    def minCost(self, nums, cost):
        def f(x):
            return sum(c * abs(a - x) for a, c in zip(nums, cost))

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if f(mid) <= f(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        return f(lo)
