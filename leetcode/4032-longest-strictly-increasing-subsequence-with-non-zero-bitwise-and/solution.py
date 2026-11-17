from bisect import bisect_left

class Solution(object):
    def longestSubsequence(self, nums):
        best = 0
        for b in range(30):
            tails = []
            for x in nums:
                if (x >> b) & 1:
                    i = bisect_left(tails, x)
                    if i == len(tails):
                        tails.append(x)
                    else:
                        tails[i] = x
            if len(tails) > best:
                best = len(tails)
        return best
