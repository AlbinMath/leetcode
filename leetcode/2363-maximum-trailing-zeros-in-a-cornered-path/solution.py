class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def factor(v, p):
            c = 0
            while v % p == 0:
                v //= p
                c += 1
            return c

        t = [[factor(v, 2) for v in row] for row in grid]
        f = [[factor(v, 5) for v in row] for row in grid]

        def build(a):
            row = [[0] * n for _ in range(m)]
            col = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    row[i][j] = a[i][j] + (row[i][j - 1] if j else 0)
                    col[i][j] = a[i][j] + (col[i - 1][j] if i else 0)
            return row, col

        rt, ct = build(t)
        rf, cf = build(f)

        res = 0
        for i in range(m):
            for j in range(n):
                c2, c5 = t[i][j], f[i][j]
                # (horizontal arm, vertical arm) options for 2s
                L2 = rt[i][j]
                R2 = rt[i][n - 1] - rt[i][j] + c2
                U2 = ct[i][j]
                D2 = ct[m - 1][j] - ct[i][j] + c2
                L5 = rf[i][j]
                R5 = rf[i][n - 1] - rf[i][j] + c5
                U5 = cf[i][j]
                D5 = cf[m - 1][j] - cf[i][j] + c5

                for H2, H5 in ((L2, L5), (R2, R5)):
                    for V2, V5 in ((U2, U5), (D2, D5)):
                        res = max(res, min(H2 + V2 - c2, H5 + V5 - c5))
        return res
