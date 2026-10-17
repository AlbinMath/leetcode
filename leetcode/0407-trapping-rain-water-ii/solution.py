import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        seen = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i in (0, m - 1) or j in (0, n - 1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    seen[i][j] = True
        total = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not seen[x][y]:
                    seen[x][y] = True
                    g = heightMap[x][y]
                    if h > g:
                        total += h - g
                    heapq.heappush(heap, (max(g, h), x, y))
        return total
