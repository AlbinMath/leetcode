from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, -1

        mx = float('-inf')
        for i in range(n):
            if nums[i] < mx:
                end = i
            else:
                mx = nums[i]

        mn = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > mn:
                start = i
            else:
                mn = nums[i]

        return end - start + 1
