from collections import deque
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        sub_island_count = 0

        def bfs(start_r: int, start_c: int) -> bool:
            queue = deque([(start_r, start_c)])
            grid2[start_r][start_c] = 0
            is_sub = True

            while queue:
                r, c = queue.popleft()

                # If this cell is water in grid1, this island cannot be a sub-island
                if grid1[r][c] == 0:
                    is_sub = False

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                        grid2[nr][nc] = 0  # Mark visited in grid2
                        queue.append((nr, nc))

            return is_sub

        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1:
                    if bfs(r, c):
                        sub_island_count += 1

        return sub_island_count
