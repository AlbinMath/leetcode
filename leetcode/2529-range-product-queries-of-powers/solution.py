class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        powers = []
        b = 0
        while n:
            if n & 1:
                powers.append(1 << b)
            n >>= 1
            b += 1

        res = []
        for l, r in queries:
            p = 1
            for i in range(l, r + 1):
                p = p * powers[i] % MOD
            res.append(p)
        return res
