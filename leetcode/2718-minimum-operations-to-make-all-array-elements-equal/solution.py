from bisect import bisect_right
from itertools import accumulate
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre = [0] + list(accumulate(nums))
        total = pre[n]

        ans = []
        for q in queries:
            k = bisect_right(nums, q)
            left = q * k - pre[k]
            right = (total - pre[k]) - q * (n - k)
            ans.append(left + right)
        return ans
