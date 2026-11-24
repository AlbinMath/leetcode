from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        d = [[float('inf')]*n for _ in range(m)]
        d[0][0] = 0
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    w = d[r][c] + grid[x][y]
                    if w < d[x][y]:
                        d[x][y] = w
                        if grid[x][y]:
                            q.append((x,y))
                        else:
                            q.appendleft((x,y))

        return d[m-1][n-1]
