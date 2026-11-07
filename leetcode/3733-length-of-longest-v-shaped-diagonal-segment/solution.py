from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        def order(dx, dy):
            # visit cells so that (i+dx, j+dy) is processed before (i, j)
            rows = range(n - 1, -1, -1) if dx == 1 else range(n)
            cols = range(m - 1, -1, -1) if dy == 1 else range(m)
            return rows, cols

        straight = [[0] * (n * m) for _ in range(4)]
        turn = [[0] * (n * m) for _ in range(4)]

        for d in range(4):
            dx, dy = dirs[d]
            rows, cols = order(dx, dy)
            S = straight[d]
            for i in rows:
                for j in cols:
                    need = 2 if grid[i][j] != 2 else 0
                    best = 1
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = 1 + S[x * m + y]
                    S[i * m + j] = best

        for d in range(4):
            dx, dy = dirs[d]
            nd = (d + 1) % 4
            ndx, ndy = dirs[nd]
            rows, cols = order(dx, dy)
            T = turn[d]
            SN = straight[nd]
            for i in rows:
                for j in cols:
                    need = 2 if grid[i][j] != 2 else 0
                    best = 1
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = 1 + T[x * m + y]
                    x, y = i + ndx, j + ndy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = max(best, 1 + SN[x * m + y])
                    T[i * m + j] = best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, turn[d][i * m + j])
        return ans
