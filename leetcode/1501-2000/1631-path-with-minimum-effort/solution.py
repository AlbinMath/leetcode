import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        d = [[float('inf')]*n for _ in range(m)]
        d[0][0] = 0
        q = [(0, 0, 0)]

        while q:
            e, r, c = heapq.heappop(q)
            if (r, c) == (m-1, n-1):
                return e
            if e > d[r][c]:
                continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    ne = max(e, abs(heights[r][c]-heights[x][y]))
                    if ne < d[x][y]:
                        d[x][y] = ne
                        heapq.heappush(q, (ne, x, y))
        return 0
