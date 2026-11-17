class Solution(object):
    def findMaximumNumber(self, k, x):
        def price(num):
            n = num + 1
            total = 0
            p = x
            while p <= 61:
                b = p - 1
                full = (n >> (b + 1)) << b
                rem = n & ((1 << (b + 1)) - 1)
                total += full + max(0, rem - (1 << b))
                p += x
            return total

        lo, hi = 0, 1 << 60
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if price(mid) <= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
