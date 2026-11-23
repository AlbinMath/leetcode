class Solution(object):
    def minOperations(self, queries):
        res = 0
        for l, r in queries:
            total = 0
            k = 1
            lo = 1
            while lo <= r:
                hi = lo * 4 - 1
                a = max(l, lo)
                b = min(r, hi)
                if a <= b:
                    total += (b - a + 1) * k
                lo *= 4
                k += 1
            res += (total + 1) // 2
        return res
