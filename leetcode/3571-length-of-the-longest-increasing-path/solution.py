from bisect import bisect_left
from typing import List

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        px, py = coordinates[k]

        def lis(points):
            points.sort(key=lambda p: (p[0], -p[1]))
            tails = []
            for _, y in points:
                pos = bisect_left(tails, y)      # strictly increasing
                if pos == len(tails):
                    tails.append(y)
                else:
                    tails[pos] = y
            return len(tails)

        left = [(x, y) for x, y in coordinates if x < px and y < py]
        right = [(x, y) for x, y in coordinates if x > px and y > py]

        return lis(left) + 1 + lis(right)
