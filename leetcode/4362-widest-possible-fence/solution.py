from typing import List
from collections import Counter, defaultdict

class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        cnt = Counter(planks)
        vals = sorted(cnt)
        score = defaultdict(int)

        for i, a in enumerate(vals):
            ca = cnt[a]
            score[2 * a] += ca // 2
            for j in range(i + 1, len(vals)):
                b = vals[j]
                score[a + b] += min(ca, cnt[b])

        ans = max(cnt.values())              # a single height, no pairing
        for h, s in score.items():
            ans = max(ans, s + cnt.get(h, 0))
        return ans
