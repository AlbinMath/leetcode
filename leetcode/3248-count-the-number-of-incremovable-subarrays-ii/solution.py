from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        p = 1
        while p < n and nums[p - 1] < nums[p]:
            p += 1
        if p == n:
            return n * (n + 1) // 2

        s = n - 1
        while s > 0 and nums[s - 1] < nums[s]:
            s -= 1

        ans = 0
        t = s
        for i in range(p + 1):          # keep nums[0..i-1]
            t = max(t, i + 1)           # removed segment [i, t-1] non-empty
            if i > 0:
                while t < n and nums[t] <= nums[i - 1]:
                    t += 1
            ans += n - t + 1            # t in [t, n]
        return ans
