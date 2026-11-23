class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False

        # Power of 4 must have exactly one set bit
        if n & (n - 1):
            return False

        # The set bit must be in an even position
        return (n & 0x55555555) != 0
