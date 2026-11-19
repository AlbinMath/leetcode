from typing import List
from itertools import combinations
import heapq

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        top = []
        for row in board:
            top.append(heapq.nlargest(3, [(v, c) for c, v in enumerate(row)]))

        best = float('-inf')
        for i, j, k in combinations(range(m), 3):
            for v1, c1 in top[i]:
                for v2, c2 in top[j]:
                    if c2 == c1:
                        continue
                    for v3, c3 in top[k]:
                        if c3 != c1 and c3 != c2:
                            s = v1 + v2 + v3
                            if s > best:
                                best = s
        return best
