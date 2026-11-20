from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3:
            return m + n - 2

        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        visited[0][0][0] = True
        q = deque([(0, 0, 0, 0)])  # (r, c, obstacles used, steps)

        while q:
            r, c, used, d = q.popleft()
            if r == m - 1 and c == n - 1:
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nu = used + grid[nr][nc]
                    if nu <= k and not visited[nr][nc][nu]:
                        visited[nr][nc][nu] = True
                        q.append((nr, nc, nu, d + 1))
        return -1
