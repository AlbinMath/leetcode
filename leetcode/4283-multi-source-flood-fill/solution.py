from typing import List

class Solution:
    def colorGrid(self, n: int, m: int, sources: List[List[int]]) -> List[List[int]]:
        grid = [[0] * m for _ in range(n)]
        frontier = []
        for r, c, col in sources:
            grid[r][c] = col
            frontier.append((r, c))

        while frontier:
            new = {}  # (r, c) -> max color arriving this step
            for r, c in frontier:
                col = grid[r][c]
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        if new.get((nr, nc), 0) < col:
                            new[(nr, nc)] = col
            for (r, c), col in new.items():
                grid[r][c] = col
            frontier = list(new.keys())
        return grid
