from bisect import bisect_left
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[1])
        ends = [e[1] for e in events]

        pref = []
        cur = 0
        for _, _, v in events:
            cur = max(cur, v)
            pref.append(cur)

        ans = 0
        for s, e, v in events:
            best = v
            idx = bisect_left(ends, s) - 1
            if idx >= 0:
                best += pref[idx]
            ans = max(ans, best)

        return ans
