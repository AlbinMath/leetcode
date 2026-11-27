from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = 0
        ans = 0
        for x in nums:
            if x > 0:
                pos, neg = pos + 1, (neg + 1 if neg > 0 else 0)
            elif x < 0:
                pos, neg = (neg + 1 if neg > 0 else 0), pos + 1
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans
