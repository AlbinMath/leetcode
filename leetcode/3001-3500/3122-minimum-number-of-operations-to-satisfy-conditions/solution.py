class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = [[0] * 10 for _ in range(n)]
        for row in grid:
            for j, v in enumerate(row):
                count[j][v] += 1

        dp = [m - count[0][v] for v in range(10)]

        for j in range(1, n):
            nxt = [0] * 10
            for v in range(10):
                best = min(dp[u] for u in range(10) if u != v)
                nxt[v] = best + m - count[j][v]
            dp = nxt

        return min(dp)
