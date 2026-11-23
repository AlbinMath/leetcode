class Solution:
    def rotateElements(self, nums: list[int], k: int) -> list[int]:
        vals = [x for x in nums if x >= 0]
        m = len(vals)
        if m == 0:
            return nums
        k %= m
        vals = vals[k:] + vals[:k]
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = vals[j]
                j += 1
        return nums
