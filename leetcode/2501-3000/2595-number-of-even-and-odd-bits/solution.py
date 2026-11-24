class Solution(object):
    def evenOddBit(self, n):
        res = [0, 0]
        i = 0
        while n:
            if n & 1:
                res[i & 1] += 1
            n >>= 1
            i += 1
        return res
