from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(sources):
            dist = [[INF] * n for _ in range(m)]
            q = deque()
            for r, c in sources:
                dist[r][c] = 0
                q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and dist[nr][nc] == INF:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
            return dist

        fire = bfs([(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1])
        me = bfs([(0, 0)])

        if me[m - 1][n - 1] == INF:
            return -1
        if fire[m - 1][n - 1] == INF:
            return INF  # fire can never reach the safehouse or anything on your path

        d = fire[m - 1][n - 1] - me[m - 1][n - 1]
        if d < 0:
            return -1

        for x, y in ((m - 2, n - 1), (m - 1, n - 2)):
            if me[x][y] != INF and fire[x][y] - me[x][y] > d:
                return d
        return d - 1
