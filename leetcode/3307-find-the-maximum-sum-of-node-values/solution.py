class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        total = 0
        flips = 0
        min_abs = float('inf')
        for x in nums:
            gain = (x ^ k) - x
            if gain > 0:
                total += x ^ k
                flips += 1
            else:
                total += x
            if abs(gain) < min_abs:
                min_abs = abs(gain)
        if flips % 2:
            total -= min_abs
        return total
