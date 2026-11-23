from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:  # make the pair loop run over the smaller dimension
            matrix = [list(r) for r in zip(*matrix)]
            m, n = n, m
        best = float('-inf')
        for top in range(m):
            cols = [0] * n
            for bottom in range(top, m):
                row = matrix[bottom]
                for c in range(n):
                    cols[c] += row[c]
                prefixes = [0]
                p = 0
                for v in cols:
                    p += v
                    i = bisect_left(prefixes, p - k)
                    if i < len(prefixes):
                        s = p - prefixes[i]
                        if s > best:
                            best = s
                            if best == k:
                                return k
                    insort(prefixes, p)
        return best
