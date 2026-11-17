from collections import Counter

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        res = 0
        for v, c in Counter(nums).items():
            if c == 2:
                res ^= v
        return res
