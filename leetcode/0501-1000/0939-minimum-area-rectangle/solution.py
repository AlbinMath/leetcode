from collections import defaultdict
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cols = defaultdict(list)
        for x, y in points:
            cols[x].append(y)

        last = {}                      # (y1, y2) -> most recent x containing both
        best = float('inf')
        for x in sorted(cols):
            ys = sorted(cols[x])
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    pair = (ys[i], ys[j])
                    if pair in last:
                        best = min(best, (x - last[pair]) * (ys[j] - ys[i]))
                    last[pair] = x
        return 0 if best == float('inf') else best
