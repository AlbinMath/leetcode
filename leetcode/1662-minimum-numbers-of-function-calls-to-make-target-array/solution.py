from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx == 0:
            return 0
        ones = sum(x.bit_count() for x in nums)
        return ones + mx.bit_length() - 1
