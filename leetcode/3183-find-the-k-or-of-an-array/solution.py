class Solution(object):
    def findKOr(self, nums, k):
        res = 0
        for b in range(31):
            c = sum((x >> b) & 1 for x in nums)
            if c >= k:
                res |= 1 << b
        return res
