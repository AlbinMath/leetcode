from typing import List
from itertools import combinations

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        n = len(matrix[0])
        rows = []
        for row in matrix:
            m = 0
            for j, v in enumerate(row):
                if v:
                    m |= 1 << j
            rows.append(m)

        best = 0
        for cols in combinations(range(n), numSelect):
            sel = 0
            for c in cols:
                sel |= 1 << c
            covered = sum(1 for m in rows if m & sel == m)
            best = max(best, covered)
        return best
