from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0
        for i in range(n):
            ya = points[i][1]
            max_y = float('-inf')
            for j in range(i + 1, n):
                yb = points[j][1]
                if max_y < yb <= ya:
                    count += 1
                    max_y = yb
        return count
