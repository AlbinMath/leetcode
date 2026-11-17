from bisect import bisect_left

class Solution(object):
    def minOperations(self, nums):
        pals = []
        for v in range(1, 8193):
            b = bin(v)[2:]
            if b == b[::-1]:
                pals.append(v)

        res = []
        for x in nums:
            i = bisect_left(pals, x)
            best = abs(pals[i] - x)           # smallest palindrome >= x
            if i > 0:
                best = min(best, x - pals[i - 1])  # largest palindrome < x
            res.append(best)
        return res
