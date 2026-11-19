from typing import List

class Solution:
    def countIntersectingIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            a, b = intervals[i]
            for j in range(i + 1, n):
                c, d = intervals[j]
                if a <= d and c <= b:
                    ans += 1
        return ans
