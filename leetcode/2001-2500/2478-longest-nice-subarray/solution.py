class Solution(object):
    def longestNiceSubarray(self, nums):
        mask = 0
        l = 0
        best = 0
        for r, x in enumerate(nums):
            while mask & x:
                mask ^= nums[l]
                l += 1
            mask |= x
            if r - l + 1 > best:
                best = r - l + 1
        return best
