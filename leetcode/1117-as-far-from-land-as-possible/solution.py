from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque((r, c) for r in range(n) for c in range(n) if grid[r][c] == 1)
        if not q or len(q) == n * n:
            return -1

        ans = 0
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    ans = max(ans, grid[nr][nc] - 1)
                    q.append((nr, nc))
        return ans
