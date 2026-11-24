class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(r: int) -> int:
            return 2 * r * (r + 1) * (2 * r + 1)

        lo, hi = 1, 100_000
        while lo < hi:
            mid = (lo + hi) // 2
            if apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo
