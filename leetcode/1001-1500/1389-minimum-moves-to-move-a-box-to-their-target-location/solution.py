from collections import deque
from typing import List

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sr, sc = i, j
                elif grid[i][j] == 'B':
                    br, bc = i, j
                elif grid[i][j] == 'T':
                    tr, tc = i, j

        def free(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] != '#'

        def can_reach(src, dst, box):
            # can the player walk from src to dst without stepping on the box?
            if src == dst:
                return True
            seen = {src}
            q = deque([src])
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) == box or (nr, nc) in seen or not free(nr, nc):
                        continue
                    if (nr, nc) == dst:
                        return True
                    seen.add((nr, nc))
                    q.append((nr, nc))
            return False

        start = (br, bc, sr, sc)
        visited = {start}
        q = deque([(br, bc, sr, sc, 0)])
        while q:
            r, c, pr, pc, d = q.popleft()
            if (r, c) == (tr, tc):
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc          # box destination
                stand = (r - dr, c - dc)         # where player must stand
                if not free(nr, nc) or not free(*stand):
                    continue
                # after the push the player will be at (r, c)
                if (nr, nc, r, c) in visited:
                    continue
                if can_reach((pr, pc), stand, (r, c)):
                    visited.add((nr, nc, r, c))
                    q.append((nr, nc, r, c, d + 1))
        return -1
