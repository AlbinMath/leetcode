class Solution(object):
    def hasTrailingZeros(self, nums):
        return sum(1 for x in nums if x % 2 == 0) >= 2
