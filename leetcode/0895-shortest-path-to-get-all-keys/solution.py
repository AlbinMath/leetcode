from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        sr = sc = 0
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == '@':
                    sr, sc = r, c
                elif 'a' <= ch <= 'f':
                    total += 1

        full = (1 << total) - 1
        seen = {(sr, sc, 0)}
        q = deque([(sr, sc, 0, 0)])

        while q:
            r, c, keys, d = q.popleft()
            if keys == full:
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                ch = grid[nr][nc]
                if ch == '#':
                    continue
                nk = keys
                if 'A' <= ch <= 'F':
                    if not (keys >> (ord(ch) - 65)) & 1:
                        continue
                elif 'a' <= ch <= 'f':
                    nk |= 1 << (ord(ch) - 97)
                if (nr, nc, nk) not in seen:
                    seen.add((nr, nc, nk))
                    q.append((nr, nc, nk, d + 1))

        return -1
