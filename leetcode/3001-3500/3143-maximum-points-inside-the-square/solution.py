from typing import List

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        INF = float('inf')
        first = [INF] * 26
        second = [INF] * 26

        ds = []
        for (x, y), ch in zip(points, s):
            d = max(abs(x), abs(y))
            ds.append(d)
            k = ord(ch) - 97
            if d < first[k]:
                second[k] = first[k]
                first[k] = d
            elif d < second[k]:
                second[k] = d

        limit = min(second) - 1
        return sum(1 for d in ds if d <= limit)
