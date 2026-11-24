from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a // gcd(a, b) * b
        ac = a // gcd(a, c) * c
        bc = b // gcd(b, c) * c
        abc = ab // gcd(ab, c) * c

        def count(x):
            return (x // a + x // b + x // c
                    - x // ab - x // ac - x // bc
                    + x // abc)

        lo, hi = 1, 2 * 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
