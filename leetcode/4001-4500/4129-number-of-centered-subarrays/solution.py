from typing import List

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            total = 0
            for j in range(i, n):
                total += nums[j]
                seen.add(nums[j])
                if total in seen:
                    ans += 1
        return ans
