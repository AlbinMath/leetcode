class Solution:
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)
        nums = sorted(nums)
        t = nums[len(nums) - k]
        return sum(1 for x in nums if x < t)
