from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        for a, b, c, d in rectangles:
            area += (c - a) * (d - b)
            x1, y1 = min(x1, a), min(y1, b)
            x2, y2 = max(x2, c), max(y2, d)
            for p in ((a, b), (a, d), (c, b), (c, d)):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        if area != (x2 - x1) * (y2 - y1):
            return False
        return corners == {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
