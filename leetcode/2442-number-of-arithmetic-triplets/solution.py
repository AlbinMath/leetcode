class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        seen = set(nums)
        return sum(1 for x in nums if (x + diff) in seen and (x + 2 * diff) in seen)
