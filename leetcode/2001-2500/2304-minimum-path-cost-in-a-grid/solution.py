class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]

        for i in range(m - 1):
            nxt = [float('inf')] * n
            for k in range(n):
                costs = moveCost[grid[i][k]]
                for j in range(n):
                    nxt[j] = min(nxt[j], dp[k] + costs[j])
            dp = [nxt[j] + grid[i + 1][j] for j in range(n)]

        return min(dp)
