from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            gold = grid[r][c]
            grid[r][c] = 0  # mark visited
            best = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    best = max(best, dfs(nr, nc))
            grid[r][c] = gold  # restore
            return gold + best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        return ans
