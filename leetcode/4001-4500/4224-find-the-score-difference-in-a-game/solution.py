class Solution:
    def scoreDifference(self, nums: list[int]) -> int:
        sign = 1
        diff = 0
        for i, x in enumerate(nums):
            if x % 2 == 1:
                sign = -sign
            if i % 6 == 5:
                sign = -sign
            diff += sign * x
        return diff
