from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] + (nums[i - 1] % 2 == nums[i] % 2)

        return [pre[r] - pre[l] == 0 for l, r in queries]
