from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        first = {}
        s = 0
        ans = 0
        for i, h in enumerate(hours):
            s += 1 if h > 8 else -1
            if s > 0:
                ans = i + 1
            else:
                if s not in first:
                    first[s] = i
                if s - 1 in first:
                    ans = max(ans, i - first[s - 1])
        return ans
