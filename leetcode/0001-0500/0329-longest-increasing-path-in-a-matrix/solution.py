from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cells = sorted(((matrix[i][j], i, j) for i in range(m) for j in range(n)),
                       reverse=True)
        L = [[1] * n for _ in range(m)]
        best = 1
        for v, i, j in cells:
            cur = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > v:
                    if L[x][y] + 1 > cur:
                        cur = L[x][y] + 1
            L[i][j] = cur
            if cur > best:
                best = cur
        return best
