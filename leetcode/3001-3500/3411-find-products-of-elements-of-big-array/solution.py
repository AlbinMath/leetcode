class Solution(object):
    def findProductsOfElements(self, queries):
        def bit_counts(x):
            # (total set bits in 1..x, total sum of bit positions in 1..x)
            total = 0
            exps = 0
            n = x + 1
            for b in range(60):
                full = (n >> (b + 1)) << b
                rem = n & ((1 << (b + 1)) - 1)
                c = full + max(0, rem - (1 << b))
                total += c
                exps += b * c
            return total, exps

        def S(N):
            # sum of exponents of the first N elements of big_nums
            if N <= 0:
                return 0
            lo, hi = 0, 1 << 51
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if bit_counts(mid)[0] <= N:
                    lo = mid
                else:
                    hi = mid - 1
            x = lo
            c, e = bit_counts(x)
            r = N - c
            y = x + 1
            b = 0
            while r > 0:
                if (y >> b) & 1:
                    e += b
                    r -= 1
                b += 1
            return e

        res = []
        for f, t, m in queries:
            res.append(pow(2, S(t + 1) - S(f), m))
        return res
