from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i] > nums[i - 1]

        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]

        best = -1
        for i in range(n - 1):
            if inc[i] and dec[i + 1]:
                diff = abs(P[i + 1] - (P[n] - P[i + 1]))
                if best == -1 or diff < best:
                    best = diff
        return best
