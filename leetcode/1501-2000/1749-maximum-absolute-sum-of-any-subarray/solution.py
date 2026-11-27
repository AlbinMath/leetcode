class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prefix_sum = 0
        max_prefix = 0
        min_prefix = 0
        
        for x in nums:
            prefix_sum += x
            if prefix_sum > max_prefix:
                max_prefix = prefix_sum
            elif prefix_sum < min_prefix:
                min_prefix = prefix_sum
                
        return max_prefix - min_prefix
