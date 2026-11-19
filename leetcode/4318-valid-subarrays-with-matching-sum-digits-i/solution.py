from typing import List

class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total % 10 == x and str(total)[0] == chr(48 + x):
                    ans += 1
        return ans
