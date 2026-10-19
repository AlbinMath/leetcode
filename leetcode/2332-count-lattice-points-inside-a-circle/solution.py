from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        pts = set()
        for cx, cy, r in circles:
            r2 = r * r
            for x in range(cx - r, cx + r + 1):
                dx = x - cx
                for y in range(cy - r, cy + r + 1):
                    dy = y - cy
                    if dx * dx + dy * dy <= r2:
                        pts.add((x, y))
        return len(pts)
