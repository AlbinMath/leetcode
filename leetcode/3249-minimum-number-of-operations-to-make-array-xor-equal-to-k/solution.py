class Solution(object):
    def minOperations(self, nums, k):
        x = k
        for v in nums:
            x ^= v
        return bin(x).count('1')
