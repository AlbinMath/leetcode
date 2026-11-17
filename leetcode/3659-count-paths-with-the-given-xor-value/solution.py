class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0] * 16 for _ in range(n)]
        for i in range(m):
            cur = [[0] * 16 for _ in range(n)]
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    cur[0][g] = 1
                    continue
                up = prev[j] if i > 0 else None
                left = cur[j - 1] if j > 0 else None
                row = cur[j]
                for x in range(16):
                    t = x ^ g
                    v = 0
                    if up is not None:
                        v += up[t]
                    if left is not None:
                        v += left[t]
                    row[x] = v % MOD
            prev = cur
        return prev[n - 1][k]
