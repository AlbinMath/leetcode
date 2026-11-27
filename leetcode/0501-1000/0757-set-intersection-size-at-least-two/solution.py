from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1  # two largest chosen points, a < b
        ans = 0
        for s, e in intervals:
            if s > b:
                # neither point is inside
                ans += 2
                a, b = e - 1, e
            elif s > a:
                # only b is inside
                ans += 1
                if b == e:
                    a, b = e - 1, e
                else:
                    a, b = b, e
        return ans
