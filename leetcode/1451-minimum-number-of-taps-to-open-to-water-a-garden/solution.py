from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach = list(range(n + 1))  # reach[s] = farthest end of an interval starting at s
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            reach[left] = max(reach[left], right)

        count = 0
        cur_end = 0
        farthest = 0
        for i in range(n + 1):
            if i > cur_end:
                return -1
            farthest = max(farthest, reach[i])
            if i == cur_end and cur_end < n:
                if farthest <= cur_end:
                    return -1
                cur_end = farthest
                count += 1
        return count
