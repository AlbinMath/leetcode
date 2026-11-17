class Solution(object):
    def maxBalancedSubarray(self, nums):
        first = {(0, 0): 0}
        x = 0
        bal = 0
        best = 0
        for i, v in enumerate(nums, 1):
            x ^= v
            bal += 1 if v & 1 else -1
            key = (x, bal)
            if key in first:
                length = i - first[key]
                if length > best:
                    best = length
            else:
                first[key] = i
        return best
