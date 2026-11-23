from typing import List
from collections import defaultdict

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cnt = defaultdict(int)
        for x, y in coordinates:
            for bx in (x - 1, x):
                for by in (y - 1, y):
                    if 0 <= bx < m - 1 and 0 <= by < n - 1:
                        cnt[(bx, by)] += 1

        ans = [0] * 5
        for c in cnt.values():
            ans[c] += 1
        ans[0] = (m - 1) * (n - 1) - len(cnt)
        return ans
