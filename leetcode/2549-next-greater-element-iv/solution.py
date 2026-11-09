from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        s1, s2 = [], []

        for j, x in enumerate(nums):
            while s2 and nums[s2[-1]] < x:
                ans[s2.pop()] = x

            tmp = []
            while s1 and nums[s1[-1]] < x:
                tmp.append(s1.pop())
            s2.extend(reversed(tmp))

            s1.append(j)

        return ans
