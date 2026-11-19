from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        run = 1
        ans = 0
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                run += 1
            else:
                run = 1
            if run >= k:
                ans += 1
        return ans
