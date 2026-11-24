from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}          # lake -> last day it rained
        dry_days = []      # sorted indices of unused dry days

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1                  # default: harmless dry
            else:
                if lake in full:
                    pos = bisect_right(dry_days, full[lake])
                    if pos == len(dry_days):
                        return []
                    day = dry_days.pop(pos)
                    ans[day] = lake
                full[lake] = i

        return ans
