from collections import deque

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        q, dist = deque([(0,0)]), [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0

        while q:
            r, c = q.popleft()
            for i, (dr, dc) in enumerate(d, 1):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    w = dist[r][c] + (grid[r][c] != i)
                    if w < dist[x][y]:
                        dist[x][y] = w
                        if grid[r][c] == i:
                            q.appendleft((x,y))
                        else:
                            q.append((x,y))

        return dist[m-1][n-1]
