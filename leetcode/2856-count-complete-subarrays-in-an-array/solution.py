from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        D = len(set(nums))
        cnt = defaultdict(int)
        distinct = 0
        l = 0
        ans = 0
        for x in nums:
            if cnt[x] == 0:
                distinct += 1
            cnt[x] += 1
            while distinct == D:
                y = nums[l]
                cnt[y] -= 1
                if cnt[y] == 0:
                    distinct -= 1
                l += 1
            ans += l
        return ans
