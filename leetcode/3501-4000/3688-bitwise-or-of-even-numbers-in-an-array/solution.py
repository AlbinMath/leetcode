class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        res = 0
        for x in nums:
            if x % 2 == 0:
                res |= x
        return res
