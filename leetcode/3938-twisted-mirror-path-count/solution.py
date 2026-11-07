from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]
        R[0][0] = 1  # start counts as one path at an empty cell

        for i in range(m):
            for j in range(n):
                r, d = R[i][j], D[i][j]
                if grid[i][j] == 0:
                    t = (r + d) % MOD
                    if i == m - 1 and j == n - 1:
                        return t
                    R[i][j + 1] = (R[i][j + 1] + t) % MOD
                    D[i + 1][j] = (D[i + 1][j] + t) % MOD
                else:
                    # entered moving right -> turned down
                    D[i + 1][j] = (D[i + 1][j] + r) % MOD
                    # entered moving down -> turned right
                    R[i][j + 1] = (R[i][j + 1] + d) % MOD
        return 0
