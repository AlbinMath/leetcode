class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        cells = sorted(((grid[i][j], i, j) for i in range(m) for j in range(n)),
                       reverse=True)

        def relax(base):
            dp = [[INF] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        dp[0][0] = 0
                        continue
                    best = base[i][j]
                    if i > 0:
                        best = min(best, dp[i - 1][j] + grid[i][j])
                    if j > 0:
                        best = min(best, dp[i][j - 1] + grid[i][j])
                    dp[i][j] = best
            return dp

        dp = relax([[INF] * n for _ in range(m)])  # layer 0

        for _ in range(k):
            tele = [[INF] * n for _ in range(m)]
            run = INF
            idx = 0
            total = len(cells)
            while idx < total:
                v = cells[idx][0]
                j2 = idx
                # include the whole group of equal values before reading run
                while j2 < total and cells[j2][0] == v:
                    _, a, b = cells[j2]
                    run = min(run, dp[a][b])
                    j2 += 1
                for t in range(idx, j2):
                    _, a, b = cells[t]
                    tele[a][b] = run
                idx = j2

            base = [[min(dp[i][j], tele[i][j]) for j in range(n)] for i in range(m)]
            dp = relax(base)

        return dp[m - 1][n - 1]
