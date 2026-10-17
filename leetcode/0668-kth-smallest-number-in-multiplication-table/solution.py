class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) >= k:
                r = mid
            else:
                l = mid + 1
        return l
