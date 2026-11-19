from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        cnt = 0
        l = 0
        ans = 0
        for x in nums:
            if x == M:
                cnt += 1
            while cnt >= k:
                if nums[l] == M:
                    cnt -= 1
                l += 1
            ans += l
        return ans
