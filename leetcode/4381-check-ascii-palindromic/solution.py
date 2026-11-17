class Solution(object):
    def isPalindromic(self, s):
        b = ''.join(format(ord(c), '08b') for c in s)
        return b == b[::-1]
