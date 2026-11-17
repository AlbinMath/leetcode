class Solution(object):
    def minEnd(self, n, x):
        k = n - 1
        res = x
        bit = 1
        while k:
            if not (x & bit):      # a zero position of x
                if k & 1:
                    res |= bit
                k >>= 1
            bit <<= 1
        return res
