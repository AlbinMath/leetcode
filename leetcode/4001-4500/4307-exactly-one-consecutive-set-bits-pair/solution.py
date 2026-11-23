class Solution(object):
    def consecutiveSetBits(self, n):
        return bin(n & (n >> 1)).count('1') == 1
