from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        M = [0] * (n + 1)
        for f in range(1, n + 1):
            M[f] = sum(cnt[f::f])          # harmonic sieve, O(n log n)
        pmin = min(p for _, p in items)

        groups = defaultdict(int)
        for f, p in items:
            d = M[f] - 1
            if d > 0:
                groups[p] += d

        R = budget
        total = 0
        for p in sorted(groups):
            if p > 2 * pmin:
                break
            t = min(groups[p], R // p)
            total += 2 * t
            R -= t * p
            if t < groups[p]:
                break
        total += R // pmin
        return total
