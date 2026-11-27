from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        cnt = Counter(changed)
        res = []
        for x in sorted(cnt):
            if cnt[x] == 0:
                continue
            if x == 0:
                if cnt[0] % 2:
                    return []
                res.extend([0] * (cnt[0] // 2))
                cnt[0] = 0
                continue
            if cnt[2 * x] < cnt[x]:
                return []
            res.extend([x] * cnt[x])
            cnt[2 * x] -= cnt[x]
            cnt[x] = 0
        return res
