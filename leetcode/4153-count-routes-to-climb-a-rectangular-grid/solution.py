from math import isqrt

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])
        w = isqrt(d * d - 1)

        def window(pref, c, rad):
            lo, hi = max(0, c - rad), min(m - 1, c + rad)
            return pref[hi + 1] - pref[lo]

        def prefix(arr):
            p = [0] * (m + 1)
            for i, v in enumerate(arr):
                p[i + 1] = (p[i] + v) % MOD
            return p

        # bottom row
        A = [1 if grid[n - 1][c] == '.' else 0 for c in range(m)]
        pa = prefix(A)
        B = [0] * m
        for c in range(m):
            if grid[n - 1][c] == '.':
                B[c] = (window(pa, c, d) - A[c]) % MOD

        for r in range(n - 2, -1, -1):
            tot = [(A[c] + B[c]) % MOD for c in range(m)]
            pt = prefix(tot)
            newA = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    newA[c] = window(pt, c, w)
            pa = prefix(newA)
            newB = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    newB[c] = (window(pa, c, d) - newA[c]) % MOD
            A, B = newA, newB

        return (sum(A) + sum(B)) % MOD
