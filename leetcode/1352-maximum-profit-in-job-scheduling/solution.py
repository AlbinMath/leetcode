from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends = []
        best = [0]

        for e, s, p in jobs:
            idx = bisect_right(ends, s)       # jobs already processed that end <= s
            take = best[idx] + p
            ends.append(e)
            best.append(max(best[-1], take))

        return best[-1]
