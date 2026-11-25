class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0] * k for _ in range(n)]  # dp for the previous row

        for i in range(m):
            cur = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j] % k
                if i == 0 and j == 0:
                    cur[0][v] = 1
                    continue
                up = prev[j]
                left = cur[j - 1] if j > 0 else None
                for r in range(k):
                    total = up[r]
                    if left is not None:
                        total += left[r]
                    if total:
                        cur[j][(r + v) % k] = total % MOD
            prev = cur

        return prev[n - 1][0]
