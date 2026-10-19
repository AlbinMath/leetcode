from typing import List

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        parent = list(range(n + 2))
        A, B = n, n + 1          # A = left+top edges, B = bottom+right edges
        X, Y = xCorner, yCorner

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        def clamp(v, lo, hi):
            return max(lo, min(v, hi))

        # a circle covering either corner blocks everything
        for x, y, r in circles:
            if x * x + y * y <= r * r or (x - X) ** 2 + (y - Y) ** 2 <= r * r:
                return False

        # connect circles to the edge segments they actually touch
        for i, (x, y, r) in enumerate(circles):
            r2 = r * r
            if x * x + (y - clamp(y, 0, Y)) ** 2 <= r2:          # left edge
                union(i, A)
            if (y - Y) ** 2 + (x - clamp(x, 0, X)) ** 2 <= r2:   # top edge
                union(i, A)
            if y * y + (x - clamp(x, 0, X)) ** 2 <= r2:          # bottom edge
                union(i, B)
            if (x - X) ** 2 + (y - clamp(y, 0, Y)) ** 2 <= r2:   # right edge
                union(i, B)

        # connect overlapping circles whose contact point lies inside the rectangle
        for i in range(n):
            x1, y1, r1 = circles[i]
            for j in range(i + 1, n):
                x2, y2, r2 = circles[j]
                s = r1 + r2
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= s * s:
                    px = x1 * r2 + x2 * r1          # contact x, scaled by s
                    py = y1 * r2 + y2 * r1
                    if 0 <= px <= X * s and 0 <= py <= Y * s:
                        union(i, j)

        return find(A) != find(B)
