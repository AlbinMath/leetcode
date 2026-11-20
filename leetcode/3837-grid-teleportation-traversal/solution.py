from collections import deque, defaultdict
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if ch.isupper():
                    portals[ch].append((i, j))

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        used = set()
        dq = deque([(0, 0, 0)])  # (r, c, d)

        while dq:
            r, c, d = dq.popleft()
            if d > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d

            ch = matrix[r][c]
            if ch.isupper() and ch not in used:
                used.add(ch)
                for pr, pc in portals[ch]:
                    if dist[pr][pc] > d:
                        dist[pr][pc] = d
                        dq.appendleft((pr, pc, d))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#' and dist[nr][nc] > d + 1:
                    dist[nr][nc] = d + 1
                    dq.append((nr, nc, d + 1))
        return -1
