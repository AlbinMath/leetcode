from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        # odd palindromes: d1[i] = number of palindromes centered at i
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # even palindromes: d2[i] = number centered between i-1 and i
        d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l, r = i - k, i + k - 1

        best = 0
        for i in range(n):
            k = d1[i]
            best = max(best, pre[i + k] - pre[i - k + 1])
            k = d2[i]
            if k:
                best = max(best, pre[i + k] - pre[i - k])
        return best
