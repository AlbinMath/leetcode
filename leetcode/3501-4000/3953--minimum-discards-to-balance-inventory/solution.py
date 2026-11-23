from typing import List
from collections import defaultdict

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        kept = [False] * len(arrivals)
        ans = 0
        for i, t in enumerate(arrivals):
            j = i - w
            if j >= 0 and kept[j]:
                cnt[arrivals[j]] -= 1
            if cnt[t] >= m:
                ans += 1
            else:
                cnt[t] += 1
                kept[i] = True
        return ans
