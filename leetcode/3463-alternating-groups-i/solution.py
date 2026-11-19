from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            a = colors[(i - 1) % n]
            b = colors[i]
            c = colors[(i + 1) % n]
            if a != b and b != c:
                ans += 1
        return ans
