from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        border = []

        stack = [(row, col)]
        visited[row][col] = True
        while stack:
            r, c = stack.pop()
            is_border = False
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != orig:
                    is_border = True
                elif not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
            if is_border:
                border.append((r, c))

        for r, c in border:
            grid[r][c] = color
        return grid
