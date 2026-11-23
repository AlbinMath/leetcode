from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [0] * (n + 1)
        best = 0
        for x in nums1:
            for j in range(n, 0, -1):
                if x == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    if dp[j] > best:
                        best = dp[j]
                else:
                    dp[j] = 0
        return best
