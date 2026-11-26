from typing import List

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        c = [0] * n
        for i in range(1, n - 1):
            c[i] = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])

        if n % 2 == 1:
            return sum(c[i] for i in range(1, n - 1, 2))

        k = (n - 2) // 2
        # pre[t] = c[1] + c[3] + ... + c[2t-1]
        pre = [0] * (k + 1)
        for t in range(1, k + 1):
            pre[t] = pre[t - 1] + c[2 * t - 1]
        # suf[t] = c[2t+2] + c[2t+4] + ... + c[n-2]
        suf = [0] * (k + 2)
        for t in range(k - 1, -1, -1):
            suf[t] = suf[t + 1] + c[2 * t + 2]

        return min(pre[t] + suf[t] for t in range(k + 1))
