class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        q, r = divmod(n, 3)
        if r == 0:
            return 3 ** q
        if r == 1:
            return 3 ** (q - 1) * 4
        return 3 ** q * 2
