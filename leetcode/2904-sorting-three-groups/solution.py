from bisect import bisect_right

class Solution:
    def minimumOperations(self, nums):
        tails = []
        for x in nums:
            pos = bisect_right(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(nums) - len(tails)
