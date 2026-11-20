from collections import deque
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start

        seen = [[False] * n for _ in range(m)]
        seen[sr][sc] = True
        layer = [(sr, sc)]
        ans = []

        while layer and len(ans) < k:
            items = []
            nxt = []
            for r, c in layer:
                p = grid[r][c]
                if low <= p <= high:
                    items.append((p, r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and not seen[nr][nc]:
                        seen[nr][nc] = True
                        nxt.append((nr, nc))
            items.sort()
            for p, r, c in items:
                ans.append([r, c])
            layer = nxt

        return ans[:k]
