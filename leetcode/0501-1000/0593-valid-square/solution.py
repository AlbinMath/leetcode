from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pts = [p1, p2, p3, p4]
        d = []
        for i in range(4):
            for j in range(i + 1, 4):
                dx = pts[i][0] - pts[j][0]
                dy = pts[i][1] - pts[j][1]
                d.append(dx * dx + dy * dy)
        d.sort()
        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5]
