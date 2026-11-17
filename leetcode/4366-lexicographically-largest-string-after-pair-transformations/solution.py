class Solution(object):
    def largestString(self, nums):
        res = []
        for x in nums:
            q = x >> 25
            r = x & ((1 << 25) - 1)
            s = 'z' * q
            s += ''.join(chr(97 + b) for b in range(24, -1, -1) if (r >> b) & 1)
            res.append(s)
        return res
