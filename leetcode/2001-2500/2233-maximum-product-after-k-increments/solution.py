import heapq
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0] + 1)
        ans = 1
        for x in nums:
            ans = ans * x % MOD
        return ans
