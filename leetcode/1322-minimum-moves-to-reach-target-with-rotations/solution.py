from collections import deque
from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[[False] * 2 for _ in range(n)] for _ in range(n)]
        visited[0][0][0] = True
        q = deque([(0, 0, 0, 0)])  # (r, c, orientation, moves)

        while q:
            r, c, o, d = q.popleft()
            if r == n - 1 and c == n - 2 and o == 0:
                return d

            nxt = []
            if o == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    nxt.append((r, c + 1, 0))
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r + 1, c, 0))
                    nxt.append((r, c, 1))
            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    nxt.append((r + 1, c, 1))
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r, c + 1, 1))
                    nxt.append((r, c, 0))

            for nr, nc, no in nxt:
                if not visited[nr][nc][no]:
                    visited[nr][nc][no] = True
                    q.append((nr, nc, no, d + 1))
        return -1
