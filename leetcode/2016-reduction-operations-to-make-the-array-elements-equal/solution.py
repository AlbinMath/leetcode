class Solution:
    def reductionOperations(self, nums):
        nums.sort()
        return sum(i for i in range(1, len(nums)) if nums[i] != nums[i-1]) * 0 + sum(len(nums)-i for i in range(1, len(nums)) if nums[i] != nums[i-1])
