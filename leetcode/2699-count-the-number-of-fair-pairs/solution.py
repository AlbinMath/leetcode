class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            lo = bisect_left(nums, lower - x, i + 1)
            hi = bisect_right(nums, upper - x, i + 1)
            ans += hi - lo
        return ans
