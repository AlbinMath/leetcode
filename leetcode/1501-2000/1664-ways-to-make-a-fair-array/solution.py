class Solution:
    def waysToMakeFair(self, nums):
        even = sum(nums[::2])
        odd = sum(nums[1::2])
        le = lo = ans = 0
        for i, x in enumerate(nums):
            if i % 2:
                odd -= x
            else:
                even -= x
            if le + odd == lo + even:
                ans += 1
            if i % 2:
                lo += x
            else:
                le += x
        return ans
