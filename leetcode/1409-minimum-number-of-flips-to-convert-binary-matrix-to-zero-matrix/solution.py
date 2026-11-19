from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        start = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    start |= 1 << (r * n + c)

        flips = []
        for r in range(m):
            for c in range(n):
                mask = 1 << (r * n + c)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask |= 1 << (nr * n + nc)
                flips.append(mask)

        if start == 0:
            return 0

        seen = {start}
        q = deque([(start, 0)])
        while q:
            state, d = q.popleft()
            for f in flips:
                nxt = state ^ f
                if nxt == 0:
                    return d + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))

        return -1
