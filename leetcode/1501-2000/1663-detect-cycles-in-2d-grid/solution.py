import sys
from typing import List

# Increase recursion depth for deep grid traversals (up to 500 * 500 = 250,000)
sys.setrecursionlimit(300000)

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int, parent_r: int, parent_c: int) -> bool:
            visited[r][c] = True
            val = grid[r][c]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == val:
                    # Skip the cell we just came from
                    if nr == parent_r and nc == parent_c:
                        continue
                    # Back-edge found -> cycle exists
                    if visited[nr][nc]:
                        return True
                    if dfs(nr, nc, r, c):
                        return True

            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False
