from typing import List

class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        n = len(nums)
        CAP = 10**15  
        prod = [1] * n
        for i in range(n - 2, -1, -1):
            prod[i] = min(CAP, prod[i + 1] * nums[i + 1])

        left = 0
        for i in range(n):
            if left == prod[i]:
                return i
            left += nums[i]
        return -1
