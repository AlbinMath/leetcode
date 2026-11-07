from typing import List
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[mat[i][j]].append((i, j))

        row = [0] * m
        col = [0] * n
        ans = 0

        for v in sorted(groups, reverse=True):
            cells = groups[v]
            vals = [1 + max(row[i], col[j]) for i, j in cells]
            for (i, j), d in zip(cells, vals):
                if d > row[i]:
                    row[i] = d
                if d > col[j]:
                    col[j] = d
                if d > ans:
                    ans = d
        return ans
