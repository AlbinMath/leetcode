import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        while q:
            t, r, c = heapq.heappop(q)
            if (r, c) == (n-1, n-1):
                return t
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < n and 0 <= y < n and (x,y) not in seen:
                    seen.add((x,y))
                    heapq.heappush(q, (max(t, grid[x][y]), x, y))
