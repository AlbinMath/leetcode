class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side(v: int, length: int) -> int:
            # sum of `length` elements descending from v-1, floored at 1
            if length < v:
                return length * (2 * v - length - 1) // 2
            return v * (v - 1) // 2 + (length - (v - 1))

        def total(v: int) -> int:
            return v + side(v, index) + side(v, n - index - 1)

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if total(mid) <= maxSum:
                lo = mid
            else:
                hi = mid - 1

        return lo
