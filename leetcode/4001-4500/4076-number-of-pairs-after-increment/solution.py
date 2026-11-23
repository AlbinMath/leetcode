from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, queries):
        n = len(nums2)
        B = 300
        nb = (n + B - 1) // B

        a = nums2[:]                      # base values (without block lazy)
        lz = [0] * nb
        cnt = [dict() for _ in range(nb)]
        for i, v in enumerate(a):
            d = cnt[i // B]
            d[v] = d.get(v, 0) + 1

        mult = list(Counter(nums1).items())   # (value, multiplicity)

        def partial(b, lo, hi, val):          # inclusive range inside block b
            d = cnt[b]
            for i in range(lo, hi + 1):
                old = a[i]
                d[old] -= 1
                new = old + val
                a[i] = new
                d[new] = d.get(new, 0) + 1

        ans = []
        for q in queries:
            if q[0] == 1:
                _, x, y, val = q
                bx, by = x // B, y // B
                if bx == by:
                    partial(bx, x, y, val)
                else:
                    partial(bx, x, (bx + 1) * B - 1, val)
                    partial(by, by * B, y, val)
                    for b in range(bx + 1, by):
                        lz[b] += val
            else:
                tot = q[1]
                res = 0
                for av, m in mult:
                    t = tot - av
                    s = 0
                    for b in range(nb):
                        s += cnt[b].get(t - lz[b], 0)
                    res += m * s
                ans.append(res)
        return ans
