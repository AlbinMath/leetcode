class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            grid[r][c] = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # 1. Flood-fill from left and right boundaries
        for r in range(m):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][n - 1] == 1:
                dfs(r, n - 1)

        # 2. Flood-fill from top and bottom boundaries
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[m - 1][c] == 1:
                dfs(m - 1, c)

        # 3. Count remaining enclosed land cells
        return sum(grid[r][c] == 1 for r in range(m) for c in range(n))
