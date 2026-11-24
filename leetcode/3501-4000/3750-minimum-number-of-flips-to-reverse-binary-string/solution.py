class Solution(object):
    def minimumFlips(self, n):
        s = bin(n)[2:]
        return sum(a != b for a, b in zip(s, s[::-1]))
