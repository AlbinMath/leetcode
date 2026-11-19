from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int]) -> int:
        last1 = last2 = -1
        ans = float('inf')
        for i, v in enumerate(nums):
            if v == 1:
                last1 = i
                if last2 != -1:
                    ans = min(ans, i - last2)
            elif v == 2:
                last2 = i
                if last1 != -1:
                    ans = min(ans, i - last1)
        return -1 if ans == float('inf') else ans
