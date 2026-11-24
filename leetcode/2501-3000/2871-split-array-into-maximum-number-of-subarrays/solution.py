class Solution(object):
    def maxSubarrays(self, nums):
        total = nums[0]
        for x in nums:
            total &= x
        if total != 0:
            return 1

        count = 0
        cur = -1  # all bits set
        for x in nums:
            cur &= x
            if cur == 0:
                count += 1
                cur = -1
        return count
