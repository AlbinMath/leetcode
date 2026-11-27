from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        small, large = nums[:half], nums[half:]
        res = [0] * n
        res[0::2] = small
        res[1::2] = large
        return res
