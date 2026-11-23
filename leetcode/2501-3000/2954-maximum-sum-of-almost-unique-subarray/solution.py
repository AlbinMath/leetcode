from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = defaultdict(int)
        total = 0
        ans = 0
        for i, x in enumerate(nums):
            total += x
            cnt[x] += 1
            if i >= k:
                y = nums[i - k]
                total -= y
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
            if i >= k - 1 and len(cnt) >= m:
                ans = max(ans, total)
        return ans
