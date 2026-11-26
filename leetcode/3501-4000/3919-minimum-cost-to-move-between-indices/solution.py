from typing import List

class Solution:
    def minCost(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        def closest(i):
            if i == 0:
                return 1
            if i == n - 1:
                return n - 2
            return i - 1 if nums[i] - nums[i - 1] <= nums[i + 1] - nums[i] else i + 1

        PR = [0] * n
        for i in range(n - 1):
            step = 1 if closest(i) == i + 1 else nums[i + 1] - nums[i]
            PR[i + 1] = PR[i] + step

        PL = [0] * n
        for i in range(1, n):
            step = 1 if closest(i) == i - 1 else nums[i] - nums[i - 1]
            PL[i] = PL[i - 1] + step

        ans = []
        for l, r in queries:
            if l <= r:
                ans.append(PR[r] - PR[l])
            else:
                ans.append(PL[l] - PL[r])
        return ans
