from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        S = sum(nums)
        cnt = Counter(nums)
        ans = float('-inf')

        for s in cnt:
            o = S - 2 * s
            if o in cnt and (o != s or cnt[s] >= 2):
                ans = max(ans, o)

        return ans
