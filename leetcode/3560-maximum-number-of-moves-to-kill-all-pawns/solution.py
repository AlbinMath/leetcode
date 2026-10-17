from collections import deque
from functools import lru_cache

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        p = [(kx, ky)] + [tuple(x) for x in positions]
        n = len(positions)
        d = [[0] * (n + 1) for _ in range(n + 1)]
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        for i, (x, y) in enumerate(p):
            dist = [[-1] * 50 for _ in range(50)]
            dist[x][y] = 0
            q = deque([(x, y)])
            while q:
                a, b = q.popleft()
                for dx, dy in dirs:
                    u, v = a + dx, b + dy
                    if 0 <= u < 50 and 0 <= v < 50 and dist[u][v] == -1:
                        dist[u][v] = dist[a][b] + 1
                        q.append((u, v))
            for j, (a, b) in enumerate(p):
                d[i][j] = dist[a][b]

        @lru_cache(None)
        def dp(mask, cur):
            if mask == (1 << n) - 1:
                return 0
            vals = [d[cur][i + 1] + dp(mask | (1 << i), i + 1)
                    for i in range(n) if not (mask >> i) & 1]
            return max(vals) if mask.bit_count() % 2 == 0 else min(vals)

        return dp(0, 0)
