from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        pre = 1
        while pre < n and nums[pre - 1] < nums[pre]:
            pre += 1

        suf = n - 1
        while suf > 0 and nums[suf - 1] < nums[suf]:
            suf -= 1

        ans = 0
        for i in range(n):
            if i > pre:
                break
            for j in range(i, n):
                if j + 1 < suf:
                    continue
                if i == 0 or j == n - 1 or nums[i - 1] < nums[j + 1]:
                    ans += 1
        return ans
