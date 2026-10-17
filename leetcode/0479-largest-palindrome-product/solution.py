class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        hi = 10 ** n - 1
        lo = 10 ** (n - 1)
        for h in range(hi, lo - 1, -1):
            s = str(h)
            p = int(s + s[::-1])
            x = hi
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1
        return -1
