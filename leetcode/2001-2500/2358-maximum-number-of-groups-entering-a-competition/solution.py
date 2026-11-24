class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) // 2 <= n:
                lo = mid
            else:
                hi = mid - 1
        return lo
