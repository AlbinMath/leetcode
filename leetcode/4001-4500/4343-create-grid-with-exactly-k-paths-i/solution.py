from typing import List

class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        # Single row or column: exactly one path if all free
        if m == 1 or n == 1:
            if k == 1:
                return ["." * n for _ in range(m)]
            return []

        # Row-based construction: k <= n
        if k <= n:
            g = [['#'] * n for _ in range(m)]
            for j in range(n):
                g[0][j] = '.'
            for i in range(m):
                g[i][n - 1] = '.'
            for j in range(n - k, n):
                g[1][j] = '.'
            return ["".join(r) for r in g]

        # Column-based construction: k <= m
        if k <= m:
            g = [['#'] * n for _ in range(m)]
            for i in range(m):
                g[i][0] = '.'
            for j in range(n):
                g[m - 1][j] = '.'
            for i in range(m - k, m):
                g[i][1] = '.'
            return ["".join(r) for r in g]

        # Remaining: k > n and k > m  -> only 3x3 with k = 4 works
        if m == 3 and n == 3 and k == 4:
            return ["..#", "...", "#.."]
        return []
