from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        best = 0
        for i in range(n):
            a1, b1 = bottomLeft[i]
            c1, d1 = topRight[i]
            for j in range(i + 1, n):
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]
                w = min(c1, c2) - max(a1, a2)
                h = min(d1, d2) - max(b1, b2)
                if w > 0 and h > 0:
                    best = max(best, min(w, h))
        return best * best
